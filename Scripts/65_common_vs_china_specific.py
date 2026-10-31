"""
65_common_vs_china_specific.py
Central decomposition of the thesis (Chapter 6.2): how much of the change in
Kazakhstan's bilateral balance with China is common to Kazakhstan's trade with
all partners, and how much is specific to China?

Logic (shift-share counterfactual). If Kazakhstan's trade with China in each
product had grown at the same rate as its trade in that product with the rest
of the world (RoW), the bilateral flow would have been
    CF_p,t1 = CN_p,t0 x (RoW_p,t1 / RoW_p,t0).
Then, for each flow,
    common component        = sum_p (CF_p,t1 - CN_p,t0)
    China-specific component = sum_p (CN_p,t1 - CF_p,t1)
and the two add up to the actual change. The BRI, like any bilateral factor
(China's own demand, bilateral policy, bilateral logistics), can only act
through the China-specific component, so that component is an upper bound on
the change the BRI could account for. It is a bound, not an estimate of a BRI
effect.

Exports: China leg = China-reported imports from KZ (no suppression), by HS-2
chapter; RoW growth = KZ-reported exports to World minus China, by chapter.
Where a chapter's RoW base is below USD 1m, the product group's RoW growth is
used. Robustness: KZ-reported China leg.
Imports: product detail for KZ's imports from RoW is not available, so the
import side is aggregate. China leg = China-reported exports to KZ; RoW growth
= KZ-reported imports from World minus China. Robustness: KZ-reported China
leg. Periods: 2013-2019, 2019-2024, 2013-2024 (2020-2022 avoided because of
the reporting break).

Also: growth of China's exports to Kazakhstan vs to Kyrgyzstan, Uzbekistan,
Russia and the World (regional comparison for the import side).

Outputs: Outputs/generated_tables/balance_common_vs_china_specific.csv,
         export_components_by_group.csv, china_exports_regional_comparison.csv
"""
from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).parent.parent
RAW = ROOT / "Collected_Raw_Data" / "raw_downloads"
T = ROOT / "Outputs" / "generated_tables"
GROUPS = ["energy", "metals_ores", "agrifood", "other"]
PERIODS = [(2013, 2019), (2019, 2024), (2013, 2024)]

p = pd.read_csv(ROOT / "Collected_Raw_Data" / "hs2_panel_long.csv")
w = p.pivot_table(index=["year", "hs2", "group"], columns="flow", values="value_usd").reset_index()
w = w.fillna({"kz_x_chn": 0, "cn_m_kaz": 0})
w["row"] = (w["kz_x_wld"] - w["kz_x_chn"]).clip(lower=0)

# totals file
tot = {}
for line in (RAW / "comtrade_totals_imports_and_china_exports.txt").read_text().splitlines():
    if line.startswith("#") or not line.strip():
        continue
    blk, y, body = line.split("|")
    tot[(blk, int(y))] = {int(k): float(v) for k, v in (x.split(":") for x in body.split(";"))}


def export_components(t0, t1, china_col):
    a = w[w["year"] == t0].set_index("hs2")
    b = w[w["year"] == t1].set_index("hs2")
    idx = a.index.union(b.index)
    a, b = a.reindex(idx), b.reindex(idx)
    grp = a["group"].fillna(b["group"])
    rowa, rowb = a["row"].fillna(0), b["row"].fillna(0)
    g_growth = rowb.groupby(grp).sum() / rowa.groupby(grp).sum()
    growth = np.where(rowa >= 1e6, rowb / rowa.replace(0, np.nan), grp.map(g_growth))
    cn0, cn1 = a[china_col].fillna(0), b[china_col].fillna(0)
    cf = cn0 * growth
    df = pd.DataFrame({"group": grp, "cn0": cn0, "cn1": cn1, "cf": cf})
    out = df.groupby("group")[["cn0", "cn1", "cf"]].sum()
    out["actual_change"] = out["cn1"] - out["cn0"]
    out["common"] = out["cf"] - out["cn0"]
    out["china_specific"] = out["cn1"] - out["cf"]
    return out


def import_components(t0, t1, china_source):
    kz0, kz1 = tot[("KZM", t0)], tot[("KZM", t1)]
    row_growth = (kz1[0] - kz1[156]) / (kz0[0] - kz0[156])
    if china_source == "china_reported":
        m0, m1 = tot[("CNX", t0)][398], tot[("CNX", t1)][398]
    else:
        m0, m1 = kz0[156], kz1[156]
    cf = m0 * row_growth
    return {"m0": m0, "m1": m1, "row_growth": row_growth, "actual_change": m1 - m0,
            "common": cf - m0, "china_specific": m1 - cf}


rows, grp_rows = [], []
for t0, t1 in PERIODS:
    for label, xcol, msrc in [("China-reported China legs (main)", "cn_m_kaz", "china_reported"),
                              ("Kazakhstan-reported China legs (robustness)", "kz_x_chn", "kz_reported")]:
        ex = export_components(t0, t1, xcol)
        im = import_components(t0, t1, msrc)
        r = {"period": f"{t0}-{t1}", "source": label,
             "exports_change_bn": ex["actual_change"].sum() / 1e9,
             "exports_common_bn": ex["common"].sum() / 1e9,
             "exports_china_specific_bn": ex["china_specific"].sum() / 1e9,
             "imports_change_bn": im["actual_change"] / 1e9,
             "imports_common_bn": im["common"] / 1e9,
             "imports_china_specific_bn": im["china_specific"] / 1e9,
             "kz_imports_row_growth": im["row_growth"]}
        r["balance_change_bn"] = r["exports_change_bn"] - r["imports_change_bn"]
        r["balance_common_bn"] = r["exports_common_bn"] - r["imports_common_bn"]
        r["balance_china_specific_bn"] = r["exports_china_specific_bn"] - r["imports_china_specific_bn"]
        rows.append(r)
        for g in GROUPS:
            grp_rows.append({"period": f"{t0}-{t1}", "source": label, "group": g,
                             "actual_change_bn": ex.loc[g, "actual_change"] / 1e9,
                             "common_bn": ex.loc[g, "common"] / 1e9,
                             "china_specific_bn": ex.loc[g, "china_specific"] / 1e9})
res = pd.DataFrame(rows)
res.round(3).to_csv(T / "balance_common_vs_china_specific.csv", index=False)
gr = pd.DataFrame(grp_rows)
gr.round(3).to_csv(T / "export_components_by_group.csv", index=False)
pd.set_option("display.width", 250)
print(res.round(2).T.to_string())
print(gr[gr["source"].str.startswith("China")].round(2).to_string())

# Strategic minerals sub-aggregate: HS 26, 28, 72, 74, 79
SM = [26, 28, 72, 74, 79]
sm_rows = []
for t0, t1 in PERIODS:
    a = w[(w["year"] == t0) & w["hs2"].isin(SM)].set_index("hs2")
    b = w[(w["year"] == t1) & w["hs2"].isin(SM)].set_index("hs2")
    g = b["row"] / a["row"]
    cf = a["cn_m_kaz"] * g
    sm_rows.append({"period": f"{t0}-{t1}", "actual_change_bn": (b["cn_m_kaz"].sum() - a["cn_m_kaz"].sum()) / 1e9,
                    "common_bn": (cf.sum() - a["cn_m_kaz"].sum()) / 1e9,
                    "china_specific_bn": (b["cn_m_kaz"].sum() - cf.sum()) / 1e9})
sm = pd.DataFrame(sm_rows)
sm.round(3).to_csv(T / "strategic_minerals_components.csv", index=False)
print("Strategic minerals (HS 26, 28, 72, 74, 79)\n", sm.round(2).to_string())

# Regional comparison: growth of China's exports by destination
names = {0: "World", 398: "Kazakhstan", 417: "Kyrgyzstan", 860: "Uzbekistan", 643: "Russia"}
reg = []
for code, n in names.items():
    v = {y: tot[("CNX", y)][code] for y in (2013, 2019, 2024)}
    reg.append({"destination": n, "2013_bn": v[2013] / 1e9, "2019_bn": v[2019] / 1e9, "2024_bn": v[2024] / 1e9,
                "growth_2013_2019": v[2019] / v[2013], "growth_2019_2024": v[2024] / v[2019]})
reg = pd.DataFrame(reg)
reg.round(3).to_csv(T / "china_exports_regional_comparison.csv", index=False)
print(reg.round(2).to_string())
