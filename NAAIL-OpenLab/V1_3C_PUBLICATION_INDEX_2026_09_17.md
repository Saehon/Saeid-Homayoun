# NAAIL OpenLab™ — V1.3C Architecture-Effect Validation Publication Index

**Date:** 2026-09-17  
**Platform:** NAAIL OpenLab™ — V2026.3 Multi-Agent Digital Twin  
**Architecture:** exactly **Stable Knowledge Core™ + Replaceable Technology Core™**  
**Maturity:** `RESEARCH_PROTOTYPE`  
**Conceptual design:** `REVISED_AFTER_CHALLENGE`  
**Architecture-effect design:** `FROZEN_DESIGN`  
**Scoring rubric:** `FROZEN_DESIGN`  
**Analysis pre-registration:** `FROZEN_DESIGN`  
**Task-to-architecture intervention protocol:** `FROZEN_DESIGN`  
**Scientific execution:** `REGISTERED_NOT_EXECUTED`  
**Gold_Key:** `LOCKED`  
**Stage 2C:** `LOCKED`

> **PATENT RIGHTS RESERVED — PATENT APPLICATION PREPARATION IN PROGRESS**

## Scientific question

V1.3C tests whether the **NAAIL governance architecture itself improves professional accounting/auditing judgment when the underlying model, professional task and substantive evidence are held constant**.

The experiment is intentionally not a provider leaderboard. Provider identity is treated as a robustness/blocking factor.

## Frozen architecture conditions

- **A0 — Model + Frozen Evidence**: best direct answer from the common evidence, without required NAAIL governance structures.
- **A1 — Evidence Passport™**: A0 evidence plus structured provenance, relevance, sufficiency, gaps and claim–evidence linkage.
- **A2 — Full NAAIL Verify**: A1 plus public-safe risk/assertion/decision structure, contradiction challenge, falsification/disconfirming-evidence checks, evidence-sufficiency gate and human-review-ready decision path.

**Identification rule:** A1/A2 may organize, transform and challenge the same evidence; they may not receive better or additional substantive evidence.

## Planned experiment

**3 providers × 3 architecture conditions × 21 professional tasks = 189 blinded outputs**

Provider robustness blocks:

- C01 — OpenAI `gpt-6-astra`
- C02 — Google `gemini-3.8-flash`
- C03 — Anthropic `claude-fable-5`

Private benchmark scope:

- 21 tasks = 7 professional domains × 3 companies;
- companies: Microsoft (`MSFT`), Walmart (`WMT`), JPMorgan Chase (`JPM`);
- frozen tasks SHA-256: `2a0857f94beff1f4c6f25b76621bd0a1f02bb8272e7f1e68eacb6acd39146eaf`;
- frozen E1–E8 evidence SHA-256: `30cd72360b68d5f62f610e143aad712382edb201e972642c40b43c445061748e`;
- private prompts and Gold_Key are intentionally excluded from public GitHub.

## Seven professional domains

1. CAM classification
2. audit assertion mapping
3. ICFR reasoning
4. accounting judgment
5. evidence retrieval from the frozen packet
6. contradiction detection
7. professional explanation quality

## Frozen primary outcome

**Overall Professional Quality Score (OPQS), 0–100**

- professional correctness — 35%
- evidence grounding — 20%
- contradiction handling — 15%
- calibration / evidence sufficiency — 10%
- auditability / traceability — 10%
- professional decision usefulness — 10%

Primary confirmatory estimand:

`Δ_NAAIL = mean[OPQS(A2) − OPQS(A0)]`

Primary practical-effect threshold:

`mean A2−A0 ≥ +5.0 OPQS points`

Primary uncertainty specification:

- task-cluster bootstrap 95% CI;
- 10,000 replications;
- seed `20260917`;
- provider observations retained within each resampled task cluster.

A1−A0, A2−A1 and all dimension/provider/company/domain analyses are secondary.

## Promotion guardrails

`SUPPORTED_AFTER_CHALLENGE` cannot be assigned from statistical significance alone. The frozen design requires, at minimum:

1. mean A2−A0 OPQS improvement ≥ +5.0;
2. no >0.20 raw-point deterioration in grounding, contradiction handling or calibration;
3. positive mean A2−A0 effect in at least 2 of 3 providers;
4. positive mean A2−A0 effect in at least 2 of 3 companies;
5. no hidden increase in material professional errors;
6. prospective human verification evidence;
7. reviewer reliability/adjudication disclosure.

## Blinded professional review

- minimum 2 independent professional reviewers per output;
- provider and architecture condition masked;
- opaque response/reviewer IDs;
- randomized review order;
- adjudication if OPQS disagreement >10 points or any dimension differs by ≥2 raw points;
- reviewer reliability calculated before condition labels are unblinded;
- API/system failures remain `FAILED_CALL` and are not imputed as quality scores;
- substantive model refusals are scored normally.

## Intervention fidelity

Each provider-task A0/A1/A2 triplet must establish evidence and task parity before OPQS is interpreted as an architecture effect.

Frozen fidelity outcomes:

- `PASS`
- `PASS_WITH_DOCUMENTED_DEVIATION`
- `CONTAMINATED_EXCLUDE_CONFIRMATORY`
- `FAILED_CALL`

The protocol includes 15 pre-scoring fidelity controls covering task parity, evidence parity, external-retrieval prohibition, provider/model parity, condition independence, Gold blindness, knowledge parity, visible-output budget, human pre-freeze repair, A0 fairness, A1 scope, A2 evidence boundary, contradiction preservation, failure preservation and fidelity-before-scoring.

## Canonical public V1.3C package

All paths below are under:
`NAAIL-OpenLab/prototypes/three-company-scientific-validation-v1-3/`

### Architecture-effect design

- [`README.md`](./prototypes/three-company-scientific-validation-v1-3/README.md)
- [`STAGE2B_CONCEPTUAL_REDESIGN_ARCHITECTURE_EFFECT_V1_3C.md`](./prototypes/three-company-scientific-validation-v1-3/STAGE2B_CONCEPTUAL_REDESIGN_ARCHITECTURE_EFFECT_V1_3C.md)
- [`stage2b_architecture_effect_experiment_matrix_v1_3c.csv`](./prototypes/three-company-scientific-validation-v1-3/stage2b_architecture_effect_experiment_matrix_v1_3c.csv)
- [`stage2b_architecture_effect_success_criteria_v1_3c.csv`](./prototypes/three-company-scientific-validation-v1-3/stage2b_architecture_effect_success_criteria_v1_3c.csv)
- [`STAGE2B_CONCEPTUAL_REDESIGN_DUAL_SAVE_SYNC_2026_09_17.md`](./prototypes/three-company-scientific-validation-v1-3/STAGE2B_CONCEPTUAL_REDESIGN_DUAL_SAVE_SYNC_2026_09_17.md)

### Scoring and analysis pre-registration

- [`STAGE2B_BLINDED_SCORING_RUBRIC_V1_3C.md`](./prototypes/three-company-scientific-validation-v1-3/STAGE2B_BLINDED_SCORING_RUBRIC_V1_3C.md)
- [`STAGE2B_ARCHITECTURE_EFFECT_PREREGISTRATION_V1_3C.md`](./prototypes/three-company-scientific-validation-v1-3/STAGE2B_ARCHITECTURE_EFFECT_PREREGISTRATION_V1_3C.md)
- [`stage2b_blinded_scoring_template_v1_3c.csv`](./prototypes/three-company-scientific-validation-v1-3/stage2b_blinded_scoring_template_v1_3c.csv)
- [`STAGE2B_SCORING_PREREG_DUAL_SAVE_SYNC_2026_09_17.md`](./prototypes/three-company-scientific-validation-v1-3/STAGE2B_SCORING_PREREG_DUAL_SAVE_SYNC_2026_09_17.md)

### Task-to-architecture intervention identification

- [`STAGE2B_TASK_TO_ARCHITECTURE_INTERVENTION_PROTOCOL_V1_3C.md`](./prototypes/three-company-scientific-validation-v1-3/STAGE2B_TASK_TO_ARCHITECTURE_INTERVENTION_PROTOCOL_V1_3C.md)
- [`stage2b_task_architecture_domain_matrix_v1_3c.csv`](./prototypes/three-company-scientific-validation-v1-3/stage2b_task_architecture_domain_matrix_v1_3c.csv)
- [`stage2b_intervention_fidelity_checklist_v1_3c.csv`](./prototypes/three-company-scientific-validation-v1-3/stage2b_intervention_fidelity_checklist_v1_3c.csv)
- [`STAGE2B_INTERVENTION_PROTOCOL_DUAL_SAVE_SYNC_2026_09_17.md`](./prototypes/three-company-scientific-validation-v1-3/STAGE2B_INTERVENTION_PROTOCOL_DUAL_SAVE_SYNC_2026_09_17.md)

### Consolidated publication state

- [`V1_3C_CONSOLIDATED_PUBLICATION_RECORD_2026_09_17.md`](./prototypes/three-company-scientific-validation-v1-3/V1_3C_CONSOLIDATED_PUBLICATION_RECORD_2026_09_17.md)
- [`V1_3C_FINAL_DUAL_SAVE_PUBLICATION_CHECKPOINT_2026_09_17.md`](./prototypes/three-company-scientific-validation-v1-3/V1_3C_FINAL_DUAL_SAVE_PUBLICATION_CHECKPOINT_2026_09_17.md)

### Earlier Stage 2 controls preserved

The V1.3C redesign does not erase earlier Stage 2A/V1.3B execution-governance records. The private blind packet, cross-candidate input lock, provider run controls, failure preservation, and scientific-status history remain preserved in the prototype directory.

## Preserved scientific boundaries

- exactly two permanent cores;
- 3 companies × 20 steps = 60 company-step states;
- no private prompt or Gold_Key disclosure;
- no 189-output execution claim;
- no simulated human review;
- no numeric Cost per Verified Professional Output™ claim;
- no Stage 2C scoring before all required outputs are frozen and fidelity/blinding conditions are satisfied;
- no independent-replication claim without a separate reviewer/environment;
- patent-sensitive enabling internals remain private until filing review.

## Current scientific state

`architecture effect frozen → scoring frozen → preregistration frozen → intervention protocol frozen → fidelity controls frozen → scientific execution REGISTERED_NOT_EXECUTED → Gold_Key LOCKED → Stage 2C LOCKED`

## Next conceptual gate

Freeze the **condition-instruction and manipulation-check protocol**: public-safe A0/A1/A2 instruction shells, randomization/masking rules and an independent manipulation check demonstrating that governance intensity changes while substantive evidence does not.

---

**NAAIL OpenLab™ principle:** Models generate. Agents debate. Research grounds. Standards govern. Evidence decides. Humans remain accountable.
