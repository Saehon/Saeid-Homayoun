# NAAIL OpenLab™ — Three-Company Prototype V1.3 / V1.3C Scientific Validation

**Date:** 2026-09-17  
**Maturity:** `RESEARCH_PROTOTYPE`  
**Companies:** Microsoft (`MSFT`) · Walmart (`WMT`) · JPMorgan Chase (`JPM`)  
**Architecture:** exactly **Stable Knowledge Core™ + Replaceable Technology Core™**. No third permanent core.

> **PATENT RIGHTS RESERVED — PATENT APPLICATION PREPARATION IN PROGRESS**

## Scientific objective

The current V1.3C validation question is not **which LLM provider is best**. It is whether the **NAAIL governance architecture itself improves professional accounting/auditing judgment when the underlying model, task and evidence are held constant**.

Provider identity is retained as a robustness/blocking factor rather than the scientific outcome.

## Frozen governance boundary

- exactly two permanent cores;
- 3 companies × 20 steps = 60 company-step states;
- failed, null, contradictory, blocked and sensitivity-dependent evidence is preserved;
- data availability ≠ execution;
- code existence ≠ execution;
- agent agreement ≠ verification;
- statistical significance ≠ scientific discovery;
- Human Gate requires real human review;
- Step 20 independent replication remains `REGISTERED_NOT_EXECUTED` until a separate reviewer/environment executes it;
- private benchmark prompts and Gold_Key remain outside public GitHub;
- patent-sensitive enabling internals remain private until filing review.

Canonical systems-thinking sequence:

`Stage 0 → 2A → 2B → 2C → 2D → 2E → 3A → 3B → 3C → 3D → 3E → 4A → 4B → 4C`

See `SYSTEMS_THINKING_EXECUTION_ROADMAP_V1_3.md`.

## Stage 0 — Governance lock

**Status:** complete as governance infrastructure. No scientific execution is inferred from design artifacts.

## Phase 1 — Reproducibility & factor falsification

The earlier V1.2 → V1.3 factor discrepancy was reconciled as `SUPPORTED_AFTER_CHALLENGE`: the V1.2 factor package reproduced, and the discrepancy was isolated to the HC3 p-value reference distribution rather than data, coefficient or standard-error differences.

Existing V1.3 evidence includes HC3/HAC(3) sensitivity, influence diagnostics, leave-one-month-out stability, factor robustness summaries, the reconciled clean replay, Human–AI pilot power grid and the 60-step scientific-status matrix.

These do not constitute independent replication or Phase 2 model validation.

## Stage 2A — Private blind benchmark packet

**Design outcome:** `REVISED_AFTER_CHALLENGE`  
**Scientific execution:** `REGISTERED_NOT_EXECUTED`

The original public 12-task packet is preserved as development/calibration only. A separate promotion-grade private V1.3B packet is frozen with:

- **21 tasks = 7 professional domains × 3 companies**;
- frozen task SHA-256: `2a0857f94beff1f4c6f25b76621bd0a1f02bb8272e7f1e68eacb6acd39146eaf`;
- frozen E1–E8 evidence SHA-256: `30cd72360b68d5f62f610e143aad712382edb201e972642c40b43c445061748e`;
- private prompts and Gold_Key excluded from public GitHub.

## Stage 2B — V1.3C architecture-effect design

**Conceptual design:** `REVISED_AFTER_CHALLENGE`  
**Architecture-effect design:** `FROZEN_DESIGN`  
**Scoring rubric:** `FROZEN_DESIGN`  
**Analysis pre-registration:** `FROZEN_DESIGN`  
**Scientific execution:** `REGISTERED_NOT_EXECUTED`

### Architecture conditions

- `A0` — Model + Frozen Evidence
- `A1` — Evidence Passport™
- `A2` — Full NAAIL Verify

Primary estimand:

`Δ_NAAIL = mean[OPQS(A2) − OPQS(A0)]`

Secondary estimands:

- `A1 − A0` — structured evidence-governance effect
- `A2 − A1` — incremental verification/falsification effect

### Provider robustness blocks

- C01 — OpenAI `gpt-6-astra`
- C02 — Google `gemini-3.8-flash`
- C03 — Anthropic `claude-fable-5`

Planned design:

**3 providers × 3 architecture conditions × 21 tasks = 189 blinded outputs**

Providers are not ranked as the scientific conclusion.

## Frozen primary outcome — OPQS

**Overall Professional Quality Score (OPQS), 0–100**

- professional correctness — 35%
- evidence grounding — 20%
- contradiction handling — 15%
- calibration / evidence sufficiency — 10%
- auditability / traceability — 10%
- professional decision usefulness — 10%

Separate verification telemetry is retained for reviewer time, corrections, rework, final verified-output status, escalation and remaining material-error status.

## Frozen confirmatory analysis

Primary comparison:

**A2 Full NAAIL Verify vs A0 Model + Frozen Evidence**

Primary practical-effect threshold:

`mean A2−A0 ≥ +5.0 OPQS points`

Primary uncertainty specification:

- task-cluster bootstrap 95% CI;
- 10,000 replications;
- fixed seed `20260917`;
- all provider observations retained within each resampled task cluster.

Only A2 vs A0 on OPQS is confirmatory. A1−A0, A2−A1 and all dimension/provider/company/domain analyses are secondary. Holm adjustment applies within secondary p-value families.

## Promotion guardrails

`SUPPORTED_AFTER_CHALLENGE` cannot be assigned from statistical significance alone. It requires:

1. mean A2−A0 OPQS improvement ≥ +5.0;
2. no >0.20 raw-point deterioration in grounding, contradiction handling or calibration;
3. positive mean A2−A0 effect in at least 2 of 3 providers;
4. positive mean A2−A0 effect in at least 2 of 3 companies;
5. no hidden increase in material professional errors;
6. prospective human verification evidence;
7. reviewer reliability/adjudication disclosure.

## Blinded professional review design

- minimum two independent professional reviewers per output;
- provider and architecture condition masked;
- opaque response and reviewer IDs;
- randomized review order;
- adjudication when OPQS disagreement >10 points or any dimension differs by ≥2 raw points;
- reliability calculated before condition labels are unblinded;
- system/API failures remain `FAILED_CALL` and are not imputed as quality scores;
- substantive model refusals are scored normally.

## Stage 2B execution infrastructure

The public execution controls remain available, but implementation plumbing is not the main scientific contribution.

Current infrastructure state:

- cross-candidate input lock: `EXECUTED_VALIDATED`;
- C01/C02/C03 structural preflights: `PASS`;
- SDK provenance: `EXECUTED_VALIDATED`;
- provider API contract verification: `EXECUTED_VALIDATED`;
- GitHub CI runtime validation: `BLOCKED_CI_RUN_NOT_OBSERVED`;
- live provider calls: `BLOCKED_PROVIDER_CREDENTIAL_AND_RUNTIME`.

No candidate response or score is claimed from these controls.

## Stage 2C–2E

Not executed.

Stage 2C scoring remains locked until the required architecture-condition responses are frozen and the blinding protocol is satisfied. Gold_Key scoring access remains `LOCKED`. Numeric Cost per Verified Professional Output™ remains `NOT_EXECUTED` until actual model cost, reviewer time and rework telemetry exist.

## Canonical V1.3C public records

Conceptual redesign:

- `STAGE2B_CONCEPTUAL_REDESIGN_ARCHITECTURE_EFFECT_V1_3C.md`
- `stage2b_architecture_effect_experiment_matrix_v1_3c.csv`
- `stage2b_architecture_effect_success_criteria_v1_3c.csv`
- `STAGE2B_CONCEPTUAL_REDESIGN_DUAL_SAVE_SYNC_2026_09_17.md`

Scoring and pre-registration:

- `STAGE2B_BLINDED_SCORING_RUBRIC_V1_3C.md`
- `STAGE2B_ARCHITECTURE_EFFECT_PREREGISTRATION_V1_3C.md`
- `stage2b_blinded_scoring_template_v1_3c.csv`
- `STAGE2B_SCORING_PREREG_DUAL_SAVE_SYNC_2026_09_17.md`

Consolidated state:

- `V1_3C_CONSOLIDATED_PUBLICATION_RECORD_2026_09_17.md`

Earlier Stage 2 controls and evidence remain preserved in this directory and are not overwritten by the V1.3C conceptual redesign.

## Current scientific state

- two-core architecture: frozen;
- 3-company × 20-step contract: frozen;
- architecture-effect design: frozen;
- OPQS rubric: frozen;
- primary estimand/inference: frozen;
- 189 blinded outputs: `REGISTERED_NOT_EXECUTED`;
- Gold_Key access: `LOCKED`;
- human verification: `NOT_EXECUTED`;
- numeric CVPO: `NOT_EXECUTED`;
- Stage 2C: `LOCKED`.

## Next conceptual gate

Freeze the **professional task-to-architecture intervention protocol**: exactly what A0, A1 and A2 may do in each of the seven professional domains while holding substantive evidence constant. This is required so any measured difference can be attributed to architecture rather than to extra information.
