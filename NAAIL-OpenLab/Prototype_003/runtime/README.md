# NAAIL OpenLab — Prototype 003 Runtime

**Status:** executable research scaffold  
**Architecture target:** V2026.3  
**Current validated public release remains:** v0.2.2 / Prototype 002

This directory implements the first runnable public scaffold for Prototype 003 under the frozen experimental rule:

> **Same case. Same evidence. Same gold labels. Same evaluator. Different execution architecture.**

## What is executable now

The first migrated benchmark is the frozen synthetic **Revenue Recognition & Cut-off** case (`P003-B-REV-001`). It compares four provider-neutral execution modes:

1. deterministic baseline;
2. single-agent architecture;
3. sequential-agent architecture;
4. governed multi-agent architecture.

The governed multi-agent path includes a Rights/License gate, Evidence Agent, Audit Risk Agent, Accounting Agent, Critic, Replicator, Falsifier, Evidence Passport, Professional Decision DAG and mandatory Human Gate.

This scaffold is intentionally deterministic and provider-neutral. It does **not** claim that Google ADK, Microsoft Agent Framework, Gemini, Azure, OpenAI, or any external LLM has been invoked. Provider adapters can be added later without changing the frozen case/evaluator contract.

## Run

```bash
cd NAAIL-OpenLab/Prototype_003/runtime
python prototype003.py
```

The runner writes `outputs/latest_results.json` and prints a compact architecture comparison.

## Test

```bash
python -m unittest discover -s tests -v
```

No third-party Python packages are required for the current scaffold.

## Frozen benchmark facts

- case: synthetic Revenue Recognition & Cut-off;
- period end: 2024-12-31;
- planted exceptions: `TX-002`, `TX-003`;
- proposed adjustment: EUR 190,000;
- planning materiality: EUR 120,000;
- required terminal state: `PENDING_HUMAN_APPROVAL`.

These values belong only to the synthetic benchmark and are not claims about any real company, auditor, accounting failure, or audit quality.

## Current evaluation fields

- RPA — Risk–Procedure Alignment;
- AA — Assertion Alignment;
- EG — Evidence Grounding;
- PS — Professional Skepticism proxy;
- DS — Documentation Sufficiency;
- DIST — deterministic decision/replay stability;
- precision / recall;
- false positives / false negatives;
- gold-adjustment match;
- Human Gate enforcement.

The current metrics are engineering-test proxies. They are not yet validated research constructs for external empirical claims.

## Governance invariants

```text
same_case_across_architectures = true
same_evidence_across_architectures = true
same_gold_labels_across_architectures = true
same_evaluator_across_architectures = true
human_gate_required = true
benchmark_leakage_allowed = false
unsupported_discovery_claim_allowed = false
```

## Next implementation gates

Before Prototype 003 can support a candidate v0.3.0 release:

- freeze the Goodwill/Impairment benchmark under the existing SEC-only three-company scope;
- freeze the ICFR Deficiency benchmark;
- add provider adapters behind a common interface;
- preserve identical evidence/gold/evaluator state across providers;
- add clean-environment CI replication and leakage tests;
- export the linked empirical tables defined in `PROTOTYPE_003_EXECUTION_SPEC.md`;
- complete rights/privacy/IP review;
- retain the Human Gate for every professional or scientific claim.

See also:

- `../../PROTOTYPE_003_EXECUTION_SPEC.md`
- `../../CURRENT_PROJECT_STATE.md`
- `../../versions/V2026.3_MULTI_AGENT_DIGITAL_TWIN.md`
