# Hypothesis Model

## Core Logic

The project begins from the observation that Kazakhstan-China trade expanded after the launch of the Belt and Road Initiative. The analytical issue is whether this expansion improved Kazakhstan's bilateral trade balance or primarily increased trade volume without changing the underlying asymmetry of exchange.

The central mechanism is strategic mineral exports. Kazakhstan's mineral exports to China may improve the trade balance because they generate export revenue in sectors where Kazakhstan has resource endowments and global market relevance. However, if Kazakhstan continues to import a larger or faster-growing value of manufactured goods from China, mineral exports may not be sufficient to improve the overall bilateral balance.

## Theoretical Logic

Dependency Theory and asymmetrical interdependence suggest that trade relations between a resource-exporting economy and a larger manufacturing economy can reproduce uneven benefits. In this framework, Kazakhstan may become more connected to China while remaining dependent on commodity exports and vulnerable to price cycles, demand shifts, and limited domestic value addition.

Trade facilitation theory offers a different but complementary expectation. BRI may reduce transaction costs, improve logistics, and expand trade opportunities. If Kazakhstan can use improved connectivity to export strategic minerals more effectively, BRI could strengthen Kazakhstan's trade position. The project therefore treats BRI as a context that may either reinforce asymmetry or improve export capacity.

## Hypotheses

### H1: Post-BRI Trade Balance Hypothesis

The post-BRI period is associated with a change in Kazakhstan's bilateral trade balance with China.

This hypothesis does not assume the direction of the change in advance. The empirical question is whether the trade balance became more favorable, less favorable, or remained broadly unchanged after BRI.

### H2: Strategic Mineral Export Hypothesis

Higher strategic mineral exports from Kazakhstan to China are associated with a more favorable Kazakhstan-China bilateral trade balance.

This hypothesis follows from the expectation that mineral export revenue can improve Kazakhstan's trade position, especially when strategic minerals represent a significant share of exports.

### H3: Post-BRI Interaction Hypothesis

The association between strategic mineral exports and Kazakhstan's bilateral trade balance changed after BRI.

This hypothesis tests whether the post-BRI period altered the importance of mineral exports for Kazakhstan's trade position. A positive interaction would suggest that strategic mineral exports became more strongly associated with trade balance improvement after BRI. A weak or negative interaction would suggest that BRI-related trade growth did not strengthen the role of minerals in improving the balance.

## Variable Logic

The planned dependent variable is Kazakhstan's bilateral trade balance with China:

```text
trade_balance_usd = exports_kazakhstan_to_china_usd - imports_kazakhstan_from_china_usd
```

A secondary dependent variable may be a normalized trade balance measure:

```text
trade_balance_ratio = trade_balance_usd / total_bilateral_trade_usd
```

The main explanatory variables are:

```text
post_bri
strategic_mineral_exports_usd
strategic_mineral_export_share
post_bri * strategic_mineral_exports_usd
```

Possible controls, subject to data availability and sample size, include Kazakhstan's GDP, exchange rate indicators, or a commodity price proxy. These controls will be used only if they improve interpretation without making the model overfitted.

## Model Logic

The baseline model is:

```text
trade_balance = beta0
              + beta1 post_bri
              + beta2 strategic_mineral_exports
              + beta3 post_bri * strategic_mineral_exports
              + limited controls
              + error
```

The coefficient on `post_bri` is interpreted as the average association between the post-BRI period and the trade balance when strategic mineral exports are at the reference value used in the model. The coefficient on `strategic_mineral_exports` is interpreted as the association between mineral exports and the trade balance before BRI or at the baseline period. The interaction term is the central test of whether this association changed after BRI.

## Interpretation Boundaries

This model should be interpreted cautiously. Annual data will produce a small number of observations, and BRI is not randomly assigned. The project can identify patterns and associations, but it cannot claim definitive causal effects without a stronger identification strategy. The final paper will avoid treating regression coefficients as proof of causality.
