# Multi-firm ICFR research expansion — 2026-10-12

**Status:** Working paper and deterministic scalable baseline; **NOT** live Microsoft Decision-1 or LEMON inference.

Canonical Drive folder: https://drive.google.com/drive/folders/1_uMkhVWC8jw9mqTHwhmejCiqrGitTBqL

Word manuscript: https://drive.google.com/file/d/1AAmtremMEM3YSSl9Reu66Jw2tyh7Od_z/view

Full ZIP with `scalable_icfr.py`, sample JSONL, deterministic output, manuscript text and Word document: https://drive.google.com/file/d/1fNbzfslzoJt3sTxbK98o9xnmociU6Gq1/view

## Executed offline baseline

| Case | Auditor reference | Deterministic triage | Independent deterministic gate |
|---|---|---|---|
| NVIDIA FY2025 | Effective | INSUFFICIENT | ABSTAIN |
| HP FY2024 | Adverse | HIGH | ESCALATE_TO_HUMAN |

Both outcomes are simulation only. Two cases do not establish statistical performance.

## Scale-up protocol

1. Build an issuer-year panel from public SEC EDGAR 10-K/10-K-A, CIK, accession, year, source spans and source hashes.
2. Keep auditor 404(b) reference opinions **outside** blinded model packets. Audit applicability and exclusions must be documented.
3. Use the ZIP's offline `scalable_icfr.py` JSONL processor as a reproducible transparent baseline. It processes arbitrary numbers of issuer-years; it is not a hosted AI model.
4. Only with approved real-public-data execution adapter and explicit API cost/data governance, run actual Microsoft Decision-1 and LEMON on identical blinded packets and archive traces.
5. Pre-register recall of adverse opinions, precision, abstention coverage, evidence-citation precision, reviewer disagreement and issuer-clustered uncertainty.
6. Require human sign-off; do not infer audit effectiveness from absence of deficiencies.

No data at scale have yet been collected or analyzed; this is a prospective multi-firm design and working manuscript, not a completed empirical TAR paper.
