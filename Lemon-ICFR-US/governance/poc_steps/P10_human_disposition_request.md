# P10 — Human disposition request

## What was done

Executed the committed `tools/human_review_sheet.py` against the live P10 input path. The required P07 passport is absent, so the tool stopped with `FileNotFoundError` and did not generate a review sheet. A dependency-limited notice was then written at the canonical sheet path to record that no owner decision is currently actionable; it contains no passport hash, findings, evidence claim, disposition, signature, or approval.

## Files changed

- `governance/poc_steps/P10_HUMAN_REVIEW_SHEET.md`
- `governance/poc_steps/P10_human_disposition_request.md`
- `governance/POC_STATE.md`
- `governance/OPERATOR_LOCK.md`
- `governance/poc_runs/2026-10-07_R202610071959-P10.md`

## POC demonstration (command + REAL output excerpt)

Command: `python tools/human_review_sheet.py`

Real result: exit 1 with `FileNotFoundError` for `organized/poc/msft/passports/h1_run1.json`. Real Microsoft passports, passport hashes, findings, evidence items, owner dispositions, and owner signatures produced: `0 / 0 / 0 / 0 / 0 / 0`.

## Tests (command, commit SHA, PASS/FAIL counts)

- Starting SHA: `f85d8589b40bd590f2d22561fe013f29968132f0`.
- First pytest launch could not start because pytest was absent: `No module named pytest`.
- After installing pytest 9.1.1, `python -m pytest -q tests/poc/test_poc_program.py::P04_P07_EndToEnd::test_full_chain` → `1 passed in 0.07s`; 0 failed.
- `python -m pytest -q` → `84 passed, 33 subtests passed in 0.17s`; 0 failed; 0 skipped.
- The synthetic engineering test confirms the committed builder uses the supplied passport content hash and does not create an AI disposition. It is not evidence that a real Microsoft review sheet was generated.

## Problems found (ORQ ids, or "none")

`ORQ-016` remains the controlling dependency: no compliant SEC acquisition occurred, so P05–P07 produced no Microsoft facts, hypotheses, execution, or passport. No new problem and no OPEN REPAIR QUEUE change.

## Decisions made without review (list every one)

Created a dependency notice instead of inventing the missing passport hash or silently presenting an empty sheet as review-ready. Classified P10 as `NOT_RUN_DEPENDENCY: P07` and continued to P11 as required by the no-wait rule. No owner decision, signature, human approval, independent review, or scientific conclusion was made.

## Phase status: NOT_RUN_DEPENDENCY

P10 cannot produce an actionable human disposition request until a real P07 passport exists. The canonical sheet path records the dependency honestly and preserves the future decision options without selecting one.

## Labels: UNREVIEWED, DEVELOPMENT_ONLY

UNREVIEWED; DEVELOPMENT_ONLY; NOT_RUN_DEPENDENCY: P07. ACK2007 remains SCIENTIFIC_HOLD. No scientific PASS, human approval, independent review, or merge is claimed.
