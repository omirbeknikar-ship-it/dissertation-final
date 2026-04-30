"""
30_full_diagnostics.py
Complete diagnostics suite for dissertation upgrade.

Produces:
  - VIF table
  - Influence diagnostics (Cook's D, leverage, leave-one-out)
  - Residual diagnostics (plot, heteroskedasticity, autocorrelation)
  - Post-2014-only subsample check
  - Leave-one-out coefficient stability
  - All required figures for the paper
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
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor, OLSInfluence
from scipy import stats

ROOT = Path(__file__).parent.parent
PANEL = ROOT / "Collected_Raw_Data" / "clean_panel_annual.csv"
TABLES = ROOT / "Outputs" / "generated_tables"
FIGS = ROOT / "Outputs" / "generated_figures"
TABLES.mkdir(parents=True, exist_ok=True)
FIGS.mkdir(parents=True, exist_ok=True)

# ---- Style ----
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 11,
    "axes.titlesize": 13,
    "axes.labelsize": 11,
    "figure.dpi": 150,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.15,
})

# ---- Load ----
df = pd.read_csv(PANEL)
df = df[df["year"] < 2024].dropna(
    subset=["trade_balance_usd", "minerals_narrow", "brent_annual_mean",
            "kz_gdp", "cn_gdp"]
).copy()
df = df.sort_values("year").reset_index(drop=True)
df["minerals_narrow_B"] = df["minerals_narrow"] / 1e9
df["trade_balance_B"] = df["trade_balance_usd"] / 1e9
df["exports_B"] = df["exports_kazakhstan_to_china_usd"] / 1e9
df["imports_B"] = df["imports_kazakhstan_from_china_usd"] / 1e9
df["log_kz_gdp"] = np.log(df["kz_gdp"])
df["log_cn_gdp"] = np.log(df["cn_gdp"])
df["post_bri_x_minerals"] = df["post_bri_2013"] * df["minerals_narrow_B"]
n = len(df)
print(f"Diagnostics sample: n={n}, years {df['year'].min()}-{df['year'].max()}")

exog_cols = ["minerals_narrow_B", "brent_annual_mean", "kzt_usd",
             "log_kz_gdp", "log_cn_gdp", "post_bri_2013", "post_bri_x_minerals"]
X = sm.add_constant(df[exog_cols])
ols = sm.OLS(df["trade_balance_B"], X).fit()
ols_hac = ols.get_robustcov_results(cov_type="HAC", maxlags=3)

# ======================================================================
# 1. VIF DIAGNOSTICS
# ======================================================================
print("\n" + "="*60)
print("  VIF DIAGNOSTICS")
print("="*60)
vif_data = []
for i, col in enumerate(X.columns):
    if col == "const":
        continue
    vif_val = variance_inflation_factor(X.values, i)
    vif_data.append({"Variable": col, "VIF": round(vif_val, 2)})
vif_df = pd.DataFrame(vif_data)
print(vif_df.to_string(index=False))
vif_df.to_csv(TABLES / "vif_diagnostics.csv", index=False)
print(f"\nSaved {TABLES / 'vif_diagnostics.csv'}")

# ======================================================================
# 2. INFLUENCE DIAGNOSTICS
# ======================================================================
print("\n" + "="*60)
print("  INFLUENCE DIAGNOSTICS")
print("="*60)
influence = OLSInfluence(ols)
cooks_d = influence.cooks_distance[0]
leverage = influence.hat_matrix_diag
dffits_val = influence.dffits[0]

inf_df = pd.DataFrame({
    "Year": df["year"].values,
    "Cooks_D": np.round(cooks_d, 4),
    "Leverage": np.round(leverage, 4),
    "DFFITS": np.round(dffits_val, 4),
    "Studentized_Resid": np.round(influence.resid_studentized_external, 4),
})
# Thresholds
k = len(exog_cols)
cooks_thresh = 4.0 / n
leverage_thresh = 2.0 * (k + 1) / n
inf_df["Flag_Cooks"] = inf_df["Cooks_D"] > cooks_thresh
inf_df["Flag_Leverage"] = inf_df["Leverage"] > leverage_thresh
inf_df["Flag_Any"] = inf_df["Flag_Cooks"] | inf_df["Flag_Leverage"]
print(inf_df.to_string(index=False))
inf_df.to_csv(TABLES / "influence_diagnostics.csv", index=False)
print(f"\nCook's D threshold (4/n): {cooks_thresh:.4f}")
print(f"Leverage threshold (2(k+1)/n): {leverage_thresh:.4f}")
print(f"Flagged years: {inf_df[inf_df['Flag_Any']]['Year'].tolist()}")

# ======================================================================
# 3. LEAVE-ONE-OUT COEFFICIENT STABILITY
# ======================================================================
print("\n" + "="*60)
print("  LEAVE-ONE-OUT COEFFICIENT STABILITY")
print("="*60)
loo_rows = []
for i in range(n):
    df_loo = df.drop(index=i).reset_index(drop=True)
    X_loo = sm.add_constant(df_loo[exog_cols])
    y_loo = df_loo["trade_balance_B"]
    fit_loo = sm.OLS(y_loo, X_loo).fit(cov_type="HAC", cov_kwds={"maxlags": 3})
    loo_rows.append({
        "Excluded_Year": int(df.loc[i, "year"]),
        "Interaction_Coef": round(fit_loo.params["post_bri_x_minerals"], 4),
        "Interaction_SE": round(fit_loo.bse["post_bri_x_minerals"], 4),
        "Interaction_Pval": round(fit_loo.pvalues["post_bri_x_minerals"], 4),
        "Minerals_Coef": round(fit_loo.params["minerals_narrow_B"], 4),
        "PostBRI_Coef": round(fit_loo.params["post_bri_2013"], 4),
        "R_squared": round(fit_loo.rsquared, 4),
    })
loo_df = pd.DataFrame(loo_rows)
print(loo_df.to_string(index=False))
loo_df.to_csv(TABLES / "leave_one_out.csv", index=False)

# Check sign stability
sign_changes = loo_df[loo_df["Interaction_Coef"] > 0]
print(f"\nSign reversals in leave-one-out: {len(sign_changes)} of {n}")
if len(sign_changes) > 0:
    print(f"Years causing reversal: {sign_changes['Excluded_Year'].tolist()}")

# Key years
for yr in [2009, 2011, 2020, 2022, 2023]:
    row = loo_df[loo_df["Excluded_Year"] == yr]
    if len(row) > 0:
        r = row.iloc[0]
        print(f"  Excluding {yr}: β_interaction = {r['Interaction_Coef']:.4f} (p={r['Interaction_Pval']:.4f})")

# ======================================================================
# 4. POST-2014 ONLY SUBSAMPLE
# ======================================================================
print("\n" + "="*60)
print("  POST-2014 ONLY SUBSAMPLE (descriptive check)")
print("="*60)
df_post = df[df["year"] >= 2014].copy().reset_index(drop=True)
n_post = len(df_post)
print(f"Post-2014 sample: n={n_post}")
if n_post >= 8:
    exog_post = ["minerals_narrow_B", "brent_annual_mean", "kzt_usd"]
    X_post = sm.add_constant(df_post[exog_post])
    ols_post = sm.OLS(df_post["trade_balance_B"], X_post).fit(
        cov_type="HAC", cov_kwds={"maxlags": 2})
    print("Post-2014-only OLS (parsimonious):")
    for nm, c, p in zip(ols_post.model.exog_names, ols_post.params, ols_post.pvalues):
        print(f"  {nm:25s} coef={c:8.4f}  p={p:.4f}")
    print(f"  R² = {ols_post.rsquared:.4f}")
else:
    print("Insufficient observations for post-2014-only regression.")

# ======================================================================
# 5. RESIDUAL DIAGNOSTICS
# ======================================================================
print("\n" + "="*60)
print("  RESIDUAL DIAGNOSTICS")
print("="*60)
resids = ols.resid.values
fitted = ols.fittedvalues.values

# Durbin-Watson
from statsmodels.stats.stattools import durbin_watson
dw = durbin_watson(resids)
print(f"Durbin-Watson: {dw:.4f}")
if dw < 1.5:
    print("  → Positive autocorrelation likely.")
elif dw > 2.5:
    print("  → Negative autocorrelation likely.")
else:
    print("  → Inconclusive / mild autocorrelation.")

# Breusch-Pagan
from statsmodels.stats.diagnostic import het_breuschpagan
bp_stat, bp_pval, _, _ = het_breuschpagan(resids, X)
print(f"Breusch-Pagan: stat={bp_stat:.4f}, p={bp_pval:.4f}")

# ======================================================================
# 6. FIGURES
# ======================================================================
print("\n" + "="*60)
print("  GENERATING FIGURES")
print("="*60)

# Color palette
C_EXPORT = "#2166AC"
C_IMPORT = "#B2182B"
C_BALANCE = "#4DAF4A"
C_MINERAL = "#FF7F00"
C_BRI = "#E7E7E7"
C_PRE = "#1B7837"
C_POST = "#762A83"

# --- Figure 1: Exports and Imports over time ---
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df["year"], df["exports_B"], "o-", color=C_EXPORT, linewidth=2, markersize=5, label="KAZ Exports to CHN")
ax.plot(df["year"], df["imports_B"], "s-", color=C_IMPORT, linewidth=2, markersize=5, label="KAZ Imports from CHN")
ax.axvspan(2013.5, df["year"].max() + 0.5, alpha=0.08, color="gray", label="Post-BRI period")
ax.axvline(2013.5, color="gray", linestyle="--", linewidth=0.8)
ax.set_xlabel("Year")
ax.set_ylabel("USD Billions")
ax.set_title("Figure 1. Kazakhstan–China Bilateral Exports and Imports, 2000–2023")
ax.legend(loc="upper left", fontsize=9)
ax.set_xlim(1999.5, 2023.5)
ax.grid(True, alpha=0.3)
fig.savefig(FIGS / "fig_1_exports_imports.png")
plt.close(fig)
print("  Saved fig_1_exports_imports.png")

# --- Figure 2: Trade balance over time ---
fig, ax = plt.subplots(figsize=(10, 5))
colors = [C_PRE if y < 2014 else C_POST for y in df["year"]]
ax.bar(df["year"], df["trade_balance_B"], color=colors, edgecolor="white", linewidth=0.5, width=0.8)
ax.axhline(0, color="black", linewidth=0.8)
ax.axvline(2013.5, color="gray", linestyle="--", linewidth=0.8, label="BRI announcement")
ax.set_xlabel("Year")
ax.set_ylabel("USD Billions")
ax.set_title("Figure 2. Kazakhstan–China Bilateral Trade Balance, 2000–2023")
ax.legend(fontsize=9)
ax.set_xlim(1999.5, 2023.5)
ax.grid(True, alpha=0.3, axis="y")
fig.savefig(FIGS / "fig_2_trade_balance.png")
plt.close(fig)
print("  Saved fig_2_trade_balance.png")

# --- Figure 3: Strategic mineral exports over time ---
fig, ax = plt.subplots(figsize=(10, 5))
ax.fill_between(df["year"], df["minerals_narrow_B"], alpha=0.3, color=C_MINERAL)
ax.plot(df["year"], df["minerals_narrow_B"], "o-", color=C_MINERAL, linewidth=2, markersize=5, label="Narrow minerals (U+Cu+Cr)")
ax.axvline(2013.5, color="gray", linestyle="--", linewidth=0.8, label="BRI announcement")
# Add annotation for measurement break
ax.annotate("← WITS proxy | Comtrade HS-2 →", xy=(2013.5, df["minerals_narrow_B"].max()*0.95),
            fontsize=8, ha="center", color="gray", style="italic")
ax.set_xlabel("Year")
ax.set_ylabel("USD Billions")
ax.set_title("Figure 3. Strategic Mineral Exports (Narrow), Kazakhstan → China, 2000–2023")
ax.legend(fontsize=9)
ax.set_xlim(1999.5, 2023.5)
ax.grid(True, alpha=0.3)
fig.savefig(FIGS / "fig_3_minerals.png")
plt.close(fig)
print("  Saved fig_3_minerals.png")

# --- Figure 4: Minerals vs Trade Balance scatter ---
fig, ax = plt.subplots(figsize=(8, 6))
pre = df[df["post_bri_2013"] == 0]
post = df[df["post_bri_2013"] == 1]
ax.scatter(pre["minerals_narrow_B"], pre["trade_balance_B"], c=C_PRE, s=60, label="Pre-BRI (2000–2013)", zorder=3, edgecolors="white")
ax.scatter(post["minerals_narrow_B"], post["trade_balance_B"], c=C_POST, s=60, label="Post-BRI (2014–2023)", zorder=3, edgecolors="white", marker="D")
# Label 2023
yr23 = df[df["year"] == 2023]
if len(yr23) > 0:
    ax.annotate("2023", (yr23["minerals_narrow_B"].values[0], yr23["trade_balance_B"].values[0]),
                textcoords="offset points", xytext=(8, -12), fontsize=8, color=C_POST)
yr11 = df[df["year"] == 2011]
if len(yr11) > 0:
    ax.annotate("2011", (yr11["minerals_narrow_B"].values[0], yr11["trade_balance_B"].values[0]),
                textcoords="offset points", xytext=(8, 5), fontsize=8, color=C_PRE)
ax.axhline(0, color="black", linewidth=0.5, linestyle=":")
ax.set_xlabel("Strategic Mineral Exports (USD Billions)")
ax.set_ylabel("Bilateral Trade Balance (USD Billions)")
ax.set_title("Figure 4. Mineral Exports vs. Trade Balance, Pre- and Post-BRI")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
fig.savefig(FIGS / "fig_4_scatter.png")
plt.close(fig)
print("  Saved fig_4_scatter.png")

# --- Figure 5: Residuals and influence diagnostics ---
fig, axes = plt.subplots(2, 2, figsize=(12, 9))

# Residuals vs fitted
axes[0, 0].scatter(fitted, resids, c=C_EXPORT, s=40, edgecolors="white")
axes[0, 0].axhline(0, color="black", linewidth=0.8)
axes[0, 0].set_xlabel("Fitted Values (USD bn)")
axes[0, 0].set_ylabel("Residuals (USD bn)")
axes[0, 0].set_title("(a) Residuals vs. Fitted Values")
axes[0, 0].grid(True, alpha=0.3)

# Cook's distance
axes[0, 1].stem(df["year"], cooks_d, linefmt="-", markerfmt="o", basefmt="k-")
axes[0, 1].axhline(cooks_thresh, color=C_IMPORT, linestyle="--", label=f"4/n = {cooks_thresh:.3f}")
axes[0, 1].set_xlabel("Year")
axes[0, 1].set_ylabel("Cook's Distance")
axes[0, 1].set_title("(b) Cook's Distance")
axes[0, 1].legend(fontsize=8)
axes[0, 1].grid(True, alpha=0.3)

# Leverage
axes[1, 0].stem(df["year"], leverage, linefmt="-", markerfmt="o", basefmt="k-")
axes[1, 0].axhline(leverage_thresh, color=C_IMPORT, linestyle="--", label=f"2(k+1)/n = {leverage_thresh:.3f}")
axes[1, 0].set_xlabel("Year")
axes[1, 0].set_ylabel("Leverage (hat value)")
axes[1, 0].set_title("(c) Leverage Values")
axes[1, 0].legend(fontsize=8)
axes[1, 0].grid(True, alpha=0.3)

# Leave-one-out interaction coefficient
axes[1, 1].plot(loo_df["Excluded_Year"], loo_df["Interaction_Coef"], "o-", color=C_POST, markersize=5)
beta_full = ols.params["post_bri_x_minerals"]
axes[1, 1].axhline(beta_full, color=C_EXPORT, linestyle="-", linewidth=1.5, label=f"Full-sample β = {beta_full:.2f}")
axes[1, 1].axhline(0, color="black", linewidth=0.5, linestyle=":")
axes[1, 1].set_xlabel("Excluded Year")
axes[1, 1].set_ylabel("Interaction Coefficient")
axes[1, 1].set_title("(d) Leave-One-Out: Post-BRI × Minerals")
axes[1, 1].legend(fontsize=8)
axes[1, 1].grid(True, alpha=0.3)

fig.suptitle("Figure 5. Residual and Influence Diagnostics", fontsize=14, y=1.01)
fig.tight_layout()
fig.savefig(FIGS / "fig_5_diagnostics.png")
plt.close(fig)
print("  Saved fig_5_diagnostics.png")

# --- Figure 6: Pre-BRI vs Post-BRI comparison bars ---
pre_means = {
    "Trade Balance": pre["trade_balance_B"].mean(),
    "Minerals Narrow": pre["minerals_narrow_B"].mean(),
    "Exports": pre["exports_B"].mean(),
    "Imports": pre["imports_B"].mean(),
}
post_means = {
    "Trade Balance": post["trade_balance_B"].mean(),
    "Minerals Narrow": post["minerals_narrow_B"].mean(),
    "Exports": post["exports_B"].mean(),
    "Imports": post["imports_B"].mean(),
}

fig, ax = plt.subplots(figsize=(9, 5))
x_pos = np.arange(len(pre_means))
width = 0.35
ax.bar(x_pos - width/2, list(pre_means.values()), width, label="Pre-BRI (2000–2013)", color=C_PRE, alpha=0.85)
ax.bar(x_pos + width/2, list(post_means.values()), width, label="Post-BRI (2014–2023)", color=C_POST, alpha=0.85)
ax.set_xticks(x_pos)
ax.set_xticklabels(list(pre_means.keys()), fontsize=10)
ax.set_ylabel("USD Billions (mean)")
ax.set_title("Figure 6. Pre-BRI vs. Post-BRI Mean Comparison")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3, axis="y")
ax.axhline(0, color="black", linewidth=0.5)
fig.savefig(FIGS / "fig_6_pre_post.png")
plt.close(fig)
print("  Saved fig_6_pre_post.png")

# ======================================================================
# 7. FULL REGRESSION TABLE (complete, no dashes)
# ======================================================================
print("\n" + "="*60)
print("  FULL REGRESSION TABLE")
print("="*60)
reg_table = []
for nm, c, se, t, p in zip(ols_hac.model.exog_names,
                            ols_hac.params,
                            ols_hac.bse,
                            ols_hac.tvalues,
                            ols_hac.pvalues):
    stars = ""
    if p < 0.01: stars = "***"
    elif p < 0.05: stars = "**"
    elif p < 0.10: stars = "*"
    reg_table.append({
        "Variable": nm,
        "Coefficient": round(c, 4),
        "HAC_SE": round(se, 4),
        "t_stat": round(t, 3),
        "p_value": round(p, 4),
        "Significance": stars,
    })
reg_df = pd.DataFrame(reg_table)
reg_df.to_csv(TABLES / "full_regression_table.csv", index=False)
print(reg_df.to_string(index=False))
print(f"\nN = {ols.nobs:.0f}")
print(f"R² = {ols.rsquared:.4f}")
print(f"Adj R² = {ols.rsquared_adj:.4f}")
print(f"F-stat = {ols.fvalue:.4f} (p = {ols.f_pvalue:.4f})")

# ======================================================================
# 8. HYPOTHESIS SUMMARY TABLE
# ======================================================================
hyp_table = pd.DataFrame([
    {"Hypothesis": "H1: Post-BRI trade-balance deterioration",
     "Variable": "post_bri_2013",
     "Coefficient": round(float(ols.params["post_bri_2013"]), 4),
     "p_value": round(float(ols.pvalues["post_bri_2013"]), 4),
     "Interpretation": "Positive level shift, but offset by negative interaction"},
    {"Hypothesis": "H2: Minerals → better pre-BRI balance",
     "Variable": "minerals_narrow_B",
     "Coefficient": round(float(ols.params["minerals_narrow_B"]), 4),
     "p_value": round(float(ols.pvalues["minerals_narrow_B"]), 4),
     "Interpretation": "Supported: positive pre-BRI mineral-balance association"},
    {"Hypothesis": "H3: Post-BRI × minerals interaction < 0",
     "Variable": "post_bri_x_minerals",
     "Coefficient": round(float(ols.params["post_bri_x_minerals"]), 4),
     "p_value": round(float(ols.pvalues["post_bri_x_minerals"]), 4),
     "Interpretation": "Supported: weaker mineral-balance payoff post-BRI"},
    {"Hypothesis": "H4: Cautious interpretation required",
     "Variable": "—",
     "Coefficient": "—",
     "p_value": "—",
     "Interpretation": "Multiple confounders: oil shock, tenge, measurement break"},
])
hyp_table.to_csv(TABLES / "hypothesis_summary.csv", index=False)
print("\nHypothesis summary saved.")

print("\n" + "="*60)
print("  ALL DIAGNOSTICS COMPLETE")
print("="*60)
print(f"Tables saved to: {TABLES}")
print(f"Figures saved to: {FIGS}")
print("Done: 30_full_diagnostics.py")
