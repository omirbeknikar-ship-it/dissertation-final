"""
33_multi_partner_panel.py
Build a multi-partner bilateral trade panel for Kazakhstan.

Attempts to pull IMF DOTS bilateral trade data for Kazakhstan vs.
China, Russia, EU (Germany proxy), Uzbekistan, Turkey, USA.
Falls back gracefully if the network is unavailable.

If the IMF DOTS API is reachable:
  - Fetches annual bilateral exports and imports (2000-2023)
  - Stacks into long format: partner x year x {exports, imports, balance, balance_ratio}
  - Saves to Collected_Raw_Data/kz_multi_partner_panel.csv

If the API is unreachable:
  - Loads the existing Kazakhstan-China panel (the only local bilateral data)
  - Saves a single-partner panel with [DATA_GAP] flags
  - Documents the gap for KNOWN_ISSUES.md

The multi-partner panel is used by Script 34 for the DiD partner-placebo design.
"""

import warnings
warnings.filterwarnings("ignore")

import json
import time
import pandas as pd
import numpy as np
from pathlib import Path

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False

ROOT = Path(__file__).parent.parent
PANEL_PATH = ROOT / "Collected_Raw_Data" / "clean_panel_annual.csv"
OUT_PATH = ROOT / "Collected_Raw_Data" / "kz_multi_partner_panel.csv"
TABLES = ROOT / "Outputs" / "generated_tables"
TABLES.mkdir(parents=True, exist_ok=True)

# IMF DOTS API configuration
DOTS_BASE = "https://dataservices.imf.org/REST/SDMX_JSON.svc/CompactData/DOT"
PARTNERS = {
    "CHN": "China",
    "RUS": "Russia",
    "DEU": "Germany (EU proxy)",
    "UZB": "Uzbekistan",
    "TUR": "Turkey",
    "USA": "USA",
}
REPORTER = "KZ"
START_YEAR = 2000
END_YEAR = 2023


def fetch_dots_bilateral(reporter, partner_code, flow, start, end, timeout=20):
    """
    Fetch IMF DOTS bilateral annual data.
    flow: 'TXG_FOB_USD' (exports) or 'TMG_CIF_USD' (imports)
    Returns a dict {year: value_usd} or None on failure.
    """
    url = (f"{DOTS_BASE}/A.{reporter}.{flow}.{partner_code}."
           f"?startPeriod={start}&endPeriod={end}")
    try:
        r = requests.get(url, timeout=timeout)
        if r.status_code != 200:
            return None
        data = r.json()
        obs = (data.get("CompactData", {})
                   .get("DataSet", {})
                   .get("Series", {})
                   .get("Obs", []))
        if isinstance(obs, dict):
            obs = [obs]
        result = {}
        for o in obs:
            yr = int(o.get("@TIME_PERIOD", 0))
            val = o.get("@OBS_VALUE")
            if val is not None:
                result[yr] = float(val) * 1e6  # IMF DOTS values are in millions USD
        return result
    except Exception:
        return None


def load_kz_china_fallback():
    """Load existing Kazakhstan-China panel as single-partner fallback."""
    df = pd.read_csv(PANEL_PATH)
    df = df[df["year"].between(START_YEAR, END_YEAR)].copy()
    df["partner_code"] = "CHN"
    df["partner_name"] = "China"
    df["exports_usd"] = df["exports_kazakhstan_to_china_usd"]
    df["imports_usd"] = df["imports_kazakhstan_from_china_usd"]
    df["balance_usd"] = df["trade_balance_usd"]
    df["balance_ratio"] = df["trade_balance_ratio"]
    return df[["year", "partner_code", "partner_name",
               "exports_usd", "imports_usd", "balance_usd", "balance_ratio"]]


# ── Main ─────────────────────────────────────────────────────────────────────
rows = []
network_available = False

if REQUESTS_AVAILABLE:
    print("Attempting IMF DOTS API pulls...")
    test_result = fetch_dots_bilateral(REPORTER, "CHN", "TXG_FOB_USD", 2020, 2023, timeout=15)
    if test_result:
        network_available = True
        print(f"  Network available — test pull returned {len(test_result)} observations")
    else:
        print("  [DATA_GAP] IMF DOTS API unreachable (network timeout or blocked)")

if network_available:
    for partner_code, partner_name in PARTNERS.items():
        print(f"  Fetching KZ exports → {partner_name}...", end=" ")
        exports = fetch_dots_bilateral(REPORTER, partner_code, "TXG_FOB_USD",
                                       START_YEAR, END_YEAR)
        time.sleep(1)
        print(f"  Fetching KZ imports ← {partner_name}...", end=" ")
        imports_ = fetch_dots_bilateral(REPORTER, partner_code, "TMG_CIF_USD",
                                        START_YEAR, END_YEAR)
        time.sleep(1)

        if exports is None and imports_ is None:
            print(f"[DATA_GAP] Both flows missing for {partner_name}")
            continue

        all_years = sorted(set(list((exports or {}).keys()) +
                               list((imports_ or {}).keys())))
        for yr in all_years:
            x = (exports or {}).get(yr, np.nan)
            m = (imports_ or {}).get(yr, np.nan)
            bal = x - m if not (np.isnan(x) or np.isnan(m)) else np.nan
            ratio = bal / (x + m) if not np.isnan(bal) and (x + m) > 0 else np.nan
            rows.append({
                "year": yr, "partner_code": partner_code,
                "partner_name": partner_name,
                "exports_usd": x, "imports_usd": m,
                "balance_usd": bal, "balance_ratio": ratio
            })
        print(f"OK ({len(all_years)} years)")

    panel = pd.DataFrame(rows)
else:
    print("[DATA_GAP] Using Kazakhstan-China single-partner fallback.")
    print("  For full multi-partner DiD, run this script with network access.")
    panel = load_kz_china_fallback()
    panel["data_source"] = "local_panel"
    panel["network_gap_flag"] = True

panel = panel.sort_values(["partner_code", "year"]).reset_index(drop=True)
panel.to_csv(OUT_PATH, index=False)

print(f"\nMulti-partner panel saved: {OUT_PATH}")
print(f"  Partners: {panel['partner_code'].unique().tolist()}")
print(f"  Years: {panel['year'].min()} - {panel['year'].max()}")
print(f"  Rows: {len(panel)}")
print(panel.head(5).to_string())

# ── Summary statistics by partner ───────────────────────────────────────────
summary = panel.groupby("partner_code").agg(
    n_years=("year", "count"),
    mean_balance_ratio=("balance_ratio", "mean"),
    pre_bri_balance=("balance_ratio", lambda x: x[panel.loc[x.index, "year"] < 2014].mean()),
    post_bri_balance=("balance_ratio", lambda x: x[panel.loc[x.index, "year"] >= 2014].mean()),
).reset_index()
summary["change_pp"] = summary["post_bri_balance"] - summary["pre_bri_balance"]
print("\nPre vs Post BRI balance ratio by partner:")
print(summary.to_string(index=False))

summary_path = TABLES / "multi_partner_summary.csv"
summary.to_csv(summary_path, index=False)
print(f"\nSummary saved: {summary_path}")
