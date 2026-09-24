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
