# LEMON OPEN REPAIR QUEUE — 2026-10-04 failure triage

This file records blockers only. No repair was applied in this triage session.

## ACK2007 compiler / fixture runner

- **Classification:** DEFERRED_ENGINEERING
- **Workflow:** LEMON-SCI ACK2007 Compiler Tests
- **Branch:** `feature/lemon-scientific-compute-reuse`
- **Observed failed runs:** 37200893688, 37200922018, 37200963440, 37201010928, 37201053397
- **Trigger pattern:** five separate `push` runs on five different commits; these were not five identical automatic reruns of one commit.
- **Triggering commits:**
  - b238aae1fccf5ca79221ea411109c81bc8e9377f
  - ff81413c06956dbfd60da536abef8af3fba085a6
  - 138ef62649d9f3c4e52e62955f4dcfe09986f8c4
  - 006e509320251877c85bf53af9a129d9be5551ff
  - 0c0c5a109db63eec7591d49c329c17404b674a5a
- **Command:** `pytest -q ../../verification/ACK2007/test_admission_gates.py ../../verification/ACK2007/test_fixture_runner.py`
- **Environment observed in log:** Python 3.12.14; pytest 9.1.1.
- **Exact failing collection target:** `research/scientific-compute-reuse/verification/ACK2007/test_fixture_runner.py`
- **Exact error:** `SyntaxError: unexpected character after line continuation character`
- **Source location:** `Lemon-ICFR-US/research/scientific-compute-reuse/verification/ACK2007/run_fixtures.py`, line 16.
- **Observed malformed line:** import text contains literal `\n` escape sequences inside the Python source.
- **Likely root cause:** a source-generation/edit step wrote escaped newline characters into the import block instead of real line breaks, making `run_fixtures.py` syntactically invalid.
- **Exact next repair:** replace the literal `\n` sequences in the import block with valid Python line breaks/parenthesized imports; then run `python -m py_compile .../run_fixtures.py` followed by the two targeted ACK2007 tests before any broader test run.
- **Retry rule:** parked after diagnosis; do not retry until the source repair is made deliberately.

## Lemon ICFR assurance test

- **Classification:** DEFERRED_ENGINEERING
- **Workflow:** Lemon ICFR tests
- **Branch:** `lemon/r1-assurance-core`
- **Failed run:** 37201609555
- **Triggering commit:** 26628b90b7a28a74b76d78e860a7985e1eda928f
- **Command:** `pytest -q`
- **Environment observed in log:** Python 3.12.x toolchain; pytest 9.1.1; editable package `lemon-icfr-us==0.1.0`.
- **Exact failing test:** `tests/assurance/test_no_fake_gates.py::NoFakeGates::test_no_boolean_review_or_falsification_gates`
- **Exact error:** `AssertionError ... legacy fake gates present`
- **Flagged source lines:**
  - `lemon_icfr/orchestrator.py:61: support_ok = bool(hypotheses) and all(`
  - `lemon_icfr/orchestrator.py:76: reviewer_ok = bool(hypotheses)`
  - `lemon_icfr/orchestrator.py:77: falsification_ok = bool(challenges)`
- **Run summary:** 1 failed, 46 passed, 1 warning, 26 subtests passed.
- **Likely root cause:** legacy boolean shortcuts remain in the orchestrator and bypass the evidence-grounded assurance-core gates that the new test requires.
- **Exact next repair:** replace the three legacy boolean gate assignments with the assurance-core evidence/reviewer/falsification outputs; first rerun only `tests/assurance/test_no_fake_gates.py`, then run the full test suite.
- **Retry rule:** parked; no repair or rerun in this triage session.

## Separation rule

These blockers belong to LEMON only. They must not be mixed into NAAIL scientific PRs, NAAIL assurance evidence, or NAAIL COVID execution decisions.
