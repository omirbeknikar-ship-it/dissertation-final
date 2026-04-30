# BRI's Impact on Kazakhstan-China Trade Balance: The Role of Strategic Mineral Exports

This repository contains the working materials for a master's-level term paper research project on Kazakhstan-China trade after the launch of the Belt and Road Initiative (BRI). The project examines whether the expansion of bilateral trade after BRI corresponded with an improvement in Kazakhstan's trade balance with China, and whether strategic mineral exports changed that relationship.

The repository is organized as a research workspace rather than a software product. It contains research planning documents, literature review drafts, data source notes, a preliminary descriptive data analysis, script files, and output folders for tables and figures.

## Research Question

Did the Belt and Road Initiative improve Kazakhstan's bilateral trade balance with China, and did BRI change the effect of strategic mineral exports on that trade balance?

## Project Overview

The starting point of the research is a distinction between trade growth and trade balance improvement. Kazakhstan-China trade expanded substantially in the post-BRI period, but higher trade volume does not necessarily imply a stronger trade position for Kazakhstan. Kazakhstan's exports to China are concentrated in resource-based products, while imports from China include a wide range of manufactured and higher-value goods. Strategic mineral exports, especially uranium and copper-related exports, may improve Kazakhstan's bilateral trade position, but this claim requires empirical testing.

The project uses Dependency Theory and asymmetrical interdependence as its primary theoretical framework. Trade facilitation and connectivity arguments associated with BRI are used as a supporting framework to explain why trade volumes may increase after infrastructure, logistics, and policy coordination improve.

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
- OLS association models with HAC (Newey–West) standard errors
- VIF diagnostics (full model VIF > 100 for GDP controls; parsimonious model VIF < 10)
- Influence diagnostics: Cook's D, leverage, studentised residuals, leave-one-out analysis
- AIC-selected ADL dynamic association model with PSS bounds test
- A 288-specification robustness grid
- Structural-break diagnostics (Chow and Bai–Perron-style)
- A WITS-consistent mineral proxy for robustness

The narrow strategic mineral variable (uranium, copper, chromium) uses WITS Ores and Metals as a proxy for 2000–2013 and UN Comtrade HS-2 codes for 2014–2023. This measurement break is documented in `Paper/final_dissertation.md` §4.3 and addressed by a consistent-proxy robustness specification.

Bilateral oil and energy export data (HS 27) were not available for the full sample period and are treated as an acknowledged omitted variable.

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
python Scripts/10_descriptives.py
python Scripts/11_structural_breaks.py
python Scripts/12_ardl.py
python Scripts/20_robustness.py
python Scripts/30_full_diagnostics.py
python Scripts/31_revision_computations.py
```

Outputs are written to `Outputs/generated_tables/` and `Outputs/generated_figures/`.

## Research Integrity Notes

- No fabricated empirical results are included.
- No fabricated citations or bibliographic references are included.
- All regression outputs are computed from real data and saved in `Outputs/generated_tables/`.
- All figures are generated programmatically and saved in `Outputs/generated_figures/`.
- The dissertation explicitly acknowledges fragile findings, influence of the 2023 observation, multicollinearity in GDP controls, and the absence of causal identification.
