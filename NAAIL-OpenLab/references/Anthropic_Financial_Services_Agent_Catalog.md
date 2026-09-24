# Anthropic Financial Services — Agent Reference Catalog

Upstream: https://github.com/anthropics/financial-services  
License: Apache-2.0

This catalog links the public upstream agents relevant to the NAAIL accounting/audit research program. These are **references**, not vendored copies. GPT-native implementations remain separated under `NAAIL-OpenLab/adapters/gpt/`.

## Public agents

- GL Reconciler: https://github.com/anthropics/financial-services/tree/main/plugins/agent-plugins/gl-reconciler
- Month-End Closer: https://github.com/anthropics/financial-services/tree/main/plugins/agent-plugins/month-end-closer
- Statement Auditor: https://github.com/anthropics/financial-services/tree/main/plugins/agent-plugins/statement-auditor
- Valuation Reviewer: https://github.com/anthropics/financial-services/tree/main/plugins/agent-plugins/valuation-reviewer
- Earnings Reviewer: https://github.com/anthropics/financial-services/tree/main/plugins/agent-plugins/earnings-reviewer
- Market Researcher: https://github.com/anthropics/financial-services/tree/main/plugins/agent-plugins/market-researcher
- Model Builder: https://github.com/anthropics/financial-services/tree/main/plugins/agent-plugins/model-builder

## NAAIL mapping

| Upstream reference | GPT/NAAIL target |
|---|---|
| GL Reconciler | GPT GL Reconciliation Agent |
| Month-End Closer | GPT Close Review Agent |
| Statement Auditor | GPT Financial Statement / Audit Review Agent |
| Valuation Reviewer | GPT Valuation Review Agent |
| Earnings Reviewer | GPT SEC Filing & Earnings Review Agent |
| Market Researcher | GPT Evidence/Market Context Agent |
| Model Builder | GPT Financial Modeling Agent |

## PCAOB extension

The NAAIL research layer extends beyond these upstream financial-services examples with independently developed:

- PCAOB Standards Agent
- CAM Inspection Agent
- ICFR Inspection Agent
- Audit Evidence Agent
- Documentation/Compliance Agent
- Reviewer/Falsification Agent
- Human Approval Gate

No affiliation or endorsement by Anthropic or PCAOB is implied.
