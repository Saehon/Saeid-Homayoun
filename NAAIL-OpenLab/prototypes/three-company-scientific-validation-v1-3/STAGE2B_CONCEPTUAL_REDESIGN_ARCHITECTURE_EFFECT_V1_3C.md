# NAAIL OpenLab™ — Stage 2B Conceptual Redesign: Architecture-Effect Validation V1.3C

**Date:** 2026-09-17  
**Design decision:** `REVISED_AFTER_CHALLENGE`  
**Scientific execution:** `REGISTERED_NOT_EXECUTED`  
**Stage 2C scoring:** `LOCKED`

## Why this redesign is necessary

A three-provider tournament can show that models differ. It does **not** establish that NAAIL itself adds professional value. The central scientific claim of NAAIL is architectural: verified professional judgment should improve because evidence, accounting/auditing knowledge, contradiction handling, falsification, decision structure, and human-governance controls are organized systematically around the model.

Therefore, provider identity is moved from the primary scientific question to a **blocking/robustness factor**. The primary treatment is the NAAIL governance architecture.

## Primary research question

> **Does the NAAIL OpenLab™ governance architecture improve the quality, verifiability, calibration, and auditability of professional accounting/auditing judgments beyond the same underlying model using the same frozen evidence without the NAAIL governance layer?**

This is the main concept that V1.3C is designed to test.

## Frozen architecture

The constitutional architecture remains unchanged:

1. **Stable Knowledge Core™**
2. **Replaceable Technology Core™**

No third permanent core is introduced.

Canonical professional flow:

`Stable Knowledge → Frozen Evidence → Replaceable Model → Evidence Passport™ → Assertion / Risk Mapping → Professional Decision DAG™ → Contradiction & Falsification → Verification → Human-Review-Ready Output`

## Experimental design

The existing private V1.3B benchmark remains the task base:

- 21 private tasks
- 7 professional domains
- 3 companies: Microsoft, Walmart, JPMorgan Chase
- same frozen task hash and same frozen E1–E8 evidence hash
- private gold key remains unavailable during generation

### Three architecture conditions

#### A0 — Model + Frozen Evidence

The model receives the benchmark task and the identical frozen evidence packet. It receives no NAAIL-specific structuring beyond the closed-evidence instruction.

Purpose: establish the same-evidence model baseline.

#### A1 — Evidence Passport™ Condition

The same model and evidence are used, but the response must first structure the evidence into an Evidence Passport™ containing claim/evidence mapping, source identity, uncertainty, missing evidence, and contradiction flags.

Purpose: isolate the incremental effect of structured evidence governance.

#### A2 — Full NAAIL Verify Condition

The same model and evidence are used through the full governed professional reasoning chain:

`Evidence Passport™ → accounting/audit assertion mapping → Professional Decision DAG™ → contradiction check → adversarial/falsification challenge → verifier → human-review-ready conclusion`

Purpose: estimate the incremental effect of the complete NAAIL verification architecture.

Human approval is **not simulated**. Actual Human Gate decisions remain separate and require real human review.

## Cross-provider robustness design

The three registered providers remain useful, but as robustness blocks rather than a winner-take-all comparison:

- C01 — OpenAI `gpt-6-astra`
- C02 — Google `gemini-3.8-flash`
- C03 — Anthropic `claude-fable-5`

Each provider should complete all three architecture conditions on the same 21 tasks.

Planned output count:

`3 providers × 3 architecture conditions × 21 tasks = 189 blinded outputs`

This paired design allows the architecture effect to be estimated **within the same provider and task**, reducing confounding from provider strength and task difficulty.

## Primary and secondary estimands

### Primary estimand

`Δ Full NAAIL = Score(A2) − Score(A0)` within the same provider-task pair.

This is the principal test of whether NAAIL adds value beyond access to the same model and evidence.

### Secondary estimands

- `Δ Evidence Governance = Score(A1) − Score(A0)`
- `Δ Verification Layer = Score(A2) − Score(A1)`
- provider × architecture interaction
- company × architecture interaction
- professional-domain × architecture interaction

Provider rankings are not the scientific objective.

## Blinded professional outcome dimensions

The output scorer should not know provider or architecture condition. Core outcome dimensions are:

1. professional correctness / decision validity;
2. evidence grounding and traceability;
3. contradiction detection and handling;
4. accounting/audit assertion specificity;
5. uncertainty and `REQUEST_MORE_EVIDENCE` calibration;
6. explanation quality and decision auditability;
7. reproducibility of the evidence-to-judgment path;
8. latency, token use, API cost, reviewer time, and rework;
9. final verified-output status for Cost per Verified Professional Output™.

## Conceptual success rule

NAAIL is not promoted because one provider wins, because outputs sound better, or because a single p-value is significant.

Architecture-effect evidence should be considered supportive only when all of the following are satisfied:

- A2 improves the paired professional-quality outcome relative to A0 under a pre-specified scoring model;
- the direction of improvement is not driven by one provider, one company, or one professional domain;
- evidence grounding and contradiction handling do not materially deteriorate;
- nulls, refusals, failures, and `REQUEST_MORE_EVIDENCE` decisions are preserved;
- human blinded review is completed prospectively;
- cost/reviewer-time trade-offs are disclosed rather than hidden;
- practical-effect thresholds are frozen before the main scoring analysis, not selected after seeing results.

## Recommended empirical model

Use the paired structure rather than treating the 189 outputs as independent model observations. A suitable specification is:

`ProfessionalScore = β1 A1 + β2 A2 + Provider FE + Task FE + error`

with clustered or paired inference at the task level as appropriate. Additional models can test architecture interactions by professional domain and company.

The precise inferential specification must be frozen before the gold key is used for scoring.

## What this redesign changes

- The **main concept** becomes the effect of NAAIL governance architecture.
- The three AI providers become robustness blocks.
- The existing 21 private tasks remain valid.
- The existing input hashes remain valid.
- The gold key remains private.
- The technical SDK/runtime work becomes implementation infrastructure, not the scientific centerpiece.
- Stage 2C remains locked until real outputs exist.

## Scientific boundary

This document is a conceptual and experimental-design upgrade. It does not claim that NAAIL improves outcomes, does not execute the 189 outputs, does not score any model, and does not open the Human Gate.

**Current state:** design `REVISED_AFTER_CHALLENGE`; execution `REGISTERED_NOT_EXECUTED`.
