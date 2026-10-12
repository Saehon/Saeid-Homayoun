# CAM/KAM AuditBERT — 12 October 2026 validation update

**Scope:** Public-safe summary of findings documented in the project's Google Drive `DATA_CHECKS_REPORT.md` and asset inventory (12 October 2026). No model rerun, regression, or independent raw-data recount was performed for this GitHub update. The authoritative source files remain in restricted Google Drive storage.

## Latest verified inventory (aggregate statistics)

| File | Matter-level records | Other reported facts |
|---|---:|---|
| `CAM.csv` (licensed US Audit Analytics) | 45,924 | 262 columns; 6,671 companies; 32,859 audit opinions; 55 CAM topics |
| `KAM.csv` (licensed European Audit Analytics) | 86,122 | 76 columns; 5,520 entities; 35,567 audit opinions; 59 KAM topics |
| `kam (uk)2023.xlsx` (licensed) | 28,826 | 75 columns; 28,764 matter keys overlap the larger KAM extract |
| `KAM20240505.csv` (original AuditBERT input) | 65,535 | 76 columns; 4,210 distinct entity IDs; ends partway through an entity's block |

**Unit of analysis:** These are *audit-matter records*, not company-year counts.

## Material validation findings

1. **Historical report year is not available in the CAM/KAM raw tables.** The existing date fields are company snapshots, fiscal year-end, or other metadata, not verified historical audit-report dates. A separate Audit Analytics audit-opinion table must be joined on `AUDIT_OPINION_FKEY` before constructing CAM/KAM dynamics, panel fixed effects, or `t+1` outcomes.
2. **Original KAM input is truncated.** The notebook source has exactly 65,535 KAM rows, is ordered by entity key and stops partway through an entity. The later comprehensive file has 86,122 records. Not every difference from the later export necessarily represents loss at the original extraction date; changing vendor coverage/time must be distinguished from truncation.
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

- **G1 — Restricted provenance:** establish extract date, Audit Analytics module, redistribution rights, data dictionary and key coverage.
- **G2 — Build dated panel:** join opinion dates/years; resolve reissued opinions and persistent issuer identities; publish attrition and duplication counts.
- **G3 — Reconstruct KAM benchmark:** measure coverage and sample differences by extraction vintage; preregister the >=100 class filter; rerun topic comparison and report uncertainty.
- **G4 — Remediate secrets:** revoke all exposed credentials, sanitize every copy and output, scan again. Never publish source tokens.
- **G5 — Empirical CAM/KAM study:** construct lagged account-risk and macro/earnings-pressure predictors; define risk sets for new, continuing and exited CAM/KAMs; prevent look-ahead; use out-of-time and firm-blocked validation. Estimate tests only on a verified dated panel.
- **G6 — Manuscript consistency:** reconcile 48/49 class labels, 65,192/86,122 records, sample years, model estimands, uncertainty, code execution logs and reproducibility claims.

## Publication boundary

This repository is the public methods/reproducibility layer. Do **not** commit Audit Analytics row data, unpublished manuscripts, private Drive identifiers, personal/company contacts, credentials, or restricted archives. This file contains only aggregate diagnostics and methodological action items. No experimental PASS or statistical significance is claimed.
