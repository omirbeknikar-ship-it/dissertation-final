"""
01b_load_prices.py
Phase 1 — Load commodity price data.

Sources:
  - World Bank Pink Sheet (Monthly Prices sheet): Brent crude oil (col 2),
    Copper LME (col 64), 1960M01–2026M03. Primary source for 2000–2023.
  - FRED DCOILBRENTEU.csv: Daily Brent, April 2021–2025. Used for validation.

Output: Collected_Raw_Data/processed/prices_annual.csv
Columns: year, brent_annual_mean, copper_annual_mean, brent_source
"""

import pandas as pd
import numpy as np
import openpyxl
from pathlib import Path

ROOT = Path(__file__).parent.parent
RAW  = ROOT / "Collected_Raw_Data" / "raw_downloads"
PROC = ROOT / "Collected_Raw_Data" / "processed"
PROC.mkdir(parents=True, exist_ok=True)

# -----------------------------------------------------------------------
# 1. Parse Pink Sheet Monthly Prices
# -----------------------------------------------------------------------
wb = openpyxl.load_workbook(
    str(RAW / "pink_sheet.xlsx"), read_only=True, data_only=True
)
ws = wb["Monthly Prices"]
rows = list(ws.iter_rows(values_only=True))

# Row index 4 (0-based) = column headers (row 5 in Excel)
# Row index 5 = units
# Row index 6 = first data row (1960M01)
headers = rows[4]
units   = rows[5]

# Identify relevant columns
COL_DATE   = 0   # Date (e.g. 1960M01)
COL_BRENT  = 2   # "Crude oil, Brent"  (0-based index 2)
COL_COPPER = 64  # "Copper"            (0-based index 64)

print(f"Brent column header: {headers[COL_BRENT]} | units: {units[COL_BRENT]}")
print(f"Copper column header: {headers[COL_COPPER]} | units: {units[COL_COPPER]}")

data_rows = rows[6:]  # first data row = 1960M01

records = []
for row in data_rows:
    date_str = row[COL_DATE]
    if date_str is None:
        continue
    date_str = str(date_str).strip()
    if not date_str:
        continue
    # Format: YYYYMXX where XX is month (01-12)
    try:
        year  = int(date_str[:4])
        month = int(date_str[5:])
    except (ValueError, IndexError):
        continue

    brent  = row[COL_BRENT]  if COL_BRENT  < len(row) else None
    copper = row[COL_COPPER] if COL_COPPER < len(row) else None

    records.append({
        "year":   year,
        "month":  month,
        "brent":  float(brent)  if brent  is not None and str(brent).strip() else np.nan,
        "copper": float(copper) if copper is not None and str(copper).strip() else np.nan,
    })

monthly_df = pd.DataFrame(records)
print(f"\nPink Sheet monthly records: {len(monthly_df)} "
      f"({monthly_df['year'].min()}–{monthly_df['year'].max()})")

# Annual means
annual_pink = (
    monthly_df.groupby("year")
    .agg(brent_annual_mean=("brent", "mean"), copper_annual_mean=("copper", "mean"))
    .reset_index()
    .assign(brent_source="PinkSheet_Monthly")
)

# -----------------------------------------------------------------------
# 2. Parse FRED Brent (daily → annual mean, validation)
# -----------------------------------------------------------------------
fred = pd.read_csv(RAW / "brent_daily.csv")
fred.columns = fred.columns.str.strip()
fred["date"] = pd.to_datetime(fred["observation_date"], errors="coerce")
fred["year"] = fred["date"].dt.year
fred["brent_fred"] = pd.to_numeric(fred.iloc[:, 1], errors="coerce")

fred_annual = (
    fred.dropna(subset=["year", "brent_fred"])
    .groupby("year")["brent_fred"]
    .mean()
    .reset_index()
    .rename(columns={"brent_fred": "brent_fred_annual"})
)
print(f"\nFRED Brent annual coverage: {fred_annual['year'].min()}–{fred_annual['year'].max()}")

# -----------------------------------------------------------------------
# 3. Merge: use Pink Sheet as primary, FRED for validation
# -----------------------------------------------------------------------
prices_annual = (
    annual_pink.merge(fred_annual, on="year", how="left")
    .query("year >= 2000")
    .reset_index(drop=True)
)

# Validate Pink Sheet vs FRED for overlapping years (2021+)
overlap = prices_annual.dropna(subset=["brent_annual_mean", "brent_fred_annual"])
if len(overlap) > 0:
    corr = overlap[["brent_annual_mean", "brent_fred_annual"]].corr().iloc[0, 1]
    mae  = (overlap["brent_annual_mean"] - overlap["brent_fred_annual"]).abs().mean()
    print(f"\nPink Sheet vs FRED validation (n={len(overlap)}):")
    print(f"  Correlation: {corr:.4f}")
    print(f"  MAE: ${mae:.2f}/bbl")

# Drop FRED column (validation only) and save
prices_annual = prices_annual[["year", "brent_annual_mean", "copper_annual_mean",
                                "brent_source"]].copy()

prices_annual.to_csv(PROC / "prices_annual.csv", index=False)
print(f"\nSaved prices_annual.csv: {len(prices_annual)} rows")
print(prices_annual[["year", "brent_annual_mean", "copper_annual_mean"]].to_string(index=False))
