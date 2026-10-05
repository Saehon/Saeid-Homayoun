# P06 — Hypotheses and alternatives

## What was done

Executed the committed `tools/build_hypotheses.py` entry point against the canonical Microsoft POC facts path. The program stopped before constructing any hypothesis because P05 produced no admissible `facts.json`. No period end, ICFR conclusion, alternative explanation, rebuttal evidence identifier, or control-level evidence was guessed or substituted. The supplied synthetic end-to-end test was run only as an engineering check.

## Files changed

- `governance/poc_steps/P06_hypotheses_and_alternatives.md`
- `governance/POC_STATE.md`
- `governance/OPERATOR_LOCK.md`
- `governance/poc_runs/2026-10-05_R202610051417-P06.md`

## POC demonstration (command + REAL output excerpt)

Command: `python tools/build_hypotheses.py`

Real result: exit 1 with `FileNotFoundError: [Errno 2] No such file or directory: '.../organized/poc/msft/facts.json'`. Zero real Microsoft hypotheses were created. The selected H1, four competing explanations, evidence-linked rebuttals, and the deliberate control-level `INSUFFICIENT_EVIDENCE` case were therefore not evaluated on real evidence.

## Tests (command, commit SHA, PASS/FAIL counts)

- Starting SHA: `200707729a58a93dc896fdc12bb39e522040011e`.
- Synthetic-only P04–P07 chain: `python -m pytest -q tests/poc/test_poc_program.py::P04_P07_EndToEnd::test_full_chain` → `1 passed in 0.20s`; 0 failed.
- Full regression: `python -m pytest -q` → `84 passed, 33 subtests passed in 0.30s`; 0 failed; 0 skipped.
- Real Microsoft hypothesis construction and adapter load: `NOT_RUN_DEPENDENCY: P05`; 0 real hypotheses, 0 real alternatives evaluated, and 0 real rebuttal-evidence identifiers produced.

## Problems found (ORQ ids, or "none")

ORQ-016 remains the controlling dependency blocker. No new ORQ item was added because the absent facts file is the direct downstream consequence already recorded for P04 and P05.

## Decisions made without review (list every one)

Marked P06 `NOT_RUN_DEPENDENCY: P05` and advanced. Treated the passing synthetic test solely as engineering evidence for the committed hypothesis builder and adapter chain, not as evidence about Microsoft. Did not create empty or placeholder hypothesis JSON files because they could be mistaken for an executed scientific result.

## Phase status: NOT_RUN_DEPENDENCY

P05 supplied no admissible Microsoft facts. Consequently P06 could not select the filing-derived H1, construct evidence-grounded alternatives and rebuttals, load a real hypothesis through the R2 adapter, or demonstrate the control claim as `INSUFFICIENT_EVIDENCE` on the Microsoft path.

## Labels: UNREVIEWED, DEVELOPMENT_ONLY

UNREVIEWED; DEVELOPMENT_ONLY. ACK2007 remains SCIENTIFIC_HOLD. No Microsoft conclusion, model execution, independent review, human approval, cryptography approval, or merge is claimed.
