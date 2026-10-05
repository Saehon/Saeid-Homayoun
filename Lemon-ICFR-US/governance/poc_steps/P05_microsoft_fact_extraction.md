# P05 — Microsoft filing fact extraction

## What was done

Executed the committed Microsoft extraction entry point against the canonical evidence location. It failed before extracting any fact because P04 produced no admissible SEC manifest. No synthetic filing, legacy mock, memory-based value, or alternate Microsoft artifact was substituted. The supplied synthetic end-to-end test was executed only as an engineering check and is not treated as Microsoft evidence.

## Files changed

- `governance/poc_steps/P05_microsoft_fact_extraction.md`
- `governance/POC_STATE.md`
- `governance/OPERATOR_LOCK.md`
- `governance/poc_runs/2026-10-05_R202610051304-P05.md`

## POC demonstration (command + REAL output excerpt)

Command: `PYTHONPATH=src:tools python tools/extract_msft.py`

Real result: exit 1 with `FileNotFoundError: [Errno 2] No such file or directory: '.../organized/evidence/msft/manifest.json'`. No facts file was created and no Microsoft factual result is claimed.

## Tests (command, commit SHA, PASS/FAIL counts)

- Starting SHA: `3b900835dfd7dd625adf83cfc866cb2ed6db0b2e`.
- Initial pytest attempt could not start because pytest was absent; the first installation attempt timed out while retrieving the package.
- A second installation attempt succeeded with pytest 9.1.1.
- Synthetic-only extraction chain: `PYTHONPATH=src python -m pytest -q tests/poc/test_poc_program.py::P04_P07_EndToEnd::test_full_chain` → `1 passed in 0.18s`; 0 failed.
- Full regression: `PYTHONPATH=src python -m pytest -q` → `84 passed, 33 subtests passed in 0.42s`; 0 failed; 0 skipped.
- Real Microsoft span verification: NOT_RUN_DEPENDENCY P04; zero real facts extracted and zero real spans verified.

## Problems found (ORQ ids, or "none")

ORQ-016 remains the controlling dependency blocker. No new ORQ item was added because the missing manifest is the direct downstream effect already recorded for P04.

## Decisions made without review (list every one)

Marked P05 `NOT_RUN_DEPENDENCY: P04` and advanced. Treated the synthetic test solely as engineering evidence for the committed extractor, not as evidence about Microsoft. Did not inspect or reuse mock Microsoft artifacts covered by ORQ-009.

## Phase status: NOT_RUN_DEPENDENCY

P04 supplied no admissible manifest or filing source. Therefore management's ICFR conclusion, auditor opinion, auditor identity, material-weakness disclosure, period end, source spans and hashes were not extracted.

## Labels: UNREVIEWED, DEVELOPMENT_ONLY

UNREVIEWED; DEVELOPMENT_ONLY. ACK2007 remains SCIENTIFIC_HOLD. No Microsoft conclusion, independent review, human approval, or merge is claimed.
