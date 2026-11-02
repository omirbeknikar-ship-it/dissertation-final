"""
64_two_sided_dependence.py
Two-sided dependence by chapter, 2024 (Chapter 7 discussion).
  - Kazakhstan's dependence on China: China's share of Kazakhstan's exports of
    the chapter (Kazakhstan-reported exports to China / to World).
  - China's dependence on Kazakhstan: Kazakhstan's share of China's imports of
    the chapter (China-reported imports from Kazakhstan / from World).
Both are value shares at HS-2 level; HS-2 mixes products (e.g. HS 28 includes
uranium compounds and other inorganic chemicals), so these are indicators,
not measures of substitutability.
Output: Outputs/generated_tables/two_sided_dependence_2024.csv
"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).parent.parent
RAW = ROOT / "Collected_Raw_Data" / "raw_downloads"
line = [l for l in (RAW / "comtrade_hs2_chn_imports_from_world_2024_selected.txt").read_text().splitlines()
        if l and not l.startswith("#")][0]
cw = {int(k): float(v) for k, v in (x.split(":") for x in line.split("|")[1].split(";"))}
p = pd.read_csv(ROOT / "Collected_Raw_Data" / "hs2_panel_long.csv")
w = p[p["year"] == 2024].pivot_table(index="hs2", columns="flow", values="value_usd")
NAMES = {10: "Cereals", 12: "Oilseeds", 15: "Fats and oils", 23: "Food residues, fodder", 26: "Ores",
         27: "Energy", 28: "Inorganic chemicals incl. uranium compounds", 72: "Iron and steel incl. ferroalloys",
         74: "Copper", 79: "Zinc"}
rows = []
for hs, name in NAMES.items():
    rows.append({"hs2": hs, "chapter": name,
                 "kz_exports_to_china_musd": w.loc[hs, "kz_x_chn"] / 1e6,
                 "china_share_of_kz_exports_pct": 100 * w.loc[hs, "kz_x_chn"] / w.loc[hs, "kz_x_wld"],
                 "china_imports_from_kz_musd": w.loc[hs, "cn_m_kaz"] / 1e6,
                 "china_imports_from_world_musd": cw[hs] / 1e6,
                 "kz_share_of_china_imports_pct": 100 * w.loc[hs, "cn_m_kaz"] / cw[hs]})
out = pd.DataFrame(rows)
out.round(2).to_csv(ROOT / "Outputs" / "generated_tables" / "two_sided_dependence_2024.csv", index=False)
print(out.round(1).to_string())
