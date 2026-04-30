# Codebook — Kazakhstan–China BRI Trade Study

## Unit of Analysis

Annual bilateral trade relationship: Kazakhstan ↔ China, 2000–2024.

## HS-6 Commodity Basket

All codes are HS 2017. Where data are available at HS-4 or HS-2, the aggregation level is noted.

### minerals_narrow (uranium + copper + chromium)

| HS Code | Description |
|---------|-------------|
| 261200  | Uranium or thorium ores and concentrates |
| 284410  | Natural uranium, its compounds, alloys, dispersions, ceramics |
| 284420  | Uranium enriched in U235 and its compounds |
| 260300  | Copper ores and concentrates |
| 740311  | Copper cathodes, unwrought |
| 740319  | Copper, unwrought (other) |
| 261000  | Chromium ores and concentrates |
| 720241  | Ferro-chromium containing > 4% carbon |
| 720249  | Ferro-chromium, other |

### minerals_broad (narrow + zinc + lead + titanium + rare earths)

All codes from minerals_narrow, plus:

| HS Code | Description |
|---------|-------------|
| 260800  | Zinc ores and concentrates |
| 790110  | Zinc, unwrought, not alloyed |
| 260700  | Lead ores and concentrates |
| 780110  | Lead, unwrought, refined |
| 261400  | Titanium ores and concentrates |
| 810891  | Titanium waste and scrap |
| 810899  | Titanium and articles thereof, n.e.c. |
| 280530  | Rare-earth metals, scandium and yttrium |
| 284610  | Cerium compounds |
| 284690  | Compounds of rare-earth metals, n.e.c. |

### oil_exports (HS 2709)

| HS Code | Description |
|---------|-------------|
| 270900  | Petroleum oils, crude |

## Panel Variables

| Variable | Type | Source | Definition |
|----------|------|---------|------------|
| year | int | all | Calendar year, 2000–2024 |
| exports_kaz_to_chn | float | Comtrade/WITS | KAZ exports to CHN, current USD |
| imports_kaz_from_chn | float | Comtrade/WITS | KAZ imports from CHN, current USD |
| total_bilateral_trade | float | constructed | exports + imports |
| trade_balance | float | constructed | exports − imports |
| trade_balance_ratio | float | constructed | trade_balance / total_bilateral_trade |
| minerals_narrow | float | Comtrade HS-6 | Sum of narrow basket exports (USD) |
| minerals_broad | float | Comtrade HS-6 | Sum of broad basket exports (USD) |
| oil_exports | float | Comtrade HS-6 | HS 270900 exports (USD) |
| minerals_proxy | float | WITS | Ores & metals exports (broad proxy when HS-6 unavailable) |
| brent | float | Pink Sheet / FRED | Annual mean Brent crude (USD/bbl) |
| copper_price | float | Pink Sheet | Annual mean LME copper (USD/mt) |
| kz_gdp | float | WDI NY.GDP.MKTP.KD | KAZ GDP, constant 2015 USD |
| cn_gdp | float | WDI NY.GDP.MKTP.KD | CHN GDP, constant 2015 USD |
| kzt_usd | float | WDI PA.NUS.FCRF | KZT per USD, period average |
| kz_cpi | float | WDI FP.CPI.TOTL | KAZ CPI, 2010=100 |
| cn_cpi | float | WDI FP.CPI.TOTL | CHN CPI, 2010=100 |
| bri_flows_annual | float | AidData GCDF v3 | Annual committed Chinese ODA/OOF to KAZ, nominal USD |
| bri_flows_cumulative | float | constructed | Cumulative sum of bri_flows_annual |
| bri_intensity | float | constructed | log1p(bri_flows_cumulative) |
| post_bri_2013 | int | constructed | 1 if year ≥ 2014, 0 otherwise (2013 is coded 0; sensitivity check at 2013) |
| years_since_announcement | int | constructed | max(0, year − 2013) |

## BRI Period Coding Convention

- `post_bri_2013 = 0` for years 2000–2013 (announcement year coded 0)
- `post_bri_2013 = 1` for years 2014–2024
- Robustness checks vary the threshold: 2013 (inclusive), 2014, 2015, 2016

## Data Availability Notes

The HS-6 disaggregated Comtrade files provided cover only 2014 at HS-2 chapter level; they cannot support the full 2000–2024 HS-6 time series. The variable `minerals_proxy` (WITS Ores & Metals total) is used as the primary observable throughout; `minerals_narrow` and `minerals_broad` are constructed analytically but labeled as WITS-proxy in all tables. See `KNOWN_ISSUES.md`.
