# Change Log: Thesis Reconstruction (October 2026)

Branch: `thesis-reconstruction`. Previous manuscript archived as `Paper/archive/v2_minerals_trade_balance_dissertation.md` (and `.pdf`).

## What changed and why

| Area | Before (v2) | After (reconstruction) | Reason |
|---|---|---|---|
| Title | "BRI's Impact on Kazakhstan–China Trade Balance: The Role of Strategic Mineral Exports" | "The Belt and Road Initiative and Kazakhstan–China Trade: Export Composition, Strategic Minerals and the Bilateral Balance, 2005–2024"; registered title shown as subtitle | Keeps BRI, KZ–China trade, the balance and minerals; "impact" removed because no causal effect is identified. **Check with the department whether a title change needs approval; if not allowed, keep the registered title and use the new one as subtitle.** |
| Research question | How did the post-BRI period change the mineral–balance relationship? | Was the post-2013 change in export composition China-specific and BRI-timed, and what does it imply for the balance? | Old question could not separate BRI from the oil price collapse |
| BRI role | Post-2013 dummy | Explicit levels A/B/C; design reaches B, never claims C | Required by the brief |
| Theory | Asymmetric interdependence as primary framework with coefficient-sign predictions | Gravity plus extensive-margin theory generate testable expectations (E0, E1, E2); asymmetric interdependence moved to the discussion as interpretation | The regressions could not test bargaining power; the old framework assumed concentration implies leverage |
| Unit of analysis | One country pair, annual (n = 24) and monthly (n = 120) | HS-2 chapter × destination (China, RoW) × year, 3,160 observations | Allows product-year fixed effects that remove world prices |
| Period | 2000–2023 | 2005–2024 (2020–2022 excluded from KZ-reported product comparisons) | HS-2 data retrieved for 2005–2024; suppression in 2020–2022 |
| Method | OLS/HAC, ADL, Granger, DiD with 6 partners, interpolation | Balance decomposition; PPML triple difference; event study; trend-break test; extensive-margin LPM; robustness | Identification and inference problems in v2 (Appendix B) |
| Balance measure | Kazakhstan-reported | China-reported both directions | KZ import gap (×1.5–2.5) and 2020–2022 suppression |
| Main conclusion | Negative post-BRI minerals × post interaction; "consistent with asymmetric interdependence" | Balance fell because of oil (2013–19) and imports (2019–24); minerals rose; agri-food is the only robust China-specific shift and it pre-dates the BRI | Evidence |
| Chapters | 8 chapters, about 23,400 words, 61 pages | 8 chapters, about 11,700 words, 34 pages | Old chapters 5–6 (most of the length) replaced |

## New files

- Data: `Collected_Raw_Data/raw_downloads/comtrade_hs2_*.txt` (6 files), `wdi_kaz_merch_exports.csv`, `Collected_Raw_Data/hs2_panel_long.csv`
- Scripts: `60_build_hs2_panel.py`, `61_composition_diversification.py`, `62_ppml_triple_difference.py`, `63_figures_reconstruction.py`, `64_two_sided_dependence.py`
- Tables (Outputs/generated_tables): `hs2_validation`, `composition_kz_exports_to_china`, `china_share_by_group`, `diversification_indices`, `mirror_suppression`, `trade_balance_decomposition`, `import_composition_china_reported`, `aiddata_by_sector_period`, `aiddata_by_year`, `russia_manufactures_check`, `agrifood_chapters`, `ppml_main`, `ppml_event_study`, `ppml_pretrend_test`, `ppml_trend_break`, `ppml_chapters_per_group`, `extensive_margin_lpm`, `two_sided_dependence_2024`
- Figures: `fig_r1`–`fig_r6`
- Documents: this file, `research_logic_map.md`, `evidence_audit.md`, `examiner_evaluation.md`, `plain_english_explanation.md`

## Bibliography

Added 16 entries (Melitz 2003; Chaney 2008; Hummels and Klenow 2005; Imbs and Wacziarg 2003; Cadot, Carrère and Strauss-Kahn 2011; Santos Silva and Tenreyro 2006; AidData 2023; Custer et al. 2023; WDI; UN Comtrade HS-2; China Daily 2013; KTZ Express; Astana Times 2023 and 2026; Pan 2024; WNA 2026). Each was checked against a publisher, RePEc or source page (see `evidence_audit.md`). No existing entry was removed; entries no longer cited (e.g. Granger, ARDL and interpolation references) stay in the .bib file but do not appear in the reference list because pandoc lists only cited works.

## Not changed

- Scripts 10–45 and their outputs still run and are documented in Appendix B.
- Defence slides (`defense_presentation.pptx`) and `defense_script.md` still describe v2 and **must be rebuilt** before the pre-defence.
- `reply_to_supervisor.md` describes v2.

---

# Second Round (31 October 2026): Unifying the Argument

## Why a second round was needed

A review of the first reconstruction found that it presented several findings (oil, imports, agri-food, Chinese finance, minerals, statistics) without one question that connected them. Its research question had two loosely joined halves (export composition; implications for the balance), the import surge was described but not tested, and the agri-food result risked being read as the main contribution simply because it was the most significant result. The first round's disclosure (§3.3) also overstated how much was pre-specified: it said all product-level tests were run after the expectations were fixed, but descriptive shares by group had been inspected before the group predictions were written. This has been corrected.

## What changed

| Area | First reconstruction | Second round |
|---|---|---|
| Central question | Was export composition change China-specific and BRI-timed; what does it imply for the balance? | How much of the BRI-era balance deterioration was bilateral, and does the bilateral part match BRI mechanisms, in particular via strategic minerals? |
| Organising idea | Separate tests by product group | Upper bound (China-specific component) + mechanism test for each part of it |
| New analysis | none | Shift-share decomposition of exports, imports and balance into common and China-specific parts (Script 65); strategic-minerals component; China's exports to Kyrgyzstan, Uzbekistan, Russia and World as an import-side comparison; Holm corrections, one-sided acceleration tests and randomisation inference (Script 66) |
| New data | none | Kazakhstan's total imports from World and China (2013, 2019, 2024); China's total exports to KZ, KG, UZ, RU, World (2013, 2019, 2024); WDI merchandise imports |
| Main finding | Balance fell because of oil, then imports; agri-food China-specific | 92% of the deterioration is bilateral; its two largest parts (post-2022 regional import surge; China-specific oil fall) do not fit BRI mechanisms; minerals and agri-food improved the balance |
| Role of agri-food | Presented as the clearest China-specific change | Supporting result: the only component consistent with a BRI mechanism in products and channel, small (+0.8 bn), not BRI-timed |
| Strategic minerals | Rose; did not cause deterioration | China-specific stabiliser (+3.4 bn), post-2019 |
| Timing claim | "Agri-food trend slowed after 2013 (p = 0.02)" | "No acceleration" (one-sided p = 0.99; CI below zero). The slowdown fails Holm correction (adjusted p = 0.059) and is not relied on |
| Earlier statement corrected | §7.1 said post-2013 export change was "mostly the commodity cycle" | Decomposition shows about half of the 2013–2019 export fall was China-specific; statement removed |
| Disclosure | §3.3 overstated pre-specification | §3.4 states which elements were exploratory; §5.7 lists safeguards |
| Title | "...Export Composition, Strategic Minerals and the Bilateral Balance" | "The Belt and Road Initiative and the Kazakhstan–China Trade Balance: Bilateral Change, BRI Mechanisms and the Role of Strategic Mineral Exports, 2005–2024" (closer to the registered topic) |
| Length | about 11,700 words, 34 pages | about 13,200 words, 36 pages |

New files: `Scripts/65_common_vs_china_specific.py`, `Scripts/66_multiple_testing_permutation.py`, `Collected_Raw_Data/raw_downloads/comtrade_totals_imports_and_china_exports.txt`, `wdi_kaz_merch_imports.csv`, `comtrade_hs2_chn_imports_from_world_2024_selected.txt`, tables `balance_common_vs_china_specific.csv`, `export_components_by_group.csv`, `strategic_minerals_components.csv`, `china_exports_regional_comparison.csv`, `multiple_testing.csv`, `permutation_agrifood.csv`, figures `fig_r7`, `fig_r8`.


---

# Third Round (1 November 2026): Resolving the "Bilateral" Ambiguity

**Problem found.** The second round claimed the deterioration was "bilateral" (92 per cent China-specific) and, a few pages later, that its largest part was a regional shock shared with China's other neighbours. Both statements were true, but against different benchmarks, and the manuscript did not say so. The central claim was therefore internally inconsistent.

**Fix.** A second, explicit benchmark for imports (Script 65, `import_benchmarks.csv`, new Table 6.10b): imports from China are compared with China's exports to the world, to Russia, to Kyrgyzstan and Uzbekistan, and to all three neighbours. Under every neighbour benchmark, the Kazakhstan-specific part of the import rise is close to zero or negative (2013–2024: −1.2 bn vs Russia, −4.2 bn vs all three). The answer is now stated as a funnel: 15.5 bn total → 14.3 bn China-specific relative to Kazakhstan's other partners → about zero net specific to the Kazakhstan–China pair (export side −0.2 bn). The manuscript states that the neighbour benchmark also removes any region-wide BRI effect, so the import conclusion rests on timing (post-2022), not on the benchmark alone.

**Edits.** Abstract, §1.4, §1.6 (contribution, provisions 1–2), §5.5, §6.2, §6.6 (new Table 6.10b), §6.9, §7.1 (funnel), §7.2, §8.1, §8.2 (new limitation on benchmarks and base year), Appendix A. Display equation in §5.1 simplified so it converts in the Word file. About 14,000 words.

---

# Fourth Round (1 November 2026): Final Adversarial Audit

| Area | Before | After | Reason |
|---|---|---|---|
| Research question | "How much of the BRI-era deterioration ... was specific to the bilateral relationship" | "Is the post-2013 swing ... distinctive to the Kazakhstan–China relationship, and are its distinctive components consistent with BRI mechanisms" | "Deterioration" presumed a deficit is bad; the question now treats the balance as an accounting summary (§1.3) |
| "Upper bound" | The China-specific component was called an upper bound on any BRI effect | Removed; called a comparison-adjusted measure of distinctiveness | Not mathematically justified: the BRI can move the benchmark, and BRI effects can be offset within the component |
| Funnel and "approximately zero" | 15.5 → 14.3 → ≈0, applied sequentially | Two comparisons reported side by side; "≈0" removed | The comparisons use different reporters and benchmarks; the export-side "−0.2 bn" was specific to a 2013 base (+2.0 to +3.7 bn from other bases) |
| 92 per cent | Headline | Reported as the maximum of a 16-cell grid; range 52–92 per cent; 71 per cent with averaged endpoints | 2013 was the peak year of oil exports to China |
| Import neighbour comparison | One base, value-weighted, four comparators | China-reported on both sides; Central Asia (4 states) with and without Russia; value-weighted and median; 16 base/end combinations | Robustness; result unchanged (≤ +0.7 bn by 2023–24) |
| Export neighbour comparison | Not done | Computed (Script 67) but not used in conclusions | Comparators' exports to China are oil and gas |
| Oil | "China-specific fall began with the 2014 price collapse" | "Concentrated in 2013→2014; negative from every pre-2014 base; small and sign-unstable from a 2014 base" | Grid |
| Strategic minerals | "Almost entirely after 2019" | "Positive in every specification; timing base-dependent (0.2–2.4 bn by 2019)" | Grid |
| Agri-food timing | "began 2010–2012" | "rising from 2008" (event study) | Consistency with Table 6.8 |
| Trend tests | "Absence of acceleration in every group" | No group shows significant acceleration; positive imprecise δ for other goods is absence of evidence; power reported (MDE 0.39 and 0.16) | Wording exceeded the test |
| Literature | BRI trade-cost studies only | New §2.3 on positive-effect studies (de Soyres et al.; Baniya et al.; Bird et al.; Foo et al. 2020; Mau & Seuren 2023) and how they relate | Required engagement; transit services point |
| Mechanisms | Prediction table | Table 3.1: support / inconsistent / uninformative observation for each mechanism | Distinguish absence of evidence from contradiction |
| Data | Discrepancies described in text | Table 4.4: every discrepancy, likely cause, treatment, limitation; corrected CIF/FOB reasoning for the import gap (valuation widens, not explains, the gap) | Data audit |
| Verification | Scripts run once | All tables regenerated from raw files (identical to 0.001); main PPML re-estimated as a weighted binomial model in statsmodels (identical point estimates); Script 68 checks 29 manuscript figures against tables | Independent checks |
| Bibliography | de Soyres et al. (International Economics) dated 2020 | Corrected to 2019 (vol. 159, pp. 151–164); added Mau & Seuren 2023, Foo et al. 2020 | Verified on RePEc / Springer |
| Length | about 14,000 words, 36 pages | about 16,300 words, 40 pages | Robustness tables, discrepancy table, literature |

New files: `Scripts/67_robustness_baselines_comparators.py`, `Scripts/68_reconcile_manuscript.py`, `Collected_Raw_Data/raw_downloads/comtrade_china_totals_by_partner.txt`; tables `robust_kz_partner_grid.csv`, `robust_china_neighbour_grid.csv`, `robust_export_groups_grid.csv`, `reconciliation_report.csv`. KZ import totals for 2011, 2012, 2014, 2023 added to `comtrade_totals_imports_and_china_exports.txt`.

---

# Fifth Round (2 November 2026): Final Validation

| Area | Before | After | Reason |
|---|---|---|---|
| Research question | "Is the post-2013 swing in Kazakhstan's trade balance with China distinctive ... consistent with the mechanisms through which the BRI was expected to operate" | "Is the post-2013 change in Kazakhstan–China merchandise trade, summarised by the swing in the bilateral balance, distinctive ... consistent with the BRI mechanisms that are observable in merchandise trade" | Distinguishes the balance (accounting summary) from the trade relationship; limits conclusions to what merchandise data can show |
| §1.3 | "Why the trade balance" | "The trade balance and the trade relationship": BRI could expand trade and worsen the balance; investment imports; transit; explicit scope | Conceptual coherence |
| Turnover | Not reported | China-specific turnover: −0.9 to +2.0 bn to 2019; +12.2 to +18.3 bn to 2023–24 | Links to the BRI trade-expansion literature |
| Literature | Narrative §2.3 | Table 2.1: design, outcome, finding and comparability of the four key studies | Requested verification of what they measure |
| Mechanisms | M1 connectivity/market access; M2 resource finance | M1 trade costs; M2 time-sensitive goods and market access; M3 resource finance; M4 investment-linked imports; M5 transit; scorecard with expectation, implication, data needed, evidence, established, untested, verdict (§6.9) | Requested mechanism-by-mechanism assessment |
| Timing | Break at 2013 only | Breaks at 2012, 2013, 2015, 2017 (Table 6.9b, exploratory); dated milestones table (Table 6.13b) with verification status | Announcement ≠ implementation |
| Import comparison | "No faster than neighbours under every comparator" | Withdrawn for the whole period: against the median of Uzbekistan, Tajikistan, Turkmenistan Kazakhstan grew faster (+0.0 to +9.9 bn). Retained for 2019–2024: lowest growth of six (each neighbour separately) | New comparators (excluding Kyrgyzstan; Uzbekistan alone) and partner-by-partner growth (Table 6.10c) |
| Import verdict | "Inconsistent with the timing predicted by M1" | "Not specific to Kazakhstan (2019–2024); does not match a Kazakhstan-specific expansion in 2013–2019; region-wide or lagged BRI contribution inconclusive" | Lagged infrastructure effects cannot be excluded |
| Conclusion | "None of the large components has the timing or direction BRI mechanisms predict" | "The merchandise-trade evidence does not show a change that both matches a BRI mechanism and starts or accelerates at a BRI milestone; not evidence of no effect" | Narrower and accurate |
| Agri-food level | "Consistent with a BRI mechanism (B) in products and channel" | "Matches M2 in products and channel but not in timing; falls short of level B" | Consistent use of the level definitions |
| Synthesis | Table of components | Table 6.14 plus established / interpretation / untested lists | Requested separation of claims |
| Figure 6.7 | Four destinations | All five neighbours and the world | Comparator completeness |
| Files | | Supervisor reply rewritten (old version archived); slides rebuilt (`build_presentation_v5.py`, 16 slides; v4 archived); defence script rewritten (v4 archived); plain-English summary under 250 words | Requested deliverables |
| Verification | 29 figures reconciled | 34 figures reconciled; all tables regenerated from raw files and identical to within 0.001 | |
| Length | about 16,300 words, 40 pages | about 18,100 words, 44 pages | Tables 2.1, 6.9b, 6.10c, 6.13b; scorecard |

New files: `Scripts/69_timing_alternatives.py`, `Scripts/build_presentation_v5.py`, tables `trend_break_alternative_years.csv`, `china_exports_growth_by_partner.csv`. New sources (pages accessed): Tengrinews (24 Dec 2012, Altynkol–Khorgos), Kazinform (21 May 2015, Western Europe–Western China planned completion), Fergana Agency (30 Sep 2025, Dostyk–Moyynty second track).
