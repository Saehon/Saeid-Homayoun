# Claude Finance Stack Adapter for Lemon-ICFR-US

## Objective
Use Anthropic/Claude financial capabilities where useful while keeping Lemon's ICFR assurance logic provider-neutral.

## Component mapping

### Claude for Financial Services
Use as a financial-services interaction/workflow surface for authorized users and connected enterprise data.

### Financial Analysis Solution
Use as a specialist financial-analysis capability for:
- trend and variance analysis,
- ratio analysis,
- anomaly hypothesis generation,
- filing comparison,
- financial context supporting ICFR risk assessment.

Its output is analytical evidence or a hypothesis, not an ICFR conclusion by itself.

### Claude for Excel
Use as an optional spreadsheet interface for:
- control matrices,
- sample populations,
- reconciliations,
- exception logs,
- evidence registers,
- reviewer workbooks.

Sensitive or consequential workbook changes should remain reviewable and versioned.

### Claude Code
Use as Lemon's development plane for:
- repository work,
- tests,
- benchmark execution,
- prompt/agent configuration,
- CI validation,
- adapter development,
- reproducible engineering changes.

### Financial Services Agents
Use patterns from finance-focused agents to construct specialized Lemon subagents, but constrain them with Lemon evidence contracts, COSO/ICFR context, falsification, and human approval.

## MCP / connector layer
Connectors may expose:
- SEC/EDGAR/XBRL
- approved document stores
- ERP extracts
- GRC/control repositories
- ticketing/workflow systems
- spreadsheets
- audit/research datasets

Connector permissions must follow least privilege. Secrets must not be committed to the repository.

## Provider-neutral adapter contract
Every model provider adapter should implement:
- `retrieve_evidence()`
- `analyze_case()`
- `generate_hypotheses()`
- `challenge_claim()`
- `produce_structured_output()`
- `return_model_lineage()`

This allows Claude to be replaced or cross-checked by GPT, Gemini, local/open models, or deterministic code.

## Model cross-check mode
For high-impact research experiments, Lemon may run a second provider/model as an independent challenger. Agreement does not establish truth; disagreement is escalated to evidence review.

## Safety
No API/model call may bypass:
Evidence Passport → Reviewer → Falsification → Human Approval
for material ICFR conclusions.
