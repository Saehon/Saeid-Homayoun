# Free & Open-Source Accounting, Audit and Assurance Stack

**Profile-level index for the Saehon research ecosystem — updated 24 September 2026**

This page connects the **Open Agentic Accounting & Audit Lab** with free/open-source or research-accessible tools that can be tested across GPT/Codex, Claude, Gemini, Microsoft/Azure, Kimi, DeepSeek and local models.

> **Licensing rule:** "free", "open source", and "source available" are not the same. The categories below use current GitHub license metadata where available. Always freeze the exact upstream version and re-check the license before redistribution or commercial use.

## Main integrated project

- **Open Agentic Accounting & Audit Lab**  
  https://github.com/Saehon/Saeid-Homayoun/tree/main/Open-Agentic-Accounting-Audit-Lab

The project integrates financial accounting, audit testing, ICFR/internal control, corporate governance, CAM/KAM, IFRS, ESG, evidence verification, deterministic controls, cross-model challenge and human approval.

## Verified open-source components

| Project | Current GitHub license metadata | Primary role | Upstream |
|---|---|---|---|
| CPA Skills for AI Agents | MIT | Bank reconciliation, statement extraction, tie-outs, audit sampling, JE anomaly tests | https://github.com/adoptai/cpa-skills |
| FinanceSkills | MIT | Finance, accounting, IFRS/GAAP, audit and compliance skills | https://github.com/GAJETOso/financeskills |
| closegate | Apache-2.0 | SOX/SoD, materiality routing, finance-agent policy gate, HITL approvals | https://github.com/esploro-group/closegate |
| Docling MCP | MIT | Document parsing and evidence ingestion through MCP | https://github.com/docling-project/docling-mcp |
| SEC EDGAR MCP | AGPL-3.0 | SEC filing/XBRL evidence and public-company research | https://github.com/stefanoamorelli/sec-edgar-mcp |
| Google ADK (Python) | Apache-2.0 | Open-source multi-agent orchestration | https://github.com/google/adk-python |
| Microsoft Agent Framework | MIT | Python/.NET agent and multi-agent orchestration | https://github.com/microsoft/agent-framework |

## Free/research-accessible components requiring license review

| Project | Status | Role | Upstream |
|---|---|---|---|
| AI4SustainableX | Source-available / license requires direct review | ESG and sustainability reporting workflows | https://github.com/lokeshbohra/ai4sustainablex |
| LiteLLM | Public source; GitHub license metadata currently reports NOASSERTION | Provider-neutral model gateway | https://github.com/BerriAI/litellm |

Do not label these as OSI open source solely because the repositories are public. Review the current LICENSE/terms before bundling or redistribution.

## Provider families to benchmark

The same accounting/audit case should be run with a frozen toolchain while changing only the model/provider layer:

- OpenAI GPT / Codex
- Anthropic Claude
- Google Gemini
- Microsoft/Azure-hosted model services
- Kimi / Moonshot
- DeepSeek
- optional local models through Ollama or comparable runtimes

## Public data and benchmark sources

### Official / primary
- SEC EDGAR APIs: https://www.sec.gov/search-filings/edgar-application-programming-interfaces
- PCAOB AS 3101: https://pcaobus.org/oversight/standards/auditing-standards/details/AS3101
- ESMA ESEF: https://www.esma.europa.eu/issuer-disclosure/electronic-reporting
- ESMA ESEF Taxonomy: https://www.esma.europa.eu/electronic-reporting/esef-taxonomy
- IFRS Standards portal: https://www.ifrs.org/issued-standards/
- IFRS Sustainability Standards Navigator: https://www.ifrs.org/issued-standards/ifrs-sustainability-standards-navigator/

### Hugging Face
- SFD-v1 SEC Filings: https://huggingface.co/datasets/sfd-anonymous/sfd-v1
- SEC filings catalogue: https://huggingface.co/datasets?other=sec-filings
- FinancialPhraseBank: https://huggingface.co/datasets/lmassaron/FinancialPhraseBank
- FiQA: https://huggingface.co/datasets/llamafactory/fiqa
- Sustainability datasets: https://huggingface.co/datasets?other=sustainability

### Kaggle
- Credit Card Fraud Detection: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
- ESG Analytics: https://www.kaggle.com/datasets/crmerfu/esg-analytics
- ESG and Financial Performance: https://www.kaggle.com/datasets/shriyashjagtap/esg-and-financial-performance-dataset

Kaggle and mirrored datasets should be treated as secondary benchmark sources unless their provenance to an authoritative original source is independently established.

## Related public Saehon repositories

These repositories already exist under the Saehon account and are relevant research assets. They remain separate projects; this index only links them.

| Repository | Potential connection to the integrated lab |
|---|---|
| https://github.com/Saehon/AAA | Audit/accounting research and teaching assets |
| https://github.com/Saehon/AuditData-API | Audit-data/API research layer |
| https://github.com/Saehon/IFRS-AI-Inspector | IFRS-focused AI inspection experiments |
| https://github.com/Saehon/sec-edgar-downloader | SEC/EDGAR data acquisition |
| https://github.com/Saehon/openesef | ESEF/XBRL European reporting work |
| https://github.com/Saehon/openai-agents-python | Agent-framework experimentation |
| https://github.com/Saehon/timesfm | Time-series/forecasting experimentation |
| https://github.com/Saehon/fg-data-synthetic | Synthetic-data research assets |

## Scientific boundary

The integrated stack is for **education, academic research, simulation and benchmarking**. A public repository, a passing test, or a successful agent run does not establish audit assurance, regulatory approval, accounting correctness, IFRS authority, commercial readiness or superiority over professional systems.

**Evidence before narrative. Human accountability remains required for material professional conclusions.**


## Taming the Modern Prometheus release

The catalogue and benchmark are now connected to the cybernetic-control article package:

- [Free/Open Agent and Tool Catalogue 2026](OPEN_AGENT_CATALOG_2026.md)
- [Taming the Modern Prometheus paper package](papers/taming-modern-prometheus/README.md)
- [Agentic Financial Assurance Benchmark](open-data/taming-modern-prometheus/README.md)
- [Kaggle dataset package](kaggle/datasets/taming-modern-prometheus/)
- [Hugging Face dataset package](huggingface/datasets/taming-modern-prometheus/)

The benchmark contains three public-derived Microsoft aggregate checks and ten explicitly synthetic gate cases. It is a research and education scaffold, not audit evidence or a professional assurance conclusion.

## Microsoft, Copilot & IBM companion registry

A dedicated machine-readable registry and safe clone scripts are maintained here:

- [Microsoft, Copilot & IBM Accounting/Finance/Audit Stack](open-source/accounting-finance-audit/README.md)
- [Machine-readable repository registry](open-source/accounting-finance-audit/repos.yml)
- [Linux/macOS/Codespaces clone script](open-source/accounting-finance-audit/bootstrap.sh)
- [Windows PowerShell clone script](open-source/accounting-finance-audit/bootstrap.ps1)
- [Security and licence rules](open-source/accounting-finance-audit/SECURITY_AND_LICENSE.md)

The companion registry covers Microsoft FinanceBenchmark, Copilot Studio samples, Microsoft Finance analytics/forecasting/Qlib, IBM AML and fraud datasets/tools, watsonx examples, financial-agent assurance benchmarks, Arelle XBRL, SEC EDGAR download tooling, audit analytics, FinBERT and FinGPT. Third-party source is referenced or cloned from upstream rather than silently copied into this repository.
