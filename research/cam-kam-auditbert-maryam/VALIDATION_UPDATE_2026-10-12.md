# CAM/KAM AuditBERT — 12 October 2026 validation update

**Scope:** Public-safe summary of findings documented in the project's Google Drive `DATA_CHECKS_REPORT.md` and asset inventory (12 October 2026). **Source-provenance correction, same day:** The research owner states that the underlying data were collected from **SEC EDGAR**, and that an **Audit Analytics-like format** was used. This statement supersedes our earlier categorical attribution of these files to Audit Analytics. **The source lineage has not been independently verified at the record level.** No model rerun, regression, or independent raw-data recount was performed for this GitHub update. The authoritative source files remain in Google Drive.

## Latest verified inventory (aggregate statistics)

| File | Matter-level records | Other reported facts |
|---|---:|---|
| `CAM.csv` (owner-reported SEC EDGAR origin; Audit Analytics-like schema) | 45,924 | 262 columns; 6,671 companies; 32,859 audit opinions; 55 CAM topics |
| `KAM.csv` (owner-reported SEC EDGAR origin; source geography requires verification) | 86,122 | 76 columns; 5,520 entities; 35,567 audit opinions; 59 KAM topics |
| `kam (uk)2023.xlsx` (owner-reported SEC EDGAR origin; to be traced) | 28,826 | 75 columns; 28,764 matter keys overlap the larger KAM extract |
| `KAM20240505.csv` (original AuditBERT input) | 65,535 | 76 columns; 4,210 distinct entity IDs; ends partway through an entity's block |

**Unit of analysis:** These are *audit-matter records*, not company-year counts. The source columns include vendor-style identifiers, such as `AUDIT_OPINION_FKEY`; their presence identifies a **schema convention, not evidence of the source provider**. Because European/UK KAMs are included, we must verify the claimed SEC-EDGAR lineage separately for those records (for example, a corresponding EDGAR foreign-private-issuer filing), rather than automatically treat all geographically European records as EDGAR-origin.

## Material validation findings

1. **Historical report year is not available in the CAM/KAM tables as currently validated.** Existing date fields are company snapshots, fiscal year-end, or other metadata, not verified historical audit-report dates. For SEC-origin records, reconstruct filing and opinion dates from source filing URLs, SEC accession numbers, CIKs and auditor report dates, linked to the matter-level records through a **verified mapping**. Do not assume `AUDIT_OPINION_FKEY` is an SEC identifier; if it is only an internal schema key, supply the crosswalk. No dated panel or `t+1` model should be claimed before this join passes.
2. **Original KAM input is truncated.** The notebook source has exactly 65,535 KAM rows, is ordered by entity key and stops partway through an entity. The later comprehensive file has 86,122 records. Not every difference from the later export necessarily represents loss at the original extraction date; changing source coverage and extraction vintage must be distinguished from truncation.
3. **Original trained class count is 49, not 48.** The source notebook applies `topic_counts >= 100`, retaining 49 topics and 65,192 rows from the 65,535-row input (58 original topics). The later full extract has 59 source topics; the same rule retains 49 classes and 85,625 rows. The paper abstract's 48-topic statement must be reconciled.
4. **Panel and reissue duplication.** Some US pre-AI sample rows contain more than one audit opinion per company-year, and their recoded `company_id` does not equal source `COMPANY_FKEY`. Reconstruct persistent issuer IDs, dates and a principled duplicate/reissue selection rule.
5. **Security blocker.** Six distinct Hugging Face access tokens were reported hard-coded in source research notebooks and copied ZIPs. They have **not** been verified revoked or sanitized. Do not publish the implicated notebooks, generated outputs, or ZIPs before rotation, redaction and a new secrets scan.

## Additional materials now catalogued in Google Drive

- `CoFold_AuditBERT_Management_Science_Submission_Package_V5.zip`
- `AuditBERTFold_ThreeStudy_v1_2.zip`
- `KAM-Paper-Code.zip` (restricted: secret-remediation gate)
- `CAMBERT_repo_scaffold_v2_active_learning.zip`
- `CAM_CAR_Empirical_Review_Package_2026-10-12.zip`
- `CAM_CAR_Empirical_Completion_Package_V2_2026-10-12.zip`
- `DATA_CHECKS_REPORT.md`, `ASSET_INVENTORY.csv`, topic counts and truncation-check tables

The previous CAM/CAR review package reported an 11-row measurement exercise and **no regressions**. Newer package filenames are not evidence of completed empirical tests; code and outputs need separate audit.

## Next empirical gates

- **G1 — Reconcile SEC provenance:** establish the actual EDGAR extraction script, CIK/accession numbers, filing URLs, filing dates, auditor report pages, extraction timestamps, jurisdictions and any non-SEC enrichment. Distinguish public SEC content, local processing, and third-party licensed sources; confirm rights case-by-case.
- **G2 — Build dated panel:** derive opinion dates/years via verified EDGAR filing crosswalks (not schema keys alone); resolve reissued opinions and persistent issuer identities; publish attrition and duplication counts.
- **G3 — Reconstruct KAM benchmark:** measure coverage and sample differences by extraction vintage; preregister the >=100 class filter; rerun topic comparison and report uncertainty.
- **G4 — Remediate secrets:** revoke all exposed credentials, sanitize every copy and output, scan again. Never publish source tokens.
- **G5 — Empirical CAM/KAM study:** construct lagged account-risk and macro/earnings-pressure predictors; define risk sets for new, continuing and exited CAM/KAMs; prevent look-ahead; use out-of-time and firm-blocked validation. Estimate tests only on a verified dated panel.
- **G6 — Manuscript consistency:** reconcile 48/49 class labels, 65,192/86,122 records, sample years, model estimands, uncertainty, code execution logs and reproducibility claims.

## Publication boundary

This repository is the public methods/reproducibility layer. **SEC EDGAR public filing data can be considered for a traceable public replication subset** after checking the individual filing provenance, third-party enrichments, redistribution rights, personal information and embedded secrets. Do **not** commit unverified data extracts, unpublished manuscripts, personal/company contacts, credentials, or restricted archives. This file contains only aggregate diagnostics and methodological action items. No experimental PASS or statistical significance is claimed.
