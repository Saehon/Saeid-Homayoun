# OPEN REPAIR QUEUE

Queue version: 1.0  
Last updated: 2026-10-05  
Policy: persistent two-failure move-on; a new run never resets attempts.

## Current summary

| Status | Count |
|---|---:|
| BLOCKED before second failure | 0 |
| OPEN / REPAIR_QUEUE | 0 |
| QUARANTINED dependency-critical | 0 |
| REOPENED | 0 |
| CLOSED | 0 |

No blockers are currently in the repair queue.

## Stable blocker identity and rule

Use `BLK-JFE-YYYY-NNN`. Identity is gate + bounded task + target object/data/model + failure class. A new hour, operator, wording, or superficial retry does not reset it.

First failure records exact action/evidence/repair/dependencies at 1/2. Second persistent failure records attempt 2, moves to REPAIR_QUEUE at 2/2, quarantines dependencies, stops equivalent retries, and advances to independent work. Reopen only on documented new evidence/dependency/authorization/method or final repair sweep. CLOSED is never PASS.

Classifications: `ACCESS | EXTERNAL | DATA | SCIENTIFIC | ENGINEERING | GOVERNANCE | SCOPE`.

## Active blocker table

| Blocker ID | Gate/task | Class | Fail count | First failure | Second failure | Dependency/quarantine | Exact repair | Reopening condition | Status |
|---|---|---|---:|---|---|---|---|---|---|

## Required record template

```yaml
blocker_id: BLK-JFE-YYYY-NNN
gate: string
bounded_task: string
target: string
classification: ACCESS|EXTERNAL|DATA|SCIENTIFIC|ENGINEERING|GOVERNANCE|SCOPE
severity: LOW|MEDIUM|HIGH|CRITICAL
status: BLOCKED|REPAIR_QUEUE|QUARANTINED|REOPENED|CLOSED
owner: string|null
fail_count: 2
attempt_1: {timestamp: ISO-8601, action: string, evidence: [string], result: string, attempted_repair: string}
attempt_2: {timestamp: ISO-8601, action: string, evidence: [string], result: string, attempted_repair: string}
inputs_or_dependencies_changed: boolean
affected_gates: [string]
affected_artifacts_or_claims: [string]
quarantine_decision: string
independent_work_permitted: [string]
exact_future_repair_action: string
reopening_condition: string
human_approval_id: string|null
closure_limitation: string|null
history: [{timestamp: ISO-8601, from: string, to: string, reason: string}]
```

Closed records remain append-only and state whether repaired, scientifically closed with limitation, superseded through approved change control, or unresolved in the final gap report.
