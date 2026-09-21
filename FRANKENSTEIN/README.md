# FRANKENSTEIN™ — Evidence-Governed Accounting, Audit & Assurance Orchestrator

**NAAIL OpenLab specialist programme · Claude-enabled · model-replaceable · human-gated**

FRANKENSTEIN integrates deterministic audit analytics with a society of specialist accounting, audit, assurance, sustainability, cost and AI-governance agents. It is deliberately **not a third NAAIL core**.

- **Stable Knowledge Core™:** accounting, auditing, IFRS/assurance, ICFR, forensic, ESG, management accounting, evidence, professional judgment.
- **Replaceable Technology Core™:** Claude or other LLMs, Python, BERT, TimesFM, retrieval, graph systems, synthetic data and future tools.

## End-to-end workflow

**Transactions / ERP / Evidence → Deterministic Tests → Evidence Ledger → Specialist Agent Society → FRANKENSTEIN Leader → Evidence-Grounded Report → Human Approval Gate™**

## Specialist society

| Agent | Primary scope |
|---|---|
| Finance Controls | authorization, SoD, transaction integrity |
| Internal Audit | risk, control design/effectiveness, remediation |
| IFRS Reporting | reporting judgments and evidence needs |
| ICFR | financial-reporting controls and deficiency indicators |
| Forensic | anomalies and possible circumvention indicators |
| ESG & Sustainability Assurance | provenance, consistency and assurance readiness |
| Cost & AI FinOps | activity/time/token cost and cost-to-evidence |
| Operations Risk | resilience, accountability and workflow dependencies |
| AI & Data Governance | lineage, access, logs, model/agent governance |
| FRANKENSTEIN Leader | cross-domain synthesis and escalation |

## What is executable now

The public prototype contains its own deterministic transaction engine, synthetic demonstration data, structured evidence IDs, offline-safe specialist scaffolding, Claude API orchestration, Pydantic schemas, tests and GitHub Actions CI.

Run without any API call:

```bash
cd FRANKENSTEIN
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
PYTHONPATH=. python -m frankenstein.cli --offline
```

Run with Claude:

```bash
export ANTHROPIC_API_KEY="YOUR_KEY"
export CLAUDE_MODEL="claude-sonnet-5"
PYTHONPATH=. python -m frankenstein.cli
```

## Professional boundaries

FRANKENSTEIN does not autonomously issue an audit opinion, conclude fraud, declare IFRS/regulatory compliance, declare a material weakness, post accounting entries, modify controls, or sanction any person or counterparty. Material conclusions require corroborating evidence and qualified human review.

## NAAIL governance

FRANKENSTEIN follows the repository chain:

**Real Evidence → Evidence Passport → Analysis → Adversarial Review → Reproducibility → Human Approval**

See [ARCHITECTURE.md](ARCHITECTURE.md), [PORTFOLIO_INTEGRATION.md](PORTFOLIO_INTEGRATION.md) and [GOVERNANCE.md](GOVERNANCE.md).
