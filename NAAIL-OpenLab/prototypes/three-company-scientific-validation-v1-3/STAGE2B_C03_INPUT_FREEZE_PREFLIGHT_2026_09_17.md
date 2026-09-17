# NAAIL OpenLab™ — Stage 2B C03 Input Freeze & Preflight

**Date:** 2026-09-17  
**Candidate:** C03 — Anthropic `claude-fable-5`  
**Scientific benchmark:** `REGISTERED_NOT_EXECUTED`  
**Input-freeze status:** `EXECUTED_VALIDATED`  
**Structural preflight:** `PASS`  
**Live provider-call status:** `BLOCKED_PROVIDER_CREDENTIAL_AND_SDK`  
**Stage 2C scoring:** `LOCKED`

## Frozen identity

- task count: 21
- tasks SHA-256: `2a0857f94beff1f4c6f25b76621bd0a1f02bb8272e7f1e68eacb6acd39146eaf`
- evidence SHA-256: `30cd72360b68d5f62f610e143aad712382edb201e972642c40b43c445061748e`
- gold-key access: `NOT_READ`
- scoring opened: `false`

## Structural preflight

PASS:
- exactly 21 unique tasks;
- no forbidden answer/gold/rubric fields;
- registered task hash matches;
- registered evidence hash matches;
- output location outside Git;
- no gold key loaded;
- scoring remains closed.

## Credential gate

The same preflight with `--require-key` was executed and correctly blocked because `ANTHROPIC_API_KEY` is absent. The provider SDK is also not installed in this validation environment. This is recorded as a dependency, not bypassed.

No provider API request was made and no candidate response exists.
