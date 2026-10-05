# P03 — Entity-level scope mode

## What was done
Executed the committed P03 entity-scope implementation without rewriting phase logic. A clearly labelled synthetic entity-level ICFR claim was supported by an admissible synthetic evidence fact. A synthetic control-operating-effectiveness claim under the same entity scope returned `INSUFFICIENT_EVIDENCE`, and the scope kept process, account, and control details as `NOT_PUBLICLY_OBSERVABLE`.

## Files changed
This P03 step record, the machine-updated `governance/POC_STATE.md`, the released `governance/OPERATOR_LOCK.md`, and the append-only hourly run record. No entity-scope source or test was changed because the supplied toolkit already implements P03.

## POC demonstration (command + REAL output excerpt)
`PYTHONPATH=src python - <synthetic P03 demonstration>` exited 0 and printed `scope_issues= []`, `scope_control= NOT_PUBLICLY_OBSERVABLE`, `entity_claim= SUPPORTED`, and `control_claim= INSUFFICIENT_EVIDENCE`. The exact note was `control-level predicates ['control_operating_effective'] are NOT_PUBLICLY_OBSERVABLE under entity scope`.

## Tests (command, commit SHA, PASS/FAIL counts)
At starting SHA `0a19173c2c77718e1bdf4ecdf7fea0f047b46fd2`, `PYTHONPATH=src python -m pytest -q tests/poc -k P03` exited 0 after installing the missing test-runner dependency: **1 passed, 17 deselected in 0.10s; 0 failed**. Full regression `PYTHONPATH=src python -m pytest -q` exited 0: **84 passed, 33 subtests passed in 0.17s; 0 failed, 0 skipped**.

## Problems found (ORQ ids, or "none")
No new program defect. The first phase-test invocation exited 1 solely because `pytest` was absent from the ephemeral execution environment (`No module named pytest`); installing pytest 9.1.1 restored the prescribed command in the same cycle. This was one resolved environmental attempt and was not added to OPEN REPAIR QUEUE.

## Decisions made without review
Created the dedicated P03 branch specified by the program and used only synthetic evidence for the POC. Treated `NOT_PUBLICLY_OBSERVABLE` and `INSUFFICIENT_EVIDENCE` as correct governed outcomes. No real-company control design, operating effectiveness, scientific approval, merge, or human disposition was asserted.

## Phase status: COMPLETE

## Labels: UNREVIEWED, DEVELOPMENT_ONLY
