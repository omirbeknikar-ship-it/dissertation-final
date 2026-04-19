# IMF DOTS Notes

## Source Purpose

The IMF Direction of Trade Statistics (DOTS) will be used as a planned source for annual bilateral trade flows between Kazakhstan and China. The main value of this source is that it provides a consistent country-pair structure for exports and imports over time.

## Planned Use in This Project

The project will use DOTS to verify or construct annual values for:

```text
exports_kazakhstan_to_china_usd
imports_kazakhstan_from_china_usd
total_bilateral_trade_usd
trade_balance_usd
trade_balance_ratio
```

The trade balance will be calculated from Kazakhstan's perspective:

```text
trade_balance_usd = exports_kazakhstan_to_china_usd - imports_kazakhstan_from_china_usd
```

## Collection Status

Data collection is pending. No DOTS data file has been added to this repository yet. Once collected, the raw data file should be stored separately from cleaned analysis files, and the download date should be recorded in this note.

## Expected Strengths

- Provides standardized bilateral trade flow data.
- Useful for constructing the main dependent variable.
- Allows comparison across pre-BRI and post-BRI years.

## Expected Limitations

- DOTS is not designed to identify detailed commodity composition.
- Reported values may differ from mirror statistics in Chinese or Kazakhstani sources.
- The source is useful for aggregate trade balance but not sufficient for strategic mineral export measurement.

## Planned Cleaning Notes

After downloading, the dataset should be checked for:

1. Country naming consistency for Kazakhstan and China.
2. Currency units and whether values are reported in current USD or another unit.
3. Missing years.
4. Differences between reporter-based and partner-based values.
5. Whether re-exports or reporting revisions affect interpretation.

## Research Integrity Note

This file documents a planned data source. It does not report final values or empirical findings.
