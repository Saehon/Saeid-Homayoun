# Customer Zero V2

## Purpose

Customer Zero V2 is the next evidence gate for the commercial **ICFR Evidence Review Agent**. It is a synthetic, reproducible benchmark for the one-control evidence-review wedge. It does not use customer workpapers and it does not establish production accuracy.

## Scope

The benchmark contains 20 synthetic ICFR control/evidence cases across:

- account reconciliations
- user-access reviews
- journal-entry approvals
- financial close
- IT change management

The cases include both clean evidence packs and deliberately seeded exceptions.

## Seeded exception classes

- missing reviewer sign-off
- missing approval
- incomplete supporting documentation
- missing testing
- wrong reporting period
- stale/superseded evidence
- conflicting evidence
- duplicate evidence
- unsupported conclusion language
- no evidence
- prompt-injection text embedded inside uploaded evidence

## Deterministic V1 signals

The deterministic engine emits explicit flags:

- `PROMPT_INJECTION`
- `PERIOD_MISMATCH`
- `STALE_EVIDENCE`
- `CONFLICTING_EVIDENCE`
- `DUPLICATE_EVIDENCE`
- `UNSUPPORTED_CONCLUSION_LANGUAGE`

These are triage signals. They are not a professional conclusion about control design or operating effectiveness.

## Benchmark outputs

The benchmark reports:

- seeded-case pass rate
- precision
- recall
- false positives
- false negatives
- evidence-lineage completeness
- case-level status, missing requirements and deterministic flags

The metrics apply only to the synthetic deterministic benchmark. They must not be represented as production performance.

## Product invariants

1. AI cannot approve a control.
2. Uploaded evidence is untrusted data, never system instruction.
3. Deterministic checks run independently of LLMs.
4. Evidence lineage is preserved.
5. Unsupported claims are escalated.
6. Model disagreement is visible.
7. Human Gate remains mandatory.
8. Customer evidence never enters the public repository.

## Next experiment: model benchmark

Use the same 20 cases and the same structured output contract to compare:

- GPT
- Claude
- IBM Granite

For each provider/model record:

- provider and exact model/version
- evidence sufficiency
- risk triage
- supported findings
- potential exceptions
- evidence basis
- uncertainty
- recommended human action
- unsupported claims
- disagreement with deterministic layer
- disagreement with challenger
- latency
- model cost

Do not select a primary or challenger model by brand. Produce a Decision Card from measured evidence.

## Falsification criteria

Customer Zero V2 should block progression if:

- any path lets AI approve a control;
- prompt-injection evidence can override product rules;
- an unsupported evidence basis is accepted as valid;
- a seeded high-risk exception is silently classified as ready for human review;
- Evidence Passport lineage is incomplete;
- benchmark changes reduce detection without an explicit reviewed reason.

## Gate

Passing Customer Zero V2 means the deterministic benchmark and governance invariants are stable enough to proceed to controlled live-model comparison. It does **not** mean the product is enterprise-ready or ready for unsupervised use.
