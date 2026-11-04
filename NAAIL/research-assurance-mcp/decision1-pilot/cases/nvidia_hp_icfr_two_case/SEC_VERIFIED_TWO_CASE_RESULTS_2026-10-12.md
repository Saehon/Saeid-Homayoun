# Two-case SEC-verified ICFR result — 2026-10-12

Scope: NVIDIA FY2025 vs HP Inc FY2024. No forecasting.

## Verified auditor reference labels (SEC primary filings)

- NVIDIA FY2025 (FY ended 2025-01-26): PwC opinion: effective ICFR. SEC: https://www.sec.gov/Archives/edgar/data/1045810/000104581025000023/nvda-20250126.htm
- HP Inc FY2024 (FY ended 2024-10-31): Ernst & Young adverse ICFR opinion; material weakness in IT general controls (user access, change management, job schedule monitoring) affecting certain IT applications and dependent controls. The financial statement opinion remained unqualified. SEC: https://www.sec.gov/Archives/edgar/data/47217/000004721724000080/hpq-20241031.htm

## Execution status
- Actual Microsoft Decision-1 hosted inference on these SEC cases: NOT RUN.
- Actual LEMON-ICFR-US inference on these SEC cases: NOT RUN.
- Therefore agreement, sensitivity, specificity, accuracy and comparative superiority: NOT MEASURABLE.
- Existing Decision-1 pilot enforces synthetic-only and its offline baseline is NOT Microsoft's hosted model. Do not bypass authorization or mislabel offline rules as hosted model results.

## Next gated steps
- Prepare blinded, matched SEC evidence packets excluding auditor opinion and reference labels from model inputs; retain independent evaluator gold labels separately.
- Approve real-public-data execution adapter and API/privacy/cost policy; run and archive raw traces for both models with versions and evidence IDs.
- Independently adjudicate results, including abstentions. With only two cases, treat any observed agreement as a case demonstration, not generalizable statistical evidence.

Canonical Google Drive folder: https://drive.google.com/drive/folders/1_uMkhVWC8jw9mqTHwhmejCiqrGitTBqL
