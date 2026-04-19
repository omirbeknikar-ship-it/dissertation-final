# Diagnostics Plan

## Purpose

The diagnostics plan is intended to prevent overinterpretation of a small annual dataset. The goal is not to make the model appear more sophisticated than the data allow. The goal is to identify whether the basic estimates are stable enough to support cautious interpretation.

## Data Diagnostics

Before modeling, the dataset should be checked for:

1. Missing years.
2. Inconsistent units or currencies.
3. Duplicate country-year observations.
4. Sudden breaks caused by source changes or HS code revisions.
5. Extreme values in strategic mineral exports or trade balance.

## Model Diagnostics

After estimating the baseline model, the following checks should be considered:

1. Residual plots to detect strong nonlinearity or outliers.
2. Influence diagnostics to identify whether one year drives the results.
3. Correlation checks among explanatory variables.
4. Sensitivity to alternative coding of 2013.
5. Sensitivity to using `trade_balance_ratio` instead of `trade_balance_usd`.

## Small-Sample Restrictions

Because the sample is annual and likely small, the project should avoid:

1. Too many control variables.
2. Highly complex time-series models.
3. Overstated statistical significance.
4. Strong causal claims based only on before-after comparison.

## Robustness Checks

Possible robustness checks include:

```text
1. Re-estimate the model excluding 2013.
2. Compare results using mineral export value and mineral export share.
3. Compare absolute trade balance and trade balance ratio.
4. Test whether conclusions depend on one outlier year.
```

These checks should be reported only after the data are available.

## Reporting Standard

The final paper should clearly separate:

```text
descriptive evidence
model-based association
theoretical interpretation
```

This separation is important because the research question is theoretically ambitious, but the available annual data may support only cautious empirical claims.
