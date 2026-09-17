# NAAIL OpenLab™ — Stage 2B Conceptual Redesign Dual-Save Sync

**Date:** 2026-09-17  
**Conceptual design:** `REVISED_AFTER_CHALLENGE`  
**Scientific execution:** `REGISTERED_NOT_EXECUTED`  
**Stage 2C:** `LOCKED`

## Main conceptual decision

The primary scientific question is no longer which AI provider performs best. The primary question is whether the **NAAIL governance architecture itself** improves professional accounting/auditing judgment when the underlying model, task, and evidence are held constant.

Providers are retained as blocking/robustness factors.

## Architecture-effect design

Three conditions are frozen conceptually:

- `A0` — Model + Frozen Evidence
- `A1` — Evidence Passport™
- `A2` — Full NAAIL Verify

Primary estimand:

`Δ Full NAAIL = Score(A2) − Score(A0)` within the same provider-task pair.

Secondary estimands:

- `Score(A1) − Score(A0)` — structured evidence-governance effect
- `Score(A2) − Score(A1)` — incremental verification/falsification effect

The registered three providers are robustness blocks:

- C01 OpenAI `gpt-6-astra`
- C02 Google `gemini-3.8-flash`
- C03 Anthropic `claude-fable-5`

Planned design size:

`3 providers × 3 architecture conditions × 21 tasks = 189 blinded outputs`

## GitHub public publications

Repository: `Saehon/Saeid-Homayoun`  
Branch: `main`  
Directory: `NAAIL-OpenLab/prototypes/three-company-scientific-validation-v1-3/`

- conceptual redesign: `STAGE2B_CONCEPTUAL_REDESIGN_ARCHITECTURE_EFFECT_V1_3C.md`
  - commit `908e29e3f1f7d3a38fcfa5c6bc2539a9090a4d1d`
- experiment matrix: `stage2b_architecture_effect_experiment_matrix_v1_3c.csv`
  - commit `ccfefe46215f60fc7bbb68cb80ce484e0e24acde`
- success criteria: `stage2b_architecture_effect_success_criteria_v1_3c.csv`
  - commit `fed0e7813cdff02f796a81d1b5f70f9c106a7324`

## Google Drive canonical mirror

Canonical V1.3 folder: `1x7BrFxvVJ-j2R_YZ80Tw36vGhjCugUDM`

- native Doc: `NAAIL V1.3C — Architecture-Effect Conceptual Redesign`
  - file ID `1AQpnK4fx_Av-qo6V37h8k4xelTqPQKNIF0i0Gm4rR_g`
- native Sheet: `NAAIL V1.3C — Architecture-Effect Experiment Matrix`
  - file ID `1JJNI8WdHb2vYPFX0MOtLzkOIL0XrVzOGLfex-zL4utA`
  - tabs: `Experiment_Matrix`, `Success_Criteria`

The Drive matrix has been read back successfully: 9 provider-condition cells, 21 tasks each, total planned outputs 189. The success-criteria tab has 10 pre-specified conceptual gates and anti-overclaim rules.

## Scientific boundary

No output has been generated or scored. The private task prompts and Gold_Key remain private. Human verification is not simulated. Technical runtime work is implementation infrastructure and is not the primary scientific contribution.

## Next conceptual gate

Before execution, freeze the **blinded scoring rubric and analysis pre-registration** for the architecture-effect comparison. The rubric must define professional correctness, evidence grounding, contradiction handling, calibration, auditability, reviewer time/rework, and practical-effect thresholds before the Gold_Key is used.
