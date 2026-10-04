# P01 — R2 closure record

## What was done
Recorded R2 for human review from live GitHub evidence without changing R2 code. PR #119 currently reports head `52dabc6a2b47a41d34e29ae38b59550d93b304fa`, merged into the stacked base `lemon/r1-assurance-core` at 2026-10-04T18:30:31Z, with main-chain merge and scientific approval still reserved to the human owner. The program start point `5ede5d32534a94f7363a571f506b2caec95768e9` was checked out separately and tested directly.

## Files changed
This P01 record, the machine-updated `governance/POC_STATE.md`, the released `governance/OPERATOR_LOCK.md`, and the append-only hourly run record. No R2 source code was changed.

## POC demonstration (command + REAL output excerpt)
At start point `5ede5d32534a94f7363a571f506b2caec95768e9`, `PYTHONPATH=src python examples/minimal_case.py` exited 0 and its first line was exactly `BLOCKED:icfr_coso_grounding,evidence_consistency`. The following lines reported `provenance True`, `rights_license True`, `icfr_coso_grounding False`, and `evidence_consistency False`.

## Tests (command, commit SHA, PASS/FAIL counts)
`python -m pytest -q` at start point `5ede5d32534a94f7363a571f506b2caec95768e9` exited 0: **66 passed, 26 subtests passed in 0.16s; 0 failed, 0 skipped**. A post-cycle regression run on the POC branch exited 0: **84 passed, 33 subtests passed in 0.28s; 0 failed, 0 skipped**. Program-named CI run `37219751336` was read back as `Lemon ICFR tests`, completed/success on SHA `ba0186b625764401eb916ba62e18a34969296b94`. The current PR #119 head also has `Lemon ICFR tests` run `37224668774` completed/success. Codex Deep PR Review run `37224703749` failed before review because `Checkout pull request merge ref` failed; the Codex review and publish steps were skipped, so no independent Codex-review conclusion is claimed.

## Problems found (ORQ ids, or "none")
No new scientific blocker. The literal demo command without `PYTHONPATH=src` initially failed with `ModuleNotFoundError: No module named 'lemon_icfr'`; rerunning with the repository's source path succeeded, so this was resolved in the same cycle and was not added to OPEN REPAIR QUEUE. Codex run `37224703749` did not execute a review because its merged-PR checkout step failed; human review remains pending.

## Decisions made without review
None affecting science or merge state. Live GitHub state was recorded even though it is newer than the program's original wording. No merge, approval, PASS promotion, cryptography work, or ACK2007 execution was performed. `owner_approved_cryptography` remains `no`, and ACK2007 remains `SCIENTIFIC_HOLD`/quarantined.

## Phase status: COMPLETE

## Labels: UNREVIEWED, DEVELOPMENT_ONLY
