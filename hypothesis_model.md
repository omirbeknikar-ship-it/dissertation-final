# Hypothesis Model

## Core Mechanism

BRI-linked connectivity can reduce trade costs and expand Kazakhstan-China exchange, but the balance-of-power implication depends on the structure of trade. If Kazakhstan's China-facing exports remain concentrated in minerals while imports from China grow in machinery, manufactured goods, and inputs, trade expansion may coincide with a weaker bilateral balance. If mineral exports produce sustained export revenue or downstream upgrading, the balance may improve.

## Hypotheses

### H1: Post-BRI Trade-Balance Change

The post-BRI period is associated with a change in Kazakhstan's bilateral trade balance with China.

This is tested through structural-break diagnostics and post-BRI coefficients in the ARDL specifications. The hypothesis is directional only after estimation; the theory allows improvement or deterioration.

### H2: Mineral Export Payoff

Higher strategic mineral exports are associated with a more favorable Kazakhstan-China trade balance before accounting for post-BRI interaction effects.

This is tested with `minerals_narrow`, `minerals_broad`, and WITS legacy ores/metals definitions.

### H3: Post-BRI x Minerals Interaction

The association between mineral exports and Kazakhstan's trade balance changed after BRI.

A positive interaction would suggest a stronger post-BRI trade-balance payoff from minerals. A negative interaction would suggest that mineral export growth did not translate into a stronger bilateral external position and may be consistent with asymmetric interdependence, import growth, or commodity-cycle exposure.

### H4: Finance-Intensity Alternative

Chinese development finance intensity is associated with the minerals-trade-balance relationship, but this relationship may be unstable because AidData commitments are lumpy and the annual sample is short.

## Main Estimating Equation

The preferred dummy specification is:

```text
trade_balance_B =
    beta0
  + beta1 minerals_narrow_B
  + beta2 brent_annual_mean
  + beta3 kzt_usd
  + beta4 log(kz_gdp)
  + beta5 log(cn_gdp)
  + beta6 post_bri_2013
  + beta7 post_bri_2013 * minerals_narrow_B
  + error
```

The finance-intensity alternative replaces `post_bri_2013` with `bri_intensity` and uses `bri_intensity * minerals_narrow_B`.

## Diagnostics and Robustness

The project reports:

- ADF, Phillips-Perron, and KPSS tests for integration order.
- Chow tests at 2013, 2014, 2015, and 2016.
- Bai-Perron-style multiple-break detection with bootstrap confidence intervals.
- AIC-selected ARDL lags and Pesaran-Shin-Smith bounds tests.
- Long-run ARDL multipliers with HAC standard errors.
- Robustness across start years, minerals definitions, outcomes, sample exclusions, and estimators.
- Explicit skipped status for synthetic control and DiD when donor/placebo panels are unavailable.

## Interpretation Boundary

The main ARDL results are associational time-series evidence. Because donor-pool synthetic control and partner-placebo DiD cannot be estimated from the available local files, the final paper must not claim that BRI causally changed Kazakhstan's trade balance. It can claim that the post-BRI period is associated with specific changes, subject to the documented data constraints and robustness fragility.
