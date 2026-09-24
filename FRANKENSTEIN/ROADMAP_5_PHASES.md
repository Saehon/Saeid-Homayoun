# FRANKENSTEIN™ — Five-Phase Data & Agent Roadmap

FRANKENSTEIN develops from a simple reproducible public-data connector into a sophisticated provider-neutral accounting, audit and assurance research system.

## Phase 1 — Public Data Connection
**Goal:** prove one clean, free, reproducible connection.

- GitHub = code, architecture, manifests, small reproducible samples.
- Hugging Face = public dataset/model source.
- Kaggle = benchmark publication source; Phase-1 package is now published privately through GitHub Actions.
- Google Drive = controlled research-document layer; Phase-2 registry is now active.
- No paid API is required.
- No secret is required for the first Hugging Face example.

**Implemented example:** Hugging Face FinancialPhraseBank → small sample + provenance manifest → GitHub.

## Phase 2 — Registered Data Fabric — ACTIVE
**Goal:** connect multiple data sources without turning GitHub into a data warehouse.

**Current live path:** Hugging Face → GitHub → Kaggle → Google Drive.

- Hugging Face dataset/model registry.
- Kaggle API connector using a GitHub secret.
- Google Drive controlled-source registry.
- SEC/EDGAR, PCAOB, ESMA/ESEF and other authoritative public sources.
- Checksums, source URL, license, retrieval timestamp and dataset version for every asset.

## Phase 3 — Specialist Free/Open Agent Layer
**Goal:** attach reusable domain agents and deterministic tools.

- Financial Accounting Agent.
- Audit Testing Agent.
- Evidence Agent.
- ICFR/Internal Control Agent.
- Corporate Governance Agent.
- CAM Agent.
- KAM Agent.
- IFRS Agent.
- ESG Agent.
- Reviewer Agent.

External open/research-accessible components may include CPA Skills, FinanceSkills, Docling MCP, closegate, SEC EDGAR MCP, Google ADK, Microsoft Agent Framework and provider-neutral routing.

## Phase 4 — Cross-Model Scientific Benchmarking
**Goal:** run the same accounting/audit task across multiple model families while holding the evidence and tools constant.

Provider families:
- GPT/Codex.
- Claude.
- Gemini.
- Microsoft/Azure-hosted models.
- Kimi.
- DeepSeek.
- local models.

Research outputs:
- accuracy/F1;
- numerical error;
- unsupported-claim rate;
- evidence precision/recall;
- control violations;
- cost/time;
- disagreement;
- human override.

## Phase 5 — Evidence-Governed Research Platform
**Goal:** sophisticated professional-grade research architecture.

```text
Data Sources
   ↓
Provenance Registry
   ↓
Deterministic Accounting/Audit Tools
   ↓
Specialist Agent Society
   ↓
Cross-Model Challenge
   ↓
Evidence Passport
   ↓
Control / Policy Gate
   ↓
Human Approval Gate
   ↓
Reproducible Research Output
```

Phase 5 may add:
- knowledge graphs / GraphRAG;
- digital evidence lineage;
- scenario and synthetic-data generation;
- adversarial/falsification agents;
- independent replication agents;
- experiment registry;
- cost and compute telemetry;
- formal reproducibility packages.

## Design rule

**Do not move large raw datasets into GitHub by default.**  
GitHub should hold the reproducible code, metadata, source registry, tests and small demonstration samples. Large/public datasets stay with Hugging Face or Kaggle; controlled working files can stay in Google Drive.