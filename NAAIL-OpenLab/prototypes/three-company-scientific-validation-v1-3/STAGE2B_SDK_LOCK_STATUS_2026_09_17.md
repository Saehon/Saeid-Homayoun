# NAAIL OpenLab™ — Stage 2B SDK Lock Status

**Date:** 2026-09-17  
**Scientific benchmark:** `REGISTERED_NOT_EXECUTED`  
**Cross-candidate input lock:** `EXECUTED_VALIDATED`  
**SDK provenance verification:** `EXECUTED_VALIDATED`  
**Provider API contract verification:** `EXECUTED_VALIDATED`  
**SDK CI runtime validation:** `BLOCKED_CI_RUN_NOT_OBSERVED`  
**Live provider calls:** `BLOCKED_PROVIDER_CREDENTIAL_AND_RUNTIME`  
**Stage 2C:** `LOCKED`

## Frozen SDK pins

- OpenAI Python SDK `3.14.1`
- Google GenAI Python SDK `2.23.0`
- Anthropic Python SDK `1.6.0`

The corresponding PyPI wheel SHA-256 digests are recorded in `stage2b_sdk_provenance.csv` and were verified against official PyPI release pages on 2026-09-17.

## Provider API contract validation

A static provider-contract audit was executed before any credentialed call. The patched runner now explicitly enforces the frozen closed-evidence conditions:

- OpenAI Responses API: `instructions=SYSTEM_CONTRACT`, `store=False`, `tools=[]`, high reasoning, stateless input.
- Google Interactions API: `system_instruction=SYSTEM_CONTRACT`, `store=False`, `tools=[]`, high thinking, no `previous_interaction_id`.
- Anthropic Claude Fable 5: `system=SYSTEM_CONTRACT`, `tools=[]`, `output_config={"effort":"high"}` and no manual thinking budget.

Validation executed:

- Python compile: PASS
- existing Stage 2B hardening tests: **2 passed**
- AST provider-contract checker: **PASS**
- patched runner SHA-256: `f14a11a571e94f8988c00a084a7075279c0bcbe15b311c7c9a60be2698f37dd9`

Public records:

- `stage2b_api_contract_check.py`
- `STAGE2B_API_CONTRACT_RESULT.json`
- `STAGE2B_API_CONTRACT_VALIDATION_2026_09_17.md`

## GitHub state

- pinned `requirements-stage2b.txt`: commit `5997d54513191b04aa3a35bb9234dcad999c9278`
- SDK provenance registry: commit `c3220c3b8b27e622ee47e5ae20191d997208ecf3`
- SDK-lock workflow created: commit `c52d332c9fb527e41873017dafa62be51d1a204d`
- pull-request trigger added: commit `2d87779bf7e502ac3a902ec2482cb6bc4ed461fa`
- controlled validation PR #26 merged to `main`: merge/squash commit `4bbc741e2d0a0bd9bcba87e10f19535ab7a3b290`
- provider request contract hardening: commit `d119ee426f2ba3c3211388f1d88f7ccb9b57b09b`
- API contract checker: commit `a47ca2d4c9f40063ccfac7e244ceacf340b4995a`
- API contract result: commit `53662790d18bdc73538f56328a05598e6eed9b46`
- API contract validation record: commit `410e95e0973cc47c8def00f7340114c5c195d978`
- SDK-lock workflow upgraded with contract checker: commit `fd51cdf6ed2817e86c7ac6f5d4c56b6ae6aa9d34`

No API keys, private prompts, gold key, evidence runtime file, or provider response are included in public GitHub.

## Runtime validation finding

The current chat execution container cannot resolve PyPI because outbound package-index/network access is unavailable. A GitHub Actions workflow was therefore published to perform the SDK install/import/environment-freeze step in GitHub CI.

A controlled PR trigger, merge, runner update, and workflow update were all executed, but the connected GitHub Actions read endpoint continued to report zero observable workflow runs. Therefore no CI success, environment artifact, or runtime lock is claimed.

This condition remains `BLOCKED_CI_RUN_NOT_OBSERVED`, not an SDK incompatibility.

## Existing scientific controls remain unchanged

- 21-task V1.3B input hash is unchanged.
- E1–E8 evidence hash is unchanged.
- C01/C02/C03 structural preflights remain passed.
- gold key remains unopened for scoring.
- no candidate response exists.
- numeric CVPO remains `NOT_EXECUTED`.
- Stage 2C remains locked.

## Next permitted operation

One of the following must occur before a live model benchmark:

1. GitHub Actions produces a successful `NAAIL Stage2B SDK Lock` run and its artifact is verified; or
2. an independent connected/local environment installs exactly the pinned SDK versions, records the full `pip freeze`, verifies imports, runs `stage2b_api_contract_check.py`, and produces the same runtime lock evidence.

After runtime validation, provision the private C01 credential and execute the registered-hash C01 run. Then freeze/hash/verify C01, followed by C02 and C03 on identical inputs before Stage 2C scoring.
