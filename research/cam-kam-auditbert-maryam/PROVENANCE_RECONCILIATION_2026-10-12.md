# SEC EDGAR provenance reconciliation — CAM/KAM AuditBERT
**Date:** 12 October 2026  
**Project:** CAM/KAM AuditBERT  
**Status:** Owner-reported origin; **record-level provenance not yet independently verified**.

## Correction log
The research owner reports that the source data were obtained from **SEC EDGAR**, **not** from Audit Analytics, and that the datasets were structured using an **Audit Analytics-like format**. Earlier project documentation described the files as licensed Audit Analytics datasets; that description should **not** be treated as established provenance. The actual source of each observation must be established from the original extraction process or filing documents rather than schema appearance.

The source-inventory report remains valid as a summary of file structures and measured counts, subject to its original checks. **Counts, schema fields, ownership and provenance are distinct facts**: no sample-size inference can establish legal licensing or exact extraction origin.

## Record-level source verification contract

For each CAM/KAM row, retain or reconstruct the following fields in a restricted local audit trail:

| Field | Requirement |
|---|---|
| `source_system` | SEC EDGAR / other identifiable primary source / transformed source; **not inferred solely from column labels** |
| `source_document_url` | Original filing or audit report URL |
| `cik` | SEC Central Index Key where applicable |
| `accession_number` | SEC filing accession number where applicable |
| `form_type` | SEC form type, e.g. 10-K, 20-F, where applicable |
| `filing_date` | Filing date from the original document metadata |
| `audit_report_date` | Auditor's actual dated report when available; do not equate automatically to SEC filing date |
| `fiscal_period_end` | Reporting period end distinguished from filing and signature dates |
| `matter_number_or_heading` | Original CAM/KAM span locator, title and a document-position anchor |
| `extraction_method` | Parser/script and version; manual verification protocol if applicable |
| `extracted_at` | Extraction date/time and extraction batch |
| `transformation_lineage` | Script/steps producing current Audit Analytics-like column names and taxonomies |
| `derived_topic_rule` | Source-extracted label versus mapped classifier topic |
| `vendor_or_other_enrichment` | Explicit yes/no/unknown, provider and license/rights if non-SEC data added |
| `match_status` | Matched primary filing / conflicting primary filing / no SEC match / pending |
| `document_hash` | Stable document checksum when permitted and feasible |

**Special check for the EU/UK KAM files:** The source claim is recorded, but a UK/European issuer is **not by itself evidence of an SEC filing**. Match each matter to an EDGAR filing if EDGAR is asserted as its origin. If no EDGAR filing exists, inspect the original extraction pipeline for another primary filing/report source and reclassify that subset explicitly. Do not force an SEC label or silently discard unmatched records.

## Current dataset and inference boundaries

| Dataset | Records reported in 12 October Drive checks | Ownership/source statement | Verification outcome |
|---|---:|---|---|
| `CAM.csv` | 45,924 | Owner reports SEC EDGAR origin; vendor-like schema | Filing-level accession/CIK crosswalk outstanding |
| `KAM.csv` | 86,122 | Owner reports SEC EDGAR origin; geographically broad KAM data | Individual SEC record coverage and any non-SEC subset outstanding |
| `kam (uk)2023.xlsx` | 28,826 | Owner reports SEC EDGAR origin | Original document links and mapping outstanding |
| `KAM20240505.csv` | 65,535 | Original notebook input / transformed extract | Sample truncation documented; row-level origin not independently traced |

## Required tests before a full scientific rerun or public release

1. **Extract/source concordance:** link representative rows, then all available rows, to verified original documents. Report matched/unmatched counts overall and by year, country and topic. Maintain a separate no-SEC-match category.
2. **Time reconstruction:** obtain the historical SEC filing date and, where available, auditor report date. Do not use `AUDIT_OPINION_FKEY` as an SEC key without a verified crosswalk. Test duplicates, multiple matters per report, amended filings and auditor changes.
3. **Topic reconstruction:** determine whether the 55 CAM and 59 KAM classifications are local annotation, rule-mapped, ML-predicted or other-source enrichments. Preserve original text and topic mapping separately.
4. **Vintages/truncation:** preserve input checksums; explain exactly why `KAM20240505.csv` contains 65,535 rows, and distinguish truncation from differences introduced by later EDGAR/source coverage. Reconcile notebook 49 topics against abstract 48.
5. **Security:** revoke reported hard-coded Hugging Face tokens and rescan all notebook and archive copies. Public repository content must contain no credentials.
6. **Rights/privacy:** EDGAR-accessible public text may allow a primary-source reproducibility subset, but check each record's provenance, embedded sensitive fields, any third-party enrichment, and applicable reuse obligations before publishing a combined CSV.
7. **Empirical integrity:** publish the firm-year/account-year panel only after matching audit-report dates, stable issuer identities, source drift and reissues. Maintain documented `t` versus `t+1` cutoff to prevent look-ahead.

## Archive and GitHub roles
- Google Drive: original files, provenance logs, restricted data and previous versions.
- Public GitHub: scripts, schemas, extraction instructions, synthetic test fixtures, and source-verified/redacted replication subsets where acceptable.
- Kaggle/Hugging Face: only separately approved source-verified public data and sanitized models/notebooks.

**This note is a source-attribution correction and verification plan, not a finding that all rows are independently confirmed SEC EDGAR records.**
