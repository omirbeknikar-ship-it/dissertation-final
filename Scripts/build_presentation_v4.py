"""
build_presentation_v4.py
Defence presentation for the final (audited) version of the thesis.
Reuses the visual helpers of build_presentation.py. Output: Paper/defense_presentation.pptx
All numbers are taken from the final manuscript and its output tables.
"""
from pathlib import Path
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

ROOT = Path(__file__).parent.parent
src = (ROOT / "Scripts" / "build_presentation.py").read_text()
helpers = src.split("# SLIDE 1")[0].rsplit("# ════", 1)[0]
ns = {"__file__": str(ROOT / "Scripts" / "build_presentation.py")}
exec(compile(helpers, "helpers", "exec"), ns)
prs, add_rect, add_text, content_slide, bullet_box, stat_box = (
    ns["prs"], ns["add_rect"], ns["add_text"], ns["content_slide"], ns["bullet_box"], ns["stat_box"])
NAVY, BLUE, RED, WHITE, BLACK, LGRAY, MGRAY = (ns[k] for k in ("NAVY", "BLUE", "RED", "WHITE", "BLACK", "LGRAY", "MGRAY"))
BLANK = ns["BLANK"]
FIGS = ROOT / "Outputs" / "generated_figures"
OUT = ROOT / "Paper" / "defense_presentation.pptx"
LIGHT = RGBColor(0xBF, 0xD7, 0xED)


def pic(slide, name, l, t, w=None, h=None):
    kw = {}
    if w: kw["width"] = Inches(w)
    if h: kw["height"] = Inches(h)
    slide.shapes.add_picture(str(FIGS / name), Inches(l), Inches(t), **kw)


def table(slide, rows, l, t, w, h, col_w=None, size=12, header_fill=NAVY):
    shp = slide.shapes.add_table(len(rows), len(rows[0]), Inches(l), Inches(t), Inches(w), Inches(h))
    tb = shp.table
    if col_w:
        for i, cw in enumerate(col_w):
            tb.columns[i].width = Inches(cw)
    for r, row in enumerate(rows):
        for c, val in enumerate(row):
            cell = tb.cell(r, c)
            cell.text = str(val)
            for p in cell.text_frame.paragraphs:
                for run in p.runs:
                    run.font.size = Pt(size)
                    run.font.bold = (r == 0)
                    run.font.color.rgb = WHITE if r == 0 else BLACK
            cell.fill.solid()
            cell.fill.fore_color.rgb = header_fill if r == 0 else (LGRAY if r % 2 else WHITE)
    return tb


def note(slide, text):
    add_text(slide, text, 0.4, 7.05, 12.5, 0.35, size=10, italic=True, color=RGBColor(0x59, 0x59, 0x59))


# 1. Title
s = prs.slides.add_slide(BLANK)
add_rect(s, 0, 0, 13.33, 7.5, fill=NAVY); add_rect(s, 0, 5.6, 13.33, 1.9, fill=BLUE)
add_rect(s, 0, 5.55, 13.33, 0.08, fill=WHITE)
add_text(s, "The Belt and Road Initiative and the Kazakhstan–China Trade Balance", 0.6, 1.0, 12.2, 1.0,
         size=30, bold=True, color=WHITE)
add_text(s, "Sources of the Post-2013 Swing and the Role of Strategic Mineral Exports, 2005–2024", 0.6, 1.95, 12.2, 0.7,
         size=22, color=LIGHT)
add_rect(s, 0.6, 2.8, 4.5, 0.05, fill=WHITE)
add_text(s, "Nikar Omirbek", 0.6, 2.95, 6, 0.5, size=18, color=WHITE)
add_text(s, "Master's thesis  |  Registered topic: BRI's Impact on Kazakhstan–China Trade Balance: "
            "The Role of Strategic Mineral Exports", 0.6, 3.45, 12, 0.5, size=13, color=LIGHT)
add_text(s, "UN Comtrade (both reporters), World Bank WDI, AidData GCDF 3.0", 0.6, 6.0, 12, 0.5,
         size=13, italic=True, color=WHITE)

# 2. Phenomenon
s = content_slide(prs, "What Happened", "Kazakhstan's goods trade with China, China-reported data")
stat_box(s, "+3.5", "Balance 2013, USD bn", 0.6, 1.5, w=3.0, val_color=NAVY)
stat_box(s, "−3.9", "Balance 2019, USD bn", 3.9, 1.5, w=3.0)
stat_box(s, "−12.0", "Balance 2024, USD bn", 7.2, 1.5, w=3.0)
stat_box(s, "15.5", "Swing, USD bn", 10.5, 1.5, w=2.3, val_color=NAVY)
bullet_box(s, ["2013→2019: balance −7.4 bn; energy exports to China −7.6 bn; imports flat",
               "2019→2024: balance −8.2 bn; imports from China +15.2 bn; metals and ores exports +5.6 bn",
               "Oil fell from 62% to 22% of exports to China; metals and ores rose from 36% to 67%",
               "Kazakhstan's own 2020–2022 partner data omit copper, zinc, aluminium and machinery: "
               "China's mirror data are used"], 0.6, 3.2, 12.2, 3.5, size=17)
note(s, "Tables 6.1, 6.2, 4.3. The BRI was announced in Astana on 7 September 2013.")

# 3. Why the balance
s = content_slide(prs, "Why the Trade Balance, and What It Does Not Measure")
bullet_box(s, ["A bilateral deficit is not a loss: imports can be investment, cheaper goods or transit",
               ("47% of the 2019–2024 import rise is machinery, electrical equipment and vehicles", 1),
               ("BRI rail transit earns Kazakhstan service revenue, which goods-trade data do not record", 1),
               "So the balance is treated as an accounting summary, not a welfare measure",
               "Why study it anyway?",
               ("It is the outcome named in the registered topic and in public debate", 1),
               ("It is an identity: explaining it forces an account of every export and import", 1),
               ("It is where the contribution of strategic minerals can be measured", 1)],
           0.6, 1.5, 12.2, 5.4, size=18)

# 4. Puzzle and RQ
s = content_slide(prs, "Puzzle and Research Question")
bullet_box(s, ["The swing coincides with the BRI, but before-and-after comparisons cannot separate the BRI from:",
               ("shocks to all of Kazakhstan's trade (the 2014–2016 commodity collapse)", 1),
               ("shocks to all of China's regional trade (post-2022 re-routing)", 1)], 0.6, 1.4, 12.2, 1.9, size=18)
add_rect(s, 0.6, 3.5, 12.1, 1.7, fill=LGRAY, line=MGRAY)
add_text(s, "Is the post-2013 swing in Kazakhstan's trade balance with China distinctive to the Kazakhstan–China "
            "relationship, and are its distinctive components consistent with the mechanisms through which the BRI "
            "was expected to operate, in particular through strategic mineral exports?",
         0.8, 3.6, 11.7, 1.5, size=19, bold=True, color=NAVY)
bullet_box(s, ["Two comparisons, reported side by side: vs Kazakhstan's other partners; vs China's other regional partners",
               "Claims graded: A context  |  B consistent with a BRI mechanism  |  C causal (not claimed)"],
           0.6, 5.4, 12.2, 1.5, size=16)

# 5. Mechanisms
s = content_slide(prs, "BRI Mechanisms and What Would Count as Evidence")
table(s, [["Mechanism", "Predicts", "Inconsistent if", "Uninformative if"],
          ["M1 Connectivity, market access", "China-specific rise in agri-food and new exports; KZ-specific import rise from 2015",
           "Rise began earlier and did not accelerate; imports rise only after 2022 and regionally", "Change too small to detect"],
          ["M2 Resource finance", "China-specific rise in energy and strategic minerals after Chinese finance",
           "China-specific fall; gains long after finance", "Timing depends on base year"],
          ["N0 Common shocks", "No China-specific change", "Large components in either comparison", ""]],
      0.5, 1.5, 12.3, 3.2, col_w=[2.6, 3.6, 3.6, 2.5], size=13)
bullet_box(s, ["Positive BRI trade effects in the literature: trade costs −1.5 to −2.8% in BRI economies (de Soyres et al. 2019); "
               "trade up to +4.1% (Baniya et al. 2020); ex-post gains for ASEAN (Foo et al. 2020) and for "
               "European exporters via rail (Mau & Seuren 2023)",
               "These measure trade volume or costs on average; this thesis measures one pair's balance and composition. "
               "Effects of a few per cent are undetectable here"], 0.5, 4.9, 12.3, 2.0, size=15)

# 6. Method
s = content_slide(prs, "Three Kinds of Evidence, Kept Separate")
table(s, [["Kind", "What it shows", "Used for"],
          ["Accounting decomposition", "Which flows moved (identity)", "Table 6.2"],
          ["Comparison-adjusted components", "Distinctiveness vs a benchmark; not causal, not an upper bound on BRI",
           "Tables 6.3, 6.3b, 6.4, 6.10b"],
          ["Statistical tests (PPML triple difference, event study, trend break)",
           "Whether China-specific export changes exceed noise, and when they began", "Tables 6.7–6.9, 6.12"]],
      0.5, 1.5, 12.3, 2.6, col_w=[3.8, 5.6, 2.9], size=14)
bullet_box(s, ["Safeguards: four product groups fixed in advance; Holm correction; 300 random chapter sets; "
               "power reported; every comparison over 16 base/end-year combinations",
               "Checks: all tables regenerated from raw files; main model re-estimated independently; "
               "29 manuscript figures reconciled with tables",
               "Disclosure: several analyses were added after seeing earlier results (§3.3)"],
           0.5, 4.4, 12.3, 2.5, size=16)

# 7. Result 1
s = content_slide(prs, "Result 1: Most of the Swing Is China-Specific from Kazakhstan's Side",
                  "Compared with Kazakhstan's trade with its other partners")
pic(s, "fig_r7_common_vs_specific.png", 0.4, 1.35, w=7.3)
stat_box(s, "52–92%", "China-specific share, 16 base/end combinations", 8.1, 1.5, w=4.7)
stat_box(s, "71%", "With averaged endpoints (2011–13 → 2023–24)", 8.1, 3.1, w=4.7, val_color=NAVY)
bullet_box(s, ["Largest part: imports from China after 2019 (+8 to +15 bn)",
               "92% is the maximum (2013 base = oil peak)", "Distinctiveness, not causation"], 8.1, 4.7, 4.8, 2.2, size=15)
note(s, "Tables 6.3, 6.3b. Shift-share: trade with China benchmarked against the same product's trade with the rest of the world.")

# 8. Result 2
s = content_slide(prs, "Result 2: The Import Rise Is Regional from China's Side",
                  "China's exports to Kazakhstan compared with its exports to Russia and Central Asia")
pic(s, "fig_r8_regional_imports.png", 0.4, 1.35, w=7.3)
bullet_box(s, ["vs every neighbour comparator, weighting and base year: at most +0.7 bn Kazakhstan-specific by 2023–24 "
               "(under 3% of imports); usually negative",
               "Holds with and without Russia",
               "vs the world: +5.5 to +8.8 bn",
               "Timing: mostly 2022–2024; in 2013–2019 China's exports to Kazakhstan grew less than to the world",
               "Caveats: neighbours are BRI members; post-2022 re-routing affects comparators"],
           7.9, 1.4, 5.1, 5.5, size=14)
note(s, "Table 6.10b; China-reported data on both sides.")

# 9. Result 3 composition
s = content_slide(prs, "Result 3: Which Exports Changed Towards or Away from China?")
pic(s, "fig_r2_china_share_by_group.png", 0.4, 1.35, w=7.3)
table(s, [["Group (China-specific)", "2013→24, bn", "Grid range"],
          ["Energy", "−4.9", "−4.9 to +2.4"],
          ["Strategic minerals", "+3.4", "+1.8 to +6.7"],
          ["Agri-food", "+0.8", "+0.7 to +0.9"],
          ["Other", "+0.5", "+0.3 to +0.5"]], 7.9, 1.5, 5.1, 2.4, col_w=[2.3, 1.3, 1.5], size=13)
bullet_box(s, ["Oil: China-specific fall concentrated in 2014; opposite to M2",
               "Minerals: positive in every specification; timing depends on base year",
               "PPML: agri-food ×11.7 (robust); metals +39% only with 2023–24"], 7.9, 4.1, 5.1, 2.8, size=14)
note(s, "Tables 6.4, 6.6, 6.7.")

# 10. Result 4 timing
s = content_slide(prs, "Result 4: Did Anything Change When the BRI Began?")
pic(s, "fig_r3_event_study.png", 0.4, 1.35, w=8.0)
bullet_box(s, ["Agri-food: rising from 2008; trend 0.54 → 0.17 log points/yr; no acceleration (one-sided p = 0.99)",
               "Survives Holm (p < 0.001) and beats all 300 random chapter sets",
               "'Slowdown' fails Holm (0.059): not relied on",
               "Metals: no detectable acceleration (p = 0.87); test could miss < 0.16/yr",
               "Energy: one chapter, no inference"], 8.6, 1.4, 4.4, 5.5, size=14)
note(s, "Tables 6.8, 6.9, 6.12.")

# 11. Channels
s = content_slide(prs, "Result 5: What Did the BRI Consist of in Kazakhstan?")
pic(s, "fig_r5_aiddata_by_year.png", 0.4, 1.35, w=7.3)
bullet_box(s, ["Chinese official finance: 48.1 bn in 2000–2013 vs 16.0 bn in 2014–2021 (constant 2021 USD)",
               "Pre-2013: gas pipeline, oil companies, copper mines",
               "Post-2013: roads, border checkpoints; Khorgos dry port (2015)",
               "No agricultural project recorded",
               "Agri-food followed access and logistics, not finance"], 7.9, 1.4, 5.1, 5.5, size=15)
note(s, "Table 6.13; AidData GCDF 3.0, 155 projects recommended for aggregates.")

# 12. Synthesis
s = content_slide(prs, "Synthesis: Each Component Against BRI Mechanisms")
table(s, [["Component", "vs KZ partners", "vs China's neighbours", "Timing", "Verdict"],
          ["Imports from China", "+14.1 bn (+8.1 to +14.7)", "Not distinctive", "2022–2024", "Not distinctive; timing inconsistent with M1"],
          ["Energy exports", "−4.9 bn", "n/a", "2014", "Inconsistent with M2"],
          ["Strategic minerals", "+3.4 bn (+1.8 to +6.7)", "n/a", "Base-dependent", "Offsets part of swing; timing not BRI-specific"],
          ["Agri-food", "+0.8 bn", "n/a", "From 2008; no acceleration", "Consistent in products, not timing"],
          ["Other, extensive margin", "+0.5 bn", "n/a", "", "Absence of evidence"]],
      0.4, 1.5, 12.5, 3.6, col_w=[2.2, 2.4, 2.1, 2.2, 3.6], size=13)
bullet_box(s, ["No large component shows distinctiveness + predicted sign + post-2013 timing"], 0.4, 5.4, 12.5, 1.0, size=17)
note(s, "Table 6.14.")

# 13. Minerals and dependence
s = content_slide(prs, "Strategic Minerals and Two-Sided Dependence")
table(s, [["2024", "China's share of KZ exports", "KZ's share of China's imports"],
          ["Ores (HS 26)", "80.2%", "1.8%"], ["Copper (HS 74)", "64.1%", "3.8%"], ["Zinc (HS 79)", "50.3%", "28.1%"],
          ["Inorganic chem. incl. uranium (HS 28)", "32.4%", "8.9%"]], 0.5, 1.5, 7.2, 2.7, col_w=[3.4, 1.9, 1.9], size=13)
bullet_box(s, ["Minerals offset part of the swing in every specification",
               "Dependence mostly runs from Kazakhstan to China",
               "Uranium reverses it: ~2/3 of China's natural uranium imports came from Kazakhstan (2023; Pan 2024)",
               "Dependence ≠ vulnerability: China's share of KZ refined copper exports fell 65.4% → 49.1% "
               "(Jan–Nov 2024 vs 2025; Astana Times 2026)"], 7.9, 1.4, 5.1, 5.5, size=14)
note(s, "Tables 6.4, 7.1.")

# 14. What it does and does not say
s = content_slide(prs, "What These Results Do and Do Not Say About the BRI")
table(s, [["Type of finding", "Examples"],
          ["Evidence inconsistent with a mechanism", "Oil fell (vs M2); imports rose late and regionally (vs M1); agri-food did not accelerate (vs M1 timing)"],
          ["Absence of evidence", "Extensive margin; other goods; metals trend; effects below ~0.16–0.39 log points/yr"],
          ["Evidence of no effect", "None: transit services unobserved; small average effects undetectable"]],
      0.5, 1.5, 12.3, 2.8, col_w=[3.6, 8.7], size=14)
bullet_box(s, ["Limitations: no causal identification; base-year sensitivity (reported as ranges); comparators affected by "
               "re-routing; HS-2 aggregation; imports as totals; energy one chapter; merchandise only"],
           0.5, 4.6, 12.3, 2.0, size=15)

# 15. Conclusion
s = content_slide(prs, "Conclusion and Policy Implications")
bullet_box(s, ["The swing is China-specific from Kazakhstan's side, regional from China's side",
               "None of its large components has the timing or direction BRI mechanisms predict",
               "Strategic minerals offset part of it; agri-food is the one BRI-consistent channel (products, not timing)",
               "BRI: A (context) supported; B for agri-food in products and channel only; C not claimed",
               "Policy: do not read the deficit as a BRI failure or a loss; monitor by component against two benchmarks; "
               "keep phytosanitary access and border processing efficient; reconcile national trade statistics"],
           0.6, 1.5, 12.2, 5.4, size=18)

# 16. Backup: robustness
s = content_slide(prs, "Backup: Robustness Grid", "China-specific share of the swing, China-reported China legs")
table(s, [["Base \\ End", "2019", "2023", "2024", "2023–24 avg"],
          ["2011–13 avg", "58%", "64%", "77%", "71%"], ["2012", "52%", "57%", "71%", "65%"],
          ["2013", "81%", "82%", "92%", "88%"], ["2014", "71%*", "56%", "83%", "73%"]],
      1.5, 1.6, 10, 2.8, size=15)
bullet_box(s, ["* of a swing of only −0.9 bn", "Kazakhstan-reported China legs, 2013→2024: 92%",
               "Main PPML re-estimated as weighted binomial logit: identical point estimates"], 1.5, 4.7, 10, 2, size=15)
note(s, "Table 6.3b; Script 67.")

prs.save(OUT)
print(f"Saved {OUT} with {len(prs.slides)} slides")
