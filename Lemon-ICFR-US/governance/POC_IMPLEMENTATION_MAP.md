# LEMON POC — IMPLEMENTATION MAP (companion to POC_PROGRAM.md v3)
Claude wrote the toolkit below and tested it on synthetic data (Python 3.12.3: 57 assurance + 18 POC tests pass).
Status: UNREVIEWED / DEVELOPMENT_ONLY. GPT commits it ONCE in P00 (toolkit PR); later phases RUN it, never rewrite it.
If a tool has a bug: fix minimally, keep its tests, record the fix under "Decisions made without review".

## Every hourly run (from Lemon-ICFR-US/)
```bash
export PYTHONPATH=src RUN=R$(date -u +%Y%m%d%H)
python tools/poc_cycle.py begin --run-id $RUN        # prints phase + run count, or SKIP
#   ... do the phase work below, write governance/poc_steps/P##_<name>.md ...
python -m pytest -q                                  # no regressions allowed
python tools/step_file.py governance/poc_steps/P##_<name>.md
python tools/poc_cycle.py end --run-id $RUN --action "<one line>"   # advances when allowed
```
`end` advances when the step file is valid, or after the 4th run (PARTIAL). Use `--force-status PARTIAL|QUARANTINED|NOT_RUN_DEPENDENCY` for a problem you cannot fix in this run (then add an ORQ row).

## Phase → tool → POC command → check
| Phase | Tool / module | POC command | Check |
|---|---|---|---|
| P00 | poc_state, operator_lock, step_file, poc_cycle + whole toolkit | `python tools/poc_state.py current` | prints P00→P01 after step file; pytest green |
| P01 | — | `python -m pytest -q`; `python examples/minimal_case.py` | demo starts `BLOCKED:` |
| P02 | `assurance/extract.py` | `python -m pytest -q tests/poc -k P02` | span/hash tamper tests pass |
| P03 | `assurance/entity_scope.py` | `python -m pytest -q tests/poc -k P03` | control claim → INSUFFICIENT_EVIDENCE |
| P04 | `tools/sec_fetch.py`, `tools/verify_manifest.py` | `python tools/sec_fetch.py --email <owner>` then `python tools/verify_manifest.py` | all OK |
| P05 | `tools/extract_msft.py` | `python tools/extract_msft.py` | rejected = 0 |
| P06 | `tools/build_hypotheses.py` | `python tools/build_hypotheses.py` | H1 + A1–A4 + C1 written; A3/A4 unrebutted is expected |
| P07 | `tools/run_poc_pipeline.py` | run once (writes config template) → set fixed `created_at` + repro fields → run again | deterministic=true; control = INSUFFICIENT_EVIDENCE |
| P08 | `tools/run_twin.py` | `python tools/run_twin.py` (edit + justify assumptions first) | 8 rows, all ANALYTICAL_SIMULATION |
| P09 | `assurance/structure.py` | build graph from facts.json (edges CANDIDATE) → `structure_graph.json` | no VALIDATED edge without admissible evidence |
| P10 | `tools/human_review_sheet.py` | `python tools/human_review_sheet.py` | sheet shows passport hash; no AI disposition |
| P11 | `tools/benchmark_registry.py`, `assurance/evidence_loader.py` | `python tools/benchmark_registry.py` | REGISTRY.json; mock files refused |
| P12 | (document) + existing HOLD guard | `python -m pytest -q tests/assurance -k 35` | ACK2007 still SCIENTIFIC_HOLD |
| P13 | `tools/improvement_gate.py` | run on Sprint-1 dev metrics if available, else synthetic labelled files → PARTIAL | worse candidate REJECTed |
| P14 | `assurance/signatures.py` | only if owner approved `cryptography` | forgery rejected |
| P15 | `tools/check_matrix.py` | write `governance/PUBLIC_PRIVATE_MATRIX.md`, then run | ALL CLASSIFIED |
| P16 | `tools/check_doc_links.py` | fix docs + write `governance/REUSE_MAP.md`, then run | NO BROKEN REFERENCES |
| P17 | `assurance/export.py` | validate `passports/h1_run1.json` with `validate_passport_json` | 0 errors |
| P18 | `tools/value_metrics.py` | `python tools/value_metrics.py` + write POC_REPORT.md | every metric has a source |
| P19 | `tools/build_final_review.py` | `python tools/build_final_review.py` | parts ≤ 60 KB → stop schedule |

## Expected honest POC outcome (not a target to force)
H1 support SUPPORTED (if the 10-K says so) · independence LOW (same rule-based codebase) · falsification INCONCLUSIVE
(A3 scope limitation and A4 non-reliance cannot be rebutted by extraction v1) · passport AWAITING_HUMAN_APPROVAL ·
control-level claim INSUFFICIENT_EVIDENCE. These are correct governance outcomes, not failures.
