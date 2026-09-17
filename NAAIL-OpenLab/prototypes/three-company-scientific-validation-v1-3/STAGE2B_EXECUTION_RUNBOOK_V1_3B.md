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

Model IDs were rechecked against official provider documentation on 2026-09-17.

## Public execution package

- `stage2b_runner.py` — provider-neutral runner and response freezer.
- `stage2b_preflight.py` — validates blindness, task count, hashes, SDK/key readiness and output location.
- `stage2b_verify_bundle.py` — verifies the frozen 21-response bundle and manifest hashes before Stage 2C.
- `test_stage2b_runner.py` — tests 21-task dry-run behavior and rejection of gold-key fields.
- `.env.example` — names required environment variables without containing secrets.
- `.gitignore` — blocks common private benchmark, secret and run-output paths.
- `STAGE2B_SECURE_EXECUTION_CHECKLIST_V1_3B.md` — operating checklist.

The public package contains no private prompts, no gold key and no credentials.

## Private runtime inputs

Keep these outside the public Git repository:

- `tasks.jsonl` — exactly 21 private benchmark tasks; each line requires `task_id` and `prompt` only.
- `evidence.txt` — frozen E1–E8 evidence packet.
- provider API credential supplied only through a local environment variable.
- private run-output directory.

The runner rejects common answer/gold/rubric fields in `tasks.jsonl`, can require registered SHA-256 values for both private inputs, requires `--confirm-blind` for live calls and refuses a Git-worktree output directory by default.

## Required environment variables

Use only the key required for the selected candidate:

- C01: `OPENAI_API_KEY`
- C02: `GEMINI_API_KEY`
- C03: `ANTHROPIC_API_KEY`

Never put a real key in `.env.example`, GitHub, ChatGPT messages, issues, pull requests, run manifests or benchmark files.

## Installation

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements-stage2b.txt
pip freeze > environment_lock_stage2b.txt
```

macOS/Linux:

```bash
source .venv/bin/activate
pip install -r requirements-stage2b.txt
pip freeze > environment_lock_stage2b.txt
```

Freeze the environment once and do not silently update SDK versions between candidates.

## Step 1 — Preflight

Run preflight before every candidate. Prefer supplying the registered frozen hashes.

```bash
python stage2b_preflight.py \
  --candidate C01 \
  --tasks /PRIVATE/tasks.jsonl \
  --evidence /PRIVATE/evidence.txt \
  --output-dir /PRIVATE/runs \
  --expected-tasks-sha256 <REGISTERED_TASK_HASH> \
  --expected-evidence-sha256 <REGISTERED_EVIDENCE_HASH> \
  --require-key
```

A successful preflight is readiness evidence only; it is not a model observation.

## Step 2 — Dry run

```bash
python stage2b_runner.py \
  --candidate C01 \
  --tasks /PRIVATE/tasks.jsonl \
  --evidence /PRIVATE/evidence.txt \
  --output-dir /PRIVATE/runs \
  --expected-tasks-sha256 <REGISTERED_TASK_HASH> \
  --expected-evidence-sha256 <REGISTERED_EVIDENCE_HASH> \
  --dry-run
```

The dry run checks 21 unique tasks, hashes, SDK environment metadata and manifest construction without making a provider API request.

## Step 3 — Live candidate run

```bash
python stage2b_runner.py \
  --candidate C01 \
  --tasks /PRIVATE/tasks.jsonl \
  --evidence /PRIVATE/evidence.txt \
  --output-dir /PRIVATE/runs \
  --expected-tasks-sha256 <REGISTERED_TASK_HASH> \
  --expected-evidence-sha256 <REGISTERED_EVIDENCE_HASH> \
  --confirm-blind
```

The runner requests high reasoning, supplies no external tools, applies a 16,000-token output cap to each provider route, requests non-stored/stateless operation where the provider API exposes that control, records provider/SDK metadata and preserves failed calls rather than replacing them.

## Step 4 — Verify the freeze bundle

```bash
python stage2b_verify_bundle.py /PRIVATE/runs/<RUN_ID>
```

A valid bundle must contain 21 indexed response/failure records, matching per-response SHA-256 sidecars, a valid response-freeze-index hash, a valid run-manifest hash, `gold_key_access=NOT_AVAILABLE_TO_RUNNER`, and `scoring_opened=false`.

## Step 5 — Private archival

Copy the verified run directory to the restricted Google Drive folder:

`NAAIL_PRIVATE_STAGE2B_RUNS_V1_3B`

Do not publish raw responses to public GitHub before the disclosure decision.

## Execution sequence

```text
C01 preflight → C01 run → verify/freeze → private archive
C02 preflight → C02 run → verify/freeze → private archive
C03 preflight → C03 run → verify/freeze → private archive
cross-run hash/condition reconciliation → Stage 2C scoring gate
```

For comparable runs, the task hash and evidence hash must be identical. SDK/model identifiers, timestamps, failures, token telemetry and latency remain part of the record.

## Scoring lock

Stage 2C stays closed while any candidate response set is unfrozen. The gold key must not enter the runner environment. `scoring_opened` remains `false` throughout Stage 2B.

Only after C01, C02 and C03 have frozen run/failure records and each bundle passes verification may the private gold key be opened for blinded Stage 2C scoring.

## Scientific boundary

The runner being present, tested, syntactically valid, dry-run validated or credential-ready is not benchmark performance evidence. Scientific execution remains `REGISTERED_NOT_EXECUTED` until actual independent provider calls occur.
