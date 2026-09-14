# NAAIL OpenLab™ — Next Version Plan

**Status:** Development handoff / not a release  
**Current public baseline:** v0.2.2 — Audit Digital Twin Prototype 002  
**Working next-release target:** v0.3.0 candidate only; do not tag or publish until release gates pass.  
**Next executable milestone:** Prototype 003  
**Updated:** 2026-09-14

## Purpose

This file preserves the canonical handoff from the current public v0.2.2 baseline into the next development cycle. GitHub remains the source of truth; Google Drive remains the mirror/archive.

The next version must prioritize executable systems, frozen benchmarks, reproducibility, empirical comparison, and publication-quality evidence over additional architecture-only documentation.

## Prototype 003 objective

Build a multi-case, multi-architecture governed Audit Digital Twin benchmark in which every architecture receives the same frozen evidence, case definition, gold labels, materiality logic, evaluation contract, and Human Gate.

### Frozen case families

1. **Revenue Recognition & Cut-off** — retain Prototype 002 as the frozen baseline.
2. **Goodwill Impairment** — add a frozen synthetic estimate/valuation case.
3. **ICFR Deficiency** — add a frozen controls-deficiency case.

Each case must use the same public-safe case contract: case ID/version, evidence IDs, risks, assertions, procedures, controls where relevant, planted exceptions/ambiguities, gold labels, materiality/decision logic, Human Gate conditions, case hash, and reproducibility manifest.

## Execution architectures

Run every frozen case through the same four architectures:

1. **Deterministic baseline**.
2. **Single-agent AI**.
3. **Sequential-agent AI**.
4. **Governed multi-agent AI**.

Where feasible, add a human-only or human-led comparison for empirical research.

Model/provider swaps must occur through a provider-neutral adapter contract and must not change the case, evidence, gold labels, evaluation logic, or governance requirements.

## Prototype 003 implementation order

1. Freeze a common Digital Twin case schema and validation rules.
2. Refactor the Revenue Recognition baseline into that schema without changing its gold labels.
3. Build and freeze the Goodwill Impairment synthetic case.
4. Build and freeze the ICFR Deficiency synthetic case.
5. Implement the four runner contracts against identical case inputs.
6. Enforce Evidence Passport™, Professional Decision DAG™, and Human Gate outputs for every run.
7. Implement one shared evaluation harness across all cases and architectures.
8. Add regression, determinism, seed/re-run, leakage, and reproducibility tests.
9. Run the complete benchmark matrix and preserve null/negative results.
10. Export tidy, manuscript-ready outputs for statistical analysis and tables.

## Mandatory governance for every run

- Evidence Passport™.
- Professional Decision DAG™.
- Human Gate for material professional/scientific conclusions.
- Provider-neutral model/agent adapter contract.
- Frozen case hashes, gold labels, run manifests, and evaluation definitions.
- Traceable evidence IDs, model/adapter identity, limitations, and reproducibility metadata.
- Critic/reviewer output where an AI architecture is used.
- No self-certification of high-risk conclusions.
- No benchmark leakage or optimization for desired findings.

## Frozen evaluation contract

Track at minimum:

- **RPA** — Risk–Procedure Alignment.
- **AA** — Assertion Alignment.
- **EG** — Evidence Grounding.
- **PS** — Professional Skepticism.
- **DS** — Documentation Sufficiency.
- **DIST** — Decision/Inference Stability.
- Precision and recall.
- False positives and false negatives.
- Citation/evidence traceability.
- Reproducibility.
- Completion time, latency, and execution cost.
- Human overrides and reasons.

Development, validation, Blind Gold, adversarial/red-team, and temporal/modified-scenario holdout sets must remain separated.

Do not create arbitrary success thresholds after observing results. Freeze acceptance criteria before the final benchmark run.

## Release-candidate acceptance checks

Prototype 003 cannot become a v0.3.0 candidate unless:

1. All three cases are frozen, versioned, and hashable.
2. All four architectures run against identical evidence and gold labels.
3. Every completed run emits a valid run manifest.
4. Evidence Passport™, Professional Decision DAG™, and Human Gate are present for every applicable run.
5. The evaluation harness calculates the same metric definitions across all architectures.
6. Regression and reproducibility tests pass on the frozen benchmark.
7. Re-running a frozen deterministic configuration reproduces the expected output exactly.
8. Stochastic/model runs preserve complete seed/model/provider/version metadata.
9. Benchmark leakage checks pass.
10. Outputs are exportable in tidy form for empirical analysis.
11. Public artifacts contain no restricted, licensed, patent-sensitive, or private implementation material.
12. A replication README can reproduce the public-safe benchmark from a clean environment.

## Manuscript-ready empirical package

The next version should produce one analysis-ready dataset with one row per case × architecture × run plus linked metric-level and evidence-level tables.

Minimum manuscript outputs:

- benchmark descriptive statistics;
- architecture-by-case performance table;
- evidence-grounding and professional-judgment comparison table;
- reproducibility/stability table;
- latency/cost table;
- human-override summary;
- robustness/falsification outputs;
- machine-readable run manifest and case manifest.

## First empirical paper from the next version

**Research question:** Does governed multi-agent audit orchestration improve evidence grounding and professional judgment relative to single-agent AI?

Primary comparison groups: deterministic control, single-agent AI, sequential-agent AI, governed multi-agent AI, and human-led baseline where feasible.

The empirical paper should use frozen hypotheses/outcomes where feasible, preserve null and negative results, use held-out evaluation, report model/provider versions and reproducibility metadata, and include robustness/falsification tests.

## Public / private boundary

Public release may include research-safe architecture, synthetic cases, evaluation definitions, selected reproducibility artifacts, validated benchmark summaries, and replication instructions.

Private R&D must retain patent-sensitive orchestration, unpublished prompts/specifications, private benchmark construction, detailed Control Plane logic, advanced evaluation logic, pre-commercial implementation, and restricted/licensed data until IP review.

Do not claim patent pending unless an application has actually been filed. Do not fabricate DOI metadata. Preserve upstream licenses and third-party attribution.

## Candidate v0.3.0 release gate

Do not promote the next public release until Prototype 003 passes the frozen acceptance checks, IP/public-disclosure review, and clean-environment replication.

Until then, **v0.2.2 remains the current public release**.

## Canonical direction

**Models generate. Agents debate. Code tests. Evidence decides. Humans approve.**
