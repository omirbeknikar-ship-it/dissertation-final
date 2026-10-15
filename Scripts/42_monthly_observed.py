"""
42_monthly_observed.py
Supervisor feedback item 1 (preferred implementation): re-estimate the
association models on OBSERVED monthly Kazakhstan-China trade data, and run
Granger causality tests at monthly frequency (item 2).

Data
----
  Collected_Raw_Data/raw_downloads/comtrade_monthly_kaz_reporter.csv
  Collected_Raw_Data/raw_downloads/comtrade_monthly_chn_reporter.csv  (thousand USD)
      UN Comtrade monthly HS data, public preview API
      (comtradeapi.un.org/public/v1/preview/C/M/HS), retrieved 2026-10-15.
      Reporter 398 (Kazakhstan) with partner 156 (China), and the mirror
      (reporter 156, partner 398). Monthly data begin in January 2010.
  Collected_Raw_Data/raw_downloads/nbk_kzt_rates_monthly.csv
      National Bank of Kazakhstan official KZT/USD and KZT/CNY rates
      (nationalbank.kz/rss/get_rates.cfm), sampled every 3 days, averaged by month.
  Collected_Raw_Data/raw_downloads/pink_sheet_real.xlsx
      World Bank Pink Sheet monthly Brent and copper prices.

Variables (USD bn per month)
  TB   = Kazakhstan exports to China - imports from China (Kazakhstan-reported)
  TB_adj = TB with 2020-2022 imports replaced by China-reported exports to
         Kazakhstan x the 2016-2019 KZ/China reporting ratio
  MIN  = Kazakhstan-reported exports to China of HS 26 + HS 28
         (same chapter definition as minerals_narrow in Script 01)
  MIN4 = HS 2610 + 2612 + 2844 + 7403 (chromium ores, uranium ores,
         uranium compounds, refined copper): product-level robustness
  POST = 1 from 2014M01 (robustness: from 2013M10, after the Astana speech)

Primary sample: 2010M01-2019M12 (120 months; 48 pre-BRI, 72 post-BRI), one
consistent source. Extended samples to 2023M12 are robustness checks because
Kazakhstan-reported imports from China break in 2020-2022 (mirror check).

Outputs
  Collected_Raw_Data/processed/monthly_panel.csv
  Outputs/generated_tables/monthly_results.csv
  Outputs/generated_tables/monthly_fit_statistics.csv
  Outputs/generated_tables/monthly_hypothesis_tests.csv
  Outputs/generated_tables/monthly_unit_root.csv
  Outputs/generated_tables/granger_monthly.csv
  Outputs/generated_tables/monthly_mirror_check.csv
  Outputs/generated_figures/fig_monthly_trade_balance.png
"""

import warnings
warnings.filterwarnings("ignore")

from pathlib import Path
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats
from statsmodels.stats.diagnostic import acorr_breusch_godfrey, het_breuschpagan, linear_reset
from statsmodels.stats.stattools import durbin_watson, jarque_bera
from statsmodels.tsa.stattools import adfuller, kpss, grangercausalitytests
from statsmodels.tsa.api import VAR

ROOT = Path(__file__).parent.parent
RAW = ROOT / "Collected_Raw_Data" / "raw_downloads"
PROC = ROOT / "Collected_Raw_Data" / "processed"
TABLES = ROOT / "Outputs" / "generated_tables"
FIGS = ROOT / "Outputs" / "generated_figures"
HAC_LAGS = 12

# ── Load and build monthly panel ────────────────────────────────────────────
# Values in the two Comtrade files are thousands of USD; converted to USD bn.
kz = pd.read_csv(RAW / "comtrade_monthly_kaz_reporter.csv", dtype={"period": str})
cn = pd.read_csv(RAW / "comtrade_monthly_chn_reporter.csv", dtype={"period": str})
months = pd.period_range("2010-01", "2023-12", freq="M")
m = pd.DataFrame({"period": [p.strftime("%Y%m") for p in months]})
m = m.merge(kz, on="period", how="left").merge(
    cn.rename(columns={c: f"CN_{c}" for c in cn.columns if c != "period"}), on="period", how="left")
num = [c for c in m.columns if c != "period"]
m[num] = m[num] / 1e6
# Chapter rows absent from a reported month are true zeros (Comtrade omits zero rows)
for c in ["X26", "X28", "X27", "X2610", "X2612", "X2844", "X7403"]:
    m.loc[m["XTOTAL"].notna() & m[c].isna(), c] = 0.0
for c in ["CN_M26", "CN_M28"]:
    m.loc[m["CN_MTOTAL"].notna() & m[c].isna(), c] = 0.0
m["X"] = m["XTOTAL"]                      # KZ-reported exports to China
m["M"] = m["MTOTAL"]                      # KZ-reported imports from China
m["MIN"] = m["X26"] + m["X28"]            # HS 26 + 28 (as minerals_narrow in Script 01)
m["MIN4"] = m[["X2610", "X2612", "X2844", "X7403"]].sum(axis=1, min_count=1)
m["OIL27"] = m["X27"]
m["M_mirror"] = m["CN_XTOTAL"]            # China-reported exports to KZ
m["X_mirror"] = m["CN_MTOTAL"]            # China-reported imports from KZ
m["date"] = pd.PeriodIndex(m["period"].str[:4] + "-" + m["period"].str[4:], freq="M")
m["year"] = m["date"].dt.year
m["TB"] = m["X"] - m["M"]

# Import-series break: KZ-reported imports from China fall far below China's
# reported exports to Kazakhstan in 2020-2022 (see monthly_mirror_check.csv).
# Mirror-adjusted imports for 2020-2022 = China-reported exports x the average
# KZ/China ratio observed in 2016-2019 (both sources complete in those years).
ov = m[m["year"].between(2016, 2019)]
MIRROR_RATIO = ov["M"].sum() / ov["M_mirror"].sum()
m["M_adj"] = m["M"]
brk = m["year"].between(2020, 2022)
m.loc[brk, "M_adj"] = m.loc[brk, "M_mirror"] * MIRROR_RATIO
m["TB_adj"] = m["X"] - m["M_adj"]
print("KZ/China import ratio 2016-2019:", round(MIRROR_RATIO, 3))

fx = pd.read_csv(RAW / "nbk_kzt_rates_monthly.csv", dtype={"period": str})
m = m.merge(fx[["period", "KZT", "KZT_CNY"]], on="period", how="left")

pink = pd.read_excel(RAW / "pink_sheet_real.xlsx", sheet_name="Monthly Prices", header=None)
hdr = pink.iloc[4].tolist()
pm = pink.iloc[6:, [0, hdr.index("Crude oil, Brent"), hdr.index("Copper")]].copy()
pm.columns = ["m", "BRENT", "COPPER"]
pm = pm[pm["m"].astype(str).str.match(r"^\d{4}M\d{2}$")]
pm["period"] = pm["m"].str.replace("M", "")
pm[["BRENT", "COPPER"]] = pm[["BRENT", "COPPER"]].apply(pd.to_numeric, errors="coerce")
m = m.merge(pm[["period", "BRENT", "COPPER"]], on="period", how="left")

m["month"] = m["date"].dt.month
m["POST"] = (m["date"] >= pd.Period("2014-01", "M")).astype(int)
m["POST_alt"] = (m["date"] >= pd.Period("2013-10", "M")).astype(int)
m["POST_x_MIN"] = m["POST"] * m["MIN"]
m["POST_x_MIN4"] = m["POST"] * m["MIN4"]
m["POSTalt_x_MIN"] = m["POST_alt"] * m["MIN"]
m["TREND"] = np.arange(len(m)) / 12.0
m["TB_l1"] = m["TB"].shift(1)
m["TB_l2"] = m["TB"].shift(2)
for k in range(2, 13):
    m[f"m{k:02d}"] = (m["month"] == k).astype(int)
MONTH_FE = [f"m{k:02d}" for k in range(2, 13)]

m.drop(columns=["date"]).to_csv(PROC / "monthly_panel.csv", index=False)
# PRIMARY monthly sample: 2010M01-2019M12, a single consistent source
# (Kazakhstan-reported flows, before the 2020-2022 import-reporting break).
main = m[(m["year"] >= 2010) & (m["year"] <= 2019)].copy()
full = m.copy()                                   # 2010M01-2023M12, as reported
full_adj = m.copy(); full_adj["TB"] = full_adj["TB_adj"]   # mirror-adjusted 2020-2022
print("Primary monthly sample:", main["period"].min(), "-", main["period"].max(),
      "| months:", len(main), "| pre-BRI:", int((main["POST"] == 0).sum()),
      "| post-BRI:", int((main["POST"] == 1).sum()))

# ── Mirror / annual consistency check ───────────────────────────────────────
ann_panel = pd.read_csv(ROOT / "Collected_Raw_Data" / "clean_panel_annual.csv")
agg = m.groupby("year")[["X", "M", "TB", "X_mirror", "M_mirror", "M_adj", "TB_adj", "MIN"]].sum(min_count=12)
agg = agg.join(ann_panel.set_index("year")[["exports_kazakhstan_to_china_usd",
                                            "imports_kazakhstan_from_china_usd",
                                            "trade_balance_usd"]] / 1e9)
agg["months_reported"] = m.groupby("year")["X"].count()
agg["months_mirror"] = m.groupby("year")["M_mirror"].count()
agg["ratio_CNexports_to_KZimports"] = agg["M_mirror"] / agg["M"]
agg.round(3).to_csv(TABLES / "monthly_mirror_check.csv")
print(agg.round(2).to_string())


# ── Estimation helpers ──────────────────────────────────────────────────────
def estimate(data, cols, label, sample_label, maxlags=HAC_LAGS, y="TB"):
    sub = data.dropna(subset=cols + [y])
    X = sm.add_constant(sub[cols])
    ols = sm.OLS(sub[y], X).fit()
    hac = sm.OLS(sub[y], X).fit(cov_type="HAC", cov_kwds={"maxlags": maxlags}, use_t=True)
    return sub, ols, hac


def fitstats(ols, hac, cols, label, sample_label):
    k = len(cols)
    R = np.zeros((k, k + 1)); R[:, 1:] = np.eye(k)
    w = hac.f_test(R)
    bg = acorr_breusch_godfrey(ols, nlags=12)
    bp = het_breuschpagan(ols.resid, ols.model.exog)
    jb = jarque_bera(ols.resid)
    try:
        rs = linear_reset(ols, power=2, use_f=True); rF, rp = float(rs.fvalue), float(rs.pvalue)
    except Exception:
        rF, rp = np.nan, np.nan
    return {"Model": label, "Sample": sample_label, "N": int(ols.nobs), "k_regressors": k,
            "R2": ols.rsquared, "Adj_R2": ols.rsquared_adj,
            "F_classical": ols.fvalue, "F_classical_p": ols.f_pvalue,
            "F_HAC_Wald": float(np.squeeze(w.fvalue)), "F_HAC_Wald_p": float(w.pvalue),
            "LogLik": ols.llf, "AIC": ols.aic, "BIC": ols.bic, "RMSE_SER": np.sqrt(ols.scale),
            "Durbin_Watson": durbin_watson(ols.resid), "BG_LM_lag12": bg[0], "BG_p": bg[1],
            "BP_LM": bp[0], "BP_p": bp[1], "JB": jb[0], "JB_p": jb[1],
            "RESET_F": rF, "RESET_p": rp}


def coefs(hac, label, sample_label, keys):
    out = {"Model": label, "Sample": sample_label, "N": int(hac.nobs)}
    for kk in keys:
        if kk in hac.params:
            out[f"{kk}_coef"] = hac.params[kk]
            out[f"{kk}_SE"] = hac.bse[kk]
            out[f"{kk}_p"] = hac.pvalues[kk]
    return out


BASE = ["MIN", "POST", "POST_x_MIN", "BRENT", "KZT"]
P = "2010M01-2019M12"
SPECS = [
    ("M1: parsimonious + month FE", BASE + MONTH_FE, main, P),
    ("M2: M1 + linear trend", BASE + MONTH_FE + ["TREND"], main, P),
    ("M3: M1 + copper price", BASE + MONTH_FE + ["COPPER"], main, P),
    ("M4: M1 + bilateral oil/energy exports (HS 27)", BASE + MONTH_FE + ["OIL27"], main, P),
    ("M5: M1 + two lags of TB (dynamic)", BASE + MONTH_FE + ["TB_l1", "TB_l2"], main, P),
    ("M1 with POST from 2013M10",
     ["MIN", "POST_alt", "POSTalt_x_MIN", "BRENT", "KZT"] + MONTH_FE, main, P),
    ("M1 product-level minerals (HS 2610/2612/2844/7403)",
     ["MIN4", "POST", "POST_x_MIN4", "BRENT", "KZT"] + MONTH_FE, main, P),
    ("M1 extended, imports as reported (break 2020-22)", BASE + MONTH_FE, full, "2010M01-2023M12"),
    ("M1 extended, mirror-adjusted imports 2020-22", BASE + MONTH_FE, full_adj,
     "2010M01-2023M12 (adj.)"),
    ("M1 extended, mirror-adjusted, excl. 2022-2023", BASE + MONTH_FE,
     full_adj[full_adj["year"] <= 2021], "2010M01-2021M12 (adj.)"),
]
KEYS = ["MIN", "POST", "POST_x_MIN", "MIN4", "POST_x_MIN4", "POST_alt", "POSTalt_x_MIN",
        "BRENT", "KZT", "TREND", "COPPER", "OIL27", "TB_l1", "TB_l2"]

res_rows, fit_rows, hyp_rows = [], [], []
for label, cols, data, sl in SPECS:
    sub, ols, hac = estimate(data, cols, label, sl)
    res_rows.append(coefs(hac, label, sl, KEYS))
    fit_rows.append(fitstats(ols, hac, cols, label, sl))
    if label.startswith("M1: "):
        mm, ii, pp = "MIN", "POST_x_MIN", "POST"
        for hid, var, alt, h0, h1 in [("H1", pp, "less", "beta_PostBRI >= 0", "beta_PostBRI < 0"),
                                      ("H2", mm, "greater", "beta_Minerals <= 0", "beta_Minerals > 0"),
                                      ("H3", ii, "less", "beta_Interaction >= 0", "beta_Interaction < 0")]:
            b, se, t = hac.params[var], hac.bse[var], hac.tvalues[var]
            dfr = ols.df_resid
            p1 = stats.t.cdf(t, dfr) if alt == "less" else 1 - stats.t.cdf(t, dfr)
            hyp_rows.append({"Model": label, "Hypothesis": hid, "Variable": var, "H0": h0, "H1": h1,
                             "Coef": b, "HAC_SE": se, "t_stat": t, "df_resid": int(dfr),
                             "p_two_sided": hac.pvalues[var], "p_one_sided": p1,
                             "Decision": "Reject H0 at 5%" if p1 < .05 else
                             ("Reject H0 at 10% only" if p1 < .10 else "Fail to reject H0")})
        jt = hac.f_test(f"{pp} = 0, {ii} = 0")
        hyp_rows.append({"Model": label, "Hypothesis": "Joint", "Variable": f"{pp}, {ii}",
                         "H0": "beta_PostBRI = beta_Interaction = 0", "H1": "at least one non-zero",
                         "t_stat": float(np.squeeze(jt.fvalue)), "p_two_sided": float(jt.pvalue),
                         "Decision": "Reject H0 at 5%" if jt.pvalue < .05 else
                         ("Reject H0 at 10% only" if jt.pvalue < .10 else "Fail to reject H0")})
        st = hac.t_test(f"{mm} + {ii} = 0")
        hyp_rows.append({"Model": label, "Hypothesis": "Post-BRI slope", "Variable": f"{mm} + {ii}",
                         "H0": "slope = 0", "H1": "slope != 0",
                         "Coef": float(np.squeeze(st.effect)), "HAC_SE": float(np.squeeze(st.sd)),
                         "t_stat": float(np.squeeze(st.tvalue)), "p_two_sided": float(st.pvalue),
                         "Decision": "Reject H0 at 5%" if st.pvalue < .05 else
                         ("Reject H0 at 10% only" if st.pvalue < .10 else "Fail to reject H0")})

res = pd.DataFrame(res_rows); fits = pd.DataFrame(fit_rows); hyp = pd.DataFrame(hyp_rows)
res.round(4).to_csv(TABLES / "monthly_results.csv", index=False)
fits.round(4).to_csv(TABLES / "monthly_fit_statistics.csv", index=False)
hyp.round(4).to_csv(TABLES / "monthly_hypothesis_tests.csv", index=False)
show = ["Model", "N", "MIN_coef", "MIN_p", "POST_coef", "POST_p", "POST_x_MIN_coef", "POST_x_MIN_p",
        "MIN4_coef", "MIN4_p", "POST_x_MIN4_coef", "POST_x_MIN4_p", "POSTalt_x_MIN_coef", "POSTalt_x_MIN_p"]
print(res[[c for c in show if c in res]].round(3).to_string())
print(fits[["Model", "N", "R2", "Adj_R2", "F_HAC_Wald_p", "AIC", "BIC", "RMSE_SER", "Durbin_Watson", "BG_p", "BP_p"]].round(3).to_string())
print(hyp.round(3).to_string())

# ── Quarterly aggregation of OBSERVED monthly data (56 quarters) ────────────
qq = main.copy()
qq["q"] = qq["period"].str[:4] + "Q" + ((qq["month"] - 1) // 3 + 1).astype(str)
qagg = qq.groupby("q").agg(TB=("TB", "sum"), MIN=("MIN", "sum"), BRENT=("BRENT", "mean"),
                           KZT=("KZT", "mean"), POST=("POST", "max"), n=("TB", "count"))
qagg = qagg[qagg["n"] == 3].copy()
qagg["POST_x_MIN"] = qagg["POST"] * qagg["MIN"]
qagg["qtr"] = qagg.index.str[-1].astype(int)
for k in [2, 3, 4]:
    qagg[f"q{k}"] = (qagg["qtr"] == k).astype(int)
_, qols, qhac = estimate(qagg, BASE + ["q2", "q3", "q4"], "Q-obs", "2010Q1-2019Q4", maxlags=4)
qrow = coefs(qhac, "Q1: observed quarterly (aggregated from monthly)", "2010Q1-2019Q4", KEYS)
qfit = fitstats(qols, qhac, BASE + ["q2", "q3", "q4"], "Q1: observed quarterly", "2010Q1-2019Q4")
pd.DataFrame([qrow]).round(4).to_csv(TABLES / "observed_quarterly_results.csv", index=False)
pd.DataFrame([qfit]).round(4).to_csv(TABLES / "observed_quarterly_fit_statistics.csv", index=False)
print("Observed quarterly:", {k: round(v, 3) if isinstance(v, float) else v for k, v in qrow.items()})
print("Observed quarterly fit: R2 %.3f adjR2 %.3f N %d" % (qfit["R2"], qfit["Adj_R2"], qfit["N"]))

# ── Unit roots (monthly) ────────────────────────────────────────────────────
ur = []
for v in ["TB", "MIN", "BRENT", "KZT"]:
    s = main[v].dropna()
    for lab, ser in [("level", s), ("first difference", s.diff().dropna())]:
        a = adfuller(ser, autolag="AIC", regression="c")
        k = kpss(ser, regression="c", nlags="auto")
        ur.append({"Variable": v, "Form": lab, "N": len(ser), "ADF_stat": a[0], "ADF_p": a[1],
                   "KPSS_stat": k[0], "KPSS_p": k[1]})
ur = pd.DataFrame(ur)
ur.round(4).to_csv(TABLES / "monthly_unit_root.csv", index=False)
print(ur.round(3).to_string())


# ── Granger causality (monthly) ─────────────────────────────────────────────
def deseason(s, month):
    d = pd.get_dummies(month, prefix="m", drop_first=True).astype(float)
    r = sm.OLS(s.values, sm.add_constant(d.values)).fit()
    return pd.Series(r.resid, index=s.index)


def toda_yamamoto(d, y, x, p, dmax, exog=None):
    L = p + dmax
    cols = {}
    for l in range(1, L + 1):
        cols[f"y_l{l}"] = d[y].shift(l)
        cols[f"x_l{l}"] = d[x].shift(l)
    R = pd.DataFrame(cols)
    R["y"] = d[y]
    if exog is not None:
        R = R.join(exog)
    R = R.dropna()
    X = sm.add_constant(R.drop(columns="y"))
    mm_ = sm.OLS(R["y"], X).fit(cov_type="HAC", cov_kwds={"maxlags": HAC_LAGS})
    w = mm_.wald_test(", ".join(f"x_l{l} = 0" for l in range(1, p + 1)), scalar=True, use_f=False)
    return float(w.statistic), float(w.pvalue), int(mm_.nobs)


gc_rows = []
samples = {"2010M01-2019M12": main, "pre-BRI 2010M01-2013M12": main[main["POST"] == 0],
           "post-BRI 2014M01-2019M12": main[main["POST"] == 1]}
# (Extended mirror-adjusted samples are not used for Granger tests: China's
#  monthly reports are missing for 2012M10-2015M12 and 2021M08-2023M12, so the
#  adjusted series has gaps and lag structures would be invalid.)
for sl, dsub in samples.items():
    d = dsub[["TB", "MIN", "BRENT", "month"]].dropna().reset_index(drop=True)
    d["TB_sa"] = deseason(d["TB"], d["month"])
    d["MIN_sa"] = deseason(d["MIN"], d["month"])
    maxlag = 6 if len(d) < 60 else 12
    # lag order by AIC on a VAR in first differences of seasonally adjusted series
    dd = d[["TB_sa", "MIN_sa"]].diff().dropna()
    sel = VAR(dd).select_order(maxlags=maxlag)
    p_aic = max(int(sel.aic), 1)
    p_bic = max(int(sel.bic), 1)
    for p, crit in sorted({(p_aic, "AIC"), (p_bic, "BIC")}):
        for y, x in [("TB_sa", "MIN_sa"), ("MIN_sa", "TB_sa")]:
            g = grangercausalitytests(dd[[y, x]], maxlag=[p])
            F, pv, dfd, dfn = g[p][0]["ssr_ftest"]
            gc_rows.append({"Frequency": "monthly", "Sample": sl,
                            "Null": f"{x.replace('_sa','')} does not Granger-cause {y.replace('_sa','')}",
                            "Method": "VAR in first differences (seasonally adjusted)",
                            "Lags": p, "Lag_rule": crit, "N_used": int(dfd + 2 * p + 1),
                            "Statistic": "F", "Stat_value": F, "p_value": pv})
            W, pw, nu = toda_yamamoto(d, y, x, p, dmax=1)
            gc_rows.append({"Frequency": "monthly", "Sample": sl,
                            "Null": f"{x.replace('_sa','')} does not Granger-cause {y.replace('_sa','')}",
                            "Method": "Toda-Yamamoto levels, dmax=1, HAC Wald",
                            "Lags": p, "Lag_rule": crit, "N_used": nu,
                            "Statistic": "Wald chi2", "Stat_value": W, "p_value": pw})
gc = pd.DataFrame(gc_rows)
gc["Decision_5pct"] = np.where(gc["p_value"] < 0.05, "Reject H0", "Fail to reject H0")
gc.round(4).to_csv(TABLES / "granger_monthly.csv", index=False)
print(gc.round(3).to_string())

# ── Figure ──────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 4.2))
x = main["date"].dt.to_timestamp()
ax.plot(x, main["TB"], color="#1f4e79", lw=1, label="Monthly trade balance (observed)")
ax.plot(x, main["TB"].rolling(12).mean(), color="#c55a11", lw=2, label="12-month moving average")
ax.plot(x, main["MIN"], color="#548235", lw=1, alpha=.8, label="Strategic mineral exports (HS 26+28)")
ax.axvline(pd.Timestamp("2013-09-07"), color="grey", ls="--", lw=1)
ax.text(pd.Timestamp("2013-11-01"), ax.get_ylim()[1] * .9, "BRI announced\n(Sept 2013)", fontsize=8, color="grey")
ax.axhline(0, color="black", lw=.6)
ax.set_ylabel("USD bn per month")
ax.set_title("Kazakhstan-China trade balance and strategic mineral exports, monthly 2010-2019")
ax.legend(fontsize=8, loc="lower left")
fig.text(0.01, 0.01, "Source: UN Comtrade monthly data (Kazakhstan as reporter). Author's calculations.", fontsize=7)
fig.tight_layout()
fig.savefig(FIGS / "fig_monthly_trade_balance.png", dpi=200)
print("done")
