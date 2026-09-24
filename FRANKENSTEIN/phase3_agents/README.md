# FRANKENSTEIN Phase 3 — Specialist Free/Open Agent Layer

**Status: ACTIVE**

Phase 3 connects the registered data fabric to bounded accounting, audit and assurance agents.

## Agent society

| Agent | Main approved external/open tools | Human gate |
|---|---|---|
| Financial Accounting | FinanceSkills, CPA Skills, deterministic Python | material judgment |
| Audit Testing | CPA Skills, Docling MCP, deterministic Python | material exception |
| Evidence | Docling MCP, SEC EDGAR MCP | evidence/provenance checks |
| ICFR/Internal Control | closegate, CPA Skills | deficiency severity |
| Corporate Governance | SEC EDGAR MCP, Docling MCP | material judgment |
| CAM | SEC EDGAR MCP, Docling MCP | final classification |
| KAM | Docling MCP | final classification |
| IFRS | FinanceSkills + permitted authoritative sources | mandatory human gate |
| ESG | Docling MCP + AI4SustainableX (license review) | material claim |
| Reviewer | deterministic checks + evidence sources | escalation |

## Why adapters instead of copying code?

Third-party projects remain in their upstream repositories. FRANKENSTEIN stores:
- source URL;
- license/status;
- permitted role;
- approved agent mapping;
- evidence requirements;
- human-gate rule.

This avoids silently relicensing external projects and makes experiments easier to reproduce by freezing exact upstream commits later.

## Files

- `tool_registry.json` — external/open/source-available component registry.
- `agents.json` — bounded specialist-agent definitions.
- `router.py` — executable dry-run routing/control scaffold.
- `INTEGRATIONS.md` — upstream integration guide.
- `../tests/test_phase3_agents.py` — validation test.

## Run the first dry-run example

```bash
python FRANKENSTEIN/phase3_agents/router.py \
  --agent financial_accounting \
  --task "Reconcile a financial-reporting evidence packet" \
  --evidence DEMO-EVIDENCE-001
```

The output lists only the tools that the Financial Accounting Agent is permitted to use and records the Human Gate.

## Important boundary

Phase 3 proves architecture and routing. It does **not** claim that every upstream tool has been installed in the GitHub runner or that an AI has completed an audit. Exact upstream releases/commits should be frozen when a real empirical case is executed.
