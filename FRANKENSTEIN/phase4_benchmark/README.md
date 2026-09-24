# FRANKENSTEIN Phase 4 — Cross-Model Scientific Benchmarking

**Status: benchmark harness ACTIVE; live proprietary-provider comparison requires the user's provider credentials.**

Phase 4 holds the accounting case, evidence, output schema, scoring logic and temperature constant while changing the model/provider.

## Provider families

- OpenAI GPT/Codex
- Anthropic Claude
- Google Gemini
- Microsoft/Azure-hosted model
- Kimi/Moonshot
- DeepSeek

No API key or exact model ID is committed to GitHub.

## Case 001

The first case is a deterministic bank reconciliation:

- unadjusted book cash = 100,000;
- bank statement = 108,500;
- outstanding checks = 12,000;
- deposit in transit = 4,000;
- unrecorded bank fee = 500;
- unrecorded interest = 1,000.

Gold-standard adjusted bank and book balances are both **100,500**.

This is intentionally simple so differences among providers cannot be blamed on an ambiguous accounting standard.

## Metrics

The deterministic scorer checks:
1. adjusted bank balance;
2. adjusted book balance;
3. items requiring book entries;
4. bank-only reconciling items;
5. journal entries;
6. whether the reconciliation balances;
7. evidence completeness;
8. unsupported claims.

Accuracy is the share of these eight components that exactly pass.

## Run without credentials

```bash
cd FRANKENSTEIN/phase4_benchmark
python benchmark.py --mode dry-run
python benchmark.py --mode score-mock
```

## Live run

Configure the provider's API key, exact model ID, and—where required—the exact endpoint URL. Then run:

```bash
cd FRANKENSTEIN/phase4_benchmark
python benchmark.py --mode live --output results.json
```

Providers missing configuration are **skipped**, never silently substituted.

## Scientific rule

Do not compare model families unless the case, evidence packet, prompt, temperature, scoring code and run metadata are frozen. Do not claim a provider is superior from one simple case; this first case validates the benchmarking pipeline only.


## Public mirrors

- Kaggle: https://www.kaggle.com/datasets/sadhon/frankenstein-phase4-accounting-audit-benchmark
- Hugging Face: https://huggingface.co/datasets/SADHON/frankenstein-phase4-accounting-audit-benchmark

These mirrors contain the frozen case, evidence table, provider registry, scoring fixture and benchmark status. They do not contain API keys or fabricated provider results.


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
