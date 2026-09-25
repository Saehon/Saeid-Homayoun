# AWS Research Integration for Accounting, Auditing & Finance

This directory documents the AWS layer of the NAAIL OpenLab™ / FRANKENSTEIN™ provider-neutral research architecture.

## Purpose

AWS is treated as an **enterprise execution, governed-data and audit-evidence layer**, while GitHub remains the source of truth for code, manifests, provenance, documentation and small reproducible examples.

## Research stack

| AWS service | Role in accounting / audit / finance research |
|---|---|
| Amazon Bedrock | governed foundation-model access |
| Amazon Bedrock AgentCore | build and operate accounting/audit/finance agents |
| SageMaker AI | ML experiments and predictive models |
| Amazon S3 | SEC/XBRL, CAM/KAM, ICFR, ESG and other evidence/data-lake storage |
| AWS Glue | cataloguing and data engineering |
| Athena / Redshift | scalable financial-data querying and analytics |
| AWS CloudTrail | execution and activity traces |
| AWS Config | configuration and control-state evidence |
| AWS Audit Manager | automated evidence collection for audit/control assessment |

## Provider-neutral workflow

```text
GitHub
  ↓
Public / controlled research data
  ↓
S3 + Glue + Athena/Redshift
  ↓
Bedrock / AgentCore + SageMaker
  ↓
Accounting / Audit / Finance / ICFR / IFRS / ESG Agents
  ↓
CloudTrail + Config + Audit Manager evidence
  ↓
Independent Reviewer / Falsification
  ↓
Human Gate™
```

## Cross-provider comparison

AWS is evaluated beside:

- Microsoft Foundry + Fabric
- Anthropic / Claude
- Google / Gemini Enterprise Agent Platform
- Databricks Mosaic AI + MLflow + Unity Catalog
- OpenAI
- Hugging Face and open-source models

The aim is **comparative research and reproducible evaluation**, not vendor endorsement.

## Security boundary

No AWS access keys, secret keys, tokens, account identifiers or confidential client data should be committed to this public repository. Authentication belongs in local credential stores, IAM roles, workload identity, or GitHub Actions secrets when a future executable AWS pilot is approved.

## Current status

**Architecture/documentation integration only.** This repository does not claim that an AWS account, production workload or regulated audit environment is currently connected.

## Official resources

- Amazon Bedrock: https://aws.amazon.com/bedrock/
- Bedrock AgentCore: https://aws.amazon.com/bedrock/agentcore/
- SageMaker AI: https://aws.amazon.com/sagemaker/
- AWS Audit Manager: https://aws.amazon.com/audit-manager/
- AWS CloudTrail: https://aws.amazon.com/cloudtrail/
- AWS Config: https://aws.amazon.com/config/
- Amazon S3: https://aws.amazon.com/s3/

## Free/Open research data registry

A provenance-first registry now connects AWS free/open data to accounting, audit, finance and ESG research:

- [AWS Free/Open Data Registry](FREE_DATA_REGISTRY.md)
- [Machine-readable CSV](free-data-registry.csv)
- Hugging Face: https://huggingface.co/datasets/SADHON/aws-free-accounting-audit-finance-registry
- Kaggle: https://www.kaggle.com/datasets/sadhon/aws-free-accounting-audit-finance-registry

Priority domains: SEC/EDGAR/XBRL; macroeconomic stress; carbon accounting; Scope 3; climate risk; ESG assurance.
