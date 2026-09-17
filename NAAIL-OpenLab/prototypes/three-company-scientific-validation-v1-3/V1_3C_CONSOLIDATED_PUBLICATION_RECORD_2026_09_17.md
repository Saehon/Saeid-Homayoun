# NAAIL OpenLab™ — V1.3C Consolidated Publication Record

**Date:** 2026-09-17  
**Project:** NAAIL OpenLab™ — V2026.3 Multi-Agent Digital Twin  
**Prototype:** Three-Company Scientific Validation V1.3C  
**Architecture:** exactly two permanent cores — **Stable Knowledge Core™ + Replaceable Technology Core™**  
**Maturity:** `RESEARCH_PROTOTYPE`  
**Patent notice:** **PATENT RIGHTS RESERVED — PATENT APPLICATION PREPARATION IN PROGRESS**

## 1. Main conceptual decision

V1.3C reframes the core validation question. The principal question is **not which AI provider performs best**. The principal question is whether the **NAAIL governance architecture itself improves professional accounting/auditing judgment when the underlying model, task and evidence are held constant**.

Providers are retained only as robustness/blocking factors.

## 2. Architecture-effect design

Three architecture conditions are frozen:

- `A0` — Model + Frozen Evidence
- `A1` — Evidence Passport™
- `A2` — Full NAAIL Verify

Primary estimand:

`Δ_NAAIL = mean[OPQS(A2) − OPQS(A0)]`

Secondary estimands:

- `A1 − A0` — structured evidence-governance effect
- `A2 − A1` — incremental verification/falsification effect

The three registered provider blocks are:

- C01 — OpenAI `gpt-6-astra`
- C02 — Google `gemini-3.8-flash`
- C03 — Anthropic `claude-fable-5`

Planned design:

`3 providers × 3 architecture conditions × 21 tasks = 189 blinded outputs`

The 21 tasks remain the private V1.3B packet spanning seven professional domains across Microsoft, Walmart and JPMorgan Chase.

## 3. Frozen primary outcome

The confirmatory outcome is **Overall Professional Quality Score (OPQS), 0–100**.

Weights:

- Professional correctness — 35%
- Evidence grounding — 20%
- Contradiction handling — 15%
- Calibration / evidence sufficiency — 10%
- Auditability / traceability — 10%
- Professional decision usefulness — 10%

Separate prospective verification telemetry is retained for reviewer time, correction count, rework time, final verified-output status, escalation and remaining material-error status.

## 4. Frozen confirmatory analysis

Primary contrast:

`A2 Full NAAIL Verify vs A0 Model + Frozen Evidence`

Primary practical-effect threshold:

`mean A2−A0 ≥ +5.0 OPQS points`

Primary uncertainty specification:

- task-cluster bootstrap 95% confidence interval;
- 10,000 replications;
- fixed seed `20260917`;
- all provider observations retained within each resampled task cluster.

Only A2 vs A0 on OPQS is confirmatory. A1−A0, A2−A1, dimension-level effects, provider heterogeneity, company heterogeneity and domain heterogeneity are secondary. Holm adjustment applies within secondary p-value families.

## 5. Promotion guardrails

`SUPPORTED_AFTER_CHALLENGE` cannot be assigned from statistical significance alone. Promotion requires all of the following:

1. mean A2−A0 OPQS improvement of at least +5.0 points;
2. no mean deterioration greater than 0.20 raw scale points in grounding, contradiction handling or calibration;
3. positive mean A2−A0 effect in at least 2 of 3 provider blocks;
4. positive mean A2−A0 effect in at least 2 of 3 companies;
5. no hidden increase in material professional errors;
6. prospective human verification evidence;
7. reviewer reliability and adjudication disclosure.

## 6. Blinded reviewer protocol

- minimum two independent professional reviewers per output;
- provider identity masked;
- architecture condition masked;
- opaque response IDs and reviewer IDs;
- randomized review order;
- adjudication when OPQS disagreement exceeds 10 points or any dimension differs by at least 2 raw points;
- reviewer reliability calculated before unblinding condition labels.

System/API failures remain `FAILED_CALL` and are not imputed as quality scores. Substantive model refusals remain reviewable outputs and are scored normally.

## 7. Canonical Google Drive V1.3C records

Canonical V1.3 folder: `1x7BrFxvVJ-j2R_YZ80Tw36vGhjCugUDM`

Native Docs:

- **NAAIL V1.3C — Architecture-Effect Conceptual Redesign** — `1AQpnK4fx_Av-qo6V37h8k4xelTqPQKNIF0i0Gm4rR_g`
- **NAAIL V1.3C — Blinded Professional Scoring Rubric** — `1-Zqxde_VmZ9dofiKcvl8Q9XppZBSqeSBdSHqrcjkXzA`
- **NAAIL V1.3C — Architecture-Effect Analysis Pre-Registration** — `15EMbR7ipuxYQ2Zx7q5BPSgiESinaX6X6ihdLYi510ow`
- **NAAIL V1.3C — Conceptual Redesign Dual-Save Sync** — `1KJbEX0Md5e-BpytdOo4BkZmyzlXcHn5utnKKOVEt-ew`
- **NAAIL V1.3C — Scoring & Pre-Registration Dual-Save Sync** — `1149LMS0D_fTQ_qREpb-SprfUmg4oGiaDJ8INLng7T84`

Native Sheet:

- **NAAIL V1.3C — Architecture-Effect Experiment Matrix** — `1JJNI8WdHb2vYPFX0MOtLzkOIL0XrVzOGLfex-zL4utA`

Tabs:

- `Experiment_Matrix`
- `Success_Criteria`
- `Rubric_Weights`
- `PreReg_Summary`
- `Scoring_Template`

## 8. Public GitHub V1.3C records

Repository: `Saehon/Saeid-Homayoun`  
Branch: `main`  
Directory: `NAAIL-OpenLab/prototypes/three-company-scientific-validation-v1-3/`

Conceptual redesign:

- `STAGE2B_CONCEPTUAL_REDESIGN_ARCHITECTURE_EFFECT_V1_3C.md` — commit `908e29e3f1f7d3a38fcfa5c6bc2539a9090a4d1d`
- `stage2b_architecture_effect_experiment_matrix_v1_3c.csv` — commit `ccfefe46215f60fc7bbb68cb80ce484e0e24acde`
- `stage2b_architecture_effect_success_criteria_v1_3c.csv` — commit `fed0e7813cdff02f796a81d1b5f70f9c106a7324`
- `STAGE2B_CONCEPTUAL_REDESIGN_DUAL_SAVE_SYNC_2026_09_17.md` — commit `e8f4d9941f2194982c0f473d1be1d91df80f5b70`

Scoring and preregistration:

- `STAGE2B_BLINDED_SCORING_RUBRIC_V1_3C.md` — commit `bb7f4d060d1a24e65567c8b8a5424ffe3c7bbdbd`
- `STAGE2B_ARCHITECTURE_EFFECT_PREREGISTRATION_V1_3C.md` — commit `b227f5a974e915d741d50d11da2d7f87542eba46`
- `stage2b_blinded_scoring_template_v1_3c.csv` — commit `fee0cbbe1bc9899825208b45d01a97fdb0c89103`
- `STAGE2B_SCORING_PREREG_DUAL_SAVE_SYNC_2026_09_17.md` — commit `5c64a67a8ddf3ae08ea4370fc54757d322ced8cf`

## 9. Preserved governance boundary

V1.3C does not alter the constitutional architecture or scientific-status rules:

- exactly two permanent cores;
- 3 companies × 20 steps = 60 company-step states;
- failed, null, contradictory, blocked and sensitivity-dependent evidence must be preserved;
- Human Gate requires actual human review;
- independent replication remains unexecuted until a separate reviewer/environment executes it;
- private prompts and Gold_Key remain outside public GitHub;
- patent-sensitive enabling internals remain private until filing review;
- data availability ≠ execution;
- code existence ≠ execution;
- agent agreement ≠ verification;
- statistical significance ≠ scientific discovery.

## 10. Current scientific state

- conceptual design: `REVISED_AFTER_CHALLENGE`
- architecture-effect experiment design: `FROZEN_DESIGN`
- scoring rubric: `FROZEN_DESIGN`
- analysis pre-registration: `FROZEN_DESIGN`
- 189 architecture-condition outputs: `REGISTERED_NOT_EXECUTED`
- Gold_Key scoring access: `LOCKED`
- human verification: `NOT_EXECUTED`
- numeric CVPO: `NOT_EXECUTED`
- Stage 2C: `LOCKED`

## 11. Next conceptual gate

Before any 189-output execution, freeze the **professional task-to-architecture intervention protocol**. This must specify exactly what A0, A1 and A2 are allowed to do in each of the seven professional domains while holding substantive evidence constant, so that the measured difference is attributable to architecture rather than to extra information.
