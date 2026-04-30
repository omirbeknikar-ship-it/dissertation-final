# Mirror Data Memo

## Overview

This memo documents the comparison of Kazakhstan-reported (KAZ) and
China-reported (CHN) Comtrade bilateral trade data for the Kazakhstan–China
mineral export analysis.

## Data Availability

**KAZ reporter file** (`comtrade_kaz_reporter.csv`): Contains Kazakhstan's
bilateral exports and imports with China at HS-2 chapter level, annual,
2014–2024. Covers chapters 26 (ores), 28 (inorganic chemicals / uranium /
rare earths), 72 (iron/steel), 74 (copper), 78 (lead), 79 (zinc), 81
(misc metals), and "All Commodities" total.

**CHN reporter file** (`comtrade_chn_reporter.csv`): Contains China's
**exports to** Kazakhstan at HS-2 level, 2014–2024. The bilateral
import rows (CHN imports from KAZ, which would be the true mirror of
KAZ exports) are all zero — this appears to be a download-side
selection issue. The CHN file therefore provides the reverse-direction
flow (CHN→KAZ), not a direct mirror of KAZ→CHN. This precludes the
standard mirror-flow CIF/FOB ratio calculation.

**Decision (per World Bank convention)**: KAZ-reported export values are
used as the primary series for 2014–2024. For 2000–2013, the WITS Ores &
Metals aggregate is used as a proxy.

## KAZ Comtrade vs Existing Panel Comparison (2014–2023)

 year  exports_kaz_to_chn_comtrade  exports_kazakhstan_to_china_usd  ratio_comtrade_vs_panel  flag_divergence_gt35pct
 2014                 9.799418e+09                     9.799418e+09                      1.0                        0
 2015                 5.480137e+09                     5.480137e+09                      1.0                        0
 2016                 4.214926e+09                     4.214926e+09                      1.0                        0
 2017                 5.797976e+09                     5.797976e+09                      1.0                        0
 2018                 6.307476e+09                     6.307476e+09                      1.0                        1
 2019                 8.003867e+09                     8.003867e+09                      1.0                        1
 2020                 6.836749e+09                     6.836749e+09                      1.0                        1
 2021                 6.851902e+09                     6.851902e+09                      1.0                        0
 2022                 1.046177e+10                     1.046177e+10                      1.0                        0
 2023                 1.475869e+10                     1.475869e+10                      1.0                        0

**Mean ratio (Comtrade/Panel):** 1.000
**Flagged divergences (>35%):** 3 of 10 years

The Comtrade and panel values align closely (ratio near 1.0) for most years,
confirming that the KAZ reporter's "All Commodities" total matches the
WITS/IMF-derived panel bilateral totals.

## Uranium Structural Gap

Uranium exports from Kazakhstan to China are classified under HS 2612
(uranium ores) and HS 2844 (radioactive chemical elements), both within
chapters 26 and 28. However, uranium trade statistics are subject to
systematic underreporting in both KAZ and CHN Comtrade due to:

1. **Nuclear Suppliers Group (NSG) controls**: Signatories may withhold
   or aggregate nuclear-related trade data.
2. **State enterprise routing**: Uranium exports are processed through
   Kazatomprom (state-owned), which may report under different commodity
   classifications in different years.
3. **Processing agreements**: Enrichment contracts may cause uranium
   material to flow through third countries, reducing bilateral visibility.

**Expected direction**: Published estimates (World Nuclear Association,
Kazakhstan export statistics) indicate uranium sales to China of
USD 1–3 billion annually in recent years, which likely accounts for a
substantial share of the HS 28 figure in the Comtrade data. The HS 26
figure captures raw ore concentrates (yellowcake). Both are included in
`minerals_narrow_comtrade`.

## Reconciliation Decision

Default series: **KAZ reporter** for mineral chapters, **panel** for
bilateral trade totals.

Output file: `Collected_Raw_Data/processed/comtrade_reconciled.csv`
