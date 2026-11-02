"""
45_ardl_clean.py
Final-audit re-estimation of the ADL / bounds-test results (§6.7).

Why: Script 12 includes `oil_exports_B` as a regressor. In the annual panel
that column is not observed data: it equals exactly 55% of total exports in
every year (an illustrative placeholder). Script 12's bounds test also fails
on current statsmodels (attribute renamed). This script re-estimates the
dynamic model without the placeholder, on observed variables only, using
both the parsimonious (A2) and growth-rate (B) control sets.

Specification: ARDL with AIC-selected lags (max 1, given n = 24), dependent
variable = trade balance (USD bn); regressors = minerals, Brent, KZT/USD,
post-BRI dummy, post-BRI x minerals (+ GDP growth rates in B).
Bounds test: Pesaran, Shin and Smith (2001), case 3 (unrestricted constant).

Outputs: Outputs/generated_tables/ardl_clean.csv
"""
import warnings
warnings.filterwarnings("ignore")
from pathlib import Path
import numpy as np
import pandas as pd
from statsmodels.tsa.ardl import ardl_select_order, UECM

ROOT = Path(__file__).parent.parent
df = pd.read_csv(ROOT / "Collected_Raw_Data" / "clean_panel_annual.csv")
df = df[df["year"].between(2000, 2023)].sort_values("year").reset_index(drop=True)
df["TB"] = df["trade_balance_usd"] / 1e9
df["MIN"] = df["minerals_narrow"] / 1e9
df["BRENT"] = df["brent_annual_mean"]
df["KZT"] = df["kzt_usd"]
df["POST"] = df["post_bri_2013"].astype(float)
df["POST_x_MIN"] = df["POST"] * df["MIN"]
df["dlg_kz_gdp"] = np.log(df["kz_gdp"]).diff()
df["dlg_cn_gdp"] = np.log(df["cn_gdp"]).diff()

rows = []
for label, cols in [("A2 controls", ["MIN", "BRENT", "KZT"]),
                    ("B controls", ["MIN", "BRENT", "KZT", "dlg_kz_gdp", "dlg_cn_gdp"])]:
    d = df.dropna(subset=cols + ["TB"]).reset_index(drop=True)
    exog = d[cols]
    fixed = d[["POST", "POST_x_MIN"]]
    sel = ardl_select_order(d["TB"], 1, exog, 1, fixed=fixed, ic="aic", trend="c")
    res = sel.model.fit(cov_type="HAC", cov_kwds={"maxlags": 2})
    row = {"Controls": label, "N": int(res.nobs), "AIC": res.aic,
           "selected_lags": str(sel.model.ardl_order),
           "Interaction_coef": res.params["POST_x_MIN"], "Interaction_p": res.pvalues["POST_x_MIN"]}
    lag_y = [p for p in res.params.index if p.startswith("TB.L")]
    rho = sum(res.params[p] for p in lag_y)
    row["sum_lagged_TB"] = rho
    row["long_run_interaction"] = res.params["POST_x_MIN"] / (1 - rho)
    try:
        u = UECM(d["TB"], 1, exog, 1, fixed=fixed, trend="c").fit()
        bt = u.bounds_test(case=3)
        row["PSS_F"] = float(bt.stat) if hasattr(bt, "stat") else float(bt.statistic)
        pv = bt.p_values if hasattr(bt, "p_values") else bt.pvalue
        row["PSS_p_lower_I0"] = float(pv["lower"]); row["PSS_p_upper_I1"] = float(pv["upper"])
    except Exception as e:
        row["PSS_F"] = np.nan; row["bounds_note"] = str(e)[:80]
    rows.append(row)
out = pd.DataFrame(rows)
out.round(4).to_csv(ROOT / "Outputs" / "generated_tables" / "ardl_clean.csv", index=False)
print(out.round(3).T.to_string())

# ── CUSUM / CUSUMSQ stability on the parsimonious static model (observed data only)
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import statsmodels.api as sm
FIGS = ROOT / "Outputs" / "generated_figures"
d = df.dropna(subset=["TB", "MIN", "BRENT", "KZT"]).reset_index(drop=True)
X = sm.add_constant(d[["MIN", "POST", "POST_x_MIN", "BRENT", "KZT"]])
rls = sm.RecursiveLS(d["TB"], X).fit()
stab = {}
for kind in ("cusum", "cusum_squares"):
    fig = rls.plot_cusum(alpha=0.05) if kind == "cusum" else rls.plot_cusum_squares(alpha=0.05)
    ax = fig.axes[0]
    ax.set_xticks(range(len(d))[::4]); ax.set_xticklabels(d["year"].values[::4])
    ax.set_title(("CUSUM" if kind == "cusum" else "CUSUM of squares") +
                 " - parsimonious model (A2), recursive residuals, 5% bounds")
    fig.set_size_inches(8, 3.6); fig.tight_layout()
    fig.savefig(FIGS / f"fig_{kind}_clean.png", dpi=200); plt.close(fig)
# statsmodels returns each bound as its two end points; interpolate linearly
cus = np.asarray(rls.cusum)
lw, up = rls._cusum_significance_bounds(alpha=0.05, ddof=0)
lwi = np.linspace(lw[0], lw[1], len(cus)); upi = np.linspace(up[0], up[1], len(cus))
stab["n_recursive_residuals"] = len(cus)
stab["first_year_tested"] = int(d["year"].values[-len(cus)])
stab["cusum_outside_bounds"] = bool(np.any((cus < lwi) | (cus > upi)))
cs2 = np.asarray(rls.cusum_squares)
lw2, up2 = rls._cusum_squares_significance_bounds(alpha=0.05)
lw2 = np.asarray(lw2); up2 = np.asarray(up2)
if lw2.size == 2 and cs2.size != 2:
    lw2 = np.linspace(lw2[0], lw2[1], len(cs2)); up2 = np.linspace(up2[0], up2[1], len(cs2))
outside = (cs2 < lw2) | (cs2 > up2)
stab["cusumsq_outside_bounds"] = bool(np.any(outside))
yrs = d["year"].values[-len(cs2):]
stab["cusumsq_outside_years"] = ",".join(str(y) for y in yrs[outside])
pd.DataFrame([stab]).to_csv(ROOT / "Outputs" / "generated_tables" / "stability_clean.csv", index=False)
print(stab)
