# V2 FT50/AJG4* sample redesign: The Value of Audit Oversight in AI Capital Investment

Date: 2026-10-10
Target: The Accounting Review (FT50; AJG 2024 4*). Research design, not completed 2019–2025 SEC historical dataset.
Legacy V1 424-company 2026 S&P500 sample remains intact. V2 stratification is screening, NOT a causal sample.

## A. Article-title alignment and estimands
Primary accounting/auditing question: Do previously disclosed internal-control and external audit oversight signals condition the ex post CASH FLOW REALIZATION of issuer-owned AI-related capital investment? Accounts at risk include PP&E, software capitalization, intangible assets, impairment and purchase commitments.
- Buyer/builders/adopters: analyze own AI-related capital commitments/investment and future operating cash flows. Specify company investments separate from procurement, R&D, leases, operating AI costs, and projections.
- Suppliers of AI equipment (NVIDIA and similar): their own CapEx cannot proxy for their CUSTOMERS' AI CapEx. Suppliers are analyzed separately through AI-linked sales/gross margins/operating cash flows and demand exposure, not pooled with builders as one investment construct.
- Broad adopters and controls: code actual AI activity from verified disclosed terms and direct investment; non-mention is not proof of non-adoption.
- Treat PCAOB audit-firm inspection exposure and CAM-account risk alignment as separate oversight channels; no issuer-level PCAOB finding attribution and no mechanical CAM=0 deficiency inference.

## B. Literature audit with direct verified publications
1. Babina, Fedyk, He, Hodson (2024), JFE, https://doi.org/10.1016/j.jfineco.2023.103745 : company AI input measure is AI-skilled workers based on proprietary Cognism resumes; company-wide PP&E CapEx is NOT a comparable AI measure. Mendeley V3 uses pseudo-data for proprietary inputs (https://data.mendeley.com/datasets/s26kxvspn7).
2. Biddle, Hilary, Verdi (2009), JAE, https://doi.org/10.1016/j.jacceco.2009.09.001 : reporting quality and investment efficiency; sample excludes financial firms; separate over- vs under-investment and capital from noncapital spending. Do not claim FCFF=OCF−gross CapEx proves investment failure.
3. Doyle, Ge, McVay (2007), TAR, https://doi.org/10.2308/accr.2007.82.5.1141 : account/entity control weakness, accrual quality and cash realizations. Avoid selected megacap-only sample with no material weaknesses.
4. Ashbaugh-Skaife, Collins, Kinney, LaFond (2009), JAR, https://doi.org/10.1111/j.1475-679X.2008.00315.x : cost of equity and control deficiencies, distinguish auditor-confirmed 404b opinion from management 404a/302 disclosure, separate risk valuation channels.
5. Burke, Hoitash, Hoitash, Xiao (2023), TAR, https://doi.org/10.2308/TAR-2021-0013 : actual and expected CAM topics; CAM presence counts alone do not demonstrate capital-market news; need CAM surprise and account risk.
6. Dee, Luo, Wang, Zhang (2026), JAE, https://doi.org/10.1016/j.jacceco.2025.101834 : CAM reporting and ICFR quality is ALREADY examined, especially account-level weaknesses; do NOT present their link as novel.
7. Acito, Hogan, Mergenthaler (2018), TAR, https://doi.org/10.2308/accr-51811 : client exposure via published auditor deficiency areas, not a specific inspected client's deficiency; use report release date and account risk.
8. Law and Shen (2025 journal issue; 2024 online), Management Science, https://doi.org/10.1287/mnsc.2022.04040 : auditor-office AI adoption may affect opinions; do NOT confuse AI investment BY THE AUDITOR with AI investment BY THE AUDIT CLIENT.
AJG 2024 ranks TAR, JAE and JAR 4*; AJG 4* is distinct from 4. Data rights and journal fit must be verified separately.

## C. Ordered, nested research populations
Frame F0 (NOT ASSEMBLED): all U.S. 10-K filing issuer-years, 2017–2025, by historical SEC acceptance timestamp, CIK, annual form, SIC, country, audit firm and filing status. 2017–2020 used to build baseline controls, prior ICFR and trend history. Includes subsequently delisted/failing issuers; do not use 2026 index membership to select 2019 outcomes.
Frame F1 (NOT ASSEMBLED): operating nonfinancial 10-K issuer-years after documented historical filters, no issuer excluded solely for lacking AI text or CAM. Financial industry SIC 6000–6999 generally removed for FCFF comparability; public utilities and REITs separate with explicitly differentiated capital/rate economics. Historical SIC used in preference to current GICS for primary eligibility.
Frame F2 (NOT ASSEMBLED): 2021–2025 CAM-eligible issuer-years per PCAOB AS3101 and actual fiscal-year-end/filer status, excluding CAM-exempt cases such as EGC, applicable investment companies, broker/dealers and employee benefit plans. CAM=0 can be a valid disclosed outcome for eligible issuers, NOT presumed missing or misconduct. Large accelerated filers CAM effective FY ending >=2019-06-30, others applicable >=2020-12-15; 2019–2020 for rollout/pretrend analysis, 2021–2025 as common primary CAM regime.
Frame F3 (NOT ASSEMBLED): F2 with verifiable, timestamp-safe firm-specific AI investment proxy (A direct audited dollar line; B evidenced mixed-purpose data-centre capex band; C validated AI physical/digital investment narrative; D generic AI mention only). Do not define the entire F3 solely from named early "winners"; preserve comparable noninvestors/nonreporters with explicit unknown label.
Frame F4 (NOT ASSEMBLED): F3 plus Form AP/PCAOB registered auditor match, published inspection available BEFORE the analysis cut-off date, and independent account-level risk/CAM topic map. This sample is the NESTED oversight-complete panel, not necessarily most representative; compare F1/F2/F3/F4 selection and missingness.
Primary predictive realization tests: investments with horizon +1 observed in fiscal years 2021–2024 (outcomes through 2025), +2 in 2021–2023 (outcomes through 2025); extend only after filed data and timestamp verification. Use 2025 for contemporary CAM/PCAOB/descriptive and investment event returns, NOT unknown future 2026 realized CFO outcomes as of 2026-10-10.
Provisional scale: seek >= 1,500–2,500 unique F1 issuers (NOT achieved, not quota-driven) or all accessible eligible firms; event and oversight subsets likely smaller with unknown N. Pre-extraction power simulation must determine necessary variation in high-risk/CAM mismatch and distinct registered auditor firms. It is invalid to promise any particular N until actual screening.

## D. What has ACTUALLY been done
A frozen 2026-10-09, snapshot source S&P 500 contains 503 share class rows = 500 unique SEC CIK. Excluded 76 financial CIK; retained 424 distinct nonfinancial CIK. Internal partitions:
119 technology / possible supply-chain candidates: 5 previous builders; 5 previous suppliers; 65 subindustry supply-chain candidate records; 44 broad technology/adoption candidates. These ARE NOT 119 verified AI-investing issuers and should not be pooled as a treatment.
244 other nonfinancial possible comparisons: all unverified AI activity, NOT confirmed AI-free controls.
61 utilities/real-estate special-case cohort (31, 30), separate for energy and infrastructure pathways.
Total 119+244+61=424 unique CIK. All three CSVs derived from the original 424 CSV using labels; no additional primary SEC filings were downloaded or validated at this stage.
2026 S&P index membership imposes survivorship bias. Use these cohorts only for reproducible ingestion/pilot priorities; they are NOT the F0–F4 actual research sample. Do not treat provisional labels as exposure or control assignments.
Keep all older datasets and filenames as history.

## E. Data sources and exact temporal controls
SEC filings, submissions, financial company facts: https://www.sec.gov/search-filings/edgar-application-programming-interfaces
PCAOB CAM standards and exemptions: https://pcaobus.org/oversight/standards/auditing-standards/details/AS3101
PCAOB phased CAM implementation: https://pcaobus.org/oversight/standards/implementation-resources-PCAOB-standards-rules/auditor-reporting
PCAOB Form AP match: https://pcaobus.org/resources/auditorsearch
PCAOB firm inspection data: https://pcaobus.org/oversight/inspections/firm-inspection-reports
Nonrandom inspection caution: https://pcaobus.org/oversight/inspections/inspection-data-us-global-network-firms
Damodaran industry data: https://pages.stern.nyu.edu/~adamodar/New_Home_Page/data.html
Fama French: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html
Stage A: construct issuer-year with original 10-K and acceptance datetime. Stage B: assess CAM/ICFR text with same filing date and individual account. Stage C: link audit firm registered ID and PCAOB public dates; missing public reports MUST remain missing and should not be treated as 0 deficiencies. Stage D: link previously publicly disclosed AI investments to later CFO, reinvestment and FCFF, calculate consistent invested capital and WACC. Strong date constraints apply for event-window returns and neural model training.

## F. Identification, inference and sample QA gates
- Never select cases based on significance, positive returns, or presence of a material weakness; if manually oversampling MW cases for annotation, maintain separate validation strata, known sampling probabilities and weighted comparisons.
- Compare balanced roles WITHIN industries and firm size, not AI builders versus chip suppliers with wildly different business models as though randomly treated.
- PCAOB multilevel clusters = audit firms: 10 firms with 3 auditors is not powered for oversight effects; require adequate firms and checks for cross-auditor network/time variation. Do not force a numerical minimum without power assessment.
- Prespecify two core audit oversight moderation tests (AI investment × prior ICFR information risk; AI investment × prior PCAOB exposure) and account-risk/CAM alignment separately. Avoid arbitrary 3-way interactions in small samples.
- Correct nonrandom public disclosure, missing source versions, survivorship, fiscal-year-end mismatches, management vs auditor control opinion, earnings news/confounding and spillovers.
- Case-study builder/supplier contrast is illustrative only; no claim of causal profit or mispricing from OCF−total CapEx.
- Audit firm inspection deficiencies among selected audits do not identify audited clients or all audit quality; do not conflate Part I.A and Part I.B.
- No valid results before event linkage, coverage report, power/variation checks, negative controls and pre-analysis protocol lock.

## G. Go/no-go, manifest and preserved links
Existing 10-firm audit pilot: https://docs.google.com/document/d/1_nSJJPcjKhtDv_THEekcp6CHWZrgDRbACCsUkjiN7Yg/edit
Frozen current-index screening: https://docs.google.com/document/d/1QQNxWZNyV5GhgpruMZ36Abhxxbx_rkuxICS_vp1T9F0/edit
Google Drive canonical root: https://drive.google.com/drive/folders/1O5fzl-AIMKGzwtfNavzKawBk6FfaFTR9
GitHub draft PR: https://github.com/Saehon/Saeid-Homayoun/pull/163
Outputs must be maintained with time-stamped source URLs, accession IDs, CIK mappings, 10-K fiscal years and explicit AI classification confidence flags. Missing F2/F3/F4 data are reported; not imputed as absence of investment/oversight.
