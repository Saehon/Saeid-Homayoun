# NVIDIA vs HP — ICFR two-case pilot

Status: EVIDENCE REVIEW ONLY — NOT A MODEL BENCHMARK.

Canonical Google Drive folder: https://drive.google.com/drive/folders/1_uMkhVWC8jw9mqTHwhmejCiqrGitTBqL

## Scope
Compare Microsoft Decision-1 fixed-choice ICFR risk triage with LEMON-ICFR-US independent evidence review for NVIDIA FY2025 and HP FY2024. No future-year predictions, FutureMW outcomes, or predictive claims.

## Evidence register
| Case | Evidence | Auditor ICFR opinion | Microsoft Decision-1 real run | LEMON real run |
| --- | --- | --- | --- | --- |
| NVIDIA FY2025 | SEC 10-K https://www.sec.gov/Archives/edgar/data/1045810/000104581025000023/nvda-20250126.htm ; prior DARWIN source-coding QA | Effective (per prior SEC-based QA; requires independent replication) | NOT RUN | NOT RUN |
| HP FY2024 | Drive report titled HP_FY2024_ICFR_ADVERSE_POSITIVE but its content was empty on retrieval | UNVERIFIED; do not treat title as proof | NOT RUN | NOT RUN |

## Mandatory evaluation controls
1. Independently verify original SEC source and 404(b) scope for each issuer-year.
2. Mask auditor opinion, labels and assessor notes from model-visible evidence; retain them in a separate evaluation record.
3. Run only through an approved real-public-data adapter. The current `decision1_pilot.py` explicitly rejects real cases and its offline rule baseline is NOT Microsoft Decision-1.
4. Do not transmit any confidential or licensed information to hosted services. Confirm API authorization, cost and retention before hosted execution.
5. Require evidence IDs, source provenance, abstention on incomplete or contradictory evidence, and independent human review. Never auto-approve audit conclusions.
6. Preserve raw model output and version/trace for both arms. Report disagreement only when both actual outputs exist.

No live model execution or accuracy comparison is claimed. Do not modify original case files or merge without review.
