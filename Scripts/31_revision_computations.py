"""
31_revision_computations.py
Compute parsimonious model, WITS-consistent robustness, trade decomposition,
and excluding-2023 results for the revised dissertation.
"""
import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
from pathlib import Path
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.stats.stattools import durbin_watson
from statsmodels.stats.diagnostic import het_breuschpagan
from scipy import stats

ROOT = Path(__file__).parent.parent
PANEL = ROOT / "Collected_Raw_Data" / "clean_panel_annual.csv"
WITS = ROOT / "Collected_Raw_Data" / "raw" / "wits_ores_metals_exports_kazakhstan_china.csv"
TABLES = ROOT / "Outputs" / "generated_tables"
TABLES.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(PANEL)
df = df[df["year"] < 2024].dropna(
    subset=["trade_balance_usd", "minerals_narrow", "brent_annual_mean",
            "kz_gdp", "cn_gdp"]
).copy()
df = df.sort_values("year").reset_index(drop=True)
df["minerals_narrow_B"] = df["minerals_narrow"] / 1e9
df["trade_balance_B"] = df["trade_balance_usd"] / 1e9
df["exports_B"] = df["exports_kazakhstan_to_china_usd"] / 1e9
df["imports_B"] = df["imports_kazakhstan_from_china_usd"] / 1e9
df["log_kz_gdp"] = np.log(df["kz_gdp"])
df["log_cn_gdp"] = np.log(df["cn_gdp"])
df["post_bri_x_minerals"] = df["post_bri_2013"] * df["minerals_narrow_B"]
df["oil_exports_B"] = df["oil_exports"] / 1e9
n = len(df)


print("=" * 70)
print("  1. TRADE BALANCE DECOMPOSITION")
print("=" * 70)
pre = df[df["post_bri_2013"] == 0]
post = df[df["post_bri_2013"] == 1]

decomp = {
    "Variable": [
        "Exports to China (USD bn)",
        "Imports from China (USD bn)",
        "Trade Balance (USD bn)",
        "Minerals Narrow (USD bn)",
        "Trade Balance Ratio",
    ],
    "Pre-BRI Mean": [
        pre["exports_B"].mean(),
        pre["imports_B"].mean(),
        pre["trade_balance_B"].mean(),
        pre["minerals_narrow_B"].mean(),
        pre["trade_balance_ratio"].mean(),
    ],
    "Post-BRI Mean": [
        post["exports_B"].mean(),
        post["imports_B"].mean(),
        post["trade_balance_B"].mean(),
        post["minerals_narrow_B"].mean(),
        post["trade_balance_ratio"].mean(),
    ],
}
decomp_df = pd.DataFrame(decomp)
decomp_df["Change (%)"] = ((decomp_df["Post-BRI Mean"] - decomp_df["Pre-BRI Mean"]) / decomp_df["Pre-BRI Mean"].abs() * 100).round(1)
decomp_df["Pre-BRI Mean"] = decomp_df["Pre-BRI Mean"].round(3)
decomp_df["Post-BRI Mean"] = decomp_df["Post-BRI Mean"].round(3)
print(decomp_df.to_string(index=False))
decomp_df.to_csv(TABLES / "trade_decomposition.csv", index=False)

# Growth rates
export_growth = (post["exports_B"].mean() - pre["exports_B"].mean()) / pre["exports_B"].mean() * 100
import_growth = (post["imports_B"].mean() - pre["imports_B"].mean()) / pre["imports_B"].mean() * 100
print(f"\nExport growth: {export_growth:.1f}%")
print(f"Import growth: {import_growth:.1f}%")
print(f"Import growth exceeded export growth: {import_growth > export_growth}")

# Year-by-year for the paper
print("\nYear-by-year exports, imports, balance:")
for _, row in df.iterrows():
    print(f"  {int(row['year'])}: exports={row['exports_B']:.2f}  imports={row['imports_B']:.2f}  balance={row['trade_balance_B']:.2f}")

print("\n" + "=" * 70)
print("  2. FULL MODEL (7 regressors)")
print("=" * 70)
exog_full = ["minerals_narrow_B", "brent_annual_mean", "kzt_usd",
             "log_kz_gdp", "log_cn_gdp", "post_bri_2013", "post_bri_x_minerals", "oil_exports_B"]
X_full = sm.add_constant(df[exog_full])
ols_full = sm.OLS(df["trade_balance_B"], X_full).fit()
ols_full_hac = ols_full.get_robustcov_results(cov_type="HAC", maxlags=3)
print(f"N = {int(ols_full.nobs)}, R² = {ols_full.rsquared:.4f}, Adj R² = {ols_full.rsquared_adj:.4f}")
print(f"{'Variable':<25} {'Coef':>10} {'HAC SE':>10} {'t':>8} {'p':>8}")
for nm, c, se, t, p in zip(ols_full_hac.model.exog_names, ols_full_hac.params,
                            ols_full_hac.bse, ols_full_hac.tvalues, ols_full_hac.pvalues):
    print(f"  {nm:<23} {c:>10.4f} {se:>10.4f} {t:>8.3f} {p:>8.4f}")
dw_full = durbin_watson(ols_full.resid)
bp_full = het_breuschpagan(ols_full.resid, X_full)
print(f"DW = {dw_full:.4f}, BP stat = {bp_full[0]:.4f} (p = {bp_full[1]:.4f})")

print("\n" + "=" * 70)
print("  3. PARSIMONIOUS MODEL (no GDP controls)")
print("=" * 70)
exog_pars = ["minerals_narrow_B", "brent_annual_mean", "kzt_usd",
             "post_bri_2013", "post_bri_x_minerals", "oil_exports_B"]

X_pars = sm.add_constant(df[exog_pars])
ols_pars = sm.OLS(df["trade_balance_B"], X_pars).fit()
ols_pars_hac = ols_pars.get_robustcov_results(cov_type="HAC", maxlags=3)
print(f"N = {int(ols_pars.nobs)}, R² = {ols_pars.rsquared:.4f}, Adj R² = {ols_pars.rsquared_adj:.4f}")
print(f"{'Variable':<25} {'Coef':>10} {'HAC SE':>10} {'t':>8} {'p':>8}")
for nm, c, se, t, p in zip(ols_pars_hac.model.exog_names, ols_pars_hac.params,
                            ols_pars_hac.bse, ols_pars_hac.tvalues, ols_pars_hac.pvalues):
    print(f"  {nm:<23} {c:>10.4f} {se:>10.4f} {t:>8.3f} {p:>8.4f}")

# VIF for parsimonious
vif_pars = []
for i, col in enumerate(X_pars.columns):
    if col == "const":
        continue
    vif_pars.append({"Variable": col, "VIF": round(variance_inflation_factor(X_pars.values, i), 2)})
vif_pars_df = pd.DataFrame(vif_pars)
print("\nVIF (parsimonious):")
print(vif_pars_df.to_string(index=False))

dw_pars = durbin_watson(ols_pars.resid)
bp_pars = het_breuschpagan(ols_pars.resid, X_pars)
print(f"DW = {dw_pars:.4f}, BP stat = {bp_pars[0]:.4f} (p = {bp_pars[1]:.4f})")

# Save parsimonious table
pars_table = []
for nm, c, se, t, p in zip(ols_pars_hac.model.exog_names, ols_pars_hac.params,
                            ols_pars_hac.bse, ols_pars_hac.tvalues, ols_pars_hac.pvalues):
    stars = ""
    if p < 0.01: stars = "***"
    elif p < 0.05: stars = "**"
    elif p < 0.10: stars = "*"
    pars_table.append({"Variable": nm, "Coefficient": round(c, 4), "HAC_SE": round(se, 4),
                        "t_stat": round(t, 3), "p_value": round(p, 4), "Significance": stars})
pd.DataFrame(pars_table).to_csv(TABLES / "parsimonious_regression.csv", index=False)

print("\n" + "=" * 70)
print("  4. EXCLUDING 2023")
print("=" * 70)
df_no23 = df[df["year"] != 2023].copy().reset_index(drop=True)
X_no23 = sm.add_constant(df_no23[exog_full])
ols_no23 = sm.OLS(df_no23["trade_balance_B"], X_no23).fit()
ols_no23_hac = ols_no23.get_robustcov_results(cov_type="HAC", maxlags=3)
print(f"N = {int(ols_no23.nobs)}, R² = {ols_no23.rsquared:.4f}, Adj R² = {ols_no23.rsquared_adj:.4f}")
print(f"{'Variable':<25} {'Coef':>10} {'HAC SE':>10} {'t':>8} {'p':>8}")
for nm, c, se, t, p in zip(ols_no23_hac.model.exog_names, ols_no23_hac.params,
                            ols_no23_hac.bse, ols_no23_hac.tvalues, ols_no23_hac.pvalues):
    print(f"  {nm:<23} {c:>10.4f} {se:>10.4f} {t:>8.3f} {p:>8.4f}")

# Parsimonious excluding 2023
X_no23_pars = sm.add_constant(df_no23[exog_pars])
ols_no23_pars = sm.OLS(df_no23["trade_balance_B"], X_no23_pars).fit()
ols_no23_pars_hac = ols_no23_pars.get_robustcov_results(cov_type="HAC", maxlags=3)
print(f"\nParsimonious excluding 2023:")
print(f"N = {int(ols_no23_pars.nobs)}, R² = {ols_no23_pars.rsquared:.4f}")
for nm, c, se, t, p in zip(ols_no23_pars_hac.model.exog_names, ols_no23_pars_hac.params,
                            ols_no23_pars_hac.bse, ols_no23_pars_hac.tvalues, ols_no23_pars_hac.pvalues):
    print(f"  {nm:<23} {c:>10.4f} {se:>10.4f} {t:>8.3f} {p:>8.4f}")

print("\n" + "=" * 70)
print("  5. WITS CONSISTENT PROXY (2000-2023)")
print("=" * 70)
try:
    wits = pd.read_csv(WITS)
    wits["minerals_wits_B"] = pd.to_numeric(wits["value_usd_thousand"], errors="coerce") * 1000 / 1e9
    df_w = df.merge(wits[["year", "minerals_wits_B"]], on="year", how="left")
    df_w["post_bri_x_wits"] = df_w["post_bri_2013"] * df_w["minerals_wits_B"]
    df_w = df_w.dropna(subset=["minerals_wits_B"])
    exog_wits = ["minerals_wits_B", "brent_annual_mean", "kzt_usd",
                 "post_bri_2013", "post_bri_x_wits"]
    X_wits = sm.add_constant(df_w[exog_wits])
    ols_wits = sm.OLS(df_w["trade_balance_B"], X_wits).fit()
    ols_wits_hac = ols_wits.get_robustcov_results(cov_type="HAC", maxlags=3)
    print(f"N = {int(ols_wits.nobs)}, R² = {ols_wits.rsquared:.4f}")
    for nm, c, se, t, p in zip(ols_wits_hac.model.exog_names, ols_wits_hac.params,
                                ols_wits_hac.bse, ols_wits_hac.tvalues, ols_wits_hac.pvalues):
        print(f"  {nm:<23} {c:>10.4f} {se:>10.4f} {t:>8.3f} {p:>8.4f}")
    
    # Also WITS excluding 2023
    df_w_no23 = df_w[df_w["year"] != 2023].copy()
    X_wits_no23 = sm.add_constant(df_w_no23[exog_wits])
    ols_wits_no23 = sm.OLS(df_w_no23["trade_balance_B"], X_wits_no23).fit()
    ols_wits_no23_hac = ols_wits_no23.get_robustcov_results(cov_type="HAC", maxlags=3)
    print(f"\nWITS excluding 2023: N = {int(ols_wits_no23.nobs)}, R² = {ols_wits_no23.rsquared:.4f}")
    for nm, c, se, t, p in zip(ols_wits_no23_hac.model.exog_names, ols_wits_no23_hac.params,
                                ols_wits_no23_hac.bse, ols_wits_no23_hac.tvalues, ols_wits_no23_hac.pvalues):
        print(f"  {nm:<23} {c:>10.4f} {se:>10.4f} {t:>8.3f} {p:>8.4f}")
except Exception as e:
    print(f"WITS robustness failed: {e}")

print("\n" + "=" * 70)
print("  6. MODEL COMPARISON SUMMARY TABLE")
print("=" * 70)

summary_rows = [
    {"Model": "A1: Full (7 regressors)", "Sample": "2000-2023 (n=24)",
     "Interaction_Coef": round(float(ols_full.params["post_bri_x_minerals"]), 4),
     "Interaction_SE": round(float(ols_full_hac.bse[ols_full_hac.model.exog_names.index("post_bri_x_minerals")]), 4),
     "Interaction_P": round(float(ols_full_hac.pvalues[ols_full_hac.model.exog_names.index("post_bri_x_minerals")]), 4),
     "R2": round(ols_full.rsquared, 4), "AdjR2": round(ols_full.rsquared_adj, 4)},
    {"Model": "A2: Parsimonious (no GDP)", "Sample": "2000-2023 (n=24)",
     "Interaction_Coef": round(float(ols_pars.params["post_bri_x_minerals"]), 4),
     "Interaction_SE": round(float(ols_pars_hac.bse[ols_pars_hac.model.exog_names.index("post_bri_x_minerals")]), 4),
     "Interaction_P": round(float(ols_pars_hac.pvalues[ols_pars_hac.model.exog_names.index("post_bri_x_minerals")]), 4),
     "R2": round(ols_pars.rsquared, 4), "AdjR2": round(ols_pars.rsquared_adj, 4)},
    {"Model": "A3: Full, excl. 2023", "Sample": "2000-2022 (n=23)",
     "Interaction_Coef": round(float(ols_no23.params["post_bri_x_minerals"]), 4),
     "Interaction_SE": round(float(ols_no23_hac.bse[ols_no23_hac.model.exog_names.index("post_bri_x_minerals")]), 4),
     "Interaction_P": round(float(ols_no23_hac.pvalues[ols_no23_hac.model.exog_names.index("post_bri_x_minerals")]), 4),
     "R2": round(ols_no23.rsquared, 4), "AdjR2": round(ols_no23.rsquared_adj, 4)},
    {"Model": "A4: Parsimonious, excl. 2023", "Sample": "2000-2022 (n=23)",
     "Interaction_Coef": round(float(ols_no23_pars.params["post_bri_x_minerals"]), 4),
     "Interaction_SE": round(float(ols_no23_pars_hac.bse[ols_no23_pars_hac.model.exog_names.index("post_bri_x_minerals")]), 4),
     "Interaction_P": round(float(ols_no23_pars_hac.pvalues[ols_no23_pars_hac.model.exog_names.index("post_bri_x_minerals")]), 4),
     "R2": round(ols_no23_pars.rsquared, 4), "AdjR2": round(ols_no23_pars.rsquared_adj, 4)},
]
summary_df = pd.DataFrame(summary_rows)
print(summary_df.to_string(index=False))
summary_df.to_csv(TABLES / "model_comparison_summary.csv", index=False)

# 2023 data point
yr23 = df[df["year"] == 2023].iloc[0]
print(f"\n2023 data point:")
print(f"  exports_B = {yr23['exports_B']:.2f}")
print(f"  imports_B = {yr23['imports_B']:.2f}")
print(f"  trade_balance_B = {yr23['trade_balance_B']:.2f}")
print(f"  minerals_narrow_B = {yr23['minerals_narrow_B']:.2f}")
print(f"  This is the ONLY year with negative trade balance.")

print("\nDone: 31_revision_computations.py")
