# AI Hiring Evidence Roadmap — portfolio improvements derived from job advertisements

**As of 2026-10-31. All numbers below are project targets, not results.** Source job requirements: [AI employer audit](AI_EMPLOYER_REQUIREMENTS_2026-10-31.md).

## Candidate profile

Accounting/auditing researcher with finance-leadership background and multiple AI research prototypes. The strongest industry transition is *financial LLM evaluation and evidence-governed AI programs*. The biggest employer-facing mismatch is the gap between architectural documentation/synthetic tests and **independently measured, deployed systems**.

## Priority engineering packages

| Package | Role families | Candidate repositories/branches | Acceptance gate, not yet met |
|---|---|---|---|
| A. Financial AI Evaluation Gold-50 | Google Finance Lead, Finance SME; Mistral Applied AI Evals; Vals AI | `Saehon/Saeid-Homayoun` [PR #195](https://github.com/Saehon/Saeid-Homayoun/pull/195) | 50 independently reviewed, appropriately licensed finance/audit cases, documented sampling and leakage safeguards, actual responses from at least two models, per-item correctness and evidence provenance |
| B. Audit & Control Evidence Sandbox | OpenAI GRC; Anthropic SOX; Frontier Assurance | `IFRS-AI-Inspector` [PR #3](https://github.com/Saehon/IFRS-AI-Inspector/pull/3); `IFRS-PCAOB-AI` private | Permission-scoped sample IAM and evidence service, 15 adversarial failure fixtures, testable access controls and independent reviewer sign-off; do not claim SOX certification |
| C. University Enterprise AI Pilot | OpenAI Applied AI Architect, Education; Anthropic Applied Architect | `Saeid-Homayoun-Test` [PR #17](https://github.com/Saehon/Saeid-Homayoun-Test/pull/17) | Working API/mock SSO/RBAC/retrieval, synthetic content, documented threat model and DPIA concerns, two configuration comparisons, measured P95 latency/cost, stakeholder-focused adoption brief |
| D. Usage-based Finance BI Prototype | Anthropic Finance Data Science; Microsoft AI business operations | `MACEI-AI-Cost-Manag` [PR #2](https://github.com/Saehon/MACEI-AI-Cost-Manag/pull/2) | Governed metric catalog with explicit grain, 12 months of synthetic or permitted usage events, SQL/dbt-like tests, time-valid dimensions, CFO dashboard, reconciliation and test outputs |
| E. Independent Evals Management | OpenAI Frontier Assurance/Governance; Mistral Evals | `Saeid-Homayoun-Test` [PR #16](https://github.com/Saehon/Saeid-Homayoun-Test/pull/16) | Independent annotator protocol, conflict register, frozen holdout, label disagreement, reproducible dashboard and signed approval; no self-certification |

## Common reproducibility contract

Every independently claimed model result needs **case_id, source rights, evidence_id, source_as_of, gold_labeler, gold_label_version, model_provider, model_id, model_version, prompt/template hash, tools/tool versions, response, API token counts, estimated billed cost, raw usage record, grader rule version, abstention flag, correctness finding, reviewer status and output checksum**. Preserve this in a permissioned run manifest; avoid committing private prompts, credentials, student or licensed data.

- **Demonstrated**: a tagged commit plus reproducible test output.
- **Measured**: true executed model evaluation with verifiable inputs, scoring, and source rights.
- **Independently reviewed**: non-author reviewer signed off.
- **Production**: real authorized deployment with usage and security records.
- **Published result**: frozen metadata, permissible publication, and external validation.

## Hard qualifications that GitHub cannot manufacture

- The Anthropic Audit Operations role's prior **Big Four** SOX 404/ICFR work.
- The Anthropic Dublin role's **10+ years PM/PMO** and **international entity setup experience**.
- The Anthropic Munich technical selling role's **German fluency**.
- The Scale AI Staff role's **7+ engineering years** and actual production AI ownership.
- Professional security clearances, work-location constraints, existing visa/work authorization and actual employer-specific leadership accomplishments.

## Suggested application presentation

Lead résumé with academic-domain strength, finance leadership, authored AI-research code and independently reproducible results. Keep model benchmarks, academic publications, upstream references and patent-sensitive private systems in **separate sections**. Reference *precise PR diffs* before they merge; after merge, link a tagged release and test artifact. Claims should be attributable and substantiated.

## Evidence limitations

The GitHub account's visible projects and past accomplishments do not fully establish personally held qualifications. Fit assessments in the requirements audit are qualitative screens, not estimated offer probabilities. Open roles can close at any time.
