# NAAIL OpenLab™ — Stage 2B Hardening & Dual-Save Sync

**Date:** 2026-09-17  
**Scientific benchmark status:** `REGISTERED_NOT_EXECUTED`  
**Infrastructure status:** `EXECUTED_VALIDATED`  
**Provider state:** `READY_PROVIDER_CONNECTION_REQUIRED`

## Public GitHub hardening commits

| Artifact | Commit |
|---|---|
| hardened `stage2b_runner.py` | `ead8c785b6016780235cc12ef4cb2b89b1aa5a1a` |
| `stage2b_preflight.py` | `db81a5de99420851af672edb0505d2c6535a06cc` |
| `stage2b_verify_bundle.py` | `2b8bf7ed7e5a348c109fda02027b79adf46fa0d8` |
| Stage 2B `.gitignore` | `f8c222b8c29fae1a19a83fa303cd223b8bd342ea` |
| `.env.example` | `4e3f849beff3ded78e7f925ba5e8161f2edab1c4` |
| `test_stage2b_runner.py` | `b55e7cccc88489bd9e7857e7bffc2922aca981a6` |
| secure execution checklist | `628f049a50d451f0578a95b44e3ecf2602d2a5f3` |
| hardening validation record | `63aaa667ec8aee2660146700c20c7ae02e43e62b` |
| hardened execution runbook | `8ffa27a94297b0e2bcebd749da0d489bb03dce02` |

Repository location:

`NAAIL-OpenLab/prototypes/three-company-scientific-validation-v1-3/`

## Validation result

- Python syntax checks: passed for runner, preflight, verifier and tests.
- Unit tests: `2 passed`.
- The runner rejects common answer/gold/rubric fields.
- Exactly 21 unique task IDs are required.
- Registered task/evidence SHA-256 values can be enforced.
- Live calls require `--confirm-blind`.
- Private output inside a Git worktree is refused by default.
- API keys remain local environment variables only.
- Provider storage is requested off where supported.
- Stage 2C remains locked with `scoring_opened=false`.

No provider API request was made during hardening validation.

## Current provider identifiers

- C01 OpenAI — `gpt-6-astra`
- C02 Google — `gemini-3.8-flash`
- C03 Anthropic — `claude-fable-5`

These model identifiers were reverified against current official provider documentation on 2026-09-17.

## Google Drive mirror

Canonical V1.3 folder: `1x7BrFxvVJ-j2R_YZ80Tw36vGhjCugUDM`

New mirrored artifacts:

- `STAGE2B_SECURE_EXECUTION_CHECKLIST_V1_3B.md`
  - Drive ID: `1D0oSoENMk_N0D3ogUM6rD50PKfTm3cjy`
- `STAGE2B_HARDENING_VALIDATION_2026_09_17.md`
  - Drive ID: `1jUImgbh9PU3nkkUxhZOMZ7kPRiswhWF5`

Existing private response vault remains:

- `NAAIL_PRIVATE_STAGE2B_RUNS_V1_3B`
- folder ID: `1O3fjtNvfTtHGrrrwUJA2Gh_ai48uIhrY`

## Scientific boundary

This hardening work validates execution infrastructure only. It does not constitute a C01/C02/C03 observation, model score, CVPO result, Human Gate decision, independent replication, or Phase 2 promotion.

## Next permitted event

`local provider credential → preflight → C01 live run → verify/freeze → private archive`

Then repeat independently for C02 and C03 before opening Stage 2C.
