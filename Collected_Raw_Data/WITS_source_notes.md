# WITS Source Notes

## Source Purpose

World Bank WITS is used for the preliminary descriptive analysis in this repository. It provides Kazakhstan-China bilateral trade values and a broad `Ores and Metals` product group that can be used as an initial proxy for mineral export exposure.

## Data Extracts Included

The generated raw extracts are stored in:

```text
Collected_Raw_Data/raw/wits_total_trade_kazakhstan_china.csv
Collected_Raw_Data/raw/wits_ores_metals_exports_kazakhstan_china.csv
```

The cleaned annual panel is stored in:

```text
Collected_Raw_Data/clean/kazakhstan_china_trade_panel.csv
```

## Variables Used

The preliminary analysis uses:

```text
exports_kazakhstan_to_china_usd
imports_kazakhstan_from_china_usd
trade_balance_usd
trade_balance_ratio
ores_metals_exports_usd
ores_metals_export_share
```

WITS reports trade values in US dollars thousand. The script converts them to current US dollars in the cleaned panel.

## Interpretation Limits

`Ores and Metals` is a broad category. It should not be described as a direct measure of uranium, copper, or any exact strategic mineral basket. It is useful for preliminary descriptive analysis, but the final empirical model should use documented HS-level strategic mineral codes from UN Comtrade or another verified commodity-level source.

## Reproducibility

The preliminary analysis can be regenerated with:

```bash
python3 Scripts/generate_preliminary_analysis.py
```
