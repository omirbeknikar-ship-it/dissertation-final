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

The repository now includes a preliminary descriptive data analysis based on public World Bank WITS and WDI API data for 2000-2023. The generated analysis includes a cleaned country-year panel, summary statistics, pre-BRI and post-BRI comparison tables, and SVG figures.

The project is still not a final empirical paper. The current mineral measure uses WITS `Ores and Metals` exports as a cautious proxy for mineral export exposure. A final HS-level strategic mineral dataset for uranium, copper, and related categories still needs to be constructed from UN Comtrade or another verified commodity-level source before final regression claims are made.

## Research Integrity Notes

- No fabricated empirical results are included.
- No fabricated citations or bibliographic references are included.
- Preliminary descriptive statistics are generated from public API data and saved in `Outputs/generated_tables/`.
- Preliminary figures are generated from the cleaned panel and saved in `Outputs/generated_figures/`.
- Regression results are still pending because the final strategic mineral variable has not yet been built from HS-level commodity data.
