---
license: cc0-1.0
pretty_name: FRANKENSTEIN Phase 4 Accounting & Audit Benchmark
task_categories:
- question-answering
tags:
- accounting
- auditing
- finance
- benchmarking
- agents
language:
- en
---

# FRANKENSTEIN Phase 4 Accounting & Audit Benchmark

A provider-neutral research benchmark for testing AI systems on a frozen accounting/audit case while holding the evidence packet, prompt, output schema, and deterministic scoring logic constant.

## Canonical GitHub source
https://github.com/Saehon/Saeid-Homayoun/tree/main/FRANKENSTEIN/phase4_benchmark

## Case 001 — BANK-REC-001

The first case is a deterministic bank reconciliation. The gold-standard adjusted bank balance and adjusted book balance are both **100,500**.

The benchmark evaluates:
- adjusted bank balance;
- adjusted book balance;
- book-entry items;
- bank-only reconciling items;
- journal entries;
- balance conclusion;
- evidence completeness;
- unsupported claims.

## Provider families

The research harness is designed for:
- GPT/Codex;
- Claude;
- Gemini;
- Microsoft/Azure;
- Kimi/Moonshot;
- DeepSeek.

No provider API keys are included here. No live-provider ranking is claimed from the first controlled workflow because all provider calls were skipped when credentials/model variables were absent.

## Research boundary

This is a research and educational benchmark. It does not issue an audit opinion, declare accounting compliance, or establish provider superiority.


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
