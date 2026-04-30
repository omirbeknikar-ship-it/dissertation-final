"""
12_ardl.py
Phase 2 — ARDL/UECM bounds test, long-run coefficients, CUSUM stability.

Specification (both models scaled to USD billions):
  DV: trade_balance_B (billions USD)

  Model A (dummy):
    trade_balance_B ~ minerals_narrow_B + brent + log_kz_gdp + log_cn_gdp
                    + post_bri_2013 + post_bri_2013×minerals_narrow_B

  Model B (intensity):
    trade_balance_B ~ minerals_narrow_B + brent + log_kz_gdp + log_cn_gdp
                    + bri_intensity + bri_intensity×minerals_narrow_B

Strategy:
  (1) AIC-selected ARDL with HAC covariance
  (2) UECM bounds test (Pesaran-Shin-Smith) — cointegration evidence
  (3) CUSUM/CUSUMSQ stability plots

Outputs:
  Outputs/generated_tables/ardl_results.csv
  Outputs/generated_tables/ardl_long_run_coefficients.csv
  Outputs/generated_figures/fig06_cusum_ardlA.png
  Outputs/generated_figures/fig07_cusum_ardlB.png
"""

import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
import statsmodels.api as sm
from scipy import stats
from statsmodels.tsa.ardl import UECM, ardl_select_order

ROOT   = Path(__file__).parent.parent
PANEL  = ROOT / "Collected_Raw_Data" / "clean_panel_annual.csv"
TABLES = ROOT / "Outputs" / "generated_tables"
FIGS   = ROOT / "Outputs" / "generated_figures"
TABLES.mkdir(parents=True, exist_ok=True)
FIGS.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(PANEL)
df = df[df["year"] < 2024].dropna(
    subset=["trade_balance_usd", "minerals_narrow", "brent_annual_mean",
            "kz_gdp", "cn_gdp"]
).copy()
df = df.sort_values("year").reset_index(drop=True)

df["minerals_narrow_B"] = df["minerals_narrow"] / 1e9
df["trade_balance_B"]   = df["trade_balance_usd"] / 1e9
df["log_kz_gdp"] = np.log(df["kz_gdp"])
df["log_cn_gdp"] = np.log(df["cn_gdp"])
n = len(df)
print(f"ARDL sample: n={n}, years {df['year'].min()}–{df['year'].max()}")
if df["oil_exports"].isna().all():
    print("NOTE: oil_exports is all missing in clean_panel_annual.csv; excluded from ARDL regressors.")

results_rows = []
lr_rows = []

def selected_lag_string(selector):
    y_lags = selector.ar_lags if selector.ar_lags is not None else []
    dl_lags = selector.dl_lags if selector.dl_lags is not None else {}
    dl = "; ".join(f"{k}:{v}" for k, v in dl_lags.items())
    return f"y:{list(y_lags)} | x:{dl}"

def ardl_long_run_table(fit_hac, y_name, variables, model_label):
    """
    Long-run multiplier = sum(beta_lags) / (1 - sum(phi_y_lags)).
    HAC SE uses delta method from the ARDL HAC covariance matrix.
    """
    params = fit_hac.params
    cov = fit_hac.cov_params()
    names = list(params.index)
    phi_names = [nm for nm in names if nm.startswith(f"{y_name}.L")]
    denom = 1.0 - float(params[phi_names].sum()) if phi_names else 1.0
    rows = []

    for var in variables:
        beta_names = [nm for nm in names if nm.startswith(f"{var}.L")]
        if not beta_names:
            rows.append({
                "model": model_label,
                "variable": var,
                "long_run_coef": np.nan,
                "hac_se": np.nan,
                "t_stat": np.nan,
                "p_value": np.nan,
                "selected_terms": "",
            })
            continue

        beta_sum = float(params[beta_names].sum())
        lr = beta_sum / denom
        grad = pd.Series(0.0, index=names)
        for nm in beta_names:
            grad[nm] = 1.0 / denom
        for nm in phi_names:
            grad[nm] = beta_sum / (denom ** 2)

        var_lr = float(grad.values @ cov.loc[names, names].values @ grad.values)
        se_lr = np.sqrt(var_lr) if var_lr >= 0 else np.nan
        t_stat = lr / se_lr if se_lr and not np.isnan(se_lr) else np.nan
        p_val = 2 * (1 - stats.t.cdf(abs(t_stat), df=max(int(fit_hac.df_resid), 1))) if not np.isnan(t_stat) else np.nan
        rows.append({
            "model": model_label,
            "variable": var,
            "long_run_coef": round(lr, 6),
            "hac_se": round(se_lr, 6) if not np.isnan(se_lr) else np.nan,
            "t_stat": round(t_stat, 4) if not np.isnan(t_stat) else np.nan,
            "p_value": round(p_val, 4) if not np.isnan(p_val) else np.nan,
            "selected_terms": ",".join(beta_names),
        })
    return rows

MODELS = [
    ("Model_A_dummy",     "post_bri_2013",  "BRI Dummy"),
    ("Model_B_intensity", "bri_intensity",  "BRI Intensity"),
]

for model_label, bri_var, bri_desc in MODELS:
    print(f"\n{'='*60}")
    print(f" {model_label} — {bri_desc}")
    print(f"{'='*60}")

    interaction_col = f"{bri_var}_x_minerals_narrow_B"
    df[interaction_col] = df[bri_var] * df["minerals_narrow_B"]
    exog_cols = ["minerals_narrow_B", "brent_annual_mean", "kzt_usd",
                 "log_kz_gdp", "log_cn_gdp", bri_var, interaction_col]

    # -------- (1) OLS + HAC SE, for direct comparison with earlier output --------
    X = sm.add_constant(df[exog_cols])
    ols = sm.OLS(df["trade_balance_B"], X).fit()
    ols_hac = ols.get_robustcov_results(cov_type="HAC", maxlags=3)

    print("\nOLS HAC coefficients:")
    print(f"{'Variable':<30} {'Coef':>10} {'Std':>10} {'t':>8} {'p':>8}")
    for nm, c, se, t, p in zip(ols_hac.model.exog_names,
                                ols_hac.params,
                                ols_hac.bse,
                                ols_hac.tvalues,
                                ols_hac.pvalues):
        print(f"  {nm:<28} {c:>10.4f} {se:>10.4f} {t:>8.3f} {p:>8.4f}")
    print(f"  R² = {ols.rsquared:.4f}  adj-R² = {ols.rsquared_adj:.4f}")

    param_series = pd.Series(ols_hac.params.flatten(), index=ols_hac.model.exog_names)
    pval_series  = pd.Series(ols_hac.pvalues.flatten(), index=ols_hac.model.exog_names)

    # -------- (2) AIC-selected ARDL and long-run HAC coefficients --------
    try:
        selector = ardl_select_order(
            df["trade_balance_B"],
            maxlag=1,
            exog=df[exog_cols],
            maxorder=1,
            trend="c",
            ic="aic",
            glob=False,
            missing="raise",
        )
        ardl_fit = selector.model.fit(cov_type="HAC", cov_kwds={"maxlags": 3})
        ardl_aic = float(ardl_fit.aic)
        ardl_lags = selected_lag_string(selector)
        print(f"\nAIC-selected ARDL lags: {ardl_lags}")
        print(f"ARDL AIC = {ardl_aic:.4f}")
        lr_rows.extend(ardl_long_run_table(
            ardl_fit,
            "trade_balance_B",
            exog_cols,
            model_label,
        ))
    except Exception as e:
        print(f"\nAIC-selected ARDL failed: {e}")
        ardl_aic = np.nan
        ardl_lags = f"ARDL_SELECT_FAILED: {str(e)[:80]}"
        for var in exog_cols:
            lr_rows.append({
                "model": model_label,
                "variable": var,
                "long_run_coef": np.nan,
                "hac_se": np.nan,
                "t_stat": np.nan,
                "p_value": np.nan,
                "selected_terms": "",
            })

    # -------- (3) UECM bounds test --------
    try:
        exog_df = df[exog_cols].copy()
        uecm_model = UECM(
            df["trade_balance_B"], lags=1,
            exog=exog_df,
            order={col: 1 for col in exog_cols},
        )
        uecm_fit = uecm_model.fit()
        bt = uecm_fit.bounds_test(case=2)
        pss_f = round(bt.stat, 4)
        pss_upper_p = round(bt.p_values[1], 4) if hasattr(bt, "p_values") else round(bt.upper_p_value, 4)
        pss_lower_p = round(bt.p_values[0], 4) if hasattr(bt, "p_values") else round(bt.lower_p_value, 4)
        # Determine conclusion
        if pss_upper_p < 0.05:
            coint_conclusion = "COINTEGRATED (reject H0 at 5%)"
        elif pss_lower_p < 0.05:
            coint_conclusion = "INCONCLUSIVE (between bounds)"
        else:
            coint_conclusion = "NO COINTEGRATION"
        print(f"\nPSS Bounds test: F={pss_f}, upper_p={pss_upper_p}, lower_p={pss_lower_p}")
        print(f"  → {coint_conclusion}")
    except Exception as e:
        print(f"\nUECM bounds test failed: {e}")
        pss_f, pss_upper_p, pss_lower_p = np.nan, np.nan, np.nan
        coint_conclusion = f"UECM_FAILED: {str(e)[:60]}"

    # -------- (4) CUSUM / CUSUMSQ --------
    resids = ols.resid.values
    cusum   = np.cumsum(resids) / (np.std(resids) * np.sqrt(n))
    cusumsq = np.cumsum(resids**2) / np.sum(resids**2)
    t_arr   = np.arange(1, n + 1)
    cv_cusum = 1.36

    stable_cusum   = bool((np.abs(cusum) <= cv_cusum).all())
    expected_csq   = t_arr / n
    cv_csq         = 0.1401  # approx 5% band width
    stable_cusumsq = bool(((cusumsq >= expected_csq - cv_csq) &
                            (cusumsq <= expected_csq + cv_csq)).all())

    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    axes[0].plot(df["year"], cusum, color="#2166AC", marker="o", markersize=4)
    axes[0].axhline( cv_cusum, color="#D6604D", linestyle="--", label="±1.36 (5%)")
    axes[0].axhline(-cv_cusum, color="#D6604D", linestyle="--")
    axes[0].axhline(0, color="black", linewidth=0.7)
    axes[0].set_title(f"CUSUM — {model_label}")
    axes[0].set_xlabel("Year"); axes[0].legend()

    axes[1].plot(t_arr, cusumsq, color="#2166AC", marker="o", markersize=4, label="CUSUMSQ")
    axes[1].plot(t_arr, expected_csq + cv_csq, "#D6604D", linestyle="--")
    axes[1].plot(t_arr, np.maximum(0, expected_csq - cv_csq), "#D6604D", linestyle="--", label="5% bounds")
    axes[1].plot(t_arr, expected_csq, "k", linewidth=0.7)
    axes[1].set_title(f"CUSUMSQ — {model_label}")
    axes[1].set_xlabel("Observation"); axes[1].legend()

    fig.tight_layout()
    fname = f"fig0{'6' if 'A' in model_label else '7'}_cusum_{model_label}.png"
    fig.savefig(FIGS / fname, dpi=150)
    plt.close(fig)

    results_rows.append({
        "model":               model_label,
        "bri_var":             bri_var,
        "n":                   n,
        "r_squared":           round(ols.rsquared, 4),
        "adj_r_squared":       round(ols.rsquared_adj, 4),
        "ardl_aic":            round(ardl_aic, 4) if not np.isnan(ardl_aic) else np.nan,
        "aic_selected_lags":    ardl_lags,
        "oil_exports_note":     "excluded_all_missing",
        "pss_f_stat":          pss_f,
        "pss_upper_pval":      pss_upper_p,
        "pss_lower_pval":      pss_lower_p,
        "cointegration":       coint_conclusion,
        "coef_minerals":       round(param_series.get("minerals_narrow_B", np.nan), 4),
        "pval_minerals":       round(pval_series.get("minerals_narrow_B", np.nan), 4),
        "coef_brent":          round(param_series.get("brent_annual_mean", np.nan), 4),
        "pval_brent":          round(pval_series.get("brent_annual_mean", np.nan), 4),
        "coef_bri_var":        round(param_series.get(bri_var, np.nan), 4),
        "pval_bri_var":        round(pval_series.get(bri_var, np.nan), 4),
        "coef_interaction":    round(param_series.get(interaction_col, np.nan), 4),
        "pval_interaction":    round(pval_series.get(interaction_col, np.nan), 4),
        "cusum_stable_5pct":   stable_cusum,
        "cusumsq_stable_5pct": stable_cusumsq,
    })

# -----------------------------------------------------------------------
# Save
# -----------------------------------------------------------------------
results_df = pd.DataFrame(results_rows)
results_df.to_csv(TABLES / "ardl_results.csv", index=False)
lr_df = pd.DataFrame(lr_rows)
lr_df.to_csv(TABLES / "ardl_long_run_coefficients.csv", index=False)
print(f"\nSaved Outputs/generated_tables/ardl_results.csv")
print(f"Saved Outputs/generated_tables/ardl_long_run_coefficients.csv")
print("\nKey results summary:")
print(results_df[["model", "coef_minerals", "pval_minerals",
                  "coef_interaction", "pval_interaction",
                  "cointegration", "cusum_stable_5pct"]].to_string(index=False))
print("\nLong-run ARDL coefficients:")
print(lr_df[["model", "variable", "long_run_coef", "hac_se", "p_value"]].to_string(index=False))
print("\nDone: 12_ardl.py")
