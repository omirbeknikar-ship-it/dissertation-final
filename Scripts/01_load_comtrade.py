"""
01_load_comtrade.py
Phase 1 — Load and process Comtrade bilateral trade data.

DATA NOTE: The provided Comtrade files cover 2014–2024 at HS-2 chapter level
(not HS-6). Column names in the raw CSVs are shifted by one position due to
export format quirk; the correct mappings are noted below.

Column mapping (as-read → actual meaning):
  refPeriodId → calendar year (2014, 2015, ...)
  cifvalue    → trade value in USD (reporter convention)
  partnerISO  → partner description ("China", "World")
  flowCode    → flow direction ("Export", "Import")
  cmdCode     → HS chapter description (text)

minerals_narrow (HS-2 proxy): HS 26 (ores/slag) + HS 28 (inorganic chem / uranium / rare earths)
minerals_broad  (HS-2 proxy): narrow + HS 74 (copper) + HS 78 (lead) + HS 79 (zinc) + HS 81 (misc metals)
oil_exports:    HS 27 not present in files; left as NaN (see KNOWN_ISSUES.md ISSUE-001)

For 2000–2013 (pre-Comtrade coverage), WITS ores/metals proxy is appended.
"""

import pandas as pd
import numpy as np
from pathlib import Path

ROOT = Path(__file__).parent.parent
RAW  = ROOT / "Collected_Raw_Data" / "raw_downloads"
PROC = ROOT / "Collected_Raw_Data" / "processed"
PROC.mkdir(parents=True, exist_ok=True)

# HS-2 chapter descriptions that map to our mineral baskets
NARROW_CHAPTERS = {
    "Ores, slag and ash",   # HS 26: uranium, copper, chromium, zinc, lead, titanium ores
    "Inorganic chemicals; organic and inorganic compounds of precious metals; "
    "of rare earth metals, of radio-active elements and of isotopes",  # HS 28
}
BROAD_CHAPTERS = NARROW_CHAPTERS | {
    "Copper and articles thereof",          # HS 74
    "Lead and articles thereof",            # HS 78
    "Zinc and articles thereof",            # HS 79
    "Metals; n.e.c., cermets and articles thereof",  # HS 81 (includes titanium)
}
TOTAL_CHAPTER = "All Commodities"


def load_comtrade_file(path: Path, reporter_label: str) -> pd.DataFrame:
    """Load one Comtrade bilateral CSV and return a tidy annual chapter table."""
    raw = pd.read_csv(path, low_memory=False)
    raw.columns = [c.strip() for c in raw.columns]

    # Rename shifted columns to their actual meanings
    raw = raw.rename(columns={
        "refPeriodId": "year",         # actual calendar year
        "cifvalue":    "trade_value",  # actual USD trade value
        "partnerISO":  "partner",      # "China" or "World"
        "flowCode":    "flow",         # "Export" or "Import"
        "cmdCode":     "chapter",      # HS chapter description
    })

    # Bilateral filter
    bilateral = raw[raw["partner"] == "China"].copy()
    bilateral["reporter"] = reporter_label
    bilateral["trade_value"] = pd.to_numeric(bilateral["trade_value"], errors="coerce")

    print(f"{reporter_label} file: {len(raw)} rows → bilateral China: {len(bilateral)} rows "
          f"| years: {sorted(bilateral['year'].dropna().astype(int).unique())}")

    return bilateral[["reporter", "year", "flow", "chapter", "trade_value"]]


# -----------------------------------------------------------------------
# 1. Load both reporters
# -----------------------------------------------------------------------
kaz = load_comtrade_file(RAW / "comtrade_kaz_reporter.csv", "KAZ")
chn = load_comtrade_file(RAW / "comtrade_chn_reporter.csv", "CHN")

# KAZ reporter: Export flow = KAZ→CHN (FOB); Import flow = CHN→KAZ
# CHN reporter: Import flow from KAZ = mirror of KAZ exports
kaz_exports = kaz[kaz["flow"] == "Export"].copy()
chn_imports = chn[chn["flow"] == "Import"].copy()

# -----------------------------------------------------------------------
# 2. Build annual minerals series from KAZ reporter (primary source)
#    Note: CHN reporter file contains CHN→KAZ exports (not CHN imports from KAZ).
#    CHN import rows are all zero. KAZ-reported exports are used as primary series.
#    See mirror reconciliation memo (02_mirror_reconcile.py) for full documentation.
# -----------------------------------------------------------------------
def build_annual_minerals(df: pd.DataFrame, label: str) -> pd.DataFrame:
    rows = []
    if df.empty:
        return pd.DataFrame(columns=["year", f"total_{label}",
                                     f"minerals_narrow_{label}", f"minerals_broad_{label}"])
    for yr, grp in df.groupby("year"):
        chap_vals = grp.set_index("chapter")["trade_value"]
        total  = chap_vals.get(TOTAL_CHAPTER, np.nan)
        narrow = sum(chap_vals.get(c, 0) for c in NARROW_CHAPTERS)
        broad  = sum(chap_vals.get(c, 0) for c in BROAD_CHAPTERS)
        rows.append({
            "year": int(yr),
            f"total_{label}":             total,
            f"minerals_narrow_{label}":   narrow,
            f"minerals_broad_{label}":    broad,
        })
    return pd.DataFrame(rows).sort_values("year").reset_index(drop=True)

kaz_ann = build_annual_minerals(kaz_exports, "kaz")

# CHN reporter: build from CHN EXPORTS to KAZ (the only non-zero bilateral flow)
# This gives CHN→KAZ direction (useful for import-side mirror, labeled accordingly)
chn_to_kaz = chn[chn["flow"] == "Export"].copy()  # CHN exports to KAZ = CHN→KAZ
chn_ann    = build_annual_minerals(chn_to_kaz, "chn_exports_to_kaz")

print("\nKAZ-reported annual minerals (2014–2024):")
print(kaz_ann.to_string(index=False))
print("\nCHN-reported annual minerals (2014–2024):")
print(chn_ann.to_string(index=False))

# -----------------------------------------------------------------------
# 3. Merge the two reporter series and compute ratios
# -----------------------------------------------------------------------
merged = pd.merge(kaz_ann, chn_ann, on="year", how="outer")
# ratio: CHN's exports to KAZ vs KAZ's exports to CHN (note: different directions)
merged.to_csv(PROC / "comtrade_mirror_2014_2024.csv", index=False)

# -----------------------------------------------------------------------
# 4. Build the preferred (KAZ-reported) annual mineral series 2014-2024
# -----------------------------------------------------------------------
kaz_series = kaz_ann.rename(columns={
    "total_kaz":            "exports_kaz_to_chn_comtrade",
    "minerals_narrow_kaz":  "minerals_narrow_comtrade",
    "minerals_broad_kaz":   "minerals_broad_comtrade",
})
chn_series = kaz_series  # alias for downstream
chn_series["oil_exports"] = np.nan   # HS 27 not in files
chn_series["data_source"] = "Comtrade_CHN_HS2"

# -----------------------------------------------------------------------
# 5. Append WITS proxy for 2000–2013 (pre-Comtrade coverage)
# -----------------------------------------------------------------------
wits_raw   = pd.read_csv(ROOT / "Collected_Raw_Data" / "raw" /
                          "wits_ores_metals_exports_kazakhstan_china.csv")
wits_total = pd.read_csv(ROOT / "Collected_Raw_Data" / "raw" /
                          "wits_total_trade_kazakhstan_china.csv")

minerals_wits = (
    wits_raw[wits_raw["indicator"] == "XPRT-TRD-VL"]
    .assign(year=lambda d: d["year"].astype(int),
            minerals_proxy=lambda d: d["value_usd_thousand"].astype(float) * 1000)
    [["year", "minerals_proxy"]]
)
total_wits = (
    wits_total[wits_total["indicator"] == "XPRT-TRD-VL"]
    .assign(year=lambda d: d["year"].astype(int),
            exports_wits=lambda d: d["value_usd_thousand"].astype(float) * 1000)
    [["year", "exports_wits"]]
)

wits_pre2014 = (
    minerals_wits.merge(total_wits, on="year")
    .query("year >= 2000 and year < 2014")
    .rename(columns={
        "minerals_proxy":  "minerals_narrow_comtrade",
        "exports_wits":    "exports_kaz_to_chn_comtrade",
    })
    .assign(
        minerals_broad_comtrade=lambda d: d["minerals_narrow_comtrade"],
        oil_exports=np.nan,
        data_source="WITS_PROXY",
    )
    [["year", "exports_kaz_to_chn_comtrade", "minerals_narrow_comtrade",
      "minerals_broad_comtrade", "oil_exports", "data_source"]]
)

# Combine WITS 2000-2013 with Comtrade 2014-2024
minerals_annual = (
    pd.concat([wits_pre2014, chn_series], ignore_index=True)
    .sort_values("year")
    .query("year >= 2000")
    .reset_index(drop=True)
)

minerals_annual.to_csv(PROC / "comtrade_minerals_annual.csv", index=False)
print(f"\nSaved comtrade_minerals_annual.csv: {len(minerals_annual)} rows "
      f"({minerals_annual['year'].min()}–{minerals_annual['year'].max()})")
print(minerals_annual[["year", "minerals_narrow_comtrade",
                        "minerals_broad_comtrade", "data_source"]].to_string(index=False))
