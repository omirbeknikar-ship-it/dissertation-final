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
