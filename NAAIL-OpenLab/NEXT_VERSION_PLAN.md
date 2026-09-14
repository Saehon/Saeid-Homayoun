# NAAIL OpenLab™ — Next Version Plan

**Status:** Development handoff / not a release  
**Current public baseline:** v0.2.2 — Audit Digital Twin Prototype 002  
**Working next-release target:** v0.3.0 candidate only; do not tag or publish until release gates pass.  
**Date:** 2026-09-14

## Purpose

This file preserves the canonical handoff from the current public v0.2.2 baseline into the next development cycle. GitHub remains the source of truth; Google Drive remains the mirror/archive.

## Next technical milestone — Prototype 003

Build a multi-case, multi-architecture governed Audit Digital Twin benchmark using the same evidence, frozen gold labels, evaluation contract, and Human Gate.

### Case families
1. Revenue Recognition & Cut-off — retain as frozen baseline.
2. Goodwill Impairment — add as a frozen synthetic case.
3. ICFR Deficiency — add as a frozen synthetic case.

### Execution architectures
1. Deterministic baseline.
2. Single-agent AI.
3. Sequential-agent AI.
4. Governed multi-agent AI.

Where feasible, add a human-only or human-led comparison for empirical research.

## Mandatory governance for every run

- Evidence Passport™.
- Professional Decision DAG™.
- Human Gate for material professional/scientific conclusions.
- Provider-neutral model/agent adapter contract.
- Frozen case hashes, gold labels, run manifests, and evaluation definitions.
- Traceable evidence IDs, model/adapter identity, limitations, and reproducibility metadata.
- No self-certification of high-risk conclusions.
- No benchmark leakage or optimization for desired findings.

## Frozen evaluation contract

Track at minimum:
- RPA — Risk–Procedure Alignment.
- AA — Assertion Alignment.
- EG — Evidence Grounding.
- PS — Professional Skepticism.
- DS — Documentation Sufficiency.
- DIST — Decision/Inference Stability.
- Precision and recall.
- False positives and false negatives.
- Citation/evidence traceability.
- Reproducibility.
- Completion time, latency, and execution cost.
- Human overrides and reasons.

Development, validation, Blind Gold, adversarial/red-team, and temporal/modified-scenario holdout sets must remain separated.

## First empirical paper from the next version

**Research question:** Does governed multi-agent audit orchestration improve evidence grounding and professional judgment relative to single-agent AI?

Primary comparison groups: deterministic control, single-agent AI, sequential-agent AI, governed multi-agent AI, and human-led baseline where feasible.

The empirical paper should use frozen hypotheses/outcomes where feasible, preserve null and negative results, use held-out evaluation, report model/provider versions and reproducibility metadata, and include robustness/falsification tests.

## Public / private boundary

Public release may include research-safe architecture, synthetic cases, evaluation definitions, selected reproducibility artifacts, and validated benchmark summaries.

Private R&D must retain patent-sensitive orchestration, unpublished prompts/specifications, private benchmark construction, detailed Control Plane logic, advanced evaluation logic, pre-commercial implementation, and restricted/licensed data until IP review.

Do not claim patent pending unless an application has actually been filed. Do not fabricate DOI metadata. Preserve upstream licenses and third-party attribution.

## Candidate v0.3.0 release gate

Do not promote the next public release until all of the following are true:
1. Revenue Recognition, Goodwill Impairment, and ICFR Deficiency are frozen and versioned.
2. All four execution architectures run against identical evidence and gold labels.
3. Evidence Passport™ and Professional Decision DAG™ are emitted for every run.
4. Human Gate is enforced.
5. Frozen evaluation metrics are calculated consistently.
6. Regression and reproducibility tests pass.
7. Provider/model swaps do not alter the case or evaluation contract.
8. Outputs can be exported for empirical analysis.
9. No private, restricted, or patent-sensitive implementation is exposed.
10. The benchmark is stable enough to support the first empirical manuscript.

## Canonical direction

**Models generate. Agents debate. Code tests. Evidence decides. Humans approve.**

Next work should prioritize executable systems, frozen benchmarks, tests, empirical analysis, reproducibility, and publication-quality evidence over additional architecture-only documentation.
