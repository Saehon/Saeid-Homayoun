# Phase 3 External Integrations

FRANKENSTEIN treats third-party projects as external adapters by default.

| ID | Project | License/status | Upstream | FRANKENSTEIN role |
|---|---|---|---|---|
| cpa_skills | CPA Skills for AI Agents | MIT | https://github.com/adoptai/cpa-skills | deterministic/accounting-audit skills |
| finance_skills | FinanceSkills | MIT | https://github.com/GAJETOso/financeskills | accounting/IFRS/finance skills |
| closegate | closegate | Apache-2.0 | https://github.com/esploro-group/closegate | ICFR/control/policy gate |
| docling_mcp | Docling MCP | MIT | https://github.com/docling-project/docling-mcp | document/evidence parsing |
| sec_edgar_mcp | SEC EDGAR MCP | AGPL-3.0 | https://github.com/stefanoamorelli/sec-edgar-mcp | SEC/XBRL/CAM/governance evidence |
| google_adk | Google ADK | Apache-2.0 | https://github.com/google/adk-python | optional Gemini orchestration |
| microsoft_agent_framework | Microsoft Agent Framework | MIT | https://github.com/microsoft/agent-framework | optional Azure/Microsoft orchestration |
| ai4sustainablex | AI4SustainableX | source-available; verify terms | https://github.com/lokeshbohra/ai4sustainablex | optional ESG research adapter |
| litellm | LiteLLM | verify current upstream license | https://github.com/BerriAI/litellm | Phase-4 provider routing |

## Reproducible-install principle

When a real case starts, record the exact upstream commit/release in an experiment lock file. Do not use an unpinned `main` branch as the scientific version identifier.

Example research workflow:

```text
FRANKENSTEIN case
    ↓
agent registry
    ↓
approved external adapter
    ↓
frozen upstream version
    ↓
evidence + deterministic checks
    ↓
reviewer
    ↓
human gate
```

## Licensing boundary

Do not bundle upstream source into FRANKENSTEIN merely for convenience. Review copyleft/source-available obligations before distribution. Copyrighted standards text, including restricted IFRS material, stays outside the public repository unless redistribution is permitted.
