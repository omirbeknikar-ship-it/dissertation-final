"""
44_did_robustness.py
Final-audit robustness checks for the TWFE difference-in-differences (§6.15).

Two weaknesses of the original estimate (Script 34) are addressed:

1. Inference. Script 34 applies Newey-West HAC errors to a stacked panel
   (rows ordered partner by partner), which treats the boundary between two
   partners as if it were consecutive time periods. Alternatives reported:
     - Driscoll-Kraay errors (cross-sectional sums by year, HAC over time)
     - Partner-clustered errors (only 6 clusters: reported for completeness)
     - Wild cluster bootstrap by partner, Webb 6-point weights, null imposed
     - Permutation (placebo-in-space) inference: each of the 6 partners is
       treated as if it were "China"; the p-value is China's rank. With six
       units the smallest attainable p-value is 1/6 = 0.167.

2. Data. Kazakhstan-reported imports drop sharply in 2020-2022 not only from
   China but also from Germany, the USA, Turkey and Uzbekistan (not Russia).
   Variants: exclude 2020-2022; exclude 2020-2023; exclude Russia.

Outputs:
  Outputs/generated_tables/did_robustness.csv
  Outputs/generated_tables/did_permutation.csv
  Outputs/generated_tables/partner_import_break.csv
"""
import warnings
warnings.filterwarnings("ignore")

from pathlib import Path
import numpy as np
import pandas as pd
import statsmodels.api as sm

ROOT = Path(__file__).parent.parent
TABLES = ROOT / "Outputs" / "generated_tables"
RNG = np.random.default_rng(20261030)

panel = pd.read_csv(ROOT / "Collected_Raw_Data" / "kz_multi_partner_panel.csv")
panel = panel.dropna(subset=["balance_ratio"]).copy()
panel["post"] = (panel["year"] >= 2014).astype(int)

# ── Evidence: the 2020-2022 import drop across partners ────────────────────
imp = panel.pivot(index="year", columns="partner_code", values="imports_usd") / 1e9
brk = pd.DataFrame({
    "imports_2019_bn": imp.loc[2019], "imports_2020_bn": imp.loc[2020],
    "imports_2021_bn": imp.loc[2021], "imports_2022_bn": imp.loc[2022],
    "imports_2023_bn": imp.loc[2023],
})
brk["change_2019_2020_pct"] = 100 * (brk["imports_2020_bn"] / brk["imports_2019_bn"] - 1)
brk.round(3).to_csv(TABLES / "partner_import_break.csv")
print(brk.round(2).to_string())


def design(df, treat="CHN"):
    d = df.copy()
    d["did"] = ((d["partner_code"] == treat) & (d["post"] == 1)).astype(float)
    P = pd.get_dummies(d["partner_code"], prefix="p", drop_first=True).astype(float)
    Y = pd.get_dummies(d["year"], prefix="y", drop_first=True).astype(float)
    X = sm.add_constant(pd.concat([d[["did"]], P, Y], axis=1))
    return d, X


def fit_all(df, label, treat="CHN", boot=True):
    d, X = design(df, treat)
    y = d["balance_ratio"].astype(float)
    ols = sm.OLS(y, X).fit()
    out = {"Sample": label, "N_obs": int(ols.nobs), "N_partners": d["partner_code"].nunique(),
           "DiD_coef": ols.params["did"]}
    # Original: Newey-West HAC on the stacked panel
    nw = sm.OLS(y, X).fit(cov_type="HAC", cov_kwds={"maxlags": 3})
    out["p_NW_stacked_original"] = nw.pvalues["did"]
    # Driscoll-Kraay
    tidx = d["year"].astype(int).values
    dk = sm.OLS(y, X).fit(cov_type="hac-groupsum", cov_kwds={"time": tidx - tidx.min(), "maxlags": 3},
                         use_t=True)
    out["SE_DriscollKraay"] = dk.bse["did"]; out["p_DriscollKraay"] = dk.pvalues["did"]
    # Partner-clustered
    groups = pd.factorize(d["partner_code"])[0]
    cl = sm.OLS(y, X).fit(cov_type="cluster", cov_kwds={"groups": groups}, use_t=True)
    out["SE_cluster_partner"] = cl.bse["did"]; out["p_cluster_partner"] = cl.pvalues["did"]
    # Wild cluster bootstrap (restricted, Webb weights)
    if boot:
        Xr = X.drop(columns="did")
        r = sm.OLS(y, Xr).fit()
        t_obs = cl.tvalues["did"]
        webb = np.array([-np.sqrt(1.5), -1, -np.sqrt(0.5), np.sqrt(0.5), 1, np.sqrt(1.5)])
        G = groups.max() + 1
        B = 1999
        tb = np.empty(B)
        for b in range(B):
            w = RNG.choice(webb, size=G)[groups]
            yb = r.fittedvalues + r.resid * w
            mb = sm.OLS(yb, X).fit(cov_type="cluster", cov_kwds={"groups": groups}, use_t=True)
            tb[b] = mb.tvalues["did"]
        out["p_wild_cluster_bootstrap"] = float(np.mean(np.abs(tb) >= abs(t_obs)))
    return out


samples = [
    ("All partners, 2000-2023 (original)", panel),
    ("All partners, excl. 2020-2022", panel[~panel["year"].between(2020, 2022)]),
    ("All partners, excl. 2020-2023", panel[panel["year"] <= 2019]),
    ("Excl. Russia, 2000-2023", panel[panel["partner_code"] != "RUS"]),
    ("Excl. Russia, excl. 2020-2022", panel[(panel["partner_code"] != "RUS") & ~panel["year"].between(2020, 2022)]),
]
res = pd.DataFrame([fit_all(df, lab) for lab, df in samples])
res.round(4).to_csv(TABLES / "did_robustness.csv", index=False)
print(res.round(4).to_string())

# ── Permutation (placebo-in-space) inference ───────────────────────────────
perm_rows = []
for lab, df in samples[:3]:
    coefs = {}
    for unit in sorted(df["partner_code"].unique()):
        d, X = design(df, treat=unit)
        coefs[unit] = sm.OLS(d["balance_ratio"].astype(float), X).fit().params["did"]
    s = pd.Series(coefs)
    rank = int((s <= s["CHN"]).sum())          # 1 = most negative
    perm_rows.append({"Sample": lab, **{f"DiD_if_treated_{k}": v for k, v in s.items()},
                      "China_rank_most_negative": rank, "N_units": len(s),
                      "permutation_p_one_sided": rank / len(s)})
perm = pd.DataFrame(perm_rows)
perm.round(4).to_csv(TABLES / "did_permutation.csv", index=False)
print(perm.round(3).T.to_string())

# ── Figure: permutation (placebo-in-space) estimates ────────────────────────
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
names = {"CHN": "China", "DEU": "Germany", "RUS": "Russia", "UZB": "Uzbekistan", "USA": "USA", "TUR": "Turkey"}
row = perm.iloc[0]
vals = {names[k.replace("DiD_if_treated_", "")]: row[k] for k in perm.columns if k.startswith("DiD_if_treated_")}
vals = dict(sorted(vals.items(), key=lambda kv: kv[1]))
fig, ax = plt.subplots(figsize=(7, 3.2))
cols = ["#c00000" if k == "China" else "#8faadc" for k in vals]
ax.barh(list(vals.keys()), list(vals.values()), color=cols)
ax.axvline(0, color="black", lw=0.8)
for i, v in enumerate(vals.values()):
    ax.text(v + (0.01 if v >= 0 else -0.01), i, f"{v:+.2f}", va="center",
            ha="left" if v >= 0 else "right", fontsize=9)
ax.set_xlabel("Post-2013 change in balance ratio relative to other partners")
ax.set_title("DiD estimate if each partner is treated as 'China' (2000-2023)", fontsize=10)
ax.set_xlim(-0.5, 0.55)
fig.text(0.01, 0.01, "Source: UN Comtrade; author's calculations (Script 44).", fontsize=7)
fig.tight_layout()
fig.savefig(ROOT / "Outputs" / "generated_figures" / "fig_did_permutation.png", dpi=200)
