# UN Comtrade Notes

## Source Purpose

UN Comtrade will be used as the planned source for commodity-level trade data. It is necessary for identifying Kazakhstan's strategic mineral exports to China, which cannot be measured from aggregate bilateral trade data alone.

## Planned Use in This Project

The project will use UN Comtrade to construct:

```text
strategic_mineral_exports_usd
strategic_mineral_export_share
uranium_related_exports_usd_optional
copper_related_exports_usd_optional
```

The exact commodity categories must be selected carefully after reviewing the relevant Harmonized System (HS) codes and checking whether Kazakhstan reports the relevant categories consistently across years. Candidate categories may include uranium-related and copper-related products, but final inclusion must be documented before analysis.

## Collection Status

Data collection is pending. No commodity-level extract has been added to this repository yet. After collection, the raw data file should preserve the original reporter, partner, trade flow, commodity code, commodity description, year, and trade value columns.

## Expected Strengths

- Allows measurement of strategic mineral exports rather than only aggregate exports.
- Supports analysis of trade composition.
- Helps distinguish export growth driven by minerals from broader export diversification.

## Expected Limitations

- Commodity classifications may change across HS revisions.
- Some strategic mineral categories may be reported at different levels of aggregation.
- Reported values may differ depending on whether Kazakhstan's export data or China's import data are used.
- Mineral export values can reflect price changes as well as quantity changes.

## Planned Cleaning Notes

The cleaning process should document:

1. Reporter country and partner country choices.
2. Export flow direction.
3. HS revision and code level.
4. Commodity categories included as strategic minerals.
5. Treatment of missing values and suppressed data.
6. Whether values are reported as current USD.

## Research Integrity Note

Strategic mineral export categories will not be selected to force a desired result. The selection must be theoretically justified and documented before model estimation.
