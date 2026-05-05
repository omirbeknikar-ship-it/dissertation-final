# Known Issues

This file documents known limitations, data gaps, and technical issues in the dissertation analysis pipeline. Each issue is classified by severity and includes the relevant script and a remediation path.

---

## ISSUE-001: Bilateral Oil/Energy Export Data Unavailable (HS 27)

**Severity:** Major analytical limitation  
**Script:** `Scripts/01_load_comtrade.py`; affects `Scripts/31_revision_computations.py` and all regression specifications  
**Status:** [DATA_GAP] — unresolved, acknowledged in §4.5 and §6.10

**Description:** The local Comtrade Kazakhstan-as-reporter file covers only HS chapters 26, 28, 72, 74, 78, 79, and 81. Chapter 27 (petroleum, natural gas, coal) is not present. The `oil_exports` column in `clean_panel_annual.csv` is empty for all 24 sample years. This omission is significant because Kazakhstan's bilateral oil exports to China constitute approximately 60% of total export revenues.

**Consequence:** The mineral coefficient and its interaction term likely absorb broader commodity-export dynamics. The direction and magnitude of omitted-variable bias are unquantifiable with current data.

**Remediation:** Download UN Comtrade KAZ-reporter file for HS chapter 27 via Comtrade API (`/api/get?r=398&p=156&cc=27&rg=2`), aggregate annual FOB values for HS 2709/2710/2711/2701, and re-estimate the parsimonious model with this as an additional control.

---

## ISSUE-002: Multi-Partner Bilateral Trade Panel — IMF DOTS API Blocked

**Severity:** Affects causal identification completeness  
**Script:** `Scripts/33_multi_partner_panel.py`, `Scripts/34_did_partner_placebo.py`  
**Status:** [DATA_GAP] — workaround implemented (within-unit ITS)

**Description:** The two-way fixed-effects DiD partner-placebo design (§6.15) requires Kazakhstan's bilateral trade-balance ratios with Russia, Germany, Uzbekistan, Turkey, and USA as control units. This data is available from IMF Direction of Trade Statistics (DOTS). However, the IMF DOTS REST API (`dataservices.imf.org`) was unreachable due to network restrictions in the current execution environment (SSL timeout).

**Consequence:** The full TWFE DiD with multiple partners was not estimated. An interrupted time series (ITS) with placebo break years was implemented as a within-unit fallback. The ITS evidence is weaker than the cross-partner TWFE design.

**Remediation:** Run `Scripts/33_multi_partner_panel.py` with network access. The IMF DOTS endpoint is `https://dataservices.imf.org/REST/SDMX_JSON.svc/CompactData/DOT/A.KZ.{flow}.{partner}.?startPeriod=2000&endPeriod=2023`. Partners needed: CHN, RUS, DEU, UZB, TUR, USA.

---

## ISSUE-003: HS 84/85/87 Import Decomposition — Sanctions Channel Not Fully Testable

**Severity:** Affects completeness of sanctions-evasion test (§6.14)  
**Script:** `Scripts/32_sanctions_robustness.py`  
**Status:** [DATA_GAP] — regression robustness implemented; HS-level decomposition not possible

**Description:** Testing the parallel-imports hypothesis (§6.14) requires Kazakhstan's imports from China broken down by HS chapter 84 (machinery), 85 (electronics), and 87 (vehicles) — the categories most associated with sanctions-evasion flows. The local Comtrade file covers only mineral/metal HS chapters (26, 28, 72, 74, 78, 79, 81). HS 84/85/87 are not present.

**Consequence:** The direct test of whether these import categories exploded in 2022–2023 is not possible. The regression-based evidence (exclusion of 2022–2023) is reported instead.

**Remediation:** Pull Comtrade KAZ-reporter, CHN as partner, HS chapters 84, 85, 87, import flow, 2000–2023. Compare year-on-year growth against the same categories for KAZ→RUS re-exports to test the parallel-import channel directly.

---

## ISSUE-004: Synthetic Control — Multi-Partner Donor Pool Unavailable

**Severity:** Affects causal identification strength  
**Script:** `Scripts/36_synthetic_control.py`  
**Status:** [DATA_GAP] — within-unit variant implemented; full Abadie design pending

**Description:** The full Abadie (2003) synthetic control requires multiple donor units. The intended donor pool (KZ bilateral balance ratios with Russia, EU, Turkey, USA, Uzbekistan) requires the same IMF DOTS data as ISSUE-002. A within-unit synthetic control using pre-period OLS fit is implemented instead.

**Consequence:** The within-unit SC is a weaker design. Permutation p-value is 0.857 (not significant), partly due to small sample and the use of pre-period subsamples as placebos. The full multi-partner SC would use independent time series as donors and would provide more credible identification.

**Remediation:** Once IMF DOTS data is available (see ISSUE-002), extend `Scripts/36_synthetic_control.py` with the multi-partner donor pool. The script already contains the fallback logic; set `multi_partner_available = True` and populate the `MULTI_PARTNER` CSV.

---

## ISSUE-005: Web Scraping — stat.gov.kz Historical Publications (Pre-2023)

**Severity:** Minor (validation only)  
**Script:** `Scripts/04_scrape_stat_gov_kz.py`  
**Status:** [PARTIAL] — 2023 and 2024 validated; pre-2022 not scraped

**Description:** The stat.gov.kz publications index only shows approximately 30 recent publications per page. Annual "January-December" publications prior to 2023 require pagination or sequential ID search. The 2023, 2024, and 2025 annual reports were successfully scraped and cross-validated.

**Consequence:** Cross-validation is limited to 2023–2024. Earlier years (2000–2022) were validated against WITS/Comtrade only (not against the BNS scrape). The 2023 figure is the most important validation given its outsized influence on the regression.

**Remediation:** Scrape the publications index with pagination to identify annual report IDs for 2015–2022, or use the sequential ID search strategy documented in `CANDIDATE_OLDER` in the script.

---

## ISSUE-006: Python 3.9 Compatibility — Type Annotations

**Severity:** Minor (resolved)  
**Script:** `Scripts/04_scrape_stat_gov_kz.py`  
**Status:** Resolved — union type syntax `str | None` replaced with untyped signatures

**Description:** Python 3.10+ union type syntax (`str | None`) was used initially and caused a TypeError on the Python 3.9 system.

**Remediation:** Replaced with untyped function signatures. No functional impact.

---

*Last updated: 2026-05-04*

