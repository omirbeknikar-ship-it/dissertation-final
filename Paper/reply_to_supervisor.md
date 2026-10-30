Dear Professor,

Thank you for your comments. I have worked on both points. A summary is below, and the full changes are in the updated dissertation (new §4.7, §5.5–5.6, §6.11 and §6.17–6.20).

**1. Sample size (N = 24)**

- **Quarterly disaggregation (n = 96).** I disaggregated the annual series to quarters with the Denton method (§6.17). The coefficients are almost unchanged (interaction −2.40 against −2.38 annually). Interpolated quarters are functions of the same 24 annual totals, though, so I ran a Monte Carlo check. With conventional standard errors, interpolated data reject a true null 47% of the time, against 21% for the annual data. With HAC standard errors there is no gain. I therefore report the quarterly model as a robustness check, not as independent evidence.
- **Observed monthly data (n = 120).** To address the sample-size issue with new information, I collected monthly Kazakhstan–China trade data from UN Comtrade for 2010–2019, with NBK exchange rates and World Bank commodity prices (§6.18). The results support H2 (β = 1.26, p = 0.001) and H3 (interaction −0.91, p = 0.008, adjusted R² = 0.70). They are robust to a trend, the copper price, a dynamic specification and an alternative break date. One qualification: the interaction disappears when monthly oil exports are controlled for, so I describe the weakening as not demonstrably mineral-specific.

**2. Interpretation, hypothesis testing and model fit**

- Each hypothesis now has a stated H₀ and H₁, the HAC t-statistic, degrees of freedom, one- and two-sided p-values and an explicit decision (§6.11). H1 is not supported, and H2 and H3 are supported as conditional associations. I interpret the coefficients in terms of the association between mineral exports and the balance, not causation.
- Full fit statistics are reported for every model: R², adjusted R², F-test (classical and HAC), AIC, BIC, standard error of the regression and residual diagnostics. The primary annual model has R² = 0.742 and F = 6.15 (p = 0.002).
- Granger causality tests (VAR in differences and Toda–Yamamoto) at annual and monthly frequency (§6.19) show that mineral exports do not Granger-cause the trade balance. In monthly data the two series predicted each other only before 2013.

**An additional data issue I would value your view on**

While comparing Kazakhstan's reported imports from China with China's reported exports to Kazakhstan, I found that Kazakhstan's import figures for 2020–2022 appear under-recorded. The ratio between the two sources is about 2.2 in 2016–2019, 4.6–6.0 in 2020–2022, and 1.5 in 2023, and machinery, electronics and vehicle import records are missing in those years. This explains much of the earlier finding that the result depends on 2023. With mirror-adjusted imports, the interaction remains significant without 2023 (§4.7, §6.20). I keep the original series as the baseline and report the adjusted one as a sensitivity check. Would you prefer that I keep this framing, or use the adjusted series as the main specification?

**Final audit before the pre-defence**

I also re-checked the parts of the thesis that had not been verified:

- **References:** six bibliography entries had wrong authors, titles or years, or could not be found, and two had minor date or publisher errors. I corrected them against publisher records or removed them.
- **Oil data:** an annual "oil exports" series in the dataset turned out to be a placeholder, a fixed 55% of total exports. I removed it and replaced the analysis with observed monthly oil data. These show that oil fell from 59% of exports to China in 2010–2013 to 36% in 2014–2019, which helps explain the post-BRI pattern.
- **DiD:** the cross-partner comparison originally reported p = 0.0002 using standard errors that are not suitable for a panel. With appropriate methods the estimate is unchanged (China shows the largest decline of six partners), but its precision is lower (p ≈ 0.02–0.38). I now present it as supporting rather than main evidence.

Kind regards,
Nikar Omirbek
