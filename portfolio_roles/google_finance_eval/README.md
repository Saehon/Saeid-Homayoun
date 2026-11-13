# Google DeepMind — Finance Expert Lead, Gemini Data — verifiable portfolio demonstration

**Independent academic portfolio; not affiliated with or endorsed by the employer.**

**Source job:** https://www.google.com/about/careers/applications/jobs/results/84832883583132358-finance-expert-lead-gemini-data-deepmind?page=10&sort_by=date

**Objective:** Synthetic finance task evaluation with deterministic numeric rubrics, evidence-ID grounding, and explicit failure modes.

## Run (Python 3.9+, standard library only)

From the repository root:

```bash
python portfolio_roles/google_finance_eval/demo.py
python -m unittest discover -s portfolio_roles/google_finance_eval/tests -v
```

## What this actually demonstrates

- Explicit structured inputs and deterministic checks (no external API calls).
- Fail-closed or review-gated reporting; failures are visible, not hidden.
- Four unit tests with synthetic fixtures, including counterexamples.
- A small, inspectable portfolio sample linked to a published job description.

## Limitations and reproducibility disclosure

This is an independently authored **synthetic demonstration**, not evidence of an employer partnership, production deployment, audited compliance, successful AI model safety, or full model evaluation. No restricted standards text, licensed research data, employer records, third-party code, private POMELO algorithms or identifiable financial client data are included. Verification status of external systems remains unknown. The intended next step is an evaluation protocol against a licensed or public dataset with independent human review, documented error taxonomy, coverage metrics and CI results.

**Responsible investigator:** Saeid Homayoun (ORCID: 0000-0002-2536-0446).
