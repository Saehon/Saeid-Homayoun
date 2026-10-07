# P08 — Digital Twin scenarios

## What was done

Executed the committed `tools/run_twin.py` entry point. It created an explicit analyst-assumption template and ran all eight required entity-level Digital Twin scenarios. Every result is labelled `ANALYTICAL_SIMULATION (not observed real-world evidence)`. The inputs are illustrative assumptions, not estimates from Microsoft filings, and the output is not treated as Evidence Passport evidence.

## Files changed

- `organized/poc/msft/twin_assumptions.json`
- `organized/poc/msft/twin_results.json`
- `governance/poc_steps/P08_digital_twin_scenarios.md`
- `governance/POC_STATE.md`
- `governance/OPERATOR_LOCK.md`
- `governance/poc_runs/2026-10-07_R202610071002-P08.md`

## POC demonstration (command + REAL output excerpt)

Command: `python tools/run_twin.py`

Real result: exit 0. Eight scenario rows were written. Residual-risk deltas for `R-ENTITY` were: control failure `0.07`; evidence removal `0.07`; override increase `0.0822`; population growth `0.3`; segregation-of-duties removal `0.07`; reliability change `0.05`; competing explanation `0.024`; key-control dependency failure `0.47`. Every row carried the analytical-simulation evidence type.

## Tests (command, commit SHA, PASS/FAIL counts)

- Starting SHA: `836ef9cb78ed517d545f22c3a2ea76fbca16e49b`.
- Initial targeted and full pytest launches could not start because pytest was absent from the fresh runtime; pytest 9.1.1 was installed in the combined test command.
- P08/P09 targeted suite: `python -m pytest -q tests/poc/test_poc_program.py::P08_P09_TwinGraph` → `2 passed, 4 subtests passed in 0.07s`; 0 failed.
- Full regression: `python -m pytest -q` → `84 passed, 33 subtests passed in 0.17s`; 0 failed; 0 skipped.
- Scenario gate: 8/8 required scenarios executed; 8/8 results contain `ANALYTICAL_SIMULATION`; assumptions block present.

## Problems found (ORQ ids, or "none")

No new P08 problem. ORQ-016 remains open for the Microsoft evidence path but does not prevent explicitly labelled analytical simulation based on declared assumptions.

## Decisions made without review (list every one)

Accepted the committed default values strictly as illustrative analyst assumptions and did not calibrate them to Microsoft. Marked P08 COMPLETE because all eight required simulations executed, assumptions are visible, and every output is labelled as non-observed analytical simulation. Did not add any twin result to a passport or assert that the results describe Microsoft.

## Phase status: COMPLETE

All eight required Digital Twin scenarios executed with declared assumptions and explicit non-evidence labels. This is an engineering/analytical demonstration only, not a scientific finding or real-company assessment.

## Labels: UNREVIEWED, DEVELOPMENT_ONLY

UNREVIEWED; DEVELOPMENT_ONLY; ANALYTICAL_SIMULATION. ACK2007 remains SCIENTIFIC_HOLD. No Microsoft conclusion, scientific PASS, independent review, human approval, cryptography approval, or merge is claimed.
