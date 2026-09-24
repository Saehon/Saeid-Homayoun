# Free/Open Agent and Tool Catalogue for Accounting, Audit and ESG

**Checked:** 24 September 2026  
**Purpose:** provider-neutral building blocks for academic research, education, simulation, and reproducible assurance experiments.

## Important distinction

- **Free to download** does not mean free hosted inference, free production use, or unrestricted redistribution.
- **Open-source** means the upstream license should be checked against the applicable open-source definition.
- **Source-available** or **research/non-commercial** projects must not be labelled open source merely because their repositories are public.
- Standards, proprietary ESG ratings, commercial audit datasets, and confidential company data remain outside this catalogue unless their terms permit the planned use.

## Domain-specific accounting, audit and sustainability tools

| Resource | Primary use | License/status | Link |
|---|---|---|---|
| CPA Skills | Bank reconciliations, statement extraction, tie-outs, audit sampling, journal-entry anomaly scans | MIT metadata; verify upstream version | https://github.com/adoptai/cpa-skills |
| FinanceSkills | Finance, accounting, IFRS/GAAP, audit and compliance skills | MIT metadata; verify upstream version | https://github.com/GAJETOso/financeskills |
| closegate | SOX/SoD, materiality routing, finance-agent policy chokepoint, HITL approvals | Apache-2.0 metadata | https://github.com/esploro-group/closegate |
| Docling | Document parsing, table extraction, evidence ingestion | MIT metadata; verify upstream version | https://github.com/docling-project/docling |
| Docling MCP | MCP evidence-ingestion adapter | MIT metadata; verify upstream version | https://github.com/docling-project/docling-mcp |
| SEC EDGAR MCP | SEC filings, XBRL and public-company evidence retrieval | AGPL-3.0 metadata; review deployment obligations | https://github.com/stefanoamorelli/sec-edgar-mcp |
| AI4SustainableX | Local-first ESG and sustainability reporting workflows | Public repository; license metadata requires direct review | https://github.com/lokeshbohra/ai4sustainablex |

## General open-source agent frameworks

| Framework | Best fit in this project | License metadata | Link |
|---|---|---|---|
| OpenAI Agents SDK for Python | Specialist agents, tools, guardrails, handoffs and tracing | MIT | https://github.com/openai/openai-agents-python |
| Microsoft Agent Framework | Python/.NET multi-agent orchestration and enterprise adapters | MIT | https://github.com/microsoft/agent-framework |
| Google ADK for Python | Code-first agent construction and evaluation | Apache-2.0 | https://github.com/google/adk-python |
| LangGraph | Stateful, durable, controllable agent graphs | MIT | https://github.com/langchain-ai/langgraph |
| CrewAI | Role-based multi-agent experiments | MIT | https://github.com/crewAIInc/crewAI |
| smolagents | Small code-agent experiments on Hugging Face | Apache-2.0 | https://github.com/huggingface/smolagents |
| DSPy | Programmatic prompt/module optimization and evaluation | MIT | https://github.com/stanfordnlp/dspy |
| Haystack | Retrieval, routing, RAG and agent pipelines | Apache-2.0 | https://github.com/deepset-ai/haystack |

## Evidence, policy and research infrastructure

| Tool | Role | License metadata | Link |
|---|---|---|---|
| Microsoft GraphRAG | Graph-based retrieval and corpus structuring | MIT | https://github.com/microsoft/graphrag |
| Open Policy Agent | Explicit policy and non-compensatory gate evaluation | Apache-2.0 | https://github.com/open-policy-agent/opa |
| DuckDB | Local analytical SQL over CSV/Parquet and reproducible checks | MIT | https://github.com/duckdb/duckdb |
| MLflow | Experiment tracking, evaluation and model lineage | Apache-2.0 | https://github.com/mlflow/mlflow |
| NetworkX | Evidence/control graph analysis | BSD-3-Clause | https://github.com/networkx/networkx |
| pandas | Tabular accounting and ESG transformations | BSD-3-Clause | https://github.com/pandas-dev/pandas |
| scikit-learn | Baselines, calibration, classification and evaluation | BSD-3-Clause | https://github.com/scikit-learn/scikit-learn |
| SHAP | Model explanation and sensitivity analysis | MIT | https://github.com/shap/shap |
| DVC | Dataset/version and pipeline reproducibility | Apache-2.0 | https://github.com/iterative/dvc |
| OpenTelemetry | Trace and telemetry interoperability | Apache-2.0 | https://github.com/open-telemetry/opentelemetry-specification |

## Suggested specialist mapping

| Specialist role | Minimum free/open stack |
|---|---|
| Financial accounting | CPA Skills or FinanceSkills + pandas/DuckDB + deterministic tie-outs |
| Audit testing | CPA Skills + SEC EDGAR/MCP + Python validators + reviewer |
| ICFR/internal control | closegate + Open Policy Agent + immutable run log |
| Corporate governance | SEC EDGAR/MCP + Docling + source-location checks |
| CAM/KAM | SEC EDGAR/MCP + Docling + temporal comparison + human classification gate |
| IFRS research | FinanceSkills + public authoritative navigation + calculation validator + human approval |
| ESG/sustainability | AI4SustainableX only after license review + Docling + boundary/metric reconciliation + evidence gate |
| Multi-agent orchestration | OpenAI Agents SDK, Microsoft Agent Framework, Google ADK, LangGraph, CrewAI, or smolagents |
| GraphRAG and evidence lineage | Microsoft GraphRAG + DuckDB/NetworkX + provenance manifest |
| Independent challenge | second framework/provider + Open Policy Agent + deterministic falsification tests |

## Models and hosted services

Hugging Face, Ollama, and local open-weight model runtimes can reduce API dependence, but each model has its own weights license, acceptable-use policy, size, hardware requirement, and evaluation profile. A model is not an assurance agent by itself. The agent must be wrapped with evidence retrieval, deterministic checks, provenance, red-team challenge, and a human gate.

## Required governance for every agent

Every experiment should record:

1. upstream repository/model and immutable version;
2. license and permitted use;
3. source documents and retrieval date;
4. prompts, tools, policies, and model settings;
5. evidence locations and calculations;
6. failed checks and agent disagreement;
7. reviewer decision and human approval;
8. whether the result is public-derived, synthetic, or proprietary.

See [Taming the Modern Prometheus](papers/taming-modern-prometheus/README.md) for the linked benchmark and falsification-gate design.
