# PCAOB Inspection + CAM extension: multi-level empirical design (draft)

**Integration approved as a research-scoping change, NOT a completed empirical result or causal finding.** The existing AI CapEx / ICFR / Damodaran research question remains primary.

## Economic intuition
AI infrastructure capex may be large, forward-loaded and difficult to capitalize, depreciate and value consistently. Audit committees and external auditors face challenging estimates, software capitalization, PP&E useful-life, impairment, revenue recognition and cash-flow classification questions. CAMs reflect difficult *audit judgments* rather than direct measures of quality. PCAOB public inspection reports reveal selected deficiencies of auditor firms, not necessarily a specific public-company engagement.

**Primary estimand:** Does valuation or cash-flow realization associated with AI investment vary with *ex ante high-risk account omission from disclosed CAMs* and *previously public auditor-level inspection exposure*? Hypothesized mechanisms are information reliability and monitoring constraints, not automatic proof of misstatement.

## Units, keys and temporality
- Issuer firm-year: SEC CIK × fiscal year, with each 10-K filing/accession and filing timestamp.
- CAM: company × audit report × account/risk topic (many CAMs per year). Source: original 10-K audit reports. Preserve CAM text, exact account and original year.
- PCAOB inspection: registered **audit firm** ID × report ID × inspection year × official **publication timestamp**, with Part I.A/I.B finding-topic tables and denominator for selected audits. Use ID matching and dated auditor affiliations; the same audit network name can contain separate firms.
- Link to issuer: at audit-firm/year exposure level by matched auditor ID *only*. Public Part I.A "Issuer A/B" labels are anonymized placeholders; do NOT assert a PCAOB deficiency happened at the named issuer.
- Predictions at decision date d can use only CAMs and PCAOB reports publicly available by d. CAMs in annual audit opinions may follow the investment decision date and cannot be used to predict pre-publication events.
- Part II criticism should be used ONLY if public as of the observation date; never treat private Part II as an observed variable.
- Selection: PCAOB audits selected for inspection are nonrandom. Rates are not universal firm audit-quality scores, nor necessarily comparable across firms or years. Prefer within-firm changes and report/period-level controls; pre-specify comparisons.

## Independent (pre-CAM) risk and CAM mapping
1. Construct account-level risk R(i,a,t) using timestamp-safe financial trends, economic expectations, management estimates, prior ICFR, exposures (PP&E, intangible assets, software costs, goodwill, revenue and contracts); **exclude CAM text and future inspection data from R**.
2. At each company-account-year map whether a CAM addresses topic a with audited NLP dictionary + blinded manual validation (intercoder agreement, precision/recall, confusion matrix). Report CAM applicability and reporting obligations.
3. Pre-register high-risk cutpoint from TRAINING YEARS alone. Create 2×2 cells:
   - High risk + CAM: matched audit attention.
   - High risk + no CAM: potential *underattention signal*; not automatically an audit failure.
   - Low risk + CAM: potentially judgment-intensive area despite low observable risk.
   - Low risk + no CAM: baseline.
4. Weighted high-risk/no-CAM share = CAM_MISMATCH; preserve unexplained, missing, and ineligible states. CAM counting alone is a weak signal; record specificity and changes as exploratory metrics.

## PCAOB measures
- Published lagged Part I.A deficiency share = audits with cited deficiencies / total audits selected, with denominator and selection controls.
- Part I.B CAM compliance issues = distinct count or presence, validated against original report and applicable rules.
- Inspection area mismatch exposure: previously *published*, auditor-level area tags (e.g., capitalization/software and PP&E) weighted by issuer's independently measured area risk. Topic transfer across client audits is a hypothesized **exposure**, not a firm-specific observed problem.
- Missing reports must stay missing (not zero); separate firm-year observations without prior published inspection from firms with no observed findings.
- Include publication-date shocks only in pre-specified event studies; avoid conflating inspection year with public availability.

## Main model (econometric, associational)
Y(i,t+h) = alpha + beta1 AIINV(i,t) + beta2 ICFR(i,t-1)
 + beta3 CAM_MISMATCH(i,t) + beta4 PCAOB_EXPOSURE(auditor(i,t), d<t_event)
 + beta5 AIINV × CAM_MISMATCH
 + beta6 AIINV × PCAOB_EXPOSURE
 + gamma' Controls(i,t) + FirmFE + IndustryYearFE + epsilon(i,t).

Run TWO separately-powered interaction tests (beta5 and beta6) as primary confirmatory analysis. Joint/three-way interaction and mediation are exploratory unless sample size and identification support them. Report coefficients with confidence intervals, multiple-hypothesis adjustments, firm clustering, auditor-cluster sensitivity.

## New hypotheses (in addition to previously drafted H1–H3)
H4 (CAM-risk alignment). The relation between AI investment and subsequent realized cash-flow or market outcomes is weaker when material *independently identified account risk* is not reflected in disclosed CAMs; CAM omissions are interpretative signals, not proven malpractice.
H5 (PCAOB oversight exposure). Previously PUBLIC, auditor-level PCAOB deficiencies are associated with a different AI-investment valuation/cash-flow relation; test the direction, selection and reporting-lag alternatives rather than assuming regulatory causation.
H6 (exploratory). Audit-firm CAM compliance findings in Part I.B may help explain whether the CAM alignment metric is informative about later financial-reporting outcomes.

## Empirical tables and robustness
Table 1 literature/motivation and sample construction by eligibility/date.
Table 2 variable design, coverage, hand-coded CAM/R validation and PCAOB report-lag distribution.
Table 3 2×2 CAM risk matrix, prevalence, transitions, independent risk.
Table 4 core AI CapEx–ICFR–Damodaran baselines.
Table 5 incremental CAM alignment moderation (H4).
Table 6 PCAOB prior exposure moderation (H5; Part I.A vs I.B separately).
Table 7 cash flow, economic profit, CAM topic-level, matched-industry falsification and out-of-time prediction.
Appendix: complete crosswalk, raw-source accession and report IDs, annotation criteria, held-out hand-label tests, code checks and negative controls.

## Feasibility gates before large scrape
- Nontrivial sample of clearly AI-investing firms with defensible AI-specific expenditure data (not total company capex).
- ≥2 report vintages for auditor inspection exposure and sufficient cross-auditor variation after FE.
- Substantial high-risk/no-CAM observations with reliable account topics, no artificial high-risk from CAM text itself.
- Public sample selection visible; uninspected/no-public-report cases are explicitly represented.
- Out-of-time prediction separated from investor reactions after CAM and inspection dates.
- FT50 novelty assessed against Acito et al. (2018), Aobdia and Petacchi (2023), Lennox and Wu (2024), Dee et al. (2026).

## Core sources
https://pcaobus.org/oversight/inspections/firm-inspection-reports
https://pcaobus.org/oversight/inspections/inspection-data-us-global-network-firms
https://pcaobus.org/resources/staff-publications/audit-focus/audit-focus-critical-audit-matters
https://doi.org/10.2308/accr-51811
https://doi.org/10.2308/TAR-2020-0134
https://doi.org/10.2308/TAR-2022-0482
https://doi.org/10.1016/j.jacceco.2025.101834
