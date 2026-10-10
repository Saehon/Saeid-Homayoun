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
