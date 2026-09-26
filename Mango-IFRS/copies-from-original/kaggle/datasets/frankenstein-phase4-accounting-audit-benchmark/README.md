# FRANKENSTEIN Phase 4 — Accounting & Audit Benchmark

Public benchmark package for provider-neutral accounting/audit AI experiments.

## Canonical source
https://github.com/Saehon/Saeid-Homayoun/tree/main/FRANKENSTEIN/phase4_benchmark

## Benchmark case
BANK-REC-001 is a deterministic bank-reconciliation case with a gold-standard adjusted bank and book balance of 100,500.

## Included files
- case_001_bank_reconciliation.json
- benchmark_case_evidence.csv
- providers.json
- mock_perfect_response.json
- status.json

The package contains **no API keys and no claimed live-provider ranking**. The current status records that the first controlled live workflow skipped all six providers because credentials/model variables were not configured.

Provider families represented:
GPT/Codex, Claude, Gemini, Microsoft/Azure, Kimi/Moonshot, and DeepSeek.

Use this package for research and education. Do not infer audit assurance or provider superiority from this single pipeline-validation case.


## Case 002 — MSFT-SEC-2026-001

Real-company benchmark based on Microsoft Corporation's FY2026 SEC Form 10-K.

Authoritative filing:
https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm

Frozen deterministic targets:
- FY2026 revenue growth vs FY2025: **17.79%**
- FY2026 gross margin: **67.94%**
- FY2026 operating margin: **46.78%**
- FY2026 net margin: **40.31%**
- Financial-statement audit opinion: **unqualified**
- ICFR audit opinion: **unqualified**

The case validates evidence-grounded extraction, recalculation, opinion classification, reviewer controls, and human-gate logic. It does not claim that the benchmark system performed an audit.
