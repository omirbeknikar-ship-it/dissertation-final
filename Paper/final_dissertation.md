---
title: "The Belt and Road Initiative and Kazakhstan–China Trade: Export Composition, Strategic Minerals and the Bilateral Balance, 2005–2024"
subtitle: "Master's thesis (reconstructed version). Registered topic: BRI's Impact on Kazakhstan–China Trade Balance: The Role of Strategic Mineral Exports"
author: "Nikar Omirbek"
bibliography: ../Literature_Review/bibliography.bib
---

# Abstract

Kazakhstan's trade with China changed sharply after China announced the Silk Road Economic Belt in Astana in September 2013. In China's reported trade data, Kazakhstan's surplus with China of USD 3.5 billion in 2013 became a deficit of USD 3.9 billion in 2019 and USD 12.0 billion in 2024. Over the same years the composition of Kazakhstan's exports to China changed: oil fell from 62 to 22 per cent of the basket, while metals and ores, and agri-food products, rose. It is tempting to attribute both changes to the Belt and Road Initiative (BRI). This thesis asks a narrower and testable question: *was the post-2013 change in what Kazakhstan sells to China specific to China and timed with the BRI, or did it mirror changes in Kazakhstan's exports to the rest of the world and trends that began earlier?* The answer matters for how much of the bilateral trade-balance story the BRI can carry.

The thesis builds an HS-2 chapter panel of Kazakhstan's exports to China and to the rest of the world for 2005–2024 from UN Comtrade, cross-checked against China's mirror data and World Bank totals, and adds AidData's records of Chinese official finance. It uses an accounting decomposition of the bilateral balance, concentration indices and Poisson pseudo-maximum-likelihood (PPML) triple-difference and event-study models with product-by-year and product-by-destination fixed effects, which remove world prices and every shock common to all of Kazakhstan's markets.

Four findings stand out. First, the balance deterioration has two distinct phases: in 2013–2019 the balance fell by USD 7.4 billion while energy exports to China fell by USD 7.6 billion, and in 2019–2024 imports from China doubled (+USD 15.2 billion), which outweighed a USD 5.6 billion rise in metal and ore exports. Mineral exports to China grew, so they did not cause the deterioration. Second, the clearest China-specific change is in agri-food: relative to the rest of the world, Kazakhstan's agri-food exports to China grew by a factor of about 11.7 after 2013 (PPML coefficient 2.46, clustered SE 0.21). But this reorientation began in 2010–2012, before the BRI: placebo and pre-trend tests reject parallel trends, and its proportional growth rate slowed after 2013 (trend change −0.37 log points per year, *p* = 0.02). Third, the China orientation of metals and ores was flat between 2013 and 2019 and rose only in 2023–2024; energy fell more for China than for other markets after 2013. Fourth, recorded Chinese official finance to Kazakhstan peaked in 2008–2012, before the BRI, and went mostly to pipelines, oil and copper mines; post-2013 finance was smaller and shifted towards roads and border infrastructure. No agricultural project is recorded.

The evidence therefore supports a contextual role and an associational role for the BRI (BRI-era, China-specific changes exist), but not a causal claim: no China-specific break in export composition appears at 2013. The thesis also documents that Kazakhstan's own 2020–2022 statistics omit copper, zinc and aluminium exports and machinery imports at partner level, which makes mirror data indispensable for this relationship.

**Keywords:** Belt and Road Initiative; Kazakhstan–China trade; export composition; strategic minerals; trade balance; PPML; mirror statistics; asymmetric interdependence


# 1. Introduction

## 1.1 The Phenomenon

China is one of Kazakhstan's two most important trading partners. In 2023 it supplied 27.4 per cent of Kazakhstan's imports and took 18.7 per cent of its exports [@bns_2024_foreign_trade]. Kazakhstan is also where the BRI began: Xi Jinping proposed the Silk Road Economic Belt in a speech at Nazarbayev University in Astana on 7 September 2013 [@xinhua_chinadaily_2013]. Since then, a dry port at Khorgos on the Kazakhstan–China border has started operating (2015), Chinese state companies have taken a 49 per cent stake in it (2017) [@ktze_khorgos_2025], Chinese policy banks have financed road reconstruction across the country [@aiddata_gcdf3_2023], and the two governments have signed protocols that allow Kazakh agricultural products into the Chinese market [@astanatimes_agri_2023].

Over the same period the bilateral trade relationship changed in three visible ways (Chapter 6):

1. **The balance turned against Kazakhstan.** In China's reported data (UN Comtrade), Kazakhstan's surplus of USD 3.5 billion in 2013 became a deficit of USD 12.0 billion in 2024 (Table 6.1).
2. **The export basket changed.** Oil (HS 27) fell from 62 per cent of Kazakhstan's exports to China in 2013 to 22 per cent in 2024, by Kazakhstan's own data; metals and ores rose from 36 to 67 per cent, and agri-food from 0.5 to 6.6 per cent (Table 6.2).
3. **Imports from China more than doubled** between 2019 and 2024 (USD 12.7 billion to 28.0 billion, China-reported), led by apparel and footwear, machinery, vehicles and electrical equipment (Table 6.3).

## 1.2 The Puzzle

The timing invites a simple story: the BRI lowered trade costs between the two countries and reshaped their trade. Much of the policy discussion in both countries assumes such a story, and the earlier version of this thesis was built around a variant of it (Appendix B). The story faces an obvious problem. Kazakhstan's exports to *every* destination are dominated by oil and metals whose prices collapsed in 2014–2016 and recovered after 2020. A change in the composition of exports to China after 2013 could therefore be nothing more than the commodity cycle, visible in exports to every partner. It could also be the continuation of trends that began before 2013, for instance the opening of Chinese pipelines and Chinese-financed mines in 2005–2012.

The puzzle this thesis addresses is therefore the following. **Kazakhstan's exports to China changed in composition after 2013, but it is not known whether that change was specific to China, whether it started with the BRI, and what it implies for the bilateral balance.** Without answering this, statements about the "impact of the BRI" on Kazakhstan–China trade cannot be distinguished from statements about oil prices.

## 1.3 Research Question and Sub-Questions

**Research question.** *Did the composition of Kazakhstan's exports to China change after 2013 in a way that is specific to China and timed with the Belt and Road Initiative, rather than mirroring changes in its exports to the rest of the world or continuing earlier trends; and what does the answer imply for Kazakhstan's bilateral trade balance with China?*

The question is broken into four sub-questions:

- **SQ1 (accounting).** How did the bilateral balance change between 2013 and 2024, and which export groups and which side of trade account for the change?
- **SQ2 (China-specificity and timing).** After removing everything common to Kazakhstan's exports to all destinations, did the China orientation of energy, metals and ores, agri-food and other goods change after 2013? Did the change start in 2013–2014, or earlier?
- **SQ3 (BRI channels).** What did the BRI consist of in Kazakhstan in measurable terms (official finance, transport and border infrastructure, market-access agreements), and is the timing and sector of these channels consistent with the changes found under SQ2?
- **SQ4 (data reliability).** How reliable are the two countries' bilateral statistics, and how do reporting differences affect the answers?

## 1.4 The Role of the BRI in This Thesis

The thesis is required to give the BRI a real role and to be explicit about what kind of role the evidence supports. Three levels are distinguished throughout:

- **A. Context.** The BRI is the period and policy framework within which the trade relationship is observed.
- **B. Association with BRI-era mechanisms.** Changes that are specific to China and coincide in timing or sector with identifiable BRI-era channels (transport and border infrastructure, Chinese finance, market-access protocols).
- **C. Causal effect.** A change that would not have happened without the BRI, established by a design that rules out other China-specific explanations.

The design in Chapter 5 is built to move from A to B: it removes world prices and all destination-common shocks, and it tests timing. It cannot reach C, because there is no comparison country that was exposed to the same China-specific demand but not to the BRI, and because BRI channels in Kazakhstan are not separable from changes in China's own import demand (§5.6). The thesis therefore never claims C.

## 1.5 Aim and Objectives

**Aim.** To determine whether the post-2013 changes in Kazakhstan's exports to China were China-specific and BRI-timed, and to establish what they imply for the bilateral trade balance.

**Objectives.**

1. To review the literature on resource-based trade, trade costs and the BRI, the margins of export diversification, Chinese finance, and asymmetric interdependence (Chapter 2), and to derive competing, testable expectations (Chapter 3).
2. To build and validate an HS-2 panel of Kazakhstan's exports to China and to the rest of the world for 2005–2024, reconciled with China's mirror records and World Bank totals (Chapter 4).
3. To decompose the change in the bilateral balance by product group and trade direction (§6.1).
4. To test whether the China orientation of each product group changed after 2013, net of world prices and destination-common shocks, and whether any change began before 2013 (§6.2–6.5).
5. To compare the timing and sectors of measurable BRI channels with those results (§6.6).
6. To interpret the findings, including for strategic minerals and for the asymmetric-interdependence debate, and to derive policy implications (Chapters 7–8).

**Object and subject.** The *object* of the research is Kazakhstan–China bilateral trade. The *subject* is the composition of Kazakhstan's exports to China relative to its exports to other markets, and its relationship to the bilateral balance, before and after the BRI.

## 1.6 Significance and Novelty

**Scientific novelty.**

1. The thesis replaces the before-and-after comparison common in writing on the BRI and Kazakhstan with a design that compares Kazakhstan's exports of the same product, in the same year, to China and to the rest of the world. This removes commodity prices and Kazakhstan's own supply shocks.
2. It tests the *timing* of China-specific changes and shows that the largest of them, the agri-food reorientation, began before 2013 and slowed, in proportional terms, afterwards.
3. It decomposes the bilateral balance into an energy phase (2013–2019) and an import phase (2019–2024), and shows that strategic mineral exports rose in both, so they did not drive the deterioration.
4. It documents that Kazakhstan's partner-level statistics for 2020–2022 omit copper, zinc and aluminium exports and machinery, electrical and vehicle imports, and quantifies the consequences with China's mirror data.

**Practical significance.** The findings caution against reading BRI outcomes off bilateral turnover or the bilateral balance alone. They show which parts of the export basket did reorient towards China (agri-food) and that this followed market-access and demand changes more closely than recorded Chinese finance, which matters for where Kazakhstan directs export promotion. The statistical findings are directly relevant to the Bureau of National Statistics.

**Provisions submitted for defence.**

1. Kazakhstan's bilateral balance with China (China-reported) moved from +USD 3.5 billion (2013) to −USD 12.0 billion (2024). The 2013–2019 phase is accounted for by the fall in energy exports; the 2019–2024 phase by the rise in imports. Mineral exports to China rose in both phases.
2. Net of world prices and destination-common shocks, the only large China-specific change in export composition is the reorientation of agri-food exports towards China. It began in 2010–2012 and slowed in proportional terms after 2013, so it cannot be attributed to the BRI as a break.
3. Recorded Chinese official finance in Kazakhstan peaked before 2013 and was concentrated in hydrocarbons and mining; after 2013 it was smaller and shifted to transport. The evidence supports BRI as context and as association (levels A and B), not as a demonstrated cause (level C).
4. Kazakhstan's 2020–2022 partner-level statistics omit major metal exports and machinery imports; analysis of this relationship requires mirror data.

## 1.7 Structure

Chapter 2 reviews the literature. Chapter 3 sets out the theoretical framework and three competing expectations. Chapter 4 describes the data and their validation. Chapter 5 presents the empirical strategy. Chapter 6 reports the results. Chapter 7 discusses what they mean for the BRI, for strategic minerals and for the interdependence debate. Chapter 8 concludes. Appendix A documents the data and code, and Appendix B explains how this version relates to the earlier specification.


# 2. Literature Review

## 2.1 Resource-Based Trade and the Comparative-Advantage Null

Standard trade theory predicts that a resource-abundant economy such as Kazakhstan exports resource-intensive goods and imports manufactures from a labour- and capital-abundant economy such as China [@ricardo_1817; @heckscher_1919; @ohlin_1933]. In that framework neither the bilateral balance nor the share of a particular partner has welfare significance in itself. What matters for this thesis is the empirical implication: if Kazakhstan's comparative advantage and world prices determine what it exports, the composition of its exports should change in the same way for every destination. Any change in the composition of exports to China would then reflect world prices and Kazakhstan's own supply, not anything specific to China. This is the null hypothesis against which BRI-related claims must be tested.

The commodity-dependence literature explains why that null is demanding. Commodity prices are volatile and have long cycles [@harvey_etal_2010], resource booms affect the real exchange rate and non-resource sectors [@corden_neary_1982], and the developmental consequences of resource wealth depend on institutions and policy [@sachs_warner_1995; @vanderploeg_2011; @frankel_2010]. Export growth driven by resource volume can even reduce welfare when it worsens the terms of trade [@bhagwati_1958]. For Kazakhstan, the 2014–2016 oil price collapse alone could produce large changes in export composition, the bilateral balance and the exchange rate without any change in trade costs with China.

## 2.2 Trade Costs, Gravity and the BRI

Gravity models explain bilateral trade by economic size and bilateral trade costs relative to the trade costs each country faces with all partners [@anderson_vanwincoop_2003]. Poisson pseudo-maximum-likelihood (PPML) estimation of such models is now standard because it handles zero flows and heteroskedasticity [@santos_silva_tenreyro_2006]. The BRI literature applies this framework. De Soyres et al. [-@desoyres_etal_2019; -@desoyres_etal_2020] estimate that BRI transport projects reduce shipping times and trade costs, with gains concentrated along corridors. Baniya, Rocha and Ruta [-@baniya_rocha_ruta_2020] find that BRI-related improvements raise trade flows, more so when infrastructure is complemented by trade-policy reforms. Bird, Lebrand and Venables [-@bird_lebrand_venables_2020] model Central Asia specifically and show that gains from improved connectivity are uneven across locations and sectors.

Two limits of this literature matter here. First, most estimates are simulations or cross-country averages; they do not test what happened in one country pair. Second, they predict *more trade*, not a particular balance or composition. The trade-cost channel has a compositional implication only through the next strand of theory: lower trade costs matter most for products that were previously not traded or were traded little.

## 2.3 The Margins of Export Growth and Diversification

Models with heterogeneous firms imply that lower trade costs allow new, less productive firms and new products to enter a market [@melitz_2003], so that bilateral trade responds to trade costs mainly through the *extensive margin* of new products and firms [@chaney_2008]. Across countries, larger exporters export more varieties [@hummels_klenow_2005]. Diversification also follows a development pattern: production and exports diversify as income rises and re-concentrate only at high income levels [@imbs_wacziarg_2003; @cadot_carrere_strausskahn_2011]. These studies give the BRI trade-cost argument a specific, testable form: if BRI connectivity lowered the cost of reaching China, the gains should be largest for products that Kazakhstan exported little to China before, especially perishable or time-sensitive goods such as food, and the number of products exported to China should rise relative to other markets.

## 2.4 Chinese Finance and Resource Projects

A separate strand concerns Chinese official finance. China has become the largest official creditor to developing countries [@horn_reinhart_trebesch_2021], and BRI lending raised debt-sustainability concerns in several corridor economies [@hurley_morris_portelance_2018], although claims of systematic "debt-trap diplomacy" are not supported by the evidence [@brautigam_2020]. AidData's Global Chinese Development Finance Dataset records Chinese official commitments project by project for 2000–2021 [@aiddata_gcdf3_2023; @custer_etal_2023]. For Kazakhstan, the relevant question is whether Chinese finance went into export capacity, for instance mines and processing, and whether that capacity was then oriented towards China. Jepson and Baldakova [-@jepson_2024] study whether Chinese state capital supported resource-based structural transformation in Bolivia and Kazakhstan, and Calabrese [-@calabrese_2024] asks the same question for diversification in the Kyrgyz Republic. Global value chain research adds that suppliers in captive relationships often have limited scope for upgrading [@gereffi_humphrey_sturgeon_2005].

## 2.5 Kazakhstan, Central Asia and China

Area studies emphasise that the BRI in Central Asia is a broad label applied to projects, agreements and diplomatic initiatives of very different kinds [@laruelle_2018; @cooley_2012]. Pomfret [-@pomfret_2019] documents how Central Asian trade has been shaped by transport costs, trade policy and the Eurasian Economic Union, not only by China. Laruelle and Peyrouse [-@laruelle_peyrouse_2012] and Grant [-@grant_2020] show that the Chinese presence is received ambivalently in Kazakhstan, and Primiano and Kudebayeva [-@primiano_kudebayeva_2025] find uneven views of the BRI among Kazakh students. Rolland [-@rolland_2017] and Swaine [-@swaine_2015] describe the strategic purposes China attaches to the initiative. This literature is a warning against treating "the BRI" as a single treatment with a single start date.

## 2.6 Asymmetric Interdependence

Keohane and Nye [-@keohane_nye_1977] distinguish *sensitivity*, how quickly changes in one economy affect another, from *vulnerability*, the cost of adjusting when a relationship is disrupted. Hirschman [-@hirschman_1945] showed that trade can become a source of influence for the larger partner when the smaller partner's trade is concentrated on it and hard to redirect. This framework is frequently invoked for Kazakhstan–China relations. It does not, however, predict that trade concentration is harmful, or that it will be used as leverage; it predicts that the costs of disruption are distributed according to who can substitute more easily. Whether that is the case is an empirical question about both sides of the relationship, which most applications do not measure.

## 2.7 Research Gap

Three gaps follow. First, claims about the BRI's effect on Kazakhstan–China trade rest mainly on before-and-after comparisons that cannot separate the BRI from the commodity cycle. Second, the BRI trade-cost literature predicts compositional effects (extensive margin, time-sensitive goods), but none of the studies reviewed here tests them for the Kazakhstan–China pair against Kazakhstan's trade with other markets. Third, none of these studies checks the bilateral statistics themselves, even though the two countries' records diverge. This thesis addresses all three.


# 3. Theoretical Framework and Expectations

## 3.1 Framework

The framework combines a structural gravity view of bilateral trade [@anderson_vanwincoop_2003] with the extensive-margin argument [@melitz_2003; @chaney_2008]. Kazakhstan's exports of product *p* to destination *d* in year *t* depend on three sets of factors:

1. Factors common to all destinations for that product and year: world prices, Kazakhstan's output, its exchange rate and its export policy.
2. Persistent features of the product–destination pair: distance, pipelines and rail links that existed before 2013, and long-standing contracts.
3. Changes specific to the destination over time, which can differ by product: for China, these include BRI-era infrastructure and border facilitation, sanitary and phytosanitary market access, Chinese investment and finance, and changes in China's own import demand.

Only the third set can carry a BRI effect. The empirical design (Chapter 5) removes the first two with fixed effects and estimates the third by product group.

## 3.2 Competing Expectations

Three expectations are compared. They make different predictions about *which* product groups reorient towards China and *when*.

**E0, commodity cycle and comparative advantage (null).** Changes in the composition of exports to China mirror changes in exports to the rest of the world. Net of product-by-year effects, the China orientation of each product group is unchanged after 2013.

**E1, connectivity and market access.** BRI-era transport, border and market-access improvements lower the cost of reaching China most for goods that were previously little traded with China and for time-sensitive goods. Prediction: a China-specific increase concentrated in agri-food and other non-resource goods, a rise in the number of products exported to China relative to other markets, and a change in trend that starts in 2014 or soon after (2015 for Khorgos, 2017 onward for later agreements).

**E2, resource security and finance.** Chinese finance and investment expand Kazakhstan's capacity in hydrocarbons and metals and direct that output to China. Prediction: a China-specific increase in energy and metals and ores, timed with the completion of Chinese-financed projects.

These expectations are not mutually exclusive, and none of them assumes that a change in composition is good or bad for Kazakhstan.

## 3.3 What Would Count as Evidence

- Support for E0: China × post coefficients near zero for all groups.
- Support for E1: a positive China × post coefficient for agri-food and other goods, no pre-2013 trend, and a positive extensive-margin effect.
- Support for E2: positive China × post coefficients for energy and metals and ores, timed with project completion.
- A BRI interpretation at level B requires that the China-specific change begins after 2013. A change that begins earlier, or continues an earlier trend at the same or a lower rate, is evidence against attributing it to the BRI, even if it is China-specific.

**Disclosure.** The expectations were written after the author had seen aggregate data on Kazakhstan–China trade (the earlier version of this thesis used annual and monthly totals, and monthly oil data). The product-by-destination panel and all tests in Chapters 5–6 were built and run after the expectations and the decision rules above were fixed. Readers should nonetheless treat the analysis as confirmatory only for the specific tests listed here.

## 3.4 Where Asymmetric Interdependence Fits

Asymmetric interdependence is used in Chapter 7 as an interpretive framework, not as a hypothesis tested by the regressions. The regressions measure how Kazakhstan's export structure changed; they say nothing about bargaining power. Chapter 7 uses the results, together with indicators of China's dependence on Kazakhstan, to ask which side of the relationship would bear more of the cost of disruption in each product group. This avoids the assumption, common in the literature, that concentration of trade with China implies Chinese leverage.


# 4. Data

## 4.1 Sources

All trade data come from the UN Comtrade database, retrieved through its public preview API on 31 October 2026 [@un_comtrade_hs2_2026]. Every value used is transcribed in a raw text file in `Collected_Raw_Data/raw_downloads/`, with the query URL, reporter, partner, flow, units and retrieval date in the file header (Appendix A). Table 4.1 lists the series.

**Table 4.1. Data series**

| Series | Reporter → partner | Flow | Valuation | HS level | Years | File |
|---|---|---|---|---|---|---|
| Kazakhstan's exports to China | Kazakhstan (398) → China (156) | Exports | FOB | HS-2 | 2005–2024 | `comtrade_hs2_kaz_exports_to_china.txt` |
| Kazakhstan's exports to the world | Kazakhstan → World (0) | Exports | FOB | HS-2 | 2005–2024 except 2020, 2022 | `comtrade_hs2_kaz_exports_to_world.txt` (+ gap-fill file) |
| China's imports from Kazakhstan (mirror) | China → Kazakhstan | Imports | CIF | HS-2 | 2005–2024 except 2006 | `comtrade_hs2_chn_imports_from_kaz.txt` |
| China's exports to Kazakhstan (mirror of Kazakhstan's imports) | China → Kazakhstan | Exports | FOB | HS-2 | 2013, 2019, 2024 | `comtrade_hs2_chn_exports_to_kaz.txt` |
| Kazakhstan's exports to Russia, HS 84, 85, 87 | Kazakhstan → Russia (643) | Exports | FOB | HS-2 | 2019, 2023 | `comtrade_hs2_kaz_exports_to_russia_selected.txt` |
| Merchandise exports, total | World Bank WDI | Exports | | Total | 2005–2024 | `wdi_kaz_merch_exports.csv` [@wdi_2026] |
| Chinese official finance commitments | AidData GCDF 3.0 | Commitments | Constant 2021 USD | Project | 2000–2021 | `aiddata_gcdf_v3.xlsx` [@aiddata_gcdf3_2023] |

*Values are in current US dollars unless stated. HS chapters are those reported (HS 2002 to HS 2022 vintages); chapter boundaries are stable across these vintages at the two-digit level.*

Data were retrieved year by year because the public API returns one period per call. Where the retrieval tool truncated a long response, the missing chapters were identified by comparison with neighbouring years and re-queried explicitly; these are recorded in a separate gap-fill file. One response (Kazakhstan to World, 2022) was rejected because its tail contained duplicated values and omitted the two largest chapters; Kazakhstan-to-World data for 2020 could not be retrieved. As §4.4 shows, 2020–2022 would have been excluded in any case.

## 4.2 Product Groups

The 97 HS chapters are grouped into four groups. **Energy** is HS 27 (crude oil, gas, coal and products). **Metals and ores** are HS 25, 26, 28, 71, 72 and 74–81: salt and minerals, ores and concentrates, inorganic chemicals including uranium compounds (HS 2844), precious metals, iron and steel including ferroalloys, and base metals (copper, nickel, aluminium, lead, zinc, tin and others). **Agri-food** is HS 01–24. **Other goods** are all remaining chapters, mainly chemicals, plastics, textiles, metal articles, machinery and vehicles. The "strategic minerals" of the registered topic (uranium, copper, ores and ferroalloys) fall inside the metals and ores group and are reported separately where relevant (§6.2). Energy is a single chapter, which matters for inference (§5.5).

## 4.3 Validation Against Independent Totals

Table 4.2 compares the sum of Kazakhstan's reported HS-2 exports to the world with the World Bank's merchandise export totals, and Kazakhstan's reported exports to China with China's reported imports from Kazakhstan.

**Table 4.2. Validation of the HS-2 data (USD bn)**

| Year | KZ exports to world, sum of chapters | WDI merchandise exports | Ratio, % | KZ-reported exports to China | China-reported imports from KZ | Mirror ratio |
|---|---:|---:|---:|---:|---:|---:|
| 2005 | 27.85 | 27.85 | 100.0 | 2.42 | 2.91 | 1.20 |
| 2008 | 71.17 | 71.17 | 100.0 | 7.68 | 7.73 | 1.01 |
| 2010 | 57.24 | 59.97 | 95.5 | 10.12 | 11.11 | 1.10 |
| 2011 | 88.10 | 84.34 | 104.5 | 16.29 | 15.35 | 0.94 |
| 2012 | 92.28 | 86.45 | 106.7 | 16.48 | 14.68 | 0.89 |
| 2013 | 84.66 | 84.70 | 100.0 | 14.37 | 16.05 | 1.12 |
| 2016 | 36.74 | 36.69 | 100.1 | 4.22 | 4.81 | 1.14 |
| 2019 | 58.07 | 57.31 | 101.3 | 8.00 | 8.86 | 1.11 |
| 2020 | n/a | 46.45 | | 6.84 | 10.37 | **1.52** |
| 2021 | 53.07 | 60.63 | **87.5** | 6.85 | 11.29 | **1.65** |
| 2022 | n/a | 84.59 | | 10.46 | 14.82 | **1.42** |
| 2023 | 78.74 | 78.53 | 100.3 | 14.76 | 16.36 | 1.11 |
| 2024 | 81.61 | 82.47 | 99.0 | 14.90 | 15.91 | 1.07 |

*Source: UN Comtrade [@un_comtrade_hs2_2026]; World Bank [@wdi_2026]. Author's calculations (Script 60, `hs2_validation.csv`; all years in the file). Mirror ratio = China-reported imports (CIF) / Kazakhstan-reported exports (FOB).*

In most years the chapter sums match the World Bank totals within about 1 per cent, which confirms that the transcribed data are complete. The exceptions are informative. In 2011–2012 Comtrade's totals exceed the World Bank's by 4–7 per cent; this is a difference between the two publishers' totals that affects both destinations equally and is absorbed by the fixed effects in Chapter 5. In 2010 the chapter sum is 4.5 per cent below the WDI total; the cause could not be identified. In 2021 it is 12.5 per cent below, which is explained by the suppression described in §4.4.

The mirror ratio of 1.0–1.2 in normal years is what one expects when one side reports CIF and the other FOB. In 2020–2022 it jumps to 1.4–1.65.

## 4.4 A Reporting Break: Suppressed Chapters in 2020–2022

The jump in the mirror ratio has a precise cause. In Kazakhstan's own partner-level data for 2020–2022, exports to China of copper (HS 74), aluminium (HS 76) and zinc (HS 79) are absent, although China reports importing USD 1.8–2.5 billion of Kazakh copper in each of those years (Table 4.3). In 2021, Kazakhstan's reported copper exports to the *world* are only USD 0.11 billion, against USD 2.7 billion in 2019 and USD 3.2 billion in 2023. The same pattern was found earlier for imports: Kazakhstan's partner-level records for 2020–2022 contain no machinery (HS 84), electrical equipment (HS 85) or vehicle (HS 87) imports from China, and its reported imports from China fall by about 70 per cent in 2020 while China's reported exports to Kazakhstan fall by 8 per cent (Appendix B, Table B.2).

**Table 4.3. Copper, aluminium and zinc exports to China by reporter (USD million)**

| Year | Copper: KZ-reported | Copper: China-reported | Zinc: KZ-reported | Zinc: China-reported |
|---|---:|---:|---:|---:|
| 2017 | 1,110 | 1,230 | 333 | 340 |
| 2018 | 1,365 | 1,470 | 167 | 558 |
| 2019 | 1,567 | 1,743 | 563 | 623 |
| 2020 | not reported | 1,834 | not reported | 450 |
| 2021 | not reported | 2,451 | not reported | 586 |
| 2022 | not reported | 2,388 | not reported | 33 |
| 2023 | 1,912 | 2,160 | 270 | 315 |
| 2024 | 2,695 | 2,742 | 327 | 413 |

*Source: UN Comtrade [@un_comtrade_hs2_2026]. Author's calculations (Script 61, `mirror_suppression.csv`).*

The pattern is consistent with confidentiality suppression of chapters dominated by few firms, but the reason cannot be confirmed from the data. Two consequences follow. First, Kazakhstan-reported product-level data for 2020–2022 are excluded from all comparisons of China with the rest of the world. Second, the bilateral balance is computed from China's records, which show no such gaps (§6.1). The main results are re-estimated with China's mirror data for the China side (§6.5).

## 4.5 The Persistent Import Gap

China's reported exports to Kazakhstan have long exceeded Kazakhstan's reported imports from China: by a factor of 1.5 to 2.5 in 2013–2019, before the 2020–2022 break (Appendix B, Table B.2). This gap is much larger than a CIF/FOB difference. It may reflect goods declared differently at the border, transit through the Eurasian Economic Union customs territory, or under-declaration; the data cannot distinguish these. For this reason the thesis does not use Kazakhstan's import figures to measure the balance. All balance figures in Chapter 6 are China-reported (China's imports from Kazakhstan minus China's exports to Kazakhstan), and are therefore not comparable in level with figures published by Kazakhstan's Bureau of National Statistics.

## 4.6 Chinese Official Finance

AidData's GCDF 3.0 records 155 Chinese official finance projects in Kazakhstan with commitments in 2000–2021 that AidData recommends for aggregate analysis [@aiddata_gcdf3_2023; @custer_etal_2023]. Amounts are in constant 2021 US dollars. The data record commitments, not disbursements, and they cover official finance only, not private Chinese investment. Syndicated loans appear as one record per lender. These limitations mean the data can show where and when Chinese state finance was committed, but not how much was spent or what it produced.


# 5. Empirical Strategy

## 5.1 Accounting Decomposition (SQ1)

The change in Kazakhstan's bilateral balance between two years is split into the change in exports to China by product group and the change in imports from China:

$$\Delta B = \sum_{g} \Delta X^{CN}_{g} - \Delta M^{CN},$$

where all terms are China-reported. This is an identity and implies no causal statement. It shows which components moved.

## 5.2 Shares and Concentration (SQ2, descriptive)

For each product group and year, China's share of Kazakhstan's exports is computed from Kazakhstan's data. The concentration of the export basket to China and to the rest of the world is measured by the Herfindahl–Hirschman index across HS-2 chapters, with and without HS 27, and by the number of chapters with exports above USD 1 million, a crude measure of the extensive margin at the chapter level.

## 5.3 Triple-Difference PPML (SQ2, main test)

The main model compares, within each HS-2 chapter and year, Kazakhstan's exports to China with its exports to the rest of the world (RoW = world minus China):

$$X_{pdt} = \exp\Big(\alpha_{pt} + \gamma_{pd} + \sum_{g} \beta_{g}\,(\text{China}_d \times \text{Post}_t \times G_{pg})\Big)\,\varepsilon_{pdt},$$

where *p* is the chapter, *d* ∈ {China, RoW}, *t* is the year, Post = 1 from 2014, and *G* indicates the four product groups.

- The **product-by-year effects** α~pt~ absorb everything that affects exports of a chapter to all destinations in a given year: world prices, Kazakhstan's production, its exchange rate and export policy. This is what removes the commodity cycle.
- The **product-by-destination effects** γ~pd~ absorb the average pre-2014 orientation of each chapter towards China, for instance the existence of the oil pipeline.
- **β~g~** measures the post-2013 change in the China/RoW ratio for group *g*, relative to its pre-2014 average. A value of β means that the ratio changed by a factor of exp(β).

The model is estimated by PPML, which keeps zero flows and is consistent under heteroskedasticity [@santos_silva_tenreyro_2006], using `pyfixest`. Standard errors are clustered by HS-2 chapter. Chapter–destination pairs that are zero in every year carry no information and are dropped. The main sample is 2005–2019 and 2023–2024 (17 years, 97 chapters, 3,160 observations).

Under E0 all β~g~ are zero. Under E1, β is positive for agri-food and other goods. Under E2, β is positive for energy and metals and ores.

## 5.4 Event Study, Pre-Trends and Trend Breaks (SQ2, timing)

Replacing Post with year dummies gives an event study of the China/RoW ratio for each group, relative to 2013. Coefficients before 2013 test whether a change was already under way. A joint Wald test is applied to the pre-2013 coefficients for agri-food. Because the post-2013 coefficient in §5.3 compares post-2013 levels with the *pre-2013 average*, it will be positive whenever there is an upward trend, whether or not the trend started with the BRI. The decisive test of timing is therefore a trend-break model:

$$X_{pdt} = \exp\big(\alpha_{pt} + \gamma_{pd} + \sum_{g}[\theta_{g}\,\text{China}_d G_{pg}(t-2013) + \delta_{g}\,\text{China}_d G_{pg}(t-2013)\text{Post}_t]\big)\varepsilon_{pdt}.$$

θ~g~ is the pre-2013 China-specific trend and δ~g~ its change after 2013. A BRI effect at level B would show up as δ~g~ > 0.

## 5.5 Extensive Margin and Inference

The extensive margin is tested with a linear probability model of the indicator *X*~pdt~ > USD 1 million, with the same fixed effects. Two inferential limits apply. Energy consists of one chapter, so its coefficients rest on one cluster and clustered standard errors are not defined; energy results are reported as point estimates only. Agri-food rests on 24 chapters, metals and ores on 12 and other goods on 60, so cluster-robust inference is approximate for metals and ores.

## 5.6 Robustness and Identification Limits

The main model is re-estimated (i) with China's mirror imports as the China leg, (ii) without 2023–2024, to remove the period after the 2022 sanctions on Russia, (iii) with Post starting in 2015 (Khorgos dry port) and 2017, (iv) without gold (HS 71), (v) only for chapters with mean exports above USD 1 million, and (vi) as a placebo with a false start in 2010 on 2005–2013 data.

The design identifies China-specific change. It does not identify which China-specific factor caused it. A rise in China's own demand for Kazakh sunflower oil, a phytosanitary protocol, a faster border crossing and a Chinese-financed road would all produce the same coefficient. Separating them would require product-level data on protocols and transport times, or a comparison country exposed to the same Chinese demand without BRI investment; neither is available here. This is why results are interpreted at level B at most.


# 6. Results

## 6.1 The Bilateral Balance: Two Phases (SQ1)

**Table 6.1. Kazakhstan's trade with China, China-reported data (USD bn)**

| | 2013 | 2019 | 2024 |
|---|---:|---:|---:|
| Kazakhstan's exports to China (China's imports, CIF) | 16.05 | 8.86 | 15.91 |
| Kazakhstan's imports from China (China's exports, FOB) | 12.55 | 12.73 | 27.95 |
| Balance for Kazakhstan | +3.51 | −3.87 | −12.04 |

*Source: UN Comtrade, China as reporter [@un_comtrade_hs2_2026]. Author's calculations (Script 61, `trade_balance_decomposition.csv`).*

**Table 6.1b. Decomposition of the change in the balance (USD bn)**

| Component | 2013→2019 | 2019→2024 | 2013→2024 |
|---|---:|---:|---:|
| Energy exports | −7.56 | +0.36 | −7.20 |
| Metals and ores exports | +0.06 | +5.56 | +5.62 |
| Agri-food exports | +0.30 | +0.56 | +0.86 |
| Other exports | +0.02 | +0.57 | +0.59 |
| Imports from China (enters with a minus sign) | +0.18 | +15.23 | +15.41 |
| **Change in balance** | **−7.37** | **−8.18** | **−15.55** |

*Source: as Table 6.1.*

The deterioration has two phases with different causes (Figure 6.1). Between 2013 and 2019, the balance fell by USD 7.4 billion, and the fall in energy exports (USD 7.6 billion) accounts for all of it; imports were flat. Between 2019 and 2024, the balance fell by a further USD 8.2 billion, even though exports to China rose by USD 7.0 billion, because imports from China rose by USD 15.2 billion. Exports of metals and ores to China did not fall in either phase; they rose by USD 5.6 billion over 2013–2024. The bilateral deterioration is therefore not the result of weak mineral exports.

![Figure 6.1. Decomposition of the change in Kazakhstan's balance with China, 2013–2024](../Outputs/generated_figures/fig_r4_balance_decomposition.png)

**Table 6.2b. Kazakhstan's imports from China by main chapter, China-reported (USD bn)**

| Chapters | 2013 | 2019 | 2024 |
|---|---:|---:|---:|
| Apparel and footwear (HS 61, 62, 64) | 4.24 | 3.28 | 7.67 |
| Machinery (HS 84) | 1.83 | 1.56 | 4.38 |
| Vehicles (HS 87) | 0.80 | 0.69 | 3.54 |
| Electrical equipment (HS 85) | 0.97 | 1.49 | 3.01 |
| Furniture, toys, miscellaneous (HS 94–96) | 0.46 | 1.21 | 2.05 |
| Plastics and rubber (HS 39–40) | 0.58 | 0.61 | 1.43 |
| Iron and steel articles (HS 73) | 0.77 | 0.60 | 0.83 |
| All other chapters | 2.90 | 3.30 | 5.04 |
| **Total** | **12.55** | **12.73** | **27.95** |

*Source: UN Comtrade, China as reporter. Author's calculations (Script 61, `import_composition_china_reported.csv`).*

The import surge after 2019 is broad. Consumer goods (apparel and footwear) and capital and durable goods (machinery, vehicles, electrical equipment) all roughly doubled or more. Part of the rise may be goods that pass through Kazakhstan to Russia: Kazakhstan's own reported exports of machinery, electrical equipment and vehicles to Russia rose from USD 0.33 billion in 2019 to USD 2.25 billion in 2023, and to the world from USD 0.67 billion to USD 3.56 billion (`russia_manufactures_check.csv`). Comtrade does not record the origin of re-exported goods, so the share of Chinese goods in that flow cannot be measured here. The import side is therefore described, not explained, in this thesis (§8.2).

## 6.2 Composition of Exports and China's Share (SQ2, descriptive)

**Table 6.2. Kazakhstan's exports to China by product group (Kazakhstan-reported)**

| Year | Total, USD bn | Energy | Metals and ores | Agri-food | Other |
|---|---:|---:|---:|---:|---:|
| 2005 | 2.42 | 20.2% | 66.7% | 0.2% | 12.9% |
| 2008 | 7.68 | 57.6% | 36.4% | 0.0% | 6.0% |
| 2013 | 14.37 | 62.0% | 36.4% | 0.5% | 1.1% |
| 2016 | 4.22 | 24.0% | 70.9% | 3.1% | 2.0% |
| 2019 | 8.00 | 35.3% | 58.3% | 4.6% | 1.8% |
| 2023 | 14.76 | 36.0% | 54.8% | 6.5% | 2.7% |
| 2024 | 14.90 | 22.0% | 67.0% | 6.6% | 4.4% |

*Source: UN Comtrade, Kazakhstan as reporter. Author's calculations (Script 61, `composition_kz_exports_to_china.csv`, which also gives the China-reported shares; the two sources differ by up to 10 percentage points in individual years, mainly because of CIF/FOB valuation and timing, but show the same direction of change).*

![Figure 6.2. Kazakhstan's exports to China by product group, China-reported, 2005–2024](../Outputs/generated_figures/fig_r1_composition_china.png)

Composition alone cannot tell us whether anything China-specific happened, because exports to every market went through the same commodity cycle. Figure 6.3 and Table 6.3 therefore show China's *share* of Kazakhstan's exports in each group.

**Table 6.3. China's share of Kazakhstan's exports by product group, % (Kazakhstan-reported)**

| Year | Energy | Metals and ores | Agri-food | Other | All goods |
|---|---:|---:|---:|---:|---:|
| 2005 | 2.5 | 24.5 | 0.7 | 30.1 | 8.7 |
| 2008 | 9.0 | 16.7 | 0.1 | 18.3 | 10.8 |
| 2010 | 13.5 | 33.7 | 0.8 | 6.8 | 17.7 |
| 2012 | 14.1 | 33.0 | 1.9 | 2.3 | 17.9 |
| 2013 | 13.8 | 34.8 | 2.5 | 6.8 | 17.0 |
| 2016 | 4.5 | 28.2 | 6.1 | 4.9 | 11.5 |
| 2019 | 7.4 | 33.4 | 11.1 | 6.0 | 13.8 |
| 2023 | 11.4 | 39.9 | 18.0 | 6.0 | 18.7 |
| 2024 | 7.1 | 44.2 | 19.4 | 8.5 | 18.3 |

*Source: as Table 6.2 (`china_share_by_group.csv`, all years). 2020–2022 omitted (§4.4).*

![Figure 6.3. China's share of Kazakhstan's exports by product group](../Outputs/generated_figures/fig_r2_china_share_by_group.png)

Three patterns are visible. China's share of Kazakhstan's energy exports rose from 2.5 to 14–15 per cent between 2005 and 2011, then fell back to 3–7.4 per cent in 2016–2019. China's share of metals and ores rose from 17 to 34 per cent between 2008 and 2010 and then stayed at 28–35 per cent until 2019; it rose to 40–44 per cent only in 2023–2024. China's share of agri-food rose steadily, from below 1 per cent before 2011 to 2.5 per cent in 2013, 11 per cent in 2019 and 19 per cent in 2024. Overall, China's share of Kazakhstan's exports in 2024 (18.3 per cent) was close to its level in 2010–2013 (17–18 per cent).

**Strategic minerals.** Within metals and ores, China's share of Kazakhstan's ore exports (HS 26) rose from 44 per cent in 2013 and 41 per cent in 2019 to 80 per cent in 2024; its share of copper (HS 74) rose from 56 to 64 per cent; and its share of inorganic chemicals including uranium compounds (HS 28) fell from 42 per cent in 2013 to 23 per cent in 2019 and was 32 per cent in 2024 (Script 61). The large post-2019 increase in ores occurred after the period in which BRI connectivity projects were built, and coincides with the post-2022 reorganisation of trade in the region; the data used here cannot establish its cause.

**Concentration.** The concentration of Kazakhstan's exports to China fell sharply: the HHI across chapters fell from 0.415 in 2013 to 0.203 in 2019 and 0.173 in 2024, and the share of the top three chapters from 83 to 67 per cent (`diversification_indices.csv`). Almost all of this is the fall of oil. Excluding HS 27, the HHI was 0.212 in 2013, 0.187 in 2019 and 0.205 in 2024: the non-oil basket to China did not become less concentrated. Non-resource goods (agri-food and other) rose from 1.5 to 11.0 per cent of exports to China between 2013 and 2024, compared with 6.8 to 16.7 per cent of exports to the rest of the world. The number of chapters with exports above USD 1 million to China rose from 15–20 in 2005–2010 to 26 in 2013, 31 in 2019 and 36 in 2024; to the rest of the world it rose from 60–64 to 70, 74 and 84.

![Figure 6.4. Concentration (HHI) of Kazakhstan's exports to China and to the rest of the world](../Outputs/generated_figures/fig_r6_hhi.png)

## 6.3 Was the Change China-Specific? (SQ2, main test)

**Table 6.4. PPML triple-difference: change in the China/RoW export ratio after 2013, by product group**

| Sample | N | Energy | Metals and ores | Agri-food | Other |
|---|---:|---:|---:|---:|---:|
| (1) Main: KZ-reported, 2005–19 and 2023–24 | 3,160 | −0.528 [n/a] | 0.329 (0.074)\*\*\* | 2.456 (0.213)\*\*\* | 0.634 (0.522) |
| (2) Mirror: China-reported imports for China leg | 2,754 | −0.659 [n/a] | 0.436 (0.112)\*\*\* | 2.307 (0.292)\*\*\* | 1.144 (0.628)\* |
| (3) 2005–2019 only | 2,784 | −0.669 [n/a] | 0.154 (0.096) | 1.986 (0.250)\*\*\* | 0.194 (0.379) |
| (4) Post from 2015 | 3,160 | −0.539 [n/a] | 0.319 (0.100)\*\*\* | 2.120 (0.206)\*\*\* | 0.508 (0.544) |
| (5) Post from 2017 | 3,160 | −0.446 [n/a] | 0.381 (0.149)\*\* | 1.827 (0.184)\*\*\* | 0.594 (0.540) |
| (6) Excluding HS 71 | 3,126 | −0.528 [n/a] | 0.328 (0.074)\*\*\* | 2.456 (0.213)\*\*\* | 0.634 (0.522) |
| (7) Chapters with mean > USD 1m | 2,532 | −0.528 [n/a] | 0.329 (0.074)\*\*\* | 2.462 (0.214)\*\*\* | 0.640 (0.523) |
| (8) Placebo: 2005–2013, false post = 2010 | 1,617 | 0.722 [n/a] | 0.663 (0.162)\*\*\* | 2.607 (0.876)\*\*\* | −0.228 (0.733) |

*Coefficients on China × Post × group. All models include chapter-by-year and chapter-by-destination fixed effects. Standard errors clustered by HS-2 chapter in parentheses. \*\*\* p < 0.01, \*\* p < 0.05, \* p < 0.1. Energy is a single chapter, so no standard error can be computed [n/a]. Source: Script 62, `ppml_main.csv`.*

Read at face value, the main model (row 1) rejects E0 for three of four groups. Relative to the rest of the world and to the pre-2014 average, the China ratio fell by 41 per cent for energy (exp(−0.528) − 1), rose by 39 per cent for metals and ores and rose by a factor of 11.7 for agri-food. There is no significant change for other goods. The agri-food and metals results hold with China's mirror data (row 2) and with later start dates (rows 4–5). This looks like support for E1 in agri-food.

Two results in the same table qualify that reading at once. The metals and ores coefficient falls to 0.154 and loses significance when 2023–2024 are excluded (row 3): the metals result depends on the two most recent years. And the placebo (row 8), which pretends the BRI started in 2010 and uses only pre-BRI years, finds a large "effect" for agri-food (2.61) and metals and ores (0.66). Something was already changing before 2013. The next section examines timing directly.

## 6.4 When Did the Change Begin? (SQ2, timing)

![Figure 6.5. Event study: China/RoW export ratio by product group relative to 2013](../Outputs/generated_figures/fig_r3_event_study.png)

**Table 6.5. Event-study coefficients (log China/RoW ratio relative to 2013)**

| Year | Agri-food | Metals and ores | Energy |
|---|---:|---:|---:|
| 2005 | −1.83 (0.70) | −0.56 (0.32) | −1.83 |
| 2008 | −3.37 (0.91) | −0.99 (0.22) | −0.48 |
| 2010 | −1.21 (0.14) | 0.04 (0.20) | −0.03 |
| 2011 | −1.65 (0.21) | −0.14 (0.07) | 0.11 |
| 2012 | −0.36 (0.31) | −0.04 (0.20) | 0.03 |
| 2013 | 0 | 0 | 0 |
| 2014 | 0.57 (0.14) | −0.10 (0.10) | −0.54 |
| 2016 | 0.93 (0.27) | −0.27 (0.15) | −1.21 |
| 2017 | 0.98 (0.30) | −0.09 (0.17) | −1.56 |
| 2019 | 1.45 (0.37) | −0.12 (0.21) | −0.70 |
| 2023 | 2.05 (0.11) | 0.18 (0.36) | −0.21 |
| 2024 | 2.07 (0.24) | 0.36 (0.35) | −0.74 |

*PPML with chapter-by-year and chapter-by-destination fixed effects; SE clustered by chapter in parentheses (none for energy). All years in `ppml_event_study.csv` (Script 62).*

**Agri-food.** The China/RoW ratio was already rising steeply before the BRI: from −3.37 in 2008 to −1.21 in 2010 and −0.36 in 2012, relative to 2013. The pre-2013 coefficients are jointly different from zero (Wald χ²(8) = 664, *p* < 0.001; `ppml_pretrend_test.csv`). After 2013 the ratio continued to rise, but more slowly.

**Table 6.6. Trend-break test: China-specific trend before and after 2013 (log points per year)**

| Group | Chapters | Pre-2013 trend θ | Change after 2013 δ | Post-2013 trend θ + δ |
|---|---:|---:|---:|---:|
| Agri-food | 24 | 0.538 (*p* < 0.001) | −0.368 (SE 0.157, *p* = 0.020) | 0.170 (SE 0.026) |
| Metals and ores | 12 | 0.095 (*p* = 0.006) | −0.070 (SE 0.063, *p* = 0.264) | 0.025 (SE 0.031) |
| Other | 60 | −0.017 (*p* = 0.858) | 0.107 (SE 0.138, *p* = 0.437) | 0.090 (SE 0.067) |
| Energy | 1 | 0.068 [n/a] | −0.134 [n/a] | −0.066 [n/a] |

*PPML with chapter-by-year and chapter-by-destination fixed effects; SE clustered by chapter. Source: Script 62, `ppml_trend_break.csv`.*

The China-specific trend in agri-food was 0.54 log points per year before 2013 and 0.17 after; the slowdown is statistically significant (*p* = 0.02). In proportional terms, then, the reorientation of agri-food towards China began before the BRI and slowed after it. This is the opposite of what a BRI break would produce.

Proportional rates can mislead when the starting base is very small, and here it was: Kazakhstan's agri-food exports to China were USD 4 million in 2005 and USD 70 million in 2013. In absolute terms most of the growth came after 2013, to USD 360 million in 2019 and USD 980 million in 2024 (Table 6.2 and `agrifood_chapters.csv`). It was led by vegetable oils (HS 15, USD 0.2 million in 2013 to 216 million in 2024), food residues and fodder (HS 23, 1.7 to 280 million), cereals (HS 10, 34 to 261 million) and oilseeds (HS 12, 24 to 170 million). Both facts are true: the absolute expansion happened mostly in the BRI period, and the China-specific growth rate did not accelerate when the BRI began.

**Metals and ores.** The China/RoW ratio rose before 2010 (−0.99 in 2008 relative to 2013), was flat and slightly negative between 2013 and 2019, and turned positive only in 2023–2024, with wide confidence intervals. There is no trend change after 2013 (δ = −0.07, *p* = 0.26). The rise in China's orientation of metals came before the BRI (2008–2010) and after the BRI connectivity projects (2023–2024).

**Energy.** China's orientation of energy exports rose until 2011, fell sharply in 2014–2017 (−1.56 in 2017) and partly recovered. No inference is possible with one chapter, but the descriptive pattern is clear: in 2014–2017 oil exports to China fell proportionally more than oil exports to other markets. This is the opposite of what E2 predicts for the BRI period.

## 6.5 Robustness

The qualitative conclusions do not depend on the source used for the China leg: with China's mirror imports the coefficients are of the same sign and similar size (Table 6.4, row 2), and the copper and zinc suppression in Kazakhstan's 2020–2022 data does not enter because those years are excluded. Excluding gold and very small chapters changes nothing. Moving the start date to 2015 or 2017 reduces the agri-food coefficient (2.12 and 1.83) because more of the rising trend falls into the "pre" period, which is again consistent with a trend that began before the treatment date. Excluding 2023–2024 removes the metals result but not the agri-food result.

## 6.6 The Extensive Margin

**Table 6.7. Linear probability of exporting more than USD 1 million: change for China relative to RoW after 2013**

| Term | Estimate | SE | *p* | Pre-2014 share of China chapter-years active |
|---|---:|---:|---:|---:|
| China × Post (pooled) | 0.013 | 0.040 | 0.752 | 0.20 |
| China × Post × agri-food | 0.207 | 0.109 | 0.061 | 0.10 |
| China × Post × metals and ores | 0.024 | 0.038 | 0.532 | 0.84 |
| China × Post × other | −0.070 | 0.041 | 0.090 | 0.11 |

*Same fixed effects as Table 6.4. Energy is active in every year for both destinations, so its term is not identified. Source: Script 62, `extensive_margin_lpm.csv`.*

Pooled across products, the probability that a chapter is exported to China in a meaningful amount did not rise relative to the rest of the world. The rise in the number of chapters exported to China (§6.2) was matched by a similar rise for other markets. For agri-food, the probability rose by about 21 percentage points from a base of 10 per cent, which is marginally significant (*p* = 0.06). At the HS-2 level, the extensive-margin prediction of E1 is supported only weakly and only for agri-food. A proper test needs HS-6 or firm-level data (§8.2).

## 6.7 What Did the BRI Consist of in Kazakhstan? (SQ3)

**Table 6.8. Chinese official finance commitments to Kazakhstan by sector and period (USD bn, constant 2021)**

| Sector (AidData) | 2000–2008 | 2009–2013 | 2014–2017 | 2018–2021 | Total |
|---|---:|---:|---:|---:|---:|
| Industry, mining, construction | 15.88 | 19.57 | 6.38 | 2.81 | 44.64 |
| Energy | 2.75 | 7.21 | 0.36 | 0.13 | 10.46 |
| Transport and storage | 0.43 | 0.00 | 1.92 | 1.78 | 4.13 |
| Other sectors | 0.87 | 1.39 | 1.88 | 0.78 | 4.92 |
| **All sectors** | **19.93** | **28.17** | **10.54** | **5.50** | **64.15** |

*Source: AidData GCDF 3.0, 155 projects recommended for aggregates [@aiddata_gcdf3_2023]. Author's calculations (Script 61, `aiddata_by_sector_period.csv`). "Other sectors" combines the remaining AidData sectors; no agriculture, forestry or fishing project is recorded.*

![Figure 6.6. Chinese official finance commitments to Kazakhstan by year, 2000–2021](../Outputs/generated_figures/fig_r5_aiddata_by_year.png)

Recorded Chinese official finance to Kazakhstan was largest *before* the BRI: USD 48.1 billion (constant 2021 dollars) was committed in 2000–2013 and USD 16.0 billion in 2014–2021. The largest pre-2013 commitments financed the Kazakh sections of the Central Asia–China gas pipeline (2008 and 2012), the purchase of oil companies (Mangistaumunaigas, 2009; PetroKazakhstan, 2005) and the Bozshakol (2009) and Aktogay (2011) copper mines (AidData records 61056 and 41941). After 2013, finance shifted towards transport: China Eximbank loans for five road reconstruction projects in 2017–2018 and a 2019 loan for border checkpoint modernisation. The Khorgos dry port began operating in 2015, with Chinese state companies taking a 49 per cent stake in 2017 [@ktze_khorgos_2025]. On market access, Kazakhstan reported in 2023 that protocols covered 24 plant and livestock products and that agricultural exports to China had doubled [@astanatimes_agri_2023]; the dates of individual protocols could not be verified for this thesis.

Set against the results of §6.3–6.4, these channels line up as follows:

- **Finance and E2.** Chinese finance in hydrocarbons and mining was concentrated before 2013, and the China orientation of energy and metals rose in the same pre-BRI years (2005–2011). After 2013, finance in these sectors fell, energy's China orientation fell, and metals' was flat until 2019. Copper, the product most directly linked to Chinese-financed mines, saw only a modest rise in China's share between 2013 and 2024 (56 to 64 per cent). E2 fits the *pre-BRI* period better than the BRI period.
- **Transport and border infrastructure, market access and E1.** These are the post-2013 channels. The only group whose China orientation kept rising after 2013 is agri-food, the group most likely to benefit from phytosanitary access and faster border crossings, and recorded Chinese finance never went into agriculture. But the agri-food reorientation began before any of these channels existed and did not accelerate when they appeared.

## 6.8 Summary of Results

| Question | Finding | Strength of evidence |
|---|---|---|
| SQ1: What moved the balance? | 2013–2019: energy exports (−7.6 bn). 2019–2024: imports (+15.2 bn). Metals and ores exports rose (+5.6 bn, 2013–2024). | Accounting identity on China-reported data; robust by construction |
| SQ2: China-specific change? | Agri-food: large and robust (×11.7). Energy: down (−41%), no inference. Metals: up only with 2023–24. Other: none. | Strong for agri-food; weak for metals; descriptive for energy |
| SQ2: Timed with the BRI? | No. Agri-food began 2010–2012 and its proportional trend slowed after 2013; metals rose before 2010 and after 2022; energy orientation fell after 2013. | Event study, placebo and trend-break test agree |
| SQ2: Extensive margin? | No pooled change; weak rise for agri-food (*p* = 0.06). | HS-2 level only |
| SQ3: BRI channels | Finance peaked pre-2013 in oil, gas and mining; post-2013 shift to roads and borders; no agricultural finance. | Commitments, not disbursements |
| SQ4: Data | KZ 2020–2022 partner data omit copper, zinc, aluminium exports and machinery imports; persistent import gap. | Direct comparison of the two reporters |


# 7. Discussion

## 7.1 What the BRI Explains, and at Which Level

The results allow a precise statement of the BRI's role in this relationship.

**Level A (context) is clearly supported.** The BRI period is the period in which the balance turned negative, in which oil's share of the basket collapsed, in which agri-food exports to China reached almost USD 1 billion, and in which transport and border infrastructure was built with Chinese finance. Any account of Kazakhstan–China trade in 2014–2024 must place it in this context.

**Level B (association with BRI-era mechanisms) is supported for agri-food, with a strong qualification.** Agri-food is the one product group whose orientation towards China kept rising after 2013 net of world prices and destination-common shocks, and it is the group most exposed to the channels that the BRI actually delivered after 2013: phytosanitary market access, the Khorgos dry port and road and border upgrades. Recorded Chinese finance never went into agriculture, so the association is with access and logistics, not with finance. The qualification is that the reorientation began two to three years before the BRI and did not accelerate when the BRI began. The most that can be said is that BRI-era channels are *consistent with* the continuation of an existing trend, not that they started or sped it up.

**Level C (causal effect) is not supported.** The design removes the commodity cycle, but no test shows a China-specific break at 2013 in any product group. For energy, the China-specific change after 2013 is negative, the opposite of the resource-security expectation. For metals and ores, China's orientation rose before 2010, when Chinese finance into mining was at its peak, and after 2022, for reasons this thesis cannot identify. The thesis therefore does not claim that the BRI caused any change in Kazakhstan's exports to China.

This answer is less dramatic than the "impact" in the registered title suggests, but it is what the evidence supports. It also answers a question the earlier version of this thesis could not: the post-2013 change in Kazakhstan's exports to China is mostly the commodity cycle (common to all markets) plus pre-existing China-specific trends, not a new China-specific shift.

## 7.2 Strategic Minerals and the Trade Balance

The registered topic asks about the role of strategic mineral exports in the bilateral balance. The answer has three parts.

First, mineral exports did not cause the deterioration. Exports of metals and ores to China were roughly unchanged in 2013–2019 (+USD 0.06 billion) and rose by USD 5.6 billion in 2019–2024 (Table 6.1b). Arithmetically, the recorded 2019–2024 deterioration would have been USD 5.6 billion larger had these exports stayed at their 2019 level and nothing else changed; this is an accounting statement, not an estimate of what would have happened.

Second, minerals did not offset the deterioration either. The balance deteriorated because oil exports fell in 2014–2016 and imports from China doubled after 2019. These are movements on other lines of the account. A bilateral balance is not a good measure of the gains from trade [@ricardo_1817; @heckscher_1919], and a falling balance with one partner can coexist with rising exports and a healthy overall position; Kazakhstan's total merchandise exports in 2024 (USD 82.5 billion) were close to their 2013 level (USD 84.7 billion) [@wdi_2026].

Third, China's role as a buyer of Kazakh minerals increased in the most recent years. China took 80 per cent of Kazakhstan's ore exports and 64 per cent of its copper exports in 2024 (Table 7.1). This is the most important structural fact about strategic minerals in this relationship, and it is relatively recent: China's share of ores was 41 per cent as late as 2019.

## 7.3 Dependence Is Two-Sided, but Mostly Asymmetric

The asymmetric-interdependence literature [@keohane_nye_1977; @hirschman_1945] is often applied to Kazakhstan–China relations on the assumption that trade concentration creates Chinese leverage. The data allow a more careful statement. Table 7.1 compares, for 2024, China's share of Kazakhstan's exports of each chapter with Kazakhstan's share of China's imports of the same chapter.

**Table 7.1. Two-sided dependence by chapter, 2024**

| HS | Chapter | China's share of KZ exports, % | KZ's share of China's imports, % |
|---|---|---:|---:|
| 26 | Ores | 80.2 | 1.8 |
| 74 | Copper | 64.1 | 3.8 |
| 79 | Zinc | 50.3 | 28.1 |
| 28 | Inorganic chemicals incl. uranium compounds | 32.4 | 8.9 |
| 72 | Iron and steel incl. ferroalloys | 25.0 | 5.6 |
| 27 | Energy | 7.1 | 0.6 |
| 23 | Food residues, fodder | 67.3 | 4.2 |
| 15 | Fats and oils | 39.6 | 1.3 |
| 12 | Oilseeds | 41.0 | 0.2 |
| 10 | Cereals | 17.7 | 2.0 |

*Source: UN Comtrade; Kazakhstan-reported exports and China-reported imports [@un_comtrade_hs2_2026]. Author's calculations (Script 64, `two_sided_dependence_2024.csv`).*

For ores, copper and most agri-food chapters, the dependence is strongly asymmetric: China matters far more to Kazakhstan as a buyer than Kazakhstan matters to China as a supplier. Zinc is closer to mutual dependence. Uranium is the clearest exception, and the HS-2 data understate it because HS 28 mixes uranium with other chemicals: Chinese customs data show that Kazakhstan supplied about two-thirds of China's natural uranium imports in 2023 [@pan_2024], and Kazakhstan produced 39 per cent of the world's mined uranium in 2024 [@wna_2026]. Pan [-@pan_2024] reports that Chinese companies had to accept minority positions to secure access to Kazakh uranium, which is the reverse of the leverage usually assumed.

Dependence is not the same as vulnerability. Vulnerability depends on how costly it is to redirect trade. Ores and copper are traded on world markets, and redirection is possible: China's share of Kazakhstan's refined copper exports fell from 65.4 to 49.1 per cent between January–November 2024 and the same period of 2025, while Türkiye's rose to 40.9 per cent [@astanatimes_copper_2026]. Table 7.1 therefore shows where Kazakhstan's sensitivity to Chinese demand is highest, but it does not show that China has used, or could cheaply use, that position. This thesis does not assume either.

## 7.4 Alternative Explanations

- **China's own demand.** China-specific demand growth (for instance for vegetable oils and feed) would produce the same agri-food coefficient as BRI connectivity. The design cannot separate them (§5.6), which is the main reason the agri-food finding stays at level B.
- **Russia and the post-2022 period.** The rise in metals' China orientation and the import surge both occur in 2023–2024, after sanctions on Russia changed trade routes in the region. Kazakhstan's exports of machinery, electrical equipment and vehicles to Russia rose almost sevenfold between 2019 and 2023 (§6.1). These are post-2022 phenomena; attributing them to the BRI would be a mistake.
- **Pre-BRI Chinese investment.** Chinese finance for gas pipelines, for the acquisition of Kazakh oil companies and for copper mines was committed before 2013 (§6.7), and it coincides with the rise of China's share of energy and metals in 2005–2011. The coincidence in timing is consistent with, but does not prove, a link.
- **Statistics.** The 2020–2022 suppression and the persistent import gap could create spurious changes. The main results exclude 2020–2022 and are reproduced with China's mirror data.

## 7.5 Policy Implications

1. **Monitor BRI outcomes by product and against other markets, not by bilateral turnover or balance.** The bilateral balance moved for reasons (oil prices, post-2022 import flows) unrelated to the composition of Kazakhstan's exports.
2. **Agri-food is the one area of China-specific diversification.** It was associated with market access and logistics, not with Chinese finance. Keeping phytosanitary protocols and border processing efficient is more relevant to this channel than attracting Chinese loans.
3. **Mineral export concentration on China has risen recently and deserves monitoring,** but the 2025 copper data show that redirection is feasible. Diversifying buyers for ores and copper is a commercial risk-management question, not evidence of Chinese leverage.
4. **Fix the statistics.** Kazakhstan's partner-level data for 2020–2022 omit major chapters. The Bureau of National Statistics could publish partner totals that include confidential chapters, as China does, and reconcile its import data with China's.


# 8. Conclusion

## 8.1 Answer to the Research Question

The research question asked whether the composition of Kazakhstan's exports to China changed after 2013 in a way that is specific to China and timed with the BRI, and what this implies for the bilateral balance.

The composition did change, and part of the change was specific to China. Net of world prices and everything common to Kazakhstan's markets, agri-food exports reoriented strongly towards China, energy exports turned away from China after 2013, and metals and ores became more China-oriented only in 2023–2024. None of these China-specific changes began with the BRI. The agri-food reorientation started in 2010–2012 and slowed in proportional terms after 2013; the metals reorientation came before 2010 and after 2022. Recorded Chinese official finance peaked before 2013 and went into oil, gas and mining. The BRI is therefore well supported as context and as an association for agri-food, but there is no evidence of a BRI-caused break in Kazakhstan's export composition.

For the bilateral balance, the implication is that the deterioration from +USD 3.5 billion (2013) to −USD 12.0 billion (2024) was not caused by changes in Kazakhstan's mineral exports, which rose. It was caused first by the fall of oil exports (2013–2019) and then by the doubling of imports from China (2019–2024). Strategic mineral exports partly offset the second phase.

## 8.2 Limitations

1. **HS-2 aggregation.** Chapters mix products (uranium with other chemicals; wheat with barley). The extensive margin in particular needs HS-6 or firm data. All conclusions about the extensive margin are provisional.
2. **No causal identification.** The design cannot separate BRI channels from China's own demand. No comparison country was used.
3. **Energy is one chapter,** so no statistical inference is available for it.
4. **Missing and excluded years.** Kazakhstan's 2020–2022 product data are unusable for partner comparisons, Kazakhstan-to-World 2020 and 2022 could not be retrieved, and China-reported 2006 data were not retrieved. China's exports to Kazakhstan were collected only for 2013, 2019 and 2024.
5. **AidData** records official commitments, not disbursements or private investment.
6. **Import side.** The import surge is described but not explained; the share of re-exports to Russia cannot be measured with Comtrade data.
7. **Researcher degrees of freedom.** The expectations were formulated after exposure to aggregate data (§3.3). The decision rules were fixed before the product-level tests, but readers should weigh this.

## 8.3 Future Research

The most useful extensions are: HS-6 data to test the extensive margin and product-level timing against the dates of individual phytosanitary protocols; a comparison with other Central Asian exporters to China, which would provide a counterfactual for China-specific demand; and Kazakh customs microdata to measure re-exports and to resolve the import gap.


# References

::: {#refs}
:::


# Appendix A: Data and Code

**Reproduction.** From the repository root: `python Scripts/60_build_hs2_panel.py`, then Scripts 61, 62, 63 and 64, then `python Scripts/50_build_paper.py`. Python packages: pandas, numpy, statsmodels, pyfixest (0.60), matplotlib, openpyxl, scipy.

**Table A.1. Scripts and outputs**

| Script | Purpose | Main outputs |
|---|---|---|
| 60_build_hs2_panel.py | Parse raw HS-2 files, merge gap-fills, validate totals | `hs2_panel_long.csv`, `hs2_validation.csv` |
| 61_composition_diversification.py | Composition, China shares, HHI, suppression check, balance decomposition, imports, AidData, Russia check, agri chapters | Tables 4.3, 6.1–6.3, 6.8 |
| 62_ppml_triple_difference.py | PPML triple difference, robustness, event study, pre-trend test, trend break, extensive margin | Tables 6.4–6.7 |
| 63_figures_reconstruction.py | Figures 6.1–6.6 | `fig_r1`–`fig_r6` |
| 64_two_sided_dependence.py | Two-sided dependence, 2024 | Table 7.1 |

**Units and transformations.** All trade values in current US dollars; PPML is estimated on values in USD million. Rest of world = Kazakhstan's exports to World minus exports to China (negative differences, which do not occur in the main sample, would be set to zero). Zero flows are kept. HS chapters are as reported by Comtrade in each year.

**Data handling decisions.**

1. Chapters missing from a truncated API response were re-queried and merged (gap-fill file); a chapter appearing twice keeps its first value.
2. Kazakhstan-to-World 2022 was rejected after inspection (duplicated values); 2020 could not be retrieved.
3. 2020–2022 are excluded from Kazakhstan-reported product comparisons because of suppression (§4.4).
4. Balances use China-reported data in both directions (§4.5).


# Appendix B: Relation to the Earlier Specification

The earlier version of this thesis (archived as `Paper/archive/v2_minerals_trade_balance_dissertation.md`) regressed the annual bilateral balance (2000–2023, *n* = 24) and observed monthly balances (2010–2019, *n* = 120) on mineral exports, a post-2013 dummy and their interaction, with controls for oil prices and the exchange rate. Its main results were a positive pre-2013 association between mineral exports and the balance and a negative post-2013 interaction (annual β = −2.49; monthly β = −0.91, *p* = 0.008).

That specification was replaced for four reasons, each verified during the reconstruction:

1. **Identification.** A post-2013 dummy in a single country-pair time series cannot separate the BRI from the 2014–2016 commodity price collapse. The triple-difference design in Chapter 5 removes common shocks by comparing destinations.
2. **The omitted oil channel.** The monthly interaction disappeared once bilateral oil exports were controlled for, and Granger tests found that mineral exports do not lead the balance. Section 6.1 shows why: the 2013–2019 balance change is accounted for by oil.
3. **Data problems.** An "oil exports" column in the annual panel was a placeholder (55 per cent of total exports) and was removed; the 2020–2022 import data were shown to be incomplete (Table B.2).
4. **Inference.** A cross-partner difference-in-differences with six partners originally reported *p* = 0.0002 using standard errors unsuitable for a panel; corrected inference gave *p* between 0.02 and 0.38.

**Table B.2. Kazakhstan-reported imports from China vs China-reported exports to Kazakhstan (USD bn)**

| Year | Kazakhstan-reported imports | China-reported exports | Ratio | Months with HS 84/85/87 import records |
|---|---:|---:|---:|---:|
| 2013 | 8.36 | 12.55 | 1.50 | 12 |
| 2016 | 3.67 | 8.29 | 2.26 | 12 |
| 2019 | 6.57 | 12.73 | 1.94 | 12 |
| 2020 | 1.96 | 11.70 | 5.99 | 0 |
| 2021 | 2.42 | 13.76 | 5.67 | 0 |
| 2022 | 3.58 | 16.36 | 4.57 | 0 |
| 2023 | 16.77 | 24.70 | 1.47 | 12 |

*Source: UN Comtrade monthly and annual data, both reporters [@un_comtrade_2026]. Author's calculations (Script 43, `import_break_evidence.csv`).*

The scripts of the earlier analysis (Scripts 10–45) remain in the repository and run unchanged; their outputs are no longer cited in the main text.
