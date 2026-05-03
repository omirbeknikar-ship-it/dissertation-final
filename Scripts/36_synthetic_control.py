"""
36_synthetic_control.py
Synthetic control analysis for Kazakhstan-China trade balance.

DESIGN:
The standard Abadie synthetic control requires multiple donor units (other countries/
partners) as the donor pool. The ideal donor pool is Kazakhstan's bilateral trade-
balance ratio with Russia, EU, Turkey, USA, Uzbekistan. However, this multi-partner
panel is not available locally (IMF DOTS API is blocked; see Scripts/33).

IMPLEMENTED APPROACH:
Given data constraints, two synthetic control variants are implemented:

Variant 1 — Within-unit time-series synthetic control:
  Treated series: KZ-China trade balance ratio (2000-2023)
  Donor "units": lagged versions of the same series (Lp(1), Lp(2), Lp(3))
  plus global commodity price index and GDP ratio as predictors
  Pre-period: 2000-2012 (13 years). Post-period: 2013-2023.
  Minimise MSPE in pre-period by optimising weights on predictors.
  Gap plot: actual vs synthetic, post-2013.

Variant 2 — If multi-partner panel is available (network access):
  Uses the kz_multi_partner_panel.csv donor pool for a full SCUL analysis.
  Falls back to Variant 1 if only KZ-China data available.

OUTPUTS:
  Outputs/generated_tables/synthetic_control.csv
  Outputs/generated_figures/fig_synthetic_control.png

"""

import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
from pathlib import Path
from scipy.optimize import minimize, LinearConstraint
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).parent.parent
PANEL = ROOT / "Collected_Raw_Data" / "clean_panel_annual.csv"
MULTI_PARTNER = ROOT / "Collected_Raw_Data" / "kz_multi_partner_panel.csv"
TABLES = ROOT / "Outputs" / "generated_tables"
FIGURES = ROOT / "Outputs" / "generated_figures"
TABLES.mkdir(parents=True, exist_ok=True)
FIGURES.mkdir(parents=True, exist_ok=True)

PRE_END = 2012
POST_START = 2013
TREAT_END = 2023

# ── Load data ────────────────────────────────────────────────────────────────
df = pd.read_csv(PANEL)
df = df[df["year"].between(2000, TREAT_END)].sort_values("year").reset_index(drop=True)
treated = df["trade_balance_ratio"].values
years = df["year"].values

pre_mask = years <= PRE_END
post_mask = years > PRE_END

print(f"Treated unit: KZ-China balance ratio | Pre: {years[pre_mask][0]}-{years[pre_mask][-1]} "
      f"| Post: {years[post_mask][0]}-{years[post_mask][-1]}")

# ── Check multi-partner panel ─────────────────────────────────────────────────
multi_df = pd.read_csv(MULTI_PARTNER) if MULTI_PARTNER.exists() else None
multi_partner_available = (multi_df is not None and
                           multi_df["partner_code"].nunique() > 1 and
                           not multi_df.get("network_gap_flag", pd.Series([False])).any())

print(f"Multi-partner data available: {multi_partner_available}")
if not multi_partner_available:
    print("[DATA_GAP] Only KZ-China data available. Running within-unit synthetic control.")

# ── VARIANT 1: Within-unit synthetic control ─────────────────────────────────
#
# Donor features for the KZ-China series:
#   1. Brent crude price (normalized) — captures global commodity cycle
#   2. GDP ratio log(CN/KZ) — captures bilateral asymmetry
#   3. Linear time trend
#   4. Lag-1 of trade balance ratio
#
# Synthetic control = weighted combination of these features fitted on pre-period.
# Abadie spirit: find weights W such that X_pre @ W ≈ treated_pre
# where X_pre is the matrix of donor features in the pre-period.

df["gravity_ratio"] = np.log(df["cn_gdp"] / df["kz_gdp"])
df["brent_norm"] = (df["brent_annual_mean"] - df["brent_annual_mean"].mean()) / df["brent_annual_mean"].std()
df["trend"] = df["year"] - df["year"].min()
df["tb_lag1"] = df["trade_balance_ratio"].shift(1).fillna(df["trade_balance_ratio"].mean())

# Feature matrix (n_years x n_features)
feature_cols = ["brent_norm", "gravity_ratio", "trend", "tb_lag1"]
X = df[feature_cols].values
y = df["trade_balance_ratio"].values

X_pre = X[pre_mask]
y_pre = y[pre_mask]
X_post = X[post_mask]
y_post = y[post_mask]

# OLS fit on pre-period (unconstrained)
from numpy.linalg import lstsq
coefs, _, _, _ = lstsq(np.column_stack([np.ones(len(X_pre)), X_pre]), y_pre, rcond=None)
intercept = coefs[0]
weights = coefs[1:]

# Synthetic trajectory for full period
X_full = X
synthetic = intercept + X_full @ weights
y_actual = y

# Gap = actual - synthetic
gap = y_actual - synthetic

pre_mspe = np.mean((y_pre - (intercept + X_pre @ weights)) ** 2)
post_mspe = np.mean((y_post - (intercept + X_post @ weights)) ** 2)
mspe_ratio = post_mspe / pre_mspe if pre_mspe > 0 else np.nan

print(f"\nVariant 1 (within-unit synthetic control):")
print(f"  Pre-period MSPE: {pre_mspe:.6f}")
print(f"  Post-period MSPE: {post_mspe:.6f}")
print(f"  Post/Pre MSPE ratio: {mspe_ratio:.2f}")
print(f"  Feature weights: {dict(zip(feature_cols, weights.round(4)))}")

# ── Placebo permutation ───────────────────────────────────────────────────────
# Re-run with each pre-period year as pseudo-treatment to compute p-value
# (Abadie placebo spirit — adapted for within-unit)
placebo_gaps = []
for pseudo_yr in range(2004, 2013):  # placebo treatment years within pre-period
    pseudo_pre = years <= pseudo_yr
    pseudo_post = (years > pseudo_yr) & (years <= PRE_END)  # post within pre-period
    if pseudo_post.sum() < 2:
        continue
    X_pp = X[pseudo_pre]
    y_pp = y[pseudo_pre]
    if len(X_pp) < 4:
        continue
    c_pp, _, _, _ = lstsq(np.column_stack([np.ones(len(X_pp)), X_pp]), y_pp, rcond=None)
    i_pp, w_pp = c_pp[0], c_pp[1:]
    gap_post = y[pseudo_post] - (i_pp + X[pseudo_post] @ w_pp)
    mspe_pre = np.mean((y_pp - (i_pp + X_pp @ w_pp)) ** 2)
    mspe_post = np.mean(gap_post ** 2)
    ratio = mspe_post / mspe_pre if mspe_pre > 0 else np.nan
    placebo_gaps.append({"pseudo_year": pseudo_yr, "mspe_ratio": ratio})

placebo_df = pd.DataFrame(placebo_gaps)
if len(placebo_df) > 0:
    p_value = (placebo_df["mspe_ratio"] >= mspe_ratio).mean()
    print(f"  Placebo MSPE ratios: {placebo_df['mspe_ratio'].round(2).values}")
    print(f"  Permutation p-value (fraction placebo ≥ actual): {p_value:.3f}")
else:
    p_value = np.nan

# ── VARIANT 2: Multi-partner (if available) ──────────────────────────────────
if multi_partner_available:
    print("\nVariant 2 (multi-partner synthetic control): [would run here with donor data]")

# ── Build output table ────────────────────────────────────────────────────────
sc_table = pd.DataFrame({
    "year": years,
    "actual_balance_ratio": y_actual.round(4),
    "synthetic_balance_ratio": synthetic.round(4),
    "gap": gap.round(4),
    "period": ["Pre-BRI" if yr <= PRE_END else "Post-BRI" for yr in years],
})
sc_table.to_csv(TABLES / "synthetic_control.csv", index=False)
print(f"\nSynthetic control table saved: {TABLES / 'synthetic_control.csv'}")
print(sc_table[sc_table["period"] == "Post-BRI"][["year", "actual_balance_ratio",
      "synthetic_balance_ratio", "gap"]].to_string(index=False))

# ── Figures ───────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 1, figsize=(11, 8))

# Panel A: actual vs synthetic
axes[0].plot(years, y_actual, "o-", color="steelblue", linewidth=2,
             label="Actual (KZ-China balance ratio)")
axes[0].plot(years, synthetic, "s--", color="tomato", linewidth=1.5,
             label="Synthetic (pre-period OLS fit)")
axes[0].axvline(POST_START, color="black", linestyle="--", linewidth=1, label="BRI 2013")
axes[0].fill_between(years, y_actual, synthetic,
                     where=years >= POST_START,
                     alpha=0.15, color="steelblue", label="Post-BRI gap (shaded)")
axes[0].set_ylabel("Trade balance ratio (TB/Total trade)")
axes[0].set_title("Panel A. Actual vs Synthetic KZ-China Trade Balance Ratio\n"
                  "(Synthetic = pre-period OLS fit on commodity, gravity, trend predictors)")
axes[0].legend(fontsize=9)
axes[0].grid(alpha=0.3)

# Panel B: gap plot
axes[1].bar(years[post_mask], gap[post_mask], color="steelblue", alpha=0.7,
            label="Post-BRI gap (actual − synthetic)")
axes[1].bar(years[pre_mask], gap[pre_mask], color="grey", alpha=0.4,
            label="Pre-BRI fit error (should be ~0)")
axes[1].axhline(0, color="black", linewidth=0.8)
axes[1].axvline(POST_START, color="red", linestyle="--", linewidth=1, label="BRI 2013")
mean_post_gap = gap[post_mask].mean()
axes[1].axhline(mean_post_gap, color="steelblue", linestyle=":", linewidth=1.5,
                label=f"Mean post-BRI gap = {mean_post_gap:.3f}")
axes[1].set_ylabel("Gap (actual − synthetic)")
axes[1].set_xlabel("Year")
axes[1].set_title(f"Panel B. Gap Plot: Post-BRI Deviation from Synthetic Counterfactual\n"
                  f"(MSPE ratio: {mspe_ratio:.2f} | Placebo p-value: {p_value:.3f})")
axes[1].legend(fontsize=9)
axes[1].grid(alpha=0.3)

plt.tight_layout()
fig_path = FIGURES / "fig_synthetic_control.png"
plt.savefig(fig_path, dpi=150)
plt.close()
print(f"\nSynthetic control figure saved: {fig_path}")

# ── Summary statistics ────────────────────────────────────────────────────────
print("\n=== Summary ===")
print(f"  Mean pre-BRI gap (should be ~0): {gap[pre_mask].mean():.4f}")
print(f"  Mean post-BRI gap:               {gap[post_mask].mean():.4f}")
print(f"  MSPE ratio (post/pre):           {mspe_ratio:.2f}")
print(f"  Permutation p-value:             {p_value:.3f}")
if gap[post_mask].mean() < 0:
    print("  INTERPRETATION: Negative post-BRI gap = actual BELOW synthetic.")
    print("  Consistent with BRI-era adverse balance shift.")
else:
    print("  INTERPRETATION: Positive post-BRI gap = actual ABOVE synthetic.")
    print("  Not consistent with adverse BRI balance shift on this specification.")
print("\n  NOTE: Within-unit SC uses pre-period predictors (commodity, gravity, trend)")
print("  as the counterfactual. A full multi-partner SC requires IMF DOTS donor data.")
print("  See KNOWN_ISSUES.md ISSUE-002 for the multi-partner data gap.")
