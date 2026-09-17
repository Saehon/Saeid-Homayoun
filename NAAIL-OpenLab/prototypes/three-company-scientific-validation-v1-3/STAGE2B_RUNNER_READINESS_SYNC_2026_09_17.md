# NAAIL OpenLab™ — Stage 2B Runner Readiness Sync Manifest

**Date:** 2026-09-17  
**Scientific benchmark status:** `REGISTERED_NOT_EXECUTED`  
**Infrastructure status:** `EXECUTED_VALIDATED`  
**Provider state:** `READY_PROVIDER_CONNECTION_REQUIRED`

## Candidate set

- C01 — OpenAI `gpt-6-astra`
- C02 — Google `gemini-3.8-flash`
- C03 — Anthropic `claude-fable-5`

Model identifiers were rechecked against official provider documentation on 2026-09-17.

## GitHub public state

Repository: `Saehon/Saeid-Homayoun`  
Branch: `main`  
Directory: `NAAIL-OpenLab/prototypes/three-company-scientific-validation-v1-3/`

| Artifact | Commit |
|---|---|
| corrected candidate roster | `2875dc3f8aad54f6f31930516342281eb1c3e2b6` |
| `stage2b_runner.py` | `784c120edc402f433b818ddf865299bdb1f98f83` |
| `STAGE2B_EXECUTION_RUNBOOK_V1_3B.md` | `fc853ffdf6998221eb1825fa7f7befc4b37050f6` |
| `requirements-stage2b.txt` | `ae5d057b096067d8c5522d7ff0abfd6d68cd97fa` |
| `STAGE2B_RUNNER_VALIDATION_2026_09_17.md` | `4868b15b6e8bdbe45569e8e7b1b145b0b6e5ec8f` |
| updated V1.3 README | `785f5f950b51d66ebe11e8ff8f7718a98adeda25` |
| updated Stage 2B final manifest | `e12850ccf16c11f4377204a07f9f5241d7c83a94` |

## Google Drive canonical mirror

Canonical V1.3 folder: `1x7BrFxvVJ-j2R_YZ80Tw36vGhjCugUDM`

| Artifact | Drive file ID |
|---|---|
| `stage2b_runner.py` | `1Iye1mkm_VK_kLJjRF-KjkDhsNqsFu63L` |
| `STAGE2B_EXECUTION_RUNBOOK_V1_3B.md` | `1ZDzS-jh_6pS-1_WzcC6EWuDXj5_EBg3O` |
| `requirements-stage2b.txt` | `1-f_eUCxGBnj0cEuY_Dc9zyYyFs-g2I3F` |
| `STAGE2B_RUNNER_VALIDATION_2026_09_17.md` | `1JwO3KA3S-e2PqwEwk1iugl0jTC3hzAL7` |
| Stage 2B candidate roster | `1lkRoWU_-nu5pwn8WFJs-DK43HU3dQIcZaK87WXp1dHY` |

## Private response-freeze area

Private parent benchmark folder: `1o-ljEkitKeLpqO2xFfnKlw38CpWvzNFl`

New private run-output folder:

- `NAAIL_PRIVATE_STAGE2B_RUNS_V1_3B`
- folder ID: `1O3fjtNvfTtHGrrrwUJA2Gh_ai48uIhrY`

This private folder is the intended storage location for raw provider outputs, failure records, response hashes, run manifests and environment locks before the disclosure gate.

## Dry-run validation

The public runner was syntax-checked and dry-run tested with 21 placeholder task records and placeholder evidence. The dry run verified:

- exactly 21 unique task IDs;
- task-file SHA-256;
- evidence-file SHA-256;
- pre-run manifest construction;
- provider/model mapping;
- stateless per-task execution design;
- no gold-key access;
- `scoring_opened=false`.

No provider API request was made in the dry run.

## Scientific lock

Infrastructure validation does not equal benchmark execution. Until genuine provider calls are executed and frozen:

- Stage 2B remains `REGISTERED_NOT_EXECUTED`;
- Stage 2C remains locked;
- numeric CVPO remains `NOT_EXECUTED`;
- Phase 2 is not promoted;
- Human Gate and independent-replication states remain unchanged.

## Next execution event

`provider credentials/connectors → C01 run → freeze/hash → C02 run → freeze/hash → C03 run → freeze/hash → telemetry verification → Stage 2C scoring`
