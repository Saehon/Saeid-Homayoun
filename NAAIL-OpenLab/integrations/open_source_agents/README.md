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

## Google Drive mirror — 2026-09-14

GitHub remains the technical source of truth. Exact research/archive mirrors have been saved in the user's **NAAIL OpenLab** Google Drive folder:

- Business-School Agent Evidence Pack: https://drive.google.com/file/d/1bE-TSifyja1oym-OQY0svXnlrunpVPEE/view
- Machine-readable Business-School registry: https://drive.google.com/file/d/1KfkMjFAXR-j264tIq-fpQNCTcofG4rH6/view
- Open-Source Agent Integrations mirror README: https://drive.google.com/file/d/1fX2895MAJqqgbZOKurcDlXxZUmnykYai/view
- NAAIL OpenLab Drive folder: https://drive.google.com/drive/folders/193O-ICy6843wEgP0gy713cGUbYq8rGy0

This mirror does not change the upstream-license rule: third-party software, model weights, APIs, datasets, trademarks and papers remain governed by their own terms.

## Claim discipline

Institutional affiliation, use-case evidence, and upstream authorship do not imply endorsement. NAAIL does not claim that MIT, Harvard, any Big Four firm, Microsoft, Google, or OpenAI has certified or approved NAAIL or any third-party project listed here unless a separate written source explicitly establishes that fact.
