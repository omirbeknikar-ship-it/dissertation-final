"""
01c_load_wdi.py
Phase 1 — Load World Development Indicators for KAZ and CHN.

Sources (in order of preference):
  1. Existing processed CSVs in Collected_Raw_Data/raw/ (KAZ GDP available)
  2. wbdata Python package (no API key needed) for KAZ + CHN data

Indicators pulled:
  NY.GDP.MKTP.KD  — GDP constant 2015 USD (KAZ + CHN)
  PA.NUS.FCRF     — Official exchange rate KZT/USD (KAZ)
  FP.CPI.TOTL     — CPI 2010=100 (KAZ + CHN)

Output: Collected_Raw_Data/processed/wdi_annual.csv
"""

import pandas as pd
import numpy as np
from pathlib import Path

ROOT = Path(__file__).parent.parent
RAW  = ROOT / "Collected_Raw_Data" / "raw"
PROC = ROOT / "Collected_Raw_Data" / "processed"
PROC.mkdir(parents=True, exist_ok=True)

# -----------------------------------------------------------------------
# 1. Load existing KAZ GDP CSV
# -----------------------------------------------------------------------
existing_wdi = pd.read_csv(ROOT / "Collected_Raw_Data" / "clean" /
                            "kazakhstan_china_trade_panel.csv")
kaz_gdp_existing = existing_wdi[["year", "gdp_kazakhstan_current_usd"]].copy()

# -----------------------------------------------------------------------
# 2. Try wbdata package for additional indicators
# -----------------------------------------------------------------------
INDICATORS = {
    "NY.GDP.MKTP.KD": "gdp_const2015_usd",
    "PA.NUS.FCRF":    "kzt_usd",
    "FP.CPI.TOTL":    "cpi",
}

COUNTRIES = {"KAZ": "Kazakhstan", "CHN": "China"}

wdi_records = []
wbdata_available = False

try:
    import urllib.request, json, warnings
    warnings.filterwarnings("ignore")
    BASE = "https://api.worldbank.org/v2/country/{iso}/indicator/{ind}?date=2000:2024&format=json&per_page=100"
    all_fetched = {}
    for iso in COUNTRIES:
        all_fetched[iso] = {}
        for ind_code, col_name in INDICATORS.items():
            url = BASE.format(iso=iso, ind=ind_code)
            with urllib.request.urlopen(url, timeout=15) as resp:
                data = json.load(resp)
            if len(data) < 2:
                continue
            for entry in data[1]:
                yr = int(entry["date"])
                val = entry["value"]
                all_fetched[iso].setdefault(yr, {})[col_name] = float(val) if val is not None else np.nan
    if all_fetched:
        wbdata_available = True
        for iso in COUNTRIES:
            rows_iso = [{"year": y, "country_iso": iso, **v}
                        for y, v in sorted(all_fetched[iso].items())]
            wdi_records.append(pd.DataFrame(rows_iso))
        print("World Bank API fetch succeeded")
except Exception as e:
    print(f"World Bank API fetch failed: {e}")

# -----------------------------------------------------------------------
# 3. Build WDI table from available data
# -----------------------------------------------------------------------
if wbdata_available and wdi_records:
    combined = pd.concat(wdi_records, ignore_index=True)
    combined["year"] = pd.DatetimeIndex(combined["date"]).year
    wdi_long = combined.rename(columns={v: v for v in INDICATORS.values()})

    kaz_wdi = combined[combined["country_iso"] == "KAZ"][
        ["year", "gdp_const2015_usd", "kzt_usd", "cpi"]
    ].rename(columns={"cpi": "kz_cpi", "gdp_const2015_usd": "kz_gdp"})

    chn_wdi = combined[combined["country_iso"] == "CHN"][
        ["year", "gdp_const2015_usd", "cpi"]
    ].rename(columns={"cpi": "cn_cpi", "gdp_const2015_usd": "cn_gdp"})

    wdi_out = kaz_wdi.merge(chn_wdi, on="year", how="outer")

else:
    # Fallback: use existing panel data (has KAZ GDP current USD)
    # Construct constant-USD proxy using CPI deflation (approximate)
    # Note: existing GDP is in current USD, not constant 2015 USD
    wdi_out = existing_wdi[["year", "gdp_kazakhstan_current_usd"]].rename(
        columns={"gdp_kazakhstan_current_usd": "kz_gdp_current_usd"}
    ).copy()
    wdi_out["kz_gdp"]    = np.nan  # constant USD not available without wbdata
    wdi_out["cn_gdp"]    = np.nan
    wdi_out["kzt_usd"]   = np.nan
    wdi_out["kz_cpi"]    = np.nan
    wdi_out["cn_cpi"]    = np.nan

# Fill kz_gdp with current USD if constant not available
if "kz_gdp_current_usd" not in wdi_out.columns and "kz_gdp" in wdi_out.columns:
    wdi_out["kz_gdp_current_usd"] = np.nan

# Merge existing current-USD GDP for reference
wdi_out = wdi_out.merge(
    kaz_gdp_existing.rename(columns={"gdp_kazakhstan_current_usd": "kz_gdp_current_usd_panel"}),
    on="year", how="left"
)

# Use panel current-USD as fallback for kz_gdp where constant unavailable
mask_kz_missing = wdi_out.get("kz_gdp", pd.Series(np.nan)).isna()
if mask_kz_missing.any():
    wdi_out["kz_gdp"] = wdi_out.get("kz_gdp", pd.Series(np.nan)).fillna(
        wdi_out["kz_gdp_current_usd_panel"]
    )

wdi_out = wdi_out.query("year >= 2000").sort_values("year").reset_index(drop=True)
wdi_out.to_csv(PROC / "wdi_annual.csv", index=False)
print(f"\nSaved wdi_annual.csv: {len(wdi_out)} rows")
print(wdi_out[["year", "kz_gdp", "cn_gdp", "kzt_usd", "kz_cpi"]].to_string(index=False))
print(f"\nNote: cn_gdp = {'available' if wdi_out['cn_gdp'].notna().any() else 'MISSING (wbdata unavailable)'}")
print(f"      kzt_usd = {'available' if 'kzt_usd' in wdi_out and wdi_out['kzt_usd'].notna().any() else 'MISSING'}")
