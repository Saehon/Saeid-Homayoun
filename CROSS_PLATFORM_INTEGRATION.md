# NAAIL Cross-Platform AI, Data & Research Integration

_Last updated: 25 September 2026_

This file is the canonical public integration map for the **Saehon/Saeid-Homayoun** research ecosystem.

## Core architecture

| Platform | Role |
|---|---|
| **GitHub** | source of truth for code, architecture, provenance, manifests, workflows, releases and small reproducible examples |
| **Hugging Face** | public datasets, models, dataset/model cards and open AI research artifacts |
| **Kaggle** | benchmark datasets, executable notebooks and public replication/comparison |
| **Google Drive** | controlled research files, manuscripts, working documents and larger non-public research material |
| **AWS** | secure data, model/agent execution, evidence storage, audit/control telemetry and governed cloud research |
| **Databricks** | scalable lakehouse analytics, Mosaic AI, MLflow, Unity Catalog, tracing and reproducible data/ML workflows |
| **Microsoft** | Foundry/Fabric enterprise agents, finance/data analytics and governance research |
| **Anthropic / Claude** | reasoning, document analysis and financial-services agent workflows |
| **Google / Gemini** | multimodal agents, Gemini/ADK development and BigQuery-scale analytics |
| **OpenAI** | agent orchestration, coding, research, review and cross-provider evaluation |

## Canonical links

- GitHub master repository: https://github.com/Saehon/Saeid-Homayoun
- AWS integration: https://github.com/Saehon/Saeid-Homayoun/tree/main/aws
- AWS free/open data registry: https://github.com/Saehon/Saeid-Homayoun/blob/main/aws/FREE_DATA_REGISTRY.md
- AWS free-data CSV: https://github.com/Saehon/Saeid-Homayoun/blob/main/aws/free-data-registry.csv
- Hugging Face profile: https://huggingface.co/SADHON
- Hugging Face AWS data registry: https://huggingface.co/datasets/SADHON/aws-free-accounting-audit-finance-registry
- Kaggle profile: https://www.kaggle.com/sadhon
- Kaggle AWS data registry: https://www.kaggle.com/datasets/sadhon/aws-free-accounting-audit-finance-registry
- Databricks research area: https://github.com/Saehon/Saeid-Homayoun/tree/main/databricks
- External agent ecosystems: https://github.com/Saehon/Saeid-Homayoun/tree/main/external-agent-ecosystems
- Google Drive controlled integration record: https://docs.google.com/document/d/1KI8TfBi49kUH-RVBpypnccUvUD2ZeJDBbU3aqFonnKg/edit

## Free/open data layer

The AWS-linked registry currently prioritizes:

- SEC EDGAR / 10-K / XBRL for accounting, audit, CAM/KAM, ICFR, fraud and financial-reporting research;
- World Bank GDP, CPI and unemployment for macroeconomic and earnings-pressure controls;
- Open CEDA for Scope 3 and carbon accounting;
- Climate TRACE marginal build emissions rates;
- Global Carbon Budget data;
- NASA Earth Exchange climate-risk data.

Free access is **not** treated as automatic permission to redistribute. GitHub records provenance, terms and research use before any mirror is created.

## Research flow

```text
Public / controlled data
        ↓
Provenance + licence gate
        ↓
GitHub canonical record
   ↙        ↓        ↘
Hugging   Kaggle   Google Drive
  Face              controlled files
        ↓
AWS / Databricks / Microsoft data & execution layers
        ↓
OpenAI / Claude / Gemini / AWS / Microsoft / open-source agents
        ↓
Accounting · Audit · Finance · ICFR · IFRS · ESG analysis
        ↓
Independent Reviewer / Falsification
        ↓
Replication / reproducibility
        ↓
Human Gate™
```

## Governance

- Do not commit API keys, cloud credentials, tokens or confidential client data.
- Keep provider-specific adapters separate from accounting/audit domain logic.
- Record dataset version, code commit, model version, experiment ID and human decision.
- Preserve failed experiments and negative results where scientifically relevant.
- Public platform integration does not imply vendor affiliation, endorsement, audit assurance or regulatory approval.
- Material professional conclusions remain subject to evidence review and human judgment.
