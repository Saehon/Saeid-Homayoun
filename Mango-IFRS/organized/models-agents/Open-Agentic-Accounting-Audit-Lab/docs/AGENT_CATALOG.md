# Agent and Tool Catalogue

| Resource | Financial accounting | Audit / ICFR | Governance | ESG | Provider compatibility | Link |
|---|---|---|---|---|---|---|
| CPA Skills | Strong | Strong | Limited/extendable | Limited | Claude Code, Codex and Agent Skills-compatible clients | https://github.com/adoptai/cpa-skills |
| FinanceSkills | Strong | Strong | Extendable | Extendable | Claude Code, Codex, Cursor, Windsurf, Agent Skills-compatible clients | https://github.com/GAJETOso/financeskills |
| closegate | Close/reconciliation support | Strong SOX/SoD/HITL | Strong control-governance layer | Extendable | MCP/Python; designed for finance agents using Claude/GPT/Gemini-style models | https://github.com/esploro-group/closegate |
| Docling MCP | Evidence extraction | Strong evidence ingestion | Board/proxy document extraction | Sustainability-report extraction | MCP clients; model-neutral | https://github.com/docling-project/docling-mcp |
| SEC EDGAR MCP | Strong SEC/XBRL | CAM/audit-report evidence | Strong public governance filings | Public ESG/risk disclosures | MCP; model-neutral | https://github.com/stefanoamorelli/sec-edgar-mcp |
| AI4SustainableX | Limited | Evidence verification | ESG governance evidence | Strong | Local/Ollama plus cloud providers; source-available BUSL-1.1 | https://github.com/lokeshbohra/ai4sustainablex |
| Google ADK | Framework | Framework | Framework | Framework | Optimized for Gemini; modular/model-agnostic architecture | https://github.com/google/adk-docs |
| Microsoft Agent Framework | Framework | Framework | Framework | Framework | Microsoft/Azure ecosystem plus provider adapters | https://github.com/microsoft/agent-framework |
| LiteLLM | Provider layer | Provider layer | Provider layer | Provider layer | OpenAI, Azure, Anthropic, Gemini/Vertex, DeepSeek, Moonshot/Kimi and others | https://github.com/BerriAI/litellm |

## Proposed specialist agents

| Agent | Core responsibility | Deterministic verification |
|---|---|---|
| Financial Accounting | journals, reconciliations, close, statements, estimates | tie-outs, equations, roll-forwards |
| Audit Testing | vouching, tracing, sampling, cutoff, JE tests | deterministic tests/scripts |
| Evidence | retrieval, parsing, citation and source matching | source-location checks |
| ICFR/Internal Control | control mapping, SoD, deficiency support | policy rules, thresholds |
| Corporate Governance | board/audit committee, ownership, compensation, risk oversight | source-presence/consistency checks |
| CAM | extract/classify CAMs; persistence/entry/exit | filing-location verification |
| KAM | extract/classify KAMs; procedure/topic mapping | report-location verification |
| IFRS | recognition, measurement, presentation, disclosure reasoning | calculation tools + authoritative-source gate |
| ESG | metric/claim extraction and framework mapping | evidence-to-claim + emissions calculations |
| Reviewer | independent challenge and sufficiency review | rerun, contradiction and evidence checks |
