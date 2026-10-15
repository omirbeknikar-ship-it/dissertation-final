"""
41_quarterly_interpolation.py
Supervisor feedback item 1 (option as suggested): temporal disaggregation of the
annual 2000-2023 panel to quarterly frequency (n = 96), re-estimation of the
association models, and a Monte Carlo check of what interpolation does to
statistical inference.

Method
------
Flow variables (trade balance, exports, imports, strategic minerals) are
disaggregated with the Denton-Cholette first-difference method (Denton 1971;
Dagum & Cholette 2006): the quarterly path is the smoothest path (minimum sum
of squared quarter-to-quarter changes) whose four quarters add up exactly to
the published annual total. Because no observed quarterly indicator exists for
the bilateral flows before 2010, the method uses a constant indicator.
Average-type variables (KZT/USD, GDP growth) are disaggregated the same way
under an average constraint. Brent and copper prices are NOT interpolated:
observed quarterly averages are taken from the World Bank Pink Sheet.

Why this is a robustness check, not the main result
---------------------------------------------------
Interpolated quarters are deterministic functions of the 24 annual totals.
They add rows, not information. The Monte Carlo in part 3 measures how often
interpolation produces "significant" results between two series that are
independent by construction.

Outputs
-------
  Collected_Raw_Data/processed/quarterly_interpolated_panel.csv
  Outputs/generated_tables/quarterly_interpolated_results.csv
  Outputs/generated_tables/interpolation_monte_carlo.csv
"""

import warnings
warnings.filterwarnings("ignore")

from pathlib import Path
import numpy as np
import pandas as pd
import statsmodels.api as sm

ROOT = Path(__file__).parent.parent
PANEL = ROOT / "Collected_Raw_Data" / "clean_panel_annual.csv"
PINK = ROOT / "Collected_Raw_Data" / "raw_downloads" / "pink_sheet_real.xlsx"
PROC = ROOT / "Collected_Raw_Data" / "processed"
TABLES = ROOT / "Outputs" / "generated_tables"
RNG = np.random.default_rng(20261015)


# ── 1. Denton-Cholette first-difference disaggregation ──────────────────────
def denton(annual, s=4, kind="sum"):
    """Smoothest high-frequency path consistent with annual totals/averages.

    Solves  min_q  sum_t (q_t - q_{t-1})^2   s.t.  C q = a
    where C aggregates s sub-periods into each year (sum or average).
    """
    a = np.asarray(annual, dtype=float)
    n = len(a)
    T = n * s
    C = np.kron(np.eye(n), np.ones((1, s)))
    if kind == "mean":
        C = C / s
    D = np.diff(np.eye(T), axis=0)          # (T-1) x T first-difference operator
    A = D.T @ D
    K = np.block([[2 * A, C.T], [C, np.zeros((n, n))]])
    rhs = np.concatenate([np.zeros(T), a])
    sol = np.linalg.lstsq(K, rhs, rcond=None)[0]
    return sol[:T]


ann = pd.read_csv(PANEL)
ann = ann[ann["year"].between(2000, 2023)].sort_values("year").reset_index(drop=True)
years = ann["year"].values
q_index = pd.period_range("2000Q1", "2023Q4", freq="Q")
assert len(q_index) == 4 * len(years)

q = pd.DataFrame({"quarter": q_index.astype(str)})
q["year"] = np.repeat(years, 4)
for col in ["exports_kazakhstan_to_china_usd", "imports_kazakhstan_from_china_usd",
            "minerals_narrow"]:
    q[col] = denton(ann[col].values / 1e9, kind="sum")
q["TB"] = q["exports_kazakhstan_to_china_usd"] - q["imports_kazakhstan_from_china_usd"]
q["MIN"] = q["minerals_narrow"]
q["KZT"] = denton(ann["kzt_usd"].values, kind="mean")
lg_kz, lg_cn = np.log(ann["kz_gdp"].values), np.log(ann["cn_gdp"].values)
# quarterly log-GDP path, then quarter-on-quarter growth x4 (annualised)
q["log_kz_gdp"] = denton(lg_kz, kind="mean")
q["log_cn_gdp"] = denton(lg_cn, kind="mean")
q["dlg_kz_gdp"] = q["log_kz_gdp"].diff() * 4
q["dlg_cn_gdp"] = q["log_cn_gdp"].diff() * 4

# Observed quarterly commodity prices (World Bank Pink Sheet, monthly -> quarterly mean)
pink = pd.read_excel(PINK, sheet_name="Monthly Prices", header=None)
hdr = pink.iloc[4].tolist()
col_brent, col_cu = hdr.index("Crude oil, Brent"), hdr.index("Copper")
pm = pink.iloc[6:, [0, col_brent, col_cu]].copy()
pm.columns = ["m", "BRENT", "COPPER"]
pm = pm[pm["m"].astype(str).str.match(r"^\d{4}M\d{2}$")]
pm["date"] = pd.PeriodIndex(pm["m"].str.replace("M", "-"), freq="M")
pm[["BRENT", "COPPER"]] = pm[["BRENT", "COPPER"]].apply(pd.to_numeric, errors="coerce")
pq = pm.groupby(pm["date"].dt.asfreq("Q"))[["BRENT", "COPPER"]].mean()
pq.index = pq.index.astype(str)
q = q.merge(pq, left_on="quarter", right_index=True, how="left")

q["POST"] = (q["year"] >= 2014).astype(int)
q["POST_x_MIN"] = q["POST"] * q["MIN"]
# check aggregation constraint
chk = q.groupby("year")["TB"].sum().values - ann["trade_balance_usd"].values / 1e9
assert np.max(np.abs(chk)) < 1e-6, "Denton constraint violated"
q.to_csv(PROC / "quarterly_interpolated_panel.csv", index=False)
print("Quarterly interpolated panel:", q.shape, "| max annual-sum error:", np.max(np.abs(chk)))


# ── 2. Re-estimate association models on 96 interpolated quarters ──────────
def est(data, cols, label, freq, maxlags):
    sub = data.dropna(subset=cols + ["TB"])
    X = sm.add_constant(sub[cols])
    ols = sm.OLS(sub["TB"], X).fit()
    hac = sm.OLS(sub["TB"], X).fit(cov_type="HAC", cov_kwds={"maxlags": maxlags}, use_t=True)
    out = {"Model": label, "Frequency": freq, "N": int(ols.nobs), "HAC_lags": maxlags,
           "R2": ols.rsquared, "Adj_R2": ols.rsquared_adj, "F_classical": ols.fvalue,
           "F_p": ols.f_pvalue, "AIC": ols.aic, "BIC": ols.bic,
           "RMSE": np.sqrt(ols.scale),
           "DW": sm.stats.stattools.durbin_watson(ols.resid)}
    for v in ["MIN", "POST", "POST_x_MIN"]:
        out[f"{v}_coef"] = hac.params[v]
        out[f"{v}_HAC_SE"] = hac.bse[v]
        out[f"{v}_p"] = hac.pvalues[v]
    return out


# annual reference (same construction as Script 40, A2 and B specs)
ann["TB"] = ann["trade_balance_usd"] / 1e9
ann["MIN"] = ann["minerals_narrow"] / 1e9
ann["BRENT"] = ann["brent_annual_mean"]
ann["KZT"] = ann["kzt_usd"]
ann["POST"] = ann["post_bri_2013"].astype(int)
ann["POST_x_MIN"] = ann["POST"] * ann["MIN"]
ann["dlg_kz_gdp"] = np.log(ann["kz_gdp"]).diff()
ann["dlg_cn_gdp"] = np.log(ann["cn_gdp"]).diff()

specA2 = ["MIN", "POST", "POST_x_MIN", "BRENT", "KZT"]
specB = specA2 + ["dlg_kz_gdp", "dlg_cn_gdp"]
rows = [
    est(ann, specB, "B: growth-rate controls", "annual (observed)", 3),
    est(q, specB, "B: growth-rate controls", "quarterly (Denton-interpolated)", 4),
    est(q, specB, "B: growth-rate controls", "quarterly (Denton-interpolated)", 12),
    est(ann, specA2, "A2: parsimonious", "annual (observed)", 3),
    est(q, specA2, "A2: parsimonious", "quarterly (Denton-interpolated)", 4),
    est(q, specA2, "A2: parsimonious", "quarterly (Denton-interpolated)", 12),
]
res = pd.DataFrame(rows)
res.round(4).to_csv(TABLES / "quarterly_interpolated_results.csv", index=False)
print(res[["Model", "Frequency", "N", "HAC_lags", "R2", "Adj_R2", "POST_x_MIN_coef",
           "POST_x_MIN_HAC_SE", "POST_x_MIN_p", "MIN_coef", "MIN_p", "DW"]].round(3).to_string())


# ── 3. Monte Carlo: interpolation and false-positive rates ──────────────────
def sim_once(n=24, phi=0.6):
    """Two INDEPENDENT annual AR(1) series; true slope = 0."""
    e1, e2 = RNG.normal(size=n + 50), RNG.normal(size=n + 50)
    y, x = np.zeros(n + 50), np.zeros(n + 50)
    for t in range(1, n + 50):
        y[t] = phi * y[t - 1] + e1[t]
        x[t] = phi * x[t - 1] + e2[t]
    y, x = y[50:], x[50:]
    out = {}
    m = sm.OLS(y, sm.add_constant(x)).fit(cov_type="HAC", cov_kwds={"maxlags": 3}, use_t=True)
    out["annual_n24_HAC3"] = m.pvalues[1] < 0.05
    yq, xq = denton(y, kind="sum"), denton(x, kind="sum")
    m0 = sm.OLS(yq, sm.add_constant(xq)).fit()
    out["quarterly_n96_OLS"] = m0.pvalues[1] < 0.05
    m4 = sm.OLS(yq, sm.add_constant(xq)).fit(cov_type="HAC", cov_kwds={"maxlags": 4}, use_t=True)
    out["quarterly_n96_HAC4"] = m4.pvalues[1] < 0.05
    m12 = sm.OLS(yq, sm.add_constant(xq)).fit(cov_type="HAC", cov_kwds={"maxlags": 12}, use_t=True)
    out["quarterly_n96_HAC12"] = m12.pvalues[1] < 0.05
    return out


R = 2000
sims = pd.DataFrame([sim_once() for _ in range(R)])
mc = pd.DataFrame({
    "Design": ["Annual, n=24, HAC(3)", "Interpolated quarterly, n=96, plain OLS SE",
               "Interpolated quarterly, n=96, HAC(4)", "Interpolated quarterly, n=96, HAC(12)"],
    "False_positive_rate_at_5pct": [sims["annual_n24_HAC3"].mean(), sims["quarterly_n96_OLS"].mean(),
                                    sims["quarterly_n96_HAC4"].mean(), sims["quarterly_n96_HAC12"].mean()],
    "Replications": R,
    "DGP": "two independent AR(1) annual series, phi=0.6, n=24; true slope = 0",
})


# Benchmark: an OBSERVED monthly sample of the size used in Script 42
def sim_monthly(n=120, phi=0.9):
    e1, e2 = RNG.normal(size=n + 100), RNG.normal(size=n + 100)
    y, x = np.zeros(n + 100), np.zeros(n + 100)
    for t in range(1, n + 100):
        y[t] = phi * y[t - 1] + e1[t]
        x[t] = phi * x[t - 1] + e2[t]
    y, x = y[100:], x[100:]
    m12 = sm.OLS(y, sm.add_constant(x)).fit(cov_type="HAC", cov_kwds={"maxlags": 12}, use_t=True)
    return m12.pvalues[1] < 0.05


mon = np.mean([sim_monthly() for _ in range(R)])
mc = pd.concat([mc, pd.DataFrame([{
    "Design": "Observed monthly, n=120, HAC(12) (benchmark)",
    "False_positive_rate_at_5pct": mon, "Replications": R,
    "DGP": "two independent AR(1) monthly series, phi=0.9, n=120; true slope = 0"}])],
    ignore_index=True)
mc.round(4).to_csv(TABLES / "interpolation_monte_carlo.csv", index=False)
print(mc.round(3).to_string())
