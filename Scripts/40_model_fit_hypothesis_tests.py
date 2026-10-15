"""
40_model_fit_hypothesis_tests.py
Supervisor feedback item 2: model fit statistics and explicit hypothesis-test
interpretation for the annual association models, plus Granger causality tests.

Models (annual, 2000-2023):
  B  : primary spec, GDP growth rates (n = 23)
  C  : gravity-ratio robustness spec (n = 24)
  A2 : parsimonious spec, no GDP controls (n = 24)

For each model we report:
  N, k, R2, adj. R2, F-statistic (classical) and HAC Wald F with p-values,
  log-likelihood, AIC, BIC, RMSE (= standard error of regression), Durbin-Watson,
  Breusch-Godfrey LM (lag 2), Breusch-Pagan, Jarque-Bera, Ramsey RESET.

Hypothesis tests (H1-H3) use HAC t-statistics with small-sample t(df_resid)
p-values (the normal-approximation p used in earlier tables is also kept),
and are reported with H0, H1, test statistic, p-value
(one-sided where the hypothesis is directional), and the decision at 5% and 10%.

Granger causality (annual): bivariate tests in both directions between the
trade balance and (i) strategic mineral exports, (ii) BRI financing intensity,
with lag 1 and lag 2, using first differences where series are not clearly
stationary, plus Toda-Yamamoto (1995) augmented-lag Wald tests on levels.

Outputs:
  Outputs/generated_tables/model_fit_statistics.csv
  Outputs/generated_tables/hypothesis_tests_formal.csv
  Outputs/generated_tables/granger_annual.csv
"""

import warnings
warnings.filterwarnings("ignore")

from pathlib import Path
import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats
from statsmodels.stats.diagnostic import (acorr_breusch_godfrey, het_breuschpagan,
                                          linear_reset)
from statsmodels.stats.stattools import durbin_watson, jarque_bera
from statsmodels.tsa.stattools import grangercausalitytests, adfuller

ROOT = Path(__file__).parent.parent
PANEL = ROOT / "Collected_Raw_Data" / "clean_panel_annual.csv"
TABLES = ROOT / "Outputs" / "generated_tables"
TABLES.mkdir(parents=True, exist_ok=True)
NW_BW = 3

df = pd.read_csv(PANEL)
df = df[df["year"].between(2000, 2023)].sort_values("year").reset_index(drop=True)
df["TB"] = df["trade_balance_usd"] / 1e9
df["MIN"] = df["minerals_narrow"] / 1e9
df["BRENT"] = df["brent_annual_mean"]
df["KZT"] = df["kzt_usd"]
df["POST"] = df["post_bri_2013"].astype(int)
df["POST_x_MIN"] = df["POST"] * df["MIN"]
df["log_kz_gdp"] = np.log(df["kz_gdp"])
df["log_cn_gdp"] = np.log(df["cn_gdp"])
df["dlg_kz_gdp"] = df["log_kz_gdp"].diff()
df["dlg_cn_gdp"] = df["log_cn_gdp"].diff()
df["gravity_ratio"] = df["log_cn_gdp"] - df["log_kz_gdp"]
df["BRI_INT"] = df["bri_intensity"]

SPECS = {
    "B (primary): growth-rate controls": ["MIN", "POST", "POST_x_MIN", "BRENT", "KZT",
                                          "dlg_kz_gdp", "dlg_cn_gdp"],
    "C (robustness): gravity ratio": ["MIN", "POST", "POST_x_MIN", "BRENT", "KZT",
                                      "gravity_ratio"],
    "A2 (parsimonious): no GDP controls": ["MIN", "POST", "POST_x_MIN", "BRENT", "KZT"],
}


def fit(cols, data):
    sub = data.dropna(subset=cols + ["TB"])
    y, X = sub["TB"], sm.add_constant(sub[cols])
    ols = sm.OLS(y, X).fit()
    hac = sm.OLS(y, X).fit(cov_type="HAC", cov_kwds={"maxlags": NW_BW})
    return sub, ols, hac


fit_rows, hyp_rows = [], []
for name, cols in SPECS.items():
    sub, ols, hac = fit(cols, df)
    k = len(cols)
    # HAC-robust joint significance (all slopes = 0)
    R = np.zeros((k, k + 1)); R[:, 1:] = np.eye(k)
    wald = hac.f_test(R)
    bg = acorr_breusch_godfrey(ols, nlags=2)
    bp = het_breuschpagan(ols.resid, ols.model.exog)
    jb = jarque_bera(ols.resid)
    try:
        reset = linear_reset(ols, power=2, use_f=True)
        reset_F, reset_p = float(reset.fvalue), float(reset.pvalue)
    except Exception:
        reset_F, reset_p = np.nan, np.nan
    fit_rows.append({
        "Model": name, "N": int(ols.nobs), "k_regressors": k,
        "R2": ols.rsquared, "Adj_R2": ols.rsquared_adj,
        "F_classical": ols.fvalue, "F_classical_p": ols.f_pvalue,
        "F_HAC_Wald": float(np.squeeze(wald.fvalue)), "F_HAC_Wald_p": float(wald.pvalue),
        "LogLik": ols.llf, "AIC": ols.aic, "BIC": ols.bic,
        "RMSE_SER": np.sqrt(ols.scale),
        "Mean_TB": sub["TB"].mean(),
        "Durbin_Watson": durbin_watson(ols.resid),
        "BG_LM_lag2": bg[0], "BG_p": bg[1],
        "BP_LM": bp[0], "BP_p": bp[1],
        "JB": jb[0], "JB_p": jb[1],
        "RESET_F": reset_F, "RESET_p": reset_p,
    })

    # Formal hypothesis tests (HAC t-tests)
    def ttest(var, alt):
        b, se = hac.params[var], hac.bse[var]
        t = b / se
        p_norm = float(hac.pvalues[var])
        df_resid = ols.df_resid
        p2 = 2 * (1 - stats.t.cdf(abs(t), df_resid))
        if alt == "less":
            p1 = stats.t.cdf(t, df_resid)
        else:
            p1 = 1 - stats.t.cdf(t, df_resid)
        return b, se, t, p2, p1, p_norm

    tests = [
        ("H1", "POST", "less", "beta_PostBRI >= 0", "beta_PostBRI < 0",
         "Post-BRI level shift in the trade balance (conditional on minerals and controls)"),
        ("H2", "MIN", "greater", "beta_Minerals <= 0", "beta_Minerals > 0",
         "Mineral exports positively associated with the trade balance in the pre-BRI period"),
        ("H3", "POST_x_MIN", "less", "beta_Interaction >= 0", "beta_Interaction < 0",
         "Mineral-balance association weaker after BRI"),
    ]
    for hid, var, alt, h0, h1, desc in tests:
        b, se, t, p2, p1, p_norm = ttest(var, alt)
        sign_ok = (b < 0) if alt == "less" else (b > 0)
        if p1 < 0.05:
            dec = "Reject H0 at 5%"
        elif p1 < 0.10:
            dec = "Reject H0 at 10% only"
        else:
            dec = "Fail to reject H0"
        hyp_rows.append({
            "Model": name, "Hypothesis": hid, "Description": desc, "Variable": var,
            "H0": h0, "H1": h1, "Coef": b, "HAC_SE": se, "t_stat": t,
            "df_resid": int(ols.df_resid),
            "p_two_sided_normal": p_norm,
            "p_two_sided": p2, "p_one_sided": p1,
            "Predicted_sign_observed": "yes" if sign_ok else "no",
            "Decision": dec,
        })

    # Joint test: does the post-BRI period change the mineral relationship at all?
    jt = hac.f_test("POST = 0, POST_x_MIN = 0")
    hyp_rows.append({
        "Model": name, "Hypothesis": "Joint", "Description":
        "Post-BRI level shift and interaction jointly zero (no post-BRI change at all)",
        "Variable": "POST, POST_x_MIN", "H0": "beta_PostBRI = beta_Interaction = 0",
        "H1": "at least one non-zero", "Coef": np.nan, "HAC_SE": np.nan,
        "t_stat": float(np.squeeze(jt.fvalue)), "df_resid": int(ols.df_resid),
        "p_two_sided": float(jt.pvalue), "p_one_sided": np.nan,
        "Predicted_sign_observed": "", "Decision":
        "Reject H0 at 5%" if jt.pvalue < 0.05 else ("Reject H0 at 10% only" if jt.pvalue < 0.10 else "Fail to reject H0"),
    })
    # Post-BRI mineral slope (beta_MIN + beta_interaction)
    st = hac.t_test("MIN + POST_x_MIN = 0")
    hyp_rows.append({
        "Model": name, "Hypothesis": "Post-BRI slope", "Description":
        "Mineral-balance slope in the post-BRI period (beta_Minerals + beta_Interaction)",
        "Variable": "MIN + POST_x_MIN", "H0": "slope = 0", "H1": "slope != 0",
        "Coef": float(np.squeeze(st.effect)), "HAC_SE": float(np.squeeze(st.sd)),
        "t_stat": float(np.squeeze(st.tvalue)), "df_resid": int(ols.df_resid),
        "p_two_sided": float(st.pvalue), "p_one_sided": np.nan,
        "Predicted_sign_observed": "", "Decision":
        "Reject H0 at 5%" if st.pvalue < 0.05 else ("Reject H0 at 10% only" if st.pvalue < 0.10 else "Fail to reject H0"),
    })

fit_df = pd.DataFrame(fit_rows)
hyp_df = pd.DataFrame(hyp_rows)
fit_df.round(4).to_csv(TABLES / "model_fit_statistics.csv", index=False)
hyp_df.round(4).to_csv(TABLES / "hypothesis_tests_formal.csv", index=False)
print(fit_df.round(3).T.to_string())
print(hyp_df[["Model", "Hypothesis", "Coef", "HAC_SE", "t_stat", "p_two_sided",
              "p_one_sided", "Decision"]].round(3).to_string())

# ── Granger causality, annual ────────────────────────────────────────────────
def adf_p(s):
    return adfuller(s.dropna(), autolag="AIC", maxlag=2)[1]


def toda_yamamoto(data, y, x, p, dmax=1):
    """Toda-Yamamoto: VAR(p+dmax) in levels, Wald test on first p lags of x in y-eq."""
    d = data[[y, x]].dropna().reset_index(drop=True)
    L = p + dmax
    rows = []
    for t in range(L, len(d)):
        row = {"y": d.loc[t, y]}
        for l in range(1, L + 1):
            row[f"y_l{l}"] = d.loc[t - l, y]
            row[f"x_l{l}"] = d.loc[t - l, x]
        rows.append(row)
    R = pd.DataFrame(rows)
    X = sm.add_constant(R.drop(columns="y"))
    m = sm.OLS(R["y"], X).fit()
    hyp = ", ".join([f"x_l{l} = 0" for l in range(1, p + 1)])
    w = m.wald_test(hyp, scalar=True, use_f=False)
    return float(w.statistic), float(w.pvalue), int(m.nobs)


gc_rows = []
pairs = [("TB", "MIN"), ("MIN", "TB"), ("TB", "BRI_INT"), ("BRI_INT", "TB")]
for y, x in pairs:
    base = df[["year", y, x]].dropna()
    for transform in ["first difference", "Toda-Yamamoto levels"]:
        for p in [1, 2]:
            if transform == "first difference":
                d = base[[y, x]].diff().dropna()
                res = grangercausalitytests(d[[y, x]], maxlag=[p])
                F, pv, df_d, df_n = res[p][0]["ssr_ftest"]
                chi, pchi, _ = res[p][0]["ssr_chi2test"]
                n_used = int(df_d + 2 * p + 1)
                gc_rows.append({"Frequency": "annual", "Null": f"{x} does not Granger-cause {y}",
                                "Transform": transform, "Lags": p, "N_used": n_used,
                                "Statistic": "F", "Stat_value": F, "p_value": pv})
            else:
                W, pv, n_used = toda_yamamoto(base, y, x, p, dmax=1)
                gc_rows.append({"Frequency": "annual", "Null": f"{x} does not Granger-cause {y}",
                                "Transform": transform + " (dmax=1)", "Lags": p, "N_used": n_used,
                                "Statistic": "Wald chi2", "Stat_value": W, "p_value": pv})
gc = pd.DataFrame(gc_rows)
gc["Decision_5pct"] = np.where(gc["p_value"] < 0.05, "Reject H0", "Fail to reject H0")
gc.round(4).to_csv(TABLES / "granger_annual.csv", index=False)
print(gc.round(3).to_string())
print("ADF p (levels): TB", round(adf_p(df["TB"]), 3), "MIN", round(adf_p(df["MIN"]), 3),
      "BRI_INT", round(adf_p(df["BRI_INT"]), 3))
print("ADF p (diffs): TB", round(adf_p(df["TB"].diff()), 3), "MIN", round(adf_p(df["MIN"].diff()), 3))
