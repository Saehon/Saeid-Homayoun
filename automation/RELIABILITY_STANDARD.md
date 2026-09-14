# ECONOVA-S™ AI-to-AI Reliability Standard

This document defines the reliability controls for AI-to-AI scientific automation in ECONOVA-S™. The design follows research-engineering principles common in mature industrial research labs: explicit interfaces, isolation, observability, least privilege, deterministic evaluation, fault containment, reproducibility, and human oversight.

ECONOVA-S™ is an independent research project. This standard does not imply affiliation with Microsoft or any other organization.

## 1. Separation of scientific roles

Generation, theory mapping, empirical design, replication, red-team review, welfare interpretation, and evidence sealing are separate roles. A role change alone does not establish model independence; the runtime records the actual independence class.

## 2. Contract-only handoffs

Agents communicate through machine-readable handoffs rather than hidden reasoning. Each handoff records claim, evidence, method, assumptions, confidence, contradictions, failure state, provenance, next action, parent hash, and content hash.

## 3. Tamper-evident chain

Each handoff hashes its canonical content and points to the previous handoff hash. The full run receives a chain hash. A modified intermediate record invalidates downstream chain validation.

## 4. Failure containment

Blocking failures stop downstream automation. Current stop classes include:

- missing evidence;
- provenance failure;
- chronology/leakage failure;
- invalid construct;
- invalid identification;
- replication failure;
- unresolved red-team contradiction;
- materially incomplete welfare analysis when required.

Failure is a valid scientific output and must not be silently converted into a successful run.

## 5. Independence classes

The runtime records whether a stage is:

- `role_independent_only`; or
- `role_and_tool_independent`.

For publication-grade replication, the target is stronger than role separation: isolated context plus an independently configured model/tool or execution path, and where feasible independent data/code reconstruction.

## 6. Least privilege

Public CI validates orchestration with a deterministic offline adapter and no secrets. Live model credentials belong only in explicitly authorized environments. Scientific governance must not depend on repository write permissions or model-provider credentials.

## 7. Deterministic evaluation before live models

The deterministic demo validates:

- role routing;
- handoff schema;
- hash continuity;
- stop conditions;
- failure propagation;
- Human Gate requirement;
- discovery-claim prohibition.

Passing these tests validates orchestration mechanics only, not scientific truth.

## 8. Observability

Every run should expose:

- run ID and task ID;
- stage sequence;
- model/tool and version;
- confidence and contradictions;
- failure reasons and risk flags;
- parent/content hashes;
- final chain hash;
- Human Gate state.

## 9. Scientific safety invariants

The following invariants are non-bypassable in the public automation layer:

`agent_consensus_is_scientific_truth = false`

`human_gate_required = true`

`human_gate_approved = false` by default

`discovery_claim_allowed = false`

No autonomous agent may change these invariants.

## 10. Live-model promotion gate

A live multi-model implementation should not be promoted from experimental to canonical until it demonstrates:

1. reproducible orchestration under frozen inputs;
2. stable failure handling;
3. independent reconstruction by the Replicator role;
4. red-team disagreement preservation;
5. provenance completeness;
6. no secret exposure in logs/artifacts;
7. human review of the Evidence Passport;
8. benchmarked performance against a deterministic or human gold set.

## Engineering rule

> **Automate execution, not scientific authority.**

The runtime may coordinate, challenge, replicate, and stop. Only governed evidence plus human judgment can authorize scientific progression.
