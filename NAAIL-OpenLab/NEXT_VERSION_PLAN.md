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

Build a governed Audit Digital Twin benchmark in which every execution architecture receives the same frozen case definition, evidence, gold labels, materiality logic, evaluation contract, and Human Gate.

### Case families

1. **Revenue Recognition & Cut-off** — retain Prototype 002 as the frozen baseline.
2. **P003-C: SEC-Anchored Goodwill / Impairment** — use exactly three public-company evidence anchors:
   - Microsoft Corporation;
   - Alphabet Inc. (Google);
   - Amazon.com, Inc.
3. **ICFR Deficiency** — controlled controls-deficiency benchmark.

## Hard scope rule for Prototype 003-C

Prototype 003-C is restricted to exactly **Microsoft, Alphabet, and Amazon**. No fourth company may be added without an explicit versioned scope change.

The real-company evidence layer must use **SEC EDGAR / Form 10-K / iXBRL** only. The filings provide evidence anchors and accounting-disclosure inputs; they do not themselves constitute benchmark gold labels.

Controlled or synthetic transformations must be used to generate planted ambiguities/exceptions, scenario parameters, and frozen gold labels. These research scenarios must not be represented as real findings about Microsoft, Alphabet, or Amazon.

NAAIL must not infer or state unsupported claims of undisclosed impairment, audit failure, ICFR deficiency, or deficient audit quality for any of the three companies.

Canonical scope document: [PROTOTYPE_003C_SEC_SCOPE.md](./PROTOTYPE_003C_SEC_SCOPE.md)

### P003-C evidence pipeline

**SEC EDGAR → Form 10-K / iXBRL → source hash → normalized goodwill/intangible/acquisition evidence → Evidence Passport™ → controlled benchmark transformation → frozen gold labels → four-architecture comparison → Professional Decision DAG™ → Human Gate**

Normalized evidence should capture, where available and relevant:

- goodwill balances;
- goodwill and intangible-asset notes;
- acquisitions and purchase-price allocation;
- impairment accounting policies;
- segment/reporting-unit context;
- management estimates and uncertainty disclosures;
- valuation/cash-flow-related disclosures;
- related XBRL facts and filing metadata.

Every extracted evidence object should preserve issuer, accession/source reference, filing date, reporting period, concept/section, raw fact or text reference, normalized value/meaning, and source hash where feasible.

## Execution architectures

Run every frozen benchmark case through the same four architectures:

1. **Deterministic baseline**.
2. **Single-agent AI**.
3. **Sequential-agent AI**.
4. **Governed multi-agent AI**.

Where feasible, add a human-only or human-led comparison for empirical research.

Model/provider swaps must occur through a provider-neutral adapter contract and must not change the case, evidence, gold labels, evaluation logic, or governance requirements.

## Prototype 003 implementation order

1. Freeze a common Digital Twin case/evidence/gold/run-manifest schema.
2. Refactor the Revenue Recognition baseline into that schema without changing its gold labels.
3. Build the SEC ingestion and normalization layer for Microsoft, Alphabet, and Amazon only.
4. Freeze the P003-C controlled Goodwill / Impairment benchmark derived from that evidence layer.
5. Build and freeze the ICFR Deficiency controlled benchmark.
6. Implement the four runner contracts against identical case inputs.
7. Enforce Evidence Passport™, Professional Decision DAG™, and Human Gate outputs for every material run.
8. Implement one shared evaluation harness across all cases and architectures.
9. Add regression, deterministic replay, seed/re-run, leakage, provider-swap, and clean-environment reproducibility tests.
10. Run the complete benchmark matrix and preserve null, negative, failed, and contradictory results.
11. Export tidy, manuscript-ready outputs for statistical analysis and tables.

## Mandatory governance for every run

- Evidence Passport™.
- Professional Decision DAG™.
- Human Gate for material professional/scientific conclusions.
- Provider-neutral model/agent adapter contract.
- Frozen case hashes, gold labels, run manifests, and evaluation definitions.
- Traceable SEC evidence IDs and source references for P003-C.
- Model/adapter identity, limitations, and reproducibility metadata.
- Critic/reviewer output where an AI architecture is used.
- No self-certification of high-risk conclusions.
- No benchmark leakage or optimization for desired findings.
- No post-hoc mutation of gold labels based on model performance.

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

1. Revenue, P003-C, and ICFR benchmark cases are frozen, versioned, and hashable.
2. P003-C contains only Microsoft, Alphabet, and Amazon SEC evidence anchors.
3. P003-C source provenance is reproducible back to SEC EDGAR / 10-K / iXBRL.
4. All four architectures run against identical evidence and gold labels.
5. Every completed run emits a valid run manifest.
6. Evidence Passport™, Professional Decision DAG™, and Human Gate are present for every applicable run.
7. The evaluation harness calculates the same metric definitions across all architectures.
8. Regression and reproducibility tests pass on the frozen benchmark.
9. Re-running a frozen deterministic configuration reproduces the expected output exactly.
10. Stochastic/model runs preserve complete seed/model/provider/version metadata.
11. Benchmark leakage checks pass.
12. Outputs are exportable in tidy form for empirical analysis.
13. Public artifacts contain no restricted, licensed, patent-sensitive, or private implementation material.
14. A replication README can reproduce the public-safe benchmark from a clean environment.
15. Public text clearly separates real SEC evidence from controlled/synthetic benchmark findings.

## Manuscript-ready empirical package

The next version should produce one analysis-ready dataset with one row per case × architecture × run plus linked metric-level and evidence-level tables.

Minimum manuscript outputs:

- benchmark descriptive statistics;
- architecture-by-case performance table;
- SEC evidence-grounding table for P003-C;
- professional-judgment comparison table;
- reproducibility/stability table;
- latency/cost table;
- human-override summary;
- robustness/falsification outputs;
- machine-readable run manifest and case manifest.

## First empirical paper from the next version

**Research question:** Does governed multi-agent audit orchestration improve evidence grounding and professional judgment relative to single-agent AI?

Primary comparison groups: deterministic control, single-agent AI, sequential-agent AI, governed multi-agent AI, and human-led baseline where feasible.

No claim of superiority is assumed in advance. The empirical paper should use frozen hypotheses/outcomes where feasible, preserve null and negative results, use held-out evaluation, report model/provider versions and reproducibility metadata, and include robustness/falsification tests.

## Public / private boundary

Public release may include research-safe architecture, SEC-source references, controlled/synthetic benchmark cases, evaluation definitions, selected reproducibility artifacts, validated benchmark summaries, and replication instructions.

Private R&D must retain patent-sensitive orchestration, unpublished prompts/specifications, private benchmark-construction logic, detailed Control Plane logic, advanced evaluation logic, pre-commercial implementation, and restricted/licensed data until IP review.

Do not claim patent pending unless an application has actually been filed. Do not fabricate DOI metadata. Preserve upstream licenses and third-party attribution.

References to Microsoft, Alphabet/Google, Amazon, SEC, or any other organization describe public-source evidence or research context only and do not imply affiliation, endorsement, sponsorship, or certification.

## Candidate v0.3.0 release gate

Do not promote the next public release until Prototype 003 passes the frozen acceptance checks, IP/public-disclosure review, and clean-environment replication.

Until then, **v0.2.2 remains the current public release**.

## Canonical direction

**Models generate. Agents debate. Code tests. Evidence decides. Humans approve.**
