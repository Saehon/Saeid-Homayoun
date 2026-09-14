# NAAIL OpenLab™ — Prototype 003 Execution Specification

**Status:** Research-safe public execution specification  
**Current public baseline:** v0.2.2 / Prototype 002  
**Next executable milestone:** Prototype 003  
**Candidate release after validation:** v0.3.0  
**Updated:** 2026-09-14

## Objective

Prototype 003 converts the current single-case Audit Digital Twin baseline into a controlled **multi-case × multi-architecture experimental platform** for reproducible audit-AI research.

The scientific comparison is intentionally simple:

> Same case. Same evidence. Same frozen gold labels. Same evaluation contract. Different execution architecture.

This isolates the effect of orchestration architecture from changes in evidence, labels, scoring, or case design.

## Experimental matrix

| Case family | Deterministic | Single-agent AI | Sequential-agent AI | Governed multi-agent AI |
|---|---:|---:|---:|---:|
| Revenue Recognition & Cut-off | ✓ | planned | planned | planned |
| Goodwill Impairment | planned | planned | planned | planned |
| ICFR Deficiency | planned | planned | planned | planned |

A human-only or human-led comparator may be added where feasible.

## P003 work packages

### P003-A — Common contracts
Freeze shared schemas for:
- case manifest;
- evidence registry;
- gold labels;
- materiality and decision thresholds;
- run manifest;
- evaluation output;
- Human Gate state.

### P003-B — Revenue baseline migration
Migrate the existing Prototype 002 Revenue Recognition & Cut-off case into the common contract without changing its frozen evidence or gold state.

### P003-C — Goodwill Impairment case
Build a synthetic valuation/estimate case with explicit assumptions, impairment indicators, evidence conflicts, planted ambiguities, gold labels, and review triggers.

### P003-D — ICFR Deficiency case
Build a synthetic controls case with control design/operation evidence, deficiency severity logic, contradictory evidence, gold labels, and escalation conditions.

### P003-E — Runner contracts
Implement four provider-neutral execution modes:
1. deterministic baseline;
2. single-agent AI;
3. sequential-agent AI;
4. governed multi-agent AI.

The runner may change. The case, evidence, gold labels, evaluation logic, and governance contract may not.

### P003-F — Governance artifacts
Every applicable run must emit:
- Evidence Passport™;
- Professional Decision DAG™;
- Human Gate state;
- evidence provenance;
- model/provider/tool/agent metadata;
- reviewer/critic output;
- limitations;
- run manifest.

### P003-G — Frozen evaluator
One evaluator must score all comparable architectures using the same definitions.

Core measures:
- RPA — Risk–Procedure Alignment;
- AA — Assertion Alignment;
- EG — Evidence Grounding;
- PS — Professional Skepticism;
- DS — Documentation Sufficiency;
- DIST — Decision/Inference Stability;
- precision / recall;
- false positives / false negatives;
- evidence/citation traceability;
- reproducibility;
- latency;
- execution cost;
- human overrides and reasons.

### P003-H — Reliability and leakage tests
Required tests include:
- deterministic replay;
- regression tests;
- clean-environment rerun;
- stochastic seed/version capture;
- provider/model swap checks;
- benchmark leakage checks;
- gold-label immutability checks;
- evaluation-definition immutability checks.

### P003-I — Benchmark execution
Run the complete case × architecture matrix. Preserve null, negative, failed, and contradictory results rather than selectively reporting favorable outcomes.

### P003-J — Empirical export
Create manuscript-ready linked datasets:
- `CASE_MANIFEST`;
- `RUN_LEVEL`;
- `METRIC_LEVEL`;
- `EVIDENCE_LEVEL`;
- `DECISION_LEVEL`;
- `HUMAN_GATE_LEVEL`;
- `FAILURE_LOG`.

## First empirical study

**Research question:**

> Does governed multi-agent audit orchestration improve evidence grounding and professional judgment relative to single-agent AI?

The empirical design should compare deterministic control, single-agent AI, sequential-agent AI, governed multi-agent AI, and a human-led baseline where feasible.

No claim of superiority is assumed in advance. Prototype 003 is designed to test the question, not prove a preferred answer.

## Release gate for candidate v0.3.0

Do not promote v0.3.0 until:

1. all three case families are frozen, versioned, and hashable;
2. all four architectures operate on identical case/evidence/gold conditions;
3. run manifests are complete;
4. Evidence Passport™, Professional Decision DAG™, and Human Gate are enforced;
5. the evaluator is frozen;
6. regression and leakage tests pass;
7. deterministic replay is exact;
8. model/provider/version metadata is preserved;
9. empirical datasets can be regenerated from raw run artifacts;
10. clean-environment replication succeeds;
11. public artifacts pass rights, privacy, and IP review;
12. the benchmark is stable enough to support the first empirical manuscript.

## Engineering invariants

```text
same_case_across_architectures = true
same_evidence_across_architectures = true
same_gold_labels_across_architectures = true
same_evaluator_across_architectures = true
human_gate_required = true
benchmark_leakage_allowed = false
post_hoc_gold_changes_allowed = false
optimize_for_desired_result = false
```

## Public / private boundary

This document intentionally describes the public research contract, not private implementation details. Patent-sensitive orchestration, private prompts/specifications, benchmark-construction internals, advanced Control Plane logic, unpublished evaluation mechanisms, private experimental results, restricted data, and pre-commercial implementation remain private until IP review.

## Governing principle

**Models generate. Agents debate. Code tests. Evidence decides. Humans approve.**
