# Data Cleaning Script
# Project: BRI's Impact on Kazakhstan-China Trade Balance
#
# This script is a skeleton for future data cleaning. It does not create
# empirical results. Raw data files must be collected and verified before
# this script can be run end to end.

required_packages <- c("readr", "dplyr")

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

# -------------------------------------------------------------------------
# File paths
# -------------------------------------------------------------------------

raw_trade_path <- "Collected_Raw_Data/raw/wits_total_trade_kazakhstan_china.csv"
raw_wdi_path <- "Collected_Raw_Data/raw/world_bank_wdi_kazakhstan_gdp.csv"
raw_mineral_proxy_path <-
  "Collected_Raw_Data/raw/wits_ores_metals_exports_kazakhstan_china.csv"

clean_output_path <- "Collected_Raw_Data/clean/kazakhstan_china_trade_panel.csv"

# -------------------------------------------------------------------------
# Safety checks
# -------------------------------------------------------------------------

required_files <- c(raw_trade_path, raw_wdi_path, raw_mineral_proxy_path)
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
mineral_proxy_raw <- read_csv(raw_mineral_proxy_path, show_col_types = FALSE)

# -------------------------------------------------------------------------
# Placeholder cleaning logic
# -------------------------------------------------------------------------

# Expected WITS trade columns:
# year, product, product_name, indicator, indicator_name, value_usd_thousand

exports_clean <- trade_raw %>%
  filter(indicator == "XPRT-TRD-VL") %>%
  transmute(
    year = as.integer(year),
    exports_kazakhstan_to_china_usd =
      as.numeric(value_usd_thousand) * 1000
  )

imports_clean <- trade_raw %>%
  filter(indicator == "MPRT-TRD-VL") %>%
  transmute(
    year = as.integer(year),
    imports_kazakhstan_from_china_usd =
      as.numeric(value_usd_thousand) * 1000
  )

trade_clean <- exports_clean %>%
  inner_join(imports_clean, by = "year") %>%
  mutate(
    total_bilateral_trade_usd =
      exports_kazakhstan_to_china_usd + imports_kazakhstan_from_china_usd,
    trade_balance_usd =
      exports_kazakhstan_to_china_usd - imports_kazakhstan_from_china_usd,
    trade_balance_ratio =
      trade_balance_usd / total_bilateral_trade_usd,
    post_bri = if_else(year > 2013L, 1L, 0L)
  )

# Expected WDI columns:
# year, gdp_kazakhstan_current_usd

wdi_clean <- wdi_raw %>%
  mutate(
    year = as.integer(year),
    gdp_kazakhstan_current_usd = as.numeric(gdp_kazakhstan_current_usd)
  )

# Expected WITS mineral proxy columns:
# year, product, product_name, indicator, indicator_name, value_usd_thousand

minerals_clean <- mineral_proxy_raw %>%
  filter(indicator == "XPRT-TRD-VL") %>%
  transmute(
    year = as.integer(year),
    ores_metals_exports_usd = as.numeric(value_usd_thousand) * 1000
  )

# -------------------------------------------------------------------------
# Merge annual dataset
# -------------------------------------------------------------------------

analysis_data <- trade_clean %>%
  left_join(wdi_clean, by = "year") %>%
  left_join(minerals_clean, by = "year") %>%
  mutate(
    ores_metals_export_share =
      ores_metals_exports_usd / exports_kazakhstan_to_china_usd,
    post_bri_x_ores_metals_exports =
      post_bri * ores_metals_exports_usd,
    post_bri_x_ores_metals_share =
      post_bri * ores_metals_export_share
  )

# -------------------------------------------------------------------------
# Export cleaned dataset
# -------------------------------------------------------------------------

if (!dir.exists(dirname(clean_output_path))) {
  dir.create(dirname(clean_output_path), recursive = TRUE)
}

write_csv(analysis_data, clean_output_path)

message("Cleaned dataset written to: ", clean_output_path)
