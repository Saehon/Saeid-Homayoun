# NAAIL OpenLab™ — Business-School Open Agent Pack

**Public publication date:** 14 September 2026  
**Platform:** NAAIL OpenLab™ — V2026.3 Multi-Agent Digital Twin  
**Status:** Public research and education integration layer  
**Validated executable baseline:** NAAIL OpenLab v0.2.3 / Prototype 003; this pack is a v0.2.4/V2026.3 integration target.

## Purpose

This public pack integrates open-source and research-grade agent technologies relevant to Accounting, Auditing, Finance, Economics, Sustainability, Business Analytics, and business-school education into the governed NAAIL OpenLab architecture.

## Provider-neutral orchestration layer

NAAIL does not depend on one model vendor. Provider frameworks are placed behind an adapter boundary and evaluated on frozen tasks under the same evidence and governance rules.

### OpenAI stack

- **OpenAI Agents SDK (Python / JS)** — open-source multi-agent orchestration with agents, tools, handoffs, guardrails, sessions, tracing, human-in-the-loop patterns, MCP support, and sandbox/realtime capabilities.
- Recommended NAAIL uses: orchestration baseline, handoff experiments, guardrail experiments, trace capture, and cross-provider benchmark runs.
- **Cost boundary:** the SDK/framework can be used as open-source software; OpenAI hosted model/API usage is a separate service and may incur charges.

### Anthropic / Claude stack

- **Claude Agent SDK (Python)** — open-source agent SDK for autonomous workflows, sessions, permissions, subagents, tools, hooks, filesystem/code workflows, and MCP integration.
- **Model Context Protocol (MCP)** — open protocol for connecting agent applications to tools, data and contextual resources. MCP is treated as a provider-neutral interoperability layer rather than a Claude-only feature.
- Recommended NAAIL uses: repository/research agents, evidence-workspace agents, long-document professional review experiments, permissioned tool use, and MCP-based professional data connectors.
- **Cost boundary:** SDK/protocol code can be open-source; Claude/Anthropic hosted model or API usage is a separate service and may incur charges.

### Google / Gemini stack

- **Google Agent Development Kit (ADK)** — Apache-2.0 open-source, code-first toolkit for building, evaluating, orchestrating and deploying agents; optimized for Gemini but designed to be model- and deployment-agnostic.
- **Gemini CLI** — Apache-2.0 open-source terminal agent with file, shell, web/search and MCP capabilities. Google currently documents a personal-account free tier, subject to Google's current quotas and terms.
- **Agent2Agent (A2A) Protocol** — open agent-interoperability standard originally contributed by Google and now hosted by the Linux Foundation. NAAIL uses A2A for agent-to-agent communication across vendor/framework boundaries.
- Recommended NAAIL uses: low-cost/free-tier prototyping, ADK workflow experiments, A2A interoperability tests, repository automation experiments, and provider-neutral benchmark execution.

### Microsoft stack

- **Microsoft Agent Framework** — external orchestration reference for enterprise multi-agent workflows, observability, human approval, checkpointing and professional workflow design.
- It remains an optional adapter/reference layer and is not required for the NAAIL open baseline.

These technologies remain governed by their own licenses, APIs, model terms, quotas, release cycles, trademarks and security requirements. **Open-source framework does not mean hosted model inference is free.** NAAIL must label framework license, model license, API/service cost and data-use terms separately.

## Recommended NAAIL provider-adapter structure

```text
NAAIL-OpenLab/
├── providers/
│   ├── openai_agents/
│   ├── claude_agent_sdk/
│   ├── google_adk/
│   └── local_open_models/
│
├── protocols/
│   ├── mcp/
│   └── a2a/
│
├── benchmarks/
│   └── provider_parity/
│
├── configs/
│   ├── providers.example.yaml
│   └── capability_registry.json
│
└── evaluation/
    ├── evidence_accuracy/
    ├── citation_accuracy/
    ├── tool_selection/
    ├── hallucination/
    ├── reproducibility/
    ├── latency/
    └── cost_efficiency/
```

**Security invariant:** API keys, OAuth tokens and private credentials must never be committed to GitHub. Only `.env.example` or provider configuration templates without secrets may be public.

## NAAIL cross-provider scientific benchmark

The same professional case should be runnable through OpenAI Agents SDK, Claude Agent SDK, Google ADK/Gemini, and an eligible local/open-model baseline where feasible.

Recommended first benchmark set:

- 10 IFRS / financial-reporting cases;
- 10 PCAOB / audit cases;
- 10 CAM/KAM cases;
- 10 ICFR / controls cases;
- 10 ESG / sustainability cases;
- 10 finance / ECONOVA-S™ cases.

Required common measures:

- evidence accuracy;
- citation/source accuracy;
- hallucination rate;
- tool-selection accuracy;
- professional-rule compliance;
- reproducibility;
- human-review acceptance;
- latency;
- token/compute usage where observable;
- monetary cost where applicable;
- cross-provider agreement/disagreement.

KIWI™ cases additionally retain RPA, AA, EG, PS, DS and DIST.

Provider/model identity and version must be recorded with every run. Provider comparison must use frozen tasks and equivalent evidence access; NAAIL must not claim one provider is superior from uncontrolled demonstrations.

## Recommended specialist roles by provider adapter

The roles below are research configurations, not claims that a vendor endorses or supplies a NAAIL product.

| Adapter | NAAIL research role | Primary experiment |
|---|---|---|
| OpenAI Agents SDK | Orchestrator / Handoff / Guardrail Agent | controlled multi-agent workflow and trace evaluation |
| Claude Agent SDK | Evidence Workspace / Repository Review Agent | long-form evidence synthesis, tool permissions and subagent review |
| Google ADK | Workflow / Evaluation / Interoperability Agent | graph workflows, evaluation and A2A experiments |
| Gemini CLI | Free-tier Developer / Repository Agent | low-cost repository analysis and prototype automation |
| MCP | Tool & Evidence Connector Layer | secure standardized access to data/tools |
| A2A | Cross-Agent Communication Layer | OpenAI ↔ Claude ↔ Gemini/local interoperability |

## Business-school domain layer

- **FinRobot** — finance, valuation, financial analysis, accounting analytics, and equity-research workflows.
- **TradingAgents** — multi-agent analyst, debate, trading-simulation, and risk-management research.
- **EconAgent** — economics and macroeconomic-agent research; reference-only until code-license status is clarified.
- **AI Economist** — economic-policy and multi-agent reinforcement-learning academic benchmark.

Institutional affiliations reported in source papers or project materials are evidence of authorship/provenance only. They do not imply institutional certification or endorsement.

## NAAIL specialist integration

```text
OpenAI Agents SDK | Claude Agent SDK | Google ADK / Gemini CLI | Microsoft Agent Framework
                                  ↓
                         NAAIL Adapter Boundary
                                  ↓
                           MCP Tools / Evidence
                                  ↕
                              A2A Agents
                                  ↓
              FinRobot / TradingAgents / domain benchmarks
                                  ↓
 KIWI™ | POMELO™ | IFRS | PCAOB | ICFR | ESG | Forensic | ECONOVA-S™
                                  ↓
 Evidence Passport™ → Professional Decision DAG™
                                  ↓
 RPA + AA + EG + PS + DS + DIST + AIV + CER + HOR + ESC
                                  ↓
                   Adversarial Review / Falsification
                                  ↓
                              Human Gate™
```

## Professional-practice benchmark layer

Public material from Deloitte, EY, KPMG, and PwC is used only to derive practice-oriented governance and evaluation requirements such as human-led workflows, handoff control, reliability testing, hallucination testing, identity/permission controls, audit trails, and escalation. This does **not** imply that any Big Four firm endorses NAAIL or the third-party projects in this pack.

## Canonical public resources

- [Business-School Agent Evidence Pack](./BUSINESS_SCHOOL_AGENT_EVIDENCE.md)
- [Machine-readable Business-School Registry](./integrations/open_source_agents/business_school_registry.json)
- [Open-Source Agent Integration Index](./integrations/open_source_agents/README.md)
- [General Open-Source Agent Education Stack](./OPEN_SOURCE_AGENT_STACK.md)
- [NAAIL Open-Source Student Agent Lab](./docs/education/OPEN_SOURCE_AGENT_LAB.md)
- [NAAIL Agent Governance Standard](./AGENTS.md)
- [NAAIL V2026.3 Architecture](./versions/V2026.3_MULTI_AGENT_DIGITAL_TWIN.md)

## Scientific integrity and rights

Registry inclusion does not mean installation, execution, benchmarking, security review, validation, certification, or commercial approval. Comparative claims require frozen tasks, equivalent evidence access, declared model/provider versions, retained failures/null results, prespecified metrics, robustness analysis, reproducibility, adversarial review, falsification, and Human Gate approval.

Third-party code, model weights, APIs, datasets, papers, standards, and trademarks remain subject to their original rights and licenses. NAAIL does not copy or relicense external projects merely because they are referenced or evaluated.

## Citation

Homayoun, S. (2026). *NAAIL OpenLab™ — Business-School Open Agent Pack*. NAAIL OpenLab, GitHub. ORCID: 0000-0002-2536-0446.
