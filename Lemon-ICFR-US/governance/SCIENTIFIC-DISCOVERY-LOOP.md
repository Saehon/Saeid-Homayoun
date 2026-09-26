# Scientific Discovery and Evolution Loop

## Purpose
This policy operationalizes Co-Scientist, scientific discovery, AlphaFold-inspired structure discovery, and AlphaEvolve-inspired controlled improvement inside Lemon.

## Loop A — Case-level scientific discovery
1. Observe evidence.
2. Form a precise ICFR question.
3. Generate multiple competing hypotheses.
4. Identify evidence that would support or falsify each hypothesis.
5. Execute deterministic and model-assisted tests.
6. Replicate important tests independently.
7. Run adversarial challenge.
8. Falsify where possible.
9. Escalate unresolved contradictions.
10. Human decides and records disposition.

## Loop B — Structure discovery
The Structure Discovery Engine may infer candidate links among:
`process, account, assertion, risk, control, evidence, exception, deficiency`.

For every proposed link record:
- source features/evidence,
- why the link is plausible,
- competing links,
- validation test,
- reviewer decision.

No inferred link automatically becomes canonical knowledge.

## Loop C — AlphaEvolve-style controlled improvement
Improvement candidates may include:
- prompt changes,
- routing changes,
- retrieval plans,
- deterministic rules,
- sampling logic,
- thresholds,
- agent compositions,
- test procedures.

Each candidate is evaluated on a frozen benchmark set.

### Graduation criteria
A candidate must:
- improve one or more declared metrics,
- not materially degrade critical metrics,
- preserve provenance,
- preserve reproducibility,
- preserve independent falsification,
- preserve human approval,
- pass security and rights checks.

Rejected candidates and failure reasons are retained.

## Benchmark dimensions
- evidence precision
- evidence recall
- unsupported-claim rate
- false-positive exception rate
- false-negative exception rate
- control-risk mapping accuracy
- reproducibility
- contradiction detection
- calibration
- human override rate
- time/cost per case

## Learning rule
`Learn → Evidence → Test → Challenge → Falsify → Human Approval → Graduate`

Validated learning may be promoted to the Mother repository through controlled review.
