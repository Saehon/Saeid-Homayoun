# Open Agentic Accounting & Audit Lab

A provider-neutral research and teaching project for testing AI agents in **financial accounting, auditing, ICFR/internal control, corporate governance, CAM/KAM, IFRS, and ESG/sustainability reporting**.

## Research objective

The project separates the **reasoning model** from the **accounting/audit procedure**, evidence layer, deterministic controls, and human approval. The same case can therefore be tested with Claude, GPT/Codex, Gemini, Microsoft/Azure-hosted models, Kimi, DeepSeek, or local models while keeping the domain workflow fixed.

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
       GPT | Claude | Gemini | Kimi | DeepSeek
                    |
                    v
               Human approval gate
                    |
                    v
        Evidence-backed research output
```

## Project folders

- `PROPOSAL.md` — integrated research and implementation proposal.
- `docs/AGENT_CATALOG.md` — open/free or research-accessible agent/tool catalogue.
- `docs/DATA_SOURCES.md` — GitHub, Kaggle, Hugging Face, SEC, PCAOB, ESMA, IFRS/ISSB sources.
- `docs/EXPERIMENT_DESIGN_T0_T6.md` — experimental protocol and 30-case design.
- `config/agents.yaml` — proposed specialist-agent responsibilities.
- `config/providers.example.yaml` — provider-neutral model routing template.
- `src/provider_router.py` — minimal model-family routing scaffold.
- `THIRD_PARTY_LICENSES.md` — licensing and reuse notes.

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

## Scientific rule

**Evidence before narrative.** Every material conclusion should be traceable to source evidence, deterministic calculations, model/version metadata, and reviewer decisions. Model output is not treated as audit evidence merely because it is fluent.

## Status

Research scaffold. No audit opinion, assurance conclusion, legal conclusion, or IFRS interpretation should be issued without qualified human review and appropriate authoritative sources.
