"""Generate preliminary descriptive analysis from public data APIs.

This script uses World Bank WITS trade data and World Bank WDI GDP data to
produce a cautious preliminary analysis for the repository. It does not use
fabricated data and does not estimate final regression results.

UN Comtrade HS-level extraction for uranium and copper remains a separate
future step because the current UN Comtrade API requires a subscription key.
For this preliminary analysis, WITS "Ores and Metals" exports are used only
as a proxy for mineral export exposure, not as a final strategic mineral
measure.
"""

from __future__ import annotations

import csv
import json
import math
import statistics
import urllib.request
from datetime import date
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "Collected_Raw_Data" / "raw"
CLEAN_DIR = ROOT / "Collected_Raw_Data" / "clean"
TABLE_DIR = ROOT / "Outputs" / "generated_tables"
FIGURE_DIR = ROOT / "Outputs" / "generated_figures"
ANALYSIS_PATH = ROOT / "Analysis" / "data_analysis.md"

WITS_TOTAL_URL = (
    "https://wits.worldbank.org/API/V1/SDMX/V21/datasource/"
    "tradestats-trade/reporter/kaz/year/all/partner/chn/product/Total/"
    "indicator/XPRT-TRD-VL;MPRT-TRD-VL?format=JSON"
)

WITS_ORES_METALS_URL = (
    "https://wits.worldbank.org/API/V1/SDMX/V21/datasource/"
    "tradestats-trade/reporter/kaz/year/all/partner/chn/product/OresMtls/"
    "indicator/XPRT-TRD-VL?format=JSON"
)

WDI_GDP_URL = (
    "https://api.worldbank.org/v2/country/KAZ/indicator/NY.GDP.MKTP.CD"
    "?format=json&date=2000:2023&per_page=100"
)


def fetch_json(url: str) -> dict | list:
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.loads(response.read().decode("utf-8"))


def parse_wits(data: dict) -> list[dict]:
    """Parse WITS SDMX-JSON into tidy records."""
    dimensions = data["structure"]["dimensions"]
    series_dimensions = dimensions["series"]
    observation_values = dimensions["observation"][0]["values"]

    product_values = series_dimensions[3]["values"]
    indicator_values = series_dimensions[4]["values"]

    records = []
    for key, series in data["dataSets"][0]["series"].items():
        indexes = [int(part) for part in key.split(":")]
        product = product_values[indexes[3]]["id"]
        product_name = product_values[indexes[3]]["name"]
        indicator = indicator_values[indexes[4]]["id"]
        indicator_name = indicator_values[indexes[4]]["name"]

        for obs_index, observation in series["observations"].items():
            year = int(observation_values[int(obs_index)]["id"])
            value = float(observation[0])
            records.append(
                {
                    "year": year,
                    "product": product,
                    "product_name": product_name,
                    "indicator": indicator,
                    "indicator_name": indicator_name,
                    "value_usd_thousand": value,
                }
            )
    return records


def parse_wdi_gdp(data: list) -> dict[int, float]:
    if not isinstance(data, list) or len(data) < 2:
        raise ValueError("Unexpected WDI response format")

    gdp_by_year = {}
    for item in data[1]:
        if item.get("value") is not None:
            gdp_by_year[int(item["date"])] = float(item["value"])
    return gdp_by_year


def write_csv(path: Path, rows: Iterable[dict], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def fmt_million(value: float) -> str:
    return f"{value / 1_000_000:,.1f}"


def fmt_billion(value: float) -> str:
    return f"{value / 1_000_000_000:,.2f}"


def fmt_pct(value: float) -> str:
    return f"{value * 100:,.1f}"


def safe_mean(values: list[float]) -> float:
    return statistics.mean(values) if values else math.nan


def build_panel(total_records: list[dict], ores_records: list[dict], gdp: dict[int, float]) -> list[dict]:
    totals: dict[int, dict] = {}

    for row in total_records:
        year = row["year"]
        if year < 2000 or year > 2023:
            continue
        totals.setdefault(year, {})
        if row["indicator"] == "XPRT-TRD-VL":
            totals[year]["exports_kazakhstan_to_china_usd"] = row["value_usd_thousand"] * 1000
        elif row["indicator"] == "MPRT-TRD-VL":
            totals[year]["imports_kazakhstan_from_china_usd"] = row["value_usd_thousand"] * 1000

    ores_by_year = {
        row["year"]: row["value_usd_thousand"] * 1000
        for row in ores_records
        if row["indicator"] == "XPRT-TRD-VL" and 2000 <= row["year"] <= 2023
    }

    panel = []
    for year in sorted(totals):
        values = totals[year]
        exports = values.get("exports_kazakhstan_to_china_usd")
        imports = values.get("imports_kazakhstan_from_china_usd")
        ores = ores_by_year.get(year)

        if exports is None or imports is None or ores is None:
            continue

        total_trade = exports + imports
        trade_balance = exports - imports
        post_bri = 1 if year > 2013 else 0

        panel.append(
            {
                "year": year,
                "exports_kazakhstan_to_china_usd": round(exports, 2),
                "imports_kazakhstan_from_china_usd": round(imports, 2),
                "total_bilateral_trade_usd": round(total_trade, 2),
                "trade_balance_usd": round(trade_balance, 2),
                "trade_balance_ratio": round(trade_balance / total_trade, 6),
                "ores_metals_exports_usd": round(ores, 2),
                "ores_metals_export_share": round(ores / exports, 6),
                "post_bri": post_bri,
                "gdp_kazakhstan_current_usd": round(gdp.get(year, math.nan), 2),
            }
        )

    return panel


def period_summary(panel: list[dict]) -> list[dict]:
    rows = []
    periods = [
        ("Pre/transition BRI", [row for row in panel if row["year"] <= 2013]),
        ("Post-BRI", [row for row in panel if row["year"] > 2013]),
    ]

    for label, subset in periods:
        exports = [row["exports_kazakhstan_to_china_usd"] for row in subset]
        imports = [row["imports_kazakhstan_from_china_usd"] for row in subset]
        balances = [row["trade_balance_usd"] for row in subset]
        ores = [row["ores_metals_exports_usd"] for row in subset]
        shares = [row["ores_metals_export_share"] for row in subset]

        rows.append(
            {
                "period": label,
                "years": f"{min(row['year'] for row in subset)}-{max(row['year'] for row in subset)}",
                "observations": len(subset),
                "mean_exports_usd_million": round(safe_mean(exports) / 1_000_000, 2),
                "mean_imports_usd_million": round(safe_mean(imports) / 1_000_000, 2),
                "mean_trade_balance_usd_million": round(safe_mean(balances) / 1_000_000, 2),
                "mean_ores_metals_exports_usd_million": round(safe_mean(ores) / 1_000_000, 2),
                "mean_ores_metals_export_share_pct": round(safe_mean(shares) * 100, 2),
            }
        )
    return rows


def summary_statistics(panel: list[dict]) -> list[dict]:
    variables = [
        ("exports_kazakhstan_to_china_usd", "Exports to China"),
        ("imports_kazakhstan_from_china_usd", "Imports from China"),
        ("trade_balance_usd", "Trade balance"),
        ("ores_metals_exports_usd", "Ores and metals exports"),
        ("ores_metals_export_share", "Ores and metals export share"),
    ]

    rows = []
    for column, label in variables:
        values = [row[column] for row in panel if not math.isnan(row[column])]
        scale = 100 if column.endswith("_share") else 1_000_000
        unit = "percent" if column.endswith("_share") else "USD million"
        rows.append(
            {
                "variable": label,
                "unit": unit,
                "observations": len(values),
                "mean": round(statistics.mean(values) * (100 if unit == "percent" else 1 / 1_000_000), 2),
                "median": round(statistics.median(values) * (100 if unit == "percent" else 1 / 1_000_000), 2),
                "minimum": round(min(values) * (100 if unit == "percent" else 1 / 1_000_000), 2),
                "maximum": round(max(values) * (100 if unit == "percent" else 1 / 1_000_000), 2),
            }
        )
    return rows


def scale_points(values: list[float], left: int, width: int, top: int, height: int) -> tuple[list[float], float, float]:
    minimum = min(values)
    maximum = max(values)
    if minimum == maximum:
        minimum -= 1
        maximum += 1
    padding = (maximum - minimum) * 0.08
    minimum -= padding
    maximum += padding
    scale = [top + height - ((value - minimum) / (maximum - minimum)) * height for value in values]
    return scale, minimum, maximum


def write_line_chart(path: Path, title: str, y_label: str, series: list[tuple[str, str, list[tuple[int, float]]]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

    width = 920
    height = 520
    left = 86
    right = 32
    top = 62
    bottom = 72
    plot_width = width - left - right
    plot_height = height - top - bottom

    years = sorted({year for _, _, points in series for year, _ in points})
    all_values = [value for _, _, points in series for _, value in points]
    y_scaled, y_min, y_max = scale_points(all_values, left, plot_width, top, plot_height)

    def x_for(year: int) -> float:
        return left + ((year - min(years)) / (max(years) - min(years))) * plot_width

    def y_for(value: float) -> float:
        return top + plot_height - ((value - y_min) / (y_max - y_min)) * plot_height

    elements = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        f'<text x="{left}" y="34" font-family="Arial" font-size="20" font-weight="700" fill="#111827">{title}</text>',
        f'<text x="{left}" y="54" font-family="Arial" font-size="12" fill="#4b5563">{y_label}</text>',
        f'<line x1="{left}" y1="{top + plot_height}" x2="{left + plot_width}" y2="{top + plot_height}" stroke="#111827" stroke-width="1"/>',
        f'<line x1="{left}" y1="{top}" x2="{left}" y2="{top + plot_height}" stroke="#111827" stroke-width="1"/>',
    ]

    for i in range(5):
        value = y_min + (y_max - y_min) * i / 4
        y = y_for(value)
        elements.append(f'<line x1="{left}" y1="{y:.2f}" x2="{left + plot_width}" y2="{y:.2f}" stroke="#e5e7eb" stroke-width="1"/>')
        elements.append(f'<text x="{left - 10}" y="{y + 4:.2f}" text-anchor="end" font-family="Arial" font-size="11" fill="#4b5563">{value:.1f}</text>')

    for year in [2000, 2005, 2010, 2013, 2015, 2020, 2023]:
        x = x_for(year)
        elements.append(f'<line x1="{x:.2f}" y1="{top + plot_height}" x2="{x:.2f}" y2="{top + plot_height + 5}" stroke="#111827" stroke-width="1"/>')
        elements.append(f'<text x="{x:.2f}" y="{top + plot_height + 22}" text-anchor="middle" font-family="Arial" font-size="11" fill="#4b5563">{year}</text>')

    bri_x = x_for(2013)
    elements.append(f'<line x1="{bri_x:.2f}" y1="{top}" x2="{bri_x:.2f}" y2="{top + plot_height}" stroke="#6b7280" stroke-width="1.2" stroke-dasharray="5 5"/>')
    elements.append(f'<text x="{bri_x + 6:.2f}" y="{top + 16}" font-family="Arial" font-size="11" fill="#374151">BRI announced</text>')

    legend_x = left + 8
    legend_y = height - 28
    for index, (label, color, points) in enumerate(series):
        y = legend_y - index * 20
        elements.append(f'<line x1="{legend_x}" y1="{y}" x2="{legend_x + 22}" y2="{y}" stroke="{color}" stroke-width="3"/>')
        elements.append(f'<text x="{legend_x + 30}" y="{y + 4}" font-family="Arial" font-size="12" fill="#111827">{label}</text>')
        polyline = " ".join(f"{x_for(year):.2f},{y_for(value):.2f}" for year, value in points)
        elements.append(f'<polyline points="{polyline}" fill="none" stroke="{color}" stroke-width="2.4"/>')
        for year, value in points:
            elements.append(f'<circle cx="{x_for(year):.2f}" cy="{y_for(value):.2f}" r="2.5" fill="{color}"/>')

    elements.append('<text x="86" y="505" font-family="Arial" font-size="11" fill="#6b7280">Source: World Bank WITS API. Values are preliminary and should be verified before final submission.</text>')
    elements.append("</svg>")
    path.write_text("\n".join(elements), encoding="utf-8")


def markdown_table(rows: list[dict], columns: list[str]) -> str:
    header = "| " + " | ".join(columns) + " |"
    separator = "| " + " | ".join(["---"] * len(columns)) + " |"
    body = []
    for row in rows:
        body.append("| " + " | ".join(str(row[column]) for column in columns) + " |")
    return "\n".join([header, separator, *body])


def write_analysis_markdown(panel: list[dict], period_rows: list[dict], stat_rows: list[dict]) -> None:
    latest = panel[-1]
    first = panel[0]
    balances = [row["trade_balance_usd"] for row in panel]
    positive_balance_years = sum(1 for value in balances if value > 0)
    negative_balance_years = len(balances) - positive_balance_years
    negative_year_label = "year" if negative_balance_years == 1 else "years"

    period_columns = [
        "period",
        "years",
        "observations",
        "mean_exports_usd_million",
        "mean_imports_usd_million",
        "mean_trade_balance_usd_million",
        "mean_ores_metals_exports_usd_million",
        "mean_ores_metals_export_share_pct",
    ]
    stat_columns = ["variable", "unit", "observations", "mean", "median", "minimum", "maximum"]

    content = f"""# Preliminary Data Analysis

## Status and Scope

This file provides a preliminary descriptive analysis using public World Bank WITS and World Bank WDI API data collected on {date.today().isoformat()}. It is included so the repository contains actual data analysis, summary statistics, and figures rather than only placeholders.

The analysis is still preliminary. WITS `Ores and Metals` exports are used as a cautious proxy for mineral export exposure. They are not a final HS-level measure of uranium, copper, or other strategic minerals. A final strategic-mineral dataset should still be constructed from UN Comtrade after a subscription key is available and the commodity codes are documented.

## Data Sources

- World Bank WITS API: Kazakhstan as reporter, China as partner, all products, export and import trade value.
- World Bank WITS API: Kazakhstan as reporter, China as partner, `Ores and Metals`, export trade value.
- World Bank WDI API: Kazakhstan GDP in current US dollars.

Values from WITS are reported in US dollars thousand and are converted to current US dollars in the cleaned dataset.

## Descriptive Statistics

The cleaned panel covers {first['year']}-{latest['year']} and contains {len(panel)} annual observations. Kazakhstan recorded a positive bilateral trade balance with China in {positive_balance_years} years and a negative balance in {negative_balance_years} {negative_year_label}.

In {latest['year']}, Kazakhstan's exports to China were approximately USD {fmt_billion(latest['exports_kazakhstan_to_china_usd'])} billion, imports from China were approximately USD {fmt_billion(latest['imports_kazakhstan_from_china_usd'])} billion, and the bilateral trade balance was approximately USD {fmt_billion(latest['trade_balance_usd'])} billion. Ores and metals exports were approximately USD {fmt_billion(latest['ores_metals_exports_usd'])} billion, equal to about {fmt_pct(latest['ores_metals_export_share'])} percent of Kazakhstan's exports to China.

### Pre-BRI and Post-BRI Comparison

{markdown_table(period_rows, period_columns)}

### Summary Statistics

{markdown_table(stat_rows, stat_columns)}

## Generated Figures

- `Outputs/generated_figures/exports_imports_over_time.svg`
- `Outputs/generated_figures/trade_balance_over_time.svg`
- `Outputs/generated_figures/ores_metals_share_over_time.svg`

## Preliminary Interpretation

The descriptive evidence supports the idea that Kazakhstan-China trade expanded substantially over the sample period. However, the trade balance does not move in a simple linear way. This supports the project's central argument that trade growth should not be treated as equivalent to trade-balance improvement.

The ores and metals proxy is analytically useful because it shows that mineral-related exports form a large part of Kazakhstan's exports to China in many years. At the same time, this proxy is broader than the final strategic-mineral concept. The final paper should therefore describe these figures as preliminary descriptive evidence and avoid claiming that they measure uranium or copper exports directly.

## Remaining Work

1. Obtain UN Comtrade API access or manually download verified HS-level commodity data.
2. Define the exact strategic mineral basket before regression modeling.
3. Re-run descriptive tables and figures using the final strategic mineral measure.
4. Estimate the regression model only after the final data construction is documented.
"""
    ANALYSIS_PATH.write_text(content, encoding="utf-8")


def main() -> None:
    for directory in [RAW_DIR, CLEAN_DIR, TABLE_DIR, FIGURE_DIR]:
        directory.mkdir(parents=True, exist_ok=True)

    total_json = fetch_json(WITS_TOTAL_URL)
    ores_json = fetch_json(WITS_ORES_METALS_URL)
    gdp_json = fetch_json(WDI_GDP_URL)

    total_records = parse_wits(total_json)
    ores_records = parse_wits(ores_json)
    gdp_by_year = parse_wdi_gdp(gdp_json)
    panel = build_panel(total_records, ores_records, gdp_by_year)

    write_csv(
        RAW_DIR / "wits_total_trade_kazakhstan_china.csv",
        total_records,
        ["year", "product", "product_name", "indicator", "indicator_name", "value_usd_thousand"],
    )
    write_csv(
        RAW_DIR / "wits_ores_metals_exports_kazakhstan_china.csv",
        ores_records,
        ["year", "product", "product_name", "indicator", "indicator_name", "value_usd_thousand"],
    )
    write_csv(
        RAW_DIR / "world_bank_wdi_kazakhstan_gdp.csv",
        [{"year": year, "gdp_kazakhstan_current_usd": value} for year, value in sorted(gdp_by_year.items())],
        ["year", "gdp_kazakhstan_current_usd"],
    )

    panel_columns = [
        "year",
        "exports_kazakhstan_to_china_usd",
        "imports_kazakhstan_from_china_usd",
        "total_bilateral_trade_usd",
        "trade_balance_usd",
        "trade_balance_ratio",
        "ores_metals_exports_usd",
        "ores_metals_export_share",
        "post_bri",
        "gdp_kazakhstan_current_usd",
    ]
    write_csv(CLEAN_DIR / "kazakhstan_china_trade_panel.csv", panel, panel_columns)

    period_rows = period_summary(panel)
    stat_rows = summary_statistics(panel)
    write_csv(TABLE_DIR / "pre_post_bri_summary.csv", period_rows, list(period_rows[0].keys()))
    write_csv(TABLE_DIR / "summary_statistics.csv", stat_rows, list(stat_rows[0].keys()))

    annual_rows = [
        {
            "year": row["year"],
            "exports_usd_million": round(row["exports_kazakhstan_to_china_usd"] / 1_000_000, 2),
            "imports_usd_million": round(row["imports_kazakhstan_from_china_usd"] / 1_000_000, 2),
            "trade_balance_usd_million": round(row["trade_balance_usd"] / 1_000_000, 2),
            "ores_metals_exports_usd_million": round(row["ores_metals_exports_usd"] / 1_000_000, 2),
            "ores_metals_export_share_pct": round(row["ores_metals_export_share"] * 100, 2),
        }
        for row in panel
    ]
    write_csv(TABLE_DIR / "annual_trade_balance.csv", annual_rows, list(annual_rows[0].keys()))

    write_line_chart(
        FIGURE_DIR / "exports_imports_over_time.svg",
        "Kazakhstan-China Bilateral Trade Flows",
        "Current USD, billions",
        [
            (
                "Exports to China",
                "#0f766e",
                [(row["year"], row["exports_kazakhstan_to_china_usd"] / 1_000_000_000) for row in panel],
            ),
            (
                "Imports from China",
                "#b45309",
                [(row["year"], row["imports_kazakhstan_from_china_usd"] / 1_000_000_000) for row in panel],
            ),
        ],
    )

    write_line_chart(
        FIGURE_DIR / "trade_balance_over_time.svg",
        "Kazakhstan's Bilateral Trade Balance with China",
        "Current USD, billions",
        [
            (
                "Trade balance",
                "#1d4ed8",
                [(row["year"], row["trade_balance_usd"] / 1_000_000_000) for row in panel],
            )
        ],
    )

    write_line_chart(
        FIGURE_DIR / "ores_metals_share_over_time.svg",
        "Ores and Metals Share of Kazakhstan's Exports to China",
        "Percent of exports to China",
        [
            (
                "Ores and metals share",
                "#7c3aed",
                [(row["year"], row["ores_metals_export_share"] * 100) for row in panel],
            )
        ],
    )

    write_analysis_markdown(panel, period_rows, stat_rows)
    print(f"Generated preliminary analysis for {panel[0]['year']}-{panel[-1]['year']}.")


if __name__ == "__main__":
    main()
