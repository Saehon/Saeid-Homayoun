# Forward-Deployed Customer-Zero Playbook

## Purpose

Use forward-deployed product engineering to learn the customer workflow quickly without turning the company into a consultancy.

The operating model takes a lesson from the public DXC/Anthropic approach announced in 2026: prove AI internally first, then embed trained engineers directly in customer environments for mission-critical adoption.

## Pilot pod

- Domain Lead — ICFR/accounting/audit workflow.
- Forward-Deployed Product Engineer — integrations and configuration.
- AI/Evaluation Engineer — prompts, benchmark and falsification.
- Customer Control Owner — owns the process.
- Human Reviewer — remains accountable for approval.

One startup person may cover multiple roles early.

## Customer Zero

Before an external pilot:
1. define 10–20 controls;
2. create clean and seeded-exception evidence packs;
3. run deterministic + primary model + challenger;
4. measure precision, recall and overrides;
5. record failures;
6. fix only failures that generalize.

Do not use confidential employer, university or client information without explicit authorization.

## 30–60–90 design-partner model

Days 0–30 — Observe and bound:
- one named process;
- 10–25 controls;
- evidence systems and formats;
- baseline review time;
- signed success metrics;
- read-only ingestion first.

Exit gate: one workflow, one owner, one baseline, one measurable problem.

Days 31–60 — Shadow mode:
- agent runs beside existing process;
- no automated approvals;
- compare agent flags with human review;
- classify false positives and negatives;
- capture override reasons;
- harden evidence lineage.

Exit gate: acceptable benchmark performance and no unresolved critical data-boundary issue.

Days 61–90 — Controlled production:
- reviewers use the product in live workflow;
- Human Gate remains mandatory;
- track time saved and exceptions found;
- measure support burden;
- generalize only repeated configuration patterns.

Exit gate: signed pilot outcome and commercial decision.

## Anti-consulting rule

Every request is classified as:
1. Configuration.
2. Reusable capability.
3. Customer-specific integration behind an adapter.
4. Bespoke exception that does not enter the core unless strategic.

## Forward-Deployed scorecard

Track:
- controls reviewed;
- evidence items reviewed;
- review minutes before/after;
- precision/recall;
- false positives/negatives;
- reviewer overrides;
- unsupported model claims;
- integration hours;
- FDE hours/week;
- support incidents;
- willingness to pay;
- features requested by more than one customer.

## Internal FDE certification

1. ICFR/SOX fundamentals.
2. Control and evidence design.
3. Prompt-injection/data-boundary training.
4. Model/provider operation.
5. Evaluation/falsification.
6. Security and incident handling.
7. Deployment runbook.
8. Professional-boundary rules.
9. Supervised customer deployment.
10. Practical assessment.

Brand promise: domain + engineering + evidence governance, not merely model certification.
