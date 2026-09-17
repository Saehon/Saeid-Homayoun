# NAAIL OpenLab™ — Stage 2B C01 Input Freeze & Preflight

**Date:** 2026-09-17  
**Candidate:** C01 — OpenAI `gpt-6-astra`  
**Scientific benchmark status:** `REGISTERED_NOT_EXECUTED`  
**Input-freeze status:** `EXECUTED_VALIDATED`  
**Live provider-call status:** `BLOCKED_PROVIDER_CREDENTIAL`  
**Stage 2C scoring:** `LOCKED`

## What was executed

The actual private V1.3B task packet was transformed into a runtime JSONL packet containing exactly 21 unique task IDs. The private gold-key sheet was not read, exported, or made available to the runner.

The frozen evidence packet concatenates registered E1–E8 evidence artifacts after checking each GitHub artifact against the blob SHA stored in the private Evidence Manifest.

## Frozen input hashes

- tasks SHA-256: `2a0857f94beff1f4c6f25b76621bd0a1f02bb8272e7f1e68eacb6acd39146eaf`
- evidence SHA-256: `30cd72360b68d5f62f610e143aad712382edb201e972642c40b43c445061748e`
- packet version: `V1.3B_PRIVATE_21_TASK`
- task count: `21`
- gold key access: `NOT_READ`
- scoring opened: `false`

These hashes are the registered input identity for C01 and should also be reused for C02 and C03 unless a formally documented packet revision is approved before any live run.

## Registered evidence anchors

| Source | Artifact | Verified Git blob SHA |
|---|---|---|
| E1 | MICROSOFT_POC_V1.md | `2e84a012da7e611e1639fd48afdf4fdc52b48a29` |
| E2 | executed_company_features_2026_09_17.csv | `56aecefec2cde5565101a5a4608f5d861b12641c` |
| E3 | bounded_cam_text_features_2026_09_17.csv | `3d28ab85a4b48f68d4eaa7f194b0ae98bfbdf53d` |
| E4 | evidence_passports_wmt_jpm_2026_09_17.json | `ab476376a99026bec45febd84ef827c101f544bb` |
| E5 | initial_falsification_register_wmt_jpm_2026_09_17.md | `91635d307e28a07b99dbd8fd222804e2d9b3a7d2` |
| E6 | synthetic_abc_tdabc_microcases_2026_09_17.csv | `3731cdd33b193e090e62caa261f36a5ab99b2c7b` |
| E7 | factor_robustness_diagnostics_v1_3.csv | `489ba1d9cd7e7242da0df500330c38898b36c3c9` |
| E8 | ff5_robustness_summary_v1_3.csv | `68c634b8406ebcc5720cbd03a45541c94cfc2ccc` |

## C01 preflight result

- provider: OpenAI
- model: `gpt-6-astra`
- task count: 21
- task hash match: PASS
- evidence hash match: PASS
- forbidden gold/rubric fields: none detected
- private output path outside Git: PASS
- gold-key access: `NOT_CHECKED_OR_LOADED`
- scoring opened: `false`
- API credential present: `false`
- OpenAI SDK present in this ephemeral validation environment: `false`

The missing SDK/key do not invalidate the input freeze. They prevent a live candidate call. No provider API request was made.

## Public/private boundary

Public GitHub contains only hashes, source anchors, governance state and non-secret execution code. The private `tasks.jsonl`, frozen `evidence.txt`, and private input-freeze manifest are stored only in the restricted Stage 2B Drive vault.

## Next permitted event

`provision OpenAI API credential in a private local runtime → install locked SDK environment → rerun C01 preflight with --require-key → execute C01 with --confirm-blind → freeze/hash 21 raw responses → verify bundle → archive privately`

Do not open the gold key or Stage 2C scoring before C01, C02 and C03 response sets are frozen.
