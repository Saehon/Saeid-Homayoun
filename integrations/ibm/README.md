# IBM AI / GRC Integration Layer

This folder connects IBM and IBM-origin open-source technologies to the accounting, audit, ICFR, CAM/KAM, IFRS and ESG research stack.

## Default open-source path

| Component | Role in this repository | License / access |
|---|---|---|
| IBM Granite 4.x | LLM reasoning, extraction, classification, tool use and structured outputs | Open model family; use model-specific license |
| Granite Embedding | Retrieval and RAG over filings, audit reports, standards and evidence | Open model family; use model-specific license |
| Docling | PDF, table and XBRL-oriented document conversion / parsing | Open source |
| BeeAI Framework | Multi-agent orchestration for Auditor → Reviewer → Falsification workflows | Open source; IBM-origin project now under LF AI & Data |

## Optional enterprise adapters

These are **not bundled** and require the user's own IBM access, credentials and licensing:

- IBM watsonx.ai — managed model and AI development environment.
- IBM watsonx.governance — model/AI governance, monitoring and accountability.
- IBM OpenPages Internal Audit Management — audit planning, execution and reporting.
- IBM OpenPages Financial Controls Management — financial controls / SOX / ICFR workflows.
- IBM OpenPages Risk Management for ESG — optional ESG risk/governance integration.

## Domain mapping

- `accounting-ai/`: Granite + Docling + Granite Embeddings
- `audit-ai/`: Granite + Docling + BeeAI; optional OpenPages Internal Audit
- `icfr-ai/`: Granite + Docling; optional OpenPages Financial Controls + watsonx.governance
- `cam-ai/` and `kam-ai/`: Docling extraction + Granite classification/reasoning + embeddings
- `ifrs-ai/`: Docling PDF/XBRL ingestion + Granite RAG
- `esg-ai/`: Docling sustainability-report ingestion + Granite RAG; optional OpenPages ESG

## Design rule

Open-source components are the default research path. Proprietary IBM services are adapters only, so the educational and research workflows remain reproducible without paid services.

## Official upstreams

- IBM Granite: https://github.com/ibm-granite
- Granite Hugging Face: https://huggingface.co/ibm-granite
- Docling: https://github.com/docling-project/docling
- BeeAI Framework: https://github.com/i-am-bee/beeai-framework
- watsonx.ai: https://www.ibm.com/products/watsonx-ai
- watsonx.governance: https://www.ibm.com/products/watsonx-governance
- IBM OpenPages: https://www.ibm.com/products/openpages
