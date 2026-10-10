# AI CapEx × ICFR × Damodaran | FT50 Research Project

**Stage:** New research project; no empirical results yet.
**Google Drive canonical folder:** https://drive.google.com/drive/folders/1O5fzl-AIMKGzwtfNavzKawBk6FfaFTR9
**GitHub status:** Project-specific development branch in the existing NAAIL umbrella repository; NOT a standalone repository.

## Research question
Does internal-control reporting risk moderate the relationship between AI-related investments, realized free cash flow, and capital-market valuation?

## Research contributions to test
- Damodaran-based valuation: free cash flow to the firm (FCFF), incremental return on invested capital (ROIC), weighted average cost of capital (WACC), and reinvestment intensity.
- ICFR/accounting: material weaknesses, information reliability, and timing-safe latent risk proxies.
- AI measurement: distinguish AI-specific capex from total capital expenditures; combine structured SEC facts with manually validated disclosures.
- Empirical finance: examine future cash-flow realization, market responses, and pricing errors; causal claims require identification beyond fixed effects.
- Neural research: benchmark FinBERT and temporal models (including TimesFM) against transparent econometric and tree-based baselines.

## Hypotheses — proposals, not findings
- H1: The relation between disclosed AI investment and future cash-flow realization varies with prior ICFR risk.
- H2: The market response to AI investment disclosures depends jointly on internal-control risk and the earnings–cash-flow gap.
- H3: As-of-date ICFR risk signals add incremental out-of-time information about future restatements, impairments or valuation surprises.

## Research integrity gates
1. Record source URL, accession number, CIK, filing date, extracted text span, fiscal period, license and ingestion version.
2. Define a reproducible AI investment construct with a manual labeling protocol; SEC standard capex is NOT AI capex.
3. Train only on information that existed by the decision cutoff; chronological testing and purged boundaries.
4. Report missingness, selection, calibration, imbalance metrics (PR-AUC), confidence intervals, and economic payoffs.
5. Compare to Logit / firm+time fixed-effect models / XGBoost before claiming neural superiority.
6. Separate synthetic proof-of-concept data from real empirical samples; do not treat early pilots as FT50 evidence.
7. No automatic publication, data redistribution or claims of statistical significance without independent review.

## Public source starting points
- SEC EDGAR API: https://www.sec.gov/search-filings/edgar-application-programming-interfaces
- SEC Financial Statement Datasets: https://www.sec.gov/dera/data/financial-statement-data-sets.html
- Damodaran sector valuation data: https://pages.stern.nyu.edu/~adamodar/New_Home_Page/data.html
- Ken French factor data: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html
- Google TimesFM source: https://github.com/google-research/timesfm

## Project files
- `PROJECT_MASTER_INDEX.md` — cross-platform links and milestones.
- `research/PRE_ANALYSIS_PLAN.md` — hypotheses, variables, identification, falsification.
- `research/DATA_REGISTER.md` — access/license rules and provenance.
- `src/damodaran_core.py` — auditable valuation calculation helpers.
- `tests/test_damodaran_core.py` — synthetic unit tests only.
- `AGENTS.md` — instructions for Codex in VS Code.

**Privacy:** This branch is in a PUBLIC umbrella repository. Never commit confidential manuscripts, private notes, credentials, licensed raw datasets, or restricted model weights. Keep the master archive in the Google Drive folder above.


## PCAOB inspection and CAM extension (2026-10-10)
The research scope now includes a distinct account-level CAM risk-alignment channel and a **previously-public auditor-firm-level PCAOB inspection exposure** channel. The substantive economic outcomes remain AI investment, free-cash-flow realization, ROIC-WACC and market pricing. Do not infer engagement-specific PCAOB findings from anonymous issuer identifiers.

**Required method documents**: [PCAOB/CAM integration](research/PCAOB_CAM_INTEGRATION.md), [FT50 literature matrix](research/FT50_PCAOB_CAM_LITERATURE.md), [audit oversight prototype](src/audit_oversight.py), and [synthetic unit-test specifications](tests/test_audit_oversight.py).

- **H4 (CAM mismatch):** ex ante high-risk accounts without corresponding CAM disclosures and AI investment economic outcomes.
- **H5 (PCAOB exposure):** publicly known auditor-firm inspection deficiencies condition AI-investment valuation and/or subsequent cash-flow realization.
- **H6 (exploratory):** Part I.B CAM compliance findings and information content of CAM-to-risk alignment.
- **Added Google Drive protocol:** https://docs.google.com/document/d/1N1IhXWiVYsuBxhDaL7fAFir_a3PuFw04ae5fIzgWBHs/edit
- **Free matching data:** PCAOB AuditorSearch / Form AP https://pcaobus.org/resources/auditorsearch ; official inspection datasets https://pcaobus.org/oversight/inspections/firm-inspection-reports.

*Status: research design and unexecuted scaffold only; no PCAOB/CAM sample downloaded or validated.*


## FT50 / AJG 4* revised sample — V2 (2026-10-10)
The October 2026 S&P500-based 424 nonfinancial CIK cohort is an **operational snapshot**, NOT the final 2019–2025 longitudinal sample because of survival/index membership selection.
A reproducible 424-row split is frozen into 119 prioritized technology/infrastructure **candidates**, 244 other potential comparator **candidates**, and 61 utilities/real-estate special cases. These are not verified treated/control groups.
**Primary paper**: issuer's OWN AI-related investment → future cash-flow realization conditional on previously public ICFR, account-risk/CAM alignment, and auditor-firm PCAOB public inspection exposure. Sellers' revenues from buyer AI capex are a separate mechanism; never pool equipment suppliers' own capex with builders' capex as if economically the same.
- [V2 FT50/AJG4* research protocol](sampling/FT50_AJG4_SAMPLE_REDESIGN_V2_2026-10-10.md)
- [119 tech/supply chain screened](sampling/V2_PRIORITY_119_TECH_SUPPLY_CANDIDATES.csv)
- [244 general nonfinancial potential comparators](sampling/V2_COMPARATOR_244_GENERAL_NONFINANCIAL.csv)
- [61 utilities/real estate special](sampling/V2_SPECIAL_61_UTILITIES_REAL_ESTATE.csv)
- [Rebuild V2 stratification](sampling/rebuild_v2_strata.py)
- [Verified native Drive FT50 literature reassessment](https://docs.google.com/document/d/1IdbVQSJL4bq97PqKJGyop64MZ01f1My44CvUVqaKQHc/edit)
No historical 1,500–2,500 issuer universe or new empirical regression is claimed.

## V3 FROZEN FT50 / AJG 4* empirical sample design (10 October 2026)

- Core issuer-owned AI investment / prior-public audit oversight fiscal years: **FY2021–FY2024**; main t+1 actual outcome **FY2022–FY2025**, secondary t+2 outcome **FY2023–FY2025**, baseline history **FY2017–FY2020**. FY2025 investment is supplementary until FY2026 outcomes become actually available.
- Final *eligible population rule*: all U.S. domestic operating nonfinancial 10-K filer-years FY2021–FY2024 including delisted and failed firms, excluding historical finance SIC 6000–6999, with utilities and real estate stratified, CAM eligibility as of FYE, auditor 404(b) applicability and PCAOB first-publication timestamp rules.
- Current **2026 S&P500-based 424-CIK inventory** remains a pilot screen, NOT the final historical cohort. Exactly **119+244+61=424** disjoint nonfinancial firms, 76 financial exclusions, 10 anchors. Original roster contains NO verified historical SEC 10-K eligibility or AI-only CapEx for the additional firms. Final historical numeric company N/firm-year N = **NOT ESTABLISHED**; prior 1,500–2,500 target is an unverified rough feasibility aspiration.
- [V3 protocol with FT50/AJG4* source mapping and exact data waterfall](sampling/SAMPLE_PROTOCOL_LOCKED_V3_2026-10-10.md)
- [Machine-readable V3 dates, limitations and N readiness](sampling/SAMPLE_DECISION_LOCK_V3_2026-10-10.json)
- [Validate first-stage sample counts and partition](sampling/validate_v3_screen.py)
- [Canonical Google Doc — V3 frozen protocol](https://docs.google.com/document/d/14pQ2rreS8Vph7eu0XUAHCfUJ-VUnv7g8U-bxBoqpSW0/edit)

The original V1/V2 files, CAM/ICFR/PCAOB pilot results and TAR manuscript are intentionally preserved. Do not merge the draft PR without research and data-rights review. No empirical paper-wide coefficients or significance are claimed.


## Actual SEC 10-K historical filing-metadata population — observed 10 Oct 2026

**NEW real-run result** (GitHub Actions [successful execution](https://github.com/Saehon/Saeid-Homayoun/actions/runs/38085610261) against a [pinned 2026-09-30 audited SEC submissions mirror](https://github.com/iangow/sec_submissions_data/releases/tag/2026-09-30)). Unlike the prior 424-company S&P500 convenience snapshot, this is 2017–2025 CIK, fiscal-year, original-accession-level source metadata and includes previously delisted issuers present in SEC history.

- FY2021–2024 *original 10-K filing candidates*: **28,483 issuer-years / 8,926 distinct CIK**.
- FY2021–2024 *2026-SIC provisional nonfinancial screen*: **18,336 issuer-years / 5,489 CIK**. By FY: 4,902 / 4,786 / 4,452 / 4,196. **NOT FINAL analytic/treated sample.**
- Other FY2021–2024 records: **9,578** current-financial-SIC and **569** SIC missing, plus **66** separately reviewed 10-KT and **105** company-years with multiple period ends.
- **16,581** nonfinancial-screen FY t company-years / **5,076 CIK** have original FY t+1 10-K (90.43% filing-document coverage, NOT validated CFO).
- **11,533** of **14,140** FY2021–2023 investment years / **4,391 CIK** have FY t+2 10-K (81.56% coverage).
- Balanced FY2021–2024 originals: **3,662** CIK; FY2021–2025 complete: **3,303** CIK; retain unbalanced population as primary to avoid attrition bias.
- Independent QA on the actual exported GitHub Actions artifact (full CSV row counts, original forms, exact CIK–FY uniqueness, source URL and period sequencing, SIC partition totals) **PASS**.
- Original prior 10 pilot companies each occur in all FY2021–2024: 40 original 10-K issuer-years.

**Research-critical boundary:** source companies.parquet SIC is as of the 2026 snapshot, not time-varying historical SIC. Original issuer-year audit eligibility, actual issuer-owned AI-specific CapEx, financial XBRL facts, account-risk/CAM, SOX 404(a)/(b), Form AP and public PCAOB inspection as-of join are NOT YET VERIFIED at scale. The actual causal FT50 panel remains pending. No experiment or p-value was produced from this full historical metadata frame.

**Authoritative artifacts:** [Google Drive original output ZIP](https://drive.google.com/file/d/1r698sPXTeaWEtBWajoantNCfpUk8GNyw/view) and [Drive actual extracted source QA report](https://docs.google.com/document/d/1lf6ewRvcpG4y8bTHMgF7egDvmQI2t19C4ILv2n0NbeQ/edit). The six original results files are also persisted under [actual_sec_historical_2026-09-30](sampling/actual_sec_historical_2026-09-30/), alongside independent [QA JSON](sampling/actual_sec_historical_2026-09-30/SEC_FY2021_2024_INDEPENDENT_QA_2026-10-10.json) and [forward-panel coverage JSON](sampling/actual_sec_historical_2026-09-30/SEC_FY2021_2024_FOLLOWUP_COVERAGE_2026-10-10.json). Reproducible scripts: [extract](sampling/extract_sec_historical_submissions.py) and [t+1/t+2 coverage](sampling/calculate_forward_10k_coverage.py).
