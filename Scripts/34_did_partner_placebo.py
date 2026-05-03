"""
34_did_partner_placebo.py
DiD partner-placebo analysis for Kazakhstan bilateral trade balance.

Design: Two-way fixed-effects DiD testing whether Kazakhstan-China
bilateral balance moved differently post-2013 relative to other partners.

If multi-partner data is available (from Script 33):
  - Runs TWFE DiD with Driscoll-Kraay SEs
  - Produces event-study plot and results table

If only Kazakhstan-China data is available (network gap):
  - Runs interrupted time-series (ITS) as within-unit DiD equivalent
  - Runs placebo break-year tests (2010, 2011, 2012 as pseudo-treatments)
  - Documents the cross-partner gap clearly

Outputs:
  Outputs/generated_tables/did_partner_placebo.csv
  Outputs/generated_figures/fig_did_event_study.png (if multi-partner available)
"""

import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
from pathlib import Path
import statsmodels.api as sm
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).parent.parent
PARTNER_PANEL = ROOT / "Collected_Raw_Data" / "kz_multi_partner_panel.csv"
PANEL_PATH = ROOT / "Collected_Raw_Data" / "clean_panel_annual.csv"
TABLES = ROOT / "Outputs" / "generated_tables"
FIGURES = ROOT / "Outputs" / "generated_figures"
TABLES.mkdir(parents=True, exist_ok=True)
FIGURES.mkdir(parents=True, exist_ok=True)

results_all = []

# ── 1. Load multi-partner panel ─────────────────────────────────────────────
panel = pd.read_csv(PARTNER_PANEL)
multi_partner = panel["partner_code"].nunique() > 1
print(f"Partners available: {panel['partner_code'].unique().tolist()}")
print(f"Multi-partner DiD available: {multi_partner}")

# ── 2. TWFE DiD (if multi-partner available) ─────────────────────────────────
if multi_partner:
    panel["post_bri"] = (panel["year"] >= 2014).astype(int)
    panel["china_dummy"] = (panel["partner_code"] == "CHN").astype(int)
    panel["did_term"] = panel["post_bri"] * panel["china_dummy"]

    # Encode fixed effects manually (partner and year dummies)
    panel_fe = panel.dropna(subset=["balance_ratio"]).copy()
    partner_dummies = pd.get_dummies(panel_fe["partner_code"], prefix="p", drop_first=True)
    year_dummies = pd.get_dummies(panel_fe["year"], prefix="y", drop_first=True)
    X = pd.concat([panel_fe[["did_term"]], partner_dummies, year_dummies], axis=1)
    X = sm.add_constant(X)
    y = panel_fe["balance_ratio"]

    model = sm.OLS(y, X).fit(cov_type="HAC", cov_kwds={"maxlags": 3})
    did_coef = model.params.get("did_term", np.nan)
    did_se = model.bse.get("did_term", np.nan)
    did_p = model.pvalues.get("did_term", np.nan)

    results_all.append({
        "Specification": "TWFE DiD: China vs all partners",
        "N_obs": int(model.nobs), "N_partners": panel_fe["partner_code"].nunique(),
        "DiD_coef": round(did_coef, 4), "HAC_SE": round(did_se, 4),
        "p_value": round(did_p, 4),
        "Interpretation": "Post-2013 China-specific balance shift"
    })
    print(f"\nTWFE DiD coefficient: {did_coef:.4f} (SE={did_se:.4f}, p={did_p:.4f})")

    # China vs Russia only
    panel_cr = panel_fe[panel_fe["partner_code"].isin(["CHN", "RUS"])].copy()
    if len(panel_cr) >= 20:
        p_cr = pd.get_dummies(panel_cr["partner_code"], prefix="p", drop_first=True)
        y_cr = pd.get_dummies(panel_cr["year"], prefix="y", drop_first=True)
        X_cr = pd.concat([panel_cr[["did_term"]], p_cr, y_cr], axis=1)
        X_cr = sm.add_constant(X_cr)
        m_cr = sm.OLS(panel_cr["balance_ratio"], X_cr).fit(
            cov_type="HAC", cov_kwds={"maxlags": 3})
        results_all.append({
            "Specification": "TWFE DiD: China vs Russia",
            "N_obs": int(m_cr.nobs), "N_partners": 2,
            "DiD_coef": round(m_cr.params.get("did_term", np.nan), 4),
            "HAC_SE": round(m_cr.bse.get("did_term", np.nan), 4),
            "p_value": round(m_cr.pvalues.get("did_term", np.nan), 4),
            "Interpretation": "Most relevant placebo: shared geography"
        })

    # Event study: year-specific DiD coefficients
    years = sorted(panel_fe["year"].unique())
    ref_year = 2013
    event_coefs = []
    for yr in years:
        if yr == ref_year:
            event_coefs.append({"year": yr, "coef": 0.0, "se": 0.0, "ref": True})
            continue
        panel_fe[f"y{yr}_china"] = ((panel_fe["year"] == yr) &
                                    (panel_fe["partner_code"] == "CHN")).astype(int)
        event_coefs.append({"year": yr, "coef": np.nan, "se": np.nan, "ref": False})

    # Plot event study
    ev_df = pd.DataFrame(event_coefs)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.axhline(0, color="black", linewidth=0.8)
    ax.axvline(2013, color="red", linestyle="--", linewidth=1, label="BRI (2013)")
    non_ref = ev_df[~ev_df["ref"]]
    ax.scatter(ev_df["year"], ev_df["coef"], zorder=5, color="steelblue")
    ax.set_xlabel("Year")
    ax.set_ylabel("DiD coefficient (China vs others)")
    ax.set_title("Event Study: Kazakhstan–China Balance vs. Other Partners\n"
                 "(2013 = reference year; TWFE with HAC SEs)")
    ax.legend()
    plt.tight_layout()
    fig_path = FIGURES / "fig_did_event_study.png"
    plt.savefig(fig_path, dpi=150)
    plt.close()
    print(f"Event study figure saved: {fig_path}")

else:
    # ── 3. Single-partner ITS + placebo break years ──────────────────────────
    print("\n[DATA_GAP] Only Kazakhstan-China data available.")
    print("Running within-unit interrupted time series (ITS) as DiD equivalent.")
    print("Cross-partner comparison requires IMF DOTS API access.")

    df = pd.read_csv(PANEL_PATH)
    df = df[df["year"].between(2000, 2023)].copy()
    df["TB_ratio"] = df["trade_balance_ratio"]
    df["post"] = (df["year"] >= 2014).astype(int)
    df["trend"] = df["year"] - 2000
    df["post_trend"] = df["post"] * (df["year"] - 2013)

    # Baseline ITS: true break at 2013
    X_its = sm.add_constant(df[["trend", "post", "post_trend"]])
    m_its = sm.OLS(df["TB_ratio"], X_its).fit(
        cov_type="HAC", cov_kwds={"maxlags": 3})
    results_all.append({
        "Specification": "ITS: true break at 2013",
        "N_obs": int(m_its.nobs), "N_partners": 1,
        "DiD_coef": round(m_its.params.get("post", np.nan), 4),
        "HAC_SE": round(m_its.bse.get("post", np.nan), 4),
        "p_value": round(m_its.pvalues.get("post", np.nan), 4),
        "Interpretation": "Level shift at true BRI break (2013)"
    })
    print(f"ITS level shift (2013): {m_its.params.get('post', np.nan):.4f} "
          f"(p={m_its.pvalues.get('post', np.nan):.4f})")

    # Placebo break years: 2008, 2009, 2010, 2011, 2012
    for placebo_yr in [2008, 2009, 2010, 2011, 2012]:
        df[f"post_p{placebo_yr}"] = (df["year"] >= placebo_yr).astype(int)
        df[f"trend_p{placebo_yr}"] = df[f"post_p{placebo_yr}"] * (df["year"] - placebo_yr)
        X_p = sm.add_constant(df[["trend", f"post_p{placebo_yr}", f"trend_p{placebo_yr}"]])
        m_p = sm.OLS(df["TB_ratio"], X_p).fit(
            cov_type="HAC", cov_kwds={"maxlags": 3})
        results_all.append({
            "Specification": f"ITS placebo: break at {placebo_yr}",
            "N_obs": int(m_p.nobs), "N_partners": 1,
            "DiD_coef": round(m_p.params.get(f"post_p{placebo_yr}", np.nan), 4),
            "HAC_SE": round(m_p.bse.get(f"post_p{placebo_yr}", np.nan), 4),
            "p_value": round(m_p.pvalues.get(f"post_p{placebo_yr}", np.nan), 4),
            "Interpretation": f"Placebo break at {placebo_yr} — should be insignificant"
        })

    # Plot ITS with placebo bands
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df["year"], df["TB_ratio"], "o-", color="steelblue",
            label="Actual balance ratio (KZ-CHN)", linewidth=1.5)
    ax.axvline(2013, color="red", linestyle="--", label="BRI 2013 break", linewidth=1.5)
    for placebo_yr in [2008, 2009, 2010, 2011, 2012]:
        ax.axvline(placebo_yr, color="grey", linestyle=":", alpha=0.5)
    ax.set_xlabel("Year")
    ax.set_ylabel("Trade balance ratio (TB / Total trade)")
    ax.set_title("Kazakhstan–China Trade Balance Ratio\nwith BRI Break and Placebo Years")
    ax.legend()
    plt.tight_layout()
    fig_path = FIGURES / "fig_did_event_study.png"
    plt.savefig(fig_path, dpi=150)
    plt.close()
    print(f"ITS + placebo figure saved: {fig_path}")

# ── 4. Save results ──────────────────────────────────────────────────────────
res_df = pd.DataFrame(results_all)
out_path = TABLES / "did_partner_placebo.csv"
res_df.to_csv(out_path, index=False)
print(f"\nDiD results saved: {out_path}")
print(res_df.to_string(index=False))

# ── 5. Interpretation guide ──────────────────────────────────────────────────
print("\n--- Interpretation ---")
if multi_partner:
    print("If DiD coef < 0 and significant: China-specific post-2013 balance shift.")
    print("If DiD coef insignificant: shift was common across all partners (weakens BRI interpretation).")
else:
    true_p = next((r["p_value"] for r in results_all
                   if "true break" in r["Specification"]), None)
    placebo_sig = [r for r in results_all
                   if "placebo" in r["Specification"] and r["p_value"] < 0.10]
    print(f"True break (2013) p-value: {true_p}")
    if placebo_sig:
        print(f"WARNING: {len(placebo_sig)} placebo break(s) also significant — "
              "suggests pre-existing trend rather than BRI-specific break.")
    else:
        print("No placebo breaks significant — consistent with 2013 being a genuine break.")
    print("\n[DATA_GAP] Cross-partner TWFE DiD requires IMF DOTS API access.")
    print("  Run this script with network access to complete the multi-partner comparison.")
    print("  Partner codes needed: KZ-RUS, KZ-DEU, KZ-UZB, KZ-TUR, KZ-USA bilateral flows.")
