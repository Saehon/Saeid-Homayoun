# P02 — Fact extraction core

## What was done
Executed the committed P02 span-provenanced fact extractor without rewriting phase logic. A clearly labelled synthetic filing produced one `management_icfr_conclusion` fact carrying `source_evidence_id`, accession, section, character offsets, `span_sha256`, `source_sha256`, and extraction method. The verifier then re-read the stored source bytes and accepted the intact fact.

## Files changed
This P02 step record, the machine-updated `governance/POC_STATE.md`, the released `governance/OPERATOR_LOCK.md`, and the append-only hourly run record. No extractor source or test was changed because the supplied toolkit already implements P02.

## POC demonstration (command + REAL output excerpt)
`PYTHONPATH=src python - <synthetic P02 demonstration>` exited 0. It printed a `SYNTHETIC_DEMO` fact for period `2025-06-30`, span `[39,148)`, source SHA-256 `a90e14a1a8779a58ec8d93fd07a60b0a09ed1225aa4d7360fe2a6fd64b7e4f09`, span SHA-256 `61e7c5633bb3cb29e5aebd12094ca6b48a7f1b19b41c39a928b0dc3745ff059f`, and the span `Management concluded that, as of June 30, 2025, our internal control over financial reporting was effective.` It then printed `missing_span_hash=REJECTED:ExtractionError`, `altered_span=REJECTED:IntegrityError`, and `missing_source=REJECTED:ExtractionError`.

## Tests (command, commit SHA, PASS/FAIL counts)
At starting SHA `68c51b9f37d994c5cd88cfedbd44dbf6bbffd4f9`, `PYTHONPATH=src python -m pytest -q tests/poc -k P02` exited 0: **3 passed, 15 deselected in 0.12s; 0 failed**. Full regression `PYTHONPATH=src python -m pytest -q` exited 0: **84 passed, 33 subtests passed in 0.26s; 0 failed, 0 skipped**. The conservative-extraction test preserves the false-positive guard: the generic 10-K definition sentence is not classified as a material-weakness disclosure.

## Problems found (ORQ ids, or "none")
No new problem. ORQ-006's machine-repair requirements were exercised successfully, but final independent review remains pending under the program governance; no scientific promotion is claimed.

## Decisions made without review
Created the dedicated P02 branch specified by the program and used only synthetic text for the POC. Treated the already committed extractor as the authoritative implementation and did not rewrite it. No real filing fact, ICFR deficiency, merge, human disposition, or independent-review result was asserted.

## Phase status: COMPLETE

## Labels: UNREVIEWED, DEVELOPMENT_ONLY
