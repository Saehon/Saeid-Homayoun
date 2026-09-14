# NAAIL OpenLab™ — Current Project State

**Canonical public state date:** 2026-09-14  
**Public release:** v0.2.2  
**Executable milestone:** Audit Workspace V0.4 / Prototype 002  
**Next milestone:** Prototype 003

## Purpose

This file is the compact public state checkpoint for NAAIL OpenLab. It does not replace the README, architecture, evaluation, security, citation, or research-record files. It exists so collaborators can identify the current executable state and next research milestone without relying on chat history.

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

Prototype 002 adds:

- explicit Materiality and Risk roles;
- evidence-linked testing;
- Evidence Passport™;
- persistent Professional Decision DAG™;
- provider-neutral model-adapter contract;
- deterministic control adapter;
- frozen quality metrics;
- regression testing;
- mandatory Human Gate.

Canonical workflow:

**Client XYZ → Materiality → Risk → Evidence → Evidence Passport™ → Professional Judgment → Critic / Quality Review → Professional Decision DAG™ → Human Gate**

## Prototype 003

Prototype 003 should add frozen:

1. **Goodwill Impairment** case;
2. **ICFR Deficiency** case.

Revenue Recognition remains the first baseline.

The same frozen evidence and gold labels should be evaluated across:

1. deterministic baseline;
2. single-agent AI;
3. sequential-agent AI;
4. governed multi-agent AI.

All architectures must use the same case contract and evaluation contract. Provider/model adapters may not modify gold labels, bypass Evidence Passport™, bypass the Professional Decision DAG™, or self-approve material conclusions.

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
- human overrides.

## First empirical study

Primary research question:

**Does governed multi-agent audit orchestration improve evidence grounding and professional judgment relative to single-agent AI?**

The intended comparison is deterministic control vs single-agent AI vs sequential agents vs governed multi-agent AI, with human-only or human-led comparison where feasible.

## Scientific rule

**Models generate. Agents debate. Code tests. Evidence decides. Humans approve.**

No LLM output, model score, or statistically significant result is automatically treated as a scientific discovery.

## Public / private boundary

Public repositories contain research-safe documentation, synthetic demonstrations, selected reproducibility artifacts, citation metadata, evaluation principles, and non-sensitive code.

Patent-sensitive architecture, detailed orchestration, unpublished prompts/specifications, private benchmark logic, restricted data, pre-commercial product logic, and deeper provider/runtime implementation remain private until IP review.

NAAIL OpenLab is an independent research initiative. References to Google, Microsoft, OpenAI, Big Four firms, IFRS Foundation, PCAOB, or other organizations describe public patterns, standards, research context, or interoperability targets only and do not imply affiliation or endorsement.

## Canonical links

- NAAIL OpenLab: https://github.com/Saehon/Saeid-Homayoun/tree/main/NAAIL-OpenLab
- Prototype status: https://github.com/Saehon/Saeid-Homayoun/blob/main/NAAIL-OpenLab/PROTOTYPE_STATUS_V0.4.md
- Portfolio index: https://github.com/Saehon/Saeid-Homayoun/blob/main/GITHUB_PORTFOLIO_INDEX.md
- ORCID: https://orcid.org/0000-0002-2536-0446

GitHub remains the source of truth. Google Drive is maintained as a private mirror/archive unless explicitly changed.
