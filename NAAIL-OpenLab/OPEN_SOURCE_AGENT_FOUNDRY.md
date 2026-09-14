# NAAIL OpenLab™ — Open-Source Academic Agent Foundry

**Status:** v0.2.4 target capability  
**Umbrella:** NAAIL OpenLab™ — V2026.3 Multi-Agent Digital Twin  
**Purpose:** Research-safe integration of open-source agent frameworks and academic multi-agent methods for business-school education, professional simulation, and reproducible research.

> NAAIL OpenLab™ remains the master platform. External frameworks are dependencies, research inspirations, or interoperability targets. They are not NAAIL-owned technologies and their inclusion does not imply affiliation, endorsement, sponsorship, certification, or partnership with Stanford University, MIT, Hugging Face, any Big Four firm, investment bank, regulator, or technology company.

## Canonical position

```text
NAAIL OpenLab™
V2026.3 Multi-Agent Digital Twin
│
├── Scientific Discovery & Governance Layer
├── Specialist Professional Agents
│   ├── POMELO™
│   ├── KIWI™
│   ├── IFRS Intelligence Agent™
│   ├── PCAOB Intelligence Agent™
│   ├── ECONOVA-S™
│   ├── ESG Intelligence
│   ├── ICFR Intelligence
│   └── Forensic Intelligence
│
├── Open-Source Academic Agent Foundry  ← NEW
│   ├── Stanford DSPy adapter boundary
│   ├── Stanford STORM / Co-STORM adapter boundary
│   ├── Hugging Face smolagents adapter boundary
│   ├── MIT SceneSmith-inspired Digital Twin design research
│   └── MIT/Microsoft Murakkab-inspired orchestration research
│
├── NAAIL Professional Swarm™
│   ├── Planner
│   ├── Researcher
│   ├── Analyst
│   ├── Specialist
│   ├── Critic
│   ├── Defender
│   ├── Falsifier
│   ├── Professional Reviewer
│   └── Human Gate
│
└── Education & Professional Digital Twin Layer
    ├── Audit & Assurance Simulation
    ├── Accounting / IFRS Simulation
    ├── ESG Assurance Simulation
    ├── Forensic Investigation Simulation
    ├── Internal Controls / ICFR Simulation
    ├── Consulting / Risk Simulation
    ├── Corporate Finance / M&A Simulation
    ├── Investment Banking Simulation
    └── Equity Research Simulation
```

## Executable open-source core

| Upstream | NAAIL use | Upstream license | Integration status |
|---|---|---|---|
| Stanford DSPy | LM-program optimization, evaluation-driven agent/RAG pipelines | MIT | Adapter boundary / dependency registry |
| Stanford STORM / Co-STORM | Multi-perspective evidence curation, expert-agent discussion, cited research workflows | MIT | Adapter boundary / dependency registry |
| Hugging Face smolagents | Lightweight tool-calling, code agents, managed/multi-agent orchestration | Apache-2.0 | Primary executable swarm candidate |
| MIT SceneSmith | Research inspiration for compositional, simulation-ready Digital Twin construction | MIT | Conceptual research inspiration; no copied code by default |
| MIT/Microsoft Murakkab | Research inspiration for cost/latency/resource-aware workflow orchestration | Research system | Conceptual orchestration benchmark; no copied code by default |

Canonical machine-readable registry: [`agents/open-source-agent-foundry/registry.json`](./agents/open-source-agent-foundry/registry.json).

## NAAIL Professional Swarm™ protocol

```text
Professional Problem
      ↓
Student / Researcher Initial Judgment
      ↓
Task Decomposition
      ↓
Minimum Necessary Specialist-Agent Selection
      ↓
Parallel Evidence Retrieval + Independent Analysis
      ↓
Critic ↔ Defender Adversarial Review
      ↓
Authoritative-Standards / Evidence Check
      ↓
Quantitative / Empirical Validation
      ↓
Falsifier + Replicator
      ↓
Professional Decision DAG™
      ↓
Evidence Passport™
      ↓
Human Gate
      ↓
Learning Feedback / Research Artifact
```

The swarm is **evidence-governed, not consensus-governed**. More agents agreeing does not make a claim correct. Material professional or scientific conclusions require traceable evidence and human approval.

## Business-school and professional-practice simulations

The Foundry supports neutral educational simulations inspired by professional workflows without reproducing proprietary systems or claiming equivalence to them.

### Audit / assurance lab

`Student Associate → Senior Agent → Manager Agent → Partner-Review Agent`, with optional IFRS, PCAOB, ICFR, KIWI™, forensic, valuation, ESG, tax, cybersecurity, and data-analytics specialists.

### Investment banking / finance lab

`Analyst → Associate → VP Review → Investment Committee`, with valuation, DCF, comparable-company, M&A, capital-markets, credit, risk, macro, SEC/XBRL, ECONOVA-S™, ESG, and compliance specialists.

### Consulting / risk lab

`Problem Framing → Data Evidence → Competing Recommendations → Adversarial Challenge → Implementation Risks → Human Executive Gate`.

Names of firms such as Deloitte, EY, KPMG, PwC, Goldman Sachs, Morgan Stanley, JPMorgan, or similar organizations may be discussed as public industry reference points only. NAAIL simulations use neutral fictional organizations unless written authorization permits otherwise.

## Education design

The corresponding education layer is the **NAAIL Professional Swarm Academy™**. Students must be able to:

1. form an independent judgment before seeing agent recommendations;
2. inspect the evidence used by each agent;
3. challenge or reject agent output;
4. identify unsupported or hallucinated evidence;
5. compare alternative specialist views;
6. document escalation and override decisions;
7. pass the Human Gate before a material conclusion is finalized.

See [`docs/education/NAAIL_PROFESSIONAL_SWARM_ACADEMY.md`](./docs/education/NAAIL_PROFESSIONAL_SWARM_ACADEMY.md).

## Public/private boundary

**Public:** architecture, dependency registry, attribution, synthetic role definitions, research-safe examples, evaluation contracts, and teaching specifications.

**Private / controlled:** credentials, unpublished prompts, partner-confidential content, licensed data, detailed orchestration IP, private gold labels, proprietary evaluation sets, patent-candidate mechanisms, and production deployment configuration.

## Upstream sources

- DSPy: https://github.com/stanfordnlp/dspy
- STORM / Co-STORM: https://github.com/stanford-oval/storm
- Hugging Face smolagents: https://github.com/huggingface/smolagents
- SceneSmith: https://github.com/nepfaff/scenesmith
- Murakkab overview: https://news.mit.edu/2026/improving-ai-agent-speed-and-energy-efficiency-0625

Always verify the upstream repository, current commit, dependency version, model terms, and license before a production or redistribution decision.
