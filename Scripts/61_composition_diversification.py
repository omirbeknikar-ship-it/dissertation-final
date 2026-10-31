"""
61_composition_diversification.py
Descriptive evidence for the reconstructed thesis (Chapter 4).

Uses Collected_Raw_Data/hs2_panel_long.csv (Script 60).
Kazakhstan-reported product data for 2020-2022 are excluded from all
product-level comparisons: copper (HS74), zinc (HS79) and aluminium (HS76)
are absent or near zero in those years in Kazakhstan's own returns although
China reports importing them (see table mirror_suppression.csv). 2020 and
2022 Kazakhstan-to-World chapter data could not be retrieved.

Outputs (Outputs/generated_tables/):
  composition_kz_exports_to_china.csv   value and share by product group, both sources
  china_share_by_group.csv              China's share of Kazakhstan's exports, by group
  diversification_indices.csv           HHI, number of chapters > USD 1m, top-3 share
  mirror_suppression.csv                KZ-reported vs China-reported for HS74/76/79
  trade_balance_decomposition.csv       change in the bilateral balance by component
  import_composition_china_reported.csv China-reported exports to KZ, snapshot years
  aiddata_by_sector_period.csv          Chinese official finance commitments to KZ
  russia_manufactures_check.csv         KZ exports of HS84/85/87 to Russia vs world
"""
from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).parent.parent
RAW = ROOT / "Collected_Raw_Data" / "raw_downloads"
TABLES = ROOT / "Outputs" / "generated_tables"
SUPPRESSED = {2020, 2021, 2022}

p = pd.read_csv(ROOT / "Collected_Raw_Data" / "hs2_panel_long.csv")
w = p.pivot_table(index=["year", "hs2", "group"], columns="flow", values="value_usd").reset_index()
w["kz_x_row"] = w["kz_x_wld"] - w["kz_x_chn"].fillna(0)
GROUPS = ["energy", "metals_ores", "agrifood", "other"]

# ── 1. Composition of exports to China (both reporters) ─────────────────────
g = w.groupby(["year", "group"])[["kz_x_chn", "cn_m_kaz", "kz_x_wld", "kz_x_row"]].sum(min_count=1)
comp = []
for src in ["kz_x_chn", "cn_m_kaz"]:
    t = g[src].unstack()[GROUPS]
    t = t[t.sum(axis=1) > 0]
    sh = t.div(t.sum(axis=1), axis=0) * 100
    for y in t.index:
        row = {"source": src, "year": y, "total_bn": t.loc[y].sum() / 1e9}
        for c in GROUPS:
            row[f"{c}_bn"] = t.loc[y, c] / 1e9
            row[f"{c}_share_pct"] = sh.loc[y, c]
        comp.append(row)
comp = pd.DataFrame(comp)
comp.round(3).to_csv(TABLES / "composition_kz_exports_to_china.csv", index=False)

# ── 2. China's share of Kazakhstan's exports by group (KZ-reported) ─────────
cs = (g["kz_x_chn"] / g["kz_x_wld"] * 100).unstack()[GROUPS]
cs = cs[~cs.index.isin(SUPPRESSED) & g["kz_x_wld"].unstack().sum(axis=1).gt(0).reindex(cs.index)]
tot = w.groupby("year")[["kz_x_chn", "kz_x_wld"]].sum()
cs["all_goods"] = (tot["kz_x_chn"] / tot["kz_x_wld"] * 100).reindex(cs.index)
cs.round(2).to_csv(TABLES / "china_share_by_group.csv")
print("China share of KZ exports by group (%)\n", cs.round(1).to_string())


# ── 3. Diversification indices ──────────────────────────────────────────────
def indices(s):
    s = s.dropna()
    s = s[s > 0]
    if s.sum() == 0:
        return pd.Series({"HHI": np.nan, "n_chapters_gt_1m": np.nan, "top3_share_pct": np.nan,
                          "nonresource_share_pct": np.nan})
    sh = s / s.sum()
    return pd.Series({"HHI": (sh ** 2).sum(), "n_chapters_gt_1m": int((s > 1e6).sum()),
                      "top3_share_pct": 100 * sh.sort_values(ascending=False).iloc[:3].sum()})


div = []
for col, lab in [("kz_x_chn", "KZ-reported exports to China"), ("cn_m_kaz", "China-reported imports from KZ"),
                 ("kz_x_row", "KZ-reported exports to rest of world")]:
    for y, s in w.groupby("year"):
        if col in ("kz_x_chn", "kz_x_row") and y in SUPPRESSED:
            continue
        x = s.set_index("hs2")[col]
        if x.dropna().sum() == 0:
            continue
        r = indices(x)
        nr = s.loc[~s["group"].isin(["energy", "metals_ores"]), col].sum()
        r["nonresource_share_pct"] = 100 * nr / x.sum()
        r["HHI_excl_HS27"] = indices(x.drop(27, errors="ignore"))["HHI"]
        div.append({"series": lab, "year": y, **r.to_dict()})
div = pd.DataFrame(div)
div.round(4).to_csv(TABLES / "diversification_indices.csv", index=False)
print(div.pivot(index="year", columns="series", values="n_chapters_gt_1m").to_string())

# ── 4. Mirror check of the 2020-2022 suppression ────────────────────────────
ms = w[w["hs2"].isin([74, 76, 79]) & w["year"].between(2017, 2024)]
ms = ms.pivot_table(index="year", columns="hs2", values=["kz_x_chn", "cn_m_kaz"]) / 1e6
ms.columns = [f"{a}_HS{b}_musd" for a, b in ms.columns]
ms.round(1).to_csv(TABLES / "mirror_suppression.csv")
print(ms.round(0).to_string())

# ── 5. Trade balance decomposition (China-reported, both directions) ────────
# Kazakhstan's balance with China = China's imports from KZ - China's exports to KZ.
# China-reported data are used because they show no product suppression.
cx = w.groupby("year")["cn_x_kaz"].sum(min_count=1).dropna()
rows = []
for y0, y1 in [(2013, 2019), (2019, 2024), (2013, 2024)]:
    r = {"from": y0, "to": y1}
    for gr in GROUPS:
        a = g.loc[(y0, gr), "cn_m_kaz"] if (y0, gr) in g.index else 0
        b = g.loc[(y1, gr), "cn_m_kaz"] if (y1, gr) in g.index else 0
        r[f"d_exports_{gr}_bn"] = (b - a) / 1e9
    r["d_exports_total_bn"] = sum(r[f"d_exports_{gr}_bn"] for gr in GROUPS)
    r["d_imports_total_bn"] = (cx.loc[y1] - cx.loc[y0]) / 1e9
    r["d_balance_bn"] = r["d_exports_total_bn"] - r["d_imports_total_bn"]
    r["balance_from_bn"] = (g.xs(y0)["cn_m_kaz"].sum() - cx.loc[y0]) / 1e9
    r["balance_to_bn"] = (g.xs(y1)["cn_m_kaz"].sum() - cx.loc[y1]) / 1e9
    rows.append(r)
dec = pd.DataFrame(rows)
dec.round(3).to_csv(TABLES / "trade_balance_decomposition.csv", index=False)
print(dec.round(2).T.to_string())

# ── 6. Import composition (China-reported exports to KZ) ────────────────────
IMP = {"machinery_84": [84], "electrical_85": [85], "vehicles_87": [87],
       "apparel_footwear_61_62_64": [61, 62, 64], "plastics_rubber_39_40": [39, 40],
       "iron_steel_articles_73": [73], "furniture_toys_misc_94_96": [94, 95, 96]}
imp = []
for y in sorted(cx.index):
    s = w[w["year"] == y].set_index("hs2")["cn_x_kaz"]
    r = {"year": y, "total_bn": s.sum() / 1e9}
    for k, codes in IMP.items():
        r[f"{k}_bn"] = s.reindex(codes).fillna(0).sum() / 1e9
    r["other_bn"] = r["total_bn"] - sum(r[f"{k}_bn"] for k in IMP)
    imp.append(r)
pd.DataFrame(imp).round(3).to_csv(TABLES / "import_composition_china_reported.csv", index=False)
print(pd.DataFrame(imp).round(2).to_string())

# ── 7. AidData: Chinese official finance to Kazakhstan ──────────────────────
aid = pd.read_excel(RAW / "aiddata_gcdf_v3.xlsx", sheet_name="GCDF_3.0")
aid = aid[(aid["Recipient ISO-3"] == "KAZ") & (aid["Recommended For Aggregates"] == "Yes")]
amt = "Amount (Constant USD 2021)"
aid["period"] = pd.cut(aid["Commitment Year"], [1999, 2008, 2013, 2017, 2021],
                       labels=["2000-2008", "2009-2013", "2014-2017", "2018-2021"])
t = aid.pivot_table(index="Sector Name", columns="period", values=amt, aggfunc="sum", observed=False) / 1e9
t["total"] = t.sum(axis=1)
t.loc["ALL SECTORS"] = t.sum()
cnt = aid.pivot_table(index="Sector Name", columns="period", values=amt, aggfunc="count", observed=False)
t.sort_values("total", ascending=False).round(3).to_csv(TABLES / "aiddata_by_sector_period.csv")
aid.groupby("Commitment Year")[amt].sum().div(1e9).round(3).to_csv(TABLES / "aiddata_by_year.csv")
print(t.sort_values("total", ascending=False).round(2).to_string())
print("Projects recommended for aggregates:", len(aid))

# ── 8. Re-export check: KZ exports of HS84/85/87 to Russia ──────────────────
ru = {}
for line in (RAW / "comtrade_hs2_kaz_exports_to_russia_selected.txt").read_text().splitlines():
    if line.startswith("#") or not line.strip():
        continue
    y, body = line.split("|")
    ru[int(y)] = sum(float(x.split(":")[1]) for x in body.split(";"))
chk = []
for y in ru:
    s = w[(w["year"] == y) & w["hs2"].isin([84, 85, 87])]
    chk.append({"year": y, "kz_x_russia_84_85_87_bn": ru[y] / 1e9,
                "kz_x_world_84_85_87_bn": s["kz_x_wld"].sum() / 1e9,
                "cn_x_kaz_84_85_87_bn": s["cn_x_kaz"].sum() / 1e9 if s["cn_x_kaz"].notna().any() else np.nan})
pd.DataFrame(chk).round(3).to_csv(TABLES / "russia_manufactures_check.csv", index=False)
print(pd.DataFrame(chk).round(2))

# ── 9. Agri-food chapters driving the growth (KZ-reported and mirror) ───────
AG = {10: "Cereals", 12: "Oilseeds", 15: "Animal/vegetable fats and oils", 23: "Food residues, fodder",
      11: "Milling products (flour)", 2: "Meat", 4: "Dairy, eggs, honey", 19: "Cereal preparations"}
rows = []
for hs, name in AG.items():
    for y in [2008, 2013, 2019, 2024]:
        s = w[(w["year"] == y) & (w["hs2"] == hs)]
        if s.empty:
            continue
        s = s.iloc[0]
        rows.append({"hs2": hs, "chapter": name, "year": y, "kz_x_chn_musd": s["kz_x_chn"] / 1e6,
                     "cn_m_kaz_musd": s["cn_m_kaz"] / 1e6, "kz_x_wld_musd": s["kz_x_wld"] / 1e6,
                     "china_share_pct": 100 * s["kz_x_chn"] / s["kz_x_wld"] if s["kz_x_wld"] else np.nan})
ag = pd.DataFrame(rows)
ag.round(2).to_csv(TABLES / "agrifood_chapters.csv", index=False)
print(ag.pivot(index="chapter", columns="year", values="kz_x_chn_musd").round(1).to_string())
print(ag.pivot(index="chapter", columns="year", values="china_share_pct").round(1).to_string())
