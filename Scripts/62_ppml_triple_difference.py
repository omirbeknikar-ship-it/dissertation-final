"""
62_ppml_triple_difference.py
Main test of the reconstructed thesis (Chapter 5): did the composition of
Kazakhstan's exports to China change after 2013 in a way that is specific to
China, or did the same change happen in Kazakhstan's exports to the rest of
the world?

Unit: HS-2 chapter p x destination d (China, rest of world) x year t.
Estimator: Poisson pseudo-maximum likelihood (Santos Silva and Tenreyro 2006),
which keeps zero flows and is consistent under heteroskedasticity.
Fixed effects:
  product x year      absorbs world prices, Kazakhstan's supply of each
                      product, exchange rates and any shock common to all
                      destinations
  product x destination  absorbs the pre-existing orientation of each
                      product towards China (pipelines, distance, history)
Treatment terms: China x post x group, for the four product groups.
Standard errors clustered by HS-2 chapter.

The coefficient on China x post x agrifood is the post-2013 change in the
China/rest-of-world ratio of agri-food exports, relative to the pre-2014
average ratio for the same chapters, net of everything common to both
destinations. exp(b) - 1 is the proportional change in that ratio.

Interpretation limit: the terms capture every China-specific change after
2013. This includes BRI-era transport and border projects and phytosanitary
agreements, but also changes in China's own import demand that are unrelated
to the BRI. The design separates China-specific change from common shocks;
it does not identify which China-specific mechanism is responsible.

Samples:
  main      Kazakhstan-reported, 2005-2019 and 2023-2024 (2020-2022 excluded:
            confidentiality suppression of HS74/76/79 and missing World data)
  mirror    China-reported imports (CIF) for the China leg; ROW from
            Kazakhstan's data; same years except 2006 (not retrieved)
  pre-2020  main sample without 2023-2024 (removes the post-2022 sanctions
            and re-export period)
  alt-post  post defined from 2015 (Khorgos dry port) and from 2017
  placebo   2005-2013 only, fake post = 2010-2013
  no-gold   excluding HS71 (gold and precious metals, volatile)
  no-tiny   excluding chapters below USD 1m average exports

Outputs: Outputs/generated_tables/ppml_main.csv, ppml_event_study.csv,
         extensive_margin_lpm.csv
"""
import warnings
warnings.filterwarnings("ignore")
from pathlib import Path
import numpy as np
import pandas as pd
import pyfixest as pf

ROOT = Path(__file__).parent.parent
TABLES = ROOT / "Outputs" / "generated_tables"
GROUPS = ["energy", "metals_ores", "agrifood", "other"]
EXCL = {2020, 2021, 2022}

p = pd.read_csv(ROOT / "Collected_Raw_Data" / "hs2_panel_long.csv")
w = p.pivot_table(index=["year", "hs2", "group"], columns="flow", values="value_usd").reset_index()


def build(china_col="kz_x_chn", years=None):
    """Balanced product x destination x year panel with zeros."""
    d = w.copy()
    d = d[~d["year"].isin(EXCL)]
    d = d[d["kz_x_wld"].notna() | d["kz_x_chn"].notna()]
    yrs = sorted(d["year"].unique()) if years is None else years
    if china_col == "cn_m_kaz":
        yrs = [y for y in yrs if w.loc[w["year"] == y, "cn_m_kaz"].notna().any()]
    prods = d.groupby("hs2")["group"].first()
    idx = pd.MultiIndex.from_product([yrs, prods.index], names=["year", "hs2"])
    b = d.set_index(["year", "hs2"]).reindex(idx).reset_index()
    b["group"] = b["hs2"].map(prods)
    b[["kz_x_wld", "kz_x_chn", "cn_m_kaz"]] = b[["kz_x_wld", "kz_x_chn", "cn_m_kaz"]].fillna(0)
    b["row"] = (b["kz_x_wld"] - b["kz_x_chn"]).clip(lower=0)
    chn = b[["year", "hs2", "group", china_col]].rename(columns={china_col: "value"}).assign(china=1)
    row = b[["year", "hs2", "group", "row"]].rename(columns={"row": "value"}).assign(china=0)
    out = pd.concat([chn, row], ignore_index=True)
    out["pt"] = out["hs2"].astype(str) + "_" + out["year"].astype(str)
    out["pd"] = out["hs2"].astype(str) + "_" + out["china"].astype(str)
    out["value_m"] = out["value"] / 1e6
    # drop product-destination pairs that are always zero (no information under PPML)
    keep = out.groupby("pd")["value"].transform("sum") > 0
    return out[keep].copy()


def add_terms(d, post_start=2014):
    d = d.copy()
    d["post"] = (d["year"] >= post_start).astype(int)
    for g in GROUPS:
        d[f"cxp_{g}"] = d["china"] * d["post"] * (d["group"] == g)
    return d


def fit(d, label):
    fml = "value_m ~ " + " + ".join(f"cxp_{g}" for g in GROUPS) + " | pt + pd"
    m = pf.fepois(fml, data=d, vcov={"CRV1": "hs2"})
    t = m.tidy()
    r = {"sample": label, "N": m._N, "n_chapters": d["hs2"].nunique(),
         "years": f"{d['year'].min()}-{d['year'].max()} ({d['year'].nunique()} yrs)"}
    for g in GROUPS:
        k = f"cxp_{g}"
        if k in t.index:
            r[f"{g}_b"] = t.loc[k, "Estimate"]
            r[f"{g}_se"] = t.loc[k, "Std. Error"]
            r[f"{g}_p"] = t.loc[k, "Pr(>|t|)"]
            r[f"{g}_pct_change"] = 100 * (np.exp(t.loc[k, "Estimate"]) - 1)
            if d.loc[d["group"] == g, "hs2"].nunique() < 2:
                # one chapter = one cluster: clustered SE is degenerate, no valid inference
                r[f"{g}_se"] = np.nan
                r[f"{g}_p"] = np.nan
    return r


res = []
base = build()
res.append(fit(add_terms(base), "Main: KZ-reported, 2005-19 & 2023-24"))
res.append(fit(add_terms(build("cn_m_kaz")), "Mirror: China-reported imports for China leg"))
res.append(fit(add_terms(base[base["year"] <= 2019]), "Pre-2020 only (2005-2019)"))
res.append(fit(add_terms(base, 2015), "Post from 2015 (Khorgos dry port)"))
res.append(fit(add_terms(base, 2017), "Post from 2017"))
res.append(fit(add_terms(base[base["hs2"] != 71]), "Excluding HS71 (gold)"))
avg = base.groupby("hs2")["value"].mean()
res.append(fit(add_terms(base[base["hs2"].isin(avg[avg > 1e6].index)]), "Chapters with mean > USD 1m"))
pl = base[base["year"] <= 2013]
res.append(fit(add_terms(pl, 2010), "Placebo: 2005-2013, fake post = 2010"))
res = pd.DataFrame(res)
res.round(4).to_csv(TABLES / "ppml_main.csv", index=False)
show = ["sample", "N"] + [f"{g}_{s}" for g in GROUPS for s in ("b", "p")]
print(res[show].round(3).to_string())

# ── Event study: China x year x group, base = 2013 ──────────────────────────
ev = base.copy()
years = sorted(ev["year"].unique())
terms = []
for g in ["energy", "metals_ores", "agrifood"]:
    for y in years:
        if y == 2013:
            continue
        c = f"e_{g}_{y}"
        ev[c] = ev["china"] * (ev["year"] == y) * (ev["group"] == g)
        terms.append(c)
m = pf.fepois("value_m ~ " + " + ".join(terms) + " | pt + pd", data=ev, vcov={"CRV1": "hs2"})
t = m.tidy()
es = []
for c in terms:
    y = int(c.rsplit("_", 1)[1])
    g = c[2:].rsplit("_", 1)[0]
    if c in t.index:
        es.append({"group": g, "year": y, "b": t.loc[c, "Estimate"], "se": t.loc[c, "Std. Error"],
                   "p": t.loc[c, "Pr(>|t|)"]})
for g in ["energy", "metals_ores", "agrifood"]:
    es.append({"group": g, "year": 2013, "b": 0.0, "se": 0.0, "p": np.nan})
es = pd.DataFrame(es).sort_values(["group", "year"])
es["ci_lo"] = es["b"] - 1.96 * es["se"]
es["ci_hi"] = es["b"] + 1.96 * es["se"]
es.round(4).to_csv(TABLES / "ppml_event_study.csv", index=False)
print(es.pivot(index="year", columns="group", values="b").round(2).to_string())

# Joint pre-trend test for agri-food (2005-2012 leads), Wald on cluster vcov
lead = [f"e_agrifood_{y}" for y in years if y < 2013]
b = t.loc[lead, "Estimate"].values
V = m._vcov[np.ix_([m._coefnames.index(c) for c in lead], [m._coefnames.index(c) for c in lead])]
W = float(b @ np.linalg.pinv(V) @ b)
from scipy import stats
print(f"Agri-food pre-2013 leads joint Wald = {W:.2f}, df = {len(lead)}, p = {1 - stats.chi2.cdf(W, len(lead)):.4f}")
pd.DataFrame([{"test": "agrifood leads 2005-2012 jointly zero", "wald": W, "df": len(lead),
               "p": 1 - stats.chi2.cdf(W, len(lead))}]).to_csv(TABLES / "ppml_pretrend_test.csv", index=False)

# ── Trend-break test: does the China-specific trend change after 2013? ─────
# value ~ China x group x (t - 2013) + China x group x (t - 2013) x post | pt + pd
tb = add_terms(base)
tb["tc"] = tb["year"] - 2013
tb_terms = []
for g in GROUPS:
    tb[f"tr_{g}"] = tb["china"] * (tb["group"] == g) * tb["tc"]
    tb[f"trpost_{g}"] = tb[f"tr_{g}"] * tb["post"]
    tb_terms += [f"tr_{g}", f"trpost_{g}"]
mt = pf.fepois("value_m ~ " + " + ".join(tb_terms) + " | pt + pd", data=tb, vcov={"CRV1": "hs2"})
tt = mt.tidy()
rows = []
for g in GROUPS:
    a, b = f"tr_{g}", f"trpost_{g}"
    if a in tt.index and b in tt.index:
        ia, ib = mt._coefnames.index(a), mt._coefnames.index(b)
        V = mt._vcov
        post_slope = tt.loc[a, "Estimate"] + tt.loc[b, "Estimate"]
        se_post = float(np.sqrt(V[ia, ia] + V[ib, ib] + 2 * V[ia, ib]))
        rows.append({"group": g, "n_chapters": int(base.loc[base["group"] == g, "hs2"].nunique()),
                     "pre_slope": tt.loc[a, "Estimate"], "pre_slope_p": tt.loc[a, "Pr(>|t|)"],
                     "slope_change": tt.loc[b, "Estimate"], "slope_change_se": tt.loc[b, "Std. Error"],
                     "slope_change_p": tt.loc[b, "Pr(>|t|)"], "post_slope": post_slope,
                     "post_slope_se": se_post})
        if rows[-1]["n_chapters"] < 2:
            for k in ("pre_slope_p", "slope_change_se", "slope_change_p", "post_slope_se"):
                rows[-1][k] = np.nan
tbr = pd.DataFrame(rows)
tbr.round(4).to_csv(TABLES / "ppml_trend_break.csv", index=False)
print(tbr.round(3).to_string())

# Chapters per group (clusters contributing to each coefficient)
base.groupby("group")["hs2"].nunique().rename("n_chapters").to_csv(TABLES / "ppml_chapters_per_group.csv")

# ── Extensive margin: linear probability of exporting > USD 1m ──────────────
em = add_terms(base)
em["active"] = (em["value"] > 1e6).astype(float)
lpm = pf.feols("active ~ " + " + ".join(f"cxp_{g}" for g in GROUPS) + " | pt + pd", data=em,
               vcov={"CRV1": "hs2"})
lt = lpm.tidy()
em2 = em.assign(cxp_all=em["china"] * em["post"])
lpm2 = pf.feols("active ~ cxp_all | pt + pd", data=em2, vcov={"CRV1": "hs2"})
lt2 = lpm2.tidy()
out = lt[["Estimate", "Std. Error", "Pr(>|t|)"]].copy()
out.loc["cxp_all (pooled)"] = lt2.loc["cxp_all", ["Estimate", "Std. Error", "Pr(>|t|)"]].values
pre_mean = em[(em["china"] == 1) & (em["post"] == 0)].groupby("group")["active"].mean()
out["pre_mean_china_by_group"] = [pre_mean.get(i.replace("cxp_", ""), np.nan) for i in out.index]
out.loc["cxp_all (pooled)", "pre_mean_china_by_group"] = em[(em["china"] == 1) & (em["post"] == 0)]["active"].mean()
out.round(4).to_csv(TABLES / "extensive_margin_lpm.csv")
print(out.round(3).to_string())
