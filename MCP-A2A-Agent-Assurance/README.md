# NAAIL MCP + A2A Agent Assurance Platform

**Status:** architecture and research-design package  
**Purpose:** build a vendor-neutral accounting, audit and finance assurance layer across Claude, GPT, Gemini, Mistral and other compatible agents.

## Architecture

![NAAIL MCP + A2A Agent Assurance Architecture](assets/mcp_a2a_agent_assurance_architecture.svg)

## Core idea

MCP provides standardized access to tools and data. A2A provides agent-to-agent collaboration and handoffs. NAAIL adds the domain-specific assurance layer: provenance, independent review, falsification, controls, evidence lineage and human approval.

```text
Claude / GPT / Gemini / Mistral / Other LLMs
                    |
                    v
             A2A Agent Mesh
                    |
                    v
               MCP Gateway
                    |
      +-------------+-------------+
      |             |             |
   SEC/XBRL       ICFR          IFRS
      |             |             |
     CAM           KAM        Audit/ESG
      +-------------+-------------+
                    |
             Evidence Passport
                    |
          Reviewer / Falsifier
                    |
              Control Plane
                    |
             Human Approval
                    |
        Audit-ready outputs/APIs
```

## Build order

1. SEC/XBRL Data MCP
2. LEMON-ICFR-US MCP
3. Apple-CAM-US MCP
4. Orange-KAM-EU-UK MCP
5. Mango-IFRS MCP
6. Finance & Operations Audit MCP
7. Research Assurance MCP
8. A2A orchestration across proven specialist MCPs
9. Agentic transaction assurance using AP2/UCP where relevant
10. A2UI/MCP Apps for interactive professional interfaces

## Research proposition

The central research question is whether **independent specialist agents plus adversarial AI-to-AI assurance and a targeted human gate** can reduce unsupported claims and decision errors relative to single-agent and conventional human-AI designs.

This repository package is deliberately evidence-first. Architecture claims are separated from empirical claims. No performance benefit is treated as established until tested on fresh, independent benchmarks.

## Inspiration from AI-for-science

- **AlphaFold:** benchmark-driven prediction with explicit confidence and reproducibility.
- **AlphaEvolve:** generate-evaluate-iterate loops with automated evaluators.
- **AI co-scientist:** role-specialized multi-agent generation, critique and refinement.
- **Mistral multi-agent handoffs:** practical agent-to-agent orchestration pattern.
- **NAAIL adaptation:** replace scientific candidates with accounting/audit judgments, and replace scientific evaluators with standards, controls, calculations, provenance checks and independent reviewers.

## Governance

- Model agreement is not evidence.
- Reviewer/falsifier agents must be operationally independent of the generating agent.
- Evidence lineage must be inspectable.
- Sensitive actions require explicit authorization and human approval.
- Benchmark fixtures used for development are not reused as independent evidence.
- Model/version/tool/data provenance must be recorded.

## Related project assets

The platform is designed to connect existing specialist projects rather than replace them:
LEMON-ICFR-US, Mango-IFRS, Apple-CAM-US, Orange-KAM-EU-UK, SEC/XBRL tooling, NAAIL Research Assurance, AuditData API, ESG/ESRS/VSME, PCAOB inspection concepts, and DARWIN-POMELO/VERA orchestration.
