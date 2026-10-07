# P09 — Structure discovery graph

## What was done

Executed the committed `StructureGraph` implementation against the live P09 inputs. The required Microsoft public-evidence manifest, extracted facts, hypotheses, and passports are absent because ORQ-016 remains controlling. The graph was therefore serialized honestly with zero nodes and zero edges; no process, account, assertion, risk, control, evidence relationship, or Microsoft fact was invented. The artifact retains the committed structural-analogy warning and contains no `VALIDATED` edge.

## Files changed

- `organized/poc/msft/structure_graph.json`
- `governance/poc_steps/P09_structure_discovery_graph.md`
- `governance/POC_STATE.md`
- `governance/OPERATOR_LOCK.md`
- `governance/poc_runs/2026-10-07_R202610071504-P09.md`

## POC demonstration (command + REAL output excerpt)

Command: `PYTHONPATH=src python -c '... StructureGraph(EvidenceStore()) ...'`

Real output: `wrote organized/poc/msft/structure_graph.json nodes=0 edges=0 validated=0`. The JSON contains `"analogy_note": "structural analogy only; AlphaFold is not used"`, `"nodes": []`, and `"edges": []`.

## Tests (command, commit SHA, PASS/FAIL counts)

- Starting SHA: `dfb2c86161c6342ebecd4d48f32e1578290471df`.
- First targeted launch could not start because pytest was absent: `No module named pytest`.
- After installing pytest 9.1.1, `python -m pytest -q tests/poc/test_poc_program.py::P08_P09_TwinGraph::test_graph_never_validates_without_evidence` → `1 passed, 4 subtests passed in 0.35s`; 0 failed.
- `python -m pytest -q` → `84 passed, 33 subtests passed in 0.45s`; 0 failed; 0 skipped.
- The P09 gate test rejects a `VALIDATED` edge without evidence, with missing/inadmissible evidence, with an open contradiction, or with invalid confidence; it accepts validation only with linked admissible evidence.

## Problems found (ORQ ids, or "none")

`ORQ-016` remains the controlling dependency: no compliant SEC acquisition occurred, so no Microsoft public evidence exists for graph construction. No new problem and no OPEN REPAIR QUEUE change.

## Decisions made without review (list every one)

Serialized an empty graph instead of manufacturing candidate nodes or edges from memory, prior simulations, or synthetic test data. Classified P09 as `NOT_RUN_DEPENDENCY: P04` because the engineering gate is tested but the required public-evidence graph cannot be populated. No edge was promoted to `VALIDATED`; the AlphaFold reference remains a structural analogy only.

## Phase status: NOT_RUN_DEPENDENCY

P09 cannot produce the requested Microsoft public-evidence candidate graph until ORQ-016 is repaired. The empty artifact records zero executable graph content without weakening the validation gate.

## Labels: UNREVIEWED, DEVELOPMENT_ONLY

UNREVIEWED; DEVELOPMENT_ONLY; NOT_RUN_DEPENDENCY: P04. ACK2007 remains SCIENTIFIC_HOLD. No Microsoft conclusion, scientific PASS, independent review, human approval, or merge is claimed.
