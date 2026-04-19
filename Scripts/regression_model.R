# Regression Model Script
# Project: BRI's Impact on Kazakhstan-China Trade Balance
#
# This script estimates planned models only after a verified cleaned dataset
# exists. It does not include fabricated estimates or stored results.

required_packages <- c("readr", "dplyr", "broom")

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
library(broom)

clean_data_path <- "Collected_Raw_Data/clean/kazakhstan_china_trade_panel.csv"
results_dir <- "Outputs/model_outputs"

if (!file.exists(clean_data_path)) {
  stop(
    "Cleaned dataset is not available yet. Run Scripts/data_cleaning.R ",
    "after collecting verified raw data."
  )
}

if (!dir.exists(results_dir)) {
  dir.create(results_dir, recursive = TRUE)
}

analysis_data <- read_csv(clean_data_path, show_col_types = FALSE)

required_columns <- c(
  "year",
  "trade_balance_usd",
  "trade_balance_ratio",
  "post_bri",
  "strategic_mineral_exports_usd",
  "strategic_mineral_export_share",
  "post_bri_x_strategic_mineral_exports",
  "post_bri_x_strategic_mineral_share"
)

missing_columns <- setdiff(required_columns, names(analysis_data))

if (length(missing_columns) > 0) {
  stop(
    "Cleaned dataset is missing required columns: ",
    paste(missing_columns, collapse = ", ")
  )
}

# -------------------------------------------------------------------------
# Baseline model
# -------------------------------------------------------------------------

baseline_model <- lm(
  trade_balance_usd ~
    post_bri +
    strategic_mineral_exports_usd +
    post_bri_x_strategic_mineral_exports,
  data = analysis_data
)

baseline_results <- tidy(baseline_model)
baseline_fit <- glance(baseline_model)

# -------------------------------------------------------------------------
# Alternative ratio model
# -------------------------------------------------------------------------

ratio_model <- lm(
  trade_balance_ratio ~
    post_bri +
    strategic_mineral_export_share +
    post_bri_x_strategic_mineral_share,
  data = analysis_data
)

ratio_results <- tidy(ratio_model)
ratio_fit <- glance(ratio_model)

# -------------------------------------------------------------------------
# Export model summaries
# -------------------------------------------------------------------------

write_csv(baseline_results, file.path(results_dir, "baseline_model_terms.csv"))
write_csv(baseline_fit, file.path(results_dir, "baseline_model_fit.csv"))
write_csv(ratio_results, file.path(results_dir, "ratio_model_terms.csv"))
write_csv(ratio_fit, file.path(results_dir, "ratio_model_fit.csv"))

message(
  "Model estimation completed. Interpret all estimates cautiously because ",
  "the annual sample is expected to be small."
)
