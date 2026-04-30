# Known Issues and Data Limitations

## ISSUE-001: Comtrade files are 2014-only HS-2 snapshots

**Status:** Active — affects Scripts/01_load_comtrade.py

The Comtrade files provided (`comtrade_kaz_reporter.csv`, `comtrade_chn_reporter.csv`) contain data for 2014 only, at HS chapter (HS-2) level rather than the HS-6 level required by the Codebook. They cannot support the construction of `minerals_narrow`, `minerals_broad`, or `oil_exports` as annual time series for 2000–2024.

**Workaround:** The `minerals_proxy` variable (WITS Ores & Metals exports, available 2000–2023) is used as the primary observable in all regression tables. The Comtrade 2014 snapshot is used only for a cross-sectional composition note in the mirror-reconciliation memo.

**Required to fix:** Re-download Comtrade API pulls for years 2000–2024 at HS-6, or access UN Comtrade+ with bilateral filtering, reporter=KAZ, partner=CHN, classification=HS.

---

## ISSUE-002: Brent daily series covers only 2021–2025 (FRED DCOILBRENTEU.csv)

**Status:** Active — affects Scripts/01b_load_prices.py

The FRED DCOILBRENTEU file covers only 13 April 2021 to present. Annual mean Brent for 2000–2020 is sourced from the World Bank Pink Sheet (sheet "Monthly Prices", column "Crude oil, Brent", monthly 1960–2026).

**Workaround:** Pink Sheet used as primary Brent source for 2000–2023; FRED file used for validation.

---

## ISSUE-003: R not installed; scripts rewritten in Python

**Status:** Active

The task specification calls for R scripts (`.R` extension, ARDL::auto_ardl, strucchange, tidysynth, plm packages). R is not installed on the analysis machine. All scripts are implemented in Python 3.9 using statsmodels (ARDL), ruptures (structural breaks), and linearmodels (panel models). Python script names carry `.py` extension.

**Required to fix:** Install R ≥ 4.3, then: install.packages(c("ARDL","strucchange","tidysynth","plm","sandwich","tseries","urca"))

---

## ISSUE-004: AidData file is Excel (xlsx) mislabeled as .csv

**Status:** Resolved — sheet GCDF_3.0 readable via openpyxl.

AidData GCDF v3.0 was provided with a `.csv` extension but is an Excel 2007+ workbook. Scripts read it via `pandas.read_excel(..., engine='openpyxl')`.

---

## ISSUE-005: Synthetic control donor pool unavailable from local files

**Status:** Active — affects Scripts/13_synthetic_control.py

Donor-pool countries (Uzbekistan, Turkmenistan, Mongolia, Azerbaijan, Kyrgyzstan, Georgia, Armenia) require their bilateral trade-balance-with-China series. These are not available in the local raw files. Within-country placebo DiD (Script 14) is therefore the primary identification strategy; the synthetic control script contains a shell with DECISION NEEDED notes.

---

## ISSUE-006: Year 2024 missing from all trade series

**Status:** Active — affects Scripts/03_build_panel.py

WITS bilateral trade data ends at 2023. Brent and Pink Sheet prices are available through early 2026. The panel is 24 rows (2000–2023); the target was 25 rows (2000–2024). The 2024 row is present in the panel with NA values for trade variables.

---

## ISSUE-007: Uranium proxy absent from Pink Sheet

**Status:** Active — noted in descriptive scripts.

The World Bank Pink Sheet does not include uranium spot prices. No uranium price proxy is available from local files. The variable is excluded from price controls; a note is placed in the paper's data section.
