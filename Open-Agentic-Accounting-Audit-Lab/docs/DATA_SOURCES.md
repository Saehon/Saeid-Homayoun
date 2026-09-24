# Data and Benchmark Sources

## Official / primary sources

| Source | Research use | Link |
|---|---|---|
| SEC EDGAR APIs | U.S. 10-K/10-Q/8-K, CompanyFacts, XBRL | https://www.sec.gov/search-filings/edgar-application-programming-interfaces |
| PCAOB AS 3101 | CAM criteria and reporting requirements | https://pcaobus.org/oversight/standards/auditing-standards/details/AS3101 |
| ESMA ESEF | European machine-readable annual reports | https://www.esma.europa.eu/issuer-disclosure/electronic-reporting |
| ESMA ESEF Taxonomy | IFRS/ESEF taxonomy validation | https://www.esma.europa.eu/electronic-reporting/esef-taxonomy |
| IFRS Accounting Standards portal | Authoritative navigation; licensing restrictions apply | https://www.ifrs.org/issued-standards/ |
| IFRS Sustainability Standards Navigator | IFRS S1/S2 sustainability framework navigation | https://www.ifrs.org/issued-standards/ifrs-sustainability-standards-navigator/ |

## GitHub / open research tooling

- CPA Skills: https://github.com/adoptai/cpa-skills
- FinanceSkills: https://github.com/GAJETOso/financeskills
- closegate: https://github.com/esploro-group/closegate
- Docling MCP: https://github.com/docling-project/docling-mcp
- SEC EDGAR MCP: https://github.com/stefanoamorelli/sec-edgar-mcp
- AI4SustainableX: https://github.com/lokeshbohra/ai4sustainablex
- LiteLLM: https://github.com/BerriAI/litellm
- Google ADK: https://github.com/google/adk-docs
- Microsoft Agent Framework: https://github.com/microsoft/agent-framework

## Hugging Face

| Dataset/resource | Use | Link |
|---|---|---|
| SFD-v1 SEC Filings Dataset | Large-scale SEC filing benchmark | https://huggingface.co/datasets/sfd-anonymous/sfd-v1 |
| SEC-filings dataset catalogue | Additional SEC/filing datasets | https://huggingface.co/datasets?other=sec-filings |
| FinancialPhraseBank | Finance sentiment/text classification benchmark | https://huggingface.co/datasets/lmassaron/FinancialPhraseBank |
| FiQA | Finance QA/RAG benchmark | https://huggingface.co/datasets/llamafactory/fiqa |
| Sustainability dataset catalogue | ESG/sustainability text/data discovery | https://huggingface.co/datasets?other=sustainability |

## Kaggle

Kaggle data is best treated as a **secondary benchmark source**, not an authoritative accounting source.

- Credit Card Fraud Detection: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
- ESG Analytics: https://www.kaggle.com/datasets/crmerfu/esg-analytics
- ESG and Financial Performance Dataset: https://www.kaggle.com/datasets/shriyashjagtap/esg-and-financial-performance-dataset
- Fraud dataset search: https://www.kaggle.com/search?q=fraud+in%3Adatasets

## Provenance rule

For every dataset/case, record:
- original source;
- retrieval date;
- company/jurisdiction/year;
- license/terms;
- whether authoritative, mirrored, synthetic or derived;
- preprocessing steps;
- checksum/version where feasible;
- evidence locations used by each agent.

Mirrors and Kaggle copies must not be treated as more authoritative than the originating regulatory or company source.
