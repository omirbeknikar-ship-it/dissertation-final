"""
11_structural_breaks.py
Phase 2 — Structural break tests on the trade balance series.

Tests:
  (A) Chow test at hypothesised break years: 2013, 2014, 2015, 2016
  (B) Bai-Perron-style multiple-break test via ruptures binary segmentation
      with BIC model-selection for number of breaks and bootstrap 95% CI

Output: Outputs/generated_tables/structural_breaks.csv
        Outputs/generated_figures/fig05_cusum_breaks.png
"""

import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
from scipy import stats
import ruptures as rpt
import statsmodels.api as sm

np.random.seed(20260430)

ROOT   = Path(__file__).parent.parent
PANEL  = ROOT / "Collected_Raw_Data" / "clean_panel_annual.csv"
TABLES = ROOT / "Outputs" / "generated_tables"
FIGS   = ROOT / "Outputs" / "generated_figures"
TABLES.mkdir(parents=True, exist_ok=True)
FIGS.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(PANEL)
df = df[df["year"] < 2024].dropna(subset=["trade_balance_usd"]).copy()
df = df.sort_values("year").reset_index(drop=True)

y      = df["trade_balance_usd"].values
years  = df["year"].values
n      = len(y)

print(f"Sample: {years[0]}–{years[-1]}, n={n}")

# -----------------------------------------------------------------------
# A. Chow test at hypothesised break points
# -----------------------------------------------------------------------
def chow_test(y, years, break_year):
    """
    OLS-based Chow test.
    H0: no structural break at break_year.
    Returns (F_stat, p_value, df1, df2).
    """
    t = years <= break_year
    n1, n2 = t.sum(), (~t).sum()
    if n1 < 3 or n2 < 3:
        return np.nan, np.nan, np.nan, np.nan

    y1, y2 = y[t], y[~t]
    X1 = np.column_stack([np.ones(n1), np.arange(n1)])
    X2 = np.column_stack([np.ones(n2), np.arange(n2)])
    X  = np.column_stack([np.ones(n),  np.arange(n)])

    rss_unrestricted = (
        np.sum((y1 - X1 @ np.linalg.lstsq(X1, y1, rcond=None)[0])**2) +
        np.sum((y2 - X2 @ np.linalg.lstsq(X2, y2, rcond=None)[0])**2)
    )
    rss_restricted = np.sum((y - X @ np.linalg.lstsq(X, y, rcond=None)[0])**2)

    k = X.shape[1]
    df1 = k
    df2 = n - 2 * k
    if df2 <= 0:
        return np.nan, np.nan, df1, df2

    F_stat = ((rss_restricted - rss_unrestricted) / df1) / (rss_unrestricted / df2)
    p_val  = 1 - stats.f.cdf(F_stat, df1, df2)
    return round(F_stat, 4), round(p_val, 4), df1, df2

chow_results = []
for by in [2013, 2014, 2015, 2016]:
    F, p, df1, df2 = chow_test(y, years, by)
    chow_results.append({
        "break_year": by,
        "F_stat":     F,
        "p_value":    p,
        "df1":        df1,
        "df2":        df2,
        "significant_at_10pct": (p < 0.10) if not np.isnan(p) else False,
    })

chow_df = pd.DataFrame(chow_results)
print("\nChow test results:")
print(chow_df.to_string(index=False))

# -----------------------------------------------------------------------
# B. Bai-Perron multiple break test (via ruptures Pelt + BIC)
# -----------------------------------------------------------------------
signal = y.reshape(-1, 1)

# Try Pelt (penalised exact) with BIC-like penalty on the number of breaks
bai_perron_results = []
for pen in [0.5, 1.0, 2.0, 3.0]:  # BIC penalty multipliers on sigma^2
    try:
        algo = rpt.Pelt(model="rbf").fit(signal)
        breaks = algo.predict(pen=pen * np.std(y)**2 / n)
        # ruptures returns END indices; last entry = n (end of series)
        break_years = [years[b - 1] for b in breaks[:-1]]
        bai_perron_results.append({
            "penalty_scale": pen,
            "n_breaks":      len(break_years),
            "break_years":   str(break_years),
        })
    except Exception as e:
        bai_perron_results.append({"penalty_scale": pen, "n_breaks": -1,
                                    "break_years": f"ERR: {e}"})

bp_df = pd.DataFrame(bai_perron_results)
print("\nBai-Perron (Pelt + RBF) break detection:")
print(bp_df.to_string(index=False))

# Also try Binary Segmentation with AIC/BIC model selection
bs_breaks = []
try:
    algo_bs = rpt.Binseg(model="l2").fit(signal)
    # Elbow method: compare BIC for 1,2,3 break points
    bic_scores = {}
    for nb in range(1, 5):
        brks = algo_bs.predict(n_bkps=nb)
        resid_ss = 0
        prev = 0
        for b in brks:
            seg = y[prev:b]
            resid_ss += np.sum((seg - seg.mean())**2)
            prev = b
        k_params = nb * 2 + 2   # means + linear trend per segment approximation
        bic_scores[nb] = n * np.log(resid_ss / n) + k_params * np.log(n)

    best_nb = min(bic_scores, key=bic_scores.get)
    best_brks = algo_bs.predict(n_bkps=best_nb)
    best_break_years = [years[b - 1] for b in best_brks[:-1]]
    print(f"\nBinarySeg BIC-optimal breaks: n={best_nb} at years {best_break_years}")
    print(f"BIC scores: {bic_scores}")
except Exception as e:
    best_break_years = []
    best_nb = 0
    best_brks = [n]
    bic_scores = {}
    print(f"\nBinarySeg failed: {e}")

def segmented_mean_fit(values, breaks):
    fitted = np.zeros_like(values, dtype=float)
    prev = 0
    for b in breaks:
        fitted[prev:b] = values[prev:b].mean()
        prev = b
    return fitted

def bootstrap_break_ci(values, years, n_bkps, n_boot=500):
    """
    Bootstrap uncertainty for the selected binary-segmentation break years.
    This is an approximation to the Bai-Perron confidence interval because
    the R strucchange implementation is unavailable in this environment
    (see KNOWN_ISSUES.md ISSUE-003).
    """
    if n_bkps <= 0:
        return []
    try:
        base_breaks = rpt.Binseg(model="l2").fit(values.reshape(-1, 1)).predict(n_bkps=n_bkps)
        fitted = segmented_mean_fit(values, base_breaks)
        resid = values - fitted
        resid = resid - resid.mean()
        boot_years = [[] for _ in range(n_bkps)]
        for _ in range(n_boot):
            y_star = fitted + np.random.choice(resid, size=len(resid), replace=True)
            brks_star = rpt.Binseg(model="l2").fit(y_star.reshape(-1, 1)).predict(n_bkps=n_bkps)
            yrs_star = [int(years[b - 1]) for b in brks_star[:-1]]
            if len(yrs_star) == n_bkps:
                for j, yr in enumerate(yrs_star):
                    boot_years[j].append(yr)
        ci_rows = []
        for j, vals in enumerate(boot_years):
            if len(vals) == 0:
                ci_rows.append((np.nan, np.nan, 0))
            else:
                ci_rows.append((
                    int(np.percentile(vals, 2.5)),
                    int(np.percentile(vals, 97.5)),
                    len(vals),
                ))
        return ci_rows
    except Exception as exc:
        print(f"Bootstrap break CI failed: {exc}")
        return [(np.nan, np.nan, 0) for _ in range(n_bkps)]

bp_ci = bootstrap_break_ci(y, years, best_nb, n_boot=500)
if best_break_years:
    print("\nBootstrap 95% CI for BIC-selected break year(s):")
    for yr, (lo, hi, draws) in zip(best_break_years, bp_ci):
        print(f"  break={yr}, 95% CI [{lo}, {hi}], bootstrap_draws={draws}")

# -----------------------------------------------------------------------
# C. Summary: detected break year
# -----------------------------------------------------------------------
# Synthesise: which break year has strongest evidence?
print("\n--- SYNTHESIS ---")
sig_chow = chow_df[chow_df["significant_at_10pct"] == True]
if len(sig_chow) > 0:
    preferred_break = int(sig_chow.iloc[0]["break_year"])
    print(f"Chow-preferred break year: {preferred_break} "
          f"(F={sig_chow.iloc[0]['F_stat']}, p={sig_chow.iloc[0]['p_value']})")
else:
    preferred_break = 2013  # hypothesised BRI year
    print(f"No significant Chow break; using hypothesised year {preferred_break}")

if best_break_years:
    print(f"BinarySeg BIC-preferred break year(s): {best_break_years}")
    data_preferred_break = best_break_years[0]
else:
    data_preferred_break = preferred_break

if data_preferred_break != 2013:
    print(f"NOTE: Data-preferred break {data_preferred_break} ≠ 2013. "
          f"Robustness checks use {data_preferred_break} as alternative BRI threshold.")

# -----------------------------------------------------------------------
# D. CUSUM plot
# -----------------------------------------------------------------------
X_full = sm.add_constant(np.arange(n))
model  = sm.OLS(y, X_full).fit()
resids = model.resid
cusum  = np.cumsum(resids) / (np.std(resids) * np.sqrt(n))
cusum_bounds = 1.36   # 5% critical value for CUSUM

fig, ax = plt.subplots(figsize=(9, 4))
ax.plot(years, cusum, color="#2166AC", marker="o", markersize=4, label="CUSUM")
ax.axhline( cusum_bounds, color="#D6604D", linestyle="--", label="±1.36 (5% bounds)")
ax.axhline(-cusum_bounds, color="#D6604D", linestyle="--")
ax.axhline(0, color="black", linewidth=0.7)
ax.axvline(preferred_break + 0.5, color="#666666", linestyle=":", label=f"Chow break {preferred_break}")
ax.set_xlabel("Year")
ax.set_ylabel("Cumulative Sum of Residuals (normalised)")
ax.set_title("CUSUM Test — Kazakhstan–China Trade Balance (OLS residuals)")
ax.legend()
fig.tight_layout()
fig.savefig(FIGS / "fig05_cusum_breaks.png", dpi=150)
plt.close(fig)

# -----------------------------------------------------------------------
# E. Save combined table
# -----------------------------------------------------------------------
chow_out = chow_df.rename(columns={"F_stat": "statistic"}).copy()
chow_out["test"] = "Chow"
chow_out["ci_lower"] = np.nan
chow_out["ci_upper"] = np.nan
chow_out["n_breaks"] = np.nan
chow_out["method_note"] = "OLS Chow test at fixed break year"

bp_rows = []
for idx, yr in enumerate(best_break_years):
    ci = bp_ci[idx] if idx < len(bp_ci) else (np.nan, np.nan, 0)
    bp_rows.append({
        "break_year": int(yr),
        "statistic": np.nan,
        "p_value": np.nan,
        "df1": np.nan,
        "df2": np.nan,
        "significant_at_10pct": np.nan,
        "test": "Bai-Perron-style",
        "ci_lower": ci[0],
        "ci_upper": ci[1],
        "n_breaks": best_nb,
        "method_note": (
            "ruptures Binseg l2 with BIC-selected number of breaks; "
            "bootstrap CI, see KNOWN_ISSUES.md ISSUE-003"
        ),
    })

output = pd.concat([chow_out, pd.DataFrame(bp_rows)], ignore_index=True)
output.to_csv(TABLES / "structural_breaks.csv", index=False)
print(f"\nSaved Outputs/generated_tables/structural_breaks.csv")
print(f"Saved Outputs/generated_figures/fig05_cusum_breaks.png")
print("Done: 11_structural_breaks.py")
