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
