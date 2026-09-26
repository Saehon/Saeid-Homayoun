# Open-Source Accounting, Audit & Finance Integration Registry

Updated: 2026-09-26

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
