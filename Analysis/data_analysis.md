# Preliminary Data Analysis

## Status and Scope

This file provides a preliminary descriptive analysis using public World Bank WITS and World Bank WDI API data collected on 2026-04-19. It is included so the repository contains actual data analysis, summary statistics, and figures rather than only placeholders.

The analysis is still preliminary. WITS `Ores and Metals` exports are used as a cautious proxy for mineral export exposure. They are not a final HS-level measure of uranium, copper, or other strategic minerals. A final strategic-mineral dataset should still be constructed from UN Comtrade after a subscription key is available and the commodity codes are documented.

## Data Sources

- World Bank WITS API: Kazakhstan as reporter, China as partner, all products, export and import trade value.
- World Bank WITS API: Kazakhstan as reporter, China as partner, `Ores and Metals`, export trade value.
- World Bank WDI API: Kazakhstan GDP in current US dollars.

Values from WITS are reported in US dollars thousand and are converted to current US dollars in the cleaned dataset.

## Descriptive Statistics

The cleaned panel covers 2000-2023 and contains 24 annual observations. Kazakhstan recorded a positive bilateral trade balance with China in 23 years and a negative balance in 1 year.

In 2023, Kazakhstan's exports to China were approximately USD 14.76 billion, imports from China were approximately USD 16.77 billion, and the bilateral trade balance was approximately USD -2.01 billion. Ores and metals exports were approximately USD 6.04 billion, equal to about 40.9 percent of Kazakhstan's exports to China.

### Pre-BRI and Post-BRI Comparison

| period | years | observations | mean_exports_usd_million | mean_imports_usd_million | mean_trade_balance_usd_million | mean_ores_metals_exports_usd_million | mean_ores_metals_export_share_pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Pre/transition BRI | 2000-2013 | 14 | 6317.55 | 2970.31 | 3347.25 | 1917.9 | 35.32 |
| Post-BRI | 2014-2023 | 10 | 7851.29 | 5770.5 | 2080.79 | 2759.02 | 35.17 |

### Summary Statistics

| variable | unit | observations | mean | median | minimum | maximum |
| --- | --- | --- | --- | --- | --- | --- |
| Exports to China | USD million | 24 | 6956.61 | 6098.03 | 646.65 | 16484.41 |
| Imports from China | USD million | 24 | 4137.06 | 3620.33 | 150.92 | 16772.25 |
| Trade balance | USD million | 24 | 2819.56 | 1441.41 | -2013.57 | 11270.42 |
| Ores and metals exports | USD million | 24 | 2268.37 | 2114.14 | 47.78 | 6039.36 |
| Ores and metals export share | percent | 24 | 35.26 | 34.66 | 7.1 | 55.14 |

## Generated Figures

- `Outputs/generated_figures/exports_imports_over_time.svg`
- `Outputs/generated_figures/trade_balance_over_time.svg`
- `Outputs/generated_figures/ores_metals_share_over_time.svg`

## Preliminary Interpretation

The descriptive evidence supports the idea that Kazakhstan-China trade expanded substantially over the sample period. However, the trade balance does not move in a simple linear way. This supports the project's central argument that trade growth should not be treated as equivalent to trade-balance improvement.

The ores and metals proxy is analytically useful because it shows that mineral-related exports form a large part of Kazakhstan's exports to China in many years. At the same time, this proxy is broader than the final strategic-mineral concept. The final paper should therefore describe these figures as preliminary descriptive evidence and avoid claiming that they measure uranium or copper exports directly.

## Remaining Work

1. Obtain UN Comtrade API access or manually download verified HS-level commodity data.
2. Define the exact strategic mineral basket before regression modeling.
3. Re-run descriptive tables and figures using the final strategic mineral measure.
4. Estimate the regression model only after the final data construction is documented.
