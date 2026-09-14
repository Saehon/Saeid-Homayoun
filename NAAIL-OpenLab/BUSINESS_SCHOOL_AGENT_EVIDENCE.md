# NAAIL OpenLab™ — Business-School Open Agent Evidence Pack

**Target:** NAAIL OpenLab v2026.3 / v0.2.4 integration layer  
**Date:** 2026-09-14  
**Scope:** non-commercial research, teaching, simulation, and reproducible scientific evaluation

## Evidence rule

This document separates four different claims that must not be conflated:

1. **Creator-maintained open-source framework** — the repository is maintained by the named technology organization.
2. **arXiv/domain evaluation** — a paper reports an empirical or simulation evaluation relevant to economics, finance, accounting, audit, or business education.
3. **Academic affiliation** — an author/evaluator is affiliated with an institution such as MIT or Harvard; this does **not** mean institutional endorsement.
4. **Professional-practice relevance** — Big Four public material supports the use case, governance requirement, or control pattern; this does **not** mean the firm endorses the third-party open-source project.

**No evidence was identified that one free/open-source agent has been jointly approved, certified, or endorsed by MIT, Harvard, Deloitte, EY, KPMG, PwC, Microsoft, Google, and OpenAI. NAAIL must never make that claim.**

## Recommended business-school stack

| Layer | Project | Business-school use | Evidence/provenance | License/integration state |
|---|---|---|---|---|
| Orchestration | Google Agent Development Kit (ADK) | multi-agent teaching, workflow design, evaluation | official Google open-source project | Apache-2.0; adapter target |
| Orchestration | Microsoft Agent Framework | enterprise-style workflows, handoffs, comparative orchestration | official Microsoft open-source project | MIT; adapter target |
| Orchestration | OpenAI Agents SDK | tools, guardrails, handoffs, multi-agent workflows | official OpenAI open-source project | MIT; adapter target |
| Finance/Accounting | FinRobot | equity research, financial analysis, valuation/report workflows | arXiv:2405.14767 + open-source code | Apache-2.0; domain adapter candidate |
| Finance | TradingAgents | analyst/debate/risk-manager/trader simulation | arXiv:2412.20138; project reports UCLA/MIT affiliations | Apache-2.0; simulation adapter candidate |
| Economics | EconAgent | macroeconomic household/firm simulation, policy experiments | arXiv:2310.10436 + released code | **license not verified in repository root; reference-only until clarified** |
| Economics/Policy | AI Economist | multi-agent economic-policy and mechanism-design benchmark | arXiv:2108.02755 / Science Advances; coauthor David C. Parkes, Harvard | BSD-3-Clause upstream; archived benchmark/reference |

## Why these fit NAAIL

### 1. FinRobot — financial-analysis domain agent

FinRobot is explicitly presented as an open-source financial AI-agent platform and is suitable for controlled finance/accounting assignments such as financial-statement analysis, equity-research workflows, valuation exercises, evidence retrieval, and report critique.

- Paper: https://arxiv.org/abs/2405.14767
- Repository: https://github.com/AI4Finance-Foundation/FinRobot
- NAAIL status: `DOMAIN_ADAPTER_CANDIDATE`
- Required NAAIL control: research/education only; no investment recommendation or live-trading authority.

### 2. TradingAgents — MIT-linked financial multi-agent simulation

TradingAgents models specialist analyst roles, bull/bear debate, risk management, and a trader/fund-management decision chain. The project page identifies an MIT affiliation for one author. This is evidence of **MIT-affiliated authorship**, not MIT certification or endorsement.

- Paper: https://arxiv.org/abs/2412.20138
- Project: https://tradingagents-ai.github.io/
- Repository: https://github.com/TauricResearch/TradingAgents
- NAAIL status: `DOMAIN_ADAPTER_CANDIDATE`
- Recommended teaching use: digital-twin finance lab, analyst-role separation, adversarial debate, risk escalation, and evidence-chain evaluation.

### 3. EconAgent — macroeconomic agent simulation

EconAgent uses LLM-empowered heterogeneous agents to simulate work, consumption, and macroeconomic dynamics. It is relevant to economics, strategy, public policy, and data-economy courses.

- Paper: https://arxiv.org/abs/2310.10436
- Repository: https://github.com/tsinghua-fib-lab/ACL24-EconAgent
- NAAIL status: `REFERENCE_ONLY_LICENSE_REVIEW_REQUIRED`
- Reason: no root LICENSE file was observed during the 2026-09-14 review. NAAIL should not vendor, redistribute, or package its code until rights are clarified.

### 4. AI Economist — Harvard-linked academic benchmark

The AI Economist is a two-level multi-agent reinforcement-learning framework for economic-policy design. David C. Parkes, a coauthor, is a Harvard professor/dean whose research includes multi-agent AI, economics and computation, and market/mechanism design. This creates a strong **Harvard-affiliated academic benchmark**, not a Harvard product endorsement.

- Paper: https://arxiv.org/abs/2108.02755
- Harvard publication page: https://parkes.seas.harvard.edu/publications/ai-economist-taxation-policy-design-two-level-deep-multiagent-reinforcement
- Upstream repository: https://github.com/salesforce/ai-economist
- NAAIL status: `ACADEMIC_BENCHMARK_ARCHIVED`

## Big Four validation layer — use cases and governance, not endorsement

NAAIL should use current Big Four public evidence to define evaluation requirements for educational and research agents:

- **Deloitte Omnia:** public 2026 material describes a connected network of audit/assurance agents within a human-led workflow. Use this as practice evidence for role orchestration, audit-quality controls, and human approval.  
  https://www.deloitte.com/global/en/about/press-room/unveils-connected-agentic-intelligence-omnia-advance-audit-assurance.html
- **EY Assurance:** public 2026 material describes enterprise-scale agentic AI embedded in Assurance and integrated with Microsoft technology while retaining professional judgment. Use this as practice evidence for governed agent deployment and human skepticism.  
  https://www.ey.com/en_us/newsroom/2026/04/ey-launches-enterprise-scale-agentic-ai-to-redefine-the-audit-experience-for-the-ai-era
- **KPMG:** public 2026 material reports independent AIUC-1 validation of KPMG's own aIQ Capture capability after 900+ technical tests. Use this to motivate adversarial testing, hallucination testing, prompt-injection testing, reliability and governance — **not** to imply KPMG certification of NAAIL.  
  https://kpmg.com/us/en/media/news/kpmg-llp-becomes-first-big-four-firm-with-aiuc-1-certified-ai-capability.html
- **PwC:** public 2026 material highlights control failures at cross-platform agent handoffs. Use this to test identity, permission boundaries, transaction chains, audit trails, and escalation controls.  
  https://www.pwc.com/us/en/services/consulting/cybersecurity-data-tech-risk/library/agentic-ai-controls-across-platforms.html

## NAAIL integration architecture

```text
NAAIL OpenLab™ — V2026.3 Multi-Agent Digital Twin
        │
        ├── Provider-neutral orchestration adapters
        │      ├── Google ADK
        │      ├── Microsoft Agent Framework
        │      └── OpenAI Agents SDK
        │
        ├── Business-School Domain Agent Pack
        │      ├── FinRobot adapter profile
        │      ├── TradingAgents adapter profile
        │      ├── EconAgent reference profile
        │      └── AI Economist benchmark profile
        │
        ├── NAAIL specialist agents
        │      ├── Audit / CAM-KAM / KIWI™
        │      ├── IFRS Agent
        │      ├── PCAOB Agent
        │      ├── ICFR & Controls Agent
        │      ├── ESG / Sustainability Agent
        │      └── ECONOVA-S™ Data Economy Agent
        │
        ├── Evidence Passport™
        ├── Professional Decision DAG™
        ├── RPA + AA + EG + PS + DS + DIST
        ├── AIV + CER + HOR + ESC
        ├── Adversarial / Falsification Gate
        └── Human Gate
```

## Evaluation contract for every imported framework

Every comparative experiment must freeze the case evidence and record:

- upstream repository and commit/release;
- upstream license review state;
- model/provider and exact model ID;
- prompt/agent-role specification;
- tools and permissions;
- evidence IDs supplied, used, rejected, and invented;
- token/cost/runtime where measurable;
- success, failure, timeout, and null-run states;
- hallucination/fabrication rate;
- citation/evidence-grounding accuracy;
- role/handoff integrity;
- professional-skepticism and contradiction handling;
- RPA, AA, EG, PS, DS, DIST, AIV, CER, HOR, ESC;
- adversarial-review result;
- Human Gate decision.

## Classroom profiles

**Accounting/Audit:** Google ADK or Microsoft Agent Framework + NAAIL Audit/IFRS/PCAOB agents + synthetic Client XYZ + Evidence Passport.  
**Finance:** OpenAI Agents SDK or Google ADK + FinRobot/TradingAgents pattern + public/synthetic data + risk reviewer.  
**Economics/Data Economy:** EconAgent/AI Economist research pattern + ECONOVA-S™ + policy/mechanism simulation + reproducibility checks.  
**Business Analytics:** provider-neutral framework comparison + frozen dataset + ERA empirical agent + reproducible Python/R output.

## Integrity statement

Third-party project names and institutional names are used only for factual attribution and research comparison. Inclusion does not imply affiliation, sponsorship, endorsement, certification, or professional approval. Third-party licenses, model licenses, API terms, data licenses, trademarks, and usage restrictions remain controlling for those components.

Machine-readable companion: [`integrations/open_source_agents/business_school_registry.json`](./integrations/open_source_agents/business_school_registry.json)
