# NAAIL OpenLab™ — Open-Source Agent Integrations

This directory is the governed integration boundary for third-party open-source agent frameworks and domain-agent research projects used in NAAIL OpenLab™ education and research.

## Registries

- [`registry.json`](./registry.json) — general open-source orchestration and agent-framework registry.
- [`business_school_registry.json`](./business_school_registry.json) — business-school domain pack covering finance, economics, accounting-relevant analysis, institutional provenance, arXiv evidence, and professional-practice governance references.
- [`../../BUSINESS_SCHOOL_AGENT_EVIDENCE.md`](../../BUSINESS_SCHOOL_AGENT_EVIDENCE.md) — human-readable evidence and integration rationale.

## Integration rule

Third-party code is not automatically copied into NAAIL. The default mode is **reference + governed adapter**. Each executable integration must pin the upstream project/release or commit, preserve its license and attribution, declare model/API/data terms separately, restrict tools by least privilege, and submit material outputs to NAAIL evidence controls and the Human Gate.

## Business-school target architecture

```text
Google ADK / Microsoft Agent Framework / OpenAI Agents SDK
                         ↓
                 NAAIL Adapter Boundary
                         ↓
     FinRobot / TradingAgents / approved domain pattern
                         ↓
      Audit | IFRS | PCAOB | ICFR | ESG | ECONOVA-S™
                         ↓
 Evidence Passport™ → Professional Decision DAG™ → Evaluation
                         ↓
            Adversarial Review → Human Gate
```

`EconAgent` remains reference-only until its code-license position is clarified. `AI Economist` is treated as an archived academic benchmark rather than a preferred production runtime.

## Claim discipline

Institutional affiliation, use-case evidence, and upstream authorship do not imply endorsement. NAAIL does not claim that MIT, Harvard, any Big Four firm, Microsoft, Google, or OpenAI has certified or approved NAAIL or any third-party project listed here unless a separate written source explicitly establishes that fact.
