# BRI's Impact on Kazakhstan-China Trade Balance: The Role of Strategic Mineral Exports

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
- OLS association models with HAC (Newey–West) standard errors; gravity-ratio specification as primary (replaces collinear GDP levels)
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
python Scripts/35_collinearity_resolution.py  # VIF comparison (NEW)
python Scripts/36_synthetic_control.py    # synthetic control (NEW)
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

- **n = 24** annual observations; all inference is small-sample and fragile.
- **HS-27 bilateral oil/energy data** were not available; mineral coefficient may absorb commodity dynamics.
- **Multi-partner DiD** was not executed due to IMF DOTS API unavailability; within-unit ITS is a weaker substitute.
- **2022–2023** are geopolitically contaminated (Russia-sanctions parallel imports); the regression finding depends on these years.
- **No causal identification** is claimed or achieved.

## Research Integrity Notes

- No fabricated empirical results are included.
- No fabricated citations or bibliographic references are included.
- All regression outputs are computed from real observed data and saved in `Outputs/generated_tables/`.
- All figures are generated programmatically and saved in `Outputs/generated_figures/`.
- The energy proxy in §6.12 of the paper is clearly labelled **illustrative only** — it is not observed HS-27 data.
- The within-unit synthetic control is presented as a weaker substitute for a true multi-partner design, not as causal evidence.
- The dissertation explicitly acknowledges fragile findings, the influence of the 2023 observation, multicollinearity in GDP controls, and the absence of causal identification.
