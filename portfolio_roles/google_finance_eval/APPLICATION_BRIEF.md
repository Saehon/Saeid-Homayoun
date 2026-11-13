# Application-ready project summary — Google DeepMind — Finance Expert Lead

**Authorship statement:** This `portfolio_roles/google_finance_eval` contribution is a new, independent, role-specific research demonstration. The host repository may contain third-party material; ownership of all pre-existing repository content is **not claimed**. Nothing here establishes employment, partnership or endorsement by the named employer.

## Challenge addressed

financial reasoning evaluation, evidence grounding, quantitative rubric design, error taxonomy.

## What has been developed and verified

- A Python standard-library demonstration with explicit decision states and negative tests.
- Ten synthetic contract cases: eight designed to be blocked, two ready for review.
- A comparison with a weak *always-ready* baseline, plus block-class precision/recall/F1, case-level reasoning and dataset SHA-256.
- GitHub Actions continuous integration with machine-readable JSON reports.
- Role-specific evaluation and scientific validation gates.

**Evidence level:** successfully executed synthetic regression/contract checks only. The gold labels were designed from the same rule specification, so the benchmark does not demonstrate out-of-sample predictive accuracy or a genuine AI model comparison.

## 90-second interview demo

Run the deterministic finance benchmark and explain a nonmatching number and an unsupported evidence citation.

## Suggested CV sentence (accurate only while CI remains green)

"Designed and implemented a reproducible, role-aligned Python evidence-evaluation prototype with fail-closed cases, test automation, structured quality metrics, and documented governance limitations."

## Next engineering/research milestone

Run authorized FinanceBench 150-item sample with two genuine model prediction files. Independent assessors adjudicate numeric and evidence equivalence.

## Release / disclosure gates

| Gate | Current status |
|---|---|
| Code created and unit tested | PASS — GitHub Actions evidence |
| Synthetic contract benchmark | PASS — internally constructed cases |
| External or domain-licensed data | NOT YET VERIFIED |
| Real LLM or production-system evaluation | NOT RUN |
| Independent/blind expert code and data review | PENDING |
| Ethics, security, privacy and IP review where required | PENDING |
| Production assurance, compliance or deployment certification | NOT CLAIMED |

**Research investigator:** Saeid Homayoun · ORCID: https://orcid.org/0000-0002-2536-0446.
