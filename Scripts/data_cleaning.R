# Data Cleaning Script
# Project: BRI's Impact on Kazakhstan-China Trade Balance
#
# This script is a skeleton for future data cleaning. It does not create
# empirical results. Raw data files must be collected and verified before
# this script can be run end to end.

required_packages <- c("readr", "dplyr", "stringr")

missing_packages <- required_packages[
  !required_packages %in% rownames(installed.packages())
]

if (length(missing_packages) > 0) {
  stop(
    "Install required packages before running this script: ",
    paste(missing_packages, collapse = ", ")
  )
}

library(readr)
library(dplyr)
library(stringr)

# -------------------------------------------------------------------------
# File paths
# -------------------------------------------------------------------------

raw_trade_path <- "Collected_Raw_Data/raw/imf_dots_kazakhstan_china.csv"
raw_wdi_path <- "Collected_Raw_Data/raw/world_bank_wdi_kazakhstan.csv"
raw_comtrade_path <- "Collected_Raw_Data/raw/un_comtrade_strategic_minerals.csv"

clean_output_path <- "Collected_Raw_Data/clean/kazakhstan_china_trade_panel.csv"

# -------------------------------------------------------------------------
# Safety checks
# -------------------------------------------------------------------------

required_files <- c(raw_trade_path, raw_wdi_path, raw_comtrade_path)
missing_files <- required_files[!file.exists(required_files)]

if (length(missing_files) > 0) {
  stop(
    "Raw data files are not available yet. Missing files: ",
    paste(missing_files, collapse = ", ")
  )
}

# -------------------------------------------------------------------------
# Load raw data
# -------------------------------------------------------------------------

trade_raw <- read_csv(raw_trade_path, show_col_types = FALSE)
wdi_raw <- read_csv(raw_wdi_path, show_col_types = FALSE)
comtrade_raw <- read_csv(raw_comtrade_path, show_col_types = FALSE)

# -------------------------------------------------------------------------
# Placeholder cleaning logic
# -------------------------------------------------------------------------

# Expected trade columns after manual source export:
# year, exports_kazakhstan_to_china_usd, imports_kazakhstan_from_china_usd

trade_clean <- trade_raw %>%
  mutate(
    year = as.integer(year),
    exports_kazakhstan_to_china_usd =
      as.numeric(exports_kazakhstan_to_china_usd),
    imports_kazakhstan_from_china_usd =
      as.numeric(imports_kazakhstan_from_china_usd),
    total_bilateral_trade_usd =
      exports_kazakhstan_to_china_usd + imports_kazakhstan_from_china_usd,
    trade_balance_usd =
      exports_kazakhstan_to_china_usd - imports_kazakhstan_from_china_usd,
    trade_balance_ratio =
      trade_balance_usd / total_bilateral_trade_usd,
    post_bri = if_else(year > 2013L, 1L, 0L)
  )

# Expected WDI columns:
# year, gdp_kazakhstan_current_usd, exchange_rate_optional

wdi_clean <- wdi_raw %>%
  mutate(
    year = as.integer(year),
    gdp_kazakhstan_current_usd = as.numeric(gdp_kazakhstan_current_usd)
  )

# Expected Comtrade columns:
# year, strategic_mineral_exports_usd

minerals_clean <- comtrade_raw %>%
  mutate(
    year = as.integer(year),
    strategic_mineral_exports_usd =
      as.numeric(strategic_mineral_exports_usd)
  )

# -------------------------------------------------------------------------
# Merge annual dataset
# -------------------------------------------------------------------------

analysis_data <- trade_clean %>%
  left_join(wdi_clean, by = "year") %>%
  left_join(minerals_clean, by = "year") %>%
  mutate(
    strategic_mineral_export_share =
      strategic_mineral_exports_usd / exports_kazakhstan_to_china_usd,
    post_bri_x_strategic_mineral_exports =
      post_bri * strategic_mineral_exports_usd,
    post_bri_x_strategic_mineral_share =
      post_bri * strategic_mineral_export_share
  )

# -------------------------------------------------------------------------
# Export cleaned dataset
# -------------------------------------------------------------------------

if (!dir.exists(dirname(clean_output_path))) {
  dir.create(dirname(clean_output_path), recursive = TRUE)
}

write_csv(analysis_data, clean_output_path)

message("Cleaned dataset written to: ", clean_output_path)
