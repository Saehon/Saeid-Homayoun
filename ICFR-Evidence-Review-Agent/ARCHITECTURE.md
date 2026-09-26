# Architecture

```text
Customer / Reviewer
       |
       v
Web UI / API
       |
       v
Evidence Intake
  |-- text
  |-- PDF / spreadsheet (later)
  |-- Microsoft 365 / SharePoint connector (later)
       |
       v
Deterministic Evidence Layer
  |-- file/content hash
  |-- period/date checks
  |-- required-field checks
  |-- duplicate/reconciliation checks
       |
       v
Primary ICFR Review Agent
       |
       v
Exception + Risk Triage
       |
       v
Independent Reviewer / Falsification Agent
       |
       v
Evidence Passport + Decision Record
       |
       v
HUMAN GATE
       |
       +--> Approve
       +--> Return for evidence
       +--> Escalate
```

## Model strategy

The product must be provider-neutral.

- Primary reasoning provider: GPT/OpenAI or Azure OpenAI adapter.
- Independent challenger: a separately configured model/provider when practical, e.g. IBM Granite or another approved model.
- Deterministic checks remain independent of the LLM.
- Professional sign-off remains human.

## Commercial deployment target

Prototype: local/controlled Streamlit interface.

Product: web SaaS with API backend, database/object storage, Microsoft Entra ID, tenant isolation, telemetry, admin controls and billing integration.

## Data boundary

Customer evidence is application data, not public research data. Production architecture must separate customer tenants and must not place customer workpapers in the public GitHub repository.
