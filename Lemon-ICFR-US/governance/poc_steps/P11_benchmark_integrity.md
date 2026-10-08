# P11 — Benchmark integrity

## What was done

Executed the committed `tools/benchmark_registry.py` against the live repository. Its first real output exposed a verified implementation defect: it emitted the non-program classes `CANONICAL_CANDIDATE` and `UNCLASSIFIED`, scanned unrelated operational JSON, and would ingest its own generated registry on replay. The tool was repaired narrowly to scan benchmark-like data artifacts, exclude generated outputs, use only the six permitted classes, assign stable benchmark names, write a separate hash-to-path duplicate report, require exactly one `CANONICAL` representation for each executable benchmark name, and label every entry `DEVELOPMENT_ONLY`. No file was deleted or moved.

The final registry contains 50 artifacts: 2 `CANONICAL`, 1 `DERIVED_COPY`, 39 `ARCHIVAL_COPY`, 2 `EXTERNAL_EXPORT`, and 6 `NON_EXECUTABLE_REFERENCE`. It contains 5 duplicate hash groups covering 20 paths. All six mock-response copies are `NON_EXECUTABLE_REFERENCE`. The two canonical benchmark representations are `frankenstein-phase4-case-002` and `naail-ai-cost-benchmark`; `CANONICAL` means authoritative benchmark representation, not admissible source evidence.

## Files changed

- `tools/benchmark_registry.py`
- `tests/poc/test_poc_program.py`
- `organized/benchmarks/REGISTRY.json`
- `organized/benchmarks/DUPLICATES.json`
- `governance/OPEN_REPAIR_QUEUE.md`
- `governance/poc_steps/P11_benchmark_integrity.md`
- `governance/POC_STATE.md`
- `governance/OPERATOR_LOCK.md`
- `governance/poc_runs/2026-10-08_R202610080156-P11.md`

## POC demonstration (command + REAL output excerpt)

`python tools/benchmark_registry.py` → `entries=50 duplicate_groups=5` and `canonical_counts {'frankenstein-phase4-case-002': 1, 'naail-ai-cost-benchmark': 1}`. The registry SHA-256 is `0ed7b8d3f10bf0931ae88e99f8773700b452b550921730bd5dad1e3b2c17e716`; the separate duplicate report SHA-256 is `d789b7f307bc48c4f011702ee935e555c432397d3eae12617eb535ad0ec5ae93`.

## Tests (command, commit SHA, PASS/FAIL counts)

- Starting authoritative SHA: `75843e56f0050361480c583011efdd4c912326f8`.
- Initial targeted pytest launch could not start because pytest was absent: `No module named pytest`.
- After installing pytest 9.1.1, targeted P11 gates → `2 passed in 0.05s`; 0 failed. These prove mock files cannot enter the EvidenceStore and registry output has one canonical representation per executable benchmark name using only permitted classes.
- Full regression: `python -m pytest -q` → `84 passed, 33 subtests passed in 0.18s`; 0 failed; 0 skipped.

## Problems found (ORQ ids, or "none")

`ORQ-008` is resolved conservatively by relabelling: Sprint 1 metrics remain `DEVELOPMENT_ONLY`, not holdout evidence. `ORQ-009` is partially mitigated: mock admission and competing canonical benchmark representations are closed, but the claimed SEC facts inside Case 002 still lack independently verified primary-source file provenance. Case 002 therefore remains `DEVELOPMENT_ONLY` and inadmissible as source evidence until its cited filing is retrieved and hashed.

## Decisions made without review (list every one)

Selected the FY2026-release AI-cost file and the non-export FRANKENSTEIN Case 002 file as the two authoritative benchmark representations; retained all identical copies with explicit copy classes. Treated `CANONICAL` as a benchmark-governance designation only and did not promote either artifact to admissible evidence, holdout status, scientific PASS, or production use. Repaired the committed tool because its observed output violated the P11 class enum and replay stability requirements.

## Phase status: COMPLETE

The P11 checks are met: every scanned benchmark-like artifact has a permitted classification and SHA-256; the duplicate report maps five hashes to all observed paths; mock artifacts are rejected from EvidenceStore; and each executable benchmark name has exactly one canonical representation. The unresolved Case 002 source-provenance issue remains quarantined through ORQ-009 and does not convert the benchmark into evidence.

## Labels: UNREVIEWED, DEVELOPMENT_ONLY

UNREVIEWED; DEVELOPMENT_ONLY. ACK2007 remains SCIENTIFIC_HOLD. No benchmark metric is confirmatory, no scientific result is promoted, and no independent review, human approval, deletion, merge, or production promotion is claimed.
