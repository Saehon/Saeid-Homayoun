# Case 002 — Microsoft FY2026 SEC Accounting & Audit Evidence Benchmark

This is FRANKENSTEIN's first **real-company SEC benchmark case**.

## Authoritative source

Microsoft Corporation, Form 10-K for fiscal year ended June 30, 2026  
Filed: July 29, 2026  
Accession: 0001193125-26-323660  
SEC filing: https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm

## Frozen evidence

| Metric | FY2026 | FY2025 |
|---|---:|---:|
| Revenue | 331,839 | 281,724 |
| Gross margin | 225,465 | — |
| Operating income | 155,237 | — |
| Net income | 133,749 | — |

The filing evidence also records an unqualified opinion on the financial statements and an unqualified opinion on ICFR as of June 30, 2026.

## Deterministic gold standard

- Revenue growth: **17.79%**
- Gross margin: **67.94%**
- Operating margin: **46.78%**
- Net margin: **40.31%**
- Financial-statement opinion: **unqualified**
- ICFR opinion: **unqualified**

## Pipeline

```text
SEC 10-K
  ↓
Frozen evidence packet
  ↓
Financial Accounting / Audit agents
  ↓
Provider model (when configured)
  ↓
Deterministic recalculation
  ↓
Reviewer
  ↓
Human gate for material professional interpretation
```

Run the deterministic control:

```bash
python FRANKENSTEIN/phase4_benchmark/validate_case_002_microsoft.py
```

This case does not claim that FRANKENSTEIN has performed an audit. It benchmarks evidence-grounded extraction, calculation, classification, and review.
