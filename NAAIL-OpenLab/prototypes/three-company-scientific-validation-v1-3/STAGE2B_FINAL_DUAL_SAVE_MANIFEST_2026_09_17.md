# NAAIL OpenLab™ — Stage 2B Final Dual-Save Manifest

**Date:** 2026-09-17  
**Maturity:** `RESEARCH_PROTOTYPE`  
**Scientific execution:** `REGISTERED_NOT_EXECUTED`  
**Infrastructure status:** `EXECUTED_VALIDATED`  
**Provider assignment:** `READY_PROVIDER_CONNECTION_REQUIRED`

## Public GitHub records

Repository: `Saehon/Saeid-Homayoun`  
Default branch: `main`  
Directory: `NAAIL-OpenLab/prototypes/three-company-scientific-validation-v1-3/`

Current candidate model IDs:

- C01 OpenAI — `gpt-6-astra`
- C02 Google — `gemini-3.8-flash`
- C03 Anthropic — `claude-fable-5`

The public Stage 2B runner package now includes:

- `stage2b_runner.py`
- `STAGE2B_EXECUTION_RUNBOOK_V1_3B.md`
- `requirements-stage2b.txt`
- `STAGE2B_RUNNER_VALIDATION_2026_09_17.md`
- `stage2b_candidate_roster_v1_3b.csv`
- `stage2b_response_freeze_ledger_template_v1_3b.csv`

The runner is non-secret: it contains no private benchmark prompts, no gold key and no credentials. A 21-task placeholder dry run validated infrastructure only and made no provider API call.

All three candidates remain `READY_PROVIDER_CONNECTION_REQUIRED`. No independent model output has been represented as executed.

## Google Drive records

Canonical V1.3 folder ID: `1x7BrFxvVJ-j2R_YZ80Tw36vGhjCugUDM`

Current mirrored records include:

- `NAAIL V1.3 — Stage 2B Current State & Publication Record`
- `Prototype V1.3B — Stage 2B Candidate Roster`
- `NAAIL V1.3B — Stage 2B Independent Model Run Gate`
- `Prototype V1.3B — Stage 2B Response Freeze Ledger`
- Stage 2B runner/readiness materials mirrored after publication.

## Public/private integrity boundary

The private V1.3B 21-task packet, private gold key and patent-sensitive enabling detail remain outside public GitHub. Their non-public status is intentional and required to preserve blind evaluation integrity and the patent-first boundary.

## Scientific lock

Until independent C01/C02/C03 runs are observed and frozen:

- Stage 2B remains `REGISTERED_NOT_EXECUTED`;
- Stage 2C blinded scoring remains locked;
- numeric CVPO remains `NOT_EXECUTED`;
- Phase 2 is not promoted;
- WMT/JPM Human Gate is unchanged;
- Step 20 independent replication remains `REGISTERED_NOT_EXECUTED` for all three companies;
- Phase 3 and Phase 4 are not promoted.

## Next action

`connect provider credentials → C01 independent run → freeze/hash → C02 independent run → freeze/hash → C03 independent run → freeze/hash → telemetry verification → Stage 2C blinded scoring`
