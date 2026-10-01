# NAAIL Research Assurance MCP — Hourly Build Logs

This directory stores the canonical GitHub-side record of each scheduled ~15-minute hourly build run.

## Dual-save requirement
Every hourly run must save its result in:
1. GitHub under `hourly-build/runs/YYYY-MM-DD/HHMM_<gate>_<task>.md`
2. Google Drive in the canonical Hourly Build Master Log and, when needed, the Hourly Run Logs folder.

A run is fully logged only after both saves are verified by readback.

## Required run fields
- START_TIME / END_TIME / DURATION
- delivery gate: POC / V1 / post-V1
- task/phase
- starting and ending GitHub HEAD
- open work considered
- open blockers considered
- work attempted / completed
- evidence produced
- files changed / commits
- tests / CI
- Drive updates
- blockers and disposition
- next executable task
- status
- DUAL_SAVE_STATUS

## Fail-forward rule
If a phase is blocked, record the blocker, preserve evidence, advance to the next executable item, and revisit blockers after the first build pass.
