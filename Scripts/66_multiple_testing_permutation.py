"""
66_multiple_testing_permutation.py
Inference safeguards for the PPML results (Chapter 5.7 and 6.6).

1. Holm-Bonferroni adjustment within each family of tests:
   - main triple difference: the three group coefficients with valid
     inference (metals and ores, agri-food, other); energy has none.
   - trend-break test: the three slope-change coefficients.
2. One-sided test of the BRI-acceleration hypothesis (delta > 0) for each
   group, which is the hypothesis the timing argument actually needs.
3. Randomisation (permutation) inference for the agri-food results: 24
   chapters are drawn at random from the 96 non-energy chapters and labelled
   "pseudo agri-food"; the China x Post coefficient and the slope-change
   coefficient are re-estimated for each draw (single-term models with the
   same fixed effects). The p-value is the share of draws at least as extreme
   as the actual agri-food estimate. This answers: is agri-food unusual among
   Kazakhstan's export chapters, or would a random set of chapters of the same
   size show a similar China-specific change?

Outputs: Outputs/generated_tables/multiple_testing.csv, permutation_agrifood.csv
"""
import warnings
warnings.filterwarnings("ignore")
from pathlib import Path
import numpy as np
import pandas as pd
import pyfixest as pf
from scipy import stats

ROOT = Path(__file__).parent.parent
T = ROOT / "Outputs" / "generated_tables"
RNG = np.random.default_rng(20261031)
N_PERM = 300

# reuse the panel builder from Script 62 without re-running its estimations
src = (ROOT / "Scripts" / "62_ppml_triple_difference.py").read_text()
src = src.split("res = []")[0]
ns = {"__file__": str(ROOT / "Scripts" / "62_ppml_triple_difference.py")}
exec(compile(src, "62_builder", "exec"), ns)
base = ns["add_terms"](ns["build"]())


def holm(pvals):
    p = np.asarray(pvals, float)
    order = np.argsort(p)
    m = len(p)
    adj = np.empty(m)
    run = 0.0
    for k, i in enumerate(order):
        run = max(run, (m - k) * p[i])
        adj[i] = min(1.0, run)
    return adj


main = pd.read_csv(T / "ppml_main.csv").iloc[0]
tb = pd.read_csv(T / "ppml_trend_break.csv").set_index("group")
rows = []
G3 = ["metals_ores", "agrifood", "other"]
adj = holm([main[f"{g}_p"] for g in G3])
for g, a in zip(G3, adj):
    rows.append({"family": "Main triple difference (China x Post x group)", "group": g,
                 "estimate": main[f"{g}_b"], "p_raw": main[f"{g}_p"], "p_holm": a})
adj = holm([tb.loc[g, "slope_change_p"] for g in G3])
for g, a in zip(G3, adj):
    d, se = tb.loc[g, "slope_change"], tb.loc[g, "slope_change_se"]
    rows.append({"family": "Trend break (change in China-specific slope after 2013)", "group": g,
                 "estimate": d, "p_raw": tb.loc[g, "slope_change_p"], "p_holm": a,
                 "p_one_sided_acceleration": 1 - stats.norm.cdf(d / se),
                 "ci95_upper": d + 1.96 * se})
mt = pd.DataFrame(rows)
mt.round(4).to_csv(T / "multiple_testing.csv", index=False)
print(mt.round(4).to_string())

# ── Randomisation inference for agri-food ──────────────────────────────────
d = base.copy()
d["tc"] = d["year"] - 2013
nonenergy = sorted(d.loc[d["group"] != "energy", "hs2"].unique())
agri = sorted(d.loc[d["group"] == "agrifood", "hs2"].unique())


def estimates(chapters):
    x = d.copy()
    sel = x["hs2"].isin(chapters)
    x["cxp"] = x["china"] * x["post"] * sel
    x["tr"] = x["china"] * sel * x["tc"]
    x["trpost"] = x["tr"] * x["post"]
    b1 = pf.fepois("value_m ~ cxp | pt + pd", data=x, vcov="iid").coef()["cxp"]
    b2 = pf.fepois("value_m ~ tr + trpost | pt + pd", data=x, vcov="iid").coef()["trpost"]
    return b1, b2


obs_post, obs_delta = estimates(agri)
draws = []
for i in range(N_PERM):
    pick = RNG.choice(nonenergy, size=len(agri), replace=False)
    try:
        draws.append(estimates(pick))
    except Exception:
        continue
draws = np.array(draws)
perm = pd.DataFrame([{
    "statistic": "China x Post coefficient (single-term model)", "observed_agrifood": obs_post,
    "n_draws": len(draws), "share_draws_ge_observed": float(np.mean(draws[:, 0] >= obs_post)),
    "draw_median": float(np.median(draws[:, 0])), "draw_p95": float(np.percentile(draws[:, 0], 95))},
    {"statistic": "Slope change after 2013 (single-group trend model)", "observed_agrifood": obs_delta,
     "n_draws": len(draws), "share_draws_le_observed": float(np.mean(draws[:, 1] <= obs_delta)),
     "share_draws_ge_observed": float(np.mean(draws[:, 1] >= obs_delta)),
     "draw_median": float(np.median(draws[:, 1])), "draw_p5": float(np.percentile(draws[:, 1], 5))}])
perm.round(4).to_csv(T / "permutation_agrifood.csv", index=False)
print(perm.round(3).T.to_string())
