"""
67_robustness_baselines_comparators.py
Final-audit robustness checks for the comparison-adjusted decomposition (§6.2, §6.6, §6.7).

A. Kazakhstan-partner comparison (shift-share) under alternative base and end
   periods: bases 2011-2013 average, 2012, 2013, 2014; ends 2019, 2023, 2024,
   2023-2024 average. Exports: HS-2 chapters, China leg China-reported, RoW
   growth Kazakhstan-reported. Imports: totals, China leg China-reported, RoW
   growth Kazakhstan-reported (World minus China).

B. China-neighbour comparison for BOTH flows, using China's own reports only
   (one reporter, one valuation per flow): Kazakhstan-specific change =
   actual - base x growth of the comparator. Comparator sets: World; Russia;
   Central Asia excluding Kazakhstan (Kyrgyzstan, Uzbekistan, Tajikistan,
   Turkmenistan); Central Asia + Russia. Weighting: value-weighted aggregate
   growth, and the median of the individual partners' growth factors.

C. Turnover (exports + imports): the same comparisons, to relate the thesis to
   studies that measure BRI effects on trade volume.

Outputs: Outputs/generated_tables/robust_kz_partner_grid.csv,
         robust_china_neighbour_grid.csv
"""
from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).parent.parent
RAW = ROOT / "Collected_Raw_Data" / "raw_downloads"
T = ROOT / "Outputs" / "generated_tables"

p = pd.read_csv(ROOT / "Collected_Raw_Data" / "hs2_panel_long.csv")
w = p.pivot_table(index=["year", "hs2", "group"], columns="flow", values="value_usd").reset_index()
w = w.fillna({"kz_x_chn": 0, "cn_m_kaz": 0})
w["row"] = (w["kz_x_wld"] - w["kz_x_chn"]).clip(lower=0)

kzm = {}
for line in (RAW / "comtrade_totals_imports_and_china_exports.txt").read_text().splitlines():
    if line.startswith("KZM|"):
        _, y, body = line.split("|")
        kzm[int(y)] = {int(k): float(v) for k, v in (x.split(":") for x in body.split(";"))}
cn = {}
for line in (RAW / "comtrade_china_totals_by_partner.txt").read_text().splitlines():
    if line[:2] in ("X|", "M|"):
        f, y, body = line.split("|")
        cn[(f, int(y))] = {int(k): float(v) for k, v in (x.split(":") for x in body.split(";"))}

PERIODS = {"2011-13 avg": [2011, 2012, 2013], "2012": [2012], "2013": [2013], "2014": [2014],
           "2019": [2019], "2023": [2023], "2024": [2024], "2023-24 avg": [2023, 2024]}
BASES = ["2011-13 avg", "2012", "2013", "2014"]
ENDS = ["2019", "2023", "2024", "2023-24 avg"]


def chap(years):
    d = w[w["year"].isin(years)].groupby(["hs2", "group"])[["cn_m_kaz", "row"]].mean()
    return d.reset_index().set_index("hs2")


def kz_partner(base, end):
    a, b = chap(PERIODS[base]), chap(PERIODS[end])
    idx = a.index.union(b.index)
    a, b = a.reindex(idx), b.reindex(idx)
    grp = a["group"].fillna(b["group"])
    ra, rb = a["row"].fillna(0), b["row"].fillna(0)
    gg = rb.groupby(grp).sum() / ra.groupby(grp).sum()
    growth = np.where(ra >= 1e6, rb / ra.replace(0, np.nan), grp.map(gg))
    x0, x1 = a["cn_m_kaz"].fillna(0), b["cn_m_kaz"].fillna(0)
    cf = x0 * growth
    ex_cs = (x1 - cf).sum()
    ex_ch = (x1 - x0).sum()
    m = lambda yrs, k: np.mean([kzm[y][k] for y in yrs])
    c = lambda yrs: np.mean([cn[("X", y)][398] for y in yrs])
    row0 = m(PERIODS[base], 0) - m(PERIODS[base], 156)
    row1 = m(PERIODS[end], 0) - m(PERIODS[end], 156)
    m0, m1 = c(PERIODS[base]), c(PERIODS[end])
    im_cs = m1 - m0 * row1 / row0
    im_ch = m1 - m0
    bal_ch = ex_ch - im_ch
    bal_cs = ex_cs - im_cs
    return {"base": base, "end": end, "balance_change_bn": bal_ch / 1e9,
            "balance_china_specific_bn": bal_cs / 1e9,
            "china_specific_share_pct": 100 * bal_cs / bal_ch if bal_ch < 0 else np.nan,
            "exports_china_specific_bn": ex_cs / 1e9, "imports_china_specific_bn": im_cs / 1e9,
            "turnover_china_specific_bn": (ex_cs + im_cs) / 1e9}


grid = pd.DataFrame([kz_partner(b, e) for b in BASES for e in ENDS])
grid.round(3).to_csv(T / "robust_kz_partner_grid.csv", index=False)
pd.set_option("display.width", 250)
print("A. Kazakhstan-partner comparison\n", grid.round(2).to_string())

SETS = {"World": [0], "Russia": [643], "Central Asia ex-KZ": [417, 860, 762, 795],
        "Central Asia ex-KZ + Russia": [417, 860, 762, 795, 643]}


def neighbour(flow, base, end, comp, weighting):
    v = lambda yrs, k: np.mean([cn[(flow, y)][k] for y in yrs])
    k0, k1 = v(PERIODS[base], 398), v(PERIODS[end], 398)
    codes = SETS[comp]
    if weighting == "value-weighted":
        g = sum(v(PERIODS[end], c) for c in codes) / sum(v(PERIODS[base], c) for c in codes)
    else:
        g = float(np.median([v(PERIODS[end], c) / v(PERIODS[base], c) for c in codes]))
    return k1 - k0 * g, k1 - k0, g


rows = []
for base in BASES:
    for end in ENDS:
        for comp in SETS:
            for wt in (["value-weighted"] if len(SETS[comp]) == 1 else ["value-weighted", "median"]):
                xs, xch, gx = neighbour("M", base, end, comp, wt)   # China's imports = KZ exports
                ms, mch, gm = neighbour("X", base, end, comp, wt)   # China's exports = KZ imports
                rows.append({"base": base, "end": end, "comparator": comp, "weighting": wt,
                             "kz_exports_growth": (xch + 0) and None, "comp_import_growth": gx,
                             "comp_export_growth": gm,
                             "exports_kz_specific_bn": xs / 1e9, "imports_kz_specific_bn": ms / 1e9,
                             "balance_kz_specific_bn": (xs - ms) / 1e9,
                             "turnover_kz_specific_bn": (xs + ms) / 1e9,
                             "balance_change_bn": (xch - mch) / 1e9})
nb = pd.DataFrame(rows).drop(columns=["kz_exports_growth"])
nb.round(3).to_csv(T / "robust_china_neighbour_grid.csv", index=False)
print("B. China-neighbour comparison (China-reported)\n",
      nb[(nb["base"] == "2013") & (nb["end"] == "2024")].round(2).to_string())
s = nb.groupby(["comparator", "weighting"])[["imports_kz_specific_bn", "balance_kz_specific_bn"]].agg(["min", "max"])
print(s.round(2).to_string())

# ── D. China-specific export component by product group across the grid ────
SM = [26, 28, 72, 74, 79]
grp_rows = []
for base in BASES:
    for end in ENDS:
        a, b = chap(PERIODS[base]), chap(PERIODS[end])
        idx = a.index.union(b.index)
        a, b = a.reindex(idx), b.reindex(idx)
        grp = a["group"].fillna(b["group"])
        ra, rb = a["row"].fillna(0), b["row"].fillna(0)
        gg = rb.groupby(grp).sum() / ra.groupby(grp).sum()
        growth = np.where(ra >= 1e6, rb / ra.replace(0, np.nan), grp.map(gg))
        cs = b["cn_m_kaz"].fillna(0) - a["cn_m_kaz"].fillna(0) * growth
        r = {"base": base, "end": end}
        r.update({f"{g}_bn": v / 1e9 for g, v in cs.groupby(grp).sum().items()})
        r["strategic_minerals_bn"] = cs[cs.index.isin(SM)].sum() / 1e9
        grp_rows.append(r)
gg_ = pd.DataFrame(grp_rows)
gg_.round(3).to_csv(T / "robust_export_groups_grid.csv", index=False)
print("D. China-specific export components by group\n", gg_.round(2).to_string())
