"""
03_build_panel.py
Phase 1 — Merge all processed sources into the final analysis panel.

Inputs (from processed/):
  comtrade_minerals_annual.csv  — mineral exports + total (2000-2024)
  comtrade_reconciled.csv       — bilateral trade totals + balance (2000-2024)
  prices_annual.csv             — Brent + Copper annual means (2000-2024)
  wdi_annual.csv                — KAZ GDP, exchange rate, CPI (2000-2024)
  bri_intensity_annual.csv      — BRI flows, intensity, dummies (2000-2024)

Output: Collected_Raw_Data/clean_panel_annual.csv
  25 rows × N columns (year 2000-2024)

Validation: 25 rows, no missing on key vars (trade_balance, minerals_narrow_comtrade,
            brent_annual_mean, kz_gdp, bri_intensity, post_bri_2013)
"""

import pandas as pd
import numpy as np
from pathlib import Path

ROOT = Path(__file__).parent.parent
PROC = ROOT / "Collected_Raw_Data" / "processed"
OUT  = ROOT / "Collected_Raw_Data"

# -----------------------------------------------------------------------
# 1. Load all processed files
# -----------------------------------------------------------------------
minerals = pd.read_csv(PROC / "comtrade_minerals_annual.csv")
reconciled = pd.read_csv(PROC / "comtrade_reconciled.csv")
prices  = pd.read_csv(PROC / "prices_annual.csv")
wdi     = pd.read_csv(PROC / "wdi_annual.csv")
bri     = pd.read_csv(PROC / "bri_intensity_annual.csv")

print("Loaded:")
for name, df in [("minerals", minerals), ("reconciled", reconciled),
                 ("prices", prices), ("wdi", wdi), ("bri", bri)]:
    print(f"  {name}: {len(df)} rows ({df['year'].min()}-{df['year'].max()})")

# -----------------------------------------------------------------------
# 2. Build 2000-2024 spine
# -----------------------------------------------------------------------
panel = pd.DataFrame({"year": range(2000, 2025)})

# -----------------------------------------------------------------------
# 3. Merge trade balance series (from reconciled)
# -----------------------------------------------------------------------
trade_cols = ["year", "exports_kazakhstan_to_china_usd",
              "imports_kazakhstan_from_china_usd",
              "trade_balance_usd", "trade_balance_ratio"]
panel = panel.merge(reconciled[trade_cols], on="year", how="left")

# -----------------------------------------------------------------------
# 4. Merge mineral exports (from comtrade script)
# -----------------------------------------------------------------------
mineral_cols = ["year", "minerals_narrow_comtrade", "minerals_broad_comtrade",
                "exports_kaz_to_chn_comtrade", "oil_exports"]
panel = panel.merge(minerals[mineral_cols], on="year", how="left")

# Rename to standard codebook names
panel = panel.rename(columns={
    "minerals_narrow_comtrade":    "minerals_narrow",
    "minerals_broad_comtrade":     "minerals_broad",
    "exports_kaz_to_chn_comtrade": "total_comtrade",
})

# -----------------------------------------------------------------------
# 5. Merge prices
# -----------------------------------------------------------------------
panel = panel.merge(
    prices[["year", "brent_annual_mean", "copper_annual_mean"]],
    on="year", how="left"
)

# -----------------------------------------------------------------------
# 6. Merge WDI
# -----------------------------------------------------------------------
wdi_cols = ["year"] + [c for c in wdi.columns if c != "year"]
panel = panel.merge(wdi[wdi_cols], on="year", how="left")

# Standardise GDP columns
if "kz_gdp" in panel.columns:
    pass  # already there
if "kz_gdp_current_usd_panel" in panel.columns:
    panel["kz_gdp"] = panel.get("kz_gdp", pd.Series(np.nan)).fillna(
        panel["kz_gdp_current_usd_panel"]
    )

# -----------------------------------------------------------------------
# 7. Merge BRI variables
# -----------------------------------------------------------------------
panel = panel.merge(
    bri[["year", "bri_flows_annual", "bri_flows_cumulative",
         "bri_intensity", "post_bri_2013", "years_since_announcement"]],
    on="year", how="left"
)

# -----------------------------------------------------------------------
# 8. Derived variables
# -----------------------------------------------------------------------
# Mineral export share (using reconciled exports total as denominator)
panel["minerals_narrow_share"] = (
    panel["minerals_narrow"] / panel["exports_kazakhstan_to_china_usd"]
)
panel["minerals_broad_share"] = (
    panel["minerals_broad"] / panel["exports_kazakhstan_to_china_usd"]
)

# Log transforms (avoid log(0) — use log1p)
for col in ["minerals_narrow", "minerals_broad",
            "exports_kazakhstan_to_china_usd",
            "imports_kazakhstan_from_china_usd", "brent_annual_mean"]:
    if col in panel.columns:
        panel[f"log_{col}"] = np.log1p(panel[col].clip(lower=0))

if "kz_gdp" in panel.columns:
    panel["log_kz_gdp"] = np.log(panel["kz_gdp"].clip(lower=1))
if "cn_gdp" in panel.columns:
    panel["log_cn_gdp"] = np.log(panel["cn_gdp"].clip(lower=1))

# Interaction term
panel["post_bri_x_minerals_narrow"] = panel["post_bri_2013"] * panel["minerals_narrow"]
panel["bri_intensity_x_minerals_narrow"] = panel["bri_intensity"] * panel["minerals_narrow"]

# -----------------------------------------------------------------------
# 9. Sort and validate
# -----------------------------------------------------------------------
panel = panel.sort_values("year").reset_index(drop=True)

KEY_VARS = ["trade_balance_usd", "minerals_narrow", "brent_annual_mean",
            "kz_gdp", "bri_intensity", "post_bri_2013"]

print(f"\nPanel shape: {panel.shape}")
print(f"Years: {panel['year'].min()}–{panel['year'].max()} (n={len(panel)})")
print(f"\nMissing values by key variable:")
for v in KEY_VARS:
    n_miss = panel[v].isna().sum() if v in panel.columns else "COLUMN MISSING"
    print(f"  {v}: {n_miss} missing")

print(f"\nPanel summary:")
print(panel[["year", "trade_balance_usd", "minerals_narrow",
             "bri_intensity", "post_bri_2013",
             "brent_annual_mean", "kz_gdp"]].to_string(index=False))

# -----------------------------------------------------------------------
# 10. Save
# -----------------------------------------------------------------------
panel.to_csv(OUT / "clean_panel_annual.csv", index=False)
print(f"\nSaved Collected_Raw_Data/clean_panel_annual.csv: {len(panel)} rows")

# Warn about missing key vars
missing_key = [v for v in KEY_VARS if v in panel.columns and panel[v].isna().any()]
if missing_key:
    print(f"\nWARNING: Key variables with missing values: {missing_key}")
    print("See KNOWN_ISSUES.md for details.")
else:
    print("\nVALIDATION PASSED: No missing values on key variables.")
