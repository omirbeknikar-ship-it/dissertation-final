"""
20_robustness.py
Phase 2 - Robustness grid for the main post-BRI x minerals coefficient.

Grid:
  BRI start years: 2013, 2014, 2015, 2016
  Minerals: narrow, broad, WITS legacy
  Outcomes: trade balance level, trade balance ratio
  Samples: full, ex-2009, ex-2020, ex-both
  Estimators: OLS, ARDL long-run, DiD

DiD is recorded as skipped because placebo/donor annual bilateral panels are
not available from local files. Failures are kept in the output table.

Outputs:
  Outputs/generated_tables/robustness.csv
  Outputs/generated_tables/robustness.md
"""

import warnings
warnings.filterwarnings("ignore")

from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats
from statsmodels.tsa.ardl import ardl_select_order
from statsmodels.tools.sm_exceptions import ValueWarning

warnings.filterwarnings("ignore", category=ValueWarning)

ROOT = Path(__file__).parent.parent
PANEL = ROOT / "Collected_Raw_Data" / "clean_panel_annual.csv"
WITS = ROOT / "Collected_Raw_Data" / "raw" / "wits_ores_metals_exports_kazakhstan_china.csv"
TABLES = ROOT / "Outputs" / "generated_tables"
TABLES.mkdir(parents=True, exist_ok=True)

base = pd.read_csv(PANEL)
base = base[base["year"] < 2024].copy()
base["trade_balance_B"] = base["trade_balance_usd"] / 1e9
base["minerals_narrow_B"] = base["minerals_narrow"] / 1e9
base["minerals_broad_B"] = base["minerals_broad"] / 1e9
base["log_kz_gdp"] = np.log(base["kz_gdp"])
base["log_cn_gdp"] = np.log(base["cn_gdp"])

try:
    wits = pd.read_csv(WITS)
    wits = wits[["year", "value_usd_thousand"]].copy()
    wits["minerals_wits_legacy_B"] = pd.to_numeric(wits["value_usd_thousand"], errors="coerce") * 1000 / 1e9
    base = base.merge(wits[["year", "minerals_wits_legacy_B"]], on="year", how="left")
except Exception:
    base["minerals_wits_legacy_B"] = np.nan

START_YEARS = [2013, 2014, 2015, 2016]
MINERALS = {
    "narrow": "minerals_narrow_B",
    "broad": "minerals_broad_B",
    "wits_legacy": "minerals_wits_legacy_B",
}
OUTCOMES = {
    "level": "trade_balance_B",
    "ratio": "trade_balance_ratio",
}
SAMPLES = {
    "full": [],
    "ex_2009": [2009],
    "ex_2020": [2020],
    "ex_both": [2009, 2020],
}

def post_for_start(years, start_year):
    # start_year is inclusive: e.g. 2014 means years >= 2014 are post.
    return (years >= start_year).astype(int)

def result_row(start_year, mineral_name, outcome_name, sample_name, estimator, status, coef=np.nan, se=np.nan, pval=np.nan, n=np.nan, note=""):
    return {
        "start_year": start_year,
        "minerals_definition": mineral_name,
        "outcome": outcome_name,
        "sample": sample_name,
        "estimator": estimator,
        "interaction_coef": coef,
        "std_error": se,
        "p_value": pval,
        "n_obs": n,
        "status": status,
        "note": note,
    }

def fit_ols(df, y_col, x_col, post_col, interaction_col):
    controls = [x_col, "brent_annual_mean", "kzt_usd", "log_kz_gdp", "log_cn_gdp", post_col, interaction_col]
    use = df.dropna(subset=[y_col] + controls).copy()
    if len(use) < 12:
        raise ValueError(f"insufficient observations: n={len(use)}")
    X = sm.add_constant(use[controls])
    fit = sm.OLS(use[y_col], X).fit(cov_type="HAC", cov_kwds={"maxlags": 3})
    return fit.params[interaction_col], fit.bse[interaction_col], fit.pvalues[interaction_col], len(use)

def fit_ardl_lr(df, y_col, x_col, post_col, interaction_col):
    controls = [x_col, "brent_annual_mean", "kzt_usd", "log_kz_gdp", "log_cn_gdp", post_col, interaction_col]
    use = df.dropna(subset=[y_col] + controls).copy()
    if len(use) < 16:
        raise ValueError(f"insufficient observations for ARDL: n={len(use)}")
    selector = ardl_select_order(
        use[y_col],
        maxlag=1,
        exog=use[controls],
        maxorder=1,
        trend="c",
        ic="aic",
        glob=False,
        missing="raise",
    )
    fit = selector.model.fit(cov_type="HAC", cov_kwds={"maxlags": 3})
    params = fit.params
    cov = fit.cov_params()
    names = list(params.index)
    phi_names = [nm for nm in names if nm.startswith(f"{y_col}.L")]
    denom = 1.0 - float(params[phi_names].sum()) if phi_names else 1.0
    beta_names = [nm for nm in names if nm.startswith(f"{interaction_col}.L")]
    if not beta_names:
        raise ValueError("interaction not selected by AIC ARDL")
    beta_sum = float(params[beta_names].sum())
    lr = beta_sum / denom
    grad = pd.Series(0.0, index=names)
    for nm in beta_names:
        grad[nm] = 1.0 / denom
    for nm in phi_names:
        grad[nm] = beta_sum / (denom ** 2)
    var_lr = float(grad.values @ cov.loc[names, names].values @ grad.values)
    se = np.sqrt(var_lr) if var_lr >= 0 else np.nan
    t_stat = lr / se if se and not np.isnan(se) else np.nan
    pval = 2 * (1 - stats.t.cdf(abs(t_stat), df=max(int(fit.df_resid), 1))) if not np.isnan(t_stat) else np.nan
    note = f"AIC lags y={selector.ar_lags}; x={selector.dl_lags}"
    return lr, se, pval, len(use), note

rows = []
for start_year in START_YEARS:
    for mineral_name, mineral_col in MINERALS.items():
        for outcome_name, y_col in OUTCOMES.items():
            for sample_name, excluded_years in SAMPLES.items():
                df = base[~base["year"].isin(excluded_years)].copy()
                post_col = f"post_{start_year}"
                interaction_col = f"{post_col}_x_{mineral_col}"
                df[post_col] = post_for_start(df["year"], start_year)
                df[interaction_col] = df[post_col] * df[mineral_col]

                try:
                    coef, se, pval, n = fit_ols(df, y_col, mineral_col, post_col, interaction_col)
                    rows.append(result_row(start_year, mineral_name, outcome_name, sample_name, "OLS", "ok", coef, se, pval, n))
                except Exception as exc:
                    rows.append(result_row(start_year, mineral_name, outcome_name, sample_name, "OLS", "failed", note=str(exc)))

                try:
                    coef, se, pval, n, note = fit_ardl_lr(df, y_col, mineral_col, post_col, interaction_col)
                    status = "ok"
                    if abs(coef) > 1000 or (not np.isnan(se) and se > 1000):
                        status = "estimated_unstable"
                        note = f"{note}; large long-run multiplier/SE"
                    rows.append(result_row(start_year, mineral_name, outcome_name, sample_name, "ARDL_long_run", status, coef, se, pval, n, note))
                except Exception as exc:
                    rows.append(result_row(start_year, mineral_name, outcome_name, sample_name, "ARDL_long_run", "failed", note=str(exc)))

                rows.append(result_row(
                    start_year,
                    mineral_name,
                    outcome_name,
                    sample_name,
                    "DiD",
                    "skipped_data_unavailable",
                    note="No donor/placebo annual bilateral panel in local files; see did_placebo_status.csv.",
                ))

robust = pd.DataFrame(rows)
for col in ["interaction_coef", "std_error", "p_value"]:
    robust[col] = pd.to_numeric(robust[col], errors="coerce").round(6)
robust.to_csv(TABLES / "robustness.csv", index=False)

def markdown_table(df):
    if len(df) == 0:
        return "_No rows._"
    text_df = df.copy()
    for col in text_df.columns:
        text_df[col] = text_df[col].astype(str)
    widths = {
        col: max(len(col), int(text_df[col].map(len).max()))
        for col in text_df.columns
    }
    header = "| " + " | ".join(col.ljust(widths[col]) for col in text_df.columns) + " |"
    sep = "| " + " | ".join("-" * widths[col] for col in text_df.columns) + " |"
    body = [
        "| " + " | ".join(row[col].ljust(widths[col]) for col in text_df.columns) + " |"
        for _, row in text_df.iterrows()
    ]
    return "\n".join([header, sep] + body)

headline = robust[
    (robust["start_year"] == 2014)
    & (robust["minerals_definition"] == "narrow")
    & (robust["outcome"] == "level")
    & (robust["sample"] == "full")
    & (robust["estimator"].isin(["OLS", "ARDL_long_run"]))
]
breakers = robust[
    (robust["estimator"].isin(["OLS", "ARDL_long_run"]))
    & (robust["status"].isin(["ok", "estimated_unstable"]))
    & (robust["interaction_coef"] > 0)
]

md_lines = [
    "# Robustness Results",
    "",
    "Main coefficient: post-BRI x minerals. Outcomes are USD billions for level and unitless for ratio.",
    "",
    "## Headline Rows",
    "",
    markdown_table(headline),
    "",
    "## Sign-Reversing Estimated Rows",
    "",
    markdown_table(breakers) if len(breakers) else "No estimated OLS/ARDL rows reverse the sign to positive.",
    "",
    "## Full Grid",
    "",
    markdown_table(robust),
]
(TABLES / "robustness.md").write_text("\n".join(md_lines), encoding="utf-8")

print(f"Saved {TABLES / 'robustness.csv'}")
print(f"Saved {TABLES / 'robustness.md'}")
print("Status counts:")
print(robust.groupby(["estimator", "status"]).size().to_string())
print("Done: 20_robustness.py")
