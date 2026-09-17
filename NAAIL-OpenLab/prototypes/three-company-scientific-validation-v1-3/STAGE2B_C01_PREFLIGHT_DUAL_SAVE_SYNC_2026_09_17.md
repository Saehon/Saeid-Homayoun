# NAAIL OpenLab™ — Stage 2B C01 Preflight Dual-Save Sync

**Date:** 2026-09-17  
**Scientific benchmark status:** `REGISTERED_NOT_EXECUTED`  
**C01 input-freeze status:** `EXECUTED_VALIDATED`  
**C01 live provider-call status:** `BLOCKED_PROVIDER_CREDENTIAL`  
**Stage 2C scoring:** `LOCKED`

## Frozen input identity

- packet: `V1.3B_PRIVATE_21_TASK`
- task count: 21
- tasks SHA-256: `2a0857f94beff1f4c6f25b76621bd0a1f02bb8272e7f1e68eacb6acd39146eaf`
- evidence SHA-256: `30cd72360b68d5f62f610e143aad712382edb201e972642c40b43c445061748e`
- gold-key access: `NOT_READ`
- scoring opened: `false`

## Public GitHub state

Repository: `Saehon/Saeid-Homayoun`  
Branch: `main`  
Directory: `NAAIL-OpenLab/prototypes/three-company-scientific-validation-v1-3/`

- `stage2b_input_hash_registry_v1_3b.csv`
  - commit: `51cee173a8fd08988c410eed2a767f7176bfd744`
- `STAGE2B_C01_INPUT_FREEZE_PREFLIGHT_2026_09_17.md`
  - commit: `3a60509720c28478f74512b4552884304f95ae1a`
- `stage2b_candidate_roster_v1_3b.csv`
  - updated commit: `c6e6628a1f22e12bde5f5fe00813df05964de5fb`

Previously published hardening remains in force, including the hardened runner, preflight validator, bundle verifier, `.gitignore`, `.env.example`, tests, and secure execution checklist.

## Canonical V1.3 Google Drive mirror

Folder: `1x7BrFxvVJ-j2R_YZ80Tw36vGhjCugUDM`

- public C01 preflight record: `1N6coMnU31l3YWSFw5sKqxzUT3vgjk9ck`
- public input hash registry: `1t4lmcdxmLfXduWvnVFPPcMz-xO6SCFRZ`
- candidate roster sheet: `1lkRoWU_-nu5pwn8WFJs-DK43HU3dQIcZaK87WXp1dHY`

## Restricted private Stage 2B vault

Parent vault: `1O3fjtNvfTtHGrrrwUJA2Gh_ai48uIhrY`

C01 freeze folder:
- `C01_INPUT_FREEZE_2026_09_17`
- folder ID: `1Rv2VZCrAwlsE8Ri5L4UEFn1iuF1wc1dL`

Private artifacts:
- 21-task runtime JSONL: `1Egn4G1PngKDIrjoz0TT8_-bRYRFossZ8`
- frozen E1–E8 evidence text: `1eVdAwXT2i04FbYnoGl8wQGls3omJek2d`
- input-freeze manifest JSON: `1dV0JGl8TXhWCMwaQxng5FNkHVqkaKxRW`
- C01 preflight result JSON: `1-ZarUtMAlmOuPzCr5AAWnUHjoX0keIkh`
- private freeze record: `193k4XbZYQwuMCR9ix4JIsvTuK1phLbwz`

The private prompts and frozen evidence runtime files are intentionally absent from public GitHub.

## Preflight result

PASS:
- exactly 21 unique tasks;
- no forbidden answer/gold/rubric fields;
- registered task hash matches;
- registered evidence hash matches;
- output location outside Git;
- gold key not loaded;
- scoring remains closed.

BLOCKED:
- `OPENAI_API_KEY` is not available in the active execution environment;
- OpenAI SDK is not installed in this ephemeral validation environment.

No provider API request was made. No candidate answer exists yet.

## Next permitted scientific event

`private OpenAI credential + locked SDK environment → C01 preflight with --require-key → C01 live run with --confirm-blind → freeze/hash 21 responses → verify bundle → archive privately`

C02 and C03 must then use the same registered task/evidence hashes before Stage 2C is opened.
