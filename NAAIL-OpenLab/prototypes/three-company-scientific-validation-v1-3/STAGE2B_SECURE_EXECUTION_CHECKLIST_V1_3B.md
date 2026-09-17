# NAAIL OpenLab™ — Stage 2B Secure Execution Checklist V1.3B

**Date:** 2026-09-17  
**Scientific status:** `REGISTERED_NOT_EXECUTED` until a provider call is actually observed and frozen.  
**Infrastructure target:** `EXECUTED_VALIDATED`.

## Frozen candidate set

| Candidate | Provider | Model ID | Reasoning | Tools/Browsing |
|---|---|---|---|---|
| C01 | OpenAI | `gpt-6-astra` | high | none supplied |
| C02 | Google | `gemini-3.8-flash` | high | none supplied |
| C03 | Anthropic | `claude-fable-5` | high effort | none supplied |

## Before every live run

1. Work from a clean local environment outside the public Git repository.
2. Keep the private 21-task JSONL and frozen evidence packet outside Git.
3. Keep the gold key physically/logically separate and unavailable to the runner.
4. Put provider credentials only in local environment variables; never in source files, chat, logs, issues, or commits.
5. Run `stage2b_preflight.py` with the registered task/evidence SHA-256 values.
6. Require exactly 21 unique task IDs and no answer/rubric/gold fields in the task packet.
7. Use a fresh candidate run with no prior conversation state.
8. Use the same frozen task/evidence packet for C01, C02, and C03.
9. Disable browsing/tools by not supplying them. For APIs supporting a storage switch, request stateless/non-stored operation.
10. Do not open Stage 2C scoring until all three provider runs/failures are frozen.

## Live sequence

```text
C01 preflight → C01 run → verify freeze bundle → copy privately to Drive
C02 preflight → C02 run → verify freeze bundle → copy privately to Drive
C03 preflight → C03 run → verify freeze bundle → copy privately to Drive
three-manifest reconciliation → Stage 2C scoring gate
```

## Failure preservation

A failed provider request, refusal, null output, timeout, missing telemetry, or partial 21-task run is evidence. Preserve it with the same hashes and manifest discipline. Do not replace a failed observation with a synthetic answer.

## Secrets boundary

Required environment variables:

```text
OPENAI_API_KEY
GEMINI_API_KEY
ANTHROPIC_API_KEY
```

Never commit `.env`. The repository `.gitignore` blocks common private packet, gold-key, key, and run-output names by default.

## Stage 2C unlock rule

Stage 2C may open the gold key only when:

- C01, C02, and C03 each have a frozen run/failure record;
- each bundle passes `stage2b_verify_bundle.py`;
- task/evidence SHA-256 values are identical across comparable runs;
- candidate/model identifiers and SDK versions are recorded;
- `scoring_opened=false` in every Stage 2B manifest;
- raw outputs remain private until the disclosure gate.
