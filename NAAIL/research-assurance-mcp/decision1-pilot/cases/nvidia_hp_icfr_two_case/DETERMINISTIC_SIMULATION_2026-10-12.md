# Two-case ICFR simulation — 2026-10-12

**Deterministic illustration ONLY: Microsoft Decision-1 and LEMON were NOT actually executed.**

| Issuer | SEC auditor ICFR reference | Simulated Decision-1 risk | Simulated LEMON gate |
| --- | --- | --- | --- |
| NVIDIA FY2025 | Effective | INSUFFICIENT | ABSTAIN / request independent control-testing evidence |
| HP FY2024 | Adverse | HIGH | ESCALATE_TO_HUMAN |

## Method
- Both inputs are blinded to auditor ICFR opinions. Reference opinions are evaluation-only.
- NVIDIA packet contains no independently extracted control-testing facts, so the simulated scorer must abstain.
- HP packet has source-indexed ITGC deficiencies concerning user access, change management and monitoring scheduled jobs; deterministic rules trigger HIGH risk and independent review.
- No model probabilities, live inference, or empirical model performance estimates. No forecasting.
- Human approval is false for both cases. Do not treat simulated HIGH as an auditor opinion.

Sources: [NVIDIA 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000023/nvda-20250126.htm), [HP 10-K](https://www.sec.gov/Archives/edgar/data/47217/000004721724000080/hpq-20241031.htm).

[Google Drive project folder](https://drive.google.com/drive/folders/1_uMkhVWC8jw9mqTHwhmejCiqrGitTBqL). Local full evidence packets, CSV, JSON and README delivered in chat as ZIP. This Markdown record alone is the GitHub publication.