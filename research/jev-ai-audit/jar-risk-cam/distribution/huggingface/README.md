---
pretty_name: "DARWIN-JEV Risk-CAM Synthetic Replication Starter"
license: mit
task_categories:
- tabular-classification
tags:
- accounting
- auditing
- critical-audit-matters
- internal-control
- reproducibility
- synthetic
- sec
size_categories:
- n<1K
---

# DARWIN–JEV Risk–CAM Synthetic Replication Starter

**Principal investigator:** Dr. Saeid Homayoun  
**Target study:** *Do Auditors Disclose the Risks That Matter? Ex Ante Accounting Risk, Critical Audit Matter Alignment, and Subsequent Reporting Quality*  
**Journal target:** Journal of Accounting Research  
**Version:** 2026-10-16

## Public contents
This public distribution contains **synthetic demonstration data, schema validation code, tests, and source metadata only**. It does not contain the unpublished manuscript, private Google Drive observations, restricted third-party datasets, proprietary model weights, real CAM/ICFR labels, or empirical results.

## Canonical source
- GitHub: https://github.com/Saehon/Saeid-Homayoun/tree/research/jar-risk-cam-publication-20261016/research/jev-ai-audit/jar-risk-cam
- Publication package (private Google Drive): https://drive.google.com/drive/folders/1rX5r3VIS5x4prq0hlFFNIrH6OTACyuvB

## Data fields
`firm_id, fiscal_year, domain, industry, cutoff_date, evidence_available_date, cam_present, eligible, risk_probability, outcome_event, outcome_observed_date, icfr_status, accounting_standard`.

All rows in the public example are invented. Do not use them for substantive inference.

## Validation
The included contract tests reject duplicate firm-year-domain keys, predictor look-ahead, nonfuture outcomes, invalid probabilities, and invalid schema categories.

## Research status
No real-data regression, trained DARWIN-JEV model, Jev API inference, statistical significance, or FT50 empirical replication is claimed.
