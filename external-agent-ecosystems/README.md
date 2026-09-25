# External Agent Ecosystems for Accounting, Auditing & Finance

This folder is a curated integration index of external open-source repositories discussed for research and prototyping.

**Important:** External projects are referenced as upstream resources; their code is not copied or vendored here. Each upstream project remains subject to its own license, terms, and attribution requirements.

## Master Research Architecture

Start here:
- [Scientific Discovery Master Architecture](SCIENTIFIC-DISCOVERY-MASTER-ARCHITECTURE.md)\n- [Scientific Discovery Master Architecture v2.0](SCIENTIFIC-DISCOVERY-MASTER-ARCHITECTURE-V2.md) — additive systems-thinking redesign with Co-Scientist, structure-first reasoning, evolutionary experiment search and FRANKENSTEIN orchestration.

Master logic:
Systems Thinking → FT50/ABS4 → Replication → Co-Scientist → AlphaFold-inspired Structure → AlphaEvolve-style Experiment Evolution → FRANKENSTEIN Integration → Domain Agents → Evidence Verification → Reviewer/Falsification → Independent Replication → Human Approval → Publication → Learning Loop.

**Additive governance:** preserve existing artifacts, registries, benchmarks, pilots and negative results. New architecture layers organize and connect prior work rather than deleting it.

## Gold Research Data\n\n- [Gold Research Datasets Registry](GOLD-RESEARCH-DATASETS.md) — SEFD, SEC/EDGAR/XBRL, PCAOB inspection data, AAER and domain-specific reference-data design.\n- [EU IFRS + ESG/ESRS/VSME + Student Research Data Layer](EU-IFRS-ESG-VSME-STUDENT-RESEARCH.md) — ESEF/iXBRL, European sustainability reporting and thesis-ready data/replication standards.\n\n## Research Registry Index

### Cross-platform research
- [FT50/ABS4 Replication Registry](FT50-ABS4-REPLICATION.md)
- [arXiv × GitHub Research Registry](ARXIV-GITHUB-RESEARCH-REGISTRY.md)
- [Databricks × FT50/ABS4 Research Registry](DATABRICKS-FT50-ABS4-REGISTRY.md)

### Hugging Face
- [Hugging Face Registry](HUGGINGFACE_REGISTRY.md)
- [Hugging Face × FT50/ABS4 Registry](HUGGINGFACE-FT50-ABS4-REGISTRY.md)

### Kaggle
- [Kaggle Registry](KAGGLE_REGISTRY.md)
- [Kaggle × FT50/ABS4 Registry](KAGGLE-FT50-ABS4-REGISTRY.md)

### Executable pilots
- [Databricks / SEC-XBRL research area](databricks/01-sec-xbrl/)
- [Microsoft SEC/XBRL Pilot 001](databricks/01-sec-xbrl/README.md)
- [Pilot 001 configuration](databricks/01-sec-xbrl/pilot_001_config.yaml)
- [Evidence-grounded agent contract](databricks/01-sec-xbrl/agent_contract.json)

## Platform Roles

- **GitHub:** code, architecture, provenance and replication manifests.
- **Hugging Face:** public datasets, models and benchmark artifacts.
- **Kaggle:** executable public notebooks and benchmark comparison.
- **Google Drive:** controlled research files, manuscripts and working documents.
- **arXiv:** frontier research discovery.
- **Databricks / Delta:** scalable, versioned evidence and data engineering.
- **MLflow:** experiments, traces, metrics and model/prompt/configuration lineage.
- **AWS:** secure cloud execution, model/agent hosting, governed evidence storage and continuous audit/control telemetry through Bedrock/AgentCore, S3, SageMaker, CloudTrail, Config and Audit Manager.

Shared identity across systems should use:
**Experiment ID + Evidence ID + Dataset Version + Code Commit + Model Version + Human Decision.**

## Anthropic / Claude
- https://github.com/anthropics/financial-services — financial-services agents and skills.

## Microsoft
- https://github.com/microsoft/FinanceBenchmark — finance benchmark and evaluation.
- https://github.com/microsoft/RD-Agent — research and development agents, including quantitative research use cases.
- https://github.com/microsoft/agents — Microsoft Agents SDK.
- https://github.com/microsoft/agent-governance-toolkit — agent governance and auditability.
- https://github.com/microsoft/PAX — Microsoft repository discussed for audit/log analytics.
- https://github.com/microsoft/ai-agents-for-beginners — agent development/security learning examples.
- https://github.com/MicrosoftDocs/dynamics365smb-docs — Dynamics 365 Business Central documentation, including finance/payables material.

## OpenAI
- https://github.com/openai/openai-agents-python — Agents SDK for Python.
- https://github.com/openai/openai-agents-js — Agents SDK for JavaScript/TypeScript.
- https://github.com/openai/codex — Codex.
- https://github.com/openai/plugins — plugin/skill examples and resources.

## Google / Gemini
- https://github.com/google-gemini/cookbook — Gemini API examples.
- https://github.com/google/adk-python — Agent Development Kit for Python.
- https://github.com/google/adk-java — Agent Development Kit for Java.
- https://github.com/GoogleCloudPlatform/generative-ai — Google Cloud generative-AI samples.
- https://github.com/GoogleCloudPlatform/agent-starter-pack — production-oriented agent starter templates.

## AWS
- https://aws.amazon.com/bedrock/ — Amazon Bedrock for governed access to foundation models.
- https://aws.amazon.com/bedrock/agentcore/ — Amazon Bedrock AgentCore for building and operating AI agents.
- https://aws.amazon.com/sagemaker/ — SageMaker AI for ML research and model workflows.
- https://aws.amazon.com/s3/ — S3 as an evidence/data-lake layer for research datasets.
- https://aws.amazon.com/cloudtrail/ — CloudTrail for execution/activity traceability.
- https://aws.amazon.com/config/ — AWS Config for configuration/control evidence.
- https://aws.amazon.com/audit-manager/ — AWS Audit Manager for automated evidence collection and audit assessments.
- [Repository AWS research integration](../aws/README.md)

## Community accounting/audit examples
- https://github.com/openaccountant/skills — accounting/finance skills; community project.
- https://github.com/rominirani/financial-audit-agent-tutorial — financial audit agent tutorial; community example.
- https://github.com/rajanm/retail-enterprise-agents — enterprise agents including vendor recovery/audit examples; community project.

## Domain Research Programs

SEC/XBRL → Audit Assertions → ICFR → CAM/KAM → Fraud/AAER → IFRS Judgment → ESG/VSME Assurance → Evidence/Citation Verification → Cross-Provider Evaluation → Replication/Falsification.

## Research integration map

External data / SEC-XBRL / ERP / research files
→ Databricks/Delta + Evidence Graph
→ Accounting & Finance analysis
→ Audit Evidence
→ Assertions / ICFR
→ CAM/KAM / Fraud / IFRS / ESG
→ OpenAI / Claude / Gemini / Microsoft / AWS / Databricks / open-source agents
→ FRANKENSTEIN orchestration
→ deterministic controls
→ independent Reviewer / Falsification
→ replication
→ human approval
→ research outputs
→ learning loop.

## Recommended use

1. Treat external repositories as upstream references rather than automatically merging their code.
2. Pin exact versions/commits before a reproducible experiment.
3. Record licenses and attribution before reusing code.
4. Keep provider-specific adapters separate from domain logic.
5. Benchmark providers on identical data, prompts/tasks, evidence, and evaluation criteria.
6. Preserve negative results and failed experiments.
7. Require human review for consequential accounting, audit, assurance, or financial conclusions.
8. Do not delete existing research artifacts when adding new architecture layers.

_Last curated and reorganized: 2026-09-25._
