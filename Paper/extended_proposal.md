# Extended Proposal

## Introduction

The Belt and Road Initiative has made Kazakhstan an important case for studying the economic consequences of infrastructure-led connectivity. Kazakhstan is geographically central to overland routes linking China with Central Asia, Russia, and Europe. As a result, Kazakhstan-China trade has become more prominent in policy and academic discussion since BRI was announced in 2013.

However, the expansion of trade is not the same as an improvement in trade position. A country can trade more while also experiencing a worsening trade balance. This distinction is especially important for Kazakhstan because its exports to China are concentrated in resource-based products, while imports from China include machinery, manufactured goods, industrial inputs, and consumer products. The central question is therefore not only whether BRI increased trade, but whether it improved Kazakhstan's bilateral trade balance with China.

## Research Problem

The research problem is that existing discussion of BRI often emphasizes connectivity, trade expansion, and infrastructure development without sufficiently examining the distribution of trade benefits. For Kazakhstan, a narrow focus on total trade volume may obscure whether the country gained a stronger bilateral trade position or became more deeply integrated into an asymmetric trade relationship.

Strategic mineral exports make the problem more complex. Kazakhstan's mineral resources may improve its export position because they are economically and strategically valuable. Uranium and copper-related exports, for example, may contribute to export revenue and help offset imports from China. Yet reliance on strategic minerals may also reproduce dependence on commodity exports and external demand. This tension motivates the project's focus on the relationship between BRI, strategic mineral exports, and bilateral trade balance.

## Literature Review

The literature can be organized into four main strands. The first strand views BRI through trade facilitation and connectivity. It emphasizes transport corridors, logistics improvements, customs coordination, and reduced transaction costs. This perspective is valuable because it explains why trade flows may increase after BRI. Its limitation is that it often treats trade growth as evidence of economic improvement without asking whether the smaller partner's trade balance improves.

The second strand emphasizes uneven trade outcomes. From this perspective, BRI may deepen asymmetrical relationships when one economy exports raw materials and imports higher-value manufactured goods. This argument is relevant to Kazakhstan because the country is resource-rich but less diversified than China. The strength of this strand is that it focuses on structure, not just volume. Its weakness is that it can sometimes assume dependency without testing whether specific exports may improve the smaller partner's position.

The third strand concerns Kazakhstan-China trade structure. It shows that Kazakhstan's exports to China are strongly connected to natural resources, energy, metals, and minerals, while China's exports to Kazakhstan are more diversified. This literature provides the empirical basis for the project but often remains descriptive. It identifies trade composition but does not always connect that composition to a testable model of the bilateral trade balance.

The fourth strand concerns strategic minerals. Strategic minerals may give Kazakhstan export advantages because they are linked to energy systems, industrial production, and long-term supply security. At the same time, mineral exports are vulnerable to price changes, demand shifts, and limited domestic processing. This means their contribution to trade balance must be evaluated empirically rather than assumed.

The research gap is therefore precise: existing discussions often examine BRI-related trade growth, infrastructure connectivity, or broad asymmetry, but they do not sufficiently test whether BRI improved Kazakhstan's bilateral trade balance with China and whether strategic mineral exports changed that relationship.

## Theoretical Framework

The primary theoretical framework is Dependency Theory, understood here through asymmetrical interdependence. The framework suggests that trade between a resource-exporting economy and a larger manufacturing economy can reproduce unequal benefits. Kazakhstan may become more connected to China while remaining dependent on resource exports and vulnerable to commodity cycles.

The supporting framework is trade facilitation under BRI. This framework explains how infrastructure, logistics, and policy coordination may increase trade by reducing barriers and transaction costs. It is useful for explaining the growth of trade flows, but it does not determine whether Kazakhstan's trade balance improves.

The two frameworks are integrated as follows: trade facilitation explains why trade may increase after BRI, while Dependency Theory explains why increased trade may still be uneven. Strategic mineral exports are the key mechanism linking the two frameworks because they are resource exports that may also generate significant strategic value.

## Research Question

Did the Belt and Road Initiative improve Kazakhstan's bilateral trade balance with China, and did BRI change the effect of strategic mineral exports on that trade balance?

## Aim

The aim of the project is to evaluate whether the post-BRI period is associated with an improved Kazakhstan-China bilateral trade balance and whether strategic mineral exports became more important for Kazakhstan's trade position after BRI.

## Objectives

1. Collect annual Kazakhstan-China bilateral trade data from verified public sources.
2. Construct Kazakhstan's bilateral trade balance with China.
3. Identify and measure strategic mineral exports from Kazakhstan to China.
4. Compare pre-BRI and post-BRI trade patterns.
5. Estimate a parsimonious model testing the post-BRI period, strategic mineral exports, and their interaction.
6. Interpret the findings through Dependency Theory and trade facilitation logic.

## Hypotheses

### H1: Post-BRI Trade Balance Hypothesis

The post-BRI period is associated with a change in Kazakhstan's bilateral trade balance with China.

### H2: Strategic Mineral Export Hypothesis

Higher strategic mineral exports from Kazakhstan to China are associated with a more favorable Kazakhstan-China bilateral trade balance.

### H3: Interaction Hypothesis

The association between strategic mineral exports and Kazakhstan's bilateral trade balance changed after BRI.

## Methodology

The project will use an annual country-pair dataset for Kazakhstan-China trade. The main dependent variable will be Kazakhstan's bilateral trade balance with China:

```text
trade_balance_usd = exports_kazakhstan_to_china_usd - imports_kazakhstan_from_china_usd
```

A secondary dependent variable may use the trade balance ratio:

```text
trade_balance_ratio = trade_balance_usd / total_bilateral_trade_usd
```

The main explanatory variables will be a post-BRI indicator, strategic mineral export value, and an interaction between the two. The baseline model will be:

```text
trade_balance = beta0
              + beta1 post_bri
              + beta2 strategic_mineral_exports
              + beta3 post_bri * strategic_mineral_exports
              + limited controls
              + error
```

The project will use IMF DOTS or another verified bilateral source for aggregate trade flows, UN Comtrade for commodity-level strategic mineral exports, and World Bank WDI for possible macroeconomic controls. The final selection of commodity codes must be documented before estimation.

Because the sample will use annual data, the model must remain simple. The final paper will prioritize transparent descriptive analysis, cautious model interpretation, and sensitivity checks over complex estimation.

## Expected Contribution

The expected contribution is to reframe the evaluation of BRI in Kazakhstan-China trade. Instead of asking only whether trade increased, the project asks whether Kazakhstan's trade balance improved and whether strategic minerals contributed to that improvement. This provides a more precise way to evaluate the economic implications of BRI for a resource-rich but structurally smaller partner.

The project also contributes methodologically by building a transparent research repository. The repository documents the research question, theoretical logic, planned data sources, model specification, preliminary descriptive outputs, and remaining analytical tasks. This structure makes the workflow easier to review and revise.

## Limitations

The main limitation is the small number of annual observations. This restricts the complexity of the model and limits causal inference. A second limitation is that BRI is a broad policy environment rather than a clearly isolated treatment. A third limitation is that strategic mineral export values may reflect price changes as well as quantity changes. Finally, commodity classification choices in UN Comtrade require careful documentation because different HS codes may lead to different measures.

These limitations do not make the project invalid, but they require cautious interpretation. The final paper should present findings as associations unless a stronger identification strategy is developed.

## Conclusion

This project investigates whether BRI improved Kazakhstan's bilateral trade balance with China and whether strategic mineral exports changed that relationship. It is motivated by the need to distinguish trade expansion from trade-balance improvement. By combining Dependency Theory, trade facilitation logic, and a focused empirical model, the project aims to produce a serious and transparent analysis suitable for a final term paper.
