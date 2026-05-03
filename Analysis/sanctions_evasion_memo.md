# Sanctions Evasion Channel: Analysis Memo

**Prepared:** 2026-05-03
**Script:** `Scripts/32_sanctions_robustness.py`
**Output:** `Outputs/generated_tables/sanctions_channel.csv`

---

## Background

Kazakhstan's imports from China surged sharply in 2022–2023, coinciding with Western
sanctions on Russia following the February 2022 invasion of Ukraine. A significant
hypothesis in the economic commentary is that this surge partly reflects *parallel imports*:
Western goods (electronics, machinery, vehicles — HS 84, 85, 87) routed through Kazakhstan
to Russia, avoiding direct Western-to-Russia trade restrictions. If correct, this would mean
the 2023 bilateral trade deficit is partly a sanctions-evasion artefact rather than a
structural BRI-driven outcome.

## Import Surge Magnitude

- KAZ imports from CHN in 2021: USD 2.42 bn (if available)
- KAZ imports from CHN in 2022: USD 3.58 bn
- KAZ imports from CHN in 2023: USD 16.77 bn
- 2022 vs 2021 growth: 47.5%
- 2023 vs 2022 growth: 369.2%

The 2022–2023 import acceleration is the largest two-year surge in the 2000–2023 sample.

## HS-Level Decomposition

**Data note:** [DATA_GAP] Comtrade file does not contain Kazakhstan import rows from China (partnerCode=156). All rows have partnerCode=0 (World). HS-level decomposition by partner not possible from this file.

## Regression Robustness Results

The table below shows how the key interaction coefficient changes under sanctions-era
exclusion and parallel-imports control:

| Model | N | Interaction β | HAC SE | p-value | Interpretation |
|-------|---|---:|---:|---:|---|
| Baseline parsimonious (2000–2023) | 24 | -2.382 | 0.977 | 0.015 | Full sample reference |
| Excl. 2022–2023 | 22 | 0.134 | 0.317 | 0.672 | Sanctions period excluded |
| Parallel-imports dummy | 24 | -1.906 | 1.34 | 0.155 | Dummy = 1 for 2022–2023 |

## Key Finding

After excluding 2022–2023 and after controlling for a parallel-import dummy, the
post-BRI mineral interaction coefficient **does not survive**
(attenuated by 105.6% relative to full-sample baseline).

This result is **consistent with the thesis's honest-reporting approach**: the 2022–2023
import surge has a large influence on the headline coefficient, and part of this influence
may reflect the Russia-sanctions parallel-import channel rather than BRI-specific structural
change. The thesis therefore reports both the full-sample and sanctions-excluded results
as co-equal findings, without suppressing either.

## Limitations

1. **HS 84/85/87 data gap:** The local Comtrade extract does not contain HS chapters 84,
   85, or 87 imports from China. A direct test of whether electronics/machinery/vehicle
   imports from China to Kazakhstan accelerated disproportionately in 2022–2023 is not
   possible with current local data. This is flagged as [DATA_GAP] and noted in §6.4
   of the dissertation.

2. **KAZ→RU re-export data:** Year-on-year growth in Kazakhstan's re-exports to Russia
   in the same HS categories would provide direct evidence of the parallel-import channel.
   This data is not in the local repository and would require a separate Comtrade pull
   (KAZ as reporter, RUS as partner, HS 84/85/87, export flow).

3. **Causal ambiguity:** Even if the 2022–2023 surge partly reflects sanctions routing,
   it does not *disprove* the BRI interpretation — BRI infrastructure may have enabled
   the routing capacity. Both channels can be simultaneously operative.

---
*See `Outputs/generated_tables/sanctions_channel.csv` for the full regression table.*
*See dissertation §6.4 for the academic write-up of these findings.*
