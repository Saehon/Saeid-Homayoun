# NAAIL OpenLab™ — Three-Company Prototype V1.3 Scientific Validation Readiness

**Date:** 2026-09-17  
**Maturity:** `RESEARCH_PROTOTYPE`  
**Companies:** Microsoft (`MSFT`) · Walmart (`WMT`) · JPMorgan Chase (`JPM`)  
**Architecture:** exactly **Stable Knowledge Core™ + Replaceable Technology Core™**. No third permanent core.

> **PATENT RIGHTS RESERVED — PATENT APPLICATION PREPARATION IN PROGRESS**

## Systems-thinking execution rule

Heavy scientific work is divided into auditable stages. Every completed stage must have its own evidence, status decision, GitHub publication and Google Drive mirror before a dependent stage is eligible to proceed. The existence of a design artifact never counts as execution.

Canonical sequence:

`Stage 0 → 2A → 2B → 2C → 2D → 2E → 3A → 3B → 3C → 3D → 3E → 4A → 4B → 4C`

See `SYSTEMS_THINKING_EXECUTION_ROADMAP_V1_3.md`.

## Frozen governance boundary

- exactly two permanent cores;
- 3 companies × 20 steps = 60 company-step states;
- controlled scientific-status vocabulary;
- failed, null, contradictory, blocked and sensitivity-dependent evidence is preserved;
- patent-sensitive enabling detail remains outside public GitHub until filing review;
- WMT/JPM Human Gate decisions are not inferred;
- Step 20 independent replication remains `REGISTERED_NOT_EXECUTED` for MSFT, WMT and JPM until a separate reviewer/environment actually executes it;
- Phase 3–4 are never promoted merely because design artifacts exist.

## Current staged state

### Stage 0 — State Lock

**Status:** complete as execution governance only; no scientific status promoted.

Artifact:
- `SYSTEMS_THINKING_EXECUTION_ROADMAP_V1_3.md`

### Stage 2A — Blind Benchmark Packet Freeze

**Design outcome:** `REVISED_AFTER_CHALLENGE`  
**Candidate-model execution:** `REGISTERED_NOT_EXECUTED`

The original public 12-task packet is preserved as a **development/calibration set** because its prompts are already public and it is concentrated in factor-robustness retrieval/inference.

A separate promotion-grade **private V1.3B packet** has been frozen in Google Drive with **21 tasks = 7 professional domains × 3 companies**. The private prompts and gold key are intentionally excluded from public GitHub until candidate responses are frozen.

Public Stage 2A records:
- `STAGE2A_BLIND_BENCHMARK_PACKET_FREEZE_V1_3B.md`
- `STAGE2A_PUBLICATION_MANIFEST_2026_09_17.md`
- `blind_benchmark_scoring_schema_v1_3b.csv`
- `blind_benchmark_run_manifest_template_v1_3b.csv`

### Stage 2B — Independent Blind Model Runs

**Scientific status:** `REGISTERED_NOT_EXECUTED`  
**Execution-control infrastructure:** `EXECUTED_VALIDATED`  
**Cross-candidate input lock:** `EXECUTED_VALIDATED`  
**C01/C02/C03 structural preflights:** `PASS`  
**SDK provenance verification:** `EXECUTED_VALIDATED`  
**SDK CI runtime validation:** `BLOCKED_CI_RUN_NOT_OBSERVED`  
**Live provider calls:** `BLOCKED_PROVIDER_CREDENTIAL_AND_RUNTIME`

Frozen candidate set:

- C01 — OpenAI `gpt-6-astra`
- C02 — Google `gemini-3.8-flash`
- C03 — Anthropic `claude-fable-5`

All three providers are configured for high reasoning, closed evidence, no browsing/search/tools, no prior candidate responses and no gold-key access.

The same private V1.3B inputs are registered for all three candidates:

- 21-task packet SHA-256: `2a0857f94beff1f4c6f25b76621bd0a1f02bb8272e7f1e68eacb6acd39146eaf`
- frozen E1–E8 evidence SHA-256: `30cd72360b68d5f62f610e143aad712382edb201e972642c40b43c445061748e`

Pinned Stage 2B SDKs:

- `openai==3.14.1`
- `google-genai==2.23.0`
- `anthropic==1.6.0`

Official PyPI wheel SHA-256 values are preserved in `stage2b_sdk_provenance.csv`. A non-secret GitHub Actions workflow, `.github/workflows/naail-stage2b-sdk-lock.yml`, is published to install the pinned SDKs, verify imports/versions, compile the public Stage 2B controls, freeze the resolved environment and upload lock evidence. A controlled validation PR was merged, but the connected Actions read endpoint still reported no observable workflow run, so no CI success or runtime lock is claimed.

Published Stage 2B controls and readiness records:
- `STAGE2B_INDEPENDENT_MODEL_RUN_GATE_V1_3B.md`
- `STAGE2B_EXECUTION_RUNBOOK_V1_3B.md`
- `stage2b_runner.py`
- `stage2b_preflight.py`
- `stage2b_verify_bundle.py`
- `requirements-stage2b.txt`
- `stage2b_sdk_provenance.csv`
- `STAGE2B_RUNNER_VALIDATION_2026_09_17.md`
- `STAGE2B_HARDENING_VALIDATION_2026_09_17.md`
- `STAGE2B_C01_INPUT_FREEZE_PREFLIGHT_2026_09_17.md`
- `STAGE2B_C02_INPUT_FREEZE_PREFLIGHT_2026_09_17.md`
- `STAGE2B_C03_INPUT_FREEZE_PREFLIGHT_2026_09_17.md`
- `STAGE2B_CROSS_CANDIDATE_INPUT_LOCK_2026_09_17.md`
- `STAGE2B_THREE_CANDIDATE_PREFLIGHT_SYNC_2026_09_17.md`
- `STAGE2B_SDK_LOCK_STATUS_2026_09_17.md`
- `stage2b_input_hash_registry_v1_3b.csv`
- `stage2b_cross_candidate_input_lock_v1_3b.csv`
- `stage2b_candidate_roster_v1_3b.csv`
- `stage2b_response_freeze_ledger_template_v1_3b.csv`

The public runner and public records contain no private prompts, no gold key, no credentials and no patent-sensitive enabling material. Actual candidate execution still requires a runtime-validated pinned SDK environment plus independently supplied private provider credentials. Same-session self-comparisons, simulated provider outputs, copied answers or reconstructed responses are not promotion-eligible evidence.

### Stage 2C–2E

Not executed. Stage 2C scoring may begin only after Stage 2B raw responses are frozen for C01, C02 and C03. Numeric Cost per Verified Professional Output™ remains `NOT_EXECUTED` until real model cost, reviewer time and rework telemetry exist.

## Existing executed / derived V1.3 evidence

The V1.3 package already preserves factor robustness and related research-prototype evidence, including:

- HC3 versus HAC(3) sensitivity;
- influence diagnostics;
- leave-one-month-out stability;
- factor robustness summaries and diagnostics;
- reconciled internal clean replay record;
- Human–AI pilot power grid;
- 60-step scientific-status matrix.

These do not constitute independent replication or Phase 2 model validation.

## Key records

- `PHASED_EXECUTION_PLAN_V1_3.md`
- `SYSTEMS_THINKING_EXECUTION_ROADMAP_V1_3.md`
- `REPRODUCIBILITY_DISCREPANCY_STATUS_V1_3.md`
- `PHASE1_REPRODUCIBILITY_RECONCILIATION_V1_3.md`
- `FACTOR_FALSIFICATION_ROBUSTNESS_V1_3.md`
- `ff5_robustness_summary_v1_3.csv`
- `factor_robustness_diagnostics_v1_3.csv`
- `STAGE2A_BLIND_BENCHMARK_PACKET_FREEZE_V1_3B.md`
- `STAGE2A_PUBLICATION_MANIFEST_2026_09_17.md`
- `blind_benchmark_scoring_schema_v1_3b.csv`
- `blind_benchmark_run_manifest_template_v1_3b.csv`
- `STAGE2B_INDEPENDENT_MODEL_RUN_GATE_V1_3B.md`
- `STAGE2B_EXECUTION_RUNBOOK_V1_3B.md`
- `stage2b_runner.py`
- `stage2b_preflight.py`
- `stage2b_verify_bundle.py`
- `requirements-stage2b.txt`
- `stage2b_sdk_provenance.csv`
- `STAGE2B_SDK_LOCK_STATUS_2026_09_17.md`
- `stage2b_candidate_roster_v1_3b.csv`
- `stage2b_response_freeze_ledger_template_v1_3b.csv`
- `COST_PER_VERIFIED_PROFESSIONAL_OUTPUT_V1_3.md`
- `HUMAN_AI_POWER_AND_READINESS_V1_3.md`
- `HUMAN_GATE_STATUS_V1_3.md`
- `PATENT_INNOVATION_AGGREGATE_GATE_V1_3.md`
- `three_company_60_step_execution_matrix_v1_3.csv`

## Scientific boundary

V1.3 is a governed research prototype. It does not claim scientific closure while independent blind-model runs, prospective human verification/cost telemetry, participant execution, WMT/JPM Human Gate decisions and independent replication remain open.

**Data access is not execution. Code is not execution. Agent agreement is not verification. Statistical significance is not scientific discovery. A blocked dependency is evidence and is not silently bypassed.**
