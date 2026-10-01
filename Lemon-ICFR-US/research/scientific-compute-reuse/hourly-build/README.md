# LEMON-SCI Hourly Build Logging Protocol

## Execution loop

**15-minute work → GitHub save → Google Drive save → readback verification → next hour.**

This directory is the machine-auditable hourly control layer for the LEMON-SCI / Lemon-ICFR-US benchmark build.

## Active benchmark policy

- ACK2007 is retired from the active benchmark path; preserve its historical provenance only.
- Rank candidate benchmark papers: **FT50 → ABS4 → ABS3 → ABS2 → ABS1**.
- Within a tier prefer: direct ICFR relevance, primary-source completeness, executable specification, accessible data/code, reproducibility, SEC/public-data feasibility, and one-company POC suitability.

## Progress-first blocker policy

- `LOCAL`: record in the OPEN REPAIR QUEUE and continue to the next executable phase.
- `DEPENDENCY_CRITICAL` for one paper/model: quarantine it and advance the next-best benchmark.
- `DEPENDENCY_CRITICAL` for an overall scientific claim: do not force PASS; continue all independent valid work.
- Never silently drop a blocker or fabricate evidence.

## Mandatory hourly sequence

1. Execute one focused ~15-minute work packet from the latest verified state.
2. Save meaningful state/result to the authorized GitHub feature branch.
3. Save the corresponding hourly record to the canonical Google Drive hourly log.
4. Read back and verify both saves.
5. End the run and continue from the verified state next hour.

## Mandatory hourly fields

`START_TIME`, `END_TIME`, `DURATION`, `PAPER_OR_MODEL`, `JOURNAL`, `JOURNAL_TIER`, `PHASE`, `WORK_ATTEMPTED`, `WORK_COMPLETED`, `EVIDENCE`, `CHANGED_FILES`, `GITHUB_STARTING_HEAD`, `GITHUB_ENDING_HEAD`, `GITHUB_COMMIT`, `TESTS`, `CI_STATUS`, `CODEX_STATUS`, `BLOCKERS`, `BLOCKER_CLASS`, `OPEN_REPAIR_QUEUE_CHANGES`, `DRIVE_UPDATES`, `GITHUB_READBACK`, `DRIVE_READBACK`, `ENGINEERING_STATUS`, `SCIENTIFIC_STATUS`, `GATE_STATUS`, `DUAL_SAVE_STATUS`, `POC_V1_STATUS`, `NEXT_EXECUTABLE_TASK`.

## DUAL_SAVE_STATUS

- `PASS`: GitHub save/readback **and** Google Drive save/readback verified.
- `PARTIAL`: exactly one side verified; missing save becomes a repair item.
- `BLOCKED`: neither side can be verified or a required save cannot be completed.

`PASS` is forbidden without readback evidence from both systems.

## Audit rule

Hourly records are append-only. Corrections are new corrective entries; do not silently rewrite prior evidence.

## Files

- `hourly-run.schema.json` — machine-readable run contract.
- `hourly-build-log.md` — GitHub-side append-only master run log.
- Google Drive master log is the private research/archive counterpart.
