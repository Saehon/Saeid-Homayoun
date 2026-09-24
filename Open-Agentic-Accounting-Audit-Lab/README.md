# Open Agentic Accounting & Audit Lab

**Version 0.3 — updated 24 September 2026**

A provider-neutral research and teaching project for testing AI agents in **financial accounting, auditing, ICFR/internal control, corporate governance, CAM/KAM, IFRS, and ESG/sustainability reporting**.

## Research objective

The project separates the **reasoning model** from the **accounting/audit procedure**, evidence layer, deterministic controls, and human approval. The same case can therefore be tested with Claude, GPT/Codex, Gemini, Microsoft/Azure-hosted models, Kimi, DeepSeek, or local models while keeping the domain workflow fixed.

## Current research design

- **30 cases** across the United States, Europe and Asia.
- **7 experimental conditions (T0–T6)** from human-only work to provider-neutral, cross-model, control-gated AI with human approval.
- **210 core case-treatment cells** before model-provider replications.
- Up to approximately **1,260 case-treatment-provider cells** when six AI provider families are included, subject to the final replication protocol.
- Ten specialist agents plus an Orchestrator: Financial Accounting, Audit Testing, Evidence, ICFR/Internal Control, Corporate Governance, CAM, KAM, IFRS, ESG and Reviewer.

## Core architecture

```text
Source documents / public filings / synthetic cases
                    |
                    v
          Evidence & provenance layer
             Docling / XBRL / SEC
                    |
                    v
  +---------------- Specialist agents ----------------+
  | Financial Accounting | Audit Testing | Evidence   |
  | ICFR/Internal Control | Corporate Governance      |
  | CAM | KAM | IFRS | ESG | Reviewer                |
  +----------------------------------------------------+
                    |
                    v
       Deterministic verification & policy gate
          CPA Skills / FinanceSkills / closegate
                    |
                    v
          Cross-model challenge / replication
 GPT | Claude | Gemini | Microsoft/Azure | Kimi | DeepSeek
                    |
                    v
               Human approval gate
                    |
                    v
        Evidence-backed research output
```

## Project files

- [PROPOSAL.md](PROPOSAL.md) — integrated research and implementation proposal.
- [docs/AGENT_CATALOG.md](docs/AGENT_CATALOG.md) — free/open or research-accessible agent/tool catalogue.
- [docs/DATA_SOURCES.md](docs/DATA_SOURCES.md) — GitHub, Kaggle, Hugging Face, SEC, PCAOB, ESMA and IFRS/ISSB sources.
- [docs/EXPERIMENT_DESIGN_T0_T6.md](docs/EXPERIMENT_DESIGN_T0_T6.md) — experimental protocol and 30-case design.
- [config/agents.yaml](config/agents.yaml) — specialist-agent responsibilities and gates.
- [config/providers.example.yaml](config/providers.example.yaml) — provider-neutral model routing template.
- [src/provider_router.py](src/provider_router.py) — minimal provider-routing scaffold.
- [THIRD_PARTY_LICENSES.md](THIRD_PARTY_LICENSES.md) — licensing and reuse notes.
- [CHANGELOG.md](CHANGELOG.md) — version history.
- [project_manifest.json](project_manifest.json) — machine-readable project metadata.

## Google Drive mirror

- Project folder: https://drive.google.com/drive/folders/1_Zaq6PFJIZUX9O6AzBvmrf-_CRRWw_5s
- Integrated Research Proposal V1: https://docs.google.com/document/d/16Mq0zEZJsTNd73tGzfnE86WhRL2je4fUC92iiVJgINk/edit

## Recommended external components

| Component | Function | Source |
|---|---|---|
| CPA Skills | Reconciliation, extraction, tie-outs, audit sampling, JE anomaly tests | https://github.com/adoptai/cpa-skills |
| FinanceSkills | IFRS/GAAP, finance, audit and compliance skills | https://github.com/GAJETOso/financeskills |
| closegate | SOX/SoD, materiality, HITL approval and audit log | https://github.com/esploro-group/closegate |
| Docling MCP | Document parsing and evidence extraction | https://github.com/docling-project/docling-mcp |
| SEC EDGAR MCP | SEC filings and XBRL evidence | https://github.com/stefanoamorelli/sec-edgar-mcp |
| AI4SustainableX | ESG/sustainability evidence-grounded workflows | https://github.com/lokeshbohra/ai4sustainablex |
| Google ADK | Multi-agent orchestration | https://github.com/google/adk-docs |
| Microsoft Agent Framework | Microsoft/Azure multi-agent orchestration | https://github.com/microsoft/agent-framework |
| LiteLLM | Provider-neutral LLM gateway | https://github.com/BerriAI/litellm |

## Provider comparison

The research platform is structured to compare the same accounting or audit task across:

**OpenAI GPT/Codex | Anthropic Claude | Google Gemini | Microsoft/Azure | Kimi/Moonshot | DeepSeek | optional local Ollama models**

Provider choice must not change the underlying accounting procedure, gold-standard evidence or evaluation metric.

## Scientific rule

**Evidence before narrative.** Every material conclusion should be traceable to source evidence, deterministic calculations, model/version metadata, failed checks, disagreements, and reviewer decisions. Model output is not treated as audit evidence merely because it is fluent.

## Licensing rule

Third-party projects are linked rather than copied by default. Their current licenses must be checked and frozen for every experiment. Source-available software is not described as open source unless its license qualifies. Copyrighted standards content, including IFRS material, must not be redistributed without appropriate permission.

## Status

**Research scaffold + integrated proposal + provider configuration are complete.** The next implementation milestone is the first executable pilot case with a frozen evidence packet, gold-standard answer, deterministic validators, provider-specific runs and a human-review record.

This project is for research and education. It does not issue audit opinions, assurance conclusions, legal conclusions or authoritative IFRS interpretations.


## Profile-level open-source index

The integrated lab is also indexed from the umbrella repository:

- [Free & Open-Source Accounting, Audit and Assurance Stack](../../OPEN_SOURCE_ACCOUNTING_AUDIT_STACK.md)

This profile-level catalogue links verified open-source accounting/audit tools, source-available research components, public datasets, provider families, and related Saehon repositories.
