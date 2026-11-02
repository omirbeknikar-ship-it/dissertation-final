"""
60_build_hs2_panel.py
Parse the HS-2 raw transcriptions of UN Comtrade (public preview API) into a
tidy product x flow x year panel and validate totals.

Inputs (Collected_Raw_Data/raw_downloads/):
  comtrade_hs2_kaz_exports_to_china.txt      KZ-reported exports to China (FOB)
  comtrade_hs2_kaz_exports_to_world.txt      KZ-reported exports to World (FOB)
  comtrade_hs2_kaz_exports_to_world_gapfill.txt  chapters re-queried after truncation
  comtrade_hs2_chn_imports_from_kaz.txt      China-reported imports from KZ (CIF, mirror)
  comtrade_hs2_chn_exports_to_kaz.txt        China-reported exports to KZ (FOB), snapshot years
  wdi_kaz_merch_exports.csv                  WDI merchandise exports (validation only)

Lines are "YEAR|HS2:value;HS2:value;..." in current USD. Several lines for the
same year are merged (gap-fill lines add chapters missing from the first line;
a chapter that appears twice keeps its first value and is reported).

Product groups (HS 2017 chapter numbers):
  energy     27
  metals_ores 25, 26, 28, 71, 72, 74, 75, 76, 78, 79, 80, 81
  agrifood   01-24
  other      everything else (chemicals 29-40, light industry 41-67,
             building materials 68-70, metal articles 73, 82-83,
             machinery and transport 84-89, other 90-99)

Outputs: Collected_Raw_Data/hs2_panel_long.csv (year, hs2, group, flow, value_usd)
         Outputs/generated_tables/hs2_validation.csv
"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).parent.parent
RAW = ROOT / "Collected_Raw_Data" / "raw_downloads"
TABLES = ROOT / "Outputs" / "generated_tables"
TABLES.mkdir(parents=True, exist_ok=True)

METALS_ORES = {25, 26, 28, 71, 72, 74, 75, 76, 78, 79, 80, 81}


def group_of(hs2: int) -> str:
    if hs2 == 27:
        return "energy"
    if hs2 in METALS_ORES:
        return "metals_ores"
    if 1 <= hs2 <= 24:
        return "agrifood"
    return "other"


def read_lines(path: Path) -> dict:
    out, dup = {}, []
    for line in path.read_text().splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        y, body = line.split("|", 1)
        y = int(y)
        d = out.setdefault(y, {})
        for item in body.split(";"):
            k, v = item.split(":")
            k = int(k)
            if k in d:
                dup.append((path.name, y, k))
                continue
            d[k] = float(v)
    if dup:
        print("Duplicate chapter entries ignored:", dup)
    return out


sources = {
    "kz_x_chn": [RAW / "comtrade_hs2_kaz_exports_to_china.txt"],
    "kz_x_wld": [RAW / "comtrade_hs2_kaz_exports_to_world.txt",
                 RAW / "comtrade_hs2_kaz_exports_to_world_gapfill.txt"],
    "cn_m_kaz": [RAW / "comtrade_hs2_chn_imports_from_kaz.txt"],
    "cn_x_kaz": [RAW / "comtrade_hs2_chn_exports_to_kaz.txt"],
}
rows = []
for flow, files in sources.items():
    merged = {}
    for f in files:
        for y, d in read_lines(f).items():
            m = merged.setdefault(y, {})
            for k, v in d.items():
                m.setdefault(k, v)
    for y, d in merged.items():
        for k, v in d.items():
            rows.append({"year": y, "hs2": k, "group": group_of(k), "flow": flow, "value_usd": v})
panel = pd.DataFrame(rows).sort_values(["flow", "year", "hs2"])
panel.to_csv(ROOT / "Collected_Raw_Data" / "hs2_panel_long.csv", index=False)

# Validation: sum of chapters against WDI merchandise exports (World) and coverage
wdi = pd.read_csv(RAW / "wdi_kaz_merch_exports.csv", comment="#").set_index("year")["merch_exports_usd"]
tot = panel.groupby(["flow", "year"])["value_usd"].agg(["sum", "count"]).reset_index()
tot = tot.pivot(index="year", columns="flow")
val = pd.DataFrame(index=sorted(panel["year"].unique()))
for f in sources:
    val[f"{f}_bn"] = tot[("sum", f)] / 1e9 if ("sum", f) in tot else None
    val[f"{f}_n_chapters"] = tot[("count", f)] if ("count", f) in tot else None
val["wdi_merch_exports_bn"] = wdi.reindex(val.index) / 1e9
val["kz_x_wld_pct_of_wdi"] = 100 * val["kz_x_wld_bn"] / val["wdi_merch_exports_bn"]
val["mirror_ratio_cn_m_over_kz_x"] = val["cn_m_kaz_bn"] / val["kz_x_chn_bn"]
val.index.name = "year"
val.round(3).to_csv(TABLES / "hs2_validation.csv")
print(val.round(2).to_string())
