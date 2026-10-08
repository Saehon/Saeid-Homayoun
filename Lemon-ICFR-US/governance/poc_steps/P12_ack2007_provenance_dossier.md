# P12 — ACK2007 provenance dossier

## What was done

Created a fail-closed provenance dossier for `SIZE` and `RGROWTH` using only the conflicts already recorded in the governed repository. For each variable, the dossier enumerates every recorded competing reading, identifies the exact category of primary evidence needed to resolve it, and marks the absent document/page/table/note/equation locator as `UNKNOWN`. The inspected repository does not contain a verified ACK2007 primary publication or primary appendix/supplement, so no definition, window, rank direction, missing-data rule, or sample rule was selected. ORQ-001 and ORQ-002 remain open, quarantined, and non-executable.

## Files changed

- `research/scientific-compute-reuse/ACK2007_PROVENANCE_DOSSIER.md`
- `governance/OPEN_REPAIR_QUEUE.md`
- `governance/poc_steps/P12_ack2007_provenance_dossier.md`
- `governance/POC_STATE.md`
- `governance/OPERATOR_LOCK.md`
- `governance/poc_runs/2026-10-08_R202610080600-P12.md`

## POC demonstration (command + REAL output excerpt)

Executed the committed `VariableRegistry` and `ScientificModel` HOLD path with `PYTHONPATH=src python`. Real output: `model_status=SCIENTIFIC_HOLD`, `SIZE_executable=False`, `RGROWTH_executable=False`, and `BLOCKED:ScientificHoldError:ACK2007 is SCIENTIFIC_HOLD; public prediction disabled`. No prediction result was produced. Dossier SHA-256: `7fb8daf786a22f75d12a3d99f185e90d2df4eb8d7852f339bc102f51cbb1c491`.

## Tests (command, commit SHA, PASS/FAIL counts)

- Starting authoritative SHA: `784418d830d4ceedfe8ab4a142e82f0c88fe350f`.
- Initial targeted and full pytest launches could not start because pytest was absent: `No module named pytest`.
- After installing pytest 9.1.1, `python -m pytest -q tests/assurance/test_assurance_core.py -k 'test_35_no_bypass_around_scientific_hold'` → `1 passed, 44 deselected in 0.04s`; 0 failed.
- Full regression: `python -m pytest -q` → `84 passed, 33 subtests passed in 0.16s`; 0 failed; 0 skipped.

## Problems found (ORQ ids, or "none")

`ORQ-001` and `ORQ-002` remain open. P12 confirms that the repository has conflict provenance but lacks the verified ACK2007 primary document and exact definition/construction locators needed to resolve either variable. The dossier improves repair specificity but does not repair the scientific blockers.

## Decisions made without review (list every one)

Classified the absent primary document identity and all exact page/table/note/equation locators as `UNKNOWN`; treated PR #76 only as provenance for the conflict; did not infer a bibliography, select a competing reading, encode a construction, promote a variable, or change scientific status.

## Phase status: COMPLETE

The P12 documentation and guard checks are complete: both variables have conflict-by-conflict dossier coverage, every required unresolved primary locator is explicit, and the real HOLD guard raised `ScientificHoldError`. Completion applies only to the P12 documentation/control check; ACK2007 remains `SCIENTIFIC_HOLD` and ORQ-001/ORQ-002 remain quarantined.

## Labels: UNREVIEWED, DEVELOPMENT_ONLY

UNREVIEWED; DEVELOPMENT_ONLY; SCIENTIFIC_HOLD. No scientific PASS, prediction output, independent review, human approval, cryptography approval, or merge is claimed.
