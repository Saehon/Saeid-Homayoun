# FRANKENSTEIN Finance & Operations Audit System — NAAIL OpenLab

**Specialist programme inside NAAIL OpenLab's Audit Agent Lab.**

FRANKENSTEIN is an evidence-governed research prototype for finance and operations internal audit. It combines deterministic transaction analytics, specialist AI reviewers, independent evidence challenge, structured executive synthesis, and a mandatory Human Approval Gate.

> **Architecture status:** specialist programme / replaceable implementation. FRANKENSTEIN is **not** a third NAAIL core and does not alter the frozen Two-Core Constitution.

## NAAIL placement

FRANKENSTEIN inherits the NAAIL architecture:

**Stable Knowledge Core → Evidence / Data → Replaceable Technology Core → Specialist Audit Agents → Adversarial Verification → Evidence Passport → Human Approval Gate**

The permanent NAAIL cores remain exactly:

1. **Stable Knowledge Core** — accounting, auditing, finance, ICFR, governance, professional judgment, evidence standards and research methods.
2. **Replaceable Technology Core** — LLMs, agent orchestration, analytics libraries, APIs, connectors, model providers and implementation frameworks.

FRANKENSTEIN sits **below those cores as a specialist audit programme**. Its model provider, SDK, thresholds and specialist implementation can be replaced without changing NAAIL's permanent scientific meaning.

## Pipeline

~~~mermaid
flowchart LR
    A[Transaction Population] --> B[Deterministic Tests + SHA-256 Provenance]
    B --> C[11 Specialist Audit Agents]
    C --> D[Independent Evidence Challenger]
    D --> E[Audit Leader Synthesis]
    E --> F[Evidence Passport / Run Metadata]
    F --> G{NAAIL Human Approval Gate}
~~~

## Specialist domains

| Domain | Primary audit lens |
|---|---|
| Finance Controls | Authorization, classification, transaction integrity |
| Forensic | Anomalies, duplicates, timing and circumvention indicators |
| Treasury | Cash disbursements, liquidity and high-value payments |
| Revenue | Validity, credits/reversals and cutoff evidence |
| Procurement / AP | Procure-to-pay, vendor, approval and duplicate-payment risk |
| Payroll | Payroll/people-cost controls with explicit abstention when evidence is absent |
| Tax | Tax-process implications and required corroboration |
| FP&A | Budget attribution, unusual spend and management reporting |
| ICFR | Financial-reporting control objectives and evidence sufficiency |
| AI & Data Governance | Data quality, lineage, provenance and model-use boundaries |
| Operations Risk | Resilience, accountability and third-party dependencies |

## Deterministic analytics

The current research prototype tests for duplicate IDs, missing approvals, segregation-of-duties conflicts, invalid timestamps, weekend/out-of-hours activity, robust amount outliers, large round values, missing accounting dimensions, negative transactions, repeated vendor/amount/day combinations, and high-value transactions lacking approval evidence.

These are **risk indicators only**. They are not proof of fraud, error, misconduct, regulatory breach or control failure.

## Quick start

From the repository root:

~~~bash
python -m venv .venv
source .venv/bin/activate
pip install -r NAAIL-OpenLab/audit_agents/frankenstein_finops/requirements.txt
cd NAAIL-OpenLab/audit_agents
~~~

Deterministic-only run:

~~~bash
python -m frankenstein_finops.cli --deterministic-only
~~~

Full specialist workflow:

~~~bash
export OPENAI_API_KEY="YOUR_KEY"
python -m frankenstein_finops.cli \
  --csv sample_data/transactions.csv \
  --domains all \
  --objective "Assess finance and operations audit risks and identify evidence requiring follow-up."
~~~

Never commit a real API key.

## Governance

Every material conclusion must pass:

**Deterministic Evidence → Specialist Review → Independent Challenge → Executive Synthesis → Evidence Passport / Provenance → Human Approval**

The system intentionally does not issue an audit opinion, determine that fraud occurred, accuse a person or counterparty, classify an ICFR material weakness from transaction data alone, claim regulatory compliance, or make autonomous accounting entries/control changes.

## Evaluation

See [EVALUATION.md](./EVALUATION.md). The system should be evaluated for detection quality, false positives/negatives, evidence completeness, unsupported-reference rejection, calibration, abstention quality, challenge yield, reproducibility, provenance, human override and remediation usefulness.

## OpenAI role mapping

See [JOB_ROLE_MAPPING.md](./JOB_ROLE_MAPPING.md). This is an independent portfolio/research implementation inspired by publicly described finance-and-operations audit capabilities. It is not affiliated with, endorsed by, or built for OpenAI.

## Status

**Version 0.2.0 · IMPLEMENTED research prototype · not automatically EXECUTED, VALIDATED or an EMPIRICAL_RESULT under NAAIL portfolio governance.**
