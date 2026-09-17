# NAAIL OpenLab™ — Stage 2B API Contract Dual-Save Sync

**Date:** 2026-09-17  
**Scientific benchmark:** `REGISTERED_NOT_EXECUTED`  
**Cross-candidate input lock:** `EXECUTED_VALIDATED`  
**C01/C02/C03 structural preflights:** `PASS`  
**SDK provenance verification:** `EXECUTED_VALIDATED`  
**Provider API contract verification:** `EXECUTED_VALIDATED`  
**SDK CI runtime validation:** `BLOCKED_CI_RUN_NOT_OBSERVED`  
**Live provider calls:** `BLOCKED_PROVIDER_CREDENTIAL_AND_RUNTIME`  
**Stage 2C:** `LOCKED`

## Frozen scientific inputs

- packet: `V1.3B_PRIVATE_21_TASK`
- task count: 21
- tasks SHA-256: `2a0857f94beff1f4c6f25b76621bd0a1f02bb8272e7f1e68eacb6acd39146eaf`
- evidence E1–E8 SHA-256: `30cd72360b68d5f62f610e143aad712382edb201e972642c40b43c445061748e`
- gold key access for scoring: `NOT_OPENED`
- scoring opened: `false`

## Provider/API contract lock

Frozen candidates:
- C01 — OpenAI `gpt-6-astra`
- C02 — Google `gemini-3.8-flash`
- C03 — Anthropic `claude-fable-5`

Pinned SDKs:
- `openai==3.14.1`
- `google-genai==2.23.0`
- `anthropic==1.6.0`

Patched runner SHA-256:
`f14a11a571e94f8988c00a084a7075279c0bcbe15b311c7c9a60be2698f37dd9`

Executed controls:
- Python compile: PASS
- existing Stage 2B hardening tests: 2/2 PASS
- AST provider API contract checker: PASS
- provider calls executed: false
- credentials loaded: false

The runner explicitly freezes stateless/no-tools closed-evidence request construction. No candidate response or score was generated during this step.

## GitHub public state

Repository: `Saehon/Saeid-Homayoun`  
Branch: `main`  
Directory: `NAAIL-OpenLab/prototypes/three-company-scientific-validation-v1-3/`

New/updated records:
- `stage2b_runner.py` hardening — commit `d119ee426f2ba3c3211388f1d88f7ccb9b57b09b`
- `stage2b_api_contract_check.py` — commit `a47ca2d4c9f40063ccfac7e244ceacf340b4995a`
- `STAGE2B_API_CONTRACT_RESULT.json` — commit `53662790d18bdc73538f56328a05598e6eed9b46`
- `STAGE2B_API_CONTRACT_VALIDATION_2026_09_17.md` — commit `410e95e0973cc47c8def00f7340114c5c195d978`
- `.github/workflows/naail-stage2b-sdk-lock.yml` upgraded with API-contract verification — commit `fd51cdf6ed2817e86c7ac6f5d4c56b6ae6aa9d34`
- `STAGE2B_SDK_LOCK_STATUS_2026_09_17.md` canonical status update — commit `affd5321907e3c8f6c28040d94c5be15ce5919bd`

GitHub Actions observation after the runner/workflow updates:
- observable push workflow runs: `0`
- status: `BLOCKED_CI_RUN_NOT_OBSERVED`
- no CI success or runtime environment artifact is claimed.

## Google Drive canonical mirror

Canonical V1.3 folder: `1x7BrFxvVJ-j2R_YZ80Tw36vGhjCugUDM`

- patched `stage2b_runner.py`: `1DVpIaTt9sjWm0OIppGnF2yzG4jW7d3Vv`
- `stage2b_api_contract_check.py`: `1HTsi2BXYyI1twf609ZvYLK3WDB2r2TY_`
- `STAGE2B_API_CONTRACT_RESULT.json`: `1dCI7wDg7sHEfRCK9nJ1zoBleXMYkA51P`
- `STAGE2B_API_CONTRACT_VALIDATION_2026_09_17.md`: `1KnkCcCuKRqnQgRXYZ01cki_r9B1lX126`
- updated `naail-stage2b-sdk-lock.yml`: `1bB7AKiAgQfAoZ9SCFT6UwUi0TBbyK5dE`
- canonical `STAGE2B_SDK_LOCK_STATUS_2026_09_17.md`: `1FmvPZT6kzOKPTBCbxJGorsfVto_VCEqC`

Private prompts, Gold_Key, API credentials, and provider responses remain outside public GitHub.

## Scientific boundary and next gate

This step validates the provider request contracts and strengthens the future runtime lock; it does not validate an SDK runtime and does not execute any candidate model.

The next permitted scientific event is:

`successful independent pinned-SDK runtime lock → private C01 credential → C01 live 21-task run on registered hashes → freeze/hash/verify → C02 → C03 → Stage 2C blinded scoring`

Until the runtime lock is observed and verified, Stage 2B remains `REGISTERED_NOT_EXECUTED` and Stage 2C remains `LOCKED`.
