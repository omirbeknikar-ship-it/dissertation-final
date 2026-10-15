"""
43_import_break_sensitivity.py
Data-quality finding uncovered while building the monthly dataset (Script 42):
Kazakhstan-reported imports from China (UN Comtrade, reporter 398) fall to an
implausibly low level in 2020-2022 and recover in 2023.

Evidence: China-reported exports to Kazakhstan (reporter 156) are on average
2.2 times the Kazakhstan-reported import figure in 2016-2019 (normal CIF/FOB,
timing, transit and unrecorded-trade gaps), but 6.0 times in 2020. Monthly
Kazakhstan records for 2020-2022 also omit the HS 84/85/87 import chapters
that are present in every month of 2010-2019 and 2023.

This script re-estimates the annual models after replacing 2020-2022 imports
with a mirror-based estimate:
    M_adj(t) = China-reported exports to KZ (t) x [KZ imports / CN exports](2016-2019)
and reports how H1-H3, fit statistics and the 2023 influence diagnostics change.

Outputs:
  Outputs/generated_tables/import_break_evidence.csv
  Outputs/generated_tables/import_break_sensitivity.csv
"""

import warnings
warnings.filterwarnings("ignore")

from pathlib import Path
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import OLSInfluence

ROOT = Path(__file__).parent.parent
RAW = ROOT / "Collected_Raw_Data" / "raw_downloads"
TABLES = ROOT / "Outputs" / "generated_tables"

kz = pd.read_csv(RAW / "comtrade_monthly_kaz_reporter.csv", dtype={"period": str})
cn = pd.read_csv(RAW / "comtrade_monthly_chn_reporter.csv", dtype={"period": str})
for d in (kz, cn):
    d["year"] = d["period"].str[:4].astype(int)

ev = kz.groupby("year").agg(KZ_imports_bn=("MTOTAL", "sum"), KZ_exports_bn=("XTOTAL", "sum"),
                            KZ_months=("MTOTAL", "count"),
                            HS84_85_87_months=("M84", "count"))
cnm = cn.groupby("year").agg(CN_exports_to_KZ_bn=("XTOTAL", "sum"), CN_imports_from_KZ_bn=("MTOTAL", "sum"),
                             CN_months=("XTOTAL", "count"))
# Annual China-reported totals (UN Comtrade, freq A) for years where the
# monthly China series is incomplete (2013-2015, 2021-2023).
cna = pd.read_csv(RAW / "comtrade_annual_chn_reporter_selected.csv").set_index("year")
for y in cna.index:
    cnm.loc[y, "CN_exports_to_KZ_bn"] = cna.loc[y, "XTOTAL"]   # thousand USD, converted below
    cnm.loc[y, "CN_imports_from_KZ_bn"] = cna.loc[y, "MTOTAL"]
    cnm.loc[y, "CN_months"] = 12
cnm["CN_exports_to_KZ_bn"] = cnm["CN_exports_to_KZ_bn"].astype(float)
ev = ev.join(cnm, how="left")
ev[["KZ_imports_bn", "KZ_exports_bn", "CN_exports_to_KZ_bn", "CN_imports_from_KZ_bn"]] /= 1e6
ev.loc[ev["CN_months"] < 12, ["CN_exports_to_KZ_bn", "CN_imports_from_KZ_bn"]] = np.nan  # incomplete years
ev["ratio_CN_to_KZ"] = ev["CN_exports_to_KZ_bn"] / ev["KZ_imports_bn"]
ev["ratio_CNimports_to_KZexports"] = ev["CN_imports_from_KZ_bn"] / ev["KZ_exports_bn"]
base = ev.loc[2016:2019]
RATIO = base["KZ_imports_bn"].sum() / base["CN_exports_to_KZ_bn"].sum()
RATIO_X = base["KZ_exports_bn"].sum() / base["CN_imports_from_KZ_bn"].sum()
ev["KZ_exports_mirror_adjusted_bn"] = ev["KZ_exports_bn"]
for y in (2020, 2021, 2022):
    ev.loc[y, "KZ_exports_mirror_adjusted_bn"] = ev.loc[y, "CN_imports_from_KZ_bn"] * RATIO_X
ev["KZ_imports_mirror_adjusted_bn"] = ev["KZ_imports_bn"]
for y in (2020, 2021, 2022):
    if y in ev.index and pd.notna(ev.loc[y, "CN_exports_to_KZ_bn"]):
        ev.loc[y, "KZ_imports_mirror_adjusted_bn"] = ev.loc[y, "CN_exports_to_KZ_bn"] * RATIO
    elif y in ev.index:
        ev.loc[y, "KZ_imports_mirror_adjusted_bn"] = np.nan
ev.round(3).to_csv(TABLES / "import_break_evidence.csv")
print("Mirror ratio (KZ imports / CN exports), 2016-2019:", round(RATIO, 3))
print(ev.round(2).to_string())

# ── Annual re-estimation ─────────────────────────────────────────────────────
ann = pd.read_csv(ROOT / "Collected_Raw_Data" / "clean_panel_annual.csv")
ann = ann[ann["year"].between(2000, 2023)].sort_values("year").reset_index(drop=True)
ann["X"] = ann["exports_kazakhstan_to_china_usd"] / 1e9
ann["M"] = ann["imports_kazakhstan_from_china_usd"] / 1e9
ann["MIN"] = ann["minerals_narrow"] / 1e9
ann["BRENT"] = ann["brent_annual_mean"]
ann["KZT"] = ann["kzt_usd"]
ann["POST"] = ann["post_bri_2013"].astype(int)
ann["POST_x_MIN"] = ann["POST"] * ann["MIN"]
ann["dlg_kz_gdp"] = np.log(ann["kz_gdp"]).diff()
ann["dlg_cn_gdp"] = np.log(ann["cn_gdp"]).diff()
ann["gravity_ratio"] = np.log(ann["cn_gdp"]) - np.log(ann["kz_gdp"])
ann["M_adj"] = ann["M"]
for y in (2020, 2021, 2022):
    ann.loc[ann["year"] == y, "M_adj"] = ev.loc[y, "KZ_imports_mirror_adjusted_bn"]
ann["TB_reported"] = ann["X"] - ann["M"]
ann["TB_adjusted"] = ann["X"] - ann["M_adj"]
ann["X_adj"] = ann["X"]
for y in (2020, 2021, 2022):
    ann.loc[ann["year"] == y, "X_adj"] = ev.loc[y, "KZ_exports_mirror_adjusted_bn"]
ann["TB_both_adjusted"] = ann["X_adj"] - ann["M_adj"]

SPECS = {
    "B (primary)": ["MIN", "POST", "POST_x_MIN", "BRENT", "KZT", "dlg_kz_gdp", "dlg_cn_gdp"],
    "C (gravity ratio)": ["MIN", "POST", "POST_x_MIN", "BRENT", "KZT", "gravity_ratio"],
    "A2 (parsimonious)": ["MIN", "POST", "POST_x_MIN", "BRENT", "KZT"],
}
rows = []
DEPLAB = {"TB_reported": "TB as reported", "TB_adjusted": "TB, 2020-22 imports mirror-adjusted",
          "TB_both_adjusted": "TB, 2020-22 exports and imports mirror-adjusted"}
for yname in ["TB_reported", "TB_adjusted", "TB_both_adjusted"]:
    for sname, cols in SPECS.items():
        for excl, lab in [(None, "full sample"), ([2023], "excl. 2023"), ([2022, 2023], "excl. 2022-2023")]:
            d = ann.dropna(subset=cols + [yname])
            if excl:
                d = d[~d["year"].isin(excl)]
            X = sm.add_constant(d[cols])
            ols = sm.OLS(d[yname], X).fit()
            hac = sm.OLS(d[yname], X).fit(cov_type="HAC", cov_kwds={"maxlags": 3}, use_t=True)
            infl = OLSInfluence(ols)
            cd = pd.Series(np.asarray(infl.cooks_distance[0]), index=d["year"].values)
            rows.append({
                "Dependent": DEPLAB[yname],
                "Spec": sname, "Sample": lab, "N": int(ols.nobs),
                "Interaction_coef": hac.params["POST_x_MIN"], "Interaction_SE": hac.bse["POST_x_MIN"],
                "Interaction_p": hac.pvalues["POST_x_MIN"],
                "Minerals_coef": hac.params["MIN"], "Minerals_p": hac.pvalues["MIN"],
                "PostBRI_coef": hac.params["POST"], "PostBRI_p": hac.pvalues["POST"],
                "R2": ols.rsquared, "Adj_R2": ols.rsquared_adj, "AIC": ols.aic, "BIC": ols.bic,
                "CooksD_2023": cd.get(2023, np.nan), "CooksD_threshold_4_over_n": 4 / ols.nobs,
                "Max_CooksD_year": int(cd.idxmax()), "Max_CooksD": cd.max(),
            })
res = pd.DataFrame(rows)
res.round(4).to_csv(TABLES / "import_break_sensitivity.csv", index=False)
print(res[["Dependent", "Spec", "Sample", "N", "Interaction_coef", "Interaction_p", "Minerals_p",
           "R2", "Adj_R2", "CooksD_2023", "Max_CooksD_year", "Max_CooksD"]].round(3).to_string())
print("Export ratio KZ/CN 2016-19:", round(RATIO_X, 3))
print(ann[["year", "X", "X_adj", "M", "M_adj", "TB_reported", "TB_adjusted", "TB_both_adjusted"]].tail(6).round(2).to_string())

# ── Sensitivity to the assumed reporting ratio ───────────────────────────────
# Lowest and highest annual KZ/CN ratios observed in the complete years 2013-2019,
# plus the 2016-2019 pooled ratio used above.
yrs = [y for y in range(2013, 2020) if pd.notna(ev.loc[y, "CN_exports_to_KZ_bn"])]
ratios = (ev.loc[yrs, "KZ_imports_bn"] / ev.loc[yrs, "CN_exports_to_KZ_bn"])
grid = {"lowest annual ratio 2013-19": ratios.min(), "pooled 2016-19 (baseline)": RATIO,
        "highest annual ratio 2013-19": ratios.max()}
rrows = []
for rlab, r in grid.items():
    a = ann.copy()
    for y in (2020, 2021, 2022):
        a.loc[a["year"] == y, "M_adj"] = ev.loc[y, "CN_exports_to_KZ_bn"] * r
    a["TBr"] = a["X"] - a["M_adj"]
    for sname in ["B (primary)", "A2 (parsimonious)"]:
        cols = SPECS[sname]
        for excl, lab in [(None, "full sample"), ([2023], "excl. 2023"), ([2022, 2023], "excl. 2022-2023")]:
            d = a.dropna(subset=cols + ["TBr"])
            if excl:
                d = d[~d["year"].isin(excl)]
            hac = sm.OLS(d["TBr"], sm.add_constant(d[cols])).fit(
                cov_type="HAC", cov_kwds={"maxlags": 3}, use_t=True)
            rrows.append({"Ratio_assumption": rlab, "KZ_to_CN_ratio": r, "Spec": sname, "Sample": lab,
                          "N": int(hac.nobs), "Interaction_coef": hac.params["POST_x_MIN"],
                          "Interaction_p": hac.pvalues["POST_x_MIN"],
                          "TB_2020": a.loc[a.year == 2020, "TBr"].item(),
                          "TB_2021": a.loc[a.year == 2021, "TBr"].item(),
                          "TB_2022": a.loc[a.year == 2022, "TBr"].item()})
rr = pd.DataFrame(rrows)
rr.round(4).to_csv(TABLES / "import_break_ratio_sensitivity.csv", index=False)
print(rr.round(3).to_string())

# ── Figure: reported vs mirror imports ──────────────────────────────────────
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
FIGS = ROOT / "Outputs" / "generated_figures"
fig, ax = plt.subplots(figsize=(9, 4.2))
e = ev.loc[2010:2023]
ax.plot(e.index, e["KZ_imports_bn"], marker="o", color="#1f4e79", label="Kazakhstan-reported imports from China")
ax.plot(e.index, e["CN_exports_to_KZ_bn"], marker="s", color="#c55a11", label="China-reported exports to Kazakhstan (mirror)")
ax.plot(e.loc[2019:2023].index, e.loc[2019:2023, "KZ_imports_mirror_adjusted_bn"], ls="--", color="#548235",
        label="Mirror-adjusted Kazakhstan imports (2020-2022)")
ax.axvspan(2019.5, 2022.5, color="grey", alpha=.12)
ax.text(2019.6, ax.get_ylim()[1] * .92, "reporting break", fontsize=8, color="grey")
ax.set_ylabel("USD bn"); ax.set_xticks(range(2010, 2024, 1)); ax.tick_params(axis="x", labelsize=8)
ax.set_title("Kazakhstan's imports from China: own reports vs China's mirror data")
ax.legend(fontsize=8, loc="upper left")
fig.text(0.01, 0.01, "Source: UN Comtrade (monthly and annual, both reporters). Author's calculations.", fontsize=7)
fig.tight_layout(); fig.savefig(FIGS / "fig_import_reporting_break.png", dpi=200)

# ── Annual Granger tests on the mirror-adjusted balance ─────────────────────
from statsmodels.tsa.stattools import grangercausalitytests
grow = []
for yname in ["TB_adjusted", "TB_both_adjusted"]:
    d = ann[["year", yname, "MIN"]].dropna()
    dd = d[[yname, "MIN"]].diff().dropna()
    for y, x in [(yname, "MIN"), ("MIN", yname)]:
        for p in (1, 2):
            g = grangercausalitytests(dd[[y, x]], maxlag=[p])
            F, pv, dfd, _ = g[p][0]["ssr_ftest"]
            grow.append({"Balance_series": DEPLAB[yname],
                         "Null": f"{'TB' if x != 'MIN' else 'Minerals'} does not Granger-cause {'TB' if y != 'MIN' else 'Minerals'}",
                         "Lags": p, "F": F, "p_value": pv})
gdf = pd.DataFrame(grow)
gdf.round(4).to_csv(TABLES / "granger_annual_adjusted.csv", index=False)
print(gdf.round(3).to_string())
