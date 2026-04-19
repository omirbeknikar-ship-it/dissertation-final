# World Bank WDI Notes

## Source Purpose

World Bank World Development Indicators (WDI) will be used for macroeconomic context and possible control variables. The WDI source is appropriate for annual national indicators such as GDP, exchange rates, inflation, and trade openness.

## Planned Use in This Project

The primary model will be parsimonious because the dataset is expected to contain annual observations only. WDI variables will therefore be used cautiously. Possible variables include:

```text
gdp_kazakhstan_current_usd
gdp_china_current_usd_optional
exchange_rate_kzt_per_usd_optional
trade_openness_kazakhstan_optional
inflation_kazakhstan_optional
```

The most likely control is Kazakhstan's GDP in current USD, used to account for changes in the scale of the economy. Exchange rate indicators may be considered if they are theoretically useful and do not create an overfitted model.

## Collection Status

Data collection is pending. No WDI extract has been added to this repository yet. The future dataset should record indicator codes, download date, source link, and any transformations.

## Expected Strengths

- Provides standardized macroeconomic indicators.
- Useful for contextualizing bilateral trade patterns.
- Allows limited controls in descriptive or regression analysis.

## Expected Limitations

- WDI does not provide commodity-level bilateral trade data.
- Adding too many controls would be inappropriate for a small annual sample.
- Some variables may be highly correlated with time trends, which would complicate interpretation.

## Planned Cleaning Notes

After collection, the WDI data should be checked for:

1. Indicator code accuracy.
2. Annual coverage matching the trade dataset.
3. Missing observations.
4. Whether values are current USD, constant USD, or index-based.
5. Whether transformations such as logarithms or scaling are needed.

## Research Integrity Note

WDI variables will support context and limited controls. They will not be used to create an appearance of precision that the small sample cannot support.
