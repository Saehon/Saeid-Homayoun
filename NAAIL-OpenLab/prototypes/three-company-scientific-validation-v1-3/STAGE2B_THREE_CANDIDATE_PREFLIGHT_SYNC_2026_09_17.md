# NAAIL OpenLab™ — Stage 2B Three-Candidate Preflight Sync

**Date:** 2026-09-17  
**Scientific benchmark:** `REGISTERED_NOT_EXECUTED`  
**Cross-candidate input lock:** `EXECUTED_VALIDATED`  
**C01/C02/C03 structural preflights:** `PASS`  
**Live provider calls:** `BLOCKED_PROVIDER_CREDENTIAL_AND_SDK`  
**Stage 2C:** `LOCKED`

## Shared frozen identity

- packet: `V1.3B_PRIVATE_21_TASK`
- task count: 21
- tasks SHA-256: `2a0857f94beff1f4c6f25b76621bd0a1f02bb8272e7f1e68eacb6acd39146eaf`
- evidence SHA-256: `30cd72360b68d5f62f610e143aad712382edb201e972642c40b43c445061748e`
- evidence anchors: E1–E8
- gold key: not read during this stage
- scoring opened: false

## Candidate state

| Candidate | Provider/model | Structural preflight | Credential-required gate | Live response |
|---|---|---|---|---|
| C01 | OpenAI `gpt-6-astra` | PASS | BLOCKED | none |
| C02 | Google `gemini-3.8-flash` | PASS | BLOCKED | none |
| C03 | Anthropic `claude-fable-5` | PASS | BLOCKED | none |

## Public GitHub publications

Repository: `Saehon/Saeid-Homayoun`  
Branch: `main`  
Directory: `NAAIL-OpenLab/prototypes/three-company-scientific-validation-v1-3/`

- C02 preflight: commit `356335d63dabfbf52c48a28dbbe64bd89323fd92`
- C03 preflight: commit `a66bb3dfdd375ea5a41b5d9669f61763b02be9c5`
- cross-candidate lock: commit `bb3968010c95adf72290e1c4421234b32839df1e`
- cross-candidate CSV: commit `08902ac6636d85611fadc477235b95d86ec21a88`
- synchronized candidate roster: commit `2cead0c059372df33ea93518086e82eb18015692`

No private prompt, gold key, private evidence runtime file, API key, or provider response is published to GitHub.

## Canonical V1.3 Drive mirror

Folder ID: `1x7BrFxvVJ-j2R_YZ80Tw36vGhjCugUDM`

- C02 public preflight: `1wDvn6Zqd_UE4lSWMEu8tzQoJuvVpizBI`
- C03 public preflight: `1b9TPc-kAJ6ObOfNnJ99CKvxp06AQHfbr`
- cross-candidate input lock: `1otIiTFzlqUtTEcR0HMUaAsQWXSRfMfz5`
- cross-candidate CSV: `1XW_lBF9TNSVoz2Jh0GkcX67uXLrlFc9S`
- candidate roster sheet: `1lkRoWU_-nu5pwn8WFJs-DK43HU3dQIcZaK87WXp1dHY`

## Restricted private Stage 2B vault

Parent private vault: `1O3fjtNvfTtHGrrrwUJA2Gh_ai48uIhrY`

Shared immutable-by-governance runtime input folder:
- `SHARED_STAGE2B_INPUT_LOCK_2026_09_17`
- folder ID: `1ig2bHY5vw9SqIY1ItmV9yAMJogGoyCst`
- tasks JSONL: `1BkcucoBDCQI6GEC_3VUmwtAS-AyweMKR`
- evidence E1–E8 text: `12-X4M20ISv6l7VqNjanK3_MKoqU3qllc`
- shared input-lock manifest: `1WUJAksqcL4cpaoI6WFCvc02UelHuQPF0`

Candidate-specific private preflight folders:
- C01 existing freeze folder: `1Rv2VZCrAwlsE8Ri5L4UEFn1iuF1wc1dL`
- C02: `1gKqehNA4QLO90shmviWTOjUaItXQPOkn`
  - structural preflight JSON: `18sfdVdETJR3ewUWQUXRDupTyc2PXX2E7`
  - credential-gate JSON: `1q4nnRYd891kLv-bOxvRAeaqAMVMpyaV4`
  - private preflight record: `1dBThUwq95SPC7K3B_QLZtrutIL5ZRTy5`
- C03: `1pPP9piH6hGBpL4kgdXiAasGeEH7whzmA`
  - structural preflight JSON: `11Kfc-ZQusX2wQebKUhJcmHPJIkCsu0Hc`
  - credential-gate JSON: `1X59LJDb37elcLx9iSL6BI9TUyQc9P-dQ`
  - private preflight record: `1Xvwdjcn3fkfKt3C5uVUAtoHkhWNLQYG9`

## Scientific boundary

No provider API call was made in this step. No candidate answer exists. No score, CVPO result, Phase 2 promotion, Human Gate change, or independent-replication claim is permitted.

The next permitted scientific event is a credentialed, SDK-locked C01 live run on the registered hashes, followed by freeze/hash/verification; C02 and C03 must then run on the identical hashes before Stage 2C can open.
