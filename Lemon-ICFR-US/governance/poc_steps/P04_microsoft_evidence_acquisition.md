# P04 — Microsoft evidence acquisition

## What was done

Verified the live P04 precondition and applied the program's fail-closed rule. `owner_contact_email_for_sec` remained `NOT_PROVIDED`, so no SEC EDGAR or CompanyFacts request was issued and no contact detail was invented. The committed `EdgarClient` rejected a non-email User-Agent exactly as intended. P04 is therefore PARTIAL and progression continues with the Microsoft evidence path unavailable.

## Files changed

- `governance/poc_steps/P04_microsoft_evidence_acquisition.md`
- `governance/POC_STATE.md`
- `governance/OPERATOR_LOCK.md`
- `governance/OPEN_REPAIR_QUEUE.md`
- `governance/poc_runs/2026-10-05_R202610050823-P04.md`

## POC demonstration (command + REAL output excerpt)

Command: `PYTHONPATH=src:tools python - <fail-closed EdgarClient preflight>`

Real output: `BLOCKED:SEC requires a User-Agent with a contact email` (exit 0 for the expected blocked-condition assertion). The first import attempt with `PYTHONPATH=src` exited 1 with `ModuleNotFoundError: No module named '_common'`; the corrected committed-tool import path was then used. No network request occurred.

## Tests (command, commit SHA, PASS/FAIL counts)

- Starting SHA: `91e5fc9741c0bcd7485f718e45da22e5e7d36f86`.
- Initial `PYTHONPATH=src python -m pytest -q tests/poc -k P04` could not start because pytest was absent in the fresh execution environment (`No module named pytest`).
- After installing pytest 9.1.1, `PYTHONPATH=src python -m pytest -q tests/poc -k P04` → `2 passed, 16 deselected in 0.10s`; 0 failed.
- `PYTHONPATH=src python -m pytest -q` → `84 passed, 33 subtests passed in 0.20s`; 0 failed; 0 skipped.
- Real SEC manifest verification: NOT_RUN because the required owner contact email was not provided and no SEC evidence was acquired.

## Problems found (ORQ ids, or "none")

ORQ-016 — owner SEC contact email missing. This is dependency-critical for the Microsoft evidence path. No SEC request was attempted; P05 and evidence-dependent work must remain dependency-limited until repair.

## Decisions made without review (list every one)

Applied the explicit P04 blocked rule and advanced after recording ORQ-016. Did not infer an email from repository metadata, user identity, or memory. Classified the absent P04 evidence path as dependency-critical, while preserving independent later phases where the program permits fail-forward execution.

## Phase status: PARTIAL

The acquisition and manifest check were not executed because the required compliant SEC User-Agent contact is unavailable.

## Labels: UNREVIEWED, DEVELOPMENT_ONLY

UNREVIEWED; DEVELOPMENT_ONLY. ACK2007 remains SCIENTIFIC_HOLD. No Microsoft scientific conclusion, independent review, human approval, or merge is claimed.
