"""
68_reconcile_manuscript.py
Reconciles key figures quoted in Paper/final_dissertation.md with the output
tables. Each check recomputes a value from a table, formats it as it is
written in the manuscript, and confirms that the string occurs in the text.
Run after Scripts 60-67. Output: Outputs/generated_tables/reconciliation_report.csv
"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).parent.parent
T = ROOT / "Outputs" / "generated_tables"
MS = (ROOT / "Paper" / "final_dissertation.md").read_text()
rd = lambda f: pd.read_csv(T / f)
checks = []


def chk(label, value, fmt, source):
    # tables are stored rounded to 3 decimals, so allow for half a unit of that rounding
    cands = [fmt.format(v) for v in (value, value + 0.0005, value - 0.0005)]
    hit = [c for c in cands if c in MS]
    checks.append({"figure": label, "value": value, "expected_text": hit[0] if hit else cands[0],
                   "source": source, "found": bool(hit)})


dec = rd("trade_balance_decomposition.csv").set_index(["from", "to"])
chk("Balance 2013", dec.loc[(2013, 2024), "balance_from_bn"], "+{:.2f}", "trade_balance_decomposition")
chk("Balance 2024", dec.loc[(2013, 2024), "balance_to_bn"], "{:.2f}".replace("{", "−{").replace("−{:.2f}", "−{:.2f}"),
    "trade_balance_decomposition")
checks[-1]["expected_text"] = "−{:.2f}".format(abs(dec.loc[(2013, 2024), "balance_to_bn"]))
checks[-1]["found"] = checks[-1]["expected_text"] in MS
chk("Swing 2013-2024", abs(dec.loc[(2013, 2024), "d_balance_bn"]), "−{:.2f}", "trade_balance_decomposition")
chk("Energy export change 2013-19", abs(dec.loc[(2013, 2019), "d_exports_energy_bn"]), "−{:.2f}", "trade_balance_decomposition")
chk("Import change 2019-24", dec.loc[(2019, 2024), "d_imports_total_bn"], "+{:.2f}", "trade_balance_decomposition")

bc = rd("balance_common_vs_china_specific.csv")
m = bc[bc["source"].str.startswith("China")].set_index("period")
k = bc[bc["source"].str.startswith("Kaz")].set_index("period")
chk("China-specific balance 2013-24", abs(m.loc["2013-2024", "balance_china_specific_bn"]), "−{:.2f}", "balance_common_vs_china_specific")
chk("Common balance 2013-24", abs(m.loc["2013-2024", "balance_common_bn"]), "−{:.2f}", "balance_common_vs_china_specific")
chk("China-specific imports 2013-24", m.loc["2013-2024", "imports_china_specific_bn"], "+{:.2f}", "balance_common_vs_china_specific")
chk("China-specific share 2013-24", 100 * m.loc["2013-2024", "balance_china_specific_bn"] / m.loc["2013-2024", "balance_change_bn"],
    "{:.0f} per cent", "balance_common_vs_china_specific")
chk("KZ-reported swing", abs(k.loc["2013-2024", "balance_change_bn"]), "−{:.2f}", "balance_common_vs_china_specific")
chk("KZ-reported China-specific", abs(k.loc["2013-2024", "balance_china_specific_bn"]), "−{:.2f}", "balance_common_vs_china_specific")

g = rd("robust_kz_partner_grid.csv")
shares = g.loc[~((g["base"] == "2014") & (g["end"] == "2019")), "china_specific_share_pct"]
chk("Grid share min", shares.min(), "{:.0f}", "robust_kz_partner_grid")
chk("Grid share max", shares.max(), "{:.0f}", "robust_kz_partner_grid")
avg = g[(g["base"] == "2011-13 avg") & (g["end"] == "2023-24 avg")].iloc[0]
chk("Averaged-endpoint share", avg["china_specific_share_pct"], "{:.0f}% (", "robust_kz_partner_grid")

nb = rd("robust_china_neighbour_grid.csv")
late = nb[nb["end"].isin(["2023", "2024", "2023-24 avg"]) & (nb["comparator"] != "World")]
chk("Max KZ-specific imports vs neighbours, end 2023-24", late["imports_kz_specific_bn"].max(), "+{:.2f}", "robust_china_neighbour_grid")
w = nb[(nb["comparator"] == "World") & (nb["base"] == "2013") & (nb["end"] == "2024")].iloc[0]
chk("KZ-specific imports vs world 2013-24", w["imports_kz_specific_bn"], "+{:.2f}", "robust_china_neighbour_grid")

pp = rd("ppml_main.csv").iloc[0]
for gname in ["metals_ores", "agrifood", "other"]:
    chk(f"PPML {gname}", pp[f"{gname}_b"], "{:.3f}", "ppml_main")
chk("PPML energy", abs(pp["energy_b"]), "−{:.3f}", "ppml_main")
tb = rd("ppml_trend_break.csv").set_index("group")
chk("Trend change agri", abs(tb.loc["agrifood", "slope_change"]), "−{:.3f}", "ppml_trend_break")
mt = rd("multiple_testing.csv")
h = mt[(mt["group"] == "agrifood") & mt["family"].str.startswith("Trend")].iloc[0]
chk("Holm agri trend", h["p_holm"], "{:.3f}", "multiple_testing")
chk("CI upper agri trend", abs(h["ci95_upper"]), "−{:.3f}", "multiple_testing")
pm = rd("permutation_agrifood.csv")
chk("Permutation median draw", pm.iloc[0]["draw_median"], "{:.2f}", "permutation_agrifood")
chk("Permutation 95th pct", pm.iloc[0]["draw_p95"], "{:.2f}", "permutation_agrifood")
sm = rd("strategic_minerals_components.csv").set_index("period")
chk("Strategic minerals China-specific 2013-24", sm.loc["2013-2024", "china_specific_bn"], "+{:.2f}", "strategic_minerals_components")
ag = rd("aiddata_by_sector_period.csv").set_index("Sector Name")
chk("AidData total", ag.loc["ALL SECTORS", "total"], "{:.2f}", "aiddata_by_sector_period")
td = rd("two_sided_dependence_2024.csv").set_index("hs2")
chk("Ores China share", td.loc[26, "china_share_of_kz_exports_pct"], "{:.1f}", "two_sided_dependence_2024")
chk("Ores KZ share of China", td.loc[26, "kz_share_of_china_imports_pct"], "{:.1f}", "two_sided_dependence_2024")

out = pd.DataFrame(checks)
out.to_csv(T / "reconciliation_report.csv", index=False)
print(out[["figure", "expected_text", "found"]].to_string())
print(f"{out['found'].sum()} of {len(out)} figures found in the manuscript")
