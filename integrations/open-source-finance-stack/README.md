# Open-Source Accounting, Audit & Finance Integration Registry

Updated: 2026-09-27

This registry integrates external projects by reference/adapters rather than copying third-party source code. Upstream licenses remain authoritative.

| Component | Role | License | Integration status |
|---|---|---|---|
| Accounted | Agent-native accounting/ERP and MCP reference implementation | AGPL-3.0-or-later | Evaluate via isolated adapter; do not vendor into permissive core |
| sec-data | SEC EDGAR/XBRL extraction and financial statement pipeline | Apache-2.0 | Priority benchmark/integration candidate |
| Magpie | Accounting CLI/MCP and controlled ledger interface | Verify upstream before deployment | Sandbox/evaluation candidate |
| EDGAR MCP | Agent-facing SEC/FRED/OpenFIGI data access | MIT | SEC research-agent adapter candidate |
| FinanceComplexQA | Financial document agentic-reasoning benchmark | Apache-2.0 | Evaluation-suite candidate |
| LineLedger | General ledger / journal / trial-balance engine | AGPLv3 | Isolated evaluation; do not vendor into permissive core |

## Governance

1. Preserve upstream attribution and license.
2. No external component enters the authoritative Knowledge Core automatically.
3. AGPL components remain isolated unless a deliberate licensing review approves deeper integration.
4. Data/model artifacts require provenance, version, checksum where practical, and an Evidence Passport.
5. Benchmark outputs are evidence, not ground truth.
6. Material accounting/audit conclusions remain subject to reviewer/falsification and human approval.

## Platform roles

- **GitHub:** canonical integration registry, adapters, tests, provenance and CI.
- **Hugging Face:** eligible models/datasets/evaluation artifacts; preserve dataset/model licenses and cards.
- **Kaggle:** reproducible notebooks and eligible public datasets/benchmarks; preserve original licenses and citations.

## Initial priority

1. Benchmark `sec-data` against the existing SEC/XBRL pipeline.
2. Add FinanceComplexQA as an external evaluation set.
3. Prototype EDGAR MCP behind a read-only research-agent interface.
4. Evaluate Accounted and Magpie in isolated sandboxes.
5. Keep AGPL code outside the core unless licensing implications are explicitly accepted.


## Scout batch — 2026-09-27

| Component | Platform | Purpose | Verified license | Integration mode |
|---|---|---|---|---|
| TradingAgents v0.5.1 | GitHub | Multi-agent financial research/trading framework; SEC EDGAR and point-in-time workflows | Apache-2.0 | Technology-layer sandbox and architecture benchmark |
| Finch / FinWorkBench | Hugging Face + GitHub | 172 finance/accounting spreadsheet-centric enterprise workflows for agent evaluation | CC BY 3.0 | External benchmark with attribution; no training leakage into sealed evaluation |
| Verified Credit Research Agent | GitHub | SEC/XBRL credit research with deterministic numeric verification, workpapers and guardrails | MIT | Audit/assurance architecture reference and sandbox |
| SEC-10-K-Structured-Extraction | GitHub | Deterministic/rule-based 10-K item extraction to standardized JSON | MIT | Extraction benchmark and candidate adapter |

### Installation policy for this batch

- Components are **registered and integrated by reference** in the canonical GitHub stack; upstream source is not silently copied.
- Runtime installation happens only in isolated environments/workflows, pinned to a release/commit where practical.
- TradingAgents must not be allowed to turn trading output into accounting/audit evidence without independent verification.
- Finch is treated as an external evaluation benchmark; preserve CC BY 3.0 attribution and keep sealed reference outputs out of model-development loops.
- Verified Credit Research Agent and SEC-10-K-Structured-Extraction may be adapted under MIT, while preserving copyright/license notices.
- SEC-derived numeric claims must retain filing/accession/provenance and deterministic validation before use.
- Cross-publishing to Hugging Face/Kaggle is limited to artifacts whose upstream licenses and dataset terms permit redistribution; otherwise publish adapters, manifests, notebooks, and citations rather than mirrored content.

### Cross-platform targets

- Hugging Face: benchmark/evaluation manifests, dataset cards and eligible derived evaluation artifacts.
- Kaggle: reproducible notebooks and benchmark manifests after GitHub validation.
- GitHub remains the canonical source for code, provenance, license gates and integration decisions.
