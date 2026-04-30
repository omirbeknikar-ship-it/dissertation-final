"""
01d_load_bri.py
Phase 1 — Parse AidData GCDF v3.0 for Kazakhstan BRI flows.

Source: AidData Global Chinese Development Finance Dataset v3.0
  File: Collected_Raw_Data/raw_downloads/aiddata_gcdf_v3.xlsx (xlsx renamed .csv)
  Sheet: GCDF_3.0
  Filter: Recipient ISO-3 == 'KAZ', Flow Class in {ODA-like, OOF-like}

Output columns:
  year, bri_flows_annual (nominal USD, ODA+OOF committed),
  bri_flows_cumulative, bri_intensity = log1p(bri_flows_cumulative),
  post_bri_2013, years_since_announcement

Output: Collected_Raw_Data/processed/bri_intensity_annual.csv
"""

import pandas as pd
import numpy as np
from pathlib import Path

ROOT = Path(__file__).parent.parent
RAW  = ROOT / "Collected_Raw_Data" / "raw_downloads"
PROC = ROOT / "Collected_Raw_Data" / "processed"
PROC.mkdir(parents=True, exist_ok=True)

# -----------------------------------------------------------------------
# 1. Load AidData xlsx (file has .csv extension but is Excel format)
# -----------------------------------------------------------------------
aid = pd.read_excel(
    str(RAW / "aiddata_gcdf_v3.xlsx"),
    sheet_name="GCDF_3.0",
    engine="openpyxl",
)
print(f"AidData full dataset: {len(aid):,} rows")

# -----------------------------------------------------------------------
# 2. Filter to Kazakhstan + ODA/OOF-like
# -----------------------------------------------------------------------
kaz = aid[
    (aid["Recipient ISO-3"].str.upper() == "KAZ") &
    (aid["Flow Class"].isin(["ODA-like", "OOF-like"]))
].copy()

print(f"Kazakhstan ODA/OOF rows: {len(kaz)}")
print(f"Flow class breakdown:\n{kaz['Flow Class'].value_counts()}")
print(f"Years covered: {sorted(kaz['Commitment Year'].dropna().astype(int).unique())}")

# -----------------------------------------------------------------------
# 3. Aggregate committed amount per year
# -----------------------------------------------------------------------
kaz["year"] = kaz["Commitment Year"].astype(float).astype("Int64")
kaz["amount_usd"] = pd.to_numeric(kaz["Amount (Nominal USD)"], errors="coerce")

# Flag: use "Recommended For Aggregates" == "Yes" to avoid double-counting
kaz_agg = kaz[kaz["Recommended For Aggregates"].str.upper() == "YES"].copy()
print(f"\nRecommended-for-aggregates rows: {len(kaz_agg)}")

annual_flows = (
    kaz_agg.dropna(subset=["year", "amount_usd"])
    .groupby("year")["amount_usd"]
    .sum()
    .reset_index()
    .rename(columns={"amount_usd": "bri_flows_annual"})
    .assign(year=lambda d: d["year"].astype(int))
)

# -----------------------------------------------------------------------
# 4. Build full 2000-2024 spine and compute BRI intensity variables
# -----------------------------------------------------------------------
full_years = pd.DataFrame({"year": range(2000, 2025)})
bri_panel = full_years.merge(annual_flows, on="year", how="left")
bri_panel["bri_flows_annual"] = bri_panel["bri_flows_annual"].fillna(0.0)

# Cumulative flows (absorb commitment year)
bri_panel["bri_flows_cumulative"] = bri_panel["bri_flows_annual"].cumsum()

# BRI intensity: log1p of cumulative nominal USD committed
bri_panel["bri_intensity"] = np.log1p(bri_panel["bri_flows_cumulative"])

# Post-BRI dummy (2014+; 2013 announcement year coded 0)
bri_panel["post_bri_2013"] = (bri_panel["year"] >= 2014).astype(int)

# Years since BRI announcement
bri_panel["years_since_announcement"] = bri_panel["year"].apply(
    lambda y: max(0, y - 2013)
)

bri_panel.to_csv(PROC / "bri_intensity_annual.csv", index=False)

print(f"\nSaved bri_intensity_annual.csv: {len(bri_panel)} rows")
print(bri_panel[["year", "bri_flows_annual", "bri_flows_cumulative",
                  "bri_intensity", "post_bri_2013"]].to_string(index=False))

# -----------------------------------------------------------------------
# 5. Summary stats
# -----------------------------------------------------------------------
oda_total  = kaz_agg[kaz_agg["Flow Class"] == "ODA-like"]["amount_usd"].sum()
oof_total  = kaz_agg[kaz_agg["Flow Class"] == "OOF-like"]["amount_usd"].sum()
print(f"\nTotal ODA-like committed to KAZ (nominal): ${oda_total/1e6:.1f}M")
print(f"Total OOF-like committed to KAZ (nominal): ${oof_total/1e6:.1f}M")
print(f"Grand total: ${(oda_total + oof_total)/1e6:.1f}M")
