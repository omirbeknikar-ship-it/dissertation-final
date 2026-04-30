"""
13_synthetic_control.py
Phase 2 - Synthetic control feasibility check.

Requested design:
  Treated = Kazakhstan; donors = Uzbekistan, Turkmenistan, Mongolia,
  Azerbaijan, Kyrgyzstan, Georgia, Armenia; pre = 2000-2012;
  post = 2013-2024; outcome = bilateral trade balance with China.

Result:
  The donor-pool bilateral trade-balance-with-China series are not present
  in local files. The Kazakhstan reporter Comtrade file is a 2014-2024
  HS-2/aggregate snapshot, so it also cannot support a within-country ROW placebo over
  2000-2023. Per the hard rules, this script writes explicit DECISION NEEDED
  outputs instead of fabricating donor or placebo series.

Outputs:
  Outputs/generated_tables/synthetic_control_status.csv
  Outputs/generated_tables/within_country_placebo.csv
  Outputs/generated_figures/fig08_synthetic_control_status.png
"""

import warnings
warnings.filterwarnings("ignore")

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).parent.parent
PANEL = ROOT / "Collected_Raw_Data" / "clean_panel_annual.csv"
RAW = ROOT / "Collected_Raw_Data" / "raw_downloads"
TABLES = ROOT / "Outputs" / "generated_tables"
FIGS = ROOT / "Outputs" / "generated_figures"
TABLES.mkdir(parents=True, exist_ok=True)
FIGS.mkdir(parents=True, exist_ok=True)

panel = pd.read_csv(PANEL)
panel = panel[panel["year"] < 2024].dropna(subset=["trade_balance_usd"]).copy()

donors = [
    "Uzbekistan",
    "Turkmenistan",
    "Mongolia",
    "Azerbaijan",
    "Kyrgyzstan",
    "Georgia",
    "Armenia",
]

kaz_raw_years = []
try:
    kaz_raw = pd.read_csv(RAW / "comtrade_kaz_reporter.csv", low_memory=False, index_col=False)
    kaz_raw_years = [int(x) for x in sorted(pd.to_numeric(kaz_raw["refYear"], errors="coerce").dropna().astype(int).unique())]
except Exception:
    kaz_raw_years = []

reason = (
    "Synthetic control skipped: donor-pool countries' bilateral trade-balance-with-China "
    "series are not available in local raw files. Within-country ROW placebo also skipped: "
    f"KAZ reporter Comtrade years available after correct parsing = {kaz_raw_years}, "
    "not a 2000-2023 panel."
)

status = pd.DataFrame([{
    "method": "synthetic_control",
    "status": "DECISION NEEDED - skipped",
    "treated_unit": "Kazakhstan",
    "donor_pool_requested": "; ".join(donors),
    "pre_period": "2000-2012",
    "post_period": "2013-2023 in available clean panel; 2024 trade balance missing",
    "outcome": "trade_balance_usd",
    "mspe_ratio": np.nan,
    "placebo_permutation": "not estimated",
    "reason": reason,
    "known_issue": "KNOWN_ISSUES.md ISSUE-005 and ISSUE-001",
}])
status.to_csv(TABLES / "synthetic_control_status.csv", index=False)

placebo_status = pd.DataFrame([{
    "test": "Within-country placebo fallback from script 13",
    "status": "DECISION NEEDED - skipped",
    "did_coef": np.nan,
    "did_pval": np.nan,
    "did_se": np.nan,
    "n_obs": 0,
    "note": reason,
}])
placebo_status.to_csv(TABLES / "within_country_placebo.csv", index=False)

fig, ax = plt.subplots(figsize=(9, 4.5))
ax.plot(
    panel["year"],
    panel["trade_balance_usd"] / 1e9,
    color="#2166AC",
    marker="o",
    markersize=4,
    label="Observed KAZ-CHN trade balance",
)
ax.axvline(2013.5, color="#666666", linestyle="--", label="BRI 2013")
ax.axhline(0, color="black", linewidth=0.7)
ax.set_xlabel("Year")
ax.set_ylabel("USD billion")
ax.set_title("Synthetic Control Not Estimated: Donor Series Unavailable")
ax.text(
    2000.2,
    panel["trade_balance_usd"].min() / 1e9,
    "DECISION NEEDED: donor bilateral series absent; no synthetic gap/MSPE computed.",
    fontsize=8,
    color="#333333",
)
ax.legend(fontsize=8)
fig.tight_layout()
fig.savefig(FIGS / "fig08_synthetic_control_status.png", dpi=150)
plt.close(fig)

print("=" * 72)
print("DECISION NEEDED: synthetic control skipped")
print(reason)
print("Saved Outputs/generated_tables/synthetic_control_status.csv")
print("Saved Outputs/generated_tables/within_country_placebo.csv")
print("Saved Outputs/generated_figures/fig08_synthetic_control_status.png")
print("Done: 13_synthetic_control.py")
