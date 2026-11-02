# Evidence Audit

Every factual or numerical claim in the reconstructed thesis is traced here to its source. Status: **V** = verified against the source in this session; **C** = computed by a script in this repository from verified data; **U** = could not be verified (stated as such in the thesis).

## 1. Data sources

| Source | What was checked | Status |
|---|---|---|
| UN Comtrade HS-2, KZ → China, 2005–2024 | Retrieved year by year; 2024 chapter values match Trading Economics/Comtrade figures checked earlier (HS26 3.944 bn, HS27 3.278, HS74 2.695, HS28 1.776, HS72 1.101) | V |
| UN Comtrade HS-2, KZ → World | Chapter sums vs WDI totals: within ±1.3% in 14 of 18 retrieved years; 2010 −4.5%, 2011 +4.5%, 2012 +6.7%, 2021 −12.5% (explained in §4.3) | V/C |
| UN Comtrade HS-2, China ← KZ (mirror) | 2013 total 16.05 bn; mirror ratios 0.89–1.28 outside 2020–2022 | V/C |
| UN Comtrade HS-2, China → KZ, 2013/2019/2024 | 2013 (12.55) and 2019 (12.73) match the earlier independently retrieved totals in v2 Table 4.6 | V |
| 2022 KZ → World response | Rejected: duplicated values (HS83 = HS85 = 993,254,110.654) and HS27/28 missing | Documented |
| World Bank WDI TX.VAL.MRCH.CD.WT | Retrieved from api.worldbank.org | V |
| AidData GCDF 3.0 | Kazakhstan, "Recommended For Aggregates" = Yes, n = 155; dataset page confirms version, date (6 Nov 2023) and coverage (2000–2021) | V |

## 2. Contextual claims

| Claim | Source | Status |
|---|---|---|
| Xi proposed the Silk Road Economic Belt at Nazarbayev University, Astana, 7 Sept 2013 | China Daily, 7 Sept 2013 (search result title "President Xi proposes Silk Road economic belt", dated URL) | V (title and date from URL; full text not fetched) |
| Khorgos dry port launched 2015; Lianyungang and COSCO joined 2017 with a 49% stake | KTZ Express blog | V (company source, not independent) |
| Protocols for 24 plant and livestock products; agri exports to China "doubled", USD 653.3 m | Astana Times, 6 Nov 2023 | V (period of the figure not stated in the article) |
| Dates of individual phytosanitary protocols | none | **U** (stated in §6.7) |
| China 27.4% of KZ imports, 18.7% of exports (2023) | Bureau of National Statistics (archived copy, verified in an earlier session) | V |
| KZ ≈ two-thirds of China's natural uranium imports (2023); Chinese firms accepted minority positions | Pan (2024), Carnegie, quote checked | V |
| KZ 39% of world mined uranium, 2024 | World Nuclear Association page, updated 23 Oct 2026 | V |
| China's share of KZ refined copper exports 65.4% → 49.1% (Jan–Nov 2024 vs 2025); Türkiye 40.9% | Astana Times, 25 Feb 2026 | V |
| Chinese-financed copper mines entered production after 2013 | none | **U**, removed from text |
| Pre-2013 Kazakhstan–China oil pipeline | none fetched this session | **U**, removed from text; only AidData-recorded projects are named |
| Reason for the 2020–2022 suppression | none | **U**, stated as "consistent with confidentiality suppression … cannot be confirmed" |
| Share of Chinese goods in KZ re-exports to Russia | none | **U**, stated as not measurable |

## 3. Results (all C, from scripts)

| Claim | Table / file |
|---|---|
| Balance +3.51 (2013), −3.87 (2019), −12.04 (2024) bn | `trade_balance_decomposition.csv` |
| Energy −7.56, imports +15.23, metals +5.56/+5.62 | same |
| Oil 62% → 22%, metals 36% → 67%, agri 0.5% → 6.6% of exports to China | `composition_kz_exports_to_china.csv` |
| China's shares by group, Table 6.3 | `china_share_by_group.csv` |
| HHI 0.415 → 0.203 → 0.173; excl. HS27 0.212 → 0.187 → 0.205 | `diversification_indices.csv` |
| PPML coefficients, Table 6.4 | `ppml_main.csv` |
| Event study, Table 6.5; Wald χ²(8) = 664 | `ppml_event_study.csv`, `ppml_pretrend_test.csv` |
| Trend break δ = −0.368, p = 0.020 | `ppml_trend_break.csv` |
| Extensive margin pooled 0.013 (p = 0.75); agri 0.207 (p = 0.06) | `extensive_margin_lpm.csv` |
| AidData by sector/period; 48.1 bn pre-2014, 16.0 bn 2014–21 | `aiddata_by_sector_period.csv` |
| Two-sided dependence, Table 7.1 | `two_sided_dependence_2024.csv` |
| KZ HS84/85/87 exports to Russia 0.33 → 2.25 bn | `russia_manufactures_check.csv` |
| Agri chapters (HS15, 23, 10, 12) | `agrifood_chapters.csv` |

## 4. References added (checked against)

| Reference | Checked against |
|---|---|
| Melitz 2003, Econometrica 71(6) 1695–1725 | RePEc record |
| Chaney 2008, AER 98(4) 1707–21 | RePEc record, DOI |
| Hummels & Klenow 2005, AER 95(3) 704–723 | RePEc record, DOI |
| Imbs & Wacziarg 2003, AER 93(1) 63–86 | RePEc record |
| Cadot, Carrère & Strauss-Kahn 2011, REStat 93(2) 590–605 | RePEc record |
| Santos Silva & Tenreyro 2006, REStat 88(4) 641–658 | RePEc record, DOI |
| AidData 2023; Custer et al. 2023 | AidData dataset page ("Custer, S., et al. 2023" as given there; full author list not reproduced) |
| China Daily 2013; KTZ Express; Astana Times 2023, 2026; Pan 2024; WNA 2026; WDI 2026; UN Comtrade 2026 | Pages fetched or located this session |

## 5. The earlier critique, re-checked as hypotheses

| Earlier criticism | Verdict after reconstruction |
|---|---|
| A post-2013 dummy in one country-pair time series cannot separate the BRI from the oil price collapse | **Confirmed.** The 2013–2019 balance change equals the oil fall (§6.1). |
| "Strategic minerals" drove the balance | **Refuted.** Minerals rose in both phases. |
| The asymmetric-interdependence framework was not tested by the regressions | **Confirmed.** Moved to discussion and given two-sided data (Table 7.1). |
| Trade concentration implies Chinese leverage | **Not supported as an assumption.** Dependence is mostly asymmetric, reversed for uranium, and copper exports were redirected in 2025. |
| Kazakhstan's 2020–2022 data are unreliable | **Confirmed and extended**: exports of HS74/76/79 are also missing, not only imports. |
| N = 24 is too small | **Addressed differently**: product × destination panel (3,160 obs.), but effective information is still limited (12–24 chapters per group; energy one chapter). |
| The BRI changed Kazakhstan's export composition | **Not supported as a causal claim**; the main China-specific change predates 2013. |


## 6. Second round additions

| Claim | Source / file | Status |
|---|---|---|
| KZ imports: World 48.80 / China 8.36 (2013); 39.71 / 6.79 (2019); 59.79 / 15.15 (2024) bn | Comtrade TOTAL, `comtrade_totals_imports_and_china_exports.txt` | V |
| WDI KZ merchandise imports 2013 48.81, 2019 37.76, 2024 59.13 bn (2013 matches Comtrade; 2019 and 2024 differ by 5% and 1%) | `wdi_kaz_merch_imports.csv` | V |
| China's exports to KZ, KG, UZ, RU, World (2013, 2019, 2024) | Comtrade TOTAL, China as reporter | V |
| China's 2024 imports from World, selected chapters | `comtrade_hs2_chn_imports_from_world_2024_selected.txt` | V |
| China-reported exports to KZ 2020–2023 (11.70, 13.76, 16.36, 24.70) | Earlier retrieval, v2 Table 4.6 / Appendix B Table B.2 | V (earlier session) |
| 92% China-specific; components in Tables 6.3, 6.4, 6.14 | Script 65 | C |
| Holm, one-sided and randomisation results (Table 6.12) | Script 66 (seed 20261031, 300 draws) | C |

## 7. Correction of an earlier statement

The first reconstruction's §3.3 stated that "the product-level panel and all tests in Chapters 5–6 were built and run after the expectations and the decision rules above were fixed." This was inaccurate: descriptive China shares by product group were computed before the group-level predictions were written, and the trend-break test was added after the event study was seen. The revised §3.4 and §5.7 state this correctly.

| Import benchmarks, Table 6.10b | Script 65, `import_benchmarks.csv` (from Comtrade totals above) | C |


## 8. Final audit (1 November 2026)

| Item | Check performed | Result |
|---|---|---|
| All output tables | Deleted the panel and regenerated every table from raw files with Scripts 60–67 | All values identical to within 0.001 |
| Main PPML | Re-estimated as weighted binomial logit of China's share (statsmodels), an equivalent model with chapter-year effects | Point estimates identical to 4 decimals; clustered SEs within about 4 per cent |
| Holm, CIs, permutation | Recomputed by hand from `ppml_trend_break.csv` and `multiple_testing.csv` | Agri trend δ CI −0.676 to −0.059; Holm 0.0585; permutation shares as reported |
| Manuscript figures | Script 68 recomputes 29 key figures from tables and searches the manuscript | 29 of 29 found |
| Funnel arithmetic | 15.55 = (15.91 − 27.95) − (16.05 − 12.55); 14.31 = 0.20 + 14.11; 92% = 14.31/15.55 | Correct as arithmetic; "upper bound" interpretation removed; "≈0" removed as base-dependent |
| China totals by partner, 2011–2014, 2019, 2023, 2024 | Comtrade TOTAL, China as reporter (`comtrade_china_totals_by_partner.txt`) | V |
| KZ import totals 2011, 2012, 2014, 2023 | Comtrade TOTAL (2023 China value 16.77 bn matches the earlier monthly-based figure) | V |
| de Soyres et al. | RePEc: International Economics 159 (2019) 151–164; 1.7–3.2% shipment-time and 1.5–2.8% trade-cost reductions for BRI economies; up to 11.9% / 10.2% on corridors | V; bib year corrected |
| Baniya, Rocha, Ruta (2020) | RePEc abstract: up to 4.1% trade increase; about three times larger with reforms | V |
| Foo, Lean, Salim (2020) | RePEc: NAJEF 54; positive significant OBOR dummy, 2000–2016 | V |
| Mau & Seuren (2023) | Springer: Review of World Economics 159(2) 257–297; rail connections raised European exports to China | V (effect size from body text, not quoted) |
| Import composition shares (47% capital/durable, 29% apparel and footwear of the 2019–24 rise) | Computed from `import_composition_china_reported.csv` | C |


## 9. Final validation (2 November 2026)

| Item | Check | Result |
|---|---|---|
| Swing 15.55 bn | (15.91 − 27.95) − (16.05 − 12.55) from China-reported totals | Reproduced |
| China-specific 14.31 bn, 92% | Script 65; KZ-reported version 5.74 of 6.27 (92%) | Reproduced |
| 52–92% range; 71% averaged | Script 67 grid (16 cells; 2014→2019 excluded from the range because the swing is only −0.9 bn) | Reproduced |
| Turnover China-specific | Script 67: −0.93 to +2.01 (to 2019); +12.18 to +18.28 (to 2023–24) | Computed |
| Neighbour comparisons | Script 67 with six comparator sets, two weightings, 16 cells | Computed; the "every comparator" claim failed for the median of UZ/TJ/TM and was withdrawn |
| Growth by partner 2019–24 | KZ ×2.20; RU ×2.32; KG ×3.17; UZ ×2.31; TJ ×2.21; TM ×2.39 | Computed from China-reported totals |
| Alternative break years | Script 69 (PPML trend break at 2012, 2013, 2015, 2017) | Agri-food one-sided p for acceleration 0.96–0.99 |
| Altynkol–Khorgos rail crossing opened December 2012 | Tengrinews, 24 Dec 2012 | V |
| Western Europe–Western China road, KZ section completion planned for 2016 | Kazinform, 21 May 2015 | V (plan only; actual completion not verified) |
| Dostyk–Moyynty second track inaugurated | Fergana Agency, 30 Sep 2025 | V |
| Khorgos Gateway 2015; 49% stake 2017 | KTZ Express blog | V (company source) |
| Construction start and completion dates of AidData road projects | Not found | U; stated in Table 6.13b |
| Literature Table 2.1 | Abstracts on RePEc/Springer (see §8) | V; Mau & Seuren effect sizes not quoted |
| "Upper bound" | Searched manuscript, slides, script, supporting files | Appears only as negation ("not an upper bound/bound") or in the change log/examiner notes describing its removal |
| Manuscript figures | Script 68 | 34 of 34 found |

## 10. Benchmarking round (2 November 2026)

| Claim | Source | Status |
|---|---|---|
| Huang, Yenina and Hossain (2021) apply margin and intra-industry trade indices to China–Kazakhstan trade, 2002–2017 | *Chinese Studies* 10(1), 1–16, doi:10.4236/chnstd.2021.101001 (SCIRP) | V (abstract and article record checked when the entry was added); SCIRP outlet, used for context only |
| BRI simulation: Kazakhstan exports +10.7%, imports +15.4%; China's exports to Kazakhstan +29.1% (2022) | Krulikowski and Riker, USITC Economics Working Paper 2024-04-B, https://www.usitc.gov/publications/332/working_papers/krulikowski_and_riker_2024_bri.pdf | V (working paper, not peer-reviewed; stated in §2.6) |
| Ministry of Trade and Integration of the Republic of Kazakhstan (named in §7.9) | https://www.gov.kz/memleket/entities/mti?lang=en | V (official name on the government portal) |
| Bureau of National Statistics (named in §7.9) | Already cited as a data source (§4.1) | V |
| Section page numbers in the benchmarking table | Extracted from final_dissertation.pdf with pypdf after the build | C |
| Manuscript figures | Script 68 | 34 of 34 found |
