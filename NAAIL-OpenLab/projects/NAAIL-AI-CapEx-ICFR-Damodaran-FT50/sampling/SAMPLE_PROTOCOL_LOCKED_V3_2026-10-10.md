# LOCKED V3 — FT50 / AJG 4* final sampling and analysis windows

**Research article:** *The Value of Audit Oversight in AI Capital Investment: Internal Controls, Critical Audit Matters, PCAOB Inspections, and Cash-Flow Realization.*  
**Journal target:** *The Accounting Review* (FT50; AJG 2024 4*).  
**Protocol freeze date:** 2026-10-10.  
**Status:** SAMPLING RULES AND ANALYTICAL YEARS FINALIZED. Final historical SEC numeric sample size is **NOT YET VERIFIED**; the existing index sample counts are explicitly distinguished from an empirical SEC panel.

## 1. Final fixed years

| Cohort purpose | Years and rules |
|---|---|
| Historical controls, lagged financial reporting/ICFR and placebo periods | Firm FY2017–FY2020 |
| **Main investment and oversight exposure years** | **FY2021–FY2024** |
| **Primary future one-year outcomes** | **FY2022–FY2025** (AI investment FY t to outcomes FY t+1) |
| Two-year follow-up robustness | Exposures FY2021–FY2023; outcomes FY2023–FY2025 |
| FY2025 exposure and investment | Descriptive and disclosure-event tests only; no manufactured FY2026 outcomes |
| CAM first implementation | 2019/2020 validation of legal filer-class rollout, not incorrectly pooled main period |
| PCAOB inspection information | Most recent **publicly released** report strictly before the investor/event as-of cutoff |

The fiscal-year label is the **issuer's actual fiscal year**, not a calendar year. Prior-year CAM and ICFR text only qualifies as ex ante information after the auditor opinion and SEC filing become public. A PCAOB inspection **year is not its publication date**, and subsequent releases must never be backfilled into prior investor information. Historical reports published before the October 2026 analysis may be retrospectively retrieved, but their historical public availability must be preserved.

## 2. Final population eligibility (rule-based; not quota-driven)

**Primary sample definition:** All historically reporting U.S. domestic **10-K issuer–fiscal-years FY2021–FY2024** with auditable consolidated annual operating data, including firms subsequently delisted, acquired, bankrupt, or removed from indexes. Deduplicate by 10-digit SEC CIK, fiscal year and original 10-K accession while recording amendments, restatements, name changes, shell conversions and reporting successor transitions. No October 2026 S&P500 membership requirement.

**Primary industrial valuation population:** Exclude issuer–years with contemporaneous financial/banking/insurance SIC 6000–6999, funds/trusts and true shell/blank-check vehicles where industrial FCFF is not comparable; keep an auditable count at each waterfall stage. **Utilities and REITs** require separately identified research strata and tailored valuation controls; do not silently erase them. U.S. domestic 10-K status cannot be inferred from an index membership file.

**Subsamples — separately reported, not one over-restricted panel:**
1. Baseline nonfinancial issuer-years with reported XBRL financial statements and dated available operating cash flow, earnings and capex.
2. AI information: A=directly measured issuer-owned AI capital spend, B=bounded mixed-purpose data-centre/AI capex, C=evidenced but unquantified operational/investment activity, D=generic AI statement, E=no AI mention, U=uncertain. Only A qualifies as a directly measured AI-dollar level; B and C used in explicitly labeled analyses. Nonmention does not mean zero AI adoption.
3. CAM-eligible FY2021–FY2024 under PCAOB AS 3101 (large accelerated FYE >= 2019-06-30; other covered issuers FYE >= 2020-12-15; exempt emerging growth companies, designated investment companies, brokers/dealers and employee benefit plans). An eligible no-CAM report can legitimately disclose no critical matters.
4. ICFR: distinguish management Section 404(a)/302 disclosures from auditor Section 404(b) attestation, which is not universally required. Code weaknesses and separate latent ex ante score independently of CAM.
5. PCAOB: registered audit-firm entity via original auditor name / Form AP, official inspection Part I.A and Part I.B, exact first PUBLIC release date. No report must remain MISSING, not zero findings; selected audits are nonrandom and not necessarily the named issuer's audit.
6. Market-information event study: only investments with first verifiable public-event timestamp, prior-public auditing features and valid security returns.

**Two distinct economic channels:** The primary equation examines the issuer's **own AI investment**, not the company-wide gross purchase of PP&E automatically. AI semiconductor/equipment suppliers are evaluated separately using AI-exposed sales/cash conversion; supplier earnings from buyers' capital expenditure are not supplier's own AI CapEx. This distinction is mandatory to avoid economically invalid pooling under the Damodaran builder–supplier interpretation.

**Main outcomes:** future operating cash flow conversion and future EBIT-to-cash realization, correctly calculated enterprise FCFF, economic profit/ROIC–WACC where valid, impairments, and separate market-event responses. Current cash flow minus current CapEx is mechanically affected by investment and cannot prove project value destruction. Historical sector/company-year FEs and carefully dated controls must be chosen without absorbing all variation; multilevel auditor-firm clustering and power/variation diagnostics are mandatory before PCAOB interaction inferences.

## 3. Verified arithmetic: what has actually been selected

The source for the first-stage **current-index SCREEN** was a versioned open S&P500 constituent snapshot dated **2026-10-09** at commit **36472b57910842f4025e8ca8303b93a692d2bbae** (not itself a historical SEC filing universe):

| Observed first-stage quantity | VERIFIED count |
|---|---:|
| Securities/share-class rows | 503 |
| Unique issuer SEC CIK values in roster | 500 |
| GICS Financials excluded from industrial panel screen | 76 |
| Remaining nonfinancial unique CIKs | **424** |
| Technology/infrastructure/supplier screening candidates | **119** |
| General nonfinancial potential comparators | **244** |
| Utilities/Real Estate separately analyzed | **61** (=31 Utilities +30 Real Estate) |
| Original manually reviewed case-company anchors preserved | 10 |
| Duplicate overlap among 119/244/61 | **0** |
| Original 424 rows marked historical 10-K and AI CapEx as NOT VERIFIED | **424** |
| Completed full historical 2021–2024 SEC sample | **NOT EXTRACTED** |
| Verified final sample N of firms and firm-years | **UNAVAILABLE** |

The partition was independently checked directly against the five versioned GitHub CSV files: 424/76/119/244/61 rows, 424 distinct CIKs in the selected set, 424 in the union, no dropped/extra/overlapping CIKs and 10 preserved anchor entities. The source has 2026 S&P500 index survivor selection, and **these 424 ARE NOT the final FT50 empirical cohort**. The earlier "1,500–2,500 companies" is an unvalidated sizing aspiration, NOT the actual selected sample or a statistical quota.

## 4. Required exact extraction waterfall for final empirical N

Report BOTH distinct issuer CIK and issuer-year observations in every cell, with FY2021–FY2024 columns, audit firm counts, and missingness:

- **W0** All domestic SEC 10-K annual issuer-year entries (original 10-K, 10-K/A version graph; former and delisted firms included).
- **W1** Audited nonfinancial operating issuer-years, historical SIC 6000–6999 exclusions recorded separately; 10-K year-end verified.
- **W2** Available XBRL operating/asset/cash-flow facts with source accession/time. Track missing, do NOT drop before QA by default.
- **W3** Complete AI evidence categories A/B/C/D/E/U and double-coder validation, with investment ownership and amount/unit/cash vs commitment distinction.
- **W4** Distinct CAM reporting applicability, topic/account mapping and independent account-level risk.
- **W5** Management ICFR weaknesses and separately auditor-attested ICFR where legally applicable.
- **W6** Public PCAOB registered auditor firm/exposure as-of each model/investment information event.
- **W7** Available forward t+1 and t+2 outcome years, report date, appropriate fixed effects/power and sample attrition.

Do not impose W4–W6 on all main baseline equations (would select toward large audit firms, non-EGC cases and firms with prior inspection releases). Always compare the baseline, CAM, ICFR and PCAOB nested samples and their marginal inclusion probabilities. Differences from earlier protocols are protocol amendments made BEFORE future regressions and not chosen based on p-values. 

## 5. FT50/AJG 4* scholarly evidence and novelty filters

- Babina, Fedyk, He & Hodson (2024), *Journal of Financial Economics*, AI hiring/resume investment measure, DOI: https://doi.org/10.1016/j.jfineco.2023.103745 . Their private resume inputs and corporate AI investment proxy are not mechanically reproducible from free XBRL total CapEx.
- Biddle, Hilary & Verdi (2009), *Journal of Accounting and Economics*, financial reporting quality and investment efficiency, DOI: https://doi.org/10.1016/j.jacceco.2009.09.001 . Distinguish capital intensity from ex post investment efficiency.
- Doyle, Ge & McVay (2007), *The Accounting Review*, ICFR and accrual quality, DOI: https://doi.org/10.2308/accr.2007.82.5.1141 . Historical weakness variation is essential to identify its role.
- Ashbaugh-Skaife, Collins, Kinney & LaFond (2009), *Journal of Accounting Research*, controls and cost of equity, DOI: https://doi.org/10.1111/j.1475-679X.2008.00315.x . Control quality influences information-risk valuation separately from operating cash flows.
- Burke, Hoitash, Hoitash & Xiao (2023), *The Accounting Review*, CAM information/disclosure, DOI: https://doi.org/10.2308/TAR-2021-0013 . CAM counts alone cannot establish risk-to-topic alignment or surprising information.
- Dee, Luo, Wang & Zhang (2026), *Journal of Accounting and Economics*, CAM reporting and ICFR improvements, DOI: https://doi.org/10.1016/j.jacceco.2025.101834 . A generic CAM–ICFR association is **NOT novel**.
- Acito, Hogan & Mergenthaler (2018), *The Accounting Review*, auditor inspection deficiency-area exposure and client outcomes, DOI: https://doi.org/10.2308/accr-51811 . PCAOB area-linked client exposure is not itself new; the conditional AI-investment cash realization channel is proposed.
- Law & Shen (2025 print/2024 online), *Management Science*, **AI adoption BY AUDITORS**, DOI: https://doi.org/10.1287/mnsc.2022.04040 . Separate client AI investment from auditor-office AI deployment.

The AJG 2024 category is **4*** for TAR, JAE and JAR, whereas other FT50 accounting journals such as *Contemporary Accounting Research* and *Review of Accounting Studies* carry AJG 4. FT50 is an independent list, not equivalent to AJG4*.

## 6. Regulator and public data evidence

- Official SEC API: https://www.sec.gov/search-filings/edgar-application-programming-interfaces (submissions and companyfacts; nightly bulk archives; 10-digit CIK, acceptance/timestamps).
- SEC Financial Statement Data Sets: https://www.sec.gov/dera/data/financial-statement-data-sets.html .
- Official PCAOB AS 3101: https://pcaobus.org/oversight/standards/auditing-standards/details/AS3101 .
- Official CAM implementation: https://pcaobus.org/news-events/news-releases/fact-sheet-auditors-report-standard-adoption-6-1-17 .
- PCAOB public inspection machine data 2018+ annual, 2019+ triennial: https://pcaobus.org/news-events/news-releases/news-release-detail/pcaob-makes-available-new-downloadable-datasets-featuring-pcaob-inspection-findings-from-audit-firm-inspection-reports .
- PCAOB firms: https://pcaobus.org/oversight/inspections/firm-inspection-reports .
- AuditorSearch/Form AP: https://pcaobus.org/resources/auditorsearch .
- Archived Damodaran WACC: https://pages.stern.nyu.edu/~adamodar/New_Home_Page/data.html .

## 7. Status and go/no-go

**GO** for frozen full-universe SEC 10-K data extraction, 2021–2024 core periods, and blinded construct labeling. **NO-GO** for asserting any full-universe final N or running the TAR confirmatory PCAOB–CAM–ICFR interaction model with current data; no complete historical filings list/AI capex table exists in this project at this freeze. V1/V2 artifacts must not be destroyed or overwritten. Any future sample exclusion needs dated rationale before outcome estimation. This document locks design, not a false appearance of finished data work.
