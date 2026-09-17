# NAAIL OpenLab™ — Stage 2B Independent Runbook V1.3B

**Scientific status:** `REGISTERED_NOT_EXECUTED`  
**Infrastructure status:** `EXECUTED_VALIDATED`  
**Provider state:** `READY_PROVIDER_CONNECTION_REQUIRED`

> PATENT RIGHTS RESERVED — PATENT APPLICATION PREPARATION IN PROGRESS

## Objective

Execute the frozen V1.3B blind professional benchmark independently on three provider families, preserve every response/failure as evidence, freeze raw artifacts before scoring, and keep the private gold key inaccessible until all candidate runs are frozen.

## Frozen candidate set

| Candidate | Provider | Model ID | Reasoning |
|---|---|---|---|
| C01 | OpenAI | `gpt-6-astra` | `high` |
| C02 | Google | `gemini-3.8-flash` | `high` |
| C03 | Anthropic | `claude-fable-5` | `high` / adaptive |

Model IDs were rechecked against provider documentation on 2026-09-17.

## Public runner

`stage2b_runner.py` is a non-secret execution scaffold. It contains no task prompts, no gold key, no API credentials and no patent-sensitive implementation detail.

Private runtime inputs:

- `tasks.jsonl` — exactly 21 private benchmark tasks; each line requires `task_id` and `prompt`.
- `evidence.txt` — frozen E1–E8 evidence packet.
- provider API key supplied only through an environment variable.

The script validates exactly 21 unique task IDs, records SHA-256 for the private task file and evidence packet, runs each task as a stateless request, saves every raw response or failed call, hashes each frozen artifact, writes a response-freeze index and writes a final run manifest with `scoring_opened=false`.

## Required environment variables

Use only the key required for the selected candidate:

- C01: `OPENAI_API_KEY`
- C02: `GEMINI_API_KEY`
- C03: `ANTHROPIC_API_KEY`

Never commit `.env` files, credentials, private task packets, evidence packet exports containing restricted material, raw candidate outputs before the disclosure gate, or the gold key.

## Installation

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements-stage2b.txt
pip freeze > environment_lock_stage2b.txt
```

Record the environment lock with the run package; do not silently update SDK versions between candidates.

## Preflight dry run

```bash
python stage2b_runner.py \
  --candidate C01 \
  --tasks /private/tasks.jsonl \
  --evidence /private/evidence.txt \
  --output-dir /private/runs \
  --dry-run
```

A dry run validates file structure, task count, hashes and manifest construction but does **not** count as a model execution.

## Execution sequence

```text
C01 → freeze/hash → verify manifest
C02 → freeze/hash → verify manifest
C03 → freeze/hash → verify manifest
```

For each real run:

1. create a fresh process/session;
2. use the same frozen task and evidence files;
3. supply no browsing, grounding, web search, file search or external tools;
4. do not pass prior candidate responses;
5. do not expose the gold key;
6. retain failed calls, refusals and null outputs;
7. record actual SDK version, timestamps, token telemetry and latency;
8. record price provenance separately and prospectively;
9. freeze all response artifacts and SHA-256 values before any scoring.

## Scoring lock

Stage 2C stays closed while any candidate response set is unfrozen. `scoring_opened` must remain `false` through Stage 2B.

Only after C01, C02 and C03 are frozen may the private gold key be opened for blinded Stage 2C scoring.

## Scientific boundary

The runner being present, syntactically valid, or dry-run validated is not benchmark evidence. Scientific execution remains `REGISTERED_NOT_EXECUTED` until actual provider calls occur.
