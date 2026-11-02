"""
69_timing_alternatives.py
Final validation (§6.5): the trend-break test in Script 62 places the break at
2013, the BRI announcement. Announcement is not implementation. This script
re-estimates the same PPML trend-break model with the break placed at dated
connectivity milestones:
  2012  Altynkol-Khorgos rail border crossing opened (December 2012)
  2015  Khorgos Gateway dry port began operating
  2017  Chinese state companies took a 49% stake in Khorgos Gateway; China
        Eximbank road loans committed (AidData)
Model: value ~ China x group x (t - k) + China x group x (t - k) x 1[t > k]
       | chapter-year + chapter-destination FE; SE clustered by chapter.
This is EXPLORATORY: break years were chosen after the 2013 results were seen.
Output: Outputs/generated_tables/trend_break_alternative_years.csv
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
src = (ROOT / "Scripts" / "62_ppml_triple_difference.py").read_text().split("res = []")[0]
ns = {"__file__": str(ROOT / "Scripts" / "62_ppml_triple_difference.py")}
exec(compile(src, "62_builder", "exec"), ns)
base = ns["build"]()
GROUPS = ["energy", "metals_ores", "agrifood", "other"]
rows = []
for k in (2012, 2013, 2015, 2017):
    d = base.copy()
    d["tc"] = d["year"] - k
    d["after"] = (d["year"] > k).astype(int)
    terms = []
    for g in GROUPS:
        d[f"tr_{g}"] = d["china"] * (d["group"] == g) * d["tc"]
        d[f"trpost_{g}"] = d[f"tr_{g}"] * d["after"]
        terms += [f"tr_{g}", f"trpost_{g}"]
    m = pf.fepois("value_m ~ " + " + ".join(terms) + " | pt + pd", data=d, vcov={"CRV1": "hs2"})
    t = m.tidy()
    for g in ["metals_ores", "agrifood", "other"]:
        a, b = f"tr_{g}", f"trpost_{g}"
        dlt, se = t.loc[b, "Estimate"], t.loc[b, "Std. Error"]
        rows.append({"break_year": k, "group": g, "pre_trend": t.loc[a, "Estimate"], "trend_change": dlt,
                     "se": se, "p_two_sided": t.loc[b, "Pr(>|t|)"],
                     "p_one_sided_acceleration": 1 - stats.norm.cdf(dlt / se),
                     "ci_low": dlt - 1.96 * se, "ci_high": dlt + 1.96 * se,
                     "mde_80pct_one_sided": (stats.norm.ppf(0.95) + stats.norm.ppf(0.80)) * se})
out = pd.DataFrame(rows)
out.round(4).to_csv(T / "trend_break_alternative_years.csv", index=False)
print(out.round(3).to_string())
