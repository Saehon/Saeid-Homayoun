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
| P003-C SEC-Anchored Goodwill / Impairment | planned | planned | planned | planned |
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

### P003-C — SEC-Anchored Goodwill / Impairment benchmark

P003-C is restricted to exactly three public-company evidence anchors:

1. Microsoft Corporation;
2. Alphabet Inc. (Google);
3. Amazon.com, Inc.

The real-company evidence layer must use **SEC EDGAR / Form 10-K / iXBRL only**. No fourth company may be introduced without an explicit versioned scope change.

The three companies provide public accounting evidence anchors. Controlled or synthetic transformations must generate the benchmark-specific planted ambiguities/exceptions, scenario parameters, and frozen gold labels.

The benchmark must not be represented as evidence that Microsoft, Alphabet, or Amazon has an undisclosed impairment, audit failure, ICFR deficiency, or deficient audit quality.

Canonical scope: [PROTOTYPE_003C_SEC_SCOPE.md](./PROTOTYPE_003C_SEC_SCOPE.md)

Target evidence includes, where available and relevant:
- goodwill balances;
- goodwill/intangible-asset notes;
- acquisitions and purchase-price allocation;
- impairment accounting policies;
- segment/reporting-unit context;
- management estimates and uncertainty disclosures;
- valuation/cash-flow-related disclosures;
- relevant XBRL facts and filing metadata.

Each evidence object should preserve issuer, filing/accession/source reference, reporting period, evidence type/concept, raw reference or fact, normalized value/meaning, and provenance/hash where feasible.

P003-C pipeline:

**SEC EDGAR → 10-K / iXBRL → source hash → normalized accounting evidence → Evidence Passport™ → controlled benchmark transformation → frozen gold labels → architecture comparison → Professional Decision DAG™ → Human Gate**

### P003-D — ICFR Deficiency case
Build a controlled controls case with control design/operation evidence, deficiency severity logic, contradictory evidence, gold labels, and escalation conditions.

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

For P003-C, provenance must allow a public evidence object to be traced back to the SEC filing source.

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
- evaluation-definition immutability checks;
- SEC evidence provenance checks for P003-C;
- company-scope check that fails if a fourth issuer enters P003-C.

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

For P003-C, `EVIDENCE_LEVEL` should preserve issuer and SEC-source provenance while benchmark conclusions remain explicitly separated from real-company facts.

## First empirical study

**Research question:**

> Does governed multi-agent audit orchestration improve evidence grounding and professional judgment relative to single-agent AI?

The empirical design should compare deterministic control, single-agent AI, sequential-agent AI, governed multi-agent AI, and a human-led baseline where feasible.

No claim of superiority is assumed in advance. Prototype 003 is designed to test the question, not prove a preferred answer.

## Release gate for candidate v0.3.0

Do not promote v0.3.0 until:

1. all benchmark case families are frozen, versioned, and hashable;
2. P003-C is limited to Microsoft, Alphabet, and Amazon only;
3. P003-C evidence can be traced reproducibly to SEC EDGAR / 10-K / iXBRL sources;
4. all four architectures operate on identical case/evidence/gold conditions;
5. run manifests are complete;
6. Evidence Passport™, Professional Decision DAG™, and Human Gate are enforced;
7. the evaluator is frozen;
8. regression and leakage tests pass;
9. deterministic replay is exact;
10. model/provider/version metadata is preserved;
11. empirical datasets can be regenerated from raw run artifacts;
12. clean-environment replication succeeds;
13. public artifacts pass rights, privacy, and IP review;
14. benchmark findings are clearly separated from real-company facts and do not make unsupported allegations;
15. the benchmark is stable enough to support the first empirical manuscript.

## Engineering invariants

```text
same_case_across_architectures = true
same_evidence_across_architectures = true
same_gold_labels_across_architectures = true
same_evaluator_across_architectures = true
p003c_company_scope = [Microsoft, Alphabet, Amazon]
p003c_real_company_source = SEC_EDGAR_10K_iXBRL
real_company_facts_equal_benchmark_gold = false
human_gate_required = true
benchmark_leakage_allowed = false
post_hoc_gold_changes_allowed = false
optimize_for_desired_result = false
```

## Public / private boundary

This document intentionally describes the public research contract, not private implementation details. Patent-sensitive orchestration, private prompts/specifications, benchmark-construction internals, advanced Control Plane logic, unpublished evaluation mechanisms, private experimental results, restricted data, and pre-commercial implementation remain private until IP review.

References to Microsoft, Alphabet/Google, Amazon, and the SEC identify public evidence sources or research subjects only. They do not imply affiliation, endorsement, sponsorship, certification, or any finding of accounting/audit deficiency.

## Governing principle

**Models generate. Agents debate. Code tests. Evidence decides. Humans approve.**
