"""
10_descriptives.py
Phase 2 — Descriptive statistics, stationarity tests, and time-series plots.

Outputs:
  Outputs/generated_tables/stationarity.csv
  Outputs/generated_tables/summary_stats_pre_post.csv
  Outputs/generated_figures/fig01_trade_balance.png
  Outputs/generated_figures/fig02_minerals_brent.png
  Outputs/generated_figures/fig03_bri_intensity.png
  Outputs/generated_figures/fig04_facet_panel.png
"""

import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from pathlib import Path
from statsmodels.tsa.stattools import adfuller, kpss
import statsmodels.api as sm
try:
    from arch.unitroot import PhillipsPerron
except ImportError:  # recorded in stationarity.csv if the dependency is absent
    PhillipsPerron = None

ROOT   = Path(__file__).parent.parent
PANEL  = ROOT / "Collected_Raw_Data" / "clean_panel_annual.csv"
TABLES = ROOT / "Outputs" / "generated_tables"
FIGS   = ROOT / "Outputs" / "generated_figures"
TABLES.mkdir(parents=True, exist_ok=True)
FIGS.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(PANEL)
df_reg = df[df["year"] < 2024].copy()   # exclude 2024 (trade balance missing)

# -----------------------------------------------------------------------
# 1. Summary statistics pre/post BRI
# -----------------------------------------------------------------------
VARS = {
    "trade_balance_usd":   "Trade Balance (USD)",
    "trade_balance_ratio": "Trade Balance Ratio",
    "minerals_narrow":     "Minerals Narrow (USD)",
    "minerals_broad":      "Minerals Broad (USD)",
    "brent_annual_mean":   "Brent Crude (USD/bbl)",
    "copper_annual_mean":  "Copper (USD/mt)",
    "bri_intensity":       "BRI Intensity (log1p)",
    "kz_gdp":              "KAZ GDP constant 2015 (USD)",
}

rows = []
for var, label in VARS.items():
    if var not in df_reg.columns:
        continue
    pre  = df_reg[df_reg["year"] <= 2013][var].dropna()
    post = df_reg[df_reg["year"] >= 2014][var].dropna()
    rows.append({
        "variable":       label,
        "pre_mean":       pre.mean(),
        "pre_sd":         pre.std(),
        "pre_n":          len(pre),
        "post_mean":      post.mean(),
        "post_sd":        post.std(),
        "post_n":         len(post),
        "pct_change_mean": (post.mean() - pre.mean()) / abs(pre.mean()) * 100,
    })

stats_df = pd.DataFrame(rows)
stats_df.to_csv(TABLES / "summary_stats_pre_post.csv", index=False)
print("Summary stats (pre BRI 2000-2013 vs post BRI 2014-2023):")
print(stats_df[["variable", "pre_mean", "post_mean", "pct_change_mean"]].to_string(index=False))

# -----------------------------------------------------------------------
# 2. Stationarity tests: ADF, PP, KPSS
# -----------------------------------------------------------------------
SERIES_TO_TEST = {
    "trade_balance_usd":   "Trade Balance",
    "minerals_narrow":     "Minerals Narrow",
    "brent_annual_mean":   "Brent Crude",
    "copper_annual_mean":  "Copper Price",
    "kz_gdp":              "KAZ GDP",
    "cn_gdp":              "CHN GDP",
    "bri_intensity":       "BRI Intensity",
    "log_minerals_narrow": "log(Minerals Narrow)",
}

stat_results = []
for var, label in SERIES_TO_TEST.items():
    if var not in df_reg.columns:
        continue
    series = df_reg[var].dropna()
    if len(series) < 8:
        continue

    # ADF: H0 = unit root (non-stationary)
    try:
        adf_stat, adf_pval, adf_lags, _, adf_crit, _ = adfuller(series, autolag="AIC")
        adf_conclusion = "I(0)" if adf_pval < 0.05 else "I(1)?"
    except Exception:
        adf_stat, adf_pval, adf_lags, adf_crit, adf_conclusion = [np.nan]*4 + ["ERR"]

    # KPSS: H0 = stationary (trend/level)
    try:
        kpss_stat, kpss_pval, kpss_lags, kpss_crit = kpss(series, regression="ct",
                                                             nlags="auto")
        kpss_conclusion = "I(0)" if kpss_pval > 0.05 else "I(1)?"
    except Exception:
        kpss_stat, kpss_pval, kpss_lags, kpss_crit = [np.nan]*4
        kpss_conclusion = "ERR"

    # Phillips-Perron: H0 = unit root (non-stationary)
    try:
        if PhillipsPerron is None:
            raise ImportError("arch.unitroot.PhillipsPerron unavailable")
        pp = PhillipsPerron(series, trend="ct")
        pp_stat = float(pp.stat)
        pp_pval = float(pp.pvalue)
        pp_lags = int(pp.lags)
        pp_conclusion = "I(0)" if pp_pval < 0.05 else "I(1)?"
    except Exception:
        pp_stat, pp_pval, pp_lags = np.nan, np.nan, np.nan
        pp_conclusion = "ERR"

    # Integration order: consistent if ADF, PP, and KPSS agree
    unit_root_tests_stationary = [adf_conclusion == "I(0)", pp_conclusion == "I(0)"]
    unit_root_tests_nonstationary = [adf_conclusion == "I(1)?", pp_conclusion == "I(1)?"]
    if all(unit_root_tests_stationary) and kpss_conclusion == "I(0)":
        order = "I(0)"
    elif all(unit_root_tests_nonstationary) and kpss_conclusion == "I(1)?":
        order = "I(1)"
    else:
        order = "ambiguous"

    stat_results.append({
        "variable":         label,
        "adf_stat":         round(adf_stat, 4),
        "adf_pval":         round(adf_pval, 4),
        "adf_lags":         int(adf_lags),
        "adf_5pct_crit":    round(adf_crit.get("5%", np.nan), 3),
        "pp_stat":          round(pp_stat, 4),
        "pp_pval":          round(pp_pval, 4),
        "pp_lags":          int(pp_lags) if not np.isnan(pp_lags) else np.nan,
        "kpss_stat":        round(kpss_stat, 4),
        "kpss_pval":        round(kpss_pval, 4),
        "adf_conclusion":   adf_conclusion,
        "pp_conclusion":    pp_conclusion,
        "kpss_conclusion":  kpss_conclusion,
        "integration_order": order,
    })

stat_df = pd.DataFrame(stat_results)
stat_df.to_csv(TABLES / "stationarity.csv", index=False)
print("\nStationarity test results:")
print(stat_df[["variable", "adf_pval", "pp_pval", "kpss_pval", "integration_order"]].to_string(index=False))

# -----------------------------------------------------------------------
# 3. Time series figures
# -----------------------------------------------------------------------
BRI_YEAR = 2013.5   # vertical line between 2013 and 2014

plt.style.use("seaborn-v0_8-whitegrid")
GREY  = "#666666"
BLUE  = "#2166AC"
RED   = "#D6604D"
GREEN = "#4DAC26"

def add_bri_line(ax, label=True):
    ax.axvline(BRI_YEAR, color=GREY, linestyle="--", linewidth=1.2,
               label="BRI 2013" if label else None)

# --- Fig 01: Trade balance ---
fig, ax = plt.subplots(figsize=(9, 4))
ax.bar(df_reg["year"], df_reg["trade_balance_usd"] / 1e9,
       color=[BLUE if y <= 2013 else RED for y in df_reg["year"]], width=0.8)
add_bri_line(ax)
ax.axhline(0, color="black", linewidth=0.7)
ax.set_xlabel("Year")
ax.set_ylabel("USD Billion")
ax.set_title("Kazakhstan–China Trade Balance (2000–2023)")
ax.legend(loc="upper right")
fig.tight_layout()
fig.savefig(FIGS / "fig01_trade_balance.png", dpi=150)
plt.close(fig)

# --- Fig 02: Mineral exports + Brent ---
fig, ax1 = plt.subplots(figsize=(9, 4))
ax2 = ax1.twinx()
ax1.plot(df_reg["year"], df_reg["minerals_narrow"] / 1e9,
         color=BLUE, marker="o", markersize=4, label="Minerals Narrow (LHS)")
ax1.plot(df_reg["year"], df_reg["minerals_broad"] / 1e9,
         color=BLUE, linestyle="--", marker="s", markersize=3,
         label="Minerals Broad (LHS)")
ax2.plot(df_reg["year"], df_reg["brent_annual_mean"],
         color=RED, marker="^", markersize=4, label="Brent USD/bbl (RHS)")
add_bri_line(ax1)
ax1.set_xlabel("Year")
ax1.set_ylabel("USD Billion")
ax2.set_ylabel("USD/bbl")
lines1, labs1 = ax1.get_legend_handles_labels()
lines2, labs2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labs1 + labs2, loc="upper left", fontsize=8)
ax1.set_title("Mineral Exports and Brent Crude Oil Price (2000–2023)")
fig.tight_layout()
fig.savefig(FIGS / "fig02_minerals_brent.png", dpi=150)
plt.close(fig)

# --- Fig 03: BRI intensity ---
fig, ax = plt.subplots(figsize=(9, 4))
ax.fill_between(df["year"], df["bri_intensity"], alpha=0.3, color=GREEN)
ax.plot(df["year"], df["bri_intensity"], color=GREEN, marker="o", markersize=4)
add_bri_line(ax)
ax.set_xlabel("Year")
ax.set_ylabel("log1p(Cumulative Chinese Finance, USD)")
ax.set_title("BRI Intensity — Cumulative Chinese Finance Committed to Kazakhstan (2000–2024)")
ax.legend()
fig.tight_layout()
fig.savefig(FIGS / "fig03_bri_intensity.png", dpi=150)
plt.close(fig)

# --- Fig 04: 2×2 facet ---
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
plot_spec = [
    ("trade_balance_ratio", "Trade Balance Ratio", axes[0, 0]),
    ("minerals_narrow", "Minerals Narrow (USD B)", axes[0, 1]),
    ("brent_annual_mean", "Brent Crude (USD/bbl)", axes[1, 0]),
    ("kz_gdp", "KAZ GDP const. 2015 (USD B)", axes[1, 1]),
]
for (var, title, ax) in plot_spec:
    if var not in df_reg.columns:
        ax.set_title(f"{title} — DATA MISSING")
        continue
    series = df_reg[var].copy()
    if "usd" in var.lower() and series.abs().max() > 1e9:
        series = series / 1e9
    ax.plot(df_reg["year"], series, color=BLUE, marker="o", markersize=3)
    add_bri_line(ax, label=True)
    ax.set_title(title, fontsize=9)
    ax.set_xlabel("Year", fontsize=8)
    ax.tick_params(axis="both", labelsize=7)

fig.suptitle("Kazakhstan–China Trade Panel: Key Variables (2000–2023)", fontsize=11)
fig.tight_layout()
fig.savefig(FIGS / "fig04_facet_panel.png", dpi=150)
plt.close(fig)

print("\nFigures saved to Outputs/generated_figures/")
print("Done: 10_descriptives.py")
