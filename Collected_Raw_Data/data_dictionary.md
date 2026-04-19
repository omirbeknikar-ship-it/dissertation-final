# Data Dictionary

This file defines the planned variables for the working dataset. Final variables may be revised after verified data are collected, but any changes should be documented.

## Unit of Analysis

The planned unit of analysis is:

```text
country-pair year: Kazakhstan-China annual trade relationship
```

## Core Variables

| Variable | Type | Planned Source | Definition | Status |
| --- | --- | --- | --- | --- |
| `year` | Integer | All sources | Calendar year of observation. | Pending |
| `exports_kazakhstan_to_china_usd` | Numeric | IMF DOTS or verified bilateral source | Annual exports from Kazakhstan to China in current USD. | Pending |
| `imports_kazakhstan_from_china_usd` | Numeric | IMF DOTS or verified bilateral source | Annual imports from China to Kazakhstan in current USD. | Pending |
| `total_bilateral_trade_usd` | Numeric | Constructed | Exports plus imports between Kazakhstan and China. | Pending |
| `trade_balance_usd` | Numeric | Constructed | Kazakhstan's exports to China minus Kazakhstan's imports from China. | Pending |
| `trade_balance_ratio` | Numeric | Constructed | Trade balance divided by total bilateral trade. | Pending |
| `strategic_mineral_exports_usd` | Numeric | UN Comtrade | Annual value of selected strategic mineral exports from Kazakhstan to China. | Pending |
| `strategic_mineral_export_share` | Numeric | Constructed | Strategic mineral exports divided by Kazakhstan's total exports to China. | Pending |
| `ores_metals_exports_usd` | Numeric | World Bank WITS | Preliminary proxy for mineral export exposure using WITS `Ores and Metals` exports. | Available |
| `ores_metals_export_share` | Numeric | Constructed | WITS `Ores and Metals` exports divided by Kazakhstan's total exports to China. | Available |
| `post_bri` | Binary | Constructed | Indicator equal to 1 for years after 2013 and 0 otherwise. | Available |
| `gdp_kazakhstan_current_usd` | Numeric | World Bank WDI | Kazakhstan's GDP in current USD. | Available |
| `exchange_rate_optional` | Numeric | World Bank WDI | Exchange rate indicator, if included. | Optional |
| `commodity_price_proxy_optional` | Numeric | External verified source | Commodity price proxy, if theoretically justified. | Optional |

## Planned Transformations

Possible transformations include:

```text
log_exports = log(exports_kazakhstan_to_china_usd)
log_imports = log(imports_kazakhstan_from_china_usd)
log_strategic_mineral_exports = log(strategic_mineral_exports_usd)
```

Log transformations should be used only after checking for zero or missing values. If zeros appear, the treatment must be documented.

## BRI Period Coding

The initial coding plan is:

```text
post_bri = 0 for years before 2013
post_bri = 1 for years after 2013
```

The year 2013 requires an explicit coding decision because BRI was announced during that year. The preferred approach is to test sensitivity by coding 2013 separately or excluding it in a robustness check if the sample allows.

## Missing Data Rules

Missing data should not be silently replaced. Any imputation, interpolation, or exclusion must be documented in the cleaning script and in the final methodology section.

## Data Status

A preliminary cleaned dataset is included at:

```text
Collected_Raw_Data/clean/kazakhstan_china_trade_panel.csv
```

This dataset is suitable for descriptive analysis. It is not yet the final regression dataset because the strategic mineral variable still needs to be replaced with a verified HS-level commodity basket.
