# Unified Data, AI & Research Platform Tooling

This repository uses a **provider-neutral, cross-platform research architecture** for accounting, auditing, assurance, finance, ICFR, IFRS and ESG.

GitHub remains the source of truth for code, configuration, documentation, manifests, small reproducible examples and provenance.

## Platform roles

| Platform | Primary role | Local/automation interface |
|---|---|---|
| GitHub | source code, provenance, releases, workflows and canonical research record | Git / GitHub Actions |
| Kaggle | benchmark datasets, notebooks and public reproducible experiments | `kaggle` |
| Hugging Face | public datasets, models, agents and dataset/model cards | `hf` |
| Databricks | scalable analytics, lakehouse, jobs, MLflow and governed AI workflows | `databricks` |
| AWS | secure data/evidence storage, model/agent execution and audit/control telemetry | AWS CLI / SDKs when configured |
| Google Drive | controlled research files, manuscripts and working documents | Google Drive integration |
| Microsoft | Foundry/Fabric finance/data/agent research | provider-specific APIs/SDKs |
| Anthropic / Claude | reasoning and financial-services agent workflows | provider-specific API/SDK |
| Google / Gemini | Gemini/ADK agents and scalable analytics | provider-specific API/SDK |
| OpenAI | agents, coding, research and cross-provider evaluation | provider-specific API/SDK |

## Canonical cross-platform record

- [Cross-Platform Integration Map](CROSS_PLATFORM_INTEGRATION.md)
- [AWS Research Integration](aws/README.md)
- [AWS Free/Open Data Registry](aws/FREE_DATA_REGISTRY.md)
- Hugging Face registry: https://huggingface.co/datasets/SADHON/aws-free-accounting-audit-finance-registry
- Kaggle registry: https://www.kaggle.com/datasets/sadhon/aws-free-accounting-audit-finance-registry
- Google Drive controlled record: https://docs.google.com/document/d/1KI8TfBi49kUH-RVBpypnccUvUD2ZeJDBbU3aqFonnKg/edit

## Existing repository integrations

### Kaggle

Kaggle is integrated through:

- `kaggle/`
- `.github/workflows/kaggle-sync.yml`
- `KAGGLE_API_TOKEN` as a GitHub Actions secret when publishing is enabled.

### Hugging Face

Hugging Face is integrated through:

- `huggingface/`
- Hugging Face publishing scripts and GitHub workflows;
- `HF_TOKEN` as a GitHub Actions secret when publishing is enabled;
- the public AWS accounting/audit/finance/ESG registry.

### Databricks

Databricks support is integrated through:

- `databricks/README.md`
- the unified installation scripts;
- `.github/workflows/data-platform-tooling-check.yml`.

Databricks authentication is intentionally not stored in the public repository.

### AWS

AWS is integrated at the architecture, evidence and data-registry layers through:

- `aws/README.md`
- `aws/FREE_DATA_REGISTRY.md`
- `aws/free-data-registry.csv`
- Bedrock / AgentCore / SageMaker research design;
- S3 / Glue / Athena / Redshift data design;
- CloudTrail / Config / Audit Manager evidence and control design.

No AWS credential is committed to this repository.

## One-command local CLI installation

### Windows PowerShell

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install-data-platform-clis.ps1
```

### macOS / Linux

```bash
bash scripts/install-data-platform-clis.sh
```

## Verify available data-platform CLIs

```text
kaggle --version
hf --help
databricks -v
```

AWS and model-provider CLIs/SDKs should be configured only when required by a specific experiment.

## Authentication

Do not commit credentials.

- Kaggle: `KAGGLE_API_TOKEN` in GitHub Actions secrets.
- Hugging Face: `HF_TOKEN` in GitHub Actions secrets.
- Databricks: workload identity/service principal preferred; otherwise secure `DATABRICKS_HOST` and `DATABRICKS_TOKEN`.
- AWS: use IAM roles, workload identity or secure GitHub Actions secrets for approved experiments.
- OpenAI / Anthropic / Google / Microsoft: use provider secrets or workload identity; never tracked files.

## Research architecture

```text
                         GitHub
              code + provenance + workflows
             /        |         |          \
            /         |         |           \
      Hugging Face  Kaggle  Google Drive  AWS / Databricks
      public data   benchmarks controlled    governed
      + models      + notebooks research     execution/data
            \         |         |          /
             \        |         |         /
              Provider-neutral agent layer
          OpenAI · Claude · Gemini · Microsoft · AWS
                         ↓
       Accounting · Audit · Finance · ICFR · IFRS · ESG
                         ↓
            Reviewer / Falsification / Replication
                         ↓
                      Human Gate™
```

The same validated source dataset can therefore be referenced once in GitHub, mirrored only where licensing permits, and reused across public benchmarks and controlled research without changing the canonical provenance record.
