# Research Plan

## Title

Strategic Minerals, Asymmetric Interdependence, and Kazakhstan-China Trade under the Belt and Road Initiative

## Research Question

Did the post-BRI period change Kazakhstan's bilateral trade balance with China, and did it change the trade-balance payoff associated with strategic mineral exports?

## Theoretical Frame

The lead theory is asymmetric interdependence. Kazakhstan and China can both gain from connectivity, but the distribution of adjustment costs and outside options may be unequal. This is a better primary lens than dependency theory because it allows for agency, mutual gains, and sector-specific leverage while still treating trade concentration as politically and economically consequential.

The supporting pillars are:

1. Gravity and trade facilitation: BRI may reduce trade costs and expand flows, but effects depend on geography, border frictions, and complementary reforms.
2. Resource dependence and terms of trade: mineral exports can improve the balance, but commodity prices and volatility can weaken the payoff.
3. Global value chains: the key development question is whether mineral trade supports upgrading or reinforces raw-material exchange.
4. Dependency theory as context: useful for intellectual history and unequal-exchange concerns, but not the lead explanatory model.

## Data

The annual panel covers 2000-2024, with usable trade-balance observations through 2023. Phase 1 scripts construct `Collected_Raw_Data/clean_panel_annual.csv` from local downloads and public sources. The core variables are:

- `trade_balance_usd` and `trade_balance_ratio`
- `minerals_narrow`, `minerals_broad`, and WITS legacy ores/metals proxy
- Brent and copper annual prices
- Kazakhstan and China GDP, KZT/USD, CPI
- AidData Chinese finance intensity (`bri_intensity`)
- post-BRI threshold variables and interactions

Data limitations are active parts of the design. The local Comtrade extracts are HS-2/aggregate snapshots for 2014-2024 rather than full HS-6 data for 2000-2024. Oil exports are missing in the clean panel. Donor-country and partner-placebo bilateral panels are not available locally, so synthetic control and within-country DiD are documented as infeasible rather than estimated.

## Empirical Strategy

The empirical design is convergent and associational:

1. Descriptives and stationarity: pre/post summary statistics, time plots, ADF, Phillips-Perron, and KPSS tests.
2. Structural breaks: Chow tests at 2013-2016 and Bai-Perron-style multiple-break detection with bootstrap confidence intervals.
3. ARDL: AIC-selected ARDL models for trade balance on minerals, Brent, exchange rate, GDP controls, post-BRI timing, and post-BRI x minerals. The dummy and finance-intensity specifications are both reported.
4. Identification checks: synthetic control and partner-placebo DiD are attempted as feasibility scripts. Both are skipped because required donor/placebo panels are absent from local files.
5. Robustness: a full grid over start years, minerals definitions, outcomes, sample exclusions, and estimators reports all failures and sign reversals.

## Interpretation Rules

The paper will avoid causal language unless a design supports it. Because synthetic control and DiD cannot be estimated with current local data, the main evidence is time-series association plus structural-break diagnostics. Negative or fragile robustness results are reported prominently.

## Expected Contribution

The contribution is a transparent, reproducible assessment of Kazakhstan-China trade structure under BRI. It shifts the question from "did trade grow?" to "did Kazakhstan's bilateral external position improve, and did strategic minerals become more or less beneficial after BRI?"
