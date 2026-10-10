# Project Master Index

Created: 2026-10-10 | Status: research protocol and infrastructure only; no merged sample or confirmed empirical findings.

## Verified project links
- Canonical Google Drive project: https://drive.google.com/drive/folders/1O5fzl-AIMKGzwtfNavzKawBk6FfaFTR9
- Master Google Doc: https://docs.google.com/document/d/1roGioFNb-Zlv9xtCUDF1UlSb_-5ohmDRVIHVgSsc8Ss/edit
- Development branch: https://github.com/Saehon/Saeid-Homayoun/tree/research/ai-capex-icfr-damodaran-ft50-20261010
- Kaggle: not created.
- Hugging Face: not created.

## Research objective
Test whether point-in-time internal-control information risk modifies the relation between AI-specific capital investment, future FCFF realization, and capital-market valuations.

## Governance
Google Drive stores the authoritative research archive, source documents, versioned manuscripts, and restricted data. GitHub contains public-ready research design and reproducible code, not confidential drafts or restricted datasets.

## Folder mapping
Google Drive 00_Project_Master_Index: this project index and decisions.
01_Literature_and_FT50: reviewed papers, metadata, literature matrix.
02_Data_Raw_Restricted: licensed data, download manifests, checksums.
03_Data_Processed: versioned research-ready samples and dictionaries.
04_Code_and_Methods: reproducible scripts and experimental protocols.
05_Results_and_Validation: robustness, falsification, figures and audit trails.
06_Manuscript_and_Submission: article draft, cover letters, reviewer replies.
07_Replication_and_Versions: frozen releases and independent rerun reports.

## Current milestone
M0: Confirm pipeline governance and check data availability, empirical novelty, and sample coverage before investing in large-scale data scraping.


## PCAOB & CAM extension — 2026-10-10
**Added research pillars:** (1) account-level, independent risk-to-CAM alignment; (2) previously-public PCAOB Part I.A inspection risk and Part I.B CAM compliance at registered audit-firm level; (3) issuer-to-auditor linking through Form AP/AuditorSearch; (4) conditional AI investment / Damodaran FCFF and valuation outcomes.

**New canonical Google Drive extension protocol:** https://docs.google.com/document/d/1N1IhXWiVYsuBxhDaL7fAFir_a3PuFw04ae5fIzgWBHs/edit

**GitHub design files:** research/PCAOB_CAM_INTEGRATION.md ; research/FT50_PCAOB_CAM_LITERATURE.md ; src/audit_oversight.py ; tests/test_audit_oversight.py.

**FT50 novelty gate:** Dee et al. (JAE 2026) already studies CAM and ICFR; Acito et al. (TAR 2018) already studies exposure to PCAOB findings. Primary novel question is conditional *economic valuation of AI investment*, not CAM/ICFR or PCAOB alone.

**Research status:** extension documents and initial deterministic code scaffold stored; no new empirical data/results/peer-reviewed findings created; Draft PR #163 remains open for review.


## Revised FT50-AJG4* sample — 2026-10-10
Published methodological comparison against Babina et al. JFE 2024, Biddle et al. JAE 2009, Doyle et al. TAR 2007, Ashbaugh-Skaife et al. JAR 2009, Burke et al. TAR 2023, Dee et al. JAE 2026, Acito et al. TAR 2018, and Law/Shen Management Science 2025 supports separating buyer capital expenditure from supplier-demand spillovers, CAM topical alignment, prior-public PCAOB risk and future capital realization.
The original 424-issuer 2026-index screen is preserved with derived V2 partitions 119/244/61 and explicit UNKNOWN actual AI status. It does not replace the planned historical SEC 10-K universe with delisted firms.
Canonical FT50 sampling memo: https://docs.google.com/document/d/1IdbVQSJL4bq97PqKJGyop64MZ01f1My44CvUVqaKQHc/edit
Native TAR manuscript Appendix E and native Drive master index both updated. Source code and CSVs in sampling/; draft PR #163 still open.

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
