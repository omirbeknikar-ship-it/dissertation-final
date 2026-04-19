# Exploratory Analysis Script
# Project: BRI's Impact on Kazakhstan-China Trade Balance
#
# This script will generate descriptive summaries and figures after the
# cleaned dataset is available. It does not contain final results.

required_packages <- c("readr", "dplyr", "ggplot2")

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
library(ggplot2)

clean_data_path <- "Collected_Raw_Data/clean/kazakhstan_china_trade_panel.csv"
figures_dir <- "Outputs/figures"

if (!file.exists(clean_data_path)) {
  stop(
    "Cleaned dataset is not available yet. Run Scripts/data_cleaning.R ",
    "after collecting verified raw data."
  )
}

if (!dir.exists(figures_dir)) {
  dir.create(figures_dir, recursive = TRUE)
}

analysis_data <- read_csv(clean_data_path, show_col_types = FALSE)

required_columns <- c(
  "year",
  "exports_kazakhstan_to_china_usd",
  "imports_kazakhstan_from_china_usd",
  "trade_balance_usd",
  "strategic_mineral_exports_usd",
  "strategic_mineral_export_share",
  "post_bri"
)

missing_columns <- setdiff(required_columns, names(analysis_data))

if (length(missing_columns) > 0) {
  stop(
    "Cleaned dataset is missing required columns: ",
    paste(missing_columns, collapse = ", ")
  )
}

# -------------------------------------------------------------------------
# Descriptive summaries
# -------------------------------------------------------------------------

summary_by_period <- analysis_data %>%
  mutate(period = if_else(post_bri == 1L, "Post-BRI", "Pre-BRI")) %>%
  group_by(period) %>%
  summarise(
    years = n(),
    mean_exports = mean(exports_kazakhstan_to_china_usd, na.rm = TRUE),
    mean_imports = mean(imports_kazakhstan_from_china_usd, na.rm = TRUE),
    mean_trade_balance = mean(trade_balance_usd, na.rm = TRUE),
    mean_mineral_exports =
      mean(strategic_mineral_exports_usd, na.rm = TRUE),
    .groups = "drop"
  )

print(summary_by_period)

# -------------------------------------------------------------------------
# Placeholder figure generation
# -------------------------------------------------------------------------

trade_balance_plot <- ggplot(analysis_data, aes(x = year, y = trade_balance_usd)) +
  geom_hline(yintercept = 0, linewidth = 0.3) +
  geom_line(linewidth = 0.7) +
  geom_point(size = 1.8) +
  geom_vline(xintercept = 2013, linetype = "dashed") +
  labs(
    title = "Kazakhstan-China Bilateral Trade Balance",
    subtitle = "Draft figure to be regenerated after final data verification",
    x = "Year",
    y = "Trade balance, current USD",
    caption = "Source: To be completed after data collection."
  ) +
  theme_minimal()

ggsave(
  filename = file.path(figures_dir, "trade_balance_over_time.png"),
  plot = trade_balance_plot,
  width = 8,
  height = 5,
  dpi = 300
)

message("Exploratory analysis completed with verified cleaned data.")
