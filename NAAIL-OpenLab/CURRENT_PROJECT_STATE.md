# NAAIL OpenLab™ — Current Project State

**Canonical public state date:** 2026-09-14  
**Public release:** v0.2.2  
**Executable milestone:** Audit Workspace V0.4 / Prototype 002  
**Next executable milestone:** Prototype 003  
**Candidate next release:** v0.3.0 only after release gates pass

## Purpose

This file is the compact public state checkpoint for NAAIL OpenLab. It exists so collaborators can identify the current executable state and next research milestone without relying on chat history.

## Current validated synthetic baseline

Case: **Client XYZ — Revenue Recognition & Cut-off**.

Frozen deterministic control result:

- planted exceptions: `TX-002`, `TX-003`;
- proposed adjustment: EUR 190,000;
- planning materiality: EUR 120,000;
- precision: 1.00;
- recall: 1.00;
- false positives: 0;
- false negatives: 0;
- final state: `PENDING_HUMAN_APPROVAL`;
- Prototype 002 regression tests: 5/5 passed.

These results apply only to the frozen synthetic benchmark and are not claims of real-world audit effectiveness or professional assurance.

## Prototype 002 capabilities

Prototype 002 includes explicit Materiality and Risk roles, evidence-linked testing, Evidence Passport™, a persistent Professional Decision DAG™, provider-neutral model adapters, frozen quality metrics, regression testing, and a mandatory Human Gate.

Canonical workflow:

**Client XYZ → Materiality → Risk → Evidence → Evidence Passport™ → Professional Judgment → Critic / Quality Review → Professional Decision DAG™ → Human Gate**

## Prototype 003 — execution-ready program

Prototype 003 converts the current single-case baseline into a controlled **multi-case × multi-architecture benchmark**.

### Case families

1. **Revenue Recognition & Cut-off** — retained Prototype 002 frozen baseline.
2. **P003-C: SEC-Anchored Goodwill / Impairment** — restricted to exactly three public-company evidence anchors:
   - Microsoft Corporation;
   - Alphabet Inc. (Google);
   - Amazon.com, Inc.
3. **ICFR Deficiency** — controlled controls-deficiency benchmark.

### Hard scope rule for P003-C

P003-C may use only **SEC EDGAR / Form 10-K / iXBRL** as the real-company evidence layer. No fourth company may be added without an explicit, versioned scope change.

The three companies are evidence anchors only. Controlled or synthetic transformations create benchmark scenarios, planted ambiguities/exceptions, and frozen gold labels. NAAIL must not convert those benchmark scenarios into unsupported claims that Microsoft, Alphabet, or Amazon has an undisclosed goodwill impairment, audit failure, ICFR deficiency, or deficient audit quality.

Canonical P003-C scope: [PROTOTYPE_003C_SEC_SCOPE.md](./PROTOTYPE_003C_SEC_SCOPE.md)

### P003-C evidence pipeline

**SEC EDGAR → 10-K / iXBRL → source hash → normalized accounting evidence → Evidence Passport™ → controlled research scenario → frozen gold labels → architecture comparison → Professional Decision DAG™ → Human Gate**

Target normalized evidence includes, where available and relevant, goodwill balances, goodwill/intangible notes, acquisitions and purchase-price allocation, impairment-policy disclosures, segment/reporting-unit context, management estimates and uncertainty disclosures, cash-flow/valuation-relevant disclosures, and related XBRL facts.

### Execution architectures

1. deterministic baseline;
2. single-agent AI;
3. sequential-agent AI;
4. governed multi-agent AI.

A human-only or human-led comparison may be added where feasible.

### Experimental invariant

**Same case. Same evidence. Same frozen gold labels. Same evaluator. Different execution architecture.**

Provider/model adapters may not modify gold labels, bypass Evidence Passport™, bypass the Professional Decision DAG™, bypass Human Gate, or silently change the evaluation contract.

### P003 work packages

- `P003-A` — common case/evidence/gold/run-manifest contracts;
- `P003-B` — Revenue baseline migration;
- `P003-C` — SEC-anchored Goodwill / Impairment benchmark using Microsoft, Alphabet, and Amazon only;
- `P003-D` — ICFR Deficiency case;
- `P003-E` — four runner contracts;
- `P003-F` — governance artifacts;
- `P003-G` — frozen evaluator;
- `P003-H` — regression, leakage, replay, provider-swap, and clean-environment reproducibility tests;
- `P003-I` — full case × architecture benchmark matrix;
- `P003-J` — manuscript-ready empirical export.

## Evaluation contract

Track at minimum:

- RPA — Risk–Procedure Alignment;
- AA — Assertion Alignment;
- EG — Evidence Grounding;
- PS — Professional Skepticism;
- DS — Documentation Sufficiency;
- DIST — Decision/Inference Stability;
- precision/recall;
- false positives/negatives;
- reproducibility;
- evidence/citation traceability;
- completion time;
- cost and latency;
- human overrides and reasons.

Development, validation, Blind Gold, adversarial/red-team, and temporal/modified-scenario holdouts remain separated.

## Manuscript-ready outputs

Prototype 003 is designed to export linked empirical tables including `CASE_MANIFEST`, `RUN_LEVEL`, `METRIC_LEVEL`, `EVIDENCE_LEVEL`, `DECISION_LEVEL`, `HUMAN_GATE_LEVEL`, and `FAILURE_LOG`.

## First empirical study

Primary research question:

**Does governed multi-agent audit orchestration improve evidence grounding and professional judgment relative to single-agent AI?**

The intended comparison is deterministic control vs single-agent AI vs sequential agents vs governed multi-agent AI, with a human-only or human-led comparison where feasible.

No superiority claim is assumed in advance. The benchmark is designed to test the question under frozen conditions.

## Candidate v0.3.0 promotion rule

Do not promote v0.3.0 until the benchmark cases are frozen/versioned/hashable; all four architectures run under identical evidence/gold/evaluation conditions; run manifests are complete; Evidence Passport™, Professional Decision DAG™, and Human Gate are enforced; regression/leakage/reproducibility tests pass; clean-environment replication succeeds; empirical outputs can be regenerated; and public artifacts pass rights, privacy, and IP review.

Until those gates pass, **v0.2.2 remains the current public release**.

## Scientific rule

**Models generate. Agents debate. Code tests. Evidence decides. Humans approve.**

No LLM output, model score, agent consensus, or statistically significant result is automatically treated as a scientific discovery.

## Public / private boundary

Public repositories contain research-safe documentation, SEC-source references, controlled/synthetic demonstrations, selected reproducibility artifacts, citation metadata, evaluation principles, and non-sensitive code.

Patent-sensitive architecture, detailed orchestration, unpublished prompts/specifications, private benchmark logic, restricted data, pre-commercial product logic, and deeper provider/runtime implementation remain private until IP review.

NAAIL OpenLab is an independent research initiative. References to Microsoft, Alphabet/Google, Amazon, SEC, OpenAI, Big Four firms, IFRS Foundation, PCAOB, or other organizations describe public evidence, public patterns, standards, research context, or interoperability targets only and do not imply affiliation or endorsement.

## Canonical links

- NAAIL OpenLab: https://github.com/Saehon/Saeid-Homayoun/tree/main/NAAIL-OpenLab
- Current state: https://github.com/Saehon/Saeid-Homayoun/blob/main/NAAIL-OpenLab/CURRENT_PROJECT_STATE.md
- Prototype status: https://github.com/Saehon/Saeid-Homayoun/blob/main/NAAIL-OpenLab/PROTOTYPE_STATUS_V0.4.md
- Next-version plan: https://github.com/Saehon/Saeid-Homayoun/blob/main/NAAIL-OpenLab/NEXT_VERSION_PLAN.md
- Prototype 003 execution spec: https://github.com/Saehon/Saeid-Homayoun/blob/main/NAAIL-OpenLab/PROTOTYPE_003_EXECUTION_SPEC.md
- Prototype 003-C SEC scope: https://github.com/Saehon/Saeid-Homayoun/blob/main/NAAIL-OpenLab/PROTOTYPE_003C_SEC_SCOPE.md
- Execution tracker: https://github.com/Saehon/Saeid-Homayoun/issues/18
- Portfolio index: https://github.com/Saehon/Saeid-Homayoun/blob/main/GITHUB_PORTFOLIO_INDEX.md
- ORCID: https://orcid.org/0000-0002-2536-0446

GitHub remains the source of truth. Google Drive is maintained as a private mirror/archive unless explicitly changed.
