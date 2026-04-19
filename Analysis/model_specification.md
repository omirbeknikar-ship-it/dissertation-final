# Model Specification

## Purpose

The model is designed to test whether the post-BRI period is associated with Kazakhstan's bilateral trade balance with China and whether the role of strategic mineral exports changed after BRI. The model must remain parsimonious because the dataset will use annual observations and therefore has limited statistical power.

## Dependent Variable

The main dependent variable is:

```text
trade_balance_usd = exports_kazakhstan_to_china_usd - imports_kazakhstan_from_china_usd
```

A secondary dependent variable may be:

```text
trade_balance_ratio = trade_balance_usd / total_bilateral_trade_usd
```

The ratio may be useful because it expresses the balance relative to the size of total bilateral trade.

## Main Explanatory Variables

The central explanatory variables are:

```text
post_bri
strategic_mineral_exports_usd
post_bri_x_strategic_mineral_exports
```

The interaction term is the main test of whether the relationship between strategic mineral exports and the trade balance changed in the post-BRI period.

## Baseline Model

The baseline model is:

```text
trade_balance_usd = beta0
                  + beta1 post_bri
                  + beta2 strategic_mineral_exports_usd
                  + beta3 post_bri_x_strategic_mineral_exports
                  + error
```

An alternative specification may use the trade balance ratio:

```text
trade_balance_ratio = beta0
                    + beta1 post_bri
                    + beta2 strategic_mineral_export_share
                    + beta3 post_bri_x_strategic_mineral_share
                    + error
```

## Limited Controls

Possible controls include:

```text
gdp_kazakhstan_current_usd
exchange_rate_optional
commodity_price_proxy_optional
```

Controls will be added only if they are theoretically justified and do not overfit the model. The preferred approach is to estimate a baseline model first and then test one or two limited alternatives.

## Interpretation of Coefficients

- `beta1` indicates whether the post-BRI period is associated with a different trade balance.
- `beta2` indicates whether strategic mineral exports are associated with the trade balance in the baseline period.
- `beta3` indicates whether the association between strategic mineral exports and the trade balance changed after BRI.

## Identification Limits

The model is not a full causal identification strategy. BRI is a broad policy context, not a randomly assigned treatment. The results should be interpreted as evidence of association. Any causal language in the final paper must be limited and carefully qualified.

## Preferred Reporting Style

Regression tables should report:

1. Number of observations.
2. Variable definitions.
3. Whether 2013 is coded as pre-BRI, post-BRI, or treated separately.
4. Whether standard errors are conventional or adjusted.
5. A note explaining that the small sample limits inference.
