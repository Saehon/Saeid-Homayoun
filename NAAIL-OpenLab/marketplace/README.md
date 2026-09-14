# NAAIL OpenLab™ Marketplace Edition

**Version target:** v0.2.4  
**Status:** Marketplace-ready public scaffold; not yet submitted or approved by OpenAI, Google, or Microsoft.

NAAIL OpenLab Marketplace Edition packages one evidence-governed research platform for distribution through three external AI ecosystems while preserving a strict public/private IP boundary.

## Product

**NAAIL OpenLab™ — Evidence-Governed Research Co-Scientist**

A human-led AI research environment for Accounting, Auditing, Assurance, Finance, Economics, and Sustainability that converts research questions into evidence-grounded hypotheses, reproducible empirical designs, governed analyses, and human-reviewed outputs.

## One core, three adapters

```text
NAAIL OpenLab Core™
│
├── Evidence / RAG / GraphRAG
├── Multi-Agent Co-Scientist
├── ERA-style empirical-design engine
├── Computational Discovery / evaluator-guided search
├── Digital Twin layer
├── Chain-of-Evidence / Evidence Passport™
├── Professional Decision DAG™
├── Evaluation + falsification + replication
└── Human Gate
     │
     ├── OpenAI adapter   → ChatGPT app surface / MCP-compatible tools
     ├── Google adapter   → Google Cloud / Gemini Enterprise agent surface
     └── Microsoft adapter→ Microsoft Marketplace / Copilot agent surface
```

## Public/private boundary

### Public marketplace package
- product and architecture documentation;
- tool/API contracts;
- provider-neutral schemas;
- synthetic examples;
- privacy, security and data-handling disclosures;
- submission checklists;
- non-sensitive adapter templates;
- evaluation and Human-Gate requirements.

### Private NAAIL R&D
- proprietary orchestration and routing logic;
- unpublished prompts and agent specifications;
- private or licensed datasets;
- restricted standards text and copyrighted corpora;
- private benchmark gold labels;
- patent-candidate mechanisms;
- production credentials, secrets and provider keys;
- commercial scoring logic and unpublished research results.

## Marketplace packages

- [`openai/`](./openai/) — ChatGPT Apps SDK / MCP-oriented distribution package.
- [`google/`](./google/) — Google Cloud Marketplace / Gemini Enterprise-oriented package.
- [`microsoft/`](./microsoft/) — Microsoft Marketplace / Microsoft 365 Copilot-oriented package.
- [`SUBMISSION_CHECKLIST.md`](./SUBMISSION_CHECKLIST.md) — common release gates.
- [`SECURITY_DATA_HANDLING.md`](./SECURITY_DATA_HANDLING.md) — data, privacy, logging and human-control policy.

## Canonical workflow

**Question → evidence validation → competing hypotheses → critique/ranking → empirical design → data-rights gate → executable analysis → robustness/falsification → adversarial review → replication → Chain-of-Evidence → Human Gate → exportable research artifact**

## Non-claims

This repository does not claim partnership, certification, endorsement, approval, listing, or publication by OpenAI, Google, Microsoft, or any other third party. Marketplace status must be represented only after the corresponding provider has completed its own review and approval process.

## Principal Investigator

Dr. Saeid Homayoun  
ORCID: https://orcid.org/0000-0002-2536-0446
