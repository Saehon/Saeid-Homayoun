# NAAIL OpenLab™ — Stage 2B Hardening Validation

**Date:** 2026-09-17  
**Scope:** public runner hardening only  
**Scientific benchmark status:** `REGISTERED_NOT_EXECUTED`  
**Infrastructure status:** `EXECUTED_VALIDATED`

## Validation performed

- `stage2b_runner.py` Python syntax compilation: passed.
- `stage2b_preflight.py` Python syntax compilation: passed.
- `stage2b_verify_bundle.py` Python syntax compilation: passed.
- `test_stage2b_runner.py` Python syntax compilation: passed.
- Unit tests: **2 passed**.
- Dry-run design preserves exactly 21 tasks and `scoring_opened=false`.
- Gold/rubric fields in the task JSONL are rejected.
- Live execution requires `--confirm-blind`.
- Live execution requires the selected provider's API-key environment variable.
- Registered task/evidence SHA-256 values can be enforced.
- Private run outputs are refused inside a Git worktree by default.
- Provider storage is requested off where supported by the API (`store=false`).
- A 16,000-token per-task output cap is applied across the three candidate routes for comparability.

## Current candidate identifiers reverified from official provider documentation

- OpenAI: `gpt-6-astra`
- Google: `gemini-3.8-flash`
- Anthropic: `claude-fable-5`

No provider call was executed as part of this validation. No benchmark answer was generated and no gold key was opened.

## Scientific interpretation

This validation promotes only the **execution infrastructure**, not the benchmark. Stage 2B remains `REGISTERED_NOT_EXECUTED` until genuine independent provider calls are executed and their raw outputs/failures are frozen and verified.
