---
title: "The Belt and Road Initiative and the Kazakhstan–China Trade Balance: Sources of the Post-2013 Swing and the Role of Strategic Mineral Exports, 2005–2024"
subtitle: "Master's thesis. Registered topic: BRI's Impact on Kazakhstan–China Trade Balance: The Role of Strategic Mineral Exports"
author: "Nikar Omirbek"
bibliography: ../Literature_Review/bibliography.bib
---

# Abstract

Between 2013, when the Belt and Road Initiative (BRI) was announced in Astana, and 2024, Kazakhstan's merchandise trade balance with China moved from a surplus of USD 3.5 billion to a deficit of USD 12.0 billion (China-reported data). The BRI is often credited, or blamed, for this swing. A bilateral deficit is not in itself evidence of an economic problem: imports can embody investment, integration and specialisation, and transit services, a main BRI channel for Kazakhstan, do not appear in merchandise trade at all. The thesis therefore treats the balance as an accounting summary of how the relationship changed, not as a welfare measure, and asks: **is the post-2013 swing distinctive to Kazakhstan's trade with China, and are its distinctive components consistent with the mechanisms through which the BRI was expected to act, in particular through strategic mineral exports?**

The thesis builds an HS-2 panel of Kazakhstan's exports to China and to the rest of the world for 2005–2024 from UN Comtrade, validated against China's mirror records and World Bank totals, and adds aggregate import data, China's trade with Russia and the Central Asian states, and AidData records of Chinese official finance. It uses three kinds of evidence that are kept distinct: accounting decompositions (identities), comparison-adjusted components (relative to Kazakhstan's other partners, and relative to China's other regional partners), and statistical tests on product-level data (PPML triple differences, event studies and trend breaks with Holm corrections and randomisation inference). No causal effect of the BRI is estimated.

Relative to Kazakhstan's other partners, most of the swing is specific to China: 52–92 per cent depending on base and end years, 71 per cent with averaged endpoints (2011–2013 to 2023–2024). Its largest part is a rise in imports from China after 2019. Relative to China's other regional partners, that import rise is not distinctive: under every neighbour comparator, weighting and base year, Kazakhstan's imports from China grew no faster than those of its neighbours, or at most by USD 0.7 billion (under 3 per cent of 2024 imports), with or without Russia. On the export side, China-specific changes are a fall in oil exports concentrated in 2014, which runs opposite to the BRI's resource-security mechanism, and gains in strategic minerals and agri-food. Strategic minerals offset part of the swing under every base and end year. The agri-food reorientation towards China, the one change consistent with a BRI mechanism in products and channel, is robust to multiple-testing correction and randomisation inference, but began before 2013, and its China-specific trend did not accelerate after 2013. Chinese official finance peaked before 2013.

The thesis concludes that the swing is real and China-specific from Kazakhstan's side, regional from China's side, and that none of its large components shows the timing or direction that BRI mechanisms predict. This is evidence against the specific mechanisms tested, not evidence that the BRI had no effect on Kazakhstan. The thesis also documents that Kazakhstan's 2020–2022 partner statistics omit major metal exports and machinery imports.

**Keywords:** Belt and Road Initiative; Kazakhstan–China trade balance; strategic minerals; comparison-adjusted decomposition; PPML; mirror statistics; Central Asia


# 1. Introduction

## 1.1 The Phenomenon

China is one of Kazakhstan's two most important trading partners. In 2023 it supplied 27.4 per cent of Kazakhstan's imports and took 18.7 per cent of its exports [@bns_2024_foreign_trade]. Kazakhstan is also where the BRI began: Xi Jinping proposed the Silk Road Economic Belt at Nazarbayev University in Astana on 7 September 2013 [@xinhua_chinadaily_2013]. Since then a dry port at Khorgos on the border has started operating (2015), with Chinese state companies taking a 49 per cent stake in 2017 [@ktze_khorgos_2025]; Chinese policy banks have financed road reconstruction across the country [@aiddata_gcdf3_2023]; and the two governments have signed protocols that open the Chinese market to Kazakh agricultural products [@astanatimes_agri_2023].

Over the same period Kazakhstan's merchandise trade balance with China swung by USD 15.5 billion: by China's reported data, from a surplus of USD 3.5 billion in 2013 to a deficit of USD 3.9 billion in 2019 and USD 12.0 billion in 2024 (Table 6.1). The composition of trade also changed: oil fell from 62 to 22 per cent of Kazakhstan's exports to China, metals and ores rose from 36 to 67 per cent, and imports from China more than doubled after 2019.

## 1.2 The Puzzle

The swing coincides with the BRI, and the BRI is the obvious bilateral explanation. But two other explanations predict the same before-and-after pattern. The swing may be the bilateral reflection of shocks that hit all of Kazakhstan's trade, such as the 2014–2016 collapse of oil and metal prices. Or it may be the Kazakh reflection of changes in China's trade with the whole region, such as the reorganisation of trade with Russia after 2022. Before-and-after comparisons cannot tell these apart. The puzzle is therefore: **a bilateral outcome changed sharply in the BRI era, but it is not known whether the change is distinctive to the Kazakhstan–China relationship at all, and if it is, whether it took the form the BRI's mechanisms imply.**

## 1.3 Why the Trade Balance, and What It Does Not Measure

The registered topic names the bilateral trade balance as the outcome. It is worth being explicit about why this is a meaningful object and what it cannot show.

*What it does not measure.* A bilateral balance is not a measure of gains from trade [@ricardo_1817; @heckscher_1919]. A deficit with one partner can coexist with an overall surplus, and Kazakhstan's total merchandise exports in 2024 (USD 82.5 billion) were close to their 2013 level (USD 84.7 billion) [@wdi_2026]. Rising imports from China can embody productive investment: machinery, electrical equipment and vehicles account for 47 per cent of the 2019–2024 import increase (Table 6.11). They can also reflect lower prices for consumers, deeper integration or transit to third countries. And the BRI's best-documented channel for Kazakhstan, rail transit between China and Europe [@mau_seuren_2023], generates service revenue that does not appear in merchandise trade at all. The thesis therefore does not treat the swing as a loss or the deficit as a problem.

*Why it is still the right object.* First, it is the accounting identity that ties together everything that changed on both sides of the relationship: a swing of USD 15.5 billion must be the sum of changes in specific exports and imports, so explaining it forces an account of the whole relationship rather than of one product. Second, the bilateral balance with China is the indicator most often cited in Kazakhstan's public debate about the BRI, so establishing what moved it, and whether that has anything to do with the BRI, has direct policy relevance. Third, the registered topic asks specifically about strategic mineral exports, and the balance is where their contribution can be measured against the other components.

## 1.4 Research Question

> **Central research question.** *Is the post-2013 swing in Kazakhstan's trade balance with China distinctive to the Kazakhstan–China relationship, and are its distinctive components consistent with the mechanisms through which the BRI was expected to operate, in particular through strategic mineral exports?*

"Distinctive" is assessed against two comparisons, which answer different questions and are not combined into a single number:

- **Relative to Kazakhstan's other partners.** Did trade with China change differently from Kazakhstan's trade with the rest of the world? This removes shocks common to Kazakhstan's trade, including the commodity cycle.
- **Relative to China's other regional partners.** Did China's trade with Kazakhstan change differently from China's trade with Russia and the other Central Asian states? This removes shocks common to China's trade with the region, including the post-2022 reorganisation of regional trade. Because those partners are also BRI participants, it also removes any region-wide BRI effect, so timing is used to judge whether a regional change could be a BRI effect.

Four sub-questions organise the analysis:

- **SQ1.** Which flows and product groups account for the swing, and how much of it is China-specific relative to Kazakhstan's other partners? (§6.1–6.2)
- **SQ2.** Which export groups, including strategic minerals, changed specifically towards or away from China, and did those changes begin or accelerate with the BRI? (§6.3–6.5)
- **SQ3.** Is the rise in imports from China distinctive relative to China's other regional partners, and when did it occur? (§6.6)
- **SQ4.** Do the timing and sectors of measurable BRI channels (Chinese finance, transport and border infrastructure, market access) match the components found under SQ1–SQ3? (§6.8)

The reliability of the bilateral statistics is a precondition, examined first (Chapter 4), because comparison-adjusted components are exactly what reporting discrepancies distort.

## 1.5 Why the BRI Is Central, and What Kind of Claim Is Made

The BRI is central for three reasons. First, it is the hypothesis the question is built around: the reason to ask whether the swing is distinctive to the relationship is that the BRI is a bilateral and regional framework. Second, the BRI literature specifies mechanisms with testable implications for which products change and when (Chapters 2–3). Third, the conclusion is a statement about the BRI: which mechanisms the evidence is consistent with, which it contradicts, and where it is silent.

Three kinds of evidence are kept distinct:

1. **Accounting decompositions** (Table 6.2): identities that show which flows moved. They involve no comparison and no causal claim.
2. **Comparison-adjusted components** (Tables 6.3–6.4, 6.10b): how much a flow changed relative to a benchmark. They describe distinctiveness, not causes. In particular, the China-specific component is *not* an upper bound on any BRI effect: the BRI could also change Kazakhstan's trade with other partners (for example through transit corridors or Chinese-financed capacity sold elsewhere), and BRI effects inside the China-specific component could be offset by other China-specific changes.
3. **Statistical tests** on product-level data (Tables 6.7–6.9, 6.12): whether China-specific export changes are distinguishable from noise and whether they changed at the time BRI mechanisms predict.

Claims are graded at three levels: **A** (context: the BRI is the policy framework of the period), **B** (a distinctive change whose products and timing match a BRI mechanism) and **C** (a causal effect). The design can reach A and B, never C. Where the evidence is silent, the thesis says so: a test that cannot detect a change is *absence of evidence*; a change in the opposite direction or at the wrong time is *evidence inconsistent with a mechanism*; neither is *evidence that the BRI had no effect*.

## 1.6 Aim, Objectives and Contribution

**Aim.** To determine what accounts for the post-2013 swing in Kazakhstan's balance with China, how far it is distinctive to the relationship, and whether its distinctive components are consistent with BRI mechanisms, including through strategic mineral exports.

**Objectives.**

1. To derive the BRI's expected mechanisms and their observable implications from the literature, including studies that find positive BRI trade effects (Chapters 2–3).
2. To build and validate a dataset in which distinctive components can be measured, reconciling Kazakh and Chinese statistics (Chapter 4).
3. To decompose the swing by flow and product group and adjust it against Kazakhstan's other partners (§6.1–6.2).
4. To test which export groups changed specifically towards China, and when (§6.3–6.5).
5. To compare the rise in imports with China's trade with Kazakhstan's neighbours (§6.6).
6. To compare BRI channels with these components and state what the evidence does and does not show (§6.8, Chapters 7–8).

**Object and subject.** The *object* is Kazakhstan–China bilateral trade. The *subject* is the composition and distinctiveness of the post-2013 swing in the bilateral balance and its relationship to BRI mechanisms and strategic mineral exports.

**Contribution.** The thesis replaces a before-and-after narrative with a two-sided comparison and a mechanism-by-mechanism test. It shows that the swing is China-specific from Kazakhstan's side but regional from China's side, and that its large components do not have the timing or direction BRI mechanisms predict, while strategic minerals offset part of it. Supporting contributions are a test of the timing of the agri-food reorientation and the documentation of a reporting break in Kazakhstan's 2020–2022 partner statistics.

**Provisions submitted for defence.**

1. Relative to Kazakhstan's other partners, most of the 2013–2024 swing is China-specific (52–92 per cent depending on base and end years; 71 per cent with averaged endpoints), and its largest part is a rise in imports from China after 2019.
2. Relative to China's other regional partners, that rise in imports is not distinctive: under every neighbour comparator, weighting and base year, Kazakhstan's imports from China to 2023–2024 grew no faster than its neighbours', or at most by USD 0.7 billion (under 3 per cent of 2024 imports), with or without Russia.
3. On the export side, the China-specific fall in oil exports (concentrated in 2014) runs opposite to the BRI's resource-security mechanism, strategic mineral exports offset part of the swing under every specification, and the agri-food reorientation, the one change consistent with a BRI mechanism, began before 2013 and did not accelerate after it.
4. Kazakhstan's 2020–2022 partner statistics omit major metal exports and machinery imports; China's mirror data are needed to measure the relationship.

## 1.7 Structure

Chapter 2 reviews the literature, including evidence of positive BRI trade effects. Chapter 3 states what each mechanism predicts and what would count as support or contradiction. Chapter 4 builds and validates the data. Chapter 5 sets out the decompositions, comparisons, tests and safeguards. Chapter 6 answers the sub-questions and ends with a synthesis table (Table 6.14). Chapter 7 interprets the results. Chapter 8 concludes.


# 2. Literature Review

## 2.1 Resource-Based Trade and the Comparative-Advantage Null

Standard trade theory predicts that a resource-abundant economy such as Kazakhstan exports resource-intensive goods and imports manufactures from a labour- and capital-abundant economy such as China [@ricardo_1817; @heckscher_1919; @ohlin_1933]. In that framework neither the bilateral balance nor the share of a particular partner has welfare significance in itself. What matters for this thesis is the empirical implication: if Kazakhstan's comparative advantage and world prices determine what it exports, the composition of its exports should change in the same way for every destination. Any change in the composition of exports to China would then reflect world prices and Kazakhstan's own supply, not anything specific to China. This is the null hypothesis against which BRI-related claims must be tested.

The commodity-dependence literature explains why that null is demanding. Commodity prices are volatile and have long cycles [@harvey_etal_2010], resource booms affect the real exchange rate and non-resource sectors [@corden_neary_1982], and the developmental consequences of resource wealth depend on institutions and policy [@sachs_warner_1995; @vanderploeg_2011; @frankel_2010]. Export growth driven by resource volume can even reduce welfare when it worsens the terms of trade [@bhagwati_1958]. For Kazakhstan, the 2014–2016 oil price collapse alone could produce large changes in export composition, the bilateral balance and the exchange rate without any change in trade costs with China.

## 2.2 Trade Costs, Gravity and the BRI

Gravity models explain bilateral trade by economic size and bilateral trade costs relative to the trade costs each country faces with all partners [@anderson_vanwincoop_2003]. Poisson pseudo-maximum-likelihood (PPML) estimation of such models is now standard because it handles zero flows and heteroskedasticity [@santos_silva_tenreyro_2006]. The BRI literature applies this framework. De Soyres et al. [-@desoyres_etal_2019; -@desoyres_etal_2020] estimate that BRI transport projects reduce shipping times and trade costs, with gains concentrated along corridors. Baniya, Rocha and Ruta [-@baniya_rocha_ruta_2020] find that BRI-related improvements raise trade flows, more so when infrastructure is complemented by trade-policy reforms. Bird, Lebrand and Venables [-@bird_lebrand_venables_2020] model Central Asia specifically and show that gains from improved connectivity are uneven across locations and sectors.

Two limits of this literature matter here. First, most estimates are simulations or cross-country averages; they do not test what happened in one country pair. Second, they predict *more trade*, not a particular balance or composition. The trade-cost channel has a compositional implication only through the next strand of theory: lower trade costs matter most for products that were previously not traded or were traded little.

## 2.3 Evidence of Positive BRI Trade Effects, and How It Relates to This Thesis

A substantial peer-reviewed literature finds that the BRI raises trade. It is worth stating precisely what it estimates.

- **Ex-ante, model-based estimates.** De Soyres et al. [-@desoyres_etal_2020] estimate that the planned BRI transport projects reduce shipment times by 1.7–3.2 per cent and trade costs by 1.5–2.8 per cent in BRI economies, and by up to 11.9 and 10.2 per cent along some corridors. Baniya, Rocha and Ruta [-@baniya_rocha_ruta_2020] feed such trade-time reductions into gravity and comparative-advantage models and find that the BRI increases trade flows among participants by up to 4.1 per cent, about three times more if accompanied by trade reforms, with larger gains for time-sensitive products. Bird, Lebrand and Venables [-@bird_lebrand_venables_2020] simulate Central Asian economic geography and find gains that are uneven across places and sectors.
- **Ex-post estimates.** Foo, Lean and Salim [-@foo_lean_salim_2020] estimate an augmented gravity model for ASEAN countries and China over 2000–2016 and find a positive and significant BRI dummy. Mau and Seuren [-@mau_seuren_2023] exploit the timing of China–Europe rail connections over 1996–2018 and find that they raised European exporters' revenues in China, including for countries connected indirectly.

These studies and this thesis answer different questions, and their results are compatible. First, they measure trade *volumes* (often total bilateral trade) or trade *costs*; this thesis measures the *composition and balance* of one pair's trade. A BRI that raises both exports and imports can leave the balance better, worse or unchanged. Second, the ex-ante studies predict effects of a few per cent on average; such effects would be hard to detect in one country pair's annual data against swings of the size seen here, so a failure to detect them is absence of evidence. Third, the rail evidence concerns China–Europe *transit*, in which Kazakhstan's role is that of a corridor. Transit earns Kazakhstan service revenue, which is not recorded in merchandise trade. This thesis therefore cannot speak to the BRI's transit benefits for Kazakhstan, and its conclusions are limited to Kazakhstan's own merchandise trade with China. Fourth, the mechanisms these studies identify (lower trade costs, larger gains for time-sensitive goods) have specific implications for the timing and product composition of Kazakhstan's own trade with China, and those implications are tested here (Chapter 3).


## 2.4 The Margins of Export Growth and Diversification

Models with heterogeneous firms imply that lower trade costs allow new, less productive firms and new products to enter a market [@melitz_2003], so that bilateral trade responds to trade costs mainly through the *extensive margin* of new products and firms [@chaney_2008]. Across countries, larger exporters export more varieties [@hummels_klenow_2005]. Diversification also follows a development pattern: production and exports diversify as income rises and re-concentrate only at high income levels [@imbs_wacziarg_2003; @cadot_carrere_strausskahn_2011]. These studies give the BRI trade-cost argument a specific, testable form: if BRI connectivity lowered the cost of reaching China, the gains should be largest for products that Kazakhstan exported little to China before, especially perishable or time-sensitive goods such as food, and the number of products exported to China should rise relative to other markets.

## 2.5 Chinese Finance and Resource Projects

A separate strand concerns Chinese official finance. China has become the largest official creditor to developing countries [@horn_reinhart_trebesch_2021], and BRI lending raised debt-sustainability concerns in several corridor economies [@hurley_morris_portelance_2018], although claims of systematic "debt-trap diplomacy" are not supported by the evidence [@brautigam_2020]. AidData's Global Chinese Development Finance Dataset records Chinese official commitments project by project for 2000–2021 [@aiddata_gcdf3_2023; @custer_etal_2023]. For Kazakhstan, the relevant question is whether Chinese finance went into export capacity, for instance mines and processing, and whether that capacity was then oriented towards China. Jepson and Baldakova [-@jepson_2024] study whether Chinese state capital supported resource-based structural transformation in Bolivia and Kazakhstan, and Calabrese [-@calabrese_2024] asks the same question for diversification in the Kyrgyz Republic. Global value chain research adds that suppliers in captive relationships often have limited scope for upgrading [@gereffi_humphrey_sturgeon_2005].

## 2.6 Kazakhstan, Central Asia and China

Area studies emphasise that the BRI in Central Asia is a broad label applied to projects, agreements and diplomatic initiatives of very different kinds [@laruelle_2018; @cooley_2012]. Pomfret [-@pomfret_2019] documents how Central Asian trade has been shaped by transport costs, trade policy and the Eurasian Economic Union, not only by China. Laruelle and Peyrouse [-@laruelle_peyrouse_2012] and Grant [-@grant_2020] show that the Chinese presence is received ambivalently in Kazakhstan, and Primiano and Kudebayeva [-@primiano_kudebayeva_2025] find uneven views of the BRI among Kazakh students. Rolland [-@rolland_2017] and Swaine [-@swaine_2015] describe the strategic purposes China attaches to the initiative. This literature is a warning against treating "the BRI" as a single treatment with a single start date.

## 2.7 Asymmetric Interdependence

Keohane and Nye [-@keohane_nye_1977] distinguish *sensitivity*, how quickly changes in one economy affect another, from *vulnerability*, the cost of adjusting when a relationship is disrupted. Hirschman [-@hirschman_1945] showed that trade can become a source of influence for the larger partner when the smaller partner's trade is concentrated on it and hard to redirect. This framework is frequently invoked for Kazakhstan–China relations. It does not, however, predict that trade concentration is harmful, or that it will be used as leverage; it predicts that the costs of disruption are distributed according to who can substitute more easily. Whether that is the case is an empirical question about both sides of the relationship, which most applications do not measure.

## 2.8 Research Gap

The literature supplies BRI mechanisms (trade costs and market access; resource finance), a null (comparative advantage and common shocks), and evidence that the BRI raises trade volumes on average. Among the studies reviewed here, none asks whether the swing in Kazakhstan's balance with China is distinctive to the relationship, either relative to Kazakhstan's other partners or relative to China's other regional partners, or tests whether its distinctive components have the timing and composition BRI mechanisms imply. None checks the bilateral statistics on which such conclusions depend. This thesis addresses these gaps for one country pair; it does not estimate the BRI's effect in general, and it does not address transit services.


# 3. Theoretical Framework and Expectations

## 3.1 Framework

Following the structural gravity view of bilateral trade [@anderson_vanwincoop_2003], Kazakhstan's trade with China in product *p* and year *t* depends on:

1. **Factors common to Kazakhstan's trade with all partners:** world prices, Kazakhstan's output and income, its exchange rate and trade policy.
2. **Factors common to China's trade with the region:** China's export supply and import demand, regional routing, and regional shocks such as the post-2022 reorganisation of trade with Russia.
3. **Persistent features of the Kazakhstan–China relationship:** distance, pipelines and rail links that existed before 2013, long-standing contracts.
4. **Changes specific to the Kazakhstan–China relationship over time:** BRI-era infrastructure at the Kazakhstan–China border, bilateral market-access agreements, Chinese finance in Kazakhstan, and other bilateral changes.

The BRI can operate through (2), (3) and (4): it is both a bilateral and a regional initiative. The comparison against Kazakhstan's other partners removes (1); the comparison against China's other regional partners removes (2), including any region-wide BRI effect. Neither comparison isolates the BRI, which is why mechanism predictions about products and timing are needed.

## 3.2 Mechanisms and What Would Count as Evidence

**M1. Connectivity and market access** [@desoyres_etal_2020; @baniya_rocha_ruta_2020; @bird_lebrand_venables_2020; @chaney_2008]. Lower trade costs and phytosanitary access raise trade most where it was previously small and for time-sensitive goods.

**M2. Resource finance and security** [@horn_reinhart_trebesch_2021; @jepson_2024]. Chinese finance for hydrocarbon and mining projects raises Kazakhstan's China-oriented exports of energy and strategic minerals.

**N0. Common shocks and comparative advantage** [@heckscher_1919; @ohlin_1933; @harvey_etal_2010]. Kazakhstan–China trade moves with Kazakhstan's trade with others and with China's trade with the region.

**Table 3.1. Observable implications**

| Mechanism | Prediction | Observation that would support it | Observation inconsistent with it | Observation that would be uninformative |
|---|---|---|---|---|
| M1, exports | China-specific rise in agri-food and other non-traditional exports from 2014–2015 | Positive China × Post coefficient and a positive trend break after 2013 | Rise that began earlier and did not accelerate; or no rise | Change smaller than the test can detect (§6.7) |
| M1, extensive margin | More chapters exported to China relative to other markets | Positive China × Post effect on export participation | Zero or negative effect with a precise estimate | Imprecise estimate |
| M1, imports | Kazakhstan-specific rise in imports from China from 2015 | Faster growth than China's exports to comparable neighbours, starting in 2014–2019 | No faster growth than neighbours, or rise only after 2022 | Neighbour benchmark that is itself affected by the BRI (see §3.1) |
| M2, energy | China-specific rise in energy exports | Positive China × Post for energy | China-specific fall | One chapter: no inference possible, only direction |
| M2, strategic minerals | China-specific rise after Chinese-financed projects | Positive China-specific component timed after project finance | Rise concentrated long after finance, or no rise | Rise whose timing depends on the base year |
| N0 | No China-specific component | Comparison-adjusted components near zero | Large components in either comparison | |

A component is classed as **consistent with a BRI mechanism (level B)** only if it is distinctive, has the predicted sign and product composition, and begins or accelerates after 2013. **Inconsistent** means the evidence contradicts a specific mechanism. It does not mean the BRI had no effect: the BRI may have acted through channels not visible in merchandise trade (transit services), through effects too small to detect, or through mechanisms not specified here.

## 3.3 How the Expectations Were Formed (Disclosure)

The general structure (a common-shocks null against connectivity and resource-finance mechanisms) was planned before the product-level data were collected. The product-group predictions were written after the author had inspected aggregate Kazakhstan–China data (in the earlier version of this thesis) and the descriptive shares by product group in the new panel (Table 6.6). The PPML tests were run after that inspection. The trend-break test, the comparison-adjusted decomposition, the comparison with China's regional partners, the robustness grid over base and end years, and the independent re-estimation were added in later rounds of analysis, after earlier results had been reviewed. These elements are therefore exploratory or confirmatory-after-exposure, not pre-registered. §5.7 describes the safeguards used.

## 3.4 Where Asymmetric Interdependence Fits

Asymmetric interdependence [@keohane_nye_1977; @hirschman_1945] is used in Chapter 7 to interpret the results, not as a hypothesis tested by them. The decompositions measure how trade changed; they do not measure bargaining power. Chapter 7 uses two-sided indicators of dependence without assuming that concentration of trade with China implies Chinese leverage.


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
| Kazakhstan's total imports from World and from China | Kazakhstan → World, China | Imports | CIF | Total | 2011–2014, 2019, 2023, 2024 | `comtrade_totals_imports_and_china_exports.txt` |
| China's total exports to and imports from Kazakhstan, Russia, Kyrgyzstan, Uzbekistan, Tajikistan, Turkmenistan, World | China → partners | Exports (FOB) and imports (CIF) | | Total | 2011–2014, 2019, 2023, 2024 | `comtrade_china_totals_by_partner.txt` |
| China's imports from World, selected chapters | China → World | Imports | CIF | HS-2 | 2024 | `comtrade_hs2_chn_imports_from_world_2024_selected.txt` |
| Chinese official finance commitments | AidData GCDF 3.0 | Commitments | Constant 2021 USD | Project | 2000–2021 | `aiddata_gcdf_v3.xlsx` [@aiddata_gcdf3_2023] |

*Values are in current US dollars unless stated. HS chapters are those reported (HS 2002 to HS 2022 vintages); chapter boundaries are stable across these vintages at the two-digit level.*

Data were retrieved year by year because the public API returns one period per call. Where the retrieval tool truncated a long response, the missing chapters were identified by comparison with neighbouring years and re-queried explicitly; these are recorded in a separate gap-fill file. One response (Kazakhstan to World, 2022) was rejected because its tail contained duplicated values and omitted the two largest chapters; Kazakhstan-to-World data for 2020 could not be retrieved. As §4.4 shows, 2020–2022 would have been excluded in any case.

## 4.2 Product Groups

The 97 HS chapters are grouped into four groups. **Energy** is HS 27 (crude oil, gas, coal and products). **Metals and ores** are HS 25, 26, 28, 71, 72 and 74–81: salt and minerals, ores and concentrates, inorganic chemicals including uranium compounds (HS 2844), precious metals, iron and steel including ferroalloys, and base metals (copper, nickel, aluminium, lead, zinc, tin and others). **Agri-food** is HS 01–24. **Other goods** are all remaining chapters, mainly chemicals, plastics, textiles, metal articles, machinery and vehicles. The "strategic minerals" of the registered topic (uranium, copper, ores and ferroalloys) fall inside the metals and ores group and are reported separately where relevant (§6.2). Energy is a single chapter, which matters for inference (§5.7).

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

The pattern is consistent with confidentiality suppression of chapters dominated by few firms, but the reason cannot be confirmed from the data. Two consequences follow. First, Kazakhstan-reported product-level data for 2020–2022 are excluded from all comparisons of China with the rest of the world. Second, the bilateral balance is computed from China's records, which show no such gaps (§6.1). The main export results are re-estimated with China's mirror data for the China side (§6.7, Table 6.7).

## 4.5 The Persistent Import Gap

China's reported exports to Kazakhstan have long exceeded Kazakhstan's reported imports from China: by a factor of 1.5 to 2.5 in 2013–2019, before the 2020–2022 break (Appendix B, Table B.2). Valuation cannot explain it: Kazakhstan records imports CIF and China records exports FOB, so Kazakhstan's figures should be the higher ones. It may reflect goods declared differently at the border, transit through the Eurasian Economic Union customs territory, or under-declaration; the data cannot distinguish these. For this reason the thesis does not use Kazakhstan's import figures to measure the balance. The main balance figures in Chapter 6 are China-reported (China's imports from Kazakhstan minus China's exports to Kazakhstan), and are therefore not comparable in level with figures published by Kazakhstan's Bureau of National Statistics.

## 4.6 Chinese Official Finance

AidData's GCDF 3.0 records 155 Chinese official finance projects in Kazakhstan with commitments in 2000–2021 that AidData recommends for aggregate analysis [@aiddata_gcdf3_2023; @custer_etal_2023]. Amounts are in constant 2021 US dollars. The data record commitments, not disbursements, and they cover official finance only, not private Chinese investment. Syndicated loans appear as one record per lender. These limitations mean the data can show where and when Chinese state finance was committed, but not how much was spent or what it produced.


## 4.7 Summary of Discrepancies and Substitutions

**Table 4.4. Data discrepancies, their likely causes and their treatment**

| Discrepancy | Evidence | Most likely cause | Treatment | Remaining limitation |
|---|---|---|---|---|
| KZ exports of HS 74, 76, 79 absent in 2020–2022 | China reports USD 1.8–2.5 bn of copper imports per year; KZ copper exports to the World only USD 0.11 bn in 2021 (Table 4.3) | Missing partner records, consistent with confidentiality suppression; not valuation (the gap is total, not proportional) | Years excluded from KZ-reported product comparisons; China legs China-reported | Cause cannot be confirmed |
| KZ imports of HS 84, 85, 87 absent in 2020–2022 | No monthly records in these chapters in 2020–2022, present in all other years (Table B.2) | Missing partner records | KZ-reported imports not used for 2020–2022; China's export data used | As above |
| KZ imports from China 1.5–2.5 times below China's exports in normal years | Table B.2; ratio 1.84 in 2024 | Not valuation: Kazakhstan's CIF figures should exceed China's FOB figures, so the CIF/FOB difference widens rather than explains the gap. The cause is unresolved (candidates: under-declaration, attribution by country of origin versus consignment, cross-border shuttle trade, transit within the Eurasian Economic Union) | Levels and the balance from China's data; KZ-reported robustness for comparisons (Table 6.3) | The level of the balance depends on the reporter; comparison-adjusted shares do not (92 per cent with either) |
| KZ exports to China vs China's imports from KZ, ratio 0.89–1.28 outside 2020–2022 | Table 4.2 | CIF/FOB valuation and timing | Either source; China's for comparisons with China-reported imports | Small year-to-year noise |
| Comtrade KZ export totals above WDI in 2011–2012 (4–7 per cent), below in 2010 (4.5 per cent) | Table 4.2 | Differences between publishers' totals | Affects China and RoW alike; absorbed by chapter-by-year effects; base-period averages include these years | Cause not identified |
| Truncated API responses | Missing chapters in some years | Retrieval tool length limit | Missing chapters re-queried; totals validated against WDI | None detected after gap-fill |
| KZ-to-World 2022 response with duplicated values | Identical values for different chapters; HS 27 and 28 absent | Retrieval error | Rejected; year not used | 2022 unavailable |
| Mixed reporters in the comparison against KZ's other partners | China legs China-reported, RoW growth KZ-reported | Necessary because KZ partner data have gaps | Robustness with KZ-reported China legs | Coverage differences between reporters cannot be fully excluded |

Throughout, HS chapters are as reported in each year; the two-digit chapter boundaries are stable across the HS vintages in the data, so no concordance is needed at this level.


# 5. Empirical Strategy

The strategy follows the two parts of the central question. §5.1 decomposes the swing and compares it with Kazakhstan's other partners (SQ1). §5.2–5.4 test the export components (SQ2), and §5.5 compares imports with China's other regional partners (SQ3). §5.6 states the identification limits, and §5.7 the safeguards against multiple testing, exploratory analysis, specification choice and missing data.

## 5.1 Accounting Decomposition and Comparison Against Kazakhstan's Other Partners (SQ1)

**Accounting decomposition.** With all terms China-reported, the change in Kazakhstan's balance with China between periods *t*~0~ and *t*~1~ is

$$\Delta B = \sum_{g} \Delta X^{CN}_{g} - \Delta M^{CN}.$$

For 2013–2024: $\Delta B = (15.91 - 27.95) - (16.05 - 12.55) = -15.55$ (USD bn). This is an identity.

**Comparison against Kazakhstan's other partners.** For each export chapter *p*, the benchmark assumes that exports to China grow at the rate of Kazakhstan's exports of *p* to the rest of the world (RoW):

$$X^{B}_{p,t_1} = X^{CN}_{p,t_0} \cdot \left( X^{RoW}_{p,t_1} / X^{RoW}_{p,t_0} \right)$$

The **China-specific export component** is $\sum_p (X^{CN}_{p,t_1} - X^{B}_{p,t_1})$ and the **common component** is $\sum_p (X^{B}_{p,t_1} - X^{CN}_{p,t_0})$; they sum to the actual change. Where a chapter's RoW base is below USD 1 million, its product group's RoW growth is used. For imports, the same calculation is done on totals: imports from China are benchmarked against the growth of Kazakhstan's imports from all other suppliers (Kazakhstan's imports from the world minus those from China, Kazakhstan-reported). The balance's China-specific component is the export component minus the import component, and its share is that component divided by the actual change in the balance (reported only when both have the same sign).

Data sources: the China legs are China-reported (China's imports from Kazakhstan, CIF; China's exports to Kazakhstan, FOB), because Kazakhstan's partner data have gaps (§4.4–4.5); the RoW growth rates are Kazakhstan-reported. A robustness version uses Kazakhstan-reported China legs throughout.

**What the components are and are not.** The benchmark is a description of how trade with China would have moved had it moved like trade with everyone else; it is not an estimate of what would have happened without the BRI. The China-specific component therefore measures distinctiveness, not causation. It is not an upper bound on a BRI effect, for two reasons: the BRI can change Kazakhstan's trade with other partners too, which moves the benchmark; and BRI effects within the China-specific component can be offset by other China-specific changes. Shift-share components are not additive across sub-periods, and they depend on the base and end years, so they are reported for a grid of alternatives: base years 2012, 2013, 2014 and the 2011–2013 average; end years 2019, 2023, 2024 and the 2023–2024 average (Script 67).


## 5.2 Descriptive Indicators

China's share of Kazakhstan's exports is computed by product group from Kazakhstan's data. Concentration is measured by the Herfindahl–Hirschman index across HS-2 chapters, with and without HS 27, and by the number of chapters exported above USD 1 million.

## 5.3 Triple-Difference PPML for the Export Side (SQ2)

The shift-share split shows which groups have large China-specific components; the PPML model tests whether they are statistically distinguishable from zero and robust. It compares, within each chapter and year, exports to China with exports to RoW:

$$X_{pdt} = \exp\Big(\alpha_{pt} + \gamma_{pd} + \sum_{g} \beta_{g}\,(\text{China}_d \times \text{Post}_t \times G_{pg})\Big)\,\varepsilon_{pdt},$$

where *p* is the chapter, *d* ∈ {China, RoW}, Post = 1 from 2014 and *G* indicates the four product groups.

- **Chapter-by-year effects** α~pt~ absorb everything common to all destinations: world prices, Kazakhstan's production, exchange rate and export policy. They are the regression counterpart of the "common component".
- **Chapter-by-destination effects** γ~pd~ absorb the pre-2014 orientation of each chapter towards China.
- **β~g~** is the post-2013 change in the China/RoW ratio for group *g*; the ratio changes by a factor of exp(β).

Estimation is by PPML [@santos_silva_tenreyro_2006] in `pyfixest`, with standard errors clustered by chapter. Chapter–destination pairs that are always zero are dropped. Main sample: 2005–2019 and 2023–2024 (17 years, 97 chapters, 3,160 observations).

## 5.4 Timing: Event Study and Trend Break (SQ2)

β~g~ compares post-2013 levels with the *pre-2013 average*, so any upward trend yields a positive β whether or not it began with the BRI. Timing is therefore tested directly: an event study replaces Post with year dummies (base 2013), with a joint test of the pre-2013 coefficients; and a trend-break model estimates the China-specific trend before 2013 (θ~g~) and its change afterwards (δ~g~):

$$X_{pdt} = \exp\big(\alpha_{pt} + \gamma_{pd} + \sum_{g}[\theta_{g}\,\text{China}_d G_{pg}(t-2013) + \delta_{g}\,\text{China}_d G_{pg}(t-2013)\text{Post}_t]\big)\varepsilon_{pdt}.$$

Consistency with M1 requires δ~g~ > 0 (acceleration after 2013). The relevant test is therefore one-sided.

## 5.5 Comparison Against China's Other Regional Partners, and the Extensive Margin (SQ3)

The second comparison uses only China's own reports, so each flow has one reporter and one valuation. The benchmark assumes that China's exports to Kazakhstan grow at the rate of China's exports to a comparator *C*:

$$M^{B}_{KZ,t_1} = M_{KZ,t_0} \cdot G_{C}, \qquad \text{Kazakhstan-specific import change} = M_{KZ,t_1} - M^{B}_{KZ,t_1}.$$

Comparators are the world; Russia; Central Asia excluding Kazakhstan (Kyrgyzstan, Uzbekistan, Tajikistan, Turkmenistan); and Central Asia plus Russia. *G*~C~ is computed in two ways: value-weighted (the comparator group's total in *t*~1~ divided by its total in *t*~0~) and as the median of the individual partners' growth factors, which limits the influence of any one partner. Results are reported with and without Russia and for the same grid of base and end years as §5.1.

The same comparison is *not* used for Kazakhstan's exports. China's imports from Russia and Turkmenistan are dominated by oil and gas, whose prices and post-2022 volumes move for reasons unrelated to Kazakhstan, so the regional benchmark for exports is not comparable (Script 67 computes it for completeness). Export distinctiveness is assessed product by product against Kazakhstan's other markets (§5.1, §5.3).

The two comparisons are not nested and are not applied sequentially: they use different reporters, different benchmarks and answer different questions. They are reported side by side.

The extensive margin on the export side is tested by a linear probability model of exporting more than USD 1 million, with the same fixed effects as §5.3.


## 5.6 Identification Limits

The design identifies China-specific change, not its cause. A rise in China's demand for Kazakh sunflower oil, a phytosanitary protocol, a faster border crossing and a Chinese-financed road would produce the same China-specific component. This is why the China-specific component is treated as a description of distinctiveness, not as an estimate or bound of a BRI effect, and why consistency with a BRI mechanism (level B) is the strongest claim made.

## 5.7 Safeguards: Exploratory Analysis, Multiple Testing and Missing Data

**Limiting the search.** All export tests use four product groups fixed by HS chapter boundaries before estimation (§4.2): energy, metals and ores, agri-food and other. The analysis does not search across individual chapters for significant results. Energy is a single chapter and has no valid standard error, so each family of tests has three inferential coefficients.

**Multiple testing.** Holm–Bonferroni adjustments are applied within each family: the three group coefficients of the main triple difference, and the three trend-break coefficients. Robustness variants (Table 6.7) are not counted as separate discoveries; a result is used only if it holds in the main specification after adjustment.

**Randomisation inference.** For agri-food, the group that drives the export-side conclusions, 300 random sets of 24 chapters are drawn from the 96 non-energy chapters and the China × Post and trend-break coefficients are re-estimated. This asks whether agri-food is unusual among Kazakhstan's export chapters, which guards against both small-cluster problems and the possibility that any set of chapters would show a similar change.

**Exploratory elements.** As disclosed in §3.3, the group predictions, the trend-break test, the comparison-adjusted decomposition, the neighbour comparison and the robustness grid were added after inspecting data. The decompositions are descriptive and involve no test. For the tests, the safeguards above apply, and the thesis reports which conclusions would change without them.

**Specification grids instead of single choices.** Every comparison-adjusted figure that enters a conclusion is reported over a grid of four base periods and four end periods (Tables 6.3b, 6.4, 6.10b) and, for imports, six comparator specifications. A conclusion is stated only if it holds across the grid; otherwise the range is reported.

**Independent re-estimation.** With chapter-by-year fixed effects and two destinations, the Poisson model in §5.3 is equivalent to a binomial (logit) model of China's share in each chapter-year, weighted by the chapter-year total. The main coefficients were re-estimated this way with a different library (`statsmodels`) as a check on the `pyfixest` estimates (§6.7).

**Power.** For the trend-break test, the minimum detectable change in the China-specific trend (one-sided 5 per cent test, 80 per cent power) is reported, so that a non-significant result is not mistaken for evidence of no change.

**Missing data.** Missingness has four sources, handled differently:

1. *Confidentiality-type suppression in Kazakhstan's 2020–2022 partner data* (§4.4). This is not random: it removes metals and machinery. These years are excluded from all Kazakhstan-reported product comparisons and from decomposition endpoints; China's mirror data, which show no suppression, are used for the China legs, and the main PPML is re-estimated with them.
2. *Retrieval failures*: Kazakhstan-to-World HS-2 data for 2020 and 2022 and China-reported imports for 2006. These are failures of the retrieval process, unrelated to trade values; they reduce the sample but are not expected to bias it. All three years are outside the decomposition endpoints.
3. *Truncated API responses*: missing chapters were re-queried; completeness was verified against World Bank totals (§4.3).
4. *Limited import detail*: China's exports to Kazakhstan by chapter were collected for 2013, 2019 and 2024 only, and imports from RoW only as totals. The import side is therefore analysed at aggregate level, and import results are presented as descriptive.


# 6. Results

The chapter answers the sub-questions in order: the composition of the swing and its China-specific part (§6.1–6.2, SQ1), its export side (§6.3–6.5, SQ2), its import side (§6.6, SQ3), the robustness of the inferential results (§6.7), and the BRI channels (§6.8, SQ4). §6.9 maps every result to the central question.

## 6.1 The Balance and Its Gross Components

**Table 6.1. Kazakhstan's trade with China, China-reported data (USD bn)**

| | 2013 | 2019 | 2024 |
|---|---:|---:|---:|
| Kazakhstan's exports to China (China's imports, CIF) | 16.05 | 8.86 | 15.91 |
| Kazakhstan's imports from China (China's exports, FOB) | 12.55 | 12.73 | 27.95 |
| Balance for Kazakhstan | +3.51 | −3.87 | −12.04 |

*Source: UN Comtrade, China as reporter [@un_comtrade_hs2_2026]. Author's calculations (Script 61, `trade_balance_decomposition.csv`).*

**Table 6.2. Gross decomposition of the change in the balance (USD bn)**

| Component | 2013→2019 | 2019→2024 | 2013→2024 |
|---|---:|---:|---:|
| Energy exports | −7.56 | +0.36 | −7.20 |
| Metals and ores exports | +0.06 | +5.56 | +5.62 |
| Agri-food exports | +0.30 | +0.56 | +0.86 |
| Other exports | +0.02 | +0.57 | +0.59 |
| Imports from China (enters with a minus sign) | +0.18 | +15.23 | +15.41 |
| **Change in balance** | **−7.37** | **−8.18** | **−15.55** |

*Source: as Table 6.1.*

![Figure 6.1. Gross decomposition of the change in Kazakhstan's balance with China, 2013–2024](../Outputs/generated_figures/fig_r4_balance_decomposition.png)

The swing has two phases. In 2013–2019 the balance fell by USD 7.4 billion while energy exports to China fell by USD 7.6 billion; imports were flat. In 2019–2024 the balance fell by a further USD 8.2 billion because imports rose by USD 15.2 billion, more than offsetting a USD 7.0 billion rise in exports, most of it metals and ores. These are gross changes; they do not yet say whether anything was specific to China.

## 6.2 Is the Swing China-Specific Relative to Kazakhstan's Other Partners? (SQ1)

**Table 6.3. Comparison against Kazakhstan's other partners, 2013 to 2024 (USD bn)**

| Period | Flow | Actual change | Common | China-specific |
|---|---|---:|---:|---:|
| 2013→2019 | Exports | −7.19 | −3.74 | −3.44 |
| | Imports | +0.18 | −2.33 | +2.52 |
| | **Balance** | **−7.37** | **−1.41** | **−5.96** |
| 2019→2024 | Exports | +7.05 | +2.81 | +4.24 |
| | Imports | +15.23 | +4.53 | +10.70 |
| | **Balance** | **−8.18** | **−1.72** | **−6.46** |
| 2013→2024 | Exports | −0.14 | +0.06 | −0.20 |
| | Imports | +15.41 | +1.30 | +14.11 |
| | **Balance** | **−15.55** | **−1.24** | **−14.31** |
| *Kazakhstan-reported China legs* | | | | |
| 2013→2024 | **Balance** | **−6.27** | **−0.52** | **−5.74** |

*§5.1. Export China legs: China-reported imports from Kazakhstan by HS-2 chapter; RoW growth: Kazakhstan-reported exports to World minus China, by chapter. Import China leg: China-reported exports to Kazakhstan; RoW growth: Kazakhstan-reported imports from World minus China (×0.81 in 2013–2019, ×1.36 in 2019–2024, ×1.10 in 2013–2024). Components are not additive across sub-periods. Source: Script 65, `balance_common_vs_china_specific.csv`.*

For 2013–2024, USD 14.31 billion of the USD 15.55 billion swing is China-specific (92 per cent: 14.31 ÷ 15.55). With Kazakhstan's own data the swing is smaller in level (USD 6.27 billion, because Kazakhstan records much lower imports from China, §4.5), but the China-specific share is the same (5.74 ÷ 6.27 = 92 per cent).

The 92 per cent figure is the *highest* value in the robustness grid, because 2013 was the peak year of oil exports to China. Table 6.3b reports all base and end combinations.

**Table 6.3b. China-specific share of the swing under alternative base and end years (China-reported China legs)**

| Base \ End | 2019 | 2023 | 2024 | 2023–24 average |
|---|---:|---:|---:|---:|
| 2011–13 average | 58% (−4.76 of −8.19) | 64% (−8.05 of −12.66) | 77% (−12.55 of −16.36) | **71% (−10.30 of −14.51)** |
| 2012 | 52% (−3.90 of −7.54) | 57% (−6.82 of −12.01) | 71% (−11.12 of −15.72) | 65% (−8.97 of −13.87) |
| 2013 | 81% (−5.96 of −7.37) | 82% (−9.68 of −11.84) | 92% (−14.31 of −15.55) | 88% (−11.99 of −13.70) |
| 2014 | 71% (−0.64 of −0.90) | 56% (−3.01 of −5.37) | 83% (−7.58 of −9.07) | 73% (−5.29 of −7.22) |

*China-specific balance component and actual change in USD bn in brackets. Source: Script 67, `robust_kz_partner_grid.csv`.*

Three results hold in every cell of the grid. (i) Most of the swing is China-specific: between 52 and 92 per cent, and 71 per cent with averaged endpoints, which are least sensitive to single-year spikes. (ii) The China-specific *import* component is small to 2019 (+0.4 to +3.0 billion) and large by 2023–2024 (+8.1 to +14.7 billion). (iii) The China-specific *export* component is negative to 2019 under every base (−0.2 to −3.4 billion). The China-specific export component to 2024, in contrast, depends on the base year: −0.2 billion from 2013, but +2.0 to +3.7 billion from 2011–2013, 2012 or 2014. Any statement that the export side "nets to about zero" is specific to the 2013 base and is not made.

**Table 6.4. China-specific export component by product group (USD bn)**

| Group | 2013→2019 | 2019→2024 | 2013→2024 | Range across the grid, end 2023–2024 |
|---|---:|---:|---:|---|
| Energy | −3.93 | −0.16 | −4.90 | −4.9 to +2.4 (negative from every pre-2014 base) |
| Metals and ores | +0.20 | +3.80 | +3.36 | +1.6 to +6.6 |
| of which strategic minerals (HS 26, 28, 72, 74, 79) | +0.38 | +3.70 | +3.42 | +1.8 to +6.7 |
| Agri-food | +0.25 | +0.13 | +0.82 | +0.7 to +0.9 |
| Other | +0.03 | +0.47 | +0.52 | +0.3 to +0.5 |
| **Total exports** | **−3.44** | **+4.24** | **−0.20** | −0.2 to +5.1 |

*China-reported China legs. With Kazakhstan-reported China legs, 2013→2024: energy −3.61, metals and ores +2.97, agri-food +0.89, other −0.08. Range: base 2011–13 average, 2012, 2013 or 2014; end 2023, 2024 or 2023–24 average. Sources: Script 65, `export_components_by_group.csv`, `strategic_minerals_components.csv`; Script 67, `robust_export_groups_grid.csv`.*

By product group:

1. **Energy.** Oil exports to China fell by more than oil exports to other markets. From any base before 2014 the China-specific component is negative at every end year (−1.2 to −4.9 billion). From a 2014 base it is small and changes sign (−0.7 to +2.4 billion): the China-specific fall is concentrated in the move from 2013 to 2014, and its size at the end depends on the volatile oil exports of 2023–2024.
2. **Strategic minerals.** Their China-specific component is positive under every base and end year (+1.8 to +6.7 billion by 2023–2024), so they offset part of the swing in every specification. How much of this had happened by 2019 depends on the base: +0.4 billion from 2013, +1.7 billion from the 2011–2013 average, +2.4 billion from 2012.
3. **Agri-food and other goods.** Small positive China-specific components in every specification.

![Figure 6.2. Common and China-specific components of the change in Kazakhstan's balance with China](../Outputs/generated_figures/fig_r7_common_vs_specific.png)

The remaining sections ask whether these components are distinguishable from noise (export side), whether the import component is distinctive from China's side, and whether either matches BRI mechanisms.


## 6.3 Export Composition and China's Share

**Table 6.5. Kazakhstan's exports to China by product group (Kazakhstan-reported)**

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

![Figure 6.3. Kazakhstan's exports to China by product group, China-reported, 2005–2024](../Outputs/generated_figures/fig_r1_composition_china.png)

**Table 6.6. China's share of Kazakhstan's exports by product group, % (Kazakhstan-reported)**

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

*Source: as Table 6.5 (`china_share_by_group.csv`, all years). 2020–2022 omitted (§4.4).*

![Figure 6.4. China's share of Kazakhstan's exports by product group](../Outputs/generated_figures/fig_r2_china_share_by_group.png)

China's share of Kazakhstan's energy exports rose from 2.5 to 14–15 per cent between 2005 and 2011, then fell back to 3–7.4 per cent in 2016–2019. China's share of metals and ores rose from 17 to 34 per cent between 2008 and 2010, stayed at 28–35 per cent until 2019, and reached 40–44 per cent only in 2023–2024. China's share of agri-food rose steadily, from below 1 per cent before 2011 to 2.5 per cent in 2013, 11 per cent in 2019 and 19 per cent in 2024.

**Strategic minerals.** China's share of Kazakhstan's ore exports (HS 26) was 44 per cent in 2013 and 41 per cent in 2019, then 80 per cent in 2024; its share of copper (HS 74) rose from 56 to 64 per cent between 2013 and 2024; its share of inorganic chemicals including uranium compounds (HS 28) fell from 42 per cent in 2013 to 23 per cent in 2019 and was 32 per cent in 2024 (Script 61). The largest single movement is the post-2019 shift of ores towards China; how much of the strategic-mineral gain in Table 6.4 had occurred by 2019 depends on the base year.

**Concentration.** The HHI of Kazakhstan's exports to China fell from 0.415 in 2013 to 0.173 in 2024, but almost entirely because oil fell: excluding HS 27 it was 0.212 in 2013 and 0.205 in 2024 (`diversification_indices.csv`). Non-resource goods rose from 1.5 to 11.0 per cent of exports to China, against 6.8 to 16.7 per cent of exports to the rest of the world.

![Figure 6.5. Concentration (HHI) of Kazakhstan's exports to China and to the rest of the world](../Outputs/generated_figures/fig_r6_hhi.png)

## 6.4 Which Export Changes Were Statistically China-Specific? (SQ2)

**Table 6.7. PPML triple difference: change in the China/RoW export ratio after 2013, by product group**

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

*Coefficients on China × Post × group. Chapter-by-year and chapter-by-destination fixed effects. Standard errors clustered by HS-2 chapter in parentheses (unadjusted; Holm-adjusted values in Table 6.12). \*\*\* p < 0.01, \*\* p < 0.05, \* p < 0.1. Energy is a single chapter, so no standard error can be computed [n/a]. Source: Script 62, `ppml_main.csv`.*

The regression confirms the shift-share picture. Relative to the rest of the world, the China ratio fell by 41 per cent for energy, rose by 39 per cent for metals and ores and by a factor of 11.7 for agri-food (row 1). Other goods show no significant change. The agri-food result holds in every variant. The metals result depends on 2023–2024 (row 3). The placebo (row 8), which pretends the BRI began in 2010 and uses only pre-BRI years, finds large "effects" for agri-food and metals: both were already changing before 2013.

## 6.5 Did the Export Changes Begin with the BRI? (SQ2, timing)

![Figure 6.6. Event study: China/RoW export ratio by product group relative to 2013](../Outputs/generated_figures/fig_r3_event_study.png)

**Table 6.8. Event-study coefficients (log China/RoW ratio relative to 2013)**

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

**Table 6.9. Trend-break test: China-specific trend before and after 2013 (log points per year)**

| Group | Chapters | Pre-2013 trend θ | Change after 2013 δ (95% CI) | One-sided *p* for acceleration (δ > 0) |
|---|---:|---:|---:|---:|
| Agri-food | 24 | 0.538 | −0.368 (−0.676 to −0.059) | 0.99 |
| Metals and ores | 12 | 0.095 | −0.070 (−0.194 to 0.053) | 0.87 |
| Other | 60 | −0.017 | 0.107 (−0.163 to 0.376) | 0.22 |
| Energy | 1 | 0.068 | −0.134 [n/a] | n/a |

*PPML with chapter-by-year and chapter-by-destination fixed effects; SE clustered by chapter. Source: Script 62, `ppml_trend_break.csv`; Script 66, `multiple_testing.csv`.*

**Energy.** China's orientation of Kazakhstan's energy exports rose until 2011 and fell sharply from 2014 (−1.56 log points by 2017, relative to 2013) before partly recovering. The China-specific oil decline therefore began with the 2014 price collapse and ran *opposite* to the resource-security mechanism M2. No inference is possible with one chapter.

**Metals and ores, including strategic minerals.** The China orientation rose before 2010, was flat or slightly negative between 2013 and 2019, and turned positive only in 2023–2024. There is no detectable acceleration after 2013 (one-sided *p* = 0.87), although the test could miss a change smaller than about 0.16 log points per year (§6.7). In the regression the rise in China orientation appears only in 2023–2024; in the decomposition, the part of the strategic-mineral gain that occurred by 2019 depends on the base year (§6.2).

**Agri-food.** The China/RoW ratio rose steeply before the BRI: from −3.37 in 2008 to −0.36 in 2012, relative to 2013 (pre-2013 coefficients jointly different from zero, Wald χ²(8) = 664, *p* < 0.001). After 2013 it kept rising but more slowly: the China-specific trend fell from 0.54 to 0.17 log points per year. There is no evidence of the acceleration that M1 requires: the one-sided *p*-value for δ > 0 is 0.99, and the whole unadjusted 95 per cent interval for δ lies below zero, so a non-negative trend change is outside it (with three tests in the family, the corresponding Holm-adjusted p-value for a two-sided test is 0.059, §6.7). Whether the trend significantly *slowed* is less certain (§6.7). In absolute terms, most of the growth came after 2013, from USD 70 million in 2013 to USD 980 million in 2024, led by vegetable oils (HS 15), fodder (HS 23), cereals (HS 10) and oilseeds (HS 12) (`agrifood_chapters.csv`). Both facts hold: the dollar expansion happened in the BRI period, but the China-specific growth rate did not rise when the BRI began.

## 6.6 Was the Import Surge Specific to Kazakhstan? (SQ3)

The China-specific import component is the largest part of the swing (USD 14.1 billion over 2013–2024, Table 6.3). Its timing and Kazakhstan-specificity can be checked against China's trade with neighbouring countries.

**Table 6.10. China's exports to Kazakhstan and to comparison destinations (USD bn, China-reported)**

| Destination | 2013 | 2019 | 2024 | Growth 2013–2019 | Growth 2019–2024 |
|---|---:|---:|---:|---:|---:|
| Kazakhstan | 12.55 | 12.73 | 27.95 | ×1.01 | ×2.20 |
| Kyrgyzstan | 5.08 | 6.28 | 19.90 | ×1.24 | ×3.17 |
| Uzbekistan | 2.61 | 5.03 | 11.65 | ×1.93 | ×2.31 |
| Russia | 49.59 | 49.75 | 115.28 | ×1.00 | ×2.32 |
| World | 2,209 | 2,499 | 3,577 | ×1.13 | ×1.43 |

*Source: UN Comtrade, China as reporter, total trade [@un_comtrade_hs2_2026]. Author's calculations (Script 65, `china_exports_regional_comparison.csv`).*

![Figure 6.7. Growth of China's exports to Kazakhstan, its neighbours and the world](../Outputs/generated_figures/fig_r8_regional_imports.png)

Two facts stand out. First, in the BRI construction period (2013–2019) China's exports to Kazakhstan grew *less* than its exports to the world (×1.01 against ×1.13) and much less than to Kyrgyzstan or Uzbekistan. Whether there was any China-specific import rise in this period depends on the data source: with China's export figures it is +USD 2.5 billion, with Kazakhstan's own import figures it is zero (Script 65), because the gap between the two sources widened in these years (§4.5). Second, the surge came after 2019, and mainly in 2022–2024: China's reported exports to Kazakhstan were USD 11.7 billion in 2020, 13.8 billion in 2021, 16.4 billion in 2022, 24.7 billion in 2023 and 28.0 billion in 2024 (Table B.2 and Table 6.1). Kyrgyzstan, Uzbekistan and Russia show the same or faster growth from China in 2019–2024. The import surge is therefore regional and post-2022, not specific to Kazakhstan or to the BRI's timing. Kazakhstan's own exports of machinery, electrical equipment and vehicles to Russia rose from USD 0.33 billion in 2019 to USD 2.25 billion in 2023 (`russia_manufactures_check.csv`), consistent with part of the surge passing through Kazakhstan, although Comtrade does not record the origin of re-exported goods.

**Table 6.10b. Imports from China: Kazakhstan-specific change relative to China's exports to comparators (USD bn, China-reported)**

| Comparator (weighting) | 2013→2019 | 2013→2024 | 2011–13 avg → 2023–24 avg | Range, end 2019 | Range, end 2023–2024 |
|---|---:|---:|---:|---|---|
| Russia | +0.14 | −1.21 | −1.93 | +0.14 to +0.95 | −3.37 to +0.66 |
| Central Asia excl. Kazakhstan (value-weighted) | −2.91 | −14.38 | −13.85 | −2.91 to −1.51 | −18.40 to −10.58 |
| Central Asia excl. Kazakhstan (median) | −0.37 | −8.43 | −6.10 | −0.37 to +1.12 | −12.01 to −4.33 |
| Central Asia + Russia (value-weighted) | −0.40 | −3.54 | −4.13 | −0.40 to +0.40 | −6.03 to −1.64 |
| Central Asia + Russia (median) | +0.14 | −1.21 | −1.93 | +0.14 to +0.95 | −3.37 to +0.66 |
| World | −1.46 | +7.64 | +7.62 | −1.46 to −0.69 | +5.50 to +8.75 |
| *Memo: Kazakhstan's imports from its other suppliers (Table 6.3)* | +2.52 | +14.11 | +12.98 | | |

*Actual minus benchmark imports from China (§5.5). Positive: Kazakhstan's imports from China grew faster than the comparator. Central Asia excl. Kazakhstan = Kyrgyzstan, Uzbekistan, Tajikistan, Turkmenistan. Ranges cover base years 2011–13 average, 2012, 2013, 2014 and the listed end years. The median of Central Asia plus Russia coincides with Russia's growth factor in these years. Source: Script 67, `robust_china_neighbour_grid.csv`; memo row from Scripts 65 and 67.*

The benchmark decides the answer, and Table 6.10b shows how. Against Kazakhstan's other suppliers and against China's exports to the world, Kazakhstan's imports from China rose unusually fast after 2019. Against China's exports to Kazakhstan's neighbours, they did not: in every specification ending in 2023–2024, the Kazakhstan-specific change is at most +0.66 billion and in most cases negative, with or without Russia. In the BRI construction period (to 2019) it is close to zero against every neighbour comparator (−2.9 to +1.1 billion) and negative against the world.

How credible is this as evidence about the BRI? Three qualifications apply.

1. *The comparators are not neutral.* After 2022 China's exports to Russia, and to Kyrgyzstan as a transit hub, were shaped by sanctions and re-routing. A comparator affected by re-exports to Russia may be "inflated", which would make Kazakhstan look less distinctive than it is. Kazakhstan was itself part of that re-routing: its own exports of machinery, electrical equipment and vehicles to Russia rose from USD 0.33 billion in 2019 to USD 2.25 billion in 2023 (`russia_manufactures_check.csv`), although Comtrade does not record the origin of re-exported goods. The comparison therefore shows that Kazakhstan's import rise belongs to a regional pattern, not that the pattern has a single cause.
2. *The comparators are BRI participants.* The comparison removes any region-wide BRI effect along with other regional shocks, so it cannot by itself show that the BRI played no role. The argument against a BRI explanation of the import rise rests on timing: the rise came after 2019, mostly in 2022–2024 (China's reported exports to Kazakhstan: USD 12.7 billion in 2019, 11.7 billion in 2020, 13.8 billion in 2021, 16.4 billion in 2022, 24.7 billion in 2023, 28.0 billion in 2024), whereas BRI infrastructure was built mainly in 2015–2019, a period in which Kazakhstan's imports from China grew more slowly than China's exports to the world.
3. *Imports are measured with error.* Kazakhstan records far lower imports from China than China records exports (§4.5); the comparison uses China's data on both sides to avoid mixing reporters.

The conclusion about imports is therefore graded as follows: the rise after 2019 is **not distinctive to Kazakhstan** relative to China's regional partners (robust to comparator, weighting, base year and the inclusion of Russia), and it is **inconsistent with the timing** predicted by the connectivity mechanism. Whether a region-wide BRI effect contributed to it cannot be determined from these data.


**Table 6.11. Kazakhstan's imports from China by main chapter, China-reported (USD bn)**

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

*Source: UN Comtrade, China as reporter (Script 61, `import_composition_china_reported.csv`).*

## 6.7 Inference Safeguards and Robustness

**Table 6.12. Multiple-testing and randomisation checks**

| Test | Estimate | Unadjusted *p* | Holm-adjusted *p* | Randomisation check (300 random sets of 24 chapters) |
|---|---:|---:|---:|---|
| Main: China × Post × metals and ores | 0.329 | < 0.001 | < 0.001 | n/a (12 chapters) |
| Main: China × Post × agri-food | 2.456 | < 0.001 | < 0.001 | Larger than all 300 draws (*p* < 0.004); median draw 0.39, 95th percentile 1.24 |
| Main: China × Post × other | 0.634 | 0.224 | 0.224 | n/a |
| Trend change δ, agri-food | −0.368 | 0.020 | 0.059 | Lower than 99.3% of draws (one-sided *p* = 0.007) |
| Trend change δ, metals and ores | −0.070 | 0.264 | 0.528 | n/a |
| Trend change δ, other | 0.107 | 0.437 | 0.528 | n/a |

*Holm–Bonferroni within each family of three coefficients. Source: Script 66, `multiple_testing.csv`, `permutation_agrifood.csv`.*

**What survives.** The China-specific rise in agri-food survives Holm correction and is larger than in any of 300 random sets of chapters of the same size, so it is unlikely to be an artefact of the choice of product group or of small-cluster inference. The metals result survives Holm correction in the main sample but not the exclusion of 2023–2024, so it is treated as a post-2022 result. No group shows a significant acceleration after 2013 (one-sided *p* = 0.99 for agri-food, 0.87 for metals and ores, 0.22 for other goods). The point estimates of δ are negative for agri-food and metals; for other goods it is positive but imprecise, which is absence of evidence rather than evidence either way.

**What does not.** The claim that the agri-food trend significantly *slowed* after 2013 is weaker than the other results: it fails the Holm correction at 5 per cent (adjusted *p* = 0.059), though the randomisation check (*p* = 0.007) supports it. The thesis therefore relies on "no acceleration", not on "slowdown".

**Robustness to data source and missing data.** With China's mirror data for the China leg, the export coefficients keep their signs and similar sizes (Table 6.7, row 2), and the 2020–2022 suppression does not enter because those years are excluded. In the decomposition, the China-specific share of the balance change is 92 per cent with either country's data (Table 6.3). The import-side conclusion for 2013–2019 is the only result that depends on the data source, and it is reported as such.

**Independent re-estimation.** Re-estimating the main model as a weighted binomial model of China's share in each chapter-year (§5.7) reproduces the PPML point estimates to four decimal places (metals and ores 0.3288, agri-food 2.4559, other 0.6340, energy −0.5280); clustered standard errors differ slightly because of small-sample adjustments (agri-food 0.220 against 0.213; metals and ores 0.077 against 0.074; other 0.538 against 0.522). Every main table was also regenerated from the raw files, and all values reproduced to within 0.001 (Appendix A).

**What the tests could detect.** The minimum change in the China-specific trend detectable with 80 per cent power at a one-sided 5 per cent level is about 0.39 log points per year for agri-food (SE 0.157) and 0.16 for metals and ores (SE 0.063). A BRI effect that raised the China orientation of these groups by less than this each year would not be detected. The non-significant trend changes for metals and other goods are therefore absence of evidence, not evidence of no change.

**Extensive margin.** In a linear probability model of exporting more than USD 1 million, the pooled China × Post effect is 0.013 (SE 0.040, *p* = 0.75): the number of chapters Kazakhstan exports to China did not rise relative to other markets. For agri-food alone the effect is 0.21 (SE 0.11, *p* = 0.06), from a base of 10 per cent (`extensive_margin_lpm.csv`). The extensive-margin prediction of M1 is not supported at HS-2 level.

## 6.8 Do BRI Channels Match the Distinctive Components? (SQ4)

**Table 6.13. Chinese official finance commitments to Kazakhstan by sector and period (USD bn, constant 2021)**

| Sector (AidData) | 2000–2008 | 2009–2013 | 2014–2017 | 2018–2021 | Total |
|---|---:|---:|---:|---:|---:|
| Industry, mining, construction | 15.88 | 19.57 | 6.38 | 2.81 | 44.64 |
| Energy | 2.75 | 7.21 | 0.36 | 0.13 | 10.46 |
| Transport and storage | 0.43 | 0.00 | 1.92 | 1.78 | 4.13 |
| Other sectors | 0.87 | 1.39 | 1.88 | 0.78 | 4.92 |
| **All sectors** | **19.93** | **28.17** | **10.54** | **5.50** | **64.15** |

*Source: AidData GCDF 3.0, 155 projects recommended for aggregates [@aiddata_gcdf3_2023]. Author's calculations (Script 61, `aiddata_by_sector_period.csv`). No agriculture, forestry or fishing project is recorded.*

![Figure 6.8. Chinese official finance commitments to Kazakhstan by year, 2000–2021](../Outputs/generated_figures/fig_r5_aiddata_by_year.png)

Recorded Chinese official finance to Kazakhstan was largest *before* the BRI: USD 48.1 billion (constant 2021 dollars) in 2000–2013 against USD 16.0 billion in 2014–2021. The largest pre-2013 commitments financed the Central Asia–China gas pipeline (2008, 2012), the acquisition of Kazakh oil companies (PetroKazakhstan 2005, Mangistaumunaigas 2009) and the Bozshakol (2009) and Aktogay (2011) copper mines (AidData records 61056 and 41941). After 2013 finance shifted towards transport: five China Eximbank road loans in 2017–2018 and a 2019 loan for border checkpoint modernisation. The Khorgos dry port began operating in 2015 [@ktze_khorgos_2025]. Kazakhstan reported in 2023 that protocols covered 24 plant and livestock products [@astanatimes_agri_2023]; the dates of individual protocols could not be verified.

Matching channels to components:

- **M2 (resource finance) and energy and minerals.** Resource finance was concentrated before 2013, and so was the rise in China's orientation of energy and metals (2005–2011). In the BRI period finance in these sectors fell, energy's China orientation fell, and metals' was flat until 2019. The China-specific gain in strategic minerals is positive in every specification, but its timing depends on the base year and does not coincide with the period of Chinese resource finance.
- **M1 (connectivity, market access) and agri-food.** Transport, border and market-access channels are post-2013, and agri-food is the one group whose China orientation kept rising after 2013 and which is most exposed to phytosanitary access and border speed. Recorded finance never went into agriculture, so if a BRI channel is involved it is access and logistics, not finance. But the reorientation began before these channels existed and did not accelerate when they appeared.
- **M1 and imports.** Connectivity should have raised imports from China from 2015 onwards. Instead, China's exports to Kazakhstan stagnated in 2013–2019 and surged after 2022, together with those to Kyrgyzstan, Uzbekistan and Russia.

## 6.9 Synthesis: Each Result and the Central Question

**Table 6.14. Components of the swing, their distinctiveness and their fit with BRI mechanisms**

| Component | China-specific vs Kazakhstan's other partners (2013→2024; grid range to 2023–24) | Distinctive vs China's regional partners? | Timing | Mechanism tested | Verdict | Kind of evidence |
|---|---|---|---|---|---|---|
| Imports from China | +14.1 bn (+8.1 to +14.7) | **No** (≤ +0.7 bn in every neighbour specification) | Mainly 2022–2024 | M1 (Kazakhstan-specific rise from 2015) | Not distinctive; timing inconsistent with M1 | Comparison-adjusted; descriptive |
| Energy exports | −4.9 bn (−4.9 to +2.4; negative from every pre-2014 base) | Not assessed (comparators' exports dominated by oil and gas) | Concentrated 2013→2014 | M2 (positive) | Inconsistent with M2 (opposite sign) | Comparison-adjusted; PPML point estimate, no inference |
| Strategic minerals exports | +3.4 bn (+1.8 to +6.7) | Not assessed | Base-dependent; mostly after 2019 from a 2013 base | M2 (positive after finance) | Offsets part of the swing in every specification; timing does not identify M2 | Comparison-adjusted; PPML significant only with 2023–24 |
| Agri-food exports | +0.8 bn (+0.7 to +0.9) | Not assessed | Rising from 2008; no acceleration after 2013 | M1 (positive, accelerating) | Consistent in products and channel; inconsistent in timing | PPML, Holm and randomisation; trend test |
| Other exports | +0.5 bn (+0.3 to +0.5) | Not assessed | Mainly after 2019 | M1 | Absence of evidence (not significant) | PPML |
| Extensive margin | | | | M1 | Absence of evidence (pooled estimate near zero, imprecise for agri-food) | LPM |

*Imports enter the balance with a minus sign. Sources: Tables 6.3, 6.3b, 6.4, 6.7–6.10b, 6.12.*

Read together, the table answers the central question. From Kazakhstan's side the swing is mostly China-specific, and its largest component is the post-2019 import rise. From China's side that import rise is regional, not Kazakh. The export components that are distinctive either run against the resource-security mechanism (oil), offset the swing without BRI-specific timing (strategic minerals), or match the connectivity mechanism in products but not in timing (agri-food). No component shows the combination of distinctiveness, predicted sign and post-2013 timing that level B requires, except agri-food in products and channel only.


# 7. Discussion

## 7.1 The Answer to the Central Question

The central question asked whether the post-2013 swing in Kazakhstan's balance with China is distinctive to the relationship and whether its distinctive components are consistent with BRI mechanisms. The answer has three parts.

**From Kazakhstan's side, the swing is mostly China-specific.** Relative to Kazakhstan's trade with its other partners, between 52 and 92 per cent of the swing is specific to China, depending on base and end years, and 71 per cent with averaged endpoints (Table 6.3b). The commodity cycle alone does not explain it. This is a statement about distinctiveness, not causation, and it is not an upper bound on a BRI effect (§5.1).

**From China's side, its largest component is regional.** The largest China-specific component is the rise in imports from China after 2019. Relative to China's exports to Russia and the other Central Asian states, Kazakhstan's imports from China to 2023–2024 grew no faster, or at most by USD 0.7 billion, under any comparator, weighting or base year (Table 6.10b). The rise is part of a regional pattern concentrated in 2022–2024.

**None of the large components has the timing or direction BRI mechanisms predict.** The import rise came after 2019, not when BRI connectivity was built, and in 2013–2019 China's exports to Kazakhstan grew more slowly than China's exports to the world. The China-specific fall in oil exports, concentrated in 2014, has the opposite sign to the resource-security mechanism. Strategic minerals offset part of the swing in every specification, but the timing of their China-specific gain depends on the base year and does not single out a BRI period. Agri-food matches the connectivity mechanism in products and channel, but its reorientation towards China began before 2013 and did not accelerate after it.

In the terms of §1.5: the BRI is supported as the **context (A)** of a swing that is China-specific from Kazakhstan's side; the agri-food reorientation is **consistent with a BRI mechanism (B)** in products and channel but not in timing; and **no causal claim (C)** is made or supported.

## 7.2 What These Results Do and Do Not Say About the BRI

The results must be read with three distinctions in mind.

- **Evidence inconsistent with a mechanism.** The oil decline contradicts M2's prediction for energy; the timing of the import rise contradicts M1's prediction for imports; the absence of acceleration in agri-food contradicts M1's timing prediction. These are the thesis's strongest negative findings.
- **Absence of evidence.** The extensive-margin test, the "other goods" coefficient and the post-2013 trend change for metals are imprecise: their confidence intervals include economically meaningful positive values. The minimum change the trend-break test could detect with 80 per cent power is about 0.39 log points per year for agri-food and 0.16 for metals and ores (§6.7). Effects of the size predicted by the ex-ante literature, a few per cent of trade [@baniya_rocha_ruta_2020; @desoyres_etal_2020], are well below what this design can detect.
- **No evidence of no effect.** Nothing here shows that the BRI had no economically meaningful effect on Kazakhstan. In particular, the BRI's best-documented channel, China–Europe rail transit [@mau_seuren_2023], generates service revenue for Kazakhstan that merchandise trade data do not record.

## 7.3 Why the BRI Remains the Right Frame

First, the question of whether the BRI changed Kazakhstan–China trade is the one asked in policy debate and in the registered topic, and it can only be answered by a design that compares the relationship with appropriate benchmarks. The thesis provides that design.

Second, the swing is China-specific from Kazakhstan's side. Had it been common to all of Kazakhstan's partners, the BRI would have been irrelevant and its place in the title decorative. Because it is China-specific, the BRI is the natural candidate, and because the BRI is both bilateral and regional, it had to be tested at both levels.

Third, the conclusions are about the BRI: which of its mechanisms the evidence contradicts (resource security for energy; connectivity timing for imports and agri-food), where it is silent (small average effects, transit services), and what the swing is instead (a China-specific change from Kazakhstan's side that, in its largest part, belongs to a regional pattern after 2019).

## 7.4 The Swing Is Not a Loss: Interpreting the Balance

The swing is not evidence that Kazakhstan lost from trade with China. Of the USD 15.2 billion rise in imports from China in 2019–2024, USD 7.2 billion (47 per cent) was machinery, electrical equipment and vehicles, and USD 4.4 billion (29 per cent) apparel and footwear (Table 6.11). The first group can embody investment in Kazakhstan's capital stock, and both groups can lower prices for Kazakh firms and consumers; part of the first group also appears to have been re-exported to Russia (§6.6). The data cannot separate these uses. On the export side, the China-specific gains in strategic minerals and agri-food mean that Kazakhstan sold more of these products to China than its trade with other markets would imply. A bilateral deficit is consistent with all of these outcomes.

## 7.5 Strategic Minerals and the Balance

The registered topic asks about the role of strategic mineral exports. They **offset part of the swing**. Exports to China of ores, uranium compounds, ferroalloys, copper and zinc rose by USD 5.6 billion between 2013 and 2024, and their China-specific component is positive in every specification (USD 1.8–6.7 billion by 2023–2024; Table 6.4). Three qualifications apply:

1. In the 2013-base calculation, most of the China-specific gain came after 2019, mainly through ores, whose China share rose from 41 to 80 per cent. From earlier bases, a larger part (USD 1.7–2.4 billion) had occurred by 2019. The timing does not single out the BRI period.
2. The gain increased Kazakhstan's dependence on China as a buyer of ores and copper (§7.6).
3. The earlier version of this thesis found that the association between mineral exports and the balance weakened after 2013. The decomposition explains that pattern: the balance fell for reasons on other lines of the account (oil, then imports) while minerals rose, so a regression of the balance on minerals shows a weakening association without minerals having caused anything (Appendix B).

## 7.6 Dependence Is Two-Sided, but Mostly Asymmetric

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

For ores, copper and most agri-food chapters, China matters far more to Kazakhstan as a buyer than Kazakhstan matters to China as a supplier [@keohane_nye_1977; @hirschman_1945]. Zinc is closer to mutual dependence. Uranium is the main exception, and HS-2 data understate it because HS 28 mixes uranium with other chemicals: Kazakhstan supplied about two-thirds of China's natural uranium imports in 2023 [@pan_2024] and 39 per cent of the world's mined uranium in 2024 [@wna_2026], and Chinese companies had to accept minority positions to secure access [@pan_2024].

Dependence is not vulnerability. Ores and copper trade on world markets, and redirection is possible: China's share of Kazakhstan's refined copper exports fell from 65.4 to 49.1 per cent between January–November 2024 and the same period of 2025, while Türkiye's rose to 40.9 per cent [@astanatimes_copper_2026]. The China-specific mineral gain raised Kazakhstan's sensitivity to Chinese demand; this thesis finds no evidence that it created leverage and does not assume that it did.

## 7.7 Alternative Explanations and What Remains Unexplained

- **China's own demand.** China-specific demand growth for vegetable oils and feed would produce the same agri-food component as BRI market access; the design cannot separate them (§5.6).
- **Post-2022 regional trade.** The import rise and the metals shift both occur in 2023–2024. The neighbour comparison places the import rise in a regional pattern; the share of re-exports to Russia cannot be measured with these data.
- **Oil.** The China-specific oil decline in 2014 is not explained here. Candidate explanations (routing of Kazakh crude, Chinese supply diversification, contract changes) could not be verified and are not asserted.
- **Pre-BRI Chinese investment.** Chinese finance for pipelines, oil companies and copper mines before 2013 coincides with the rise of China's share of energy and metals in 2005–2011. The coincidence is consistent with, but does not prove, a link.

## 7.8 Policy Implications

1. **Do not read the bilateral deficit as a BRI failure or a loss.** Its largest component is a regional import rise after 2019, much of it capital and durable goods.
2. **Monitor the relationship by component and against two benchmarks,** Kazakhstan's other partners and China's other regional partners, rather than by bilateral turnover or balance.
3. **Strategic minerals supported the balance.** The concentration of ore and copper sales on China rose and should be monitored, but the 2025 copper data show that redirection is feasible.
4. **Agri-food access is the BRI-era channel with a measurable footprint in merchandise trade.** Phytosanitary protocols and border processing matter more for it than Chinese finance.
5. **Fix the statistics.** Kazakhstan's partner data for 2020–2022 omit major chapters, and its imports from China are far below China's export records.


# 8. Conclusion

## 8.1 Summary

Kazakhstan's merchandise balance with China swung from +USD 3.5 billion in 2013 to −USD 12.0 billion in 2024. Relative to Kazakhstan's other partners, most of that swing (52–92 per cent; 71 per cent with averaged endpoints) is specific to China, so the commodity cycle does not explain it and the BRI is a legitimate candidate. Relative to China's other regional partners, the largest component, a rise in imports after 2019, is not specific to Kazakhstan. On the export side, the China-specific fall in oil runs against the BRI's resource-security mechanism, strategic minerals offset part of the swing in every specification, and the agri-food reorientation, the one change consistent with a BRI mechanism in products and channel, began before 2013 and did not accelerate after it. The BRI is the right frame for the question, the evidence is inconsistent with the specific BRI mechanisms tested, and it does not show that the BRI had no effect on Kazakhstan.

## 8.2 Limitations

1. **No causal identification.** The comparisons measure distinctiveness; they are neither estimates nor bounds of BRI effects.
2. **Base-year sensitivity.** Shares and components depend on base and end years; 2013 was the peak year of oil exports to China. All key conclusions are reported as ranges over a grid (Table 6.3b, 6.4, 6.10b), and claims that held only for one base year have been removed.
3. **Comparators.** The neighbour comparison is affected by post-2022 re-routing and sanctions, by re-export hubs and by the neighbours' own BRI participation.
4. **Aggregation.** HS-2 chapters mix products (uranium with other chemicals). Imports from other partners were collected as totals, and China's exports to Kazakhstan by chapter only for 2013, 2019 and 2024.
5. **Power.** The tests can detect only large changes in trends (§6.7); small average effects of the kind predicted by the ex-ante literature are undetectable here.
6. **Energy is one chapter,** so no statistical inference is available for it.
7. **Missing years.** Kazakhstan's 2020–2022 product data are unusable for partner comparisons; Kazakhstan-to-World 2020 and 2022 and China-reported 2006 were not retrieved.
8. **Merchandise only.** Transit and other services, a main BRI channel for Kazakhstan, are outside the data.
9. **AidData** records official commitments, not disbursements or private investment.
10. **Exploratory elements.** Several analyses were added after earlier results were seen (§3.3); safeguards are described in §5.7.

## 8.3 Future Research

HS-6 data would allow testing the agri-food reorientation against the dates of individual phytosanitary protocols and measuring the extensive margin properly. Product-level import data for Kazakhstan and its neighbours would show which goods drove the post-2019 rise and how much passed on to Russia. Data on transit volumes and revenues would allow the BRI's main channel for Kazakhstan, which this thesis cannot observe, to be studied directly.


# References

::: {#refs}
:::


# Appendix A: Data and Code

**Reproduction.** From the repository root: `python Scripts/60_build_hs2_panel.py`, then Scripts 61, 62, 64, 65, 66, 67 and 63 (figures), then `python Scripts/50_build_paper.py`, then `python Scripts/68_reconcile_manuscript.py`, which checks key figures in this manuscript against the output tables (29 of 29 found in the final version). All output tables were regenerated from the raw files during the final audit and reproduced the previous values to within 0.001. Python packages: pandas, numpy, statsmodels, pyfixest (0.60), matplotlib, openpyxl, scipy.

**Table A.1. Scripts and outputs**

| Script | Purpose | Main outputs |
|---|---|---|
| 60_build_hs2_panel.py | Parse raw HS-2 files, merge gap-fills, validate totals | `hs2_panel_long.csv`, `hs2_validation.csv` |
| 61_composition_diversification.py | Composition, China shares, HHI, suppression check, balance decomposition, imports, AidData, Russia check, agri chapters | Tables 4.3, 6.1, 6.2, 6.5, 6.6, 6.11, 6.13 |
| 62_ppml_triple_difference.py | PPML triple difference, robustness, event study, pre-trend test, trend break, extensive margin | Tables 6.7–6.9, extensive margin (§6.7) |
| 63_figures_reconstruction.py | Figures 6.1–6.8 | `fig_r1`–`fig_r8` |
| 64_two_sided_dependence.py | Two-sided dependence, 2024 | Table 7.1 |
| 65_common_vs_china_specific.py | Shift-share split into common and China-specific components; strategic minerals; neighbour comparison | Tables 6.3, 6.4, 6.10, 6.10b |
| 66_multiple_testing_permutation.py | Holm adjustment, one-sided acceleration tests, randomisation inference (300 draws, seed 20261031) | Table 6.12 |
| 67_robustness_baselines_comparators.py | Grids over base and end years; comparison with China's regional partners for both flows, value-weighted and median, with and without Russia | Tables 6.3b, 6.4 (ranges), 6.10b |
| 68_reconcile_manuscript.py | Checks key manuscript figures against output tables | `reconciliation_report.csv` |

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
