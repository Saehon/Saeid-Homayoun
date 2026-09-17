# NAAIL OpenLab™ — Stage 2B V1.3C Scoring & Pre-Registration Dual-Save Sync

**Date:** 2026-09-17  
**Conceptual design:** `REVISED_AFTER_CHALLENGE`  
**Scoring rubric:** `FROZEN_DESIGN`  
**Analysis pre-registration:** `FROZEN_DESIGN`  
**Scientific execution:** `REGISTERED_NOT_EXECUTED`  
**Gold_Key scoring access:** `LOCKED`  
**Stage 2C:** `LOCKED`

## Main scientific question

The primary scientific question is whether the **NAAIL governance architecture itself** improves professional accounting/auditing judgment when model, task and evidence are held constant.

Architecture conditions:
- `A0` — Model + Frozen Evidence
- `A1` — Evidence Passport™
- `A2` — Full NAAIL Verify

Providers remain robustness/blocking factors rather than the scientific outcome.

Planned design: `3 providers × 3 conditions × 21 tasks = 189 blinded outputs`.

## Frozen primary outcome

**Overall Professional Quality Score (OPQS), 0–100**

Weights:
- professional correctness — 35%
- evidence grounding — 20%
- contradiction handling — 15%
- calibration/evidence sufficiency — 10%
- auditability/traceability — 10%
- professional decision usefulness — 10%

Separate verification telemetry is retained for reviewer time, corrections, rework, final verification, escalation and material-error status.

## Frozen primary estimand and inference

Primary contrast:

`Δ_NAAIL = mean[OPQS(A2) − OPQS(A0)]`

across the 63 provider-task pairs.

Primary practical-effect threshold:

`mean A2−A0 ≥ +5.0 OPQS points`.

Primary uncertainty:
- task-cluster bootstrap 95% CI;
- 10,000 replications;
- fixed seed `20260917`;
- all provider observations retained within resampled task IDs.

The only confirmatory contrast is A2 vs A0 on OPQS. A1−A0, A2−A1 and dimension analyses are secondary; Holm adjustment applies within secondary p-value families.

## Frozen promotion guardrails

`SUPPORTED_AFTER_CHALLENGE` cannot be assigned from statistical significance alone. It requires:

1. mean A2−A0 OPQS improvement ≥ +5.0;
2. no >0.20 raw-point deterioration in grounding, contradiction handling or calibration;
3. positive mean A2−A0 effect in at least 2 of 3 providers;
4. positive mean A2−A0 effect in at least 2 of 3 companies;
5. no hidden increase in material professional errors;
6. prospective human verification evidence;
7. reviewer reliability/adjudication disclosure.

## Blinded reviewer design

- minimum 2 independent professional reviewers per output;
- provider and architecture condition masked;
- opaque response/review IDs;
- randomized review order;
- adjudication if OPQS disagreement >10 points or any dimension differs by ≥2 raw points;
- reliability calculated before condition labels are unblinded.

System/API failures remain `FAILED_CALL` and are not imputed as quality scores. Model refusals are substantive responses and are scored normally.

## GitHub public publications

Repository: `Saehon/Saeid-Homayoun`  
Branch: `main`

- `STAGE2B_BLINDED_SCORING_RUBRIC_V1_3C.md`
  - commit `bb7f4d060d1a24e65567c8b8a5424ffe3c7bbdbd`
- `STAGE2B_ARCHITECTURE_EFFECT_PREREGISTRATION_V1_3C.md`
  - commit `b227f5a974e915d741d50d11da2d7f87542eba46`
- `stage2b_blinded_scoring_template_v1_3c.csv`
  - commit `fee0cbbe1bc9899825208b45d01a97fdb0c89103`

## Google Drive canonical mirror

Canonical V1.3 folder: `1x7BrFxvVJ-j2R_YZ80Tw36vGhjCugUDM`

- `NAAIL V1.3C — Blinded Professional Scoring Rubric`
  - file ID `1-Zqxde_VmZ9dofiKcvl8Q9XppZBSqeSBdSHqrcjkXzA`
- `NAAIL V1.3C — Architecture-Effect Analysis Pre-Registration`
  - file ID `15EMbR7ipuxYQ2Zx7q5BPSgiESinaX6X6ihdLYi510ow`
- existing workbook `NAAIL V1.3C — Architecture-Effect Experiment Matrix`
  - file ID `1JJNI8WdHb2vYPFX0MOtLzkOIL0XrVzOGLfex-zL4utA`
  - tabs now include `Experiment_Matrix`, `Success_Criteria`, `Rubric_Weights`, `PreReg_Summary`, `Scoring_Template`

Drive readback verified the scoring weights, preregistration summary, masking fields and scoring template. The corrected header `weight_pct` is present.

## Scientific boundary

No architecture-condition output has been generated or scored by this step. The private task prompts and Gold_Key remain protected. Human reviewers have not been simulated. Numeric CVPO remains `NOT_EXECUTED`.

## Next conceptual gate

The next non-technical step is to freeze the **professional task-to-architecture intervention protocol**: exactly what A0, A1 and A2 are allowed to do for each of the seven professional domains, so that A2 does not receive extra substantive evidence and the architecture effect remains identifiable.
