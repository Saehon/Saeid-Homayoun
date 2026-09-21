# OpenAI Finance & Operations Audit Profile

**FRANKENSTEIN specialist implementation · OpenAI Agents SDK · evidence-grounded · adversarially challenged · human-gated**

This profile implements the finance-and-operations audit architecture developed around the publicly described OpenAI **Finance & Operations Audit Leader** role while remaining a replaceable technology implementation inside the broader NAAIL FRANKENSTEIN programme.

It does **not** replace FRANKENSTEIN, create a third NAAIL core, or imply affiliation with OpenAI.

## Why this profile exists

The root FRANKENSTEIN programme is model-replaceable. This profile demonstrates a concrete OpenAI Agents SDK implementation focused on:

- finance controls;
- forensic transaction analysis;
- treasury;
- revenue;
- procurement / accounts payable;
- payroll;
- tax;
- FP&A / management reporting;
- ICFR;
- AI & data governance;
- operations risk.

## Pipeline

~~~mermaid
flowchart LR
    A[Transaction Population] --> B[Deterministic Tests + SHA-256 Provenance]
    B --> C[11 Specialist Audit Agents]
    C --> D[Independent Evidence Challenger]
    D --> E[Audit Leader Synthesis]
    E --> F[Evidence / Run Metadata]
    F --> G{Human Approval Gate}
~~~

The key design principle is **deterministic evidence before generative interpretation**.

## Stronger-than-single-agent controls

- domain-routed evidence packets;
- structured Pydantic outputs;
- independent challenge/falsification;
- programmatic removal of unsupported finding IDs;
- confidence restriction when claims lack validated evidence;
- explicit abstention/missing-evidence requirements;
- SHA-256 source provenance;
- mandatory pending human review.

## Run locally

From the repository root:

~~~bash
cd FRANKENSTEIN
pip install -r openai_finops/requirements.txt
~~~

Deterministic-only:

~~~bash
PYTHONPATH=. python -m openai_finops.cli --deterministic-only
~~~

Full OpenAI specialist workflow:

~~~bash
export OPENAI_API_KEY="YOUR_KEY"
export OPENAI_MODEL="gpt-5.6-sol"

PYTHONPATH=. python -m openai_finops.cli \
  --csv sample_data/transactions.csv \
  --domains all \
  --objective "Assess finance and operations audit risks and identify evidence requiring follow-up."
~~~

Never commit a real API key.

## Deterministic audit tests

The profile currently checks duplicate transaction IDs, missing approval evidence, requester/approver segregation-of-duties conflicts, invalid timestamps, weekend/out-of-hours postings, robust amount outliers, large round-value transactions, missing accounting dimensions, negative transactions, repeated vendor/amount/day patterns, and high-value transactions lacking approval evidence.

These are risk indicators only; they do not prove fraud, misconduct, accounting error, regulatory breach or control failure.

## NAAIL / FRANKENSTEIN governance

**Evidence → Specialist Review → Independent Challenge → Programmatic Evidence Validation → Leader Synthesis → Human Approval Gate**

The profile does not autonomously issue an audit opinion, conclude fraud, declare compliance, classify a material weakness, post accounting entries, modify controls, or sanction a person/counterparty.

See [PROFILE_ARCHITECTURE.md](./PROFILE_ARCHITECTURE.md), [EVALUATION.md](./EVALUATION.md) and [JOB_ROLE_MAPPING.md](./JOB_ROLE_MAPPING.md).

## Status

**Version 0.2.0 · IMPLEMENTED research profile · not automatically VALIDATED or an EMPIRICAL_RESULT.**
