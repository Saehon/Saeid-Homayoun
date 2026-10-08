# P0.5 Gate Ledger, Repair Queue, and Completion Control System

Status: FROZEN v1.0  
Gate: P0.5  
Date: 2026-10-05  
Scope: NAAIL Trust Finance / Multi-LLM Financial Disagreement

## 1. Purpose

This control system defines how the 60 canonical gates are counted, transitioned, evidenced, blocked, repaired, closed, and finally completed. It prevents planning activity, documentation volume, commits, CI, elapsed time, or repeated attempts from being misreported as scientific progress.

P0.5 evaluates whether the control mechanism is operational. It does not validate later scientific gates, empirical data, model outputs, or manuscript claims.

## 2. Canonical records

| Record | Function | Canonical rule |
|---|---|---|
| `MASTER_PLAN_60_GATES.md` | Defines the 12 phases and 60 gate objectives | Scope authority; gates change only through P0.4 change control |
| `GATE_LEDGER.md` | Stores one row per gate and evidence-backed status counts | Sole project-level completion counter |
| `RUN_LOG.md` | Append-only record of each bounded run | Records state, actions, evidence, failures, saves, and next gate |
| `OPEN_REPAIR_QUEUE.md` | Persistent blocker and two-failure history | A new run never resets attempts or erases history |
| P0.1–P0.5 documents | Define research, governance, firewall, change control, and completion rules | Frozen design; implementation claims remain separate |

The shared portfolio table is outside this project's write authority. This project updates only its own canonical records.

## 3. Ledger invariants

After every mutation the ledger must contain exactly 60 unique gate IDs (P0.1–P11.5), assign exactly one status to each, and have status counts summing to 60. PASS, CLOSED, and PARTIAL require linked evidence or limitations. BLOCKED and REPAIR_QUEUE require stable blocker IDs. ACTIVE identifies only the currently owned bounded scope and does not imply progress.

No gate is promoted by commits, CI, elapsed time, documentation volume, or visiting a phase. Superseded or quarantined evidence cannot support PASS. The next gate is the highest-priority scientifically admissible gate after dependency and writer-lock checks. Ledger v1.4 contains 60 individual rows rather than aggregated phase ranges.

## 4. Status definitions and transitions

| Status | Meaning | Permitted progression |
|---|---|---|
| NOT_STARTED | No bounded gate work begun | ACTIVE or BLOCKED |
| ACTIVE | Authorized work in progress | PARTIAL, PASS, BLOCKED, or NOT_STARTED after mutation NO-OP |
| PARTIAL | Some criteria evidenced; gate incomplete | ACTIVE, PASS, BLOCKED, or REPAIR_QUEUE |
| PASS | Every frozen gate criterion evidenced | Remains PASS unless a documented change/deviation quarantines prior evidence |
| BLOCKED | A specific condition prevents valid progress/acceptance | ACTIVE on actionable change, REPAIR_QUEUE after second failure, or CLOSED with limitation |
| REPAIR_QUEUE | Two persistent failures; equivalent retries stopped | ACTIVE only on reopening condition/final sweep, or CLOSED; PASS only after repaired work independently satisfies criteria |
| CLOSED | Scientifically impossible/inappropriate and explicitly closed | Reopen only by change control; never counted as PASS |

FAIL is an attempt outcome, not a gate status. It remains in the run/blocker history.

## 5. Gate acceptance record

Before PASS, record the gate/versioned criteria; dependencies and data classification; work and evidence IDs; appropriate tests/falsification/readback; GitHub commit/path and Drive ID/revision; limitations and non-claims; fail count and linked blocker/deviation/change IDs; required human approval; and exact next gate.

Design gates may PASS when design criteria are complete, but must be labelled design-only and never imply operational or empirical validation.

## 6. Persistent failure identity

The identity is `gate + bounded task + target object/data/model + failure class`. A retry remains the same progression when inputs, dependencies, method, and repair are materially unchanged. A new hour, operator, wording, or superficial parameter change does not reset it.

A new progression requires new evidence, repaired dependency, materially changed method, new authorization, verified provider recovery, or final repair sweep. Previous history remains linked.

## 7. Two-failure move-on rule

First failure: record timestamp, exact action, target, observed result, evidence/log, likely cause, repair attempted, dependencies, and fail count 1/2. Set PARTIAL or BLOCKED; never PASS.

Second persistent failure: record the second attempt; create/update `BLK-JFE-YYYY-NNN`; set 2/2; move to OPEN REPAIR QUEUE; stop equivalent retries; quarantine dependency-critical outputs; and advance to the next independent admissible gate.

If no later gate is admissible, report the dependency-critical stop. Never skip it, fabricate results, or convert it to CLOSED/PASS merely to continue.

## 8. Blocker classes

| Class | Examples | Default handling |
|---|---|---|
| ACCESS | Missing permission, unavailable licensed data, authentication barrier | Preserve evidence; do not circumvent |
| EXTERNAL | Provider outage, rate limit, upstream removal | Reopen only on verified recovery |
| DATA | Missing, corrupt, conflicting, contaminated, non-redistributable | Quarantine affected outputs; specify lawful repair |
| SCIENTIFIC | Unsupported criterion, invalid construct, failed falsification, non-identification | Preserve failure; redesign prospectively only |
| ENGINEERING | Code, test, environment, serialization, reproducibility | Preserve logs; bounded repair; CI is not scientific PASS |
| GOVERNANCE | Approval, writer lock, privacy/license, sealed-test restriction | Mutation NO-OP or quarantine until authorized |
| SCOPE | Unauthorized task or one-PR/canonical-plan conflict | Stop mutation; use change control |

## 9. Required repair record

Each blocker records ID, gate/task, class, severity, owner/status; both failure timestamps/evidence; inputs/dependencies and changes; attempted repairs; affected gates/artifacts/claims; quarantine and independent work; exact future repair and authority; reopening condition/final-sweep state; closure limitations/approval; and append-only state history.

The queue may be empty, but its schema and zero-state remain versioned.

## 10. Dependency and quarantine

Failure propagates only along real dependencies; no cross-project dependency is invented. Independent later gates may proceed. Dependent outputs inherit quarantine and cannot support PASS or claims. Temporal-integrity, provenance, partition, or sealed-test failures block dependent confirmatory inference. Missing external-model output is never fabricated.

## 11. Run-log minimum

Every run records run ID/time; phase/gate/task; starting branch/HEAD/PR/CI, Drive state, counts, queue, and writer lock; attempted/completed work; evidence/files; tests/readback; commits/final HEAD and Drive IDs; failure count/class/queue change; ending counts/quarantines; and exact next gate. Writer-lock NO-OP runs record the lock and make no mutation.

## 12. Completion levels

A phase completes only when all five gates are PASS or scientifically CLOSED with limitations. A visited phase is not complete.

The first pass completes when all 60 gates have an evidence-backed disposition and none remains NOT_STARTED merely through omission. First pass is not final completion.

Final completion requires: all 60 gates PASS or scientifically CLOSED; final repair sweep; fresh falsification; human-approved preregistered sealed OOS; integration and clean reproduction; independent/human review; claim-to-evidence/code/table/manuscript traceability; lawful public-release controls; reconciled GitHub/Drive readback; and a final report separating PASS, CLOSED, and unresolved limitations.

A manuscript draft, POC, commit, CI pass, or 60 visited gates is insufficient.

## 13. P0.5 control audit

The audit verified 12 phases × 5 gates; upgraded the ledger to 60 unique rows with counts summing to 60; confirmed the pre-decision state of P0.1–P0.4 PASS and 56 NOT_STARTED; confirmed an empty repair queue and run history JFE-001–JFE-004; found no writer-lock artifact; confirmed Draft PR #112 as the sole scope PR; confirmed protected main unchanged; and reconciled Drive/GitHub controls at run start.

One local patch-bundle attempt failed before external mutation because it targeted the same temporary ledger twice. This ENGINEERING attempt 1/2 was repaired by separate replacement artifacts; no repository/Drive state was changed and no blocker entered the queue.

## 14. Acceptance and conclusion

P0.5 may PASS only with one 60-gate reconciled ledger, append-only run log, persistent two-failure repair queue, explicit transitions, acceptance/completion rules, dependency/quarantine logic, and dual-save/readback.

All design and audit criteria are present. P0.5 is PASS for the governance/control system. P0 is complete 5/5 for governance/control design only; no P1–P11 scientific validation is implied.
