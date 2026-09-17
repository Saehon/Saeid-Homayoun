# NAAIL OpenLab™ — Stage 2B Cross-Candidate Input Lock

**Date:** 2026-09-17  
**Input-lock status:** `EXECUTED_VALIDATED`  
**Scientific benchmark:** `REGISTERED_NOT_EXECUTED`  
**Stage 2C:** `LOCKED`

## Shared frozen packet

All three candidates C01/C02/C03 are now governed by the same registered runtime inputs:

- packet: `V1.3B_PRIVATE_21_TASK`
- task count: 21
- tasks SHA-256: `2a0857f94beff1f4c6f25b76621bd0a1f02bb8272e7f1e68eacb6acd39146eaf`
- evidence SHA-256: `30cd72360b68d5f62f610e143aad712382edb201e972642c40b43c445061748e`
- evidence anchors: E1–E8
- gold key: not read during input-freeze/preflight work
- scoring opened: false

## Candidate readiness

| Candidate | Provider/model | Structural preflight | Live call |
|---|---|---|---|
| C01 | OpenAI `gpt-6-astra` | PASS | BLOCKED — credential/SDK |
| C02 | Google `gemini-3.8-flash` | PASS | BLOCKED — credential/SDK |
| C03 | Anthropic `claude-fable-5` | PASS | BLOCKED — credential/SDK |

No candidate may use a different task/evidence hash without a new versioned packet and explicit governance record. Any mismatch invalidates direct cross-model comparison.

## Scientific lock

No provider output exists yet. Stage 2C scoring, CVPO calculation, Phase 2 promotion, Human Gate changes, and independent replication remain locked.
