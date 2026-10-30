---
title: "BRI's Impact on Kazakhstan-China Trade Balance: The Role of Strategic Mineral Exports"
subtitle: "Evidence from Annual (2000–2023) and Observed Monthly (2010–2019) Bilateral Trade Data"
author: "Nikar Omirbek"
bibliography: ../Literature_Review/bibliography.bib
---

# Abstract

This thesis examines the post-BRI association between the Belt and Road Initiative (BRI) and the Kazakhstan–China bilateral trade balance, focusing on the role of strategic mineral exports. The main dataset is an annual bilateral time series for 2000–2023 (*n* = 24), complemented by 120 months of observed UN Comtrade data for 2010–2019. The analysis applies descriptive pre/post decomposition, structural-break diagnostics, OLS association models with Newey–West standard errors, formal one-sided hypothesis tests with full model fit statistics, Granger causality tests, and a 288-specification robustness grid. The central puzzle is that strategic mineral exports rose by 29.2 per cent between the pre-BRI (2000–2013) and post-BRI (2014–2023) periods, yet the average bilateral trade balance fell by 37.8 per cent, mainly because imports from China grew far faster than exports (+94.3 per cent against +24.3 per cent). In the primary annual model, mineral exports are positively associated with the balance before BRI (β = 1.65, one-sided *p* = 0.037), and this association weakens after 2013 (interaction β = −2.49, one-sided *p* = 0.011; *R*² = 0.74). The same pattern appears in observed monthly data that end before 2020 (β = 1.26, one-sided *p* = 0.001; interaction β = −0.91, one-sided *p* = 0.004; *R*² = 0.74). Interpolating the annual data to 96 quarters reproduces the annual estimates but adds no independent information, as a Monte Carlo experiment confirms. Mirror-data validation reveals that Kazakhstan-reported imports from China are under-recorded in 2020–2022. This reporting break explains much of the apparent dependence of the annual result on 2023. Granger tests find no evidence that mineral exports lead the trade balance, and the monthly interaction disappears once bilateral oil exports are controlled for. The results are therefore interpreted as a conditional association that is robust in observed monthly data and consistent with asymmetric interdependence, not as evidence of a causal or mineral-specific BRI effect.

**Keywords:** Belt and Road Initiative; Kazakhstan–China trade; strategic minerals; asymmetric interdependence; trade balance; small-sample diagnostics; post-BRI period


# 1. Introduction

*Note on terminology: The official registered title of this dissertation uses the word "impact." Throughout this work, "impact" refers to post-BRI associations and trade-balance dynamics observed in the data, not to a causal effect established through experimental or quasi-experimental identification. The analysis is explicitly diagnostic and associational.*

Kazakhstan occupies a central position in the overland economic geography of China's Belt and Road Initiative (BRI). The Silk Road Economic Belt was announced in Astana in September 2013, and since then Kazakhstan's transport corridors, mineral exports, and financing relationships have been folded into the broader architecture of Eurasian connectivity. Policy discourse frequently treats BRI as a vehicle for mutual economic benefit: more infrastructure should reduce trade costs, increase bilateral exchange, and expand opportunities for landlocked economies. Yet the distinction between trade growth and trade-balance improvement is analytically essential. A corridor that increases both exports and imports may expand total trade while simultaneously weakening the bilateral trade-balance position of the smaller partner.

This thesis studies a specific dimension of that problem. The research question asks: *How did the post-BRI period coincide with changes in the relationship between Kazakhstan's strategic mineral exports to China and Kazakhstan's bilateral trade balance with China?* The question is deliberately associational. BRI is not a randomly assigned treatment, and the available data do not support credible causal identification. The thesis therefore provides diagnostic and suggestive evidence rather than causal proof.

The analytical motivation is straightforward. Kazakhstan's exports to China are heavily concentrated in natural resources, including uranium, copper, and chromium products. These strategic minerals are economically valuable and increasingly relevant to China's industrial and energy supply chains. If BRI-era trade facilitation strengthened Kazakhstan's mineral export position, one might expect the bilateral trade balance to improve, or at least to maintain its pre-BRI level. The descriptive evidence suggests otherwise. Between 2000–2013 and 2014–2023, Kazakhstan's average bilateral trade balance with China fell by 37.8 per cent, from USD 3.35 billion to USD 2.08 billion, even as narrow strategic mineral exports rose by 29.2 per cent, from USD 1.92 billion to USD 2.48 billion (Table 4.2). Trade decomposition reveals that this divergence is driven primarily by import-side deepening: Kazakhstan's imports from China grew by 94.3 per cent compared to export growth of 24.3 per cent (Table 4.3). This pattern motivates the central puzzle: mineral exports increased, yet the bilateral trade-balance position weakened because import growth substantially outpaced export growth.

The thesis uses asymmetric interdependence as its primary theoretical lens. Following Keohane and Nye [-@keohane_nye_1977] and Hirschman [-@hirschman_1945], the framework treats economic linkages as a source of both gains and vulnerability. Interdependence becomes asymmetric when one partner has more outside options, greater market power, or lower adjustment costs. The framework is more precise than dependency theory because it allows for mutual gains, sectoral leverage, and policy agency, while still treating trade concentration as politically and economically consequential.

The empirical strategy is convergent and transparent. The thesis constructs an annual Kazakhstan–China bilateral time-series dataset for 2000–2023, estimates descriptive pre/post comparisons, structural-break diagnostics, and dynamic association models (OLS with HAC standard errors), and performs a 288-row robustness grid. Multicollinearity is addressed by adopting GDP growth rates as the primary specification (max VIF = 10.4, down from 236.3 in the original GDP-levels model). The primary regression estimates a negative post-BRI × minerals interaction of −2.49 (*p* = 0.011). In the series as reported, this result does not survive exclusion of 2022–2023. Mirror-data validation shows that this fragility is largely caused by under-recorded imports in 2020–2022 (§4.7, §6.20). Observed monthly data for 2010–2019 (*n* = 120) reproduce the negative interaction without using any post-2019 year (§6.18). A two-way fixed-effects (TWFE) difference-in-differences design, using Kazakhstan's trade with Russia, Germany, Uzbekistan, Turkey and the USA as comparison partners, shows that the post-2013 deterioration with China (−0.305) was the largest of the six. The magnitude is robust, but with only six partners its statistical precision is limited (§6.15).

These results are interpreted as diagnostic evidence consistent with asymmetric interdependence, not as causal proof. The strongest empirical contributions are: (i) the descriptive decomposition showing import-side deepening; (ii) the weakening of the mineral–balance association in observed monthly data before 2020; (iii) the collapse of oil exports to China after 2014 as a central, previously unmeasured part of the story (§4.6); (iv) the finding that the deterioration with China was the largest among Kazakhstan's major partners; and (v) the documentation of a 2020–2022 break in Kazakhstan's import statistics.

## 1.1 Relevance, Research Problem, Aim and Objectives

**Relevance.** China is Kazakhstan's largest source of imports and its second-largest export market: in 2023 it accounted for 27.4 per cent of Kazakhstan's imports and 18.7 per cent of its exports [@bns_2024_foreign_trade]. Kazakhstan is also the country where the Silk Road Economic Belt was announced, and BRI is routinely presented in both countries' policy discourse as mutually beneficial. Whether it has been mutually beneficial *for Kazakhstan's external position* is therefore a question of direct policy interest. The question is all the more pressing because the bilateral balance as recorded turned negative for the first time in 2023 (§4.5), and because Kazakhstan's own trade statistics for 2020–2022 understate imports from China (§4.7).

**Research problem.** Kazakhstan's trade with China grew after 2013, and so did its exports of strategic minerals. Yet its bilateral trade surplus with China fell by 37.8 per cent. Existing BRI research largely measures trade *volumes* and infrastructure effects; it says little about whether a resource-exporting partner's *balance* improves, or whether its mineral exports translate into a stronger position. This thesis addresses that gap for the Kazakhstan–China pair.

**Aim.** To assess how the relationship between Kazakhstan's strategic mineral exports to China and its bilateral trade balance with China changed after the launch of BRI, and to interpret that change through the theory of asymmetric interdependence.

**Objectives.** The aim is pursued through six objectives, each addressed in a specific chapter:

1. To review the literature on trade specialisation, commodity dependence, BRI as trade facilitation and asymmetric interdependence, and to identify the research gap (Chapters 2–3).
2. To construct and validate a reproducible Kazakhstan–China dataset: annual for 2000–2023, and observed monthly for 2010–2019 (Chapter 4).
3. To decompose post-BRI changes in exports, imports and the trade balance, distinguishing trade growth from trade-balance improvement (§4.5).
4. To test whether mineral exports were associated with the trade balance before BRI, and whether that association changed afterwards (hypotheses H1–H3; Chapters 5–6).
5. To test whether the post-2013 change is larger for China than for other partners (difference-in-differences against five other partners), which way predictive causation runs (Granger tests), and how robust the results are to data and specification choices (Chapter 6).
6. To derive policy recommendations for Kazakhstan and comparable resource-exporting BRI partners (Chapters 7–8).

**Object and subject.** The *object* of the research is Kazakhstan–China bilateral trade. The *subject* is the relationship between Kazakhstan's strategic mineral exports and its bilateral trade balance with China before and after BRI.

**Methods.** Descriptive pre/post decomposition; OLS association models with Newey–West standard errors and formal one-sided hypothesis tests; monthly time-series models on observed UN Comtrade data; Granger causality tests (VAR in differences and Toda–Yamamoto); a two-way fixed-effects difference-in-differences design; influence, structural-break and robustness diagnostics; and mirror-data validation of the trade statistics.

**Scientific novelty.**

1. The thesis shifts the empirical question for the Kazakhstan–China case from trade *volume* to trade *balance*, and tests directly whether strategic mineral exports protected the balance after BRI.
2. It combines annual data with 120 months of observed monthly data, showing that the weakening of the mineral–balance association appears before 2020 and does not depend on the contested 2020–2023 years.
3. It documents, through mirror-data comparison, that Kazakhstan-reported imports from China are under-recorded in 2020–2022, and shows how this distorts conclusions drawn from the official series.
4. It shows, using observed monthly HS 27 data, that the collapse of oil exports to China after 2014 is central to the post-BRI weakening of Kazakhstan's position, and, with a multi-partner difference-in-differences design, that the deterioration with China was the largest among Kazakhstan's major partners.

**Practical significance.** The results are relevant to Kazakhstan's trade and economic-policy bodies and its statistical authority. They show that BRI outcomes should be monitored through the composition and balance of bilateral trade, not through turnover alone; that raw mineral exports did not secure a stronger bilateral position, which strengthens the case for in-country processing and export diversification; and that bilateral import statistics for 2020–2022 need reconciliation with partner data. The reproducible dataset and code can be reused for other Central Asian BRI partners.

**Provisions submitted for defence.**

1. After 2013, Kazakhstan's imports from China grew far faster than its exports (+94.3 per cent against +24.3 per cent), so trade growth coincided with a weaker bilateral balance.
2. Before BRI, strategic mineral exports were positively associated with the bilateral balance; after BRI, this association weakened and is no longer distinguishable from zero, in both annual and observed monthly data.
3. The post-2013 deterioration with China was the largest among Kazakhstan's major partners and coincided with a collapse in oil exports to China; the evidence supports an association consistent with asymmetric interdependence, not a causal or mineral-specific BRI effect.
4. Kazakhstan's official 2020–2022 import statistics understate imports from China, and correcting them changes the apparent fragility of the regression results.

## 1.2 Contribution

This thesis makes five specific contributions. First, it distinguishes between trade expansion and trade-balance improvement, shifting attention from aggregate trade volumes to bilateral trade-balance outcomes in a diagnostic case study of Kazakhstan and China. Second, it bridges theory and method by using asymmetric interdependence to interpret the moderating compositional channel of strategic mineral exports, accommodating both mutual gains and distributional asymmetry. Third, it tests whether strategic mineral exports translated into external-balance improvement, demonstrating that resource-export growth is not inherently synonymous with an improved external position. Fourth, it provides a transparent and reproducible annual Kazakhstan–China single country-pair dataset with a fully scripted pipeline. Fifth, it treats the results explicitly as diagnostic and fragile, deploying small-sample robustness checks and influence diagnostics to document the critical role of 2023. By providing an honest interpretation of fragility, the thesis strengthens methodological discipline and avoids claiming definitive causal identification of a stable structural effect.

## 1.3 Structure

The remainder of this thesis is organised as follows. Chapter 2 reviews the literature and identifies the research gap. Chapter 3 presents the theoretical framework. Chapter 4 describes the data, variable construction, and data limitations. Chapter 5 explains the empirical strategy. Chapter 6 presents the results, including influence diagnostics and model stability analysis. Chapter 7 discusses the findings and their implications. Chapter 8 concludes.


# 2. Literature Review

The literature relevant to Kazakhstan–China trade under BRI spans several overlapping debates. Rather than summarising individual studies, this review synthesises what the literature agrees on, identifies disagreements and limitations, and explains how each strand connects to the research question.

## 2.1 Trade Theory, Resource Specialisation, and Trade-Balance Outcomes

Classical trade theory predicts that countries gain from trade by specialising according to comparative advantage [@ricardo_1817]. The Heckscher–Ohlin framework extends this logic: resource-abundant countries like Kazakhstan should export resource-intensive goods, while labour- and capital-abundant countries like China should export manufactures [@heckscher_1919; @ohlin_1933]. In this framework, bilateral trade expansion is mutually beneficial regardless of trade-balance outcomes, because gains accrue through efficiency improvements rather than balance-of-payments surplus.

However, the trade-balance implications of resource specialisation are not neutral. Bhagwati [-@bhagwati_1958] demonstrated that export growth can be *immiserising* if it worsens the terms of trade sufficiently to offset volume gains. Applied to Kazakhstan, this concern is relevant because strategic mineral exports are price-taking commodities subject to global demand cycles. If mineral export values rise due to volume expansion while unit values stagnate or decline, the trade-balance benefit may be smaller than headline export figures suggest.

New trade theory [@krugman_1979; @helpman_krugman_1985] adds that trade patterns between differentiated and homogeneous goods producers create structural asymmetries. A country exporting homogeneous minerals and importing differentiated manufactures faces different elasticities of substitution on each side of its trade balance. This framework helps explain why import-side growth from China—spanning machinery, consumer goods, and intermediate inputs—may be more income-elastic than mineral export growth.

**Empirical bridge (Pillar 1 — trade theory).** This strand predicts that `minerals_narrow` should have a **positive** coefficient in the pre-BRI baseline (H2): mineral export revenues are associated with an improved bilateral balance. The differential elasticity prediction implies that import growth will outpace export growth post-BRI, consistent with the **negative** `post_bri_x_minerals` interaction in H3.

## 2.2 Commodity Dependence, Terms of Trade, and External Vulnerability

The Prebisch–Singer hypothesis posits that the terms of trade for primary commodity exporters tend to deteriorate over time relative to manufactured-goods exporters [@prebisch_1950; @singer_1950]. Harvey et al. [-@harvey_etal_2010] provide four centuries of evidence consistent with long-run commodity terms-of-trade decline, though with significant heterogeneity across commodities and periods.

Sachs and Warner [-@sachs_warner_1995] link resource abundance to development risks through the resource curse mechanism, while van der Ploeg [-@vanderploeg_2011] emphasises that resource wealth can be either a curse or blessing depending on institutional quality, volatility management, and reinvestment patterns. Auty [-@auty_1993] coined the term "resource curse" and documented how mineral-rich developing economies often underperform expectations. Corden and Neary [-@corden_neary_1982] formalised Dutch Disease, showing how resource booms can crowd out manufacturing competitiveness through real exchange-rate appreciation.

Frankel [-@frankel_2010] reviews the resource curse literature and argues that the negative association between resources and growth is not deterministic but conditional on institutions and commodity-price management. Applied to Kazakhstan, the relevant question is whether BRI-era mineral export growth was accompanied by value-added upgrading and import-substitution or whether it reproduced the commodity-dependent pattern that the resource curse literature identifies as problematic.

**Empirical bridge (Pillar 2 — resource dependence).** This strand predicts that `brent_annual_mean` should carry an **ambiguous but predominantly positive** sign: higher commodity prices improve Kazakhstan's export revenues in the short run (positive for balance), but via Dutch Disease mechanisms may also appreciate the real exchange rate and crowd out manufacturing (partially negative over time). The `kzt_usd` depreciation variable captures the reverse competitiveness channel and is predicted to be **positive** on the bilateral balance via the Marshall–Lerner condition.

## 2.3 BRI as Trade Facilitation

The strongest econometric evidence for BRI trade effects comes from gravity and GIS-linked models. De Soyres et al. [-@desoyres_etal_2019; -@desoyres_etal_2020] use shipping-time estimates to show that BRI infrastructure can reduce trade costs, with the largest gains concentrated along corridors. Baniya, Rocha, and Ruta [-@baniya_rocha_ruta_2020] estimate gravity models and find that BRI-related improvements raise trade flows, especially when transport investment is complemented by trade reforms. Anderson and van Wincoop [-@anderson_vanwincoop_2003] provide the theoretical foundation for gravity-based trade-cost analysis. Rolland [-@rolland_2017] situates these trade-facilitation dynamics within China's broader Eurasian strategic logic, arguing that BRI infrastructure serves geopolitical as well as commercial purposes. Swaine [-@swaine_2015] analyses Chinese official commentary on BRI, showing that the initiative was explicitly framed to combine economic connectivity with strategic depth.

However, the trade-facilitation literature has an important limitation for this thesis. It generally treats increased trade as the primary success metric. It does not systematically ask whether the smaller partner's bilateral trade balance improves, deteriorates, or remains unchanged. A corridor that increases both exports and imports may raise total trade while shifting the trade-balance distribution against the resource-exporting partner.

**Empirical bridge (Pillar 3 — BRI trade facilitation).** This strand predicts that `log(CN GDP / KZ GDP)` should have a **negative** sign: as China's economy grows faster relative to Kazakhstan's, its export capacity expands, worsening Kazakhstan's bilateral trade balance. It also motivates the `post_bri_2013` period dummy as a partial test of trade-cost reduction, while noting that the dummy conflates BRI-specific effects with concurrent commodity shocks. The comparative DiD design (§6.5) addresses this limitation by testing whether the post-2013 balance shift is China-specific or common across all of Kazakhstan's trading partners.

## 2.4 BRI as Asymmetric Interdependence

A second strand treats BRI-era connectivity as a context for asymmetric economic relationships. Keohane and Nye [-@keohane_nye_1977] define interdependence as mutual dependence that creates both sensitivity and vulnerability. Hirschman [-@hirschman_1945] argues that foreign trade generates political influence when a partner's dependence is concentrated and costly to replace.

Horn, Reinhart, and Trebesch [-@horn_reinhart_trebesch_2021] document the rise of China as the world's largest official creditor, showing that Chinese lending creates financial interdependencies alongside trade linkages. Hurley, Morris, and Portelance [-@hurley_morris_portelance_2018] assess the debt-sustainability implications of BRI financing for low- and middle-income countries, finding that several corridor economies face elevated risk. Brautigam [-@brautigam_2020] critically examines the "debt-trap diplomacy" narrative, cautioning against both uncritical BRI promotion and undifferentiated alarmism—a nuance relevant to the Kazakhstan case, where Chinese financing supports infrastructure without yet producing the balance-sheet stress seen in some South Asian borrowers. Recent Kazakhstan-specific evidence supports asymmetric rather than symmetric interdependence. Primiano and Kudebayeva [-@primiano_kudebayeva_2025], using a university survey, find that BRI's reception in Kazakhstan is uneven rather than uniformly positive. Grant [-@grant_2020] shows how border security, soft power, and suspicion interact at the Sino-Kazakh boundary at Khorgos.

**Empirical bridge (Pillar 4 — asymmetric interdependence, PRIMARY).** This is the load-bearing pillar. It predicts that (i) `post_bri_x_minerals` should be **negative** (H3): the post-BRI period coincided with mineral export growth failing to translate into trade-balance improvement, as China's leverage expanded faster than Kazakhstan's export revenues; (ii) `post_bri_2013` should be **negative** (H1): the post-BRI period is associated with a level shift in bilateral trade that favours the more diversified partner; (iii) this pattern should be **China-specific** rather than common across all of Kazakhstan's partners, which is evaluated by the DiD partner-placebo design (§6.15) and the synthetic counterfactual (§6.16). Variables directly operationalising this pillar are `post_bri_2013`, `post_bri_x_minerals`, and `log(CN GDP / KZ GDP)`.

## 2.5 Kazakhstan, Central Asia, and China

Central Asia studies caution that geography and local political economy matter. Bird, Lebrand, and Venables [-@bird_lebrand_venables_2020] model how BRI can reshape economic geography in Central Asia, with gains unevenly distributed across locations. Pomfret [-@pomfret_2019] analyses Central Asian trade patterns and regional integration dynamics. Cooley [-@cooley_2012] examines great-power competition in Central Asia, including China's growing economic footprint. Laruelle [-@laruelle_2018] documents China's Belt and Road Initiative in Central Asia from multiple analytical perspectives. Laruelle and Peyrouse [-@laruelle_peyrouse_2012] provide foundational analysis of the social and political dimensions of China's growing presence in the region, including the reception of Chinese labour and capital by local populations. Olcott [-@olcott_2002] offers an early and still-relevant account of Kazakhstan's post-independence challenges, establishing the resource-dependence baseline against which BRI-era changes should be measured.

Jepson and Baldakova [-@jepson_2024] directly examine whether Chinese state capital supports resource-based structural transformation, through downstream linkages, in Bolivia and Kazakhstan. Calabrese [-@calabrese_2024] asks whether Chinese capital can support diversification away from extractives in the Kyrgyz Republic. The global value chain (GVC) literature adds that governance structures shape whether suppliers upgrade or remain in captive, low-value positions [@gereffi_humphrey_sturgeon_2005].

**Empirical bridge (Pillar 5 — GVC and upgrading).** This strand predicts that if Kazakhstan occupies a captive supplier position, the `post_bri_x_minerals` interaction should be **negative**: rising mineral exports coincide with rising imports of Chinese capital goods and machinery needed for extraction, rather than supporting domestic value-chain upgrading. The import-category decomposition in §6.4 (HS 84 machinery, HS 85 electronics, HS 87 vehicles) tests this mechanism directly: if these categories exploded disproportionately post-2013, it is consistent with an extractive-infrastructure import channel that drains the trade balance while mineral exports rise.

## 2.6 Empirical Methods in BRI and Small-Sample Trade Research

Time-series analysis of bilateral trade relationships frequently involves small annual samples. Pesaran, Shin, and Smith [-@pesaran_shin_smith_2001] developed the ARDL bounds-testing approach specifically for cases with mixed integration orders and limited observations. Newey and West [-@newey_west_1987] introduced heteroskedasticity and autocorrelation consistent (HAC) standard errors for time-series regression. Chow [-@chow_1960] proposed the structural-break test used in this thesis. Bai and Perron [-@bai_perron_1998; -@bai_perron_2003] developed multiple-break detection methods.

A key methodological concern in small-sample regression is influence diagnostics. Cook [-@cook_1977] demonstrated that individual observations can disproportionately affect regression estimates, particularly in samples below 30 observations. Belsley, Kuh, and Welsch [-@belsley_kuh_welsch_1980] provided comprehensive influence diagnostic tools that are essential for validating results in the sample sizes encountered in bilateral trade studies.

## 2.7 Research Gap

Most BRI studies focus on aggregate trade expansion or infrastructure connectivity. Fewer examine whether resource exports improve the bilateral trade balance of smaller resource-exporting partners. The compositional question—whether mineral export growth translates into external-balance improvement—remains empirically underdeveloped for the Kazakhstan–China case. Moreover, no existing study applies formal influence diagnostics to assess how robust post-BRI trade findings are to individual high-leverage observations. This thesis addresses that gap.


# 3. Theoretical Framework

## 3.1 Primary Framework: Asymmetric Interdependence

The primary theoretical framework is **asymmetric interdependence**, as developed by Keohane and Nye [-@keohane_nye_1977] and Hirschman [-@hirschman_1945]. This framework is chosen over dependency theory because it is both more precise and more empirically testable: it allows for mutual gains from trade while predicting that the distribution of those gains, and the distribution of vulnerability, depend on the structural position of each partner.

Keohane and Nye define interdependence as mutual dependence between states or actors across issues, characterised by two distinct dimensions: *sensitivity* (the extent to which changes in one economy are transmitted to another before policy adjusts) and *vulnerability* (the cost of adjusting to those changes after the fact). Two economies can be simultaneously interdependent and asymmetrically so: China and Kazakhstan both depend on bilateral trade, but China can diversify mineral suppliers at lower cost than Kazakhstan can diversify its export markets. This structural asymmetry predicts that deepening bilateral integration will expand aggregate trade while potentially strengthening China's bargaining position.

Hirschman's mechanism sharpens the prediction. In *National Power and the Structure of Foreign Trade*, Hirschman shows that dependence on a large trading partner generates political influence for the partner precisely when the dependent economy's trade is *concentrated* (few substitutable partners) and *inelastic* (the dependent economy cannot easily reduce or redirect trade). Kazakhstan's export basket is highly concentrated in mineral commodities shipped predominantly to China and Russia, with limited substitution options in the short run. Hirschman's framework therefore predicts that post-BRI deepening of mineral trade—by increasing Kazakhstan's exposure to Chinese demand while China retains many alternative suppliers—will strengthen the asymmetric structure of the relationship and may translate into a weakening of Kazakhstan's bilateral trade-balance position, as import capacity grows faster than export revenues.

This framework is preferred over dependency theory, which is retained only as *historical context* (§3.3). The critical difference is falsifiability: asymmetric interdependence generates variable-level predictions that can be tested in regression models (§3.4), whereas dependency theory operates at the level of structural formations and does not readily produce falsifiable coefficient predictions. The empirical strategy in this thesis is built entirely on the asymmetric interdependence framework.

## 3.2 Supporting Frameworks

Three supporting theoretical strands inform variable selection and interpretation:

**Gravity and trade facilitation.** Anderson and van Wincoop [-@anderson_vanwincoop_2003] show that bilateral trade depends on trade costs relative to multilateral resistance. BRI infrastructure reduces bilateral trade costs, increasing trade on both sides of the bilateral relationship. For the present model, China's GDP proxies *foreign demand capacity* — a larger Chinese economy demands more inputs from Kazakhstan and exports more manufactured goods, both effects that simultaneously expand the bilateral relationship and expose Kazakhstan to the import-side risk that asymmetric interdependence theory identifies.

**Resource curse and terms-of-trade channel.** Van der Ploeg [-@vanderploeg_2011] and Sachs and Warner [-@sachs_warner_1995] identify conditions under which resource-export dependence generates macroeconomic vulnerability. For this model, the Brent crude price proxies global commodity market conditions that simultaneously drive the value of Kazakhstan's energy and mineral exports and affect China's import demand for those commodities. The predicted relationship between global commodity prices and the bilateral trade balance is theoretically ambiguous: higher oil prices raise export revenues (positive for the balance) but may also appreciate the real exchange rate and crowd out non-commodity exports (negative).

**Global value chains (GVC) and upgrading.** Gereffi, Humphrey, and Sturgeon [-@gereffi_humphrey_sturgeon_2005] show that captive supplier positions in raw-material chains provide little upgrading leverage. For this model, the minerals–post-BRI interaction term tests whether mineral export growth translates into trade-balance improvement or whether raw-mineral export growth coincides with rising imports of Chinese capital goods and intermediates, consistent with a captive supplier relationship that generates asymmetric gains.

## 3.3 Why Not Dependency Theory

Dependency theory and world-systems analysis provide the intellectual history from which the asymmetric interdependence framework builds. Frank [-@frank_1967; as cited in the dependency tradition] and Prebisch [-@prebisch_1950] argue that peripheral commodity exporters face structural terms-of-trade deterioration imposed by the architecture of the global economy. This framing is useful for contextualising Kazakhstan's commodity-export position but is not adopted as the primary framework for three reasons: (i) it tends to overpredict structural subordination and understate policy agency; (ii) it does not generate variable-level coefficient predictions; (iii) the empirical evidence on Prebisch–Singer is heterogeneous and commodity-specific (Harvey et al. [-@harvey_etal_2010]), making it a weaker anchor for regression-based analysis. The thesis therefore uses asymmetric interdependence as the testable mechanism and treats dependency theory as background context.

## 3.4 Variable Selection Rationale and Predicted Signs

Every regressor in the empirical model is anchored to the theoretical framework above. The table below maps each variable to its theoretical mechanism, predicted sign on the bilateral trade balance, and supporting citation. This mapping is the bridge between theory and empirics that structures all results in Chapter 6.

**Table 3.1. Variable Selection Rationale**

| Variable | Theoretical mechanism | Predicted sign on TB | Key citation |
|----------|----------------------|---------------------|-------------|
| `minerals_narrow` (USD bn) | Hirschman concentration proxy: higher mineral exports increase export revenues, predicted to improve the bilateral balance *before* accounting for post-BRI import deepening | **Positive** (pre-BRI baseline) | Hirschman [-@hirschman_1945]; H2 |
| `post_bri_2013` (0/1) | Period indicator for post-BRI structural change; tests whether the bilateral balance level shifted after 2013 corridor deepening | **Negative** (asymmetric interdependence predicts import-side acceleration dominates) | Keohane & Nye [-@keohane_nye_1977]; H1 |
| `post_bri_x_minerals` | Asymmetric interdependence interaction: tests whether the trade-balance payoff of mineral exports weakened post-BRI, as rising Chinese manufactured exports outpaced mineral-export revenues | **Negative** (primary test of H3) | Hirschman [-@hirschman_1945]; Keohane & Nye [-@keohane_nye_1977] |
| `brent_annual_mean` (USD/bbl) | Resource-curse / terms-of-trade channel: global commodity prices affect both export revenues and Chinese import demand; sign is theoretically ambiguous but expected positive via revenue channel | **Ambiguous** (positive via export revenue; potentially negative via Dutch disease crowding) | Van der Ploeg [-@vanderploeg_2011]; Corden & Neary [-@corden_neary_1982] |
| `kzt_usd` (tenge per USD) | Competitiveness channel: a weaker tenge (higher KZT/USD) makes Kazakh exports cheaper in dollar terms and Chinese imports more expensive, predicted to improve the bilateral balance | **Positive** (depreciation improves balance via Marshall-Lerner) | Standard open-economy macroeconomics; Bhagwati [-@bhagwati_1958] |
| `log(KZ GDP)` | Domestic income / absorption: higher Kazakh GDP increases import capacity; ambiguous net effect on bilateral balance; **severe multicollinearity (VIF > 130)** renders this variable unreliable in levels — see §5 and Appendix B | **Ambiguous** (absorption vs. export-capacity effects) | World Bank WDI; Anderson & van Wincoop [-@anderson_vanwincoop_2003] |
| `log(CN GDP)` | Foreign demand / gravity: higher Chinese GDP increases demand for Kazakh mineral exports (positive for balance) but also expands China's manufactured-export capacity (negative for balance); **severe multicollinearity (VIF > 236) in levels** — see §5 | **Ambiguous** (demand effect positive; supply effect negative); **replaced by d.log(CN GDP) growth rate in primary specification; gravity ratio in robustness** | Anderson & van Wincoop [-@anderson_vanwincoop_2003] |
| `d.log(KZ GDP)`, `d.log(CN GDP)` [**primary**] | Annual growth rates; stationary; eliminate trending-variable collinearity; VIF = 2.63 and 3.36 respectively | **Ambiguous sign** (income effects); primary specification (max VIF = 10.4) | Anderson & van Wincoop [-@anderson_vanwincoop_2003]; §6.3 |
| `log(CN GDP / KZ GDP)` [robustness] | Gravity-motivated relative size: one parsimonious regressor captures bilateral asymmetry in market size; retained as robustness check (max VIF = 33.4) | **Negative** (rising ratio = deeper asymmetry) | Anderson & van Wincoop [-@anderson_vanwincoop_2003]; §6.3 |

*Note: The primary specification uses GDP growth rates (d.log) following multicollinearity diagnostics (§6.3). The gravity-ratio specification is retained as a robustness check. Both GDP-levels specifications are retained in Appendix B for transparency.*

## 3.5 Testable Hypotheses

The asymmetric interdependence framework produces three testable hypotheses that correspond directly to the variable mapping above:

**H1 (Trade-Balance Change):** The post-BRI period (2014–2023) is associated with a weaker bilateral trade-balance position for Kazakhstan relative to China, conditional on commodity and macroeconomic controls. Mechanism: Keohane–Nye sensitivity asymmetry — BRI infrastructure simultaneously facilitates Kazakh mineral exports and Chinese manufactured exports, but China's diversified export basket grows faster than Kazakhstan's concentrated mineral exports.

**H2 (Mineral Export Payoff):** Higher strategic mineral exports are positively associated with Kazakhstan's bilateral trade balance in the pre-BRI baseline period. Mechanism: Hirschman export-revenue channel — mineral exports generate foreign exchange that directly improves the bilateral balance before post-BRI import deepening takes hold.

**H3 (Asymmetric Interaction):** The post-BRI × minerals interaction is negative, indicating that the trade-balance payoff of mineral exports weakened after BRI corridor deepening. Mechanism: asymmetric interdependence deepening — rising Chinese manufactured exports and the expansion of import-intensive infrastructure financing outpace the revenue gains from mineral exports, producing a deteriorating bilateral position despite export growth. A negative interaction is interpreted as diagnostic evidence consistent with Hirschman's dependence mechanism, not as causal proof of a BRI effect.

# 4. Data and Variables

## 4.1 Data Sources and Panel Construction

The analysis uses an annual Kazakhstan–China bilateral time-series dataset for 2000–2023 (*n* = 24). Data sources include: (i) IMF Direction of Trade Statistics (DOTS) and UN Comtrade for bilateral exports and imports; (ii) UN Comtrade HS-2 and World Bank WITS for strategic mineral and ores/metals exports; (iii) World Bank WDI for GDP, exchange rates, and CPI; (iv) Federal Reserve Bank of St. Louis (FRED) for Brent crude oil prices and London Metal Exchange copper prices; (v) AidData for Chinese finance flows. The year 2024 is excluded because import data are unavailable, preventing trade-balance construction.

Table 4.1 consolidates all variables, their sources, coverage, and key limitations. Source consistency is analytically important in this thesis: the mineral export variable switches from a World Bank WITS aggregate (2000–2013) to UN Comtrade HS-2 specific codes (2014–2023), creating a measurement break that coincides with the post-BRI dummy. This break is discussed in detail in §4.3 and addressed by a WITS-consistent robustness specification in §6.6.

**Table 4.1. Data Sources and Variable Construction**

| Variable / Concept | Definition | Source | Coverage | Key Limitation |
|-------------------|-----------|--------|----------|---------------|
| Bilateral exports to China | Kazakhstan's total exports to China, FOB (USD bn) | IMF DOTS; UN Comtrade (KAZ reporter) | 2000–2023 | Mirror-data discrepancies reconciled via bilateral cross-reporting |
| Bilateral imports from China | Kazakhstan's total imports from China, CIF (USD bn) | IMF DOTS; UN Comtrade (KAZ reporter) | 2000–2023 | CIF/FOB adjustment not applied; affects level, not trend |
| Bilateral trade balance | $TB_t = X_t - M_t$ (USD bn) | Derived | 2000–2023 | Dependent on accuracy of both export and import series |
| Strategic mineral exports (narrow) | HS chapters 26 (ores, incl. chromium and copper ores) and 28 (inorganic chemicals, incl. uranium compounds), USD bn | WITS Ores & Metals proxy (2000–2013); UN Comtrade HS 26 + 28, Kazakhstan-reported exports to China (2014–2023) | 2000–2023 | **Measurement break at 2014** coincides with BRI dummy |
| WITS ores and metals proxy | Aggregate ores and metals exports from WITS, USD bn | World Bank WITS | 2000–2023 | Broader than target minerals; used for consistent-proxy robustness |
| Brent crude price | Annual mean Brent spot price, USD/barrel | FRED (St. Louis Fed) | 2000–2023 | Controls global price conditions; does **not** proxy bilateral oil volume |
| KZT/USD exchange rate | Kazakh tenge per US dollar, annual average | World Bank WDI | 2000–2023 | Annual average; within-year volatility not captured |
| log Kazakhstan GDP | Log real GDP, constant 2015 USD | World Bank WDI | 2000–2023 | VIF > 130 in full model; excluded from parsimonious specification |
| log China GDP | Log real GDP, constant 2015 USD | World Bank WDI | 2000–2023 | VIF > 236 in full model; excluded from parsimonious specification |
| Post-BRI dummy | =1 for 2014–2023, =0 for 2000–2013 | Author-constructed | 2000–2023 | Period indicator only; coincides with oil shock, tenge devaluation, COVID-19 |
| Bilateral oil/energy exports | KAZ→CHN HS 2709/2710/2711/2701 exports, USD bn | **Not available** in current dataset | — | Major omitted variable; future research should use Comtrade HS-27 pull |

*Note: Author's compilation. Full variable definitions are available in the accompanying codebook.*

## 4.2 Variable Definitions

**Dependent variable:** Kazakhstan's bilateral trade balance with China in current USD billions: $TB_t = X_t - M_t$.

**Key explanatory variables:**
- *minerals_narrow_B*: Strategic mineral exports in USD billions, measured as HS chapters 26 (ores, slag and ash) and 28 (inorganic chemicals, which include the uranium compounds that make up most of Kazakhstan's uranium exports). Uranium, chromium and copper ores are the main strategic products inside these chapters; product-level codes (HS 2610, 2612, 2844, 7403) are used as a robustness check in the monthly data (§6.18).
- *post_bri_2013*: Binary indicator equal to 1 for 2014–2023 (BRI announced September 2013).
- *post_bri_x_minerals*: Interaction term: post_bri_2013 × minerals_narrow_B.

**Controls:** Brent crude oil price (USD/bbl), KZT/USD exchange rate, log Kazakhstan GDP (constant 2015 USD), log China GDP (constant 2015 USD).

## 4.3 Measurement Break in Mineral Data

A critical limitation concerns the mineral export variable. For 2000–2013, the narrow minerals series is constructed from WITS Ores and Metals exports as a proxy, because HS-6 level Comtrade data for specific mineral categories are not available for the full pre-2014 period. For 2014–2023, the series uses UN Comtrade data at HS-chapter level, chapters 26 and 28, as reported by Kazakhstan. This creates a measurement break at 2014 that changes the source and definition of the variable. This is analytically dangerous because it coincides precisely with the post-BRI dummy.

**Table 4.4. Mineral Variable Measurement by Period**

| Period | Source | Definition | Coverage |
|--------|--------|-----------|----------|
| 2000–2013 | WITS | Ores and Metals aggregate | Broader than target |
| 2014–2023 | Comtrade HS-2 | HS 26 + HS 28 chapters | Narrower, closer to target |

This break means that the post-BRI structural break detected in regression could partly reflect measurement-source switching rather than genuine economic change. Consequently, researchers must avoid overclaiming from the narrow mineral variable alone. A robustness check using the WITS Ores and Metals series consistently for the full 2000–2023 period (Section 6.6) is therefore essential, not optional, for validating the findings.

## 4.4 Data Validation via Independent Cross-Checking

To validate the accuracy of the IMF DOTS / Comtrade trade figures used in this thesis, a cross-validation was conducted using data independently collected from Kazakhstan's Bureau of National Statistics (`stat.gov.kz`) via automated web-scraping.

**Method.** The Bureau publishes annual foreign trade summaries ("Foreign trade turnover of the Republic of Kazakhstan, January-December [year]") at `stat.gov.kz`. Each publication reports Kazakhstan's total exports and imports in USD millions and China's percentage share of both, allowing computation of implied bilateral trade values for comparison against the WITS/Comtrade panel figures.

**Cross-validation results.** The Bureau's 2023 and 2024 annual publications yield bilateral values that are internally consistent with the panel data:

**Table 4.5. Web-Scraped Cross-Validation: Kazakhstan–China Bilateral Trade**

| Year | Panel exports (USD bn) | Scraped exports (USD bn) | Discrepancy | Panel imports (USD bn) | Scraped imports (USD bn) | Discrepancy |
|------|----------------------:|-------------------------:|:-----------:|----------------------:|-------------------------:|:-----------:|
| 2023 | 14.759 | 14.712 | **0.3%** ✓ | 16.772 | 16.758 | **0.1%** ✓ |
| 2024 | 14.897 | 14.936 | **0.3%** ✓ | — | — | — |

*Source: Author's calculations. Data collected from Bureau of National Statistics (stat.gov.kz); panel data from IMF DOTS / UN Comtrade. Discrepancy computed as |panel − scraped| / scraped × 100%.*

All discrepancies are below 0.5% — well within the < 10% threshold for validation support. This confirms that the trade values used in the analytical panel are consistent with Kazakhstan's national statistical authority's official figures. The 2023 import figure (USD 16.772 billion in the panel vs. USD 16.758 billion scraped, a difference of USD 14 million on a USD 16.8 billion total) is the most important validation given that 2023 is the most influential observation in the regression analysis.

## 4.5 Descriptive Statistics and Trade Balance Decomposition

Table 4.2 presents the summary statistics for the 24-year annual sample. The trade balance ranges from a deficit of USD 2.01 billion to a surplus of USD 11.27 billion, with high variability in both the trade balance and strategic mineral exports. This small sample size underscores the need for rigorous diagnostics, as inference may be sensitive to individual years.

**Table 4.2. Descriptive Statistics of Main Variables**

| Variable | N | Mean | Median | Min | Max |
|----------|---|-----:|-------:|----:|----:|
| Exports to China (USD bn) | 24 | 6.957 | 6.098 | 0.647 | 16.484 |
| Imports from China (USD bn) | 24 | 4.137 | 3.620 | 0.151 | 16.772 |
| Trade balance (USD bn) | 24 | 2.820 | 1.441 | −2.014 | 11.270 |
| Ores and metals exports (USD bn) | 24 | 2.268 | 2.114 | 0.048 | 6.039 |

*Source: Author's calculations.*

![Figure 1. Kazakhstan Exports to China vs Imports from China (2000–2023)](../Outputs/generated_figures/fig_1_exports_imports.png)
*Source: Author's construction based on IMF DOTS and UN Comtrade. Figure 1 shows the steady rise of exports punctuated by volatility, while imports from China show a dramatic acceleration in recent years.*

![Figure 2. Kazakhstan–China Bilateral Trade Balance (2000–2023)](../Outputs/generated_figures/fig_2_trade_balance.png)
*Source: Author's construction. Figure 2 highlights the structural decline in the bilateral surplus following the 2013 BRI announcement, culminating in the 2023 deficit.*

![Figure 3. Strategic Mineral Exports to China (2000–2023)](../Outputs/generated_figures/fig_3_minerals.png)
*Source: Author's construction. Figure 3 traces the growth of mineral exports, illustrating the measurement source transition at 2014.*

**Table 4.3. Pre-BRI vs. Post-BRI Means**

| Variable | Pre-BRI (2000–2013) | Post-BRI (2014–2023) | Change (%) |
|----------|--------------------:|---------------------:|-----------:|
| Exports to China (USD bn) | 6.318 | 7.851 | +24.3% |
| Imports from China (USD bn) | 2.970 | 5.771 | +94.3% |
| Trade Balance (USD bn) | 3.347 | 2.081 | −37.8% |
| Minerals Narrow (USD bn) | 1.918 | 2.478 | +29.2% |
| Trade Balance Ratio | 0.405 | 0.197 | −51.2% |

*Source: Author's calculations from clean_panel_annual dataset.*

The decomposition reveals that the trade-balance deterioration is driven by import-side deepening. Imports from China nearly doubled (+94.3%), while exports grew modestly (+24.3%). Strategic mineral exports grew by 29.2%, but this growth was insufficient to offset the import surge. The year 2023 is exceptional: it is the only year in the sample in which Kazakhstan recorded a bilateral trade deficit (−USD 2.01 billion), driven by imports of USD 16.77 billion exceeding exports of USD 14.76 billion. *Caveat:* the decomposition uses Kazakhstan-reported imports, which are under-recorded in 2020–2022 (§4.7). With mirror-adjusted imports for those three years, average post-BRI imports rise by 132.6 per cent rather than 94.3 per cent, and the average balance falls by 71.8 per cent (to USD 0.94 billion) rather than 37.8 per cent, so the import-side deepening finding is, if anything, understated. Whether 2023 is the only deficit year depends on the adjustment (§6.20).

## 4.6 Oil and Energy Exports: An Omitted Variable

Oil and energy products (HS chapter 27) were the largest single component of Kazakhstan's exports to China. Observed monthly UN Comtrade data, reported by Kazakhstan, show that HS 27 made up **59 per cent** of exports to China in 2010–2013 but only **36 per cent** in 2014–2019. In value terms, energy exports to China fell from USD 8.9 billion in 2013 to USD 1.0 billion in 2016, an 89 per cent drop, before partly recovering (USD 2.8 billion in 2019). Over the same period, the share of strategic minerals (HS 26 + 28) in exports to China rose from about 18–22 per cent to 21–36 per cent.

**Table 4.7. Kazakhstan's Exports to China by Main Component, USD bn (Kazakhstan-reported)**

| Year | Total exports | Energy (HS 27) | Energy share | Strategic minerals (HS 26 + 28) | Minerals share |
|---|---:|---:|---:|---:|---:|
| 2010 | 10.12 | 5.54 | 55% | 2.27 | 22% |
| 2011 | 14.78 | 9.56 | 65% | 2.47 | 17% |
| 2012 | 16.48 | 9.10 | 55% | 3.67 | 22% |
| 2013 | 14.37 | 8.92 | 62% | 2.54 | 18% |
| 2014 | 9.82 | 5.17 | 53% | 2.30 | 23% |
| 2015 | 5.48 | 2.15 | 39% | 1.48 | 27% |
| 2016 | 4.21 | 1.01 | 24% | 1.27 | 30% |
| 2017 | 5.80 | 1.00 | 17% | 2.11 | 36% |
| 2018 | 6.31 | 1.95 | 31% | 1.63 | 26% |
| 2019 | 7.82 | 2.83 | 36% | 1.66 | 21% |

*Source: UN Comtrade monthly data, summed by year [@un_comtrade_2026]. Author's calculations (Script 42). Annual totals for 2011 and 2019 differ slightly from the annual panel because of later revisions.*

This makes oil the main omitted variable in the annual models. Annual bilateral HS 27 data are not available for 2000–2009 in the dataset used here, so the annual models cannot control for it. The monthly models can, and they do (§6.18, Model M4).


## 4.7 Data Validation: A Reporting Break in Kazakhstan's Imports from China, 2020–2022

While building the monthly dataset, Kazakhstan-reported trade with China (UN Comtrade, Kazakhstan as reporter) was compared month by month with China's own customs records (China as reporter, the "mirror" data). For 2010–2019 the monthly Kazakhstan-reported series adds up exactly to the annual panel values, which confirms the panel's construction. The comparison also shows a break in the import series.

**Table 4.6. Kazakhstan-Reported Imports from China vs. China-Reported Exports to Kazakhstan (USD bn)**

| Year | Kazakhstan-reported imports | China-reported exports to Kazakhstan | Ratio (China / Kazakhstan) | Months with HS 84/85/87 import records | Mirror-adjusted imports |
|---|---:|---:|---:|---:|---:|
| 2013 | 8.36 | 12.55 | 1.50 | 12 | 8.36 |
| 2014 | 7.37 | 12.71 | 1.73 | 12 | 7.37 |
| 2015 | 5.09 | 8.44 | 1.66 | 12 | 5.09 |
| 2016 | 3.67 | 8.29 | 2.26 | 12 | 3.67 |
| 2017 | 4.69 | 11.56 | 2.46 | 12 | 4.69 |
| 2018 | 5.38 | 11.35 | 2.11 | 12 | 5.38 |
| 2019 | 6.57 | 12.73 | 1.94 | 12 | 6.57 |
| **2020** | **1.96** | 11.70 | **5.99** | **0** | **5.41** |
| **2021** | **2.42** | 13.76 | **5.67** | **0** | **6.36** |
| **2022** | **3.58** | 16.36 | **4.57** | **0** | **7.56** |
| 2023 | 16.77 | 24.70 | 1.47 | 12 | 16.77 |

*Source: UN Comtrade monthly and annual data, both reporters [@un_comtrade_2026]. Author's calculations (`import_break_evidence.csv`, Script 43). China reports exports FOB and Kazakhstan reports imports CIF; mirror gaps are normal in Central Asian trade, so the level of the ratio is not the issue. The issue is its sudden change. Mirror-adjusted imports = China-reported exports × 0.462, the pooled Kazakhstan/China ratio for 2016–2019.*

Three facts point to a reporting problem rather than a real collapse in imports:

1. Between 2013 and 2019, China's reported exports to Kazakhstan were consistently 1.5 to 2.5 times Kazakhstan's reported imports from China. In 2020–2022 the ratio jumps to 4.6–6.0 and then returns to 1.5 in 2023.
2. Kazakhstan-reported imports fall by about 70 per cent in 2020 (USD 6.57 bn to 1.96 bn in the monthly records; 6.79 bn to 1.96 bn in the annual panel), while China-reported exports to Kazakhstan fall by only 8 per cent (USD 12.73 bn to 11.70 bn).
3. In 2020–2022 the Kazakhstan-reported monthly records contain no HS 84 (machinery), 85 (electrical equipment) or 87 (vehicles) import rows, although these chapters are present in every month of 2010–2019 and 2023. These are the chapters most likely to be affected by changes in reporting or confidentiality practice.

The cause of the break cannot be confirmed from the data. Plausible explanations include a change in how imports were attributed by partner country, confidentiality suppression of detailed chapters, or a change in how trade within the Eurasian Economic Union customs territory was recorded. Whatever the cause, the consequence for this thesis is direct. The annual panel's 2020–2022 trade balances (USD 4.88, 4.43 and 6.89 bn) are almost certainly overstated, and the jump from 2022 to 2023 (USD 6.89 bn to −2.01 bn) is partly a return to complete reporting rather than a pure change in trade. Kazakhstan-reported exports show a smaller widening of the mirror gap over the same years (China/Kazakhstan ratio 1.42–1.65 in 2020–2022, against 1.10–1.28 in 2016–2019). §6.20 therefore reports sensitivity checks that adjust imports only, and both flows.

![Figure 4.1. Kazakhstan's Imports from China: Own Reports vs. China's Mirror Data](../Outputs/generated_figures/fig_import_reporting_break.png)
*Source: UN Comtrade. Author's construction (Script 43).*

# 5. Empirical Strategy

## 5.1 Baseline OLS Association Model

The baseline specification is:

$$TB_t = \alpha + \beta_1 \text{Minerals}_t + \beta_2 \text{PostBRI}_t + \beta_3 (\text{Minerals}_t \times \text{PostBRI}_t) + \gamma' Z_t + \varepsilon_t$$

where $Z_t$ includes Brent crude price, KZT/USD exchange rate, and optionally GDP controls. Standard errors are computed using the Newey–West [-@newey_west_1987] HAC estimator with bandwidth 3. The coefficient of interest is $\beta_3$: a negative value indicates that the trade-balance payoff of mineral exports weakened in the post-BRI period, consistent with the asymmetric interdependence prediction in H3 (§3.5).

Each regressor is theoretically anchored as follows (see also Table 3.1 for the full mapping):

**`minerals_narrow` (USD bn).** This variable operationalises Hirschman's [-@hirschman_1945] trade-concentration mechanism. A larger mineral export share increases export revenues and should improve the bilateral trade balance in the pre-BRI baseline, yielding a *positive* predicted sign on $\beta_1$. The interaction $\beta_3$ tests whether this payoff changed post-BRI, with asymmetric interdependence theory predicting a *negative* coefficient as import deepening outpaces mineral revenue growth.

**`post_bri_2013` (0/1).** This period indicator tests whether the bilateral trade balance shifted structurally after the BRI announcement in September 2013. Keohane and Nye's sensitivity mechanism predicts a *negative* level shift as the post-BRI period coincides with Chinese manufactured exports into Kazakhstan expanding faster than Kazakh mineral exports to China. The coefficient $\beta_2$ is a net level shift that subsumes multiple concurrent shocks (oil-price collapse, tenge devaluation, COVID-19) and is therefore interpreted as suggestive rather than causal.

**`brent_annual_mean` (USD/bbl).** This variable operationalises the resource-curse / terms-of-trade channel identified by van der Ploeg [-@vanderploeg_2011] and Corden and Neary [-@corden_neary_1982]. Higher global oil prices increase Kazakhstan's commodity export revenues, predicting a *positive* sign; however, they may also appreciate the real exchange rate and expand import-financing capacity, introducing ambiguity. The expected sign is therefore *positive but uncertain*.

**`kzt_usd` (tenge per USD).** This variable operationalises the competitiveness channel from standard open-economy macroeconomics. A higher KZT/USD value (tenge depreciation) makes Kazakh exports cheaper in dollar terms and Chinese imports more expensive, predicting a *positive* effect on the bilateral trade balance via the Marshall–Lerner condition. The Bhagwati [-@bhagwati_1958] immiserising-growth caveat applies: if depreciation also compresses import demand for Chinese capital goods on which Kazakh industries depend, the effect may be partially self-limiting.

**`log(KZ GDP)` and `log(CN GDP)` (levels).** These variables operationalise domestic absorption (KZ) and foreign demand (CN) from Anderson and van Wincoop's [-@anderson_vanwincoop_2003] gravity framework. However, both GDP series grow monotonically over 2000–2023, producing near-perfect multicollinearity (VIF = 130.9 and 236.3, respectively). Monotonic trending regressors in a 24-observation sample absorb the time trend and destabilise all other coefficient estimates. These variables are therefore **excluded from the primary specification** and retained only in the pre-revision specification in Appendix B.

**`d.log(KZ GDP)` and `d.log(CN GDP)` (annual growth rates) — primary.** The primary specification replaces GDP levels with annual log-difference growth rates, which are stationary, achieve max VIF = 10.4 (the only specification meeting the VIF < 10 target), and operationalise year-on-year income dynamics. One observation is lost to differencing (n = 23). See §6.3.

**`log(CN GDP / KZ GDP)` (gravity ratio) — robustness.** Following the methodological guidance of Anderson and van Wincoop [-@anderson_vanwincoop_2003], the gravity ratio operationalises bilateral size asymmetry and is retained as a robustness check. It reduces max VIF from 236.3 to 33.4 — a large improvement but still above the VIF < 10 target (§6.3; Appendix B).

**Interpretation constraint:** The model does not identify a causal BRI effect. PostBRI is a period indicator that coincides with multiple concurrent shocks (oil price collapse, tenge devaluation, Crimea-related trade disruption, COVID-19). All coefficients are interpreted as conditional associations. Causal language is reserved for the triple-concordance criterion: a finding is described as "causal" only where the DiD partner-placebo estimate (§6.15), the synthetic counterfactual gap (§6.16), and the sanctions-robustness check (§6.14) all point in the same direction.

## 5.2 Full vs. Parsimonious vs. Growth-Rate Specifications

Three specification families are reported:

- **Pre-revision full model (A1):** 7 regressors including log(KZ GDP) and log(CN GDP) — retained in Appendix B for transparency. Max VIF > 100. *Not used for primary interpretation.*
- **Pre-revision parsimonious model (A2):** 5 regressors excluding GDP controls. Max VIF < 10. Used for primary interpretation in the midterm version.
- **Primary growth-rate model (B) [main specification]:** Replaces both GDP levels with d.log(KZ GDP) and d.log(CN GDP). Stationary, max VIF = 10.4 — the only specification substantially meeting the VIF < 10 target. **This is the primary specification in the final version.** See §6.3 and Appendix B.
- **Robustness gravity-ratio model (C):** Replaces both GDP levels with log(CN GDP/KZ GDP). Theoretically grounded in Anderson and van Wincoop [-@anderson_vanwincoop_2003]. Max VIF = 33.4 — substantial improvement over A1, does not meet VIF < 10 target. Retained as robustness check.

The growth-rate specification is the primary model because it is the only specification that substantially meets the VIF < 10 collinearity threshold (§6.3). Coefficient direction and approximate magnitude are consistent across all full-sample specifications (B and C), supporting the directional interpretation, while exact magnitudes should not be over-interpreted given residual collinearity in Scheme C.

## 5.3 ADL Dynamic Association Model

Prior to estimating the ADL model, stationarity diagnostics were conducted. Because *n* = 24, unit-root tests have inherently low power, so these diagnostics are used to guide model choice (ARDL) rather than to definitively prove integration order.

**Table 5.1. Stationarity and Integration Order Diagnostics**

| Variable | ADF Stat | ADF *p* | PP Stat | PP *p* | KPSS Stat | KPSS *p* | Inferred Order |
|----------|----------|---------|---------|--------|-----------|----------|----------------|
| Trade Balance | −2.09 | 0.247 | −0.89 | 0.958 | 0.11 | >0.10 | Ambiguous |
| Minerals Narrow | −1.63 | 0.467 | −1.17 | 0.917 | 0.10 | >0.10 | Ambiguous |
| Brent Crude | −2.21 | 0.204 | −1.65 | 0.773 | 0.13 | 0.072 | Ambiguous |
| KAZ GDP | −1.56 | 0.506 | −1.64 | 0.777 | 0.17 | 0.027 | I(1) |
| BRI Intensity | −4.08 | 0.001 | −2.91 | 0.160 | 0.19 | 0.021 | Ambiguous |

*Note: Author's calculations. ADF and PP test H₀: unit root. KPSS tests H₀: stationarity. Low power at n = 24 is acknowledged; diagnostics guide model selection rather than definitively establishing integration orders. Diagnostics for additional series (copper price, log China GDP, log minerals) are qualitatively similar and are available from the author on request.*

Given the mixed and ambiguous integration orders (I(0) and I(1)), the bounds testing approach is appropriate. The AIC-selected autoregressive distributed lag (ADL) model is estimated to capture dynamic associations. Following Pesaran, Shin, and Smith [-@pesaran_shin_smith_2001], the bounds test is applied to assess cointegration. If the PSS F-statistic falls below the upper bound, the results are interpreted as short-run dynamic associations rather than long-run equilibrium estimates.

## 5.4 Robustness Strategy

Robustness is assessed through: (i) a 288-specification grid varying mineral measures (narrow/broad), BRI variables (dummy/intensity), lag structures, and estimators; (ii) leave-one-out coefficient stability analysis; (iii) WITS-consistent mineral proxy for the full 2000–2023 period; (iv) exclusion of 2023.


## 5.5 Sample Size and the High-Frequency Strategy

The annual sample contains 24 observations, and the primary specification estimates eight parameters on 23 of them. This leaves 15 residual degrees of freedom, which limits statistical power and makes heteroskedasticity- and autocorrelation-consistent (HAC) inference less reliable than it is in large samples. Two routes to a larger sample were considered.

**Route 1: temporal disaggregation of the annual data (robustness only).** Each annual series can be split into quarters (*n* = 96) or months (*n* = 288) with a benchmarking method such as Denton [-@denton_1971] or Chow and Lin [-@chow_lin_1971], which produces a smooth high-frequency path whose sub-periods add up to the published annual totals. This is common practice in national accounting, but it does not add information for hypothesis testing: every interpolated quarter is a deterministic function of the 24 annual totals. The interpolation also induces strong residual autocorrelation, so conventional standard errors understate uncertainty. The thesis therefore reports a Denton-interpolated quarterly model (§6.17) together with a Monte Carlo experiment that measures how often interpolation produces "significant" results between series that are unrelated by construction.

**Route 2: observed monthly data (preferred).** UN Comtrade publishes monthly bilateral trade by HS chapter for Kazakhstan and China from January 2010. Monthly Kazakhstan-reported exports and imports, strategic mineral exports (HS 26 + 28, the same chapter definition used for the annual mineral variable from 2014), and bilateral oil and energy exports (HS 27) were retrieved from the Comtrade public API. They were combined with the National Bank of Kazakhstan's official KZT/USD rate (monthly average of rates sampled every three days) and World Bank Pink Sheet monthly Brent and copper prices. These are 120 genuinely observed months for 2010M01–2019M12 (48 pre-BRI and 72 post-BRI). The monthly model is:

$$TB_m = \alpha + \beta_1 \text{Minerals}_m + \beta_2 \text{PostBRI}_m + \beta_3 (\text{Minerals}_m \times \text{PostBRI}_m) + \gamma_1 \text{Brent}_m + \gamma_2 \text{KZT}_m + \sum_{k=2}^{12}\delta_k D_k + \varepsilon_m$$

where $D_k$ are calendar-month dummies that absorb seasonality. Standard errors are Newey–West HAC with 12 lags, and *p*-values use the *t* distribution with the residual degrees of freedom. GDP is not observed monthly, so the monthly model mirrors the parsimonious annual specification (A2). Robustness variants add a linear trend, the copper price, or bilateral oil and energy exports, and they move the break to October 2013 (one month after the Astana speech).

**Why the primary monthly sample ends in 2019.** Kazakhstan-reported imports from China show a reporting break in 2020–2022 (§4.7). The primary monthly sample therefore uses one consistent source up to December 2019. Samples extended to 2023, with imports as reported and with mirror-adjusted imports, are reported as robustness checks.

## 5.6 Hypothesis Testing Procedure and Model Fit

Each hypothesis is tested formally with a stated null (H₀) and alternative (H₁). Because H1–H3 predict a direction, the decision uses a one-sided HAC *t*-test at the 5 per cent level; two-sided *p*-values are also reported.

| Hypothesis | H₀ | H₁ | Test |
|---|---|---|---|
| H1: post-BRI level shift | $\beta_2 \ge 0$ | $\beta_2 < 0$ | one-sided HAC *t*-test |
| H2: pre-BRI mineral payoff | $\beta_1 \le 0$ | $\beta_1 > 0$ | one-sided HAC *t*-test |
| H3: weaker payoff after BRI | $\beta_3 \ge 0$ | $\beta_3 < 0$ | one-sided HAC *t*-test |
| Joint post-BRI change | $\beta_2 = \beta_3 = 0$ | at least one $\neq 0$ | HAC Wald *F*-test |
| Post-BRI mineral slope | $\beta_1 + \beta_3 = 0$ | $\beta_1 + \beta_3 \neq 0$ | HAC *t*-test on the linear combination |

Every model is reported with the same fit statistics: *R*², adjusted *R*², the *F*-test of joint significance (classical and HAC-robust), log-likelihood, AIC, BIC, the standard error of the regression (RMSE), and the Durbin–Watson, Breusch–Godfrey, Breusch–Pagan, Jarque–Bera and Ramsey RESET diagnostics.

**Granger causality.** To address the direction of association, bivariate Granger causality tests [@granger_1969] are run in both directions between the trade balance and strategic mineral exports, and at annual frequency also between the trade balance and BRI financing intensity. Because unit-root tests give mixed results, two versions are reported: a VAR in first differences, and the Toda and Yamamoto [-@toda_yamamoto_1995] procedure, which estimates the VAR in levels with one extra lag and tests only the original lags. This keeps the Wald statistic valid whether the series are I(0) or I(1). Lag length is selected by AIC and BIC. Granger causality is a test of predictive precedence: whether past values of one series improve the forecast of another. It is not a test of causation in the structural sense, and it is interpreted that way here.

# 6. Results

**How to read this chapter.** The chapter reports many checks. They do not carry equal weight, and this table states in advance which results the conclusions rest on.

| Role | Evidence | Sections |
|---|---|---|
| **Core** | Descriptive decomposition of exports, imports and the balance | §4.5 |
| **Core** | Primary annual model (B): fit statistics and formal tests of H1–H3 | §6.1, §6.11 |
| **Core** | Observed monthly models, 2010–2019 | §6.18 |
| **Core** | Data validation: 2020–2022 import reporting break and sensitivity | §4.7, §6.20 |
| Qualifying | Oil-export control (removes the monthly interaction); Granger tests (no evidence that minerals lead the balance) | §6.18, §6.19 |
| Supporting | Cross-partner DiD (largest decline for China; imprecise with six partners) | §6.15 |
| Robustness only | Multicollinearity schemes, influence and leave-one-out, WITS proxy, ADL, robustness grid, placebo breaks, sanctions exclusion, synthetic control, interpolated quarters | §6.2–6.8, §6.13–6.14, §6.16–6.17 |


## 6.1 Baseline OLS Results

**Table 6.1. OLS Regression Results: Full and Parsimonious Models**

| Variable | A1 Coef. | A1 HAC SE | A1 *p* | A2 Coef. | A2 HAC SE | A2 *p* |
|----------|------:|------:|------:|------:|------:|------:|
| Constant | 197.624 | (53.040) | 0.002*** | −3.326 | (2.359) | 0.176 |
| Minerals (USD bn) | 2.463 | (0.541) | 0.000*** | 1.694 | (0.853) | 0.062* |
| Brent (USD/bbl) | 0.047 | (0.039) | 0.239 | 0.023 | (0.037) | 0.542 |
| KZT/USD | 0.016 | (0.012) | 0.198 | 0.014 | (0.012) | 0.270 |
| log(KZ GDP) | −13.230 | (6.112) | 0.046** | — | — | — |
| log(CN GDP) | 4.529 | (4.460) | 0.325 | — | — | — |
| Post-BRI | 4.927 | (1.847) | 0.017** | 0.691 | (1.492) | 0.649 |
| Minerals × Post-BRI | **−3.221** | **(1.043)** | **0.007***| **−2.382** | **(0.977)** | **0.025**|
| | | | | | | |
| N | 24 | | | 24 | | |
| R² | 0.765 | | | 0.703 | | |
| Adj. R² | 0.661 | | | 0.620 | | |
| Durbin–Watson | 1.799 | | | 1.739 | | |

*Notes: HAC (Newey–West) standard errors in parentheses, bandwidth = 3. Sample: 2000–2023 (*n* = 24). Significance: \*p<0.10, \*\*p<0.05, \*\*\*p<0.01. A1 = full model (7 regressors including log Kazakhstan GDP and log China GDP); A2 = parsimonious model (no GDP controls). Standard errors are heteroskedasticity- and autocorrelation-consistent (HAC) throughout, as motivated by the Breusch–Pagan test result (§6.2).*

In the full model, the minerals coefficient (2.46, *p* < 0.001) indicates that, during the pre-BRI period, each additional USD billion of mineral exports was associated with approximately USD 2.46 billion higher bilateral trade balance. The interaction term (−3.22 with HAC SE of 1.043, *p* = 0.007) suggests that this positive association weakened substantially in the post-BRI period. However, the large constant (197.6) and the signs on the GDP terms indicate that the model absorbs trend dynamics through GDP controls, and the severe multicollinearity (VIF > 100 for both GDP variables; see §6.3) renders these full-model coefficients unreliable as structural estimates.

The parsimonious model (A2) is therefore preferred for substantive interpretation. By removing the collinear GDP controls, all remaining VIF values fall below 10, and the interaction estimate of −2.38 (HAC SE = 0.977, *p* = 0.025) is more stable. The Post-BRI level shift becomes statistically insignificant (*p* = 0.649), confirming that the period dummy's apparent significance in A1 was driven by GDP collinearity rather than a genuine level shift in the trade balance. All results in this table are conditional associations only. No coefficient in either model should be interpreted as a causal estimate: PostBRI is a period indicator that coincides with the oil-price collapse, the tenge devaluation, and the COVID-19 shock alongside BRI-related infrastructure changes.

![Figure 4. Strategic Mineral Exports vs Bilateral Trade Balance, Pre-BRI vs Post-BRI](../Outputs/generated_figures/fig_4_scatter.png)
*Source: Author's construction. Figure 4 plots the relationship between mineral exports and the trade balance across the two periods, visualising the weakened association post-BRI.*

**Table 6.1b. Model Fit Statistics for the Annual Association Models**

| Statistic | B (primary) | C (gravity ratio) | A2 (parsimonious) |
|---|---:|---:|---:|
| N | 23 | 24 | 24 |
| Regressors (excl. constant) | 7 | 6 | 5 |
| *R*² | 0.742 | 0.703 | 0.703 |
| Adjusted *R*² | 0.621 | 0.598 | 0.620 |
| *F* (classical), *p* | 6.15, 0.002 | 6.70, 0.001 | 8.51, <0.001 |
| HAC Wald *F*, *p* | 32.35, <0.001 | 31.65, <0.001 | 21.84, <0.001 |
| Log-likelihood | −42.93 | −46.27 | −46.27 |
| AIC | 101.86 | 106.54 | 104.54 |
| BIC | 110.94 | 114.79 | 111.61 |
| Standard error of regression (USD bn) | 1.94 | 1.98 | 1.92 |
| Durbin–Watson | 1.65 | 1.73 | 1.74 |
| Breusch–Godfrey LM (2 lags), *p* | 8.85, 0.012 | 0.48, 0.785 | 0.44, 0.802 |
| Breusch–Pagan LM, *p* | 20.00, 0.006 | 19.94, 0.003 | 19.60, 0.002 |
| Jarque–Bera, *p* | 0.03, 0.987 | 0.01, 0.994 | 0.02, 0.992 |
| Ramsey RESET *F*, *p* | 0.06, 0.814 | 2.50, 0.134 | 2.61, 0.125 |

*Source: Author's calculations (`Outputs/generated_tables/model_fit_statistics.csv`, Script 40). Sample 2000–2023; Model B loses 2000 to differencing.*

**Reading the fit statistics.** In the primary model the regressors jointly explain 74.2 per cent of the year-to-year variation in the bilateral balance (62.1 per cent after the degrees-of-freedom adjustment), and the joint *F*-test rejects the null that all slope coefficients are zero (*F* = 6.15, *p* = 0.002). The typical prediction error is about USD 1.9 billion, against a mean balance of USD 2.9 billion over the sample, so the model explains the broad pattern but not individual years precisely. By AIC and BIC, Model B fits best of the three. The diagnostics justify the inference choices. Breusch–Pagan rejects homoskedasticity in all three models, which is why HAC standard errors are used throughout. Breusch–Godfrey detects residual autocorrelation in Model B (*p* = 0.012) but not in Models C or A2. Residuals are close to normal (Jarque–Bera *p* > 0.98), and RESET finds no evidence of omitted non-linearity at the 10 per cent level.

One caution applies to every annual *p*-value. A Monte Carlo experiment (§6.17, Table 6.13) shows that HAC tests with *n* = 24 and persistent regressors reject a true null about 21 per cent of the time at a nominal 5 per cent level, which is consistent with known small-sample size distortions of HAC tests [@kiefer_vogelsang_bunzel_2000]. Annual results near the 5 per cent threshold should therefore be read as suggestive.

## 6.2 Residual Diagnostics

**Table 6.2. Residual Diagnostics**

| Test | Statistic | *p*-value | Interpretation |
|------|-----------|-----------|---------------|
| Durbin–Watson | 1.799 | — | Mild positive autocorrelation; inconclusive |
| Breusch–Pagan | 19.78 | 0.006 | Heteroskedasticity detected |

*Note: Table 6.2 reports diagnostics for the full model (A1) from the original analysis. Diagnostics for the primary model (B) and for Models C and A2 are reported in Table 6.1b.*

The Breusch–Pagan test rejects the null of homoskedasticity (*p* = 0.006), which motivates the use of HAC standard errors throughout. HAC standard errors correct for both heteroskedasticity and autocorrelation in inference, but do not address potential model misspecification. The Durbin–Watson statistic (1.80) is close to 2.0, suggesting that serial correlation is mild after conditioning on regressors.

## 6.3 Multicollinearity Diagnostics and Resolution

Three variable schemes were evaluated to address the severe multicollinearity in the GDP levels specification:

**Table 6.3a. VIF Comparison Across Specification Schemes**

| Variable | Scheme A (GDP levels) | Scheme B (GDP growth) | Scheme C (Gravity ratio) |
|----------|----------------------:|----------------------:|-------------------------:|
| MIN (minerals) | 12.4 | 6.8 | 10.8 |
| BRENT | 5.7 | 4.4 | 4.9 |
| KZT/USD | 17.8 | 8.3 | 17.7 |
| log(KZ GDP) | **130.9** | — | — |
| log(CN GDP) | **236.3** | — | — |
| d.log(KZ GDP) growth | — | 2.6 | — |
| d.log(CN GDP) growth | — | 3.4 | — |
| log(CN/KZ GDP ratio) | — | — | 33.4 |
| POST dummy | 28.9 | 10.4 | 21.9 |
| POST × MIN | 16.0 | 9.7 | 13.7 |
| **Max VIF** | **236.3** | **10.4** | **33.4** |

*Note: Scheme A = pre-revision specification (retained in Appendix B). Scheme B = GDP annual growth rates (primary). Scheme C = gravity ratio log(CN GDP/KZ GDP) (robustness).*

**Scheme A (pre-revision)** has GDP-level VIFs of 130.9 and 236.3 — severe. This is the specification moved to Appendix B.

**Scheme B (growth rates) — primary specification.** Replacing GDP levels with annual log-difference growth rates reduces maximum VIF to 10.4, the only specification that substantially meets the VIF < 10 target. Growth rates are stationary, theoretically defensible (controlling for year-on-year income dynamics rather than trend levels), and eliminate the trending-variable collinearity. One year of observations is lost to differencing (n = 23). This specification is adopted as the primary model.

**Scheme C (gravity ratio) — robustness check.** Replacing the two GDP-level variables with log(CN GDP/KZ GDP) reduces maximum VIF from 236.3 to 33.4 — a large improvement, but still well above the VIF < 10 threshold. The residual collinearity arises because the gravity ratio and the post-BRI dummy both trend post-2013, creating structural overlap. Scheme C is theoretically motivated by Anderson and van Wincoop (2003) and is retained as a robustness check because it operationalises bilateral size asymmetry and preserves all 24 observations, but it does not resolve the multicollinearity problem and is **not** the primary specification.

**Table 6.3b. Coefficient Stability Across Schemes**

| Scheme | N | Interaction β | HAC SE | *p*-value | Max VIF |
|--------|---|---:|---:|---:|---:|
| A: GDP levels (pre-revision) | 24 | −3.220 | 1.043 | 0.002 | 236.3 |
| **B: GDP growth rates (primary)** | **23** | **−2.489** | **0.974** | **0.011** | **10.4** |
| B: Growth rates, excl. 2022–2023 | 21 | −0.012 | 0.283 | 0.966 | 10.4 |
| B: Growth rates, excl. 2023 | 22 | +0.065 | 0.239 | 0.785 | 10.4 |
| C: Gravity ratio (robustness) | 24 | −2.419 | 1.131 | 0.033 | 33.4 |
| C: Gravity ratio, excl. 2022–2023 | 22 | +0.102 | 0.432 | 0.813 | 33.4 |
| C: Gravity ratio, excl. 2023 | 23 | +0.307 | 0.449 | 0.494 | 33.4 |

The interaction coefficient is stable at approximately −2.4 to −2.5 across both full-sample schemes, confirming the collinearity inflated Scheme A (−3.22) but did not fundamentally alter the directional conclusion. Critically, both Scheme B and Scheme C lose significance when 2022–2023 are excluded — confirming the sanctions-robustness concern in §6.14 is structural, not an artefact of the specification choice.

**Table 6.3c. Primary Specification (Scheme B: GDP Growth Rates): Key Results**

| Variable | Notes |
|---|---|
| Minerals Narrow (USD bn) | Mineral export level (pre-BRI association) |
| d.log(KZ GDP) | Annual growth rate; stationary; VIF=2.63 |
| d.log(CN GDP) | Annual growth rate; stationary; VIF=3.36 |
| Brent (USD/bbl) | Global commodity price control |
| KZT/USD | Exchange rate control |
| Post-BRI (0/1) | Period indicator; VIF=10.43 |
| **Minerals × Post-BRI** | **−2.489 (HAC SE=0.974, *p*=0.011) — primary coefficient** |
| N | 23 (2001–2023; one obs. lost to differencing) |
| R² | 0.742 |
| Max VIF | 10.4 |
| HAC bandwidth | 3 (Newey–West) |

*Source: Author's calculations.*

**Why Scheme B is the primary specification.** The growth-rate specification is adopted as primary because: (i) it is the only scheme that substantially meets the VIF < 10 collinearity threshold (max VIF = 10.4, driven by the POST dummy); (ii) GDP growth rates are stationary, removing the trending-variable collinearity that destabilises levels-based inference; (iii) annual growth rates operationalise the income-dynamics channel (year-on-year demand and capacity changes) consistently with the underlying theory. The one-observation cost (n = 23 vs. 24) is the only trade-off relative to Scheme C.

**Remaining collinearity note.** The POST variable retains VIF = 10.4, just above the conventional threshold of 10. This is because the post-BRI dummy is correlated with the trend component in GDP growth rates post-2013. Coefficient magnitudes in Scheme B should still be interpreted directionally rather than as precise structural parameters, but the reduced collinearity severity relative to Schemes A and C substantially improves inference reliability.

## 6.4 Influence Diagnostics and the Role of 2023

This section addresses the most important empirical vulnerability in the thesis. Influence diagnostics reveal that the headline interaction coefficient is heavily dependent on the 2023 observation.

**Table 6.4. Influential Observations (Cook's Distance)**

| Year | Cook's D | Leverage | Flag |
|------|----------|----------|------|
| 2000 | 0.220 | 0.657 | ⚠️ |
| 2014 | 0.599 | 0.715 | ⚠️ |
| 2020 | 0.275 | 0.318 | ⚠️ |
| 2022 | 0.553 | 0.484 | ⚠️ |
| **2023** | **3.898** | **0.697** | **⚠️⚠️** |

*Cook's D threshold (4/n): 0.167. Flagged years exceed threshold.*

The 2023 observation has a Cook's distance of 3.90—more than 23 times the conventional 4/*n* threshold of 0.167 and seven times larger than any other observation. This is the only year in the sample with a negative bilateral trade balance (−USD 2.01 billion), driven by an unprecedented import surge to USD 16.77 billion. The studentised residual for 2023 is −9.18, indicating an extreme outlier. Part of this influence is a data artefact: Kazakhstan-reported imports are under-recorded in 2020–2022 (§4.7), which inflates the 2020–2022 balances and exaggerates the contrast with 2023. With mirror-adjusted imports, the Cook's distance of 2023 falls to 2.32 and the interaction survives its exclusion (§6.20).

**Table 6.5. Model Stability: Full Sample vs. Excluding 2023**

| Model | Sample | Interaction β | SE | *p* | R² |
|-------|--------|------:|------:|------:|------:|
| Full (A1) | 2000–2023 (n=24) | −3.221 | 1.043 | 0.007 | 0.765 |
| Parsimonious (A2) | 2000–2023 (n=24) | −2.382 | 0.977 | 0.025 | 0.703 |
| Full, excl. 2023 (A3) | 2000–2022 (n=23) | −0.407 | 0.288 | 0.178 | 0.960 |
| Parsimonious, excl. 2023 (A4) | 2000–2022 (n=23) | +0.401 | 0.257 | 0.137 | 0.928 |
| WITS proxy (A5) | 2000–2023 (n=24) | −2.965 | 0.689 | 0.000 | 0.829 |
| WITS, excl. 2023 (A6) | 2000–2022 (n=23) | −1.874 | 1.017 | 0.083 | 0.832 |

*Notes: HAC standard errors. WITS models use parsimonious specification with consistent Ores and Metals proxy.*

These results demonstrate four key findings:

1. **Excluding 2023 eliminates statistical significance** in the full model (A3: *p* = 0.178) and reverses the sign in the parsimonious model (A4: β = +0.40). This sign reversal is critical: it implies that once both the GDP controls (which inflate variance) and the 2023 observation (the outlier deficit) are removed, the negative interaction entirely collapses. Therefore, the thesis does not claim a robust structural negative interaction; the stronger contribution is the descriptive decomposition and diagnostic evidence of trade-balance fragility.
2. **The full-sample interaction is driven primarily by one observation.** The leave-one-out analysis confirms that no other year's exclusion changes the sign or significance of the interaction.
3. **The WITS-consistent proxy partially preserves significance even excluding 2023** (A6: −1.87, *p* = 0.083), suggesting that measurement-break issues in the narrow mineral variable may compound the instability.
4. **The R² rises dramatically when 2023 is excluded** (from 0.765 to 0.960), indicating that 2023 introduces substantial unexplained variance.

**Interpretation.** The negative interaction is not a stable structural finding. Rather, 2023 represents a potential inflection point—the first year of bilateral deficit—that dramatically amplifies the estimated post-BRI deterioration. The thesis interprets the evidence as diagnostic: the data are consistent with an increasingly adverse trade-balance pattern, but the statistical evidence for a systematic post-BRI interaction effect depends on whether 2023 represents the beginning of a new structural pattern or a one-time shock.

## 6.5 Leave-One-Out Coefficient Stability

![Figure 5. Influence and Leave-One-Out Diagnostics](../Outputs/generated_figures/fig_5_diagnostics.png)
*Source: Author's construction. Figure 5(d) plots the interaction coefficient from 24 leave-one-out regressions.*

Figure 5 plots the influence diagnostics, including the interaction coefficient from 24 leave-one-out regressions in panel (d). Excluding any year other than 2023 produces interaction coefficients between −2.64 and −3.88, all statistically significant at the 5% level. Excluding 2023 alone reduces the coefficient to −0.41 and renders it insignificant. This confirms that the full-sample result is robust to all observations except 2023.

## 6.6 WITS Consistent-Proxy Robustness

To address the measurement break (Section 4.3), a robustness check replaces the narrow mineral variable with WITS Ores and Metals exports, which are available from a single source for the entire 2000–2023 period. The WITS proxy is broader than the targeted narrow definition, but avoids source-switching at 2014. Results (Table 6.5, Models A5–A6) show that the WITS-based interaction is −2.97 (*p* < 0.001) in full sample and −1.87 (*p* = 0.083) excluding 2023—marginally significant. This suggests that measurement consistency partially mitigates the 2023 sensitivity, though the interaction remains fragile.

## 6.7 ADL Dynamic Association Results

The dynamic model was re-estimated in the final audit on observed variables only (Script 45). The earlier version included an annual "oil exports" regressor that was a placeholder equal to 55 per cent of total exports in every year, not observed data; that placeholder has been removed from the dataset (§6.12).

**Table 6.5b. ADL and Bounds-Test Results (Observed Variables Only)**

| Control set | AIC-selected lags | Interaction β₃ | *p* | PSS bounds *F* | *p* (I(1) upper bound) |
|---|---|---:|---:|---:|---:|
| A2 (minerals, Brent, KZT/USD) | No lag of the balance; Brent lag 1 | −2.304 | 0.003 | 2.22 | 0.443 |
| B (A2 + GDP growth rates) | No lag of the balance; one regressor lag | −2.364 | 0.001 | 2.01 | 0.520 |

*Notes: Lags selected by AIC with a maximum of one (n = 24). HAC standard errors. Bounds test of Pesaran, Shin and Smith (2001), case 3. Source: `ardl_clean.csv`, Script 45.*

Two results follow. First, the AIC selects no lagged trade balance, so the dynamic model reduces to the static model with one lagged regressor. The interaction (−2.30 to −2.36) is therefore close to the static estimate, and the ADL adds little beyond it. Second, the bounds test does not reject the null of no long-run (cointegrating) relationship (*p* = 0.44–0.52), so the results are interpreted as short-run associations, as before.

**Stability.** CUSUM and CUSUM-of-squares tests on recursive residuals of the parsimonious model (Figures 6a and 6b) can only be computed from 2016 onwards, because the post-BRI regressors are zero before 2014. The CUSUM path stays within the 5 per cent bounds, so there is no evidence of drifting coefficients. The CUSUM of squares leaves the bounds in 2020–2022 and jumps in 2023 (`stability_clean.csv`), which points to unstable error variance in exactly the years affected by the import reporting break (§4.7).

![Figure 6a. CUSUM Test, Parsimonious Model](../Outputs/generated_figures/fig_cusum_clean.png)
*Note: CUSUM of recursive residuals with 5% bounds. Author's construction (Script 45).*

![Figure 6b. CUSUM of Squares Test, Parsimonious Model](../Outputs/generated_figures/fig_cusum_squares_clean.png)
*Note: CUSUM of squares with 5% bounds. Author's construction (Script 45).*

## 6.8 Robustness Grid Summary

To systematically evaluate the fragility of the findings, a 288-specification robustness grid was estimated across different mineral measures, lag structures, estimators, and BRI dummy variants. 

**Table 6.6. Robustness Grid Summary**

| Metric | Count / Percentage |
|--------|-------------------|
| Total specifications | 288 |
| Converged successfully | 190 |
| Skipped / Data unavailable | 98 |
| Negative and significant (*p* < 0.05) | 157 (82.6% of converged) |
| Negative and insignificant (*p* ≥ 0.05) | 22 (11.6% of converged) |
| Positive or sign-reversed | 11 (5.8% of converged) |

*Source: Author's calculations.*

![Figure 6. Model Comparison and Robustness](../Outputs/generated_figures/fig_6_pre_post.png)
*Source: Author's construction. Figure 6 summarises the pre- and post-BRI coefficient instability across specifications.*

While 82.6% of the converged specifications yielded a negative and significant interaction, this consistency reflects the fact that most specifications include the 2023 observation. The grid confirms that the full-sample negative association is computationally robust across model types, but as demonstrated in Section 6.4, it remains fundamentally fragile to the exclusion of a single year.

## 6.9 Economic Interpretation of the Interaction Term

The full-model coefficient of −3.22 must **not** be interpreted mechanically as: "each additional USD 1 billion of mineral exports causes USD 3.22 billion of trade-balance deterioration." Such a causal interpretation violates accounting logic, ignores the distinction between statistical significance and economic meaning, and is economically implausible.

The coefficient is a conditional association in a small annual sample where:
- strategic mineral export growth coincided with broader post-2014 changes including import-side expansion, commodity-price shocks, and exchange-rate adjustment;
- the original GDP-levels specification had severe multicollinearity (VIF > 100); the primary growth-rate specification (Scheme B, max VIF = 10.4) substantially reduces this but residual collinearity remains;
- the interaction term absorbs variation from multiple concurrent post-2014 structural changes;
- the coefficient is dominated by the 2023 observation.

The parsimonious coefficient (−2.38) is more moderate but remains difficult to interpret structurally because *n* = 24 with 6 parameters offers limited degrees of freedom. The most defensible interpretation is qualitative: the trade-balance payoff of mineral exports appears to have weakened in the post-BRI period, driven primarily by the extreme 2023 outcome.

## 6.10 Endogeneity and Identification Limitations

The model does not achieve causal identification. Endogeneity concerns warrant explicit acknowledgement:

### Oil Exports and Omitted-Variable Bias: Direction and Bounds

Oil and energy exports are unavailable in the current bilateral dataset, representing a severe omitted variable. This omission biases the Minerals × Post-BRI coefficient. The direction and magnitude of this bias depend on:
- the correlation between bilateral oil exports and strategic mineral exports;
- the correlation between oil exports and the bilateral trade balance;
- the impact of post-2014 global commodity price shocks.

While the model includes the Brent crude price as a control, Brent only captures global oil-price movements, not the specific volume of Kazakhstan's bilateral oil exports to China. Therefore, it only partially mitigates the omitted-variable bias. The mineral coefficient and its interaction term likely absorb broader commodity-export dynamics, including the energy trade. Because the direction and magnitude of omitted oil-export bias cannot be quantified with the current data, the strategic-mineral interpretation is treated as suggestive and bounded by this limitation. This is why the thesis interprets the coefficient as diagnostic evidence of broader trade-balance fragility rather than mineral-specific causal evidence.

### Other Endogeneity Concerns

1. **Reverse causality:** The trade balance may itself affect mineral exports (through exchange-rate adjustments) and imports (through income effects). Mineral exports and trade balance are jointly determined in general equilibrium.

2. **Omitted variable bias:** Oil and energy exports, uranium spot prices, transport infrastructure quality, exchange-rate policy regimes, China-specific demand shocks, and Kazakhstan industrial policy are all plausible omitted confounders.

3. **Bad controls:** KZT/USD and Kazakhstan GDP may themselves respond to commodity prices and trade-balance dynamics. Including them may absorb part of the causal mechanism rather than controlling for confounders, introducing post-treatment bias.

The robustness strategy—comparing parsimonious and full specifications, testing multiple mineral proxies, and reporting leave-one-out sensitivity—partially addresses these concerns by showing which results are robust to specification changes. However, credible causal identification would require instrumental-variable strategies, quasi-experimental variation, or substantially larger samples.

## 6.11 Hypothesis Evaluation

Table 6.19 reports the formal tests for the primary annual model (B) and the primary monthly model (M1, §6.18). The decision rule is stated in advance: reject H₀ if the one-sided *p*-value is below 0.05.

**Table 6.19. Formal Hypothesis Tests**

| Hypothesis | H₀ vs H₁ | Model | Coef. | HAC SE | *t* | df | *p* (two-sided) | *p* (one-sided) | Decision (5%) |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| H1: post-BRI level shift | β₂ ≥ 0 vs β₂ < 0 | Annual B | 0.588 | 2.240 | 0.26 | 15 | 0.797 | 0.602 | Fail to reject H₀ |
| | | Monthly M1 | −0.222 | 0.131 | −1.70 | 103 | 0.093 | 0.046 | Reject H₀ |
| H2: pre-BRI mineral payoff | β₁ ≤ 0 vs β₁ > 0 | Annual B | 1.645 | 0.855 | 1.92 | 15 | 0.073 | 0.037 | Reject H₀ |
| | | Monthly M1 | 1.260 | 0.376 | 3.36 | 103 | 0.001 | 0.001 | Reject H₀ |
| H3: weaker payoff after BRI | β₃ ≥ 0 vs β₃ < 0 | Annual B | −2.489 | 0.974 | −2.56 | 15 | 0.022 | 0.011 | Reject H₀ |
| | | Monthly M1 | −0.913 | 0.339 | −2.69 | 103 | 0.008 | 0.004 | Reject H₀ |
| Joint post-BRI change | β₂ = β₃ = 0 | Annual B | — | — | *F* = 3.89 | 15 | 0.044 | — | Reject H₀ |
| | | Monthly M1 | — | — | *F* = 15.05 | 103 | <0.001 | — | Reject H₀ |
| Post-BRI mineral slope | β₁ + β₃ = 0 | Annual B | −0.844 | 1.381 | −0.61 | 15 | 0.541 | — | Fail to reject H₀ |
| | | Monthly M1 | 0.347 | 0.312 | 1.11 | 103 | 0.268 | — | Fail to reject H₀ |

*Source: Author's calculations (`hypothesis_tests_formal.csv`, Script 40; `monthly_hypothesis_tests.csv`, Script 42). Annual p-values use the t distribution with residual degrees of freedom; the normal-approximation values reported in Table 6.1 are slightly smaller. Results for Models C and A2 are in the same file and lead to the same decisions for H1–H3.*

**Interpretation of each test.**

- **H1 (post-BRI level shift).** In the annual model the post-BRI dummy is positive and far from significant, so H₀ is not rejected. In the monthly model, holding mineral exports, Brent, the exchange rate and seasonality constant, the monthly balance was on average USD 0.22 billion lower after 2013, which is significant at the 5 per cent level in the one-sided test (*p* = 0.046). The level shift is not robust, however: it disappears once a linear trend is added (M2, *p* = 0.84). H1 is therefore **not supported as a level shift**. The descriptive decline in the average balance (§4.5) is better explained by the change in the mineral slope (H3) than by a separate drop in level.
- **H2 (mineral payoff before BRI).** Rejected at the 5 per cent level in both datasets. Before BRI, each additional USD 1 billion of mineral exports was associated with a USD 1.65 billion higher annual balance (annual model) and a USD 1.26 billion higher monthly balance (monthly model). A coefficient above one is plausible because mineral export months also tend to be strong months for other commodity exports. **H2 is supported.**
- **H3 (weaker payoff after BRI).** Rejected at the 5 per cent level in both datasets. After 2013 the mineral slope falls by 2.49 (annual) and 0.91 (monthly). The post-BRI slope itself (β₁ + β₃) is not significantly different from zero in either dataset (annual −0.84, *p* = 0.54; monthly 0.35, *p* = 0.27). In plain terms, mineral exports were associated with a better balance before BRI, and that association is no longer detectable afterwards. **H3 is supported as a conditional association.** In the annual data it depends on the 2020–2023 observations (§6.4, §6.14, §6.20). In the observed monthly data it holds in 2010–2019, before the period those concerns apply to.
- **Joint test.** The null that the post-BRI period changed nothing (β₂ = β₃ = 0) is rejected in both datasets (annual *p* = 0.044; monthly *p* < 0.001).

**What the tests do and do not establish.** Rejecting H₀ for H2 and H3 means the data are unlikely to have produced these coefficients if the true associations were zero or of the opposite sign. It does not establish that BRI or mineral exports *caused* the change in the balance: the post-BRI indicator also captures the 2014–2016 oil price collapse and the 2015 tenge devaluation (§6.10, §6.13). The Granger tests in §6.19 address direction of association, and they do not show that mineral exports lead the balance after 2013.

**Table 6.20. Summary Verdict**

| Hypothesis | Annual evidence | Monthly evidence (observed, 2010–2019) | Verdict |
|---|---|---|---|
| H1: post-BRI level shift | Not significant | Significant at 5% (one-sided), not robust to a trend | Not supported as a level shift |
| H2: pre-BRI mineral payoff | Significant (*p* = 0.037, one-sided) | Significant (*p* = 0.001) | Supported |
| H3: weaker post-BRI payoff | Significant; sensitive to 2020–2023 data | Significant (*p* = 0.004); robust to trend, copper, dynamics, alternative break date and product-level minerals; not robust to controlling for oil exports | Supported as a conditional association |

## 6.12 Bilateral Energy-Export Control

Earlier versions of this thesis reported a sensitivity check using an "illustrative" annual energy-export proxy. That proxy was not observed data: it was set equal to 55 per cent of total bilateral exports in every year, so it carried no independent information and was mechanically collinear with exports. It has been withdrawn, and the column has been removed from the annual dataset.

Energy exports are now controlled for with **observed** data. UN Comtrade monthly records include Kazakhstan's HS 27 exports to China for 2010–2023 (§4.6). In the monthly model, adding HS 27 exports removes the post-BRI weakening of the mineral–balance association (interaction +0.25, *p* = 0.31; §6.18, Model M4). Section 7.1 discusses what this implies.

## 6.13 Placebo Break-Year Diagnostics

A standard criticism of pre/post-BRI dummy designs is that the chosen break year may coincide with unrelated shocks rather than BRI-specific structural change. For Kazakhstan, the most salient confounders at 2013–2014 are: the global oil-price collapse of 2014–2016, the Kazakhstan tenge devaluation of August 2015, and Russia's Crimea-related sanctions exposure that rerouted some Eurasian trade flows. If the detected structural break occurs primarily because of these non-BRI shocks, the post-BRI dummy is a misspecified period indicator.

To partially address this concern, Chow tests were conducted at four alternative break years (2013, 2014, 2015, 2016), and a BIC-selected Bai–Perron-style procedure was applied to detect the number and location of breaks in the bilateral trade-balance series.

**Table 6.8. Chow Test Statistics at Alternative Break Years**

| Break Year | Chow *F* | *p*-value | Significant at 10%? | Context |
|-----------|------:|------:|------:|------:|
| 2013 | 10.43 | 0.0008 | *** | BRI announcement (Sep 2013) |
| 2014 | 6.65 | 0.0061 | ** | Oil-price collapse begins; tenge devaluation (2015) |
| 2015 | 2.84 | 0.0823 | * | Tenge float; China growth slowdown |
| 2016 | 1.20 | 0.3215 | No | No major bilateral structural event |

*Note: Author's calculations. Chow test applied to the parsimonious trade-balance regression with a split at the indicated year.*

The BIC-selected Bai–Perron procedure detects two structural breaks: one in approximately 2009 (95% CI: 2004–2009) and one in approximately 2014 (95% CI: 2014–2019). The 2009 break is consistent with the Global Financial Crisis commodity collapse. The 2014 break overlaps with both the BRI implementation period and the oil-price collapse.

**Interpretation.** The Chow results show that the 2013 break is the single most statistically significant (F = 10.43, *p* < 0.001), followed by 2014. The 2016 break is statistically indistinguishable from no break. This pattern is consistent with the structural change being concentrated in the 2013–2014 window rather than diffusely distributed across the post-2013 period. However, this does not resolve the BRI-versus-oil-shock identification problem: both BRI and the oil-price collapse are 2013–2014 phenomena. The placebo evidence is more useful for ruling out *late-period* confounders (2016, 2018) than for separating early-period co-incident shocks. These limitations are fully consistent with the thesis's broader claim that the evidence is diagnostic rather than causal.

## 6.14 The 2022–2023 Sanctions-Evasion Channel

### Background and Hypothesis

Following Russia's invasion of Ukraine in February 2022, Western economies imposed broad export controls on Russia covering electronics (HS 85), machinery (HS 84), and vehicles (HS 87). These controls created strong incentives for *parallel imports*: routing restricted goods through third countries — including Kazakhstan — to reach Russian consumers and industries. Kazakhstan's geographical position as Russia's largest land-border trading partner and BRI corridor economy makes it a plausible transit route. The parallel-imports hypothesis holds that the 2022–2023 surge in Kazakhstan's imports from China is at least partly a sanctions-evasion artefact: Chinese goods entered Kazakhstan ostensibly for domestic consumption but were onward-shipped to Russia.

If this hypothesis is correct, the 2023 bilateral trade deficit (−USD 2.01 billion) does not indicate a BRI-driven structural deepening of asymmetric interdependence. Instead, it reflects a temporary geopolitical shock that inflated Kazakhstan's recorded imports from China. This would significantly weaken the causal interpretation of the post-BRI mineral interaction coefficient.

### Import Surge Magnitude

Kazakhstan's imports from China grew by 47.5% in 2022 and by a further 369.2% in 2023, from USD 3.58 billion to USD 16.77 billion. In the series as reported, this is by far the largest two-year acceleration in the sample. Much of it, however, reflects the 2020–2022 reporting break (§4.7): measured against China's own records, Kazakhstan's imports from China grew more gradually (China-reported exports to Kazakhstan: USD 11.70 billion in 2020, 13.76 billion in 2021, 16.36 billion in 2022 and 24.70 billion in 2023). The genuine increase in 2023 is still large, about 51 per cent in China's data, which leaves room for a parallel-import channel, but it is far smaller than the 369 per cent jump in the reported series.

**HS-level evidence.** The monthly UN Comtrade data collected for this revision include Kazakhstan's imports from China in HS chapters 84 (machinery), 85 (electrical equipment) and 87 (vehicles), the categories most associated with parallel imports. They are reported for every month of 2010–2019 and 2023, but not for 2020–2022 (§4.7), so a year-by-year test is not possible. Comparing 2019 with 2023 is possible: machinery imports rose from USD 1.36 to 3.38 billion (×2.5), electrical equipment from USD 1.23 to 2.57 billion (×2.1), and vehicles from USD 0.34 to 2.16 billion (×6.4). The three chapters together kept a similar share of total imports from China (45 per cent in 2019, 48 per cent in 2023). The sixfold rise in vehicle imports stands out and is consistent with a re-export channel to Russia, but the data cannot show where the goods ended up.

### Regression Robustness: Does the BRI Interaction Survive?

**Table 6.9. Sanctions-Period Robustness: Post-BRI Mineral Interaction Coefficient**

| Model | N | Interaction β | HAC SE | *p*-value | Interpretation |
|-------|---|---:|---:|---:|---|
| Baseline parsimonious (2000–2023) | 24 | −2.382 | 0.977 | 0.015 | Full sample |
| Parsimonious excl. 2022–2023 | 22 | +0.134 | 0.317 | 0.672 | Sanctions period excluded |
| Gravity ratio excl. 2022–2023 | 22 | +0.102 | 0.432 | 0.813 | Preferred spec, excl. sanctions |
| Parallel-imports dummy (2000–2023) | 24 | −1.906 | 1.340 | 0.155 | Dummy = 1 for 2022–2023 |
| Gravity ratio + parallel dummy | 24 | −1.986 | 1.397 | 0.155 | Preferred spec + dummy |
| Parsimonious excl. 2023 only | 23 | +0.401 | 0.257 | 0.118 | Midterm robustness replicated |

*Note: Author's calculations. HAC (Newey–West) standard errors, bandwidth = 3.*

### Findings and Interpretation

**After excluding 2022–2023, the post-BRI mineral interaction coefficient does not survive.** The coefficient reverses to +0.134 (*p* = 0.672) in the parsimonious specification and to +0.102 (*p* = 0.813) in the gravity-ratio specification. After controlling for a parallel-imports dummy (= 1 for 2022–2023), the interaction is −1.906 (*p* = 0.155) — attenuated by approximately 20% relative to baseline and no longer statistically significant at the 10% level.

This is an honest and important finding. The headline negative interaction is driven entirely by the 2022–2023 import surge, and that surge coincides precisely with the Russia-sanctions period that provides an alternative, overlapping channel. This weakens a narrow BRI-only interpretation, as parallel imports may account for a significant portion of the observed effect. The thesis therefore cannot claim that the post-BRI mineral interaction is a robust structural finding.

**What this does not mean.** These results do not disprove the asymmetric interdependence interpretation. Three points:

1. *BRI infrastructure may have enabled the parallel-import routing.* Kazakhstan's expanded trade capacity — a direct BRI outcome — may be what made it a viable transit route for sanctions-evasion flows. The channels are not mutually exclusive.
2. *Imports from China were already rising before 2023.* China-reported exports to Kazakhstan grew by 18 per cent in 2021 and 19 per cent in 2022, before the sanctions-period jump in 2023, which suggests that some structural acceleration preceded it.
3. *The descriptive decomposition remains robust.* Imports from China grew by 94.3% on average in the full post-BRI period (2014–2023). Even excluding 2022–2023 (years 9–10 of the post-BRI period), the remaining post-BRI import growth is substantial.

**Causal language threshold.** In light of these results, the thesis applies the triple-concordance criterion established in §5.1: a BRI-specific causal claim requires that (a) the DiD partner placebo (§6.15), (b) the synthetic counterfactual (§6.16), and (c) this sanctions robustness check all point in the same direction. The sanctions check does **not** support a China-specific BRI causal channel. Therefore, all post-BRI effect claims in this thesis are described as "consistent with" or "associated with" asymmetric interdependence rather than as causal evidence.

## 6.15 Comparative Analysis: Two-Way Fixed-Effects Difference-in-Differences

**Design.** This section tests whether Kazakhstan's bilateral trade-balance ratio deteriorated *specifically* with China post-2013, or whether it deteriorated uniformly across all major trading partners. The TWFE DiD design stacks annual bilateral trade-balance ratios for six partners — China (treatment), Russia, Germany, Uzbekistan, Turkey, and USA (controls) — into a balanced panel of 144 observations (6 partners × 24 years). The treatment indicator is `china_dummy × post_2013`. Partner and year fixed effects absorb unobserved partner heterogeneity and common time trends. HAC standard errors (bandwidth = 3) account for serial correlation within partners. Data are sourced from the UN Comtrade public API, validated against the existing Kazakhstan–China panel (0% discrepancy across all 24 years).

**Table 6.10. TWFE DiD Results: China-Specific Post-2013 Balance Shift**

| Specification | N obs | Partners | DiD coef (China) | HAC SE | *p*-value | Interpretation |
|---|---:|---:|---:|---:|---:|---|
| TWFE DiD: China vs all partners | 144 | 6 | **−0.305** | **0.083** | **0.0002**† | Largest deterioration of six partners |
| TWFE DiD: China vs Russia only | 48 | 2 | −0.151 | 0.057 | 0.008 | Robust to most similar partner |

*Note: Author's calculations. Partner and year dummies as fixed effects. HAC standard errors, bandwidth = 3. † This p-value is overstated; see Table 6.10b.*

**Original interpretation.** The TWFE DiD coefficient of −0.305 indicates that China's bilateral balance ratio declined by 30.5 percentage points more than the control partners' after 2013, after controlling for partner-level heterogeneity and common time trends. It is also negative when the comparison is restricted to Russia alone (−0.151).

**Final-audit robustness of the DiD.** The *p*-values above use Newey–West errors on the stacked panel, which treats the last year of one partner and the first year of the next as if they were consecutive periods. This understates uncertainty. In addition, Kazakhstan-reported imports fall sharply in 2020 not only from China (−71 per cent) but also from Germany (−66 per cent), the USA (−71 per cent), Uzbekistan (−62 per cent) and Turkey (−39 per cent), though not from Russia (−4 per cent) (`partner_import_break.csv`). The 2020–2022 reporting break described in §4.7 therefore affects most of the control partners too. Table 6.10b re-estimates the DiD with appropriate inference and without the affected years.

**Table 6.10b. DiD Robustness: Samples and Inference Methods**

| Sample | N | DiD coef. | *p* (original NW, stacked) | *p* (Driscoll–Kraay) | *p* (partner-clustered) | *p* (wild cluster bootstrap) |
|---|---:|---:|---:|---:|---:|---:|
| All partners, 2000–2023 | 144 | −0.305 | <0.001 | 0.022 | 0.033 | 0.330 |
| All partners, excl. 2020–2022 | 126 | −0.352 | <0.001 | 0.020 | 0.017 | 0.381 |
| All partners, 2000–2019 | 120 | −0.314 | <0.001 | 0.022 | 0.027 | 0.370 |
| Excl. Russia, 2000–2023 | 120 | −0.344 | <0.001 | 0.042 | 0.050 | 0.320 |
| Excl. Russia, excl. 2020–2022 | 105 | −0.368 | <0.001 | 0.046 | 0.046 | 0.360 |

*Notes: Driscoll–Kraay errors are robust to cross-partner and serial correlation (3 lags). Clustered errors use six partner clusters, which is too few for reliable cluster inference; the wild cluster bootstrap (Webb weights, 1,999 replications, null imposed) is the recommended correction for few clusters. Source: `did_robustness.csv`, Script 44.*

**Permutation (placebo-in-space) test.** Re-estimating the DiD with each partner in turn treated as if it were "China" gives: China −0.305, Germany −0.243, Russia −0.124, Uzbekistan +0.057, USA +0.231, Turkey +0.384 (`did_permutation.csv`). China has the most negative estimate of the six, in all three samples tested. With six units, the smallest *p*-value a permutation test can produce is 1/6 = 0.167, which is what China obtains.

**Interpretation.** Three conclusions follow:

1. **The size and sign of the China-specific shift are robust.** The estimate lies between −0.31 and −0.37 in every sample, including when the 2020–2022 reporting-break years or Russia are excluded.
2. **Its statistical precision is weaker than originally reported.** With errors suited to panel data (Driscoll–Kraay, clustered), *p* is about 0.02–0.05. With the wild cluster bootstrap and permutation inference, which are the more reliable options when there are only six partners, the effect is not statistically significant (*p* ≈ 0.17–0.38). The original *p* = 0.0002 should not be quoted as the measure of confidence.
3. **China ranks first of six, but Germany is close behind** (−0.24). A large post-2013 decline in a second, non-BRI relationship means the comparison cannot fully separate a China-specific BRI channel from shocks that hit several partners at once, such as the 2014 oil-price collapse (§4.6).

The DiD therefore shows that the post-2013 deterioration with China was the largest among Kazakhstan's major partners and is not an artefact of the 2020–2022 data. It does not, on its own, rule out common commodity-price shocks, and with six partners it cannot deliver high statistical confidence.

**Within-unit ITS cross-check.** For comparability with the pre-update analysis, the ITS placebo break-year results from within-unit estimation are preserved below:

| Specification | N | Level shift β | HAC SE | *p*-value | Interpretation |
|---|---|---:|---:|---:|---|
| True break at 2013 | 24 | −0.237 | 0.100 | 0.018 | True BRI break: significant |
| Placebo break at 2009 | 24 | +0.149 | 0.089 | 0.094 | Marginally significant ⚠ |
| Placebo break at 2010 | 24 | +0.176 | 0.101 | 0.080 | Marginally significant ⚠ |
| Placebo break at 2011 | 24 | +0.070 | 0.100 | 0.488 | Insignificant ✓ |

The 2009/2010 marginal placebo significance in the ITS is a within-unit artefact that reflects the pre-existing downward trend in the Kazakhstan–China balance. The TWFE DiD absorbs common trends through year fixed effects; its robustness is assessed in Table 6.10b above.

**Note on 2020–2022.** The reporting break affects imports from China, Germany, the USA, Uzbekistan and Turkey, but not Russia. Excluding 2020–2022 leaves the DiD estimate essentially unchanged (−0.352 against −0.305; Table 6.10b), so the result does not depend on the break years.

![Figure DiD. Event Study: Kazakhstan–China Balance vs. Other Partners (2013 = reference year)](../Outputs/generated_figures/fig_did_event_study.png)
*Note: Actual balance ratio series with BRI 2013 break marker and ITS placebo years. Author's construction.*

## 6.16 Synthetic Counterfactual

**Within-unit counterfactual.** The full multi-partner synthetic control (Abadie 2003 design) requires partner time series as donor units; these are now available via the UN Comtrade API (see §6.15). A within-unit synthetic control is implemented as a complement: the pre-period (2000–2012) dynamics of the KZ-China balance ratio are modeled using global commodity prices (Brent, normalized), the gravity ratio (log CN/KZ GDP), a linear time trend, and the lagged balance ratio as predictors. The pre-period OLS fit on these predictors serves as a within-unit synthetic counterfactual for the post-2013 period, isolating departures from pre-BRI trend dynamics without using other partners as donors.

**Design.** The synthetic counterfactual is constructed as the OLS-fitted value of the trade-balance ratio on the four predictors, with coefficients estimated only on the 2000–2012 pre-period sample. The post-2013 counterfactual is the out-of-sample projection of these pre-period dynamics. A negative gap (actual < synthetic) post-2013 is interpreted as the actual balance falling below what would be predicted by the pre-BRI dynamics of commodity prices, bilateral size asymmetry, and trend.

**Table 6.11. Post-BRI Synthetic Counterfactual Gap**

| Year | Actual balance ratio | Synthetic counterfactual | Gap (actual − synthetic) |
|------|--------------------:|------------------------:|-------------------------:|
| 2013 | 0.264 | 0.340 | −0.075 |
| 2014 | 0.142 | 0.265 | −0.123 |
| 2015 | 0.037 | 0.192 | −0.155 |
| 2016 | 0.070 | 0.160 | −0.091 |
| 2017 | 0.105 | 0.164 | −0.059 |
| 2018 | 0.079 | 0.173 | −0.094 |
| 2019 | 0.082 | 0.115 | −0.033 |
| 2020 | 0.555 | 0.112 | +0.443 |
| 2021 | 0.477 | 0.361 | +0.116 |
| 2022 | 0.491 | 0.287 | +0.204 |
| 2023 | −0.064 | 0.219 | −0.283 |

*Note: Author's calculations. Pre-period MSPE = 0.0038; post-period MSPE = 0.0362; MSPE ratio = 9.53.*

**Findings.** The gap is negative in 8 of 11 post-BRI years, with a mean post-BRI gap of −0.014. The MSPE ratio (post-period fit error / pre-period fit error) is 9.53, indicating that post-2013 outcomes are substantially harder to predict from pre-BRI dynamics alone — consistent with a post-2013 structural change. The three years with positive gaps (2020, 2021, 2022) are the years in which Kazakhstan-reported imports from China are under-recorded (§4.7). China's own data show its exports to Kazakhstan fell by only 8 per cent in 2020 and rose in 2021 and 2022. These positive gaps should therefore be read mainly as a reporting artefact, not as a COVID-19 or sanctions-related improvement in the balance. With mirror-adjusted imports the 2020–2022 balance ratios would be much lower, and the post-BRI gap would be more consistently negative.



![Figure 7. Synthetic Counterfactual: Actual vs. Synthetic KZ-China Trade Balance Ratio](../Outputs/generated_figures/fig_synthetic_control.png)
*Note: Panel A shows actual vs. synthetic trajectory. Panel B shows the gap plot of post-BRI deviations from the counterfactual.*

**Triple-concordance assessment.** The three causal identification methods produce the following pattern:

| Method | Direction | Significant | Notes |
|--------|-----------|-------------|-------|
| Regression: primary (Scheme B, growth rates) | Negative (−2.49) | p=0.011 | Driven by 2022–2023; loses significance on exclusion |
| Regression: robustness (Scheme C, gravity ratio) | Negative (−2.42) | p=0.033 | Consistent with primary; same fragility pattern |
| **TWFE DiD: China vs all partners** | **Negative (−0.305)** | **p = 0.02 (Driscoll–Kraay); 0.17–0.38 (permutation, wild bootstrap)** | **Largest of six partners; magnitude robust; low precision with six units** |
| TWFE DiD: China vs Russia | Negative (−0.151) | p=0.008 | Robust to most similar partner comparison |
| Synthetic control gap | Negative (mean=−0.014) | p=0.857 | Consistent direction; not statistically significant |
| Sanctions robustness | Attenuated to insignificance | p=0.966 excl. 2022–23 (Scheme B) | Alternative explanation not ruled out |

**Causal language.** Following the triple-concordance criterion established in §5.1: all methods point in the same direction (negative/adverse post-BRI balance shift for China). The TWFE DiD shows the largest post-2013 deterioration for China among six partners, robust in magnitude, although with only six partners its statistical precision is limited (Table 6.10b). However, the regression interaction does not survive exclusion of 2022–2023 and the sanctions robustness check cannot rule out sanctions-era parallel-import routing as an alternative mechanism. The thesis therefore upgrades its framing to: the evidence is **consistent with** asymmetric interdependence deepening post-BRI, with cross-partner identification now supporting China-specificity, but causal attribution to BRI *specifically* (versus concurrent geopolitical shocks in 2022–2023) cannot be conclusively established. No finding in the thesis meets the threshold for causal language; all results are described as associations.


## 6.17 Quarterly Disaggregation of the Annual Data (*n* = 96)

Following the supervisor's suggestion, all annual flow variables (exports, imports, trade balance, mineral exports) were disaggregated to quarters with the Denton first-difference method [@denton_1971; @dagum_cholette_2006]. The exchange rate and GDP were disaggregated under an average constraint. Brent was not interpolated: observed quarterly averages were taken from the World Bank Pink Sheet. In every year the four quarters add up exactly to the published annual total (maximum discrepancy below 10⁻¹³).

**Table 6.12. Annual vs. Interpolated Quarterly Estimates**

| Model | Data | N | Minerals β₁ (*p*) | Interaction β₃ | HAC SE | *p* | *R*² | Adj. *R*² | DW |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| B (growth controls) | Annual, observed | 23 | 1.645 (0.073) | −2.489 | 0.974 | 0.022 | 0.742 | 0.621 | 1.65 |
| B (growth controls) | Quarterly, interpolated, HAC(4) | 95 | 1.951 (0.001) | −2.570 | 0.971 | 0.010 | 0.698 | 0.674 | 0.25 |
| B (growth controls) | Quarterly, interpolated, HAC(12) | 95 | 1.951 (0.002) | −2.570 | 1.001 | 0.012 | 0.698 | 0.674 | 0.25 |
| A2 (parsimonious) | Annual, observed | 24 | 1.694 (0.062) | −2.382 | 0.977 | 0.025 | 0.703 | 0.620 | 1.74 |
| A2 (parsimonious) | Quarterly, interpolated, HAC(4) | 96 | 1.775 (0.006) | −2.404 | 0.961 | 0.014 | 0.681 | 0.663 | 0.25 |
| A2 (parsimonious) | Quarterly, interpolated, HAC(12) | 96 | 1.775 (0.011) | −2.404 | 0.960 | 0.014 | 0.681 | 0.663 | 0.25 |

*Source: Author's calculations (`quarterly_interpolated_results.csv`, Script 41). p-values use the t distribution.*

The quarterly estimates reproduce the annual coefficients almost exactly. That is expected, because the quarterly data contain the same information. What changes is the apparent precision: *p*-values fall (for β₁ from 0.073 to 0.001) only because there are four times as many rows. The Durbin–Watson statistic of 0.25 shows that the interpolated residuals are almost perfectly autocorrelated. Consecutive quarters are close to copies of each other, not independent observations.

**Table 6.13. Monte Carlo: How Often Is a True Null Rejected at the 5% Level?**

| Design | False-positive rate |
|---|---:|
| Annual, *n* = 24, HAC(3) | 20.6% |
| Interpolated quarterly, *n* = 96, OLS standard errors | 46.8% |
| Interpolated quarterly, *n* = 96, HAC(4) | 23.3% |
| Interpolated quarterly, *n* = 96, HAC(12) | 21.4% |
| Observed monthly benchmark, *n* = 120, HAC(12) | 22.6% |

*Note: 2,000 replications. The annual designs regress one AR(1) series (φ = 0.6, n = 24) on another, independent AR(1) series, so the true slope is zero. The monthly benchmark uses φ = 0.9 and n = 120. Source: `interpolation_monte_carlo.csv`, Script 41.*

The experiment shows three things. First, interpolation with conventional standard errors more than doubles the false-positive rate (46.8 per cent against 20.6 per cent at annual frequency), so a 96-observation model reported with OLS standard errors would overstate the evidence. Second, with HAC standard errors the interpolated model performs no better than the annual model: interpolation adds rows but no information. Third, every design over-rejects when both series are persistent. This is a general small-sample property of HAC tests [@kiefer_vogelsang_bunzel_2000] and a reason for caution with all levels regressions in this thesis.

**Conclusion.** The interpolated quarterly model is reported as a robustness check, and it confirms the sign and size of the annual estimates. It is not used as independent evidence. The sample-size concern is addressed with observed monthly data in §6.18.

## 6.18 Observed Monthly Evidence, 2010–2019 (*n* = 120)

**Table 6.14. Monthly Association Models (Dependent Variable: Monthly Trade Balance, USD bn)**

| Model | N | Minerals β₁ | *p* | Post-BRI β₂ | *p* | Interaction β₃ | HAC SE | *p* | *R*² | Adj. *R*² |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **M1: parsimonious + month dummies** | 120 | **1.260** | 0.001 | −0.222 | 0.093 | **−0.913** | 0.339 | **0.008** | 0.737 | 0.696 |
| M2: M1 + linear trend | 120 | 1.374 | <0.001 | −0.028 | 0.843 | −1.061 | 0.356 | 0.004 | 0.758 | 0.718 |
| M3: M1 + copper price | 120 | 1.296 | <0.001 | −0.164 | 0.303 | −1.041 | 0.414 | 0.014 | 0.742 | 0.699 |
| M5: M1 + two lags of TB | 118 | 1.401 | <0.001 | 0.012 | 0.912 | −1.177 | 0.397 | 0.004 | 0.782 | 0.742 |
| M1, break at 2013M10 | 120 | 1.208 | 0.001 | −0.225 | 0.071 | −0.583 | 0.260 | 0.027 | 0.722 | 0.679 |
| M1, product-level minerals (HS 2610/2612/2844/7403) | 120 | 1.332 | <0.001 | −0.218 | 0.093 | −0.984 | 0.342 | 0.005 | 0.741 | 0.701 |
| M4: M1 + oil and energy exports (HS 27) | 120 | 0.888 | <0.001 | −0.227 | 0.009 | +0.252 | 0.247 | 0.309 | 0.920 | 0.906 |
| *Quarterly sums of the same observed data* | 40 | 0.979 | 0.044 | −0.799 | 0.057 | −0.678 | 0.608 | 0.273 | 0.813 | 0.765 |

*Notes: Kazakhstan-reported UN Comtrade monthly data [@un_comtrade_2026], NBK exchange rates [@nbk_rates_2026] and Pink Sheet prices [@worldbank_pinksheet_2026]. All monthly models include Brent, KZT/USD and 11 calendar-month dummies; the quarterly model uses quarter dummies and HAC(4). Newey–West HAC(12) standard errors, t-distribution p-values. Source: `monthly_results.csv`, `observed_quarterly_results.csv`, Script 42.*

![Figure 8. Monthly Kazakhstan–China Trade Balance and Strategic Mineral Exports, 2010–2019](../Outputs/generated_figures/fig_monthly_trade_balance.png)
*Source: UN Comtrade monthly data, Kazakhstan as reporter. Author's construction (Script 42).*

**Table 6.15. Fit Statistics for the Primary Monthly Model (M1) and the Dynamic Variant (M5)**

| Statistic | M1 | M5 |
|---|---:|---:|
| N | 120 | 118 |
| *R*² / adjusted *R*² | 0.737 / 0.696 | 0.782 / 0.742 |
| *F* (classical), *p* | 18.05, <0.001 | — |
| HAC Wald *F*, *p* | 197.7, <0.001 | — |
| AIC / BIC | −41.8 / 5.6 | −56.9 / −4.3 |
| Standard error of regression (USD bn per month) | 0.190 | 0.177 |
| Durbin–Watson | 1.47 | 1.97 |
| Breusch–Godfrey (12 lags), *p* | 0.004 | 0.161 |
| Breusch–Pagan, *p* | 0.033 | 0.001 |
| Ramsey RESET, *p* | 0.366 | 0.242 |

*Source: `monthly_fit_statistics.csv`, Script 42.*

**Interpretation.** The monthly data give 120 independent observations instead of 24 annual totals, and they support the annual pattern without relying on 2020–2023.

1. **H2 and H3 hold in observed monthly data.** Before BRI, a USD 100 million rise in monthly mineral exports was associated with a USD 126 million higher monthly balance. After 2013 that association falls by 0.91 (*p* = 0.008), leaving a post-BRI slope of 0.35 that is not significantly different from zero. The model explains 74 per cent of monthly variation (adjusted *R*² = 0.70), with a typical error of USD 0.19 billion per month.
2. **The result survives the main threats to a levels regression.** It holds with a linear trend (M2), with the copper price (M3), and with two lags of the dependent variable (M5). M5 removes the residual autocorrelation (Breusch–Godfrey *p* = 0.16, DW = 1.97) and still gives β₃ = −1.18 (*p* = 0.004), which implies a long-run effect of about −2.3. The result also holds when the break is moved to October 2013 and when minerals are measured at product level.
3. **It does not survive controlling for bilateral oil exports (M4).** Once monthly HS 27 exports are held constant, the interaction becomes small and positive (+0.25, *p* = 0.31). Part of this is mechanical: oil exports are a component of total exports, and their coefficient is almost exactly one (0.999). Substantively, it means the post-2013 weakening of the mineral–balance association cannot be separated statistically from the post-2014 collapse in oil export values. The monthly data turn the omitted-variable concern of §6.10 into a measured result: the H3 association is not mineral-specific once energy trade is accounted for.
4. **Aggregating the observed months to 40 quarters loses significance** (β₃ = −0.68, *p* = 0.27). The sign is preserved, but quarterly sums average out much of the within-quarter co-movement that identifies the monthly estimate. With 40 observations and 9 parameters, power is low.

5. **Extended monthly samples.** Extending the sample to December 2023 with imports as reported gives β₃ = −1.50 (*p* = 0.027, N = 168), but the fit deteriorates sharply (adjusted *R*² = 0.44) because of the 2020–2022 reporting break (§4.7). With 2020–2022 imports mirror-adjusted, β₃ = −1.77 (*p* < 0.001, N = 151, adjusted *R*² = 0.63). Months from August 2021 to December 2022 drop out because China's monthly records for them could not be retrieved within the Comtrade preview quota. Excluding 2022–2023, the adjusted sample gives β₃ = −0.96 (*p* = 0.004, N = 139).

## 6.19 Granger Causality Tests

**Table 6.16. Granger Causality: Annual Data, 2000–2023**

| Null hypothesis | Method | Lags | N | Statistic | *p* | Decision (5%) |
|---|---|---:|---:|---:|---:|---|
| Minerals do not Granger-cause TB | VAR in differences | 1 | 22 | *F* = 0.01 | 0.922 | Fail to reject |
| | VAR in differences | 2 | 21 | *F* = 0.85 | 0.446 | Fail to reject |
| | Toda–Yamamoto | 1 | 22 | χ² = 0.03 | 0.870 | Fail to reject |
| | Toda–Yamamoto | 2 | 21 | χ² = 1.14 | 0.565 | Fail to reject |
| TB does not Granger-cause minerals | VAR in differences | 1 | 22 | *F* = 6.38 | 0.021 | **Reject** |
| | VAR in differences | 2 | 21 | *F* = 3.57 | 0.052 | Fail to reject |
| | Toda–Yamamoto | 1 | 22 | χ² = 3.14 | 0.076 | Fail to reject |
| | Toda–Yamamoto | 2 | 21 | χ² = 5.61 | 0.060 | Fail to reject |
| BRI intensity does not Granger-cause TB | All four variants | 1–2 | 21–22 | — | 0.747–0.895 | Fail to reject |
| TB does not Granger-cause BRI intensity | All four variants | 1–2 | 21–22 | — | 0.871–0.995 | Fail to reject |

*Source: `granger_annual.csv`, Script 40.*

**Table 6.17. Granger Causality: Observed Monthly Data (Seasonally Adjusted), 2010–2019**

| Sample | Null hypothesis | Lags (rule) | VAR-in-differences *p* | Toda–Yamamoto *p* |
|---|---|---|---:|---:|
| 2010M01–2019M12 (N ≈ 112–118) | Minerals do not Granger-cause TB | 1 (BIC) / 7 (AIC) | 0.934 / 0.873 | 0.912 / 0.550 |
| | TB does not Granger-cause minerals | 1 (BIC) / 7 (AIC) | 0.600 / 0.421 | 0.697 / **<0.001** |
| Pre-BRI 2010M01–2013M12 (N ≈ 44–46) | Minerals do not Granger-cause TB | 1 (BIC) / 3 (AIC) | 0.235 / **0.032** | 0.305 / **0.016** |
| | TB does not Granger-cause minerals | 1 (BIC) / 3 (AIC) | 0.325 / **0.003** | 0.053 / **<0.001** |
| Post-BRI 2014M01–2019M12 (N = 70) | Minerals do not Granger-cause TB | 1 (AIC and BIC) | 0.301 | 0.723 |
| | TB does not Granger-cause minerals | 1 (AIC and BIC) | 0.551 | 0.526 |

*Notes: Both series are seasonally adjusted with calendar-month dummies before testing. Toda–Yamamoto Wald tests use HAC(12) covariance. Bold: rejection at 5%. Source: `granger_monthly.csv`, Script 42.*

**Interpretation.** Granger causality asks whether past values of one series help forecast another, beyond the latter's own past. It is a test of predictive precedence, not of structural causation.

1. **Annual data: no evidence that mineral exports lead the trade balance** (all *p* ≥ 0.45). The only rejection runs the other way: changes in the balance help predict next year's mineral exports at one lag (*p* = 0.021), but not at two lags or in the Toda–Yamamoto version. This is consistent with the reverse-causality concern raised in §6.10. BRI financing intensity has no predictive content for the balance in either direction.
2. **Monthly data: the predictive link exists only before BRI.** In 2010–2013, with the AIC-selected three lags, mineral exports help predict the balance (*p* = 0.032 and 0.016) and the balance helps predict mineral exports (*p* = 0.003 and <0.001). The relationship is bidirectional, so it is a feedback relationship, not a one-way channel. After 2013 neither direction is significant at any lag. This matches H3: the mineral–balance link visible before BRI is no longer detectable afterwards. The pre-BRI result depends on lag choice (it disappears at the BIC-selected single lag) and uses only 44–46 observations, so it is suggestive.
3. **Implication for the hypotheses.** The Granger evidence does not support reading the regression coefficients as mineral exports *driving* the balance. The defensible statement is narrower: the two series co-moved and predicted each other before BRI, and they stopped doing so after 2013. This is consistent with H3 as an association and adds no causal content.

## 6.20 Sensitivity to the 2020–2022 Import Reporting Break

The fragility documented in §6.4 and §6.14 (the H3 interaction disappears when 2023, or 2022–2023, is excluded) was established on a trade-balance series whose 2020–2022 imports are under-recorded (§4.7). This section re-estimates the annual models after correcting those three years.

**Table 6.18. Post-BRI × Minerals Interaction (β₃) Under Alternative Treatments of the 2020–2022 Data**

| Balance series | Model | Full sample β₃ (*p*) | Excl. 2023 β₃ (*p*) | Excl. 2022–2023 β₃ (*p*) | Cook's D for 2023 |
|---|---|---|---|---|---:|
| As reported (original) | B (primary) | −2.489 (0.022) | +0.065 (0.789) | −0.012 (0.967) | 3.85 |
| | C (gravity ratio) | −2.419 (0.047) | +0.307 (0.504) | +0.102 (0.816) | 4.19 |
| | A2 (parsimonious) | −2.382 (0.025) | +0.401 (0.137) | +0.134 (0.678) | 5.17 |
| Imports mirror-adjusted | B (primary) | −2.873 (<0.001) | −1.791 (<0.001) | −1.987 (<0.001) | 2.32 |
| | C (gravity ratio) | −2.720 (0.001) | −1.528 (0.009) | −1.891 (0.009) | 2.00 |
| | A2 (parsimonious) | −2.552 (<0.001) | −1.340 (0.002) | −1.820 (0.009) | 2.42 |
| Exports and imports mirror-adjusted | B (primary) | −2.663 (0.004) | −0.653 (0.013) | −0.674 (0.021) | 3.58 |
| | C (gravity ratio) | −2.526 (0.016) | −0.393 (0.402) | −0.554 (0.250) | 3.71 |
| | A2 (parsimonious) | −2.466 (0.007) | −0.289 (0.319) | −0.508 (0.200) | 4.57 |

*Notes: HAC(3) standard errors, t-distribution p-values. Imports for 2020–2022 = China-reported exports to Kazakhstan × 0.462; exports for 2020–2022 = China-reported imports from Kazakhstan × 0.858 (pooled 2016–2019 Kazakhstan/China ratios). The 4/n Cook's D threshold is 0.17–0.18. Source: `import_break_sensitivity.csv`, Script 43.*

**Bounds on the import adjustment.** Replacing the pooled 2016–2019 ratio with the lowest (0.406) or highest (0.667) annual ratio observed in 2013–2019 does not change the conclusion for the imports-only adjustment. With the primary model excluding 2023, β₃ ranges from −1.40 to −3.22, with *p* < 0.001 in every case (`import_break_ratio_sensitivity.csv`). Under the highest ratio, 2020–2022 also become deficit years, so "2023 is the only deficit year" depends on how the reporting gap is treated.

**Interpretation.**

1. **The fragility reported in §6.4 and §6.14 is largely a product of the reporting break.** Once 2020–2022 imports are brought back in line with China's records, the negative interaction survives the exclusion of 2023 and of 2022–2023 in all three models. The influence of 2023 falls (Cook's D from 3.85 to 2.32 in Model B), although 2023 remains the most influential year.
2. **The correction is not neutral, and its size matters.** If exports are adjusted as well as imports, the interaction stays negative and significant in the primary model (β₃ = −0.65, *p* = 0.013 excluding 2023), but it becomes smaller and loses significance in Models C and A2. The annual evidence for H3 without 2023 is therefore stronger than the original analysis reported, but it is not specification-proof.
3. **The monthly evidence (§6.18) does not depend on this choice.** It uses 2010–2019 only, before the break, and it supports H3 directly.
4. **Granger results are unchanged.** On both adjusted balance series, mineral exports do not Granger-cause the balance (*p* = 0.62–0.97), while the balance helps predict mineral exports at one and two lags (*p* = 0.011–0.042) (`granger_annual_adjusted.csv`).

The adjusted series is an estimate, not an observed figure. The original series is kept as the baseline in Chapters 4–6 for continuity, and the adjusted results are reported alongside it. The thesis now treats the regression interaction as **moderately robust**: robust in observed monthly data before 2020, and robust in annual data once the 2020–2022 reporting gap is addressed. It remains a conditional association that cannot be separated from the post-2014 collapse in oil export values (§6.18).

# 7. Discussion

## 7.1 What the Results Show

The most robust finding is descriptive rather than econometric. Kazakhstan's imports from China grew by 94.3% between the pre-BRI and post-BRI periods, while exports grew by only 24.3%. This import-side deepening—not export collapse—explains the 37.8% decline in the average bilateral trade balance. Strategic mineral exports grew by 29.2%, but this growth was insufficient to offset the import surge. These descriptive findings are consistent with the asymmetric interdependence prediction that BRI trade facilitation would expand trade asymmetrically in favour of the more diversified partner, but this consistency does not constitute causal proof.

The regression analysis corroborates this pattern more strongly than the original annual analysis suggested. In the primary annual model, H2 and H3 are both supported by one-sided tests at the 5 per cent level (Table 6.19), and the model explains 74 per cent of the variation in the balance. In the series as reported, the interaction depends on 2023 and on 2022–2023. Mirror-data validation shows that this dependence is largely a product of under-recorded imports in 2020–2022 (§4.7, §6.20). The strongest single piece of regression evidence is the observed monthly model for 2010–2019 (§6.18). It uses 120 independent observations, none from the contested years, and it reproduces the positive pre-BRI mineral association and its post-BRI weakening (β₃ = −0.91, *p* = 0.008). Two qualifications remain. First, the monthly interaction disappears once bilateral oil exports are controlled for, so the weakening cannot be attributed to minerals specifically rather than to the commodity export base as a whole. Second, Granger tests show no evidence that mineral exports lead the balance, before or after BRI in annual data, and only a lag-sensitive two-way relationship before BRI in monthly data. The sanctions-period concern (§6.14) applies to 2022–2023 and does not affect the 2010–2019 monthly evidence.

The TWFE DiD (§6.15) shows that Kazakhstan's balance ratio with China fell by about 30 percentage points more than with its other major partners after 2013, the largest decline of the six partners. The magnitude is stable across samples, but with six partners the statistical precision is limited, and Germany also shows a large, if smaller, decline. Taken together, the evidence is **consistent with** asymmetric interdependence deepening after BRI, while leaving open how much of the shift reflects the oil-price shock.

**The oil channel.** Observed monthly data show that oil and energy (HS 27) made up 59 per cent of Kazakhstan's exports to China in 2010–2013 but only 36 per cent in 2014–2019, and that annual oil exports to China fell from USD 8.9 billion in 2013 to USD 1.0 billion in 2016 (§4.6). Over the same years, the share of strategic minerals in exports to China rose. This is the most likely reason why the post-BRI weakening of the mineral–balance association disappears once oil exports are controlled for (§6.18): minerals did not lose their value; the oil revenue that used to accompany them collapsed. For asymmetric interdependence this matters, because it shows that Kazakhstan's position with China depends on a commodity whose price it cannot control.

## 7.2 What the Results Do Not Show

The results do **not** demonstrate that:
- BRI *caused* Kazakhstan's trade-balance deterioration;
- strategic minerals *caused* the bilateral deficit;
- China *caused* Kazakhstan's external weakness;
- the interaction coefficient (−3.22, −2.42, or −2.38) is a structural parameter.

The coefficient should be read as evidence that the trade-balance association of mineral exports weakened in the post-BRI period, not as a causal multiplier. The sanctions robustness check (§6.14) cannot rule out that part or all of the post-2013 interaction is driven by the 2022–2023 Russia-sanctions routing rather than BRI-specific structural deepening.

## 7.3 Why 2023 is Retained but Treated Cautiously

The 2023 observation warrants specific and cautious discussion. It is the only year of bilateral deficit (−USD 2.01 billion) in the series as reported. Recorded imports rose to USD 16.77 billion and exceeded exports (USD 14.76 billion) for the first time. The apparent jump from USD 1.96 billion of imports in 2020 is, however, mostly a reporting artefact. China's records show its exports to Kazakhstan rising steadily from USD 11.70 billion (2020) to USD 24.70 billion (2023), and Kazakhstan's 2020–2022 import records are incomplete (§4.7). Once 2020–2022 imports are mirror-adjusted, 2023 is still the most influential year, but it no longer single-handedly determines the regression result (§6.20). Meanwhile, mineral exports reached their sample maximum (USD 5.05 billion). This combination—record mineral exports coinciding with the first deficit—is precisely the puzzle that asymmetric interdependence theory predicts, suggesting 2023 may represent an inflection point, not just a statistical nuisance.

However, from an econometric standpoint, 2023 possesses extremely high leverage. Because inference in a 24-observation dataset is fragile, the results must be reported transparently with and without this year. The full-sample interaction coefficient and the excluding-2023 estimates should be treated as co-equal evidence. The core conclusion of this thesis—that the bilateral trade relationship has grown increasingly fragile and asymmetric—is supported by the descriptive decomposition and the 2023 outcome itself, but the formal claim of a stable, systematic post-BRI statistical interaction effect must not depend solely on the full-sample regression coefficient.

## 7.4 Policy Implications

Policy implications flow directly from the diagnostic findings:

1. **Monitor bilateral trade balance decomposition**, not just total trade volumes. Aggregate trade growth can mask deteriorating bilateral positions.
2. **Track import-side dependence** on Chinese machinery, equipment, and intermediate goods. The 94.3% import growth suggests deepening structural dependence.
3. **Invest in mineral value-added processing** before export. Raw mineral exports generate lower returns and are price-sensitive.
4. **Improve HS-level trade data transparency.** The measurement break in mineral data (Section 4.3) reflects data infrastructure limitations.
5. **Diversify export destinations** where economically feasible, reducing concentration risk in a single large buyer.
6. **Treat BRI participation as a trade-structure issue**, not solely an infrastructure issue. Infrastructure that facilitates bilateral trade may disproportionately benefit the more diversified partner.
7. **Evaluate 2023 as a potential structural inflection** requiring policy response rather than a statistical anomaly.
8. **Audit the 2020–2022 partner-level import statistics.** The gap between Kazakhstan's and China's records for those years (§4.7) is large enough to change how the bilateral position is perceived and should be reconciled by the statistical authorities.


# 8. Conclusion

This thesis examined whether strategic mineral exports from Kazakhstan to China translated into sustained bilateral trade-balance improvement during the post-BRI period. The answer is cautiously negative. Descriptive decomposition shows that imports from China grew nearly four times faster than exports (+94.3% vs. +24.3%), producing a 37.8% decline in the average trade balance despite 29.2% growth in strategic mineral exports. The trade-balance ratio—a normalised measure of bilateral position—fell by 51.2%.

The regression evidence (primary specification: GDP growth rates, VIF = 10.4) estimates a negative post-BRI × minerals interaction of −2.489 (one-sided *p* = 0.011, *R*² = 0.742, adjusted *R*² = 0.621). In the series as reported, this result depends on 2022–2023. Mirror-data validation shows that Kazakhstan-reported imports from China are under-recorded in 2020–2022. Correcting those imports keeps the interaction negative and significant when 2023 or 2022–2023 are excluded. The result is weaker when exports are adjusted as well (§6.20). Observed monthly data for 2010–2019 (*n* = 120) confirm H2 and H3 without any post-2019 observation, while interpolating the annual data to quarters adds no independent information (§6.17). Granger tests do not show that mineral exports lead the balance, and the monthly interaction disappears once bilateral oil exports are held constant (§6.18–6.19).

The cross-partner TWFE DiD (§6.15) shows that the post-2013 deterioration with China was the largest among Kazakhstan's six major partners (−0.305), robust in magnitude but statistically imprecise with only six partners. Observed monthly data show that oil exports to China collapsed after 2014, which is the most plausible mechanism behind the weakening of the mineral–balance association.

The thesis therefore identifies an increasingly adverse bilateral pattern, larger with China than with Kazakhstan's other major partners, that is consistent with asymmetric interdependence theory. The strongest empirical contributions are: the descriptive decomposition showing import-side deepening; the observed monthly evidence for H2 and H3; the identification of the oil-export collapse as a central mechanism; and the documentation of the 2020–2022 reporting break in Kazakhstan's import statistics.

## 8.1 Interpretation Discipline

To ensure analytical precision, it is necessary to stipulate what this thesis can and cannot claim. This thesis can claim that: (i) Kazakhstan–China trade-balance patterns are consistent with import-side deepening and asymmetric interdependence; (ii) strategic mineral export growth did not reliably translate into sustained bilateral balance improvement; and (iii) the post-2013 deterioration with China was the largest among Kazakhstan's major trading partners (§6.15), although with six partners this cannot be established with high statistical confidence. It can also claim (iv) that the weakening of the mineral–balance association after 2013 is observed in monthly data before 2020, and in annual data once the 2020–2022 import reporting gap is corrected. It cannot claim that BRI causally worsened Kazakhstan's trade balance: the post-BRI indicator coincides with the oil price collapse and the tenge devaluation, the interaction cannot be separated from oil export dynamics, Granger tests give no evidence that mineral exports drive the balance, and the 2022–2023 parallel-import channel remains an alternative explanation for the most recent years. All results, including the DiD, are conditional associations. 

## 8.2 Limitations and Future Research

This study is subject to several severe limitations that bound its inferential power. As a diagnostic case study, its main models rely on annual data (*n* = 24), which restricts statistical degrees of freedom. This limitation is partly addressed with 120 months of observed data for 2010–2019 (§6.18). Interpolating the annual data to quarters (*n* = 96) was tested and rejected as a source of independent evidence (§6.17). In the annual series as reported, the 2023 observation has extreme leverage and drives the interaction results. Much of that leverage reflects under-recorded imports in 2020–2022 (§4.7, §6.20). The mirror adjustment used to correct this is itself an estimate, and the result is weaker when exports are adjusted too. Furthermore, the 2022–2023 data likely capture sanctions-related trade diversion and parallel imports, presenting an alternative channel that weakens a narrow BRI-only interpretation. The narrow strategic mineral data contain a measurement break at 2014, and bilateral oil and energy export data are absent from the annual model. At monthly frequency, controlling for oil and energy exports removes the post-BRI mineral interaction (§6.18), so the H3 association cannot be shown to be mineral-specific. The cross-partner DiD rests on six partners, too few for precise inference, so it is treated as supporting rather than decisive evidence. Consequently, the strongest finding remains the descriptive pattern rather than any single regression coefficient.

Future research should extend the observed monthly series beyond 2019 once the 2020–2022 reporting gap is reconciled, separate mineral from energy export effects with a richer model, obtain consistent HS-6 mineral series for the full period, and apply synthetic control methods using a multi-partner donor pool. Ultimately, monitoring the post-2023 data will be essential to determine whether the bilateral deficit reflects a permanent structural shift or a transient sanctions-era disruption.

The finding that mineral export growth did not translate into trade-balance improvement is consistent with the broader resource-dependence literature: export success in raw materials does not automatically improve external balance when the trading partner's diversified export capacity grows faster. For Kazakhstan and comparable corridor economies, this diagnostic evidence suggests that BRI participation should be evaluated not by aggregate trade volumes but by the composition and balance of bilateral exchange.

# References

<div id="refs"></div>

# Appendix A: Tables and Figures Concordance

This appendix maps the figures and tables referenced in the text to their source files to ensure computational reproducibility.

| Table/Figure | Source File | Section Used | Purpose |
|--------------|-------------|--------------|---------|
| Table 4.1 | Author's compilation; see `Codebook.md` and `Collected_Raw_Data/data_dictionary.md` | 4.1 | Consolidated data sources and variable construction |
| Table 4.2 | `Outputs/generated_tables/summary_statistics.csv` | 4.5 | Descriptive statistics |
| Table 4.3 | `Outputs/generated_tables/trade_decomposition.csv` | 4.5 | Trade balance decomposition |
| Table 4.4 | N/A (Manual summary) | 4.3 | Measurement break summary |
| Table 4.5 | Author's calculations, Bureau of National Statistics (stat.gov.kz) | 4.4 | Independent cross-validation of bilateral trade figures |
| Table 5.1 | `Outputs/generated_tables/stationarity.csv` | 5.3 | Integration order diagnostics |
| Table 6.1 | `Outputs/generated_tables/full_regression_table.csv` & `parsimonious_regression.csv` | 6.1 | Baseline OLS results |
| Table 6.2 | Computed from OLS residuals via `Scripts/30_full_diagnostics.py`; DW and Breusch–Pagan statistics reported inline | 6.2 | Residual diagnostics |
| Table 6.3a/b | `Outputs/generated_tables/collinearity_resolution.csv` | 6.3 | VIF comparison across schemes |
| Table 6.3c | `Outputs/generated_tables/gravity_ratio_main_results.csv`; full run via `Scripts/35_collinearity_resolution.py` | 6.3 | Primary growth-rate specification and robustness schemes |
| Table 6.4 | `Outputs/generated_tables/influence_diagnostics.csv` | 6.4 | Cook's distance outliers |
| Table 6.5 | `Outputs/generated_tables/leave_one_out.csv` and model summaries | 6.4 | Model stability excluding 2023 |
| Table 6.6 | `Outputs/generated_tables/robustness.csv` | 6.8 | Robustness grid summary |
| Table 6.8 | `Outputs/generated_tables/structural_breaks.csv` | 6.13 | Chow placebo break-year tests |
| Table 6.9 | `Outputs/generated_tables/sanctions_channel.csv` | 6.14 | Sanctions robustness |
| Table 6.10 | `Outputs/generated_tables/did_partner_placebo.csv` | 6.15 | TWFE DiD partner-placebo results (China vs RUS, DEU, UZB, TUR, USA) |
| Table 6.10b | `Outputs/generated_tables/did_robustness.csv`; `did_permutation.csv`; `partner_import_break.csv` | 6.15 | DiD inference and sample robustness (Script 44) |
| Table 6.11 | `Outputs/generated_tables/synthetic_control.csv` | 6.16 | Synthetic control gap |
| Table 4.7 | `Collected_Raw_Data/processed/monthly_panel.csv` (summed by year) | 4.6 | Energy and mineral components of exports to China (Script 42) |
| Figure 1 | `Outputs/generated_figures/fig_1_exports_imports.png` | 4.5 | Exports vs imports over time |
| Figure 2 | `Outputs/generated_figures/fig_2_trade_balance.png` | 4.5 | Trade balance over time |
| Figure 3 | `Outputs/generated_figures/fig_3_minerals.png` | 4.5 | Strategic minerals over time |
| Figure 4 | `Outputs/generated_figures/fig_4_scatter.png` | 6.1 | Pre/post-BRI scatter plot |
| Figure 5 | `Outputs/generated_figures/fig_5_diagnostics.png` | 6.5 | Influence and leave-one-out stability |
| Figure 6 | `Outputs/generated_figures/fig_6_pre_post.png` | 6.8 | Pre/post coefficient robustness |
| Table 6.5b | `Outputs/generated_tables/ardl_clean.csv` | 6.7 | ADL and bounds tests on observed variables (Script 45) |
| Figure 6a | `Outputs/generated_figures/fig_cusum_clean.png` | 6.7 | CUSUM stability, parsimonious model (Script 45) |
| Figure 6b | `Outputs/generated_figures/fig_cusum_squares_clean.png` | 6.7 | CUSUM-of-squares stability (Script 45) |
| Figure DiD | `Outputs/generated_figures/fig_did_event_study.png` | 6.15 | ITS + placebo event study |
| Figure SC | `Outputs/generated_figures/fig_synthetic_control.png` | 6.16 | Synthetic control gap plot |
| Table 4.6 | `Outputs/generated_tables/import_break_evidence.csv` | 4.7 | Kazakhstan-reported vs China-reported imports (Script 43) |
| Table 6.1b | `Outputs/generated_tables/model_fit_statistics.csv` | 6.1 | Annual model fit statistics (Script 40) |
| Table 6.12 | `Outputs/generated_tables/quarterly_interpolated_results.csv` | 6.17 | Denton-interpolated quarterly models (Script 41) |
| Table 6.13 | `Outputs/generated_tables/interpolation_monte_carlo.csv` | 6.17 | Monte Carlo false-positive rates (Script 41) |
| Table 6.14 | `Outputs/generated_tables/monthly_results.csv`; `observed_quarterly_results.csv` | 6.18 | Observed monthly models (Script 42) |
| Table 6.15 | `Outputs/generated_tables/monthly_fit_statistics.csv` | 6.18 | Monthly fit statistics (Script 42) |
| Table 6.16 | `Outputs/generated_tables/granger_annual.csv` | 6.19 | Annual Granger tests (Script 40) |
| Table 6.17 | `Outputs/generated_tables/granger_monthly.csv` | 6.19 | Monthly Granger tests (Script 42) |
| Table 6.18 | `Outputs/generated_tables/import_break_sensitivity.csv`; `import_break_ratio_sensitivity.csv`; `granger_annual_adjusted.csv` | 6.20 | Sensitivity to the 2020–2022 reporting break (Script 43) |
| Table 6.19 | `Outputs/generated_tables/hypothesis_tests_formal.csv`; `monthly_hypothesis_tests.csv` | 6.11 | Formal hypothesis tests (Scripts 40, 42) |
| Table 6.20 | Summary of Tables 6.19, 6.14, 6.18 | 6.11 | Hypothesis verdicts |
| Figure 4.1 | `Outputs/generated_figures/fig_import_reporting_break.png` | 4.7 | Import reporting break (Script 43) |
| Figure 8 | `Outputs/generated_figures/fig_monthly_trade_balance.png` | 6.18 | Monthly trade balance and minerals (Script 42) |

# Appendix B: Pre-Revision Specification

*This appendix documents the pre-revision OLS specification that used log(KZ GDP) and log(CN GDP) as separate level regressors. It is retained for transparency, enabling direct comparison between the midterm and final specifications and illustrating how multicollinearity resolution affected the estimates.*

## Appendix B.1 Pre-Revision Full Model (A1)

The full model with GDP levels produced severe multicollinearity (max VIF = 236.3) that inflated coefficient magnitudes and destabilised inference. This specification is **not used for substantive interpretation** in the final thesis. It is retained here so that the revision from midterm to final is transparent and reproducible.

| Variable | Pre-revision A1 Coef. | HAC SE | *p*-value |
|----------|---------------------:|-------:|----------:|
| Constant | 197.624 | 53.040 | 0.002 |
| Minerals (USD bn) | 2.463 | 0.541 | 0.000 |
| Brent (USD/bbl) | 0.047 | 0.039 | 0.239 |
| KZT/USD | 0.016 | 0.012 | 0.198 |
| log(KZ GDP) | −13.230 | 6.112 | 0.046 |
| log(CN GDP) | 4.529 | 4.460 | 0.325 |
| Post-BRI | 4.927 | 1.847 | 0.017 |
| **Minerals × Post-BRI** | **−3.221** | **1.043** | **0.007** |
| N=24, R²=0.765, max VIF=236.3 | | | |

*Notes: The large constant (197.6), implausible GDP coefficient magnitudes, and max VIF > 100 indicate that this specification's coefficients absorb trending collinearity rather than identifying genuine partial effects. This specification is superseded by the growth-rate model (Scheme B, primary) and gravity-ratio model (Scheme C, robustness) in the final version.*

## Appendix B.2 Pre-Revision Parsimonious Model (A2)

The midterm parsimonious model excluded GDP controls, reducing VIF:

| Variable | Pre-revision A2 Coef. | HAC SE | *p*-value |
|----------|---------------------:|-------:|----------:|
| Constant | −3.326 | 2.359 | 0.176 |
| Minerals (USD bn) | 1.694 | 0.853 | 0.062 |
| Brent (USD/bbl) | 0.023 | 0.037 | 0.542 |
| KZT/USD | 0.014 | 0.012 | 0.270 |
| Post-BRI | 0.691 | 1.492 | 0.649 |
| **Minerals × Post-BRI** | **−2.382** | **0.977** | **0.025** |
| N=24, R²=0.703, max VIF=8.31 | | | |

*Notes: This specification achieved VIF < 10 by excluding GDP controls entirely. The final primary specification (Scheme B, GDP growth rates) retains GDP-related regressors in stationary form (d.log), achieving max VIF = 10.4. The Scheme C gravity-ratio specification is reported as a robustness check (max VIF = 33.4).*
