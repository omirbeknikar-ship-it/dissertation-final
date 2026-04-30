"""
14_did_placebo.py
Phase 2 - Within-country placebo DiD feasibility check.

Requested design:
  KAZ's trade balance with China (treated) vs KAZ's trade balance with
  Russia, EU, and Turkey (placebos), two-way FE + Driscoll-Kraay SE, event
  study with 2013 reference.

Result:
  Local raw files do not contain Russia, EU, Turkey, or Rest-of-World annual
  bilateral trade-balance panels. The available Kazakhstan Comtrade reporter
  file is a 2014-2024 HS-2/aggregate snapshot after correct parsing. This script writes
  an explicit skipped-status table and a descriptive event-time plot for the
  China series only. No DiD estimate is reported.

Outputs:
  Outputs/generated_tables/did_event_study.csv
  Outputs/generated_tables/did_placebo_status.csv
  Outputs/generated_figures/fig09_event_study.png
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
panel["event_time"] = panel["year"] - 2013
panel["china_balance_B"] = panel["trade_balance_usd"] / 1e9

kaz_raw_years = []
available_partners = []
try:
    kaz_raw = pd.read_csv(RAW / "comtrade_kaz_reporter.csv", low_memory=False, index_col=False)
    kaz_raw_years = [int(x) for x in sorted(pd.to_numeric(kaz_raw["refYear"], errors="coerce").dropna().astype(int).unique())]
    available_partners = sorted(kaz_raw["partnerDesc"].dropna().astype(str).unique())
except Exception:
    kaz_raw_years = []
    available_partners = []

reason = (
    "Within-country placebo DiD skipped: local files do not contain annual "
    "KAZ-Russia, KAZ-EU, KAZ-Turkey, or KAZ-ROW bilateral trade-balance panels. "
    f"Correctly parsed KAZ Comtrade years = {kaz_raw_years}; partners = {available_partners}."
)

event_df = panel[["year", "event_time", "china_balance_B"]].copy()
event_df["placebo_balance_B"] = np.nan
event_df["gap_B"] = np.nan
event_df["status"] = "descriptive_china_only_no_placebo"
event_df.to_csv(TABLES / "did_event_study.csv", index=False)

status = pd.DataFrame([{
    "method": "within_country_placebo_did",
    "status": "DECISION NEEDED - skipped",
    "requested_placebos": "Russia; EU; Turkey",
    "twoway_fe": "not estimated",
    "driscoll_kraay_se": "not estimated",
    "event_study": "descriptive China-only plot saved; no placebo coefficients",
    "did_coef": np.nan,
    "did_pval": np.nan,
    "n_obs": 0,
    "reason": reason,
    "known_issue": "KNOWN_ISSUES.md ISSUE-005 and ISSUE-001",
}])
status.to_csv(TABLES / "did_placebo_status.csv", index=False)

fig, ax = plt.subplots(figsize=(9, 4.5))
colors = ["#2166AC" if t < 0 else "#D6604D" for t in event_df["event_time"]]
ax.bar(event_df["event_time"], event_df["china_balance_B"], color=colors, width=0.8)
ax.axhline(0, color="black", linewidth=0.7)
ax.axvline(-0.5, color="#666666", linestyle="--", label="BRI announcement (2013)")
ax.set_xlabel("Event time (years relative to 2013)")
ax.set_ylabel("KAZ-CHN trade balance, USD billion")
ax.set_title("Event-Time Descriptive Series Only: Placebo Partners Unavailable")
ax.text(
    event_df["event_time"].min(),
    event_df["china_balance_B"].min(),
    "No DiD coefficient estimated: Russia/EU/Turkey annual local series absent.",
    fontsize=8,
    color="#333333",
)
ax.legend(fontsize=8)
fig.tight_layout()
fig.savefig(FIGS / "fig09_event_study.png", dpi=150)
plt.close(fig)

print("=" * 72)
print("DECISION NEEDED: within-country placebo DiD skipped")
print(reason)
print("Saved Outputs/generated_tables/did_event_study.csv")
print("Saved Outputs/generated_tables/did_placebo_status.csv")
print("Saved Outputs/generated_figures/fig09_event_study.png")
print("Done: 14_did_placebo.py")
