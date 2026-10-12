# CAM/KAM AuditBERT — 12 October 2026 validation update

**Source correction (research owner, 12 October 2026):** The CAM/KAM observations were extracted from **companies' annual reports**. SEC EDGAR was identified as a source for filings where applicable; the data's resemblance to an Audit Analytics export concerns **format only**, not its origin or license. The research owner has confirmed the source and **does not require a separate provenance-retesting project**. The earlier claim that the datasets were supplied by Audit Analytics is withdrawn. This note does not imply that new source-level tests were performed.

**Analysis status:** Summary of file-level checks in Google Drive's `DATA_CHECKS_REPORT.md`; no new model execution or regression was performed in this GitHub documentation update.

## Latest data inventory

| File | Audit-matter rows | File characteristics recorded in Drive checks |
|---|---:|---|
| `CAM.csv` | 45,924 | 262 columns; 6,671 companies; 32,859 audit opinions; 55 CAM topic labels |
| `KAM.csv` | 86,122 | 76 columns; 5,520 entities; 35,567 audit opinions; 59 KAM topic labels |
| `kam (uk)2023.xlsx` | 28,826 | 75 columns; 28,764 matter keys also in larger KAM extract |
| `KAM20240505.csv` (original notebook input) | 65,535 | 76 columns; 4,210 entity identifiers; export ends partway through an entity |

These counts describe **audit-matter records, not distinct company-years**. Vendor-like field names such as `AUDIT_OPINION_FKEY` are identifiers in the existing file format; their appearance alone should not be used to attribute a data supplier.

## Methodological results from the existing checks

1. **The required historical report-year variable is missing from the inspected CAM/KAM tables.** A valid longitudinal study must obtain reporting/auditor report years from the source annual reports or an existing verified project crosswalk; this is a **research-variable construction task**, not a new test of who supplied the data.
2. **The original KAM notebook input is truncated.** It contains 65,535 observations, while the larger extract contains 86,122; differences also depend on extraction vintage and coverage.
3. **Topic-class discrepancy:** original notebook filter `topic_counts >= 100` retains **49 classes** and **65,192 rows**. The abstract says **48 topics**; manuscript and code must be reconciled. The same rule retains **49 classes** and **85,625 rows** in the larger extract.
4. **Repeated company-years/reissued reports:** distinguish audit opinions, matters and unique company-year observations before estimation. Confirm stable issuer IDs and duplicate-handling rules.
5. **Security:** previous inventory identified **six distinct Hugging Face access tokens** in source notebooks. Revoke them, remove them from notebooks/outputs, and re-scan before publishing or mirroring code. Their revocation has not yet been verified.

## Project materials retained in Google Drive

- `CoFold_AuditBERT_Management_Science_Submission_Package_V5.zip`
- `AuditBERTFold_ThreeStudy_v1_2.zip`
- `KAM-Paper-Code.zip` (contains notebooks requiring token cleanup)
- `CAMBERT_repo_scaffold_v2_active_learning.zip`
- `CAM_CAR_Empirical_Review_Package_2026-10-12.zip`
- `CAM_CAR_Empirical_Completion_Package_V2_2026-10-12.zip`
- `DATA_CHECKS_REPORT.md`, `ASSET_INVENTORY.csv`, topic counts and truncation checks

The previously inspected CAM/CAR review package documented an 11-row measurement exercise, **not completed regressions**. Do not infer that a later ZIP filename demonstrates completed statistical tests.

## Immediate empirical research plan

- **E1 — Use the owner's source statement:** Companies' annual reports are the underlying documents; preserve existing files and source notes. **No separate source-origin audit is requested.**
- **E2 — Construct time-indexed panels:** recover report year and auditor report date where required, select stable issuer identifiers, manage amended/reissued reports and multiple CAM/KAMs per opinion; report sample attrition.
- **E3 — Correct the KAM sample:** explain the 65,535-row truncation, rerun the 49-class procedure with the full 86,122-row input, and reconcile any changes in topic distribution and outcomes.
- **E4 — Prepare empirical tests:** build account-level CAM/KAM risk sets, lag earnings pressure and macroeconomic variables, estimate pre-specified `t` to `t+1` associations, and conduct robustness and falsification tests.
- **E5 — Reproducibility and security:** align abstract, data, tables and code; document commands, dependencies and inference; revoke and sanitize exposed Hugging Face tokens.

## Public project boundary

Google Drive retains the full project files. GitHub hosts the research methods, code, summaries and suitably shareable reproducibility materials. Do not upload active credentials or unpublished manuscripts without authorization. Publication of complete third-party annual-report text or enriched bulk extracts is a separate release decision; nothing in this source correction approves or prohibits such release automatically.

**This document corrects attribution and records existing findings; it does not claim a completed empirical analysis or an independent source-origin verification.**
