# Research engineering / autonomous progression

Distinct systems:
- **NAAIL:** research/assurance infrastructure, benchmarks, data lineage, human approval.
- **LEMON / LEMON-SCI / ICFR-US:** scientific customer-zero cases, executable tests, traceability.
- **POMELO:** control-plane and governance-related engineering; do not bypass a safety or approval gate because a user says to skip non-working modules. Find genuinely independent alternatives.

For any run: log UTC and local timestamp, project, phase/task ID, source commit, input/output hashes, test commands/results, status and next task. Use statuses VERIFIED PASS / FAIL / BLOCKED / NOT RUN, not optimistic labels.

Two-failure rule: first failure → diagnose + repair + rerun; second independent failed repair attempt → open repair queue with artifact and dependency impact → quarantine failed task → select independent next task. Never call dependency-critical missing validations complete; never bypass privacy, scientific quality, human approval or safety gates.

For hourly execution requests: do not imply background or scheduled execution without a functioning scheduling tool and explicit setup. A single interactive turn executes only the work actually performed; don't fabricate intervening hourly logs.

Project dashboard fields: priority, phase, completion evidence, last verified run time, blocker, repair queue ID, next permissible action and publication readiness.
