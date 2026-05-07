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

**Severity:** ~~Affects causal identification completeness~~ **RESOLVED**  
**Script:** `Scripts/33_multi_partner_panel.py`, `Scripts/34_did_partner_placebo.py`  
**Status:** [RESOLVED] — full TWFE DiD implemented using UN Comtrade public API

**Description:** IMF DOTS API remained unreachable. Partner data sourced instead from the UN Comtrade public preview API (`comtradeapi.un.org/public/v1/preview/C/A/HS`), which requires no subscription and returned complete 2000–2023 annual bilateral flows for KAZ vs CHN, RUS, DEU, UZB, TUR, USA.

**Validation:** China data cross-validated against the existing local panel — 0% discrepancy across all 24 years.

**Result:** TWFE DiD (§6.15) fully estimated. DiD coefficient = −0.305 (*p* = 0.0002), China-specific post-2013 balance deterioration confirmed. `Collected_Raw_Data/kz_multi_partner_panel.csv` updated with 144 rows (6 partners × 24 years). `data_source` field records `comtrade_public_api`.

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

**Severity:** ~~Affects causal identification strength~~ **PARTIALLY RESOLVED**  
**Script:** `Scripts/36_synthetic_control.py`  
**Status:** [PARTIAL] — partner data now available; full Abadie SC not yet re-estimated

**Description:** The full Abadie (2003) synthetic control requires multiple donor units. Partner data is now available via UN Comtrade (see ISSUE-002 resolution). `Collected_Raw_Data/kz_multi_partner_panel.csv` contains balance ratios for all 6 donor partners (RUS, DEU, UZB, TUR, USA) 2000–2023. The within-unit synthetic control remains in place pending a full multi-partner SC re-run.

**Consequence:** The TWFE DiD (§6.15) now provides strong cross-partner identification (DiD = −0.305, p=0.0002). The within-unit SC (permutation p=0.857) is a complement, not the primary causal identification method.

**Remediation:** Extend `Scripts/36_synthetic_control.py` to use the multi-partner donor pool from `kz_multi_partner_panel.csv`. Set `multi_partner_available = True`. This would provide a full Abadie SC as an additional robustness check beyond the TWFE DiD.

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

