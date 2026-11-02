"""
build_presentation_v5.py
Defence presentation for the final validated version of the thesis.
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
add_text(s, "UN Comtrade (both reporters), World Bank WDI, AidData GCDF 3.0, dated connectivity milestones", 0.6, 6.0, 12, 0.5,
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
               "Kazakhstan's 2020–2022 partner data omit copper, zinc, aluminium and machinery: China's mirror data are used"],
           0.6, 3.2, 12.2, 3.5, size=17)
note(s, "Tables 6.1, 6.2, 4.3.")

# 3. Balance vs relationship
s = content_slide(prs, "The Trade Balance Is Not the Trade Relationship")
bullet_box(s, ["The BRI is about trade costs, connectivity, investment and trade expansion, not the balance",
               ("Lower trade costs can raise both exports and imports: the balance can move either way", 1),
               ("47% of the 2019–2024 import rise is machinery, electrical equipment and vehicles (can be investment)", 1),
               ("Transit fees from China–Europe rail are services: not in goods trade at all", 1),
               "A deficit is not a loss; the balance is not a welfare measure",
               "Why use it? It is the registered outcome and an identity: every export and import change is a component of it",
               "Turnover (exports + imports) is reported alongside it",
               "Scope: conclusions about merchandise trade only; not transit, investment, productivity or welfare"],
           0.6, 1.5, 12.2, 5.4, size=17)
note(s, "§1.3.")

# 4. Puzzle and RQ
s = content_slide(prs, "Puzzle and Research Question")
bullet_box(s, ["Before-and-after comparisons cannot separate the BRI from:",
               ("shocks to all of Kazakhstan's trade (2014–2016 commodity collapse)", 1),
               ("shocks to all of China's regional trade (post-2022 re-routing)", 1)], 0.6, 1.4, 12.2, 1.6, size=18)
add_rect(s, 0.6, 3.1, 12.1, 1.9, fill=LGRAY, line=MGRAY)
add_text(s, "Is the post-2013 change in Kazakhstan–China merchandise trade, summarised by the swing in the bilateral "
            "balance, distinctive to the Kazakhstan–China relationship, and is it consistent with the BRI mechanisms "
            "that are observable in merchandise trade, in particular through strategic mineral exports?",
         0.8, 3.2, 11.7, 1.7, size=18, bold=True, color=NAVY)
bullet_box(s, ["Two separate comparisons: vs Kazakhstan's other partners; vs China's other regional partners",
               "Timing judged against dated milestones, not only the 2013 announcement",
               "Claims graded: A context  |  B consistent with a mechanism (products, direction, timing)  |  C causal (not claimed)"],
           0.6, 5.2, 12.2, 1.7, size=15)

# 5. Literature and mechanisms
s = content_slide(prs, "What the BRI Literature Finds, and What It Predicts Here")
table(s, [["Study", "Outcome", "Finding"],
          ["de Soyres et al. (2019)", "Shipment times, trade costs (ex-ante)", "Costs −1.5 to −2.8% in BRI economies"],
          ["Baniya, Rocha & Ruta (2020)", "Trade flows, 71 economies (ex-ante)", "Up to +4.1%; more for time-sensitive goods"],
          ["Foo, Lean & Salim (2020)", "ASEAN–China trade (ex-post)", "Positive significant BRI dummy"],
          ["Mau & Seuren (2023)", "European exports to China via rail (ex-post)", "Rail connections raised exports"]],
      0.4, 1.4, 6.6, 2.9, col_w=[2.2, 2.4, 2.0], size=11)
table(s, [["Mechanism", "Observable implication here"],
          ["M1 Trade costs", "China-specific turnover expansion"],
          ["M2 Time-sensitive goods, market access", "Agri-food rise that accelerates at milestones"],
          ["M3 Resource finance", "Energy and minerals rise after finance"],
          ["M4 Investment-linked imports", "KZ-specific capital-goods imports (untested)"],
          ["M5 Transit", "Not in goods trade (untested)"]],
      7.2, 1.4, 5.8, 3.3, col_w=[2.6, 3.2], size=11)
bullet_box(s, ["None of these studies uses a bilateral balance; positive volume effects are compatible with any balance direction",
               "Effects of a few per cent are below what this design can detect"], 0.4, 4.95, 12.6, 1.9, size=15)
note(s, "Tables 2.1, 3.1.")

# 6. Method
s = content_slide(prs, "Three Kinds of Evidence, Kept Separate")
table(s, [["Kind", "What it shows", "Used for"],
          ["Accounting decomposition", "Which flows moved (identity)", "Table 6.2"],
          ["Descriptive comparisons", "Distinctiveness vs a benchmark; not causal, not a bound on BRI effects",
           "Tables 6.3–6.4, 6.10b–c"],
          ["Statistical tests (PPML triple difference, event study, trend breaks)",
           "Whether China-specific export changes exceed noise, and when they began", "Tables 6.7–6.9b, 6.12"]],
      0.5, 1.5, 12.3, 2.6, col_w=[3.8, 5.6, 2.9], size=14)
bullet_box(s, ["Safeguards: four product groups fixed in advance; Holm; 300 random chapter sets; power; 16 base/end-year "
               "combinations; break years 2012, 2013, 2015, 2017; six comparator sets",
               "Checks: tables regenerated from raw files; main model re-estimated independently; 34 manuscript figures reconciled",
               "Exploratory: several analyses added after earlier results were seen (§3.3)"],
           0.5, 4.4, 12.3, 2.5, size=16)

# 7. Result 1
s = content_slide(prs, "Result 1: Mostly China-Specific from Kazakhstan's Side",
                  "Compared with Kazakhstan's trade with its other partners, product by product")
pic(s, "fig_r7_common_vs_specific.png", 0.4, 1.35, w=7.3)
stat_box(s, "52–92%", "China-specific share of the swing, 16 combinations", 8.1, 1.5, w=4.7)
stat_box(s, "71%", "With averaged endpoints (2011–13 → 2023–24)", 8.1, 3.1, w=4.7, val_color=NAVY)
bullet_box(s, ["Largest part: imports after 2019 (+8 to +15 bn)",
               "Turnover: no China-specific expansion to 2019 (−0.9 to +2.0 bn)",
               "Distinctiveness, not causation"], 8.1, 4.7, 4.8, 2.2, size=15)
note(s, "Tables 6.3, 6.3b; §6.2.")

# 8. Result 2
s = content_slide(prs, "Result 2: The Post-2019 Import Rise Was Not Specific to Kazakhstan",
                  "China's exports to Kazakhstan vs to its five neighbours (growth factors normalise for size)")
pic(s, "fig_r8_regional_imports.png", 0.4, 1.35, w=7.6)
bullet_box(s, ["2019–2024: ×2.20 to Kazakhstan, ×2.21–3.17 to each neighbour: lowest of six",
               "2013–2024: comparator-dependent (faster than Tajikistan, Turkmenistan)",
               "Cannot separate post-2022 re-routing, Chinese supply, or region-wide/lagged BRI connectivity",
               "So: no Kazakhstan-specific mechanism needed; cause not identified"],
           8.2, 1.4, 4.8, 5.5, size=14)
note(s, "Tables 6.10b, 6.10c.")

# 9. Result 3
s = content_slide(prs, "Result 3: Which Exports Changed Towards or Away from China?")
pic(s, "fig_r2_china_share_by_group.png", 0.4, 1.35, w=7.3)
table(s, [["Group (China-specific)", "2013→24, bn", "Grid range"],
          ["Energy", "−4.9", "−4.9 to +2.4"],
          ["Strategic minerals", "+3.4", "+1.8 to +6.7"],
          ["Agri-food", "+0.8", "+0.7 to +0.9"],
          ["Other", "+0.5", "+0.3 to +0.5"]], 7.9, 1.5, 5.1, 2.4, col_w=[2.3, 1.3, 1.5], size=13)
bullet_box(s, ["Oil: fall concentrated 2013→2014; opposite to M3",
               "Minerals: positive in every specification; timing not tied to finance",
               "PPML: agri-food ×11.7 (robust); metals +39% only with 2023–24"], 7.9, 4.1, 5.1, 2.8, size=14)
note(s, "Tables 6.4, 6.6, 6.7.")

# 10. Result 4 timing
s = content_slide(prs, "Result 4: Did Anything Accelerate at a BRI Milestone?")
pic(s, "fig_r3_event_study.png", 0.4, 1.35, w=7.0)
table(s, [["Break", "Agri-food δ", "p (accel.)"],
          ["2012 rail crossing", "−0.40", "0.96"], ["2013 announcement", "−0.37", "0.99"],
          ["2015 dry port", "−0.26", "0.99"], ["2017 stake, loans", "−0.17", "0.97"]],
      7.6, 1.4, 5.4, 2.4, col_w=[2.4, 1.5, 1.5], size=12)
bullet_box(s, ["Agri-food rise robust (Holm p < 0.001; beats 300 random sets) but began before 2013",
               "No acceleration at any milestone: evidence against that prediction, not against the BRI",
               "Metals, other goods: imprecise (absence of evidence)"], 7.6, 4.0, 5.4, 2.9, size=14)
note(s, "Tables 6.8, 6.9, 6.9b (exploratory), 6.12.")

# 11. Channels and milestones
s = content_slide(prs, "Result 5: What the BRI Consisted of, and When")
pic(s, "fig_r5_aiddata_by_year.png", 0.4, 1.35, w=6.6)
table(s, [["Date", "Milestone", "Stage"],
          ["Dec 2012", "Altynkol–Khorgos rail crossing", "Operational"],
          ["Sep 2013", "BRI announced, Astana", "Announcement"],
          ["2015", "Khorgos Gateway dry port", "Operational"],
          ["2016", "WE–WC road, KZ section", "Planned only"],
          ["2017–18", "Khorgos stake; 5 road loans", "Financing"],
          ["2019", "Border checkpoint loan", "Commitment"],
          ["Sep 2025", "Dostyk–Moyynty 2nd track", "After sample"]],
      7.2, 1.4, 5.8, 3.6, col_w=[1.1, 3.0, 1.7], size=11)
bullet_box(s, ["Finance: 48.1 bn 2000–2013 vs 16.0 bn 2014–2021; none for agriculture",
               "Completion dates mostly unverified: lagged effects cannot be excluded"], 0.4, 5.2, 12.6, 1.7, size=15)
note(s, "Tables 6.13, 6.13b.")

# 12. Synthesis: mechanism scorecard
s = content_slide(prs, "Mechanism Scorecard")
table(s, [["Mechanism", "Established here", "Untested", "Verdict"],
          ["M1 Trade costs", "No China-specific turnover rise to 2019; post-2019 rise regional", "Costs, region-wide and lagged effects",
           "Inconsistent (KZ-specific, 2013–19); inconclusive (regional, lagged)"],
          ["M2 Market access", "Robust agri-food rise; no acceleration at milestones", "HS-6, protocol dates",
           "Consistent in products; inconsistent with predicted acceleration"],
          ["M3 Resource finance", "Oil fell to China; minerals rose; finance pre-2013", "Project completion",
           "Inconsistent (energy); inconclusive (minerals)"],
          ["M4 Investment imports", "47% of import rise is capital/durable goods", "Link to projects", "Untested"],
          ["M5 Transit", "", "All", "Untested"]],
      0.4, 1.5, 12.5, 4.3, col_w=[2.0, 4.2, 2.6, 3.7], size=12)
bullet_box(s, ["No change both matches a mechanism and starts or accelerates at a milestone"], 0.4, 6.0, 12.5, 0.9, size=17)
note(s, "§6.9.")

# 13. Minerals and dependence
s = content_slide(prs, "Strategic Minerals and Two-Sided Dependence")
table(s, [["2024", "China's share of KZ exports", "KZ's share of China's imports"],
          ["Ores (HS 26)", "80.2%", "1.8%"], ["Copper (HS 74)", "64.1%", "3.8%"], ["Zinc (HS 79)", "50.3%", "28.1%"],
          ["Inorganic chem. incl. uranium (HS 28)", "32.4%", "8.9%"]], 0.5, 1.5, 7.2, 2.7, col_w=[3.4, 1.9, 1.9], size=13)
bullet_box(s, ["Minerals offset part of the swing in every specification",
               "Dependence mostly runs from Kazakhstan to China",
               "Uranium reverses it: ~2/3 of China's natural uranium imports from Kazakhstan (2023; Pan 2024)",
               "Dependence ≠ vulnerability: China's share of KZ refined copper exports 65.4% → 49.1% "
               "(Jan–Nov 2024 vs 2025; Astana Times 2026)"], 7.9, 1.4, 5.1, 5.5, size=14)
note(s, "Tables 6.4, 7.1.")

# 14. Established / interpretation / untested
s = content_slide(prs, "What Is Established, What Is Interpretation, What Is Untested")
table(s, [["Category", "Claims"],
          ["Established (robust descriptive or statistical)",
           "Size and components of the swing; 52–92% China-specific; no China-specific turnover rise to 2019; post-2019 import "
           "rise shared by all five neighbours; oil fell more to China; minerals offset part; agri-food reoriented, no acceleration "
           "at milestones; finance peaked pre-2013; KZ 2020–22 data gaps"],
          ["Interpretation", "Evidence does not match M1–M3 predictions in the windows tested; import rise better seen as regional; "
           "agri-food followed access and logistics, not finance"],
          ["Untested", "Any causal effect; M4, M5; region-wide and lagged effects; investment, productivity, welfare; HS-6 timing"]],
      0.5, 1.5, 12.3, 4.6, col_w=[3.3, 9.0], size=13)
note(s, "§6.9, §7.2.")

# 15. Conclusion
s = content_slide(prs, "Conclusion and Policy Implications")
bullet_box(s, ["The change in Kazakhstan–China goods trade is mostly China-specific from Kazakhstan's side",
               "Its largest part, the post-2019 import rise, was shared by China's other neighbours",
               "No change both matches a BRI mechanism and starts or accelerates at a BRI milestone",
               "This is not evidence that the BRI had no effect (transit, investment, regional and lagged effects unmeasured)",
               "Policy: don't read the deficit as a loss; monitor by component against both benchmarks; keep phytosanitary "
               "access and border processing efficient; reconcile national statistics with China's"],
           0.6, 1.5, 12.2, 5.4, size=18)

# 16. Backup
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
