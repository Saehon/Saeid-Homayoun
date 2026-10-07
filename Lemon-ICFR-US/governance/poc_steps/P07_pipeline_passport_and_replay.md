# P07 — Pipeline run, passport and replay

## What was done

Executed the committed `tools/run_poc_pipeline.py` entry point on the canonical Microsoft POC path. Its first invocation created the required configuration template and returned `NOT_RUN`; the template was deliberately left with unset reproducibility fields. A second invocation stopped before pipeline execution because P05/P06 supplied no admissible `facts.json`. No real support, reviewer, falsifier, passport, replay hash, human-approval status, or Microsoft conclusion was produced. The supplied synthetic end-to-end chain was executed only as an engineering test.

## Files changed

- `organized/poc/msft/config.json` (generated template only; not an executed case)
- `governance/poc_steps/P07_pipeline_passport_and_replay.md`
- `governance/POC_STATE.md`
- `governance/OPERATOR_LOCK.md`
- `governance/poc_runs/2026-10-07_R202610070400-P07.md`

## POC demonstration (command + REAL output excerpt)

First command: `python tools/run_poc_pipeline.py` → exit 1; `NOT_RUN: wrote .../organized/poc/msft/config.json; owner/operator must set created_at and repro fields`.

Second command: `python tools/run_poc_pipeline.py` → exit 1 with `FileNotFoundError: [Errno 2] No such file or directory: '.../organized/poc/msft/facts.json'`. No passports directory, content hash, pipeline summary, or Microsoft result was created.

## Tests (command, commit SHA, PASS/FAIL counts)

- Starting SHA: `ea57abf402d0988a20bb8ac674e9f0187ffdbdfa`.
- Initial targeted and full pytest launches could not start because pytest was absent from the fresh runtime; pytest 9.1.1 was then installed successfully.
- Synthetic-only P04–P07 chain: `python -m pytest -q tests/poc/test_poc_program.py::P04_P07_EndToEnd::test_full_chain` → `1 passed in 0.10s`; 0 failed.
- Full regression: `python -m pytest -q` → `84 passed, 33 subtests passed in 0.24s`; 0 failed; 0 skipped.
- Real Microsoft pipeline/passport/replay: `NOT_RUN_DEPENDENCY: P06`; 0 real pipeline cases, 0 passports, 0 content hashes, and 0 reviewer/falsifier outcomes.

## Problems found (ORQ ids, or "none")

ORQ-016 remains the controlling dependency blocker. No new ORQ item was added because the missing facts and hypotheses are direct downstream consequences of the already-recorded blocked P04 evidence acquisition.

## Decisions made without review (list every one)

Marked P07 `NOT_RUN_DEPENDENCY: P06` and advanced. Preserved the generated configuration strictly as an unset template. Did not populate `created_at` or reproducibility fields, create Microsoft inputs, claim LOW or other reviewer independence, reuse synthetic test outputs as evidence, or assign `AWAITING_HUMAN_APPROVAL`.

## Phase status: NOT_RUN_DEPENDENCY

P06 supplied no admissible Microsoft hypothesis, and P05 supplied no facts. Therefore the required twice-run support → reviewer → falsifier → Evidence Passport pipeline and deterministic content-hash comparison could not be executed on real evidence.

## Labels: UNREVIEWED, DEVELOPMENT_ONLY

UNREVIEWED; DEVELOPMENT_ONLY. ACK2007 remains SCIENTIFIC_HOLD. No Microsoft conclusion, scientific PASS, model execution, independent review, human approval, cryptography approval, or merge is claimed.
