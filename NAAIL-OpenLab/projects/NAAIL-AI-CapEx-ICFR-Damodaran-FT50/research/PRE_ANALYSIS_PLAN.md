# Pre-analysis plan (draft; not preregistered)

## Question
Do internal-control deficiencies and latent accounting-information risks attenuate the realization and pricing of AI-related capital investment?

## Data universe
Candidate US SEC-filing firms, approximately 2017–2026, with design-dependent outcomes extending beyond the most recent financial-year observation. Firm-by-fiscal-year identification uses CIK; maintain accession-level evidence. Proposed sample size (300–500) is only a feasibility target.

## Constructs
- AIInvestment: separately coded intensity of AI infrastructure and technology investment, extracted from filings/calls where disclosed. Keep confidence grades and do not impute total capex as AI capex.
- ICFRRisk: disclosed material-weakness indicator AND a separately constructed continuous predictive score based exclusively on prior-public information. Reconstruct actual MW disclosures from archival filings; do not use future labels as t predictors.
- Cash-flow realization: next-year/next-two-year FCFF and changes in operating cash flow, scaled as appropriate; distinguish investment-period mechanical cash-flow reductions from low NPV.
- Value creation: incremental ROIC relative to WACC; use consistent invested-capital conventions.
- Market outcome: announcement-window returns or prediction errors with fully specified event timestamps and risk-model benchmarks.

## Preliminary hypotheses — no significance claimed
H1. Higher ICFRRisk weakens the relationship between AIInvestment and subsequent cash-flow realization.
H2. The association between AIInvestment and event-window market reactions depends on the ICFRRisk × earnings–cash-flow divergence interaction.
H3. Latent pre-disclosure ICFR signals contribute incremental out-of-time predictive power above observable controls and conventional baseline models.

## Illustrative model
Outcome[i,t+h] = alpha + beta1*AIInvestment[i,t] + beta2*ICFRRisk[i,t] +
 beta3*(AIInvestment[i,t]*ICFRRisk[i,t]) + gamma'*Controls[i,t] + firmFE + industryYearFE + error[i,t].

FirmFE and industryYearFE may be redundant with some specifications. Determine identifiable estimands and variation BEFORE estimation. Cluster errors at firm or appropriate multi-way level, pre-specify inference. Interpretation of beta3 is associational unless a credible identification design is validated.

## Identification and falsification
- Leakage-safe holdouts, historical data-vintage reconstruction, synthetic placebo outcomes, event-date shifts, alternate AI-investment intensity proxies.
- Compare pretrends for any proposed DiD shock. Do not manufacture quasi-experimental status from a general AI investment trend.
- Benchmark Logit / linear models, panel estimators, gradient boosting, FinBERT text scores, and TimesFM-based features.
- Test sensitivity to non-disclosing firms, hyper-scalers, public reporting formats, low MW base rate and investment-horizon differences.
- Hypotheses and model specifications must be frozen before confirmatory analysis.

## Economic and ML evaluation
Report PR-AUC, precision/recall at fixed monitoring capacity, Brier, calibration, temporal generalization, uncertainty intervals, and net benefits. Report investment and disclosure outcomes separately. A higher AUC is not a standalone FT50 contribution.

## Go/no-go before full-scale collection
Proceed only after manually validating AI-related investment coding, proving sample variation in ICFR measures, and demonstrating viable out-of-time outcomes with accessible data and documented licensing.


## PCAOB / CAM extension — appended 2026-10-10
Add high-risk/no-CAM misalignment using independently assessed account risk, **not** CAM text as the risk-score input. New confirmatory H4/H5 interactions measure moderation of AI investment outcomes, and exploratory H6 studies public Part I.B CAM compliance. Audit eligibility matters: required CAM phased in for large accelerated filers' FYE >= 2019-06-30 and other applicable issuers' FYE >= 2020-12-15. Test only after audit report availability.

Historical PCAOB Part I.A/B inspection exposure is at **audit firm / inspected audit sample** level, not the individual named client. Match PCAOB AuditorSearch Form AP firm IDs as of observation date; missing public inspection is missing, not no deficiencies. Public inspection release date (and separately Part II disclosure date) must predate prediction/event cutoffs. Test selection and denominator sensitivity, varying audit-firm fixed effects, clustering. For full specifications and table plan, see PCAOB_CAM_INTEGRATION.md.

The previous H1–H3 remain unchanged. H4/H5 are theoretical hypotheses until formally frozen and empirically tested. Three-way interactions should NOT be the headline absent feasibility/power checks.
