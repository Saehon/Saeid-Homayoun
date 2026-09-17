# NAAIL V1.3C — TEST 001A
## XYZ-CH02 Gold Benchmark v1.0 — Freeze & Leakage Gate

**Status:** GOLD_FREEZE_PROTOCOL_ESTABLISHED / BLIND_EXECUTION_PENDING  
**Date:** 2026-09-17  
**Case:** XYZ-CH02 — *The Last Week of the Quarter*  
**Authors' case status:** `AUTHOR_FINALIZED` for book publication, as confirmed by Saeid Homayoun on behalf of the authors Saeid Homayoun and Zabihollah Rezaee.

## 1. Purpose

TEST 001A converts the author-finalized Chapter 2 case into a controlled NAAIL benchmark without publicly disclosing the protected instructor solution, private regulatory crosswalk, hidden outcome evidence or other answer-key material.

This gate must precede the 20-run A0–A3 architecture experiment.

## 2. Gold Benchmark v1.0 definition

The protected Gold Benchmark is the exact author-finalized Chapter 2 instructor/research solution and associated expert judgment boundaries used for book publication, plus a frozen evaluation rubric and evidence mapping.

The public repository records only the benchmark contract and status. The protected Gold content itself must remain in controlled private storage.

### Gold package components

- author-finalized instructor/research solution;
- professional problem definition;
- expected evidence classifications;
- JE-1 / JE-2 / JE-3 professional-priority boundaries;
- C-01 / C-02 / C-03 / C-04 control interpretations;
- competing-hypothesis interpretation and acceptable uncertainty;
- expected corroborating procedures;
- causal-claim boundary;
- detection-lead-time evaluation logic;
- acceptable alternative explanations;
- final professional-judgment boundaries;
- private historical/regulatory crosswalk where applicable;
- scoring rubric and adjudication rules.

## 3. Gold is not a forced answer

The benchmark must not reward a simplistic fraud/no-fraud conclusion. The finalized Chapter 2 design explicitly preserves benign, operational, control-risk, disclosure-risk and higher-intent explanations and requires evidence-sensitive updating.

The Gold Benchmark therefore evaluates professional reasoning, evidence discipline and calibrated judgment—not word-for-word agreement with an instructor narrative.

## 4. Freeze record

**Benchmark ID:** `NAAIL-V1.3C-XYZ-CH02-GOLD-v1.0`  
**Case status:** `AUTHOR_FINALIZED`  
**Gold status:** `GOLD_CONTENT_IDENTIFIED — IMMUTABLE HASH PENDING PRIVATE ARTIFACT FREEZE`  
**Public disclosure:** PROHIBITED for protected answer/crosswalk content  
**Human Gate:** Saeid Homayoun + Zabihollah Rezaee  
**Architecture visibility:** NONE

An immutable cryptographic hash must be calculated from the exact private Gold package bytes before the first blind architecture run. That hash—not the protected content—may be entered in the public run registry.

## 5. Blind Test Packet

A separate test packet must contain only information permitted to the architecture at the relevant T0–T6 cutoff.

It must exclude:

- instructor solution;
- compact model solution;
- expected hypothesis ordering;
- private regulatory/historical identity crosswalk;
- future-period evidence before its release point;
- realized outcome before final reveal;
- grading annotations that reveal the answer;
- Human Gate scores/rationales;
- prior A0/A1/A2/A3 outputs.

## 6. Leakage checks

Before execution, verify:

- no protected answer text is embedded in the test packet;
- no filename/path/metadata reveals the hidden answer or real-case identity;
- retrieval indexes used by tested architectures exclude the Gold Vault;
- RAG/GraphRAG/KAG corpora exclude protected gold material;
- prompts do not contain instructor conclusions;
- caches/memory/state do not expose prior solution content;
- architecture arms cannot read one another's outputs;
- T0–T6 chronological cutoffs are enforced;
- evaluator-only fields are inaccessible during generation.

**Leakage result:** `NOT YET MACHINE-VERIFIED`.

This status is intentionally conservative. Author finalization establishes the substantive benchmark source but does not by itself prove technical isolation of the execution environment.

## 7. Human Gate declaration

The authors' finalization of Chapters 2–15 is recognized in NAAIL as:

`AUTHOR_FINALIZED`

It is distinct from:

- `BLIND_TEST_READY` — requires technical leakage verification;
- `EXECUTED` — requires actual architecture runs;
- `HUMAN_GATE_EVALUATED` — requires scoring of blinded outputs;
- `INDEPENDENTLY_REPLICATED` — requires independent reproduction;
- `EXECUTED_VALIDATED` — requires the complete validation gate.

## 8. TEST 001B authorization condition

The 20-run experiment may start after all of the following are recorded:

1. exact private Gold package selected;
2. Gold package cryptographic hash recorded;
3. Blind Test Packet generated from the author-finalized case;
4. protected answer material removed from the test packet;
5. retrieval/index isolation verified;
6. T0–T6 information-cutoff test passes;
7. task contract frozen;
8. runtime/model configuration frozen for the initial comparison.

Then status advances to:

`GOLD_FROZEN → BLIND_TEST_READY → TEST 001B EXECUTION`

## 9. TEST 001B experiment

The authorized design is:

- A0 deterministic × 5 runs
- A1 single agent × 5 runs
- A2 sequential agents × 5 runs
- A3 governed NAAIL × 5 runs

Total primary runs: **20**.

No architecture is assumed to win. Null, negative, failed and contradictory outcomes must be retained.

## 10. Scientific integrity rule

**Author-finalized case ≠ architecture validation.**  
**Gold Benchmark ≠ model training data.**  
**Human Gate ≠ permission to leak the answer.**  
**Design artifact ≠ executed result.**

The purpose of TEST 001A is to protect the validity of TEST 001B.
