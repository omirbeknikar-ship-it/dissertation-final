# BRI's Impact on Kazakhstan-China Trade Balance: The Role of Strategic Mineral Exports

> **Reconstruction (31 October 2026, branch `thesis-reconstruction`).** The thesis was rebuilt around a new question: was the post-2013 change in the composition of Kazakhstan's exports to China China-specific and BRI-timed, and what does it imply for the bilateral balance? The current manuscript is `Paper/final_dissertation.md` (PDF/DOCX built by Script 50). The previous version is archived in `Paper/archive/`. New analysis: Scripts 60–64 (HS-2 panel, PPML triple difference, event study, trend break, AidData, two-sided dependence). Companion documents: `Paper/change_log.md`, `Paper/research_logic_map.md`, `Paper/evidence_audit.md`, `Paper/examiner_evaluation.md`, `Paper/plain_english_explanation.md`. Run order: `python Scripts/60_build_hs2_panel.py && python Scripts/61_composition_diversification.py && python Scripts/62_ppml_triple_difference.py && python Scripts/63_figures_reconstruction.py && python Scripts/64_two_sided_dependence.py && python Scripts/65_common_vs_china_specific.py && python Scripts/66_multiple_testing_permutation.py && python Scripts/67_robustness_baselines_comparators.py && python Scripts/63_figures_reconstruction.py && python Scripts/50_build_paper.py && python Scripts/68_reconcile_manuscript.py && python Scripts/build_presentation_v4.py` (requires `pyfixest`). Sections below describe the earlier versions and remain for the record.


> **Note on the title.** The officially registered dissertation title uses the word "impact." Throughout this repository and the paper itself, all analysis is **associational and diagnostic**, not causal. No causal effect of BRI is identified or claimed. The term "impact" refers to post-BRI trade-balance dynamics observed in the data. See `Paper/final_dissertation.md` §Abstract for the explicit clarification note.

This repository contains the complete materials for a master's dissertation examining Kazakhstan–China bilateral trade balance dynamics in the post-BRI period, with a focus on the role of strategic mineral exports. The central question is whether strategic mineral export growth in the post-2013 period was associated with sustained trade-balance improvement for Kazakhstan.

The repository is organised as a fully reproducible research pipeline: raw data, cleaned panel, analysis scripts, generated tables and figures, and the final dissertation document are all version-controlled together.

## Research Question

Did the Belt and Road Initiative improve Kazakhstan's bilateral trade balance with China, and did BRI change the effect of strategic mineral exports on that trade balance?

## Project Overview

The starting point of the research is a distinction between trade growth and trade balance improvement. Kazakhstan-China trade expanded substantially in the post-BRI period, but higher trade volume does not necessarily imply a stronger trade position for Kazakhstan. Kazakhstan's exports to China are concentrated in resource-based products, while imports from China include a wide range of manufactured and higher-value goods. Strategic mineral exports, especially uranium and copper-related exports, may improve Kazakhstan's bilateral trade position, but this claim requires empirical testing.

The project uses **asymmetric interdependence** (Keohane & Nye 1977; Hirschman 1945) as its primary theoretical framework, demoting Dependency Theory to historical context. Trade facilitation (Anderson & van Wincoop 2003) and resource-curse channels (van der Ploeg 2011) serve as supporting frameworks.

## Objectives

1. Describe the structure of Kazakhstan-China bilateral trade before and after BRI.
2. Distinguish changes in trade volume from changes in Kazakhstan's bilateral trade balance.
3. Assess whether strategic mineral exports are associated with Kazakhstan's trade balance with China.
4. Test whether the post-BRI period changed the relationship between strategic mineral exports and the trade balance.
5. Develop a cautious and transparent empirical strategy appropriate for annual data and a small sample.

## Repository Structure

```text
Collected_Raw_Data/     Source notes, raw API extracts, and cleaned panel data.
Literature_Review/      Analytical literature review and theoretical framework.
Scripts/                Scripts for preliminary analysis and future R workflow.
Analysis/               Data analysis, model specification, and diagnostics plan.
Outputs/                Generated descriptive tables, figures, and regression placeholders.
Paper/                  Proposal drafts and reflection on the research workflow.
README.md               Repository overview.
Research_Plan.md        Main research plan.
hypothesis_model.md     Hypothesis and model logic.
```

## Current Status

The dissertation is complete. `Paper/final_dissertation.md` is the submission-ready document. All empirical outputs are reproducible from the scripts in `Scripts/`.

The final analysis includes:
- A cleaned annual Kazakhstan–China bilateral panel (2000–2023, *n* = 24)
- OLS association models with HAC (Newey–West) standard errors; GDP growth-rate specification (Scheme B) as primary, gravity ratio (Scheme C) as robustness
- VIF diagnostics: three-scheme comparison (GDP levels max VIF=236; gravity ratio max VIF=33; GDP growth rates max VIF=10)
- Influence diagnostics: Cook's D, leverage, studentised residuals, leave-one-out analysis
- AIC-selected ADL dynamic association model with PSS bounds test
- A 288-specification robustness grid
- Structural-break diagnostics (Chow and Bai–Perron-style)
- A WITS-consistent mineral proxy for robustness
- **Sanctions robustness**: 2022–2023 exclusion and parallel-imports dummy (new)
- **Web-scraped cross-validation**: stat.gov.kz data confirmed 0.1–0.3% discrepancy (new)
- **Synthetic control**: within-unit counterfactual with placebo permutation (new)
- **ITS partner placebo**: interrupted time series with pre-2013 placebo breaks (new)

The narrow strategic mineral variable (uranium, copper, chromium) uses WITS Ores and Metals as a proxy for 2000–2013 and UN Comtrade HS-2 codes for 2014–2023. This measurement break is documented in `Paper/final_dissertation.md` §4.3 and addressed by a consistent-proxy robustness specification.

Bilateral oil and energy export data (HS 27) were not available for the full sample period and are treated as an acknowledged omitted variable.

## Revisions Following Midterm Feedback

The midterm version of this dissertation received a score of 75/100. Following written professor feedback, six revision items were implemented between the midterm and final defense versions:

1. **Theory-method bridge** (Item 1): §3 and §5 rewritten to map every regressor to its theoretical mechanism, predicted sign, and citation. Asymmetric interdependence (Keohane & Nye; Hirschman) promoted to primary framework; Dependency Theory demoted to historical context. Variable selection rationale table (Table 3.1) added. Literature review pillar-bridge sentences added.
2. **Sanctions robustness** (Item 2): `Scripts/32_sanctions_robustness.py` created. Key finding: the BRI mineral interaction does not survive exclusion of 2022–2023 (coefficient +0.134, p=0.672). Full results in `Outputs/generated_tables/sanctions_channel.csv` and `Analysis/sanctions_evasion_memo.md`.
3. **External controls / partner comparison** (Item 3): `Scripts/33_multi_partner_panel.py` and `Scripts/34_did_partner_placebo.py` created. IMF DOTS multi-partner panel attempted (API blocked in current environment; [DATA_GAP]). Within-unit ITS with placebo break years implemented as fallback. True 2013 break significant (p=0.018); 2009/2010 placebos marginally significant (caution warranted).
4. **Multicollinearity** (Item 4): `Scripts/35_collinearity_resolution.py` created. GDP-levels spec (max VIF=236) moved to Appendix B. Gravity ratio spec (max VIF=33) adopted as preferred main specification. VIF comparison table in `Outputs/generated_tables/collinearity_resolution.csv`.
5. **Web scraping** (Item 5): `Scripts/04_scrape_stat_gov_kz.py` created. Scraped Kazakhstan BNS (stat.gov.kz) annual trade publications. Cross-validation shows 0.1–0.3% discrepancy between scraped and panel values for 2023–2024. Results in `Outputs/generated_tables/scraped_validation.csv`.
6. **Causal identification / synthetic control** (Item 6): `Scripts/36_synthetic_control.py` created. Within-unit synthetic control with placebo permutation. Mean post-BRI gap = −0.014 (negative, consistent with adverse shift). Causal language tightened throughout §6–7: claims downgraded to "consistent with" / "associated with."

## Revisions Following Supervisor Feedback (Round 2)

The supervisor raised two points: (1) the small annual sample (N = 24), with the suggestion to disaggregate to quarterly (96) or monthly (288) observations; (2) clearer interpretation of hypothesis tests, model fit statistics, and optionally Granger causality tests.

1. **Sample size.** Two routes were implemented. (a) Denton quarterly disaggregation of the annual panel (n = 96, `Scripts/41`). It reproduces the annual estimates, but a Monte Carlo shows that interpolation adds rows, not information, so it is reported as a robustness check only (§6.17). (b) **Observed monthly UN Comtrade data, 2010-2019 (n = 120)** with NBK exchange rates and Pink Sheet prices (`Scripts/42`, §6.18). H2 and H3 hold (interaction −0.91, p = 0.008, adj. R² = 0.70) without any post-2019 year. They are robust to a trend, copper, dynamics, break date and product-level minerals, but not to controlling for bilateral oil exports (HS 27).
2. **Hypothesis testing and fit.** Formal one-sided tests with H0/H1, t, df, p and the decision (§6.11, `hypothesis_tests_formal.csv`). Full fit statistics for every model (R², adj. R², F, HAC Wald F, AIC, BIC, RMSE, DW, BG, BP, JB, RESET). Granger causality (VAR in differences and Toda-Yamamoto), annual and monthly (§6.19): mineral exports do not Granger-cause the balance. The predictive link exists only pre-BRI in monthly data and is bidirectional.
3. **New data-quality finding.** Kazakhstan-reported imports from China are under-recorded in 2020-2022 (China/Kazakhstan mirror ratio about 2.2 in 2016-2019 versus 4.6-6.0 in 2020-2022, and HS 84/85/87 rows missing). This explains much of the "2023 drives everything" fragility. With mirror-adjusted imports, the interaction survives excluding 2023 and 2022-2023 (§4.7, §6.20, `Scripts/43`). The result is weaker when exports are adjusted too.

## Final Audit (October 2026)

- **References:** six bibliography entries were wrong or unverifiable and have been corrected or removed, and two had minor errors (Jepson & Baldakova 2024; Calabrese 2024; Primiano & Kudebayeva 2025; Grant 2020 replaces a misattributed "Mostowlansky 2020"; a non-existent Petry 2023 book removed; "Keohane & Nye 1973" corrected to 1977; Frank 1967; Prebisch 1950 publisher).
- **Placeholder data removed:** the annual `oil_exports` column was 55% of exports in every year; it has been blanked and the models that used it (ADL, §6.12) re-estimated or withdrawn.
- **DiD re-assessed:** see the Key Limitations entry above and §6.15 (Table 6.10b).
- **Oil channel measured:** HS 27 fell from 59% of exports to China (2010–13) to 36% (2014–19); oil exports fell 89% from 2013 to 2016 (§4.6).

## Reproducing the Analysis

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run scripts in order

```bash
python Scripts/01_load_comtrade.py
python Scripts/01b_load_prices.py
python Scripts/01c_load_wdi.py
python Scripts/01d_load_bri.py
python Scripts/02_mirror_reconcile.py
python Scripts/03_build_panel.py
python Scripts/04_scrape_stat_gov_kz.py   # web scraping (NEW)
python Scripts/10_descriptives.py
python Scripts/11_structural_breaks.py
python Scripts/12_ardl.py
python Scripts/20_robustness.py
python Scripts/30_full_diagnostics.py
python Scripts/31_revision_computations.py
python Scripts/32_sanctions_robustness.py  # sanctions robustness (NEW)
python Scripts/33_multi_partner_panel.py   # multi-partner panel (NEW, needs network for full run)
python Scripts/34_did_partner_placebo.py   # DiD partner placebo (NEW)
python Scripts/44_did_robustness.py        # DiD inference + permutation (final audit)
python Scripts/45_ardl_clean.py            # ADL + CUSUM on observed data only (final audit)
python Scripts/35_collinearity_resolution.py  # VIF comparison (NEW)
python Scripts/36_synthetic_control.py    # synthetic control (NEW)
python Scripts/40_model_fit_hypothesis_tests.py  # fit statistics, formal H1-H3 tests, annual Granger (supervisor round 2)
python Scripts/41_quarterly_interpolation.py     # Denton quarterly disaggregation + Monte Carlo (supervisor round 2)
python Scripts/42_monthly_observed.py            # observed monthly models + monthly Granger (supervisor round 2)
python Scripts/43_import_break_sensitivity.py    # 2020-2022 import reporting break (supervisor round 2)
python Scripts/50_build_paper.py                 # rebuild PDF and DOCX from the markdown
```

Outputs are written to `Outputs/generated_tables/` and `Outputs/generated_figures/`.

## Generating the PDF

A compiled PDF can be generated with Pandoc:

```bash
pandoc Paper/final_dissertation.md \
  --citeproc \
  --bibliography Literature_Review/bibliography.bib \
  -o Paper/final_dissertation.pdf
```

Requires [Pandoc](https://pandoc.org/) and a LaTeX distribution (e.g. TeX Live or MiKTeX).

## Main Findings

- Kazakhstan's imports from China grew by **94.3%** in the post-BRI period (2014–2023) vs. export growth of **24.3%** — import-side deepening is the primary driver of trade-balance deterioration, not export collapse.
- The average bilateral trade balance fell by **37.8%** despite a **29.2%** rise in strategic mineral exports.
- The full-sample OLS interaction coefficient (Minerals × Post-BRI) is **−2.42** (*p* = 0.033, gravity-ratio preferred spec), but this result **does not survive exclusion of 2022–2023** — the two years associated with Russia-sanctions parallel-import routing.
- **2023** is the only year of bilateral deficit (−USD 2.01 bn) and has Cook's D = 3.90 (23× the threshold). The finding is diagnostic, not structural.
- The strongest contribution is the **descriptive decomposition**: import-side deepening is robustly documented regardless of regression specification.

## Key Limitations

- **n = 24** annual observations; partly addressed with 120 observed months (2010-2019). Interpolated quarterly data are not independent evidence.
- **2020-2022 import reporting break** in Kazakhstan-reported data; mirror adjustment is an estimate.
- **HS-27 bilateral oil/energy data** are now available monthly (2010-2023); controlling for them removes the monthly interaction, so H3 is not shown to be mineral-specific.
- **Multi-partner DiD** (6 partners): China shows the largest post-2013 decline (−0.31 to −0.37 across samples), but with six partners inference is imprecise (Driscoll–Kraay p ≈ 0.02; wild cluster bootstrap p ≈ 0.33; permutation p = 0.167). See `Scripts/44`.
- **2022–2023** are geopolitically contaminated (Russia-sanctions parallel imports); the regression finding depends on these years.
- **No causal identification** is claimed or achieved.

## Research Integrity Notes

- No fabricated empirical results are included.
- No fabricated citations or bibliographic references are included.
- All regression outputs are computed from real observed data and saved in `Outputs/generated_tables/`.
- All figures are generated programmatically and saved in `Outputs/generated_figures/`.
- The former annual "energy proxy" (a constant 55% of exports) has been **removed** from the data and the paper; energy is now controlled with observed monthly HS 27 data.
- The within-unit synthetic control is presented as a weaker substitute for a true multi-partner design, not as causal evidence.
- The dissertation explicitly acknowledges fragile findings, the influence of the 2023 observation, multicollinearity in GDP controls, and the absence of causal identification.
