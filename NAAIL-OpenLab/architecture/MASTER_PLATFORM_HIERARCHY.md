# NAAIL OpenLab™ — Canonical Master Platform Hierarchy

**Canonical version:** V2026.3 Multi-Agent Digital Twin  
**Status:** Master branding and architecture hierarchy  
**Applies to:** README files, architecture documents, agent families, studies, education assets, simulations, evidence/data connectors, benchmarks, public product descriptions, and future releases.

## Canonical brand relationship

**NAAIL OpenLab™ → fixed umbrella platform**  
**V2026.3 Multi-Agent Digital Twin → canonical architecture**  
**Knowledge Core™ + Technology Core™ → exactly two permanent cores**  
**All other capabilities → governed supporting layers, agents, services, Digital Twins, registries, evaluations or interfaces**

Professional agent set:

**KIWI™ · POMELO™ · VERA™ · IFRS Agent™ · PCAOB Agent™ · ESG Agent · ECONOVA-S™**

ICFR and Forensic Intelligence remain specialist capabilities under the same umbrella. No specialist family is a competing umbrella platform.

## Two permanent cores — fixed

### Core 1 — Knowledge Core™

Stable, governed, versioned professional/scientific knowledge:

- authoritative standards and regulation references;
- accounting, audit, sustainability, finance and economics ontologies;
- evidence semantics and provenance rules;
- governed GraphRAG / retrieval semantics;
- research evidence and jurisdiction mappings;
- professional judgment concepts and validated knowledge objects.

### Core 2 — Technology Core™

Replaceable implementation technology:

- foundation models and local models;
- agent runtimes and orchestrators;
- vector databases / graph databases;
- simulation frameworks;
- ERP adapters;
- code execution / sandboxes;
- provider APIs;
- evaluation tooling;
- data connectors and transformation tools.

Technology may consume governed knowledge but cannot silently change canonical evidence meaning, ontology, standards interpretation, causal DAGs or RAG semantics.

```text
permanent_core_count = 2
knowledge_core_is_permanent = true
technology_core_is_permanent = true
supporting_layer_may_become_third_core = false
technology_core_may_rewrite_knowledge_core = false
```

## Master hierarchy

```text
NAAIL OpenLab™
V2026.3 Multi-Agent Digital Twin
│
├── PERMANENT CORE 1 — Knowledge Core™
│   ├── Standards / Regulation Knowledge
│   ├── Accounting / Audit / ESG / Finance Ontologies
│   ├── Evidence Semantics + Provenance
│   ├── Governed GraphRAG
│   ├── Research Evidence
│   └── Jurisdiction / Sector / Language Packs
│
├── PERMANENT CORE 2 — Technology Core™
│   ├── Models / Embeddings
│   ├── Agent Runtimes / Orchestration
│   ├── Simulation Engines
│   ├── Vector / Graph Infrastructure
│   ├── ERP / Data / Tool Adapters
│   ├── Sandboxes / Code Execution
│   └── Replaceable Provider Integrations
│
├── NAAIL Data & Evidence Mesh™                       [SUPPORTING]
│   ├── SEC EDGAR / XBRL connectors
│   ├── FRED / ALFRED connectors
│   ├── Fama–French references
│   ├── World Bank Indicators API
│   ├── OWID CO₂ / Energy references
│   ├── OpenAlex scholarly metadata
│   ├── OpenSanctions research connector
│   ├── Optional OpenBB provider connectors
│   ├── Rights / License / Version Gate
│   ├── Evidence Passport™ Builder
│   └── Validation / Reconciliation / Agent Routing
│
├── Scientific Discovery & Governance Layer
│   ├── AI Co-Scientist / Hypothesis Arena
│   ├── ERA-style Empirical Design
│   ├── AlphaEvolve-style Model / Specification Search
│   ├── Computational Discovery
│   ├── Chain-of-Evidence
│   ├── Adversarial Review
│   ├── Reproducibility / Falsification
│   ├── Blind Gold / Evaluation
│   └── Human Approval Gate™
│
├── Professional Agent Layer
│   ├── KIWI™ — Audit / CAM / KAM Intelligence
│   ├── POMELO™ — Accounting & Assurance Intelligence
│   ├── VERA™ — Verifiable Accounting & Auditing Intelligence
│   ├── IFRS Agent™ — Reporting & Standards Digital Twin
│   ├── PCAOB Agent™ — Inspection / Regulatory Digital Twin
│   ├── ESG Agent — Sustainability / Climate / Assurance
│   ├── ECONOVA-S™ — Finance / Economics / Data Economy
│   ├── ICFR & Controls Intelligence
│   └── Forensic Intelligence
│
├── Business School Simulation & Digital Twin Layer      [SUPPORTING]
│   ├── Company Digital Twin
│   ├── Audit Firm Digital Twin
│   ├── Regulator Digital Twin
│   ├── Capital-Market Digital Twin
│   ├── Sustainability Digital Twin
│   ├── Accounting Digital Twin
│   ├── Finance Digital Twin
│   ├── Economics Digital Twin
│   └── Governance / Board Digital Twin
│
├── Decision–Consequence Engine™                         [SUPPORTING SERVICE]
│   └── Decision at state t → transparent consequence ledger → state t+1
│
├── Assessment / Learning Governance Layer               [SUPPORTING]
│   ├── Evidence Passport™
│   ├── Professional Decision DAG™
│   ├── Agent Arena™
│   ├── Professional Judgment Passport™
│   ├── Reproducibility / Falsification
│   └── Human Approval Gate™
│
├── Data & Evidence Layer                                [SUPPORTING]
│   ├── IFRS Foundation / IASB / ISSB references
│   ├── SEC / EDGAR / XBRL
│   ├── PCAOB public standards / inspections / enforcement
│   ├── EFRAG / ESRS / sustainability evidence
│   ├── AAER / CAM / KAM
│   ├── Fama–French / Damodaran / FRED / World Bank
│   ├── ESG / climate / carbon sources
│   └── Open research / replication repositories
│
└── Education & Professional Simulation Layer            [SUPPORTING]
    ├── Student Digital Twins
    ├── Audit / Accounting Simulations
    ├── IFRS / PCAOB Simulations
    ├── Finance / Economics Simulations
    ├── ESG / Sustainability Simulations
    ├── ERP / Business Process Simulations
    ├── Governance / Risk Simulations
    ├── Professional Swarm Academy
    └── Reproducible Research Laboratories
```

## NAAIL Data & Evidence Mesh™

Canonical specification: [`../DATA_EVIDENCE_MESH.md`](../DATA_EVIDENCE_MESH.md)  
Machine-readable registry: [`data_evidence_mesh_registry.json`](./data_evidence_mesh_registry.json)

The Mesh is a **supporting data/evidence routing layer**, not a permanent core. It uses APIs/connectors, source IDs, retrieval timestamps, periods/vintages, rights/license metadata, hashes/checksums where feasible, transformation lineage and Evidence Passport™ instead of committing large third-party datasets to GitHub.

Primary source families are:

- SEC EDGAR / XBRL;
- FRED / ALFRED;
- Fama–French;
- World Bank;
- Our World in Data CO₂ / Energy;
- OpenAlex;
- OpenSanctions for non-commercial/academic forensic/governance research under applicable terms;
- optional OpenBB provider connectors as Technology-Core adapters.

The Mesh inherits the existing **NAAIL Free Data Fabric™** source-governance rules. Free Data Fabric governs source discovery/admission; Data & Evidence Mesh governs runtime retrieval/reference, Evidence Passport generation, validation/reconciliation and agent/Digital Twin routing.

```text
Real Data
→ Evidence Passport™
→ Multi-Agent Analysis
→ Digital Twin Simulation
→ Decision
→ Consequence
→ Verification
→ Human Approval Gate™
```

## Business School Simulation & Digital Twin Layer

Canonical specification: [`../BUSINESS_SCHOOL_SIMULATION_DIGITAL_TWIN_LAYER.md`](../BUSINESS_SCHOOL_SIMULATION_DIGITAL_TWIN_LAYER.md)

The layer supports dynamic simulations across company, audit firm, regulator, capital market, sustainability, accounting, finance, economics and governance contexts.

It inherits the canonical simulation loop:

```text
Research-backed learning objective
→ Governed evidence
→ Evidence Passport™
→ Digital Twin state t
→ Student + professional agents
→ Professional Decision DAG™
→ Decision–Consequence Engine™
→ Digital Twin state t+1
→ Agent Arena™ / Critic / Defender / Falsifier
→ Blind Gold / Evaluation
→ Reproducibility / Falsification
→ Professional Judgment Passport™
→ Human Approval Gate™
```

## Decision–Consequence Engine™

The engine is a supporting service, not a core. It records explicit state transitions caused by learner/professional decisions across business, accounting, controls, audit, market, regulatory and ESG dimensions.

All consequence rules must state whether they are:

- `SYNTHETIC_PEDAGOGICAL_TRANSITION`;
- `EMPIRICALLY_CALIBRATED_TRANSITION`; or
- `POLICY_OR_STANDARD_CONSTRAINT`.

Synthetic transitions must never be presented as real-world causal estimates.

Reference implementation: [`../simulations/business-school/decision_consequence_engine.py`](../simulations/business-school/decision_consequence_engine.py)

## Professional Judgment Passport™

The Passport is a governed educational/research assessment record measuring:

- **EQ** — Evidence Quality;
- **PS** — Professional Skepticism;
- **RI** — Risk Identification;
- **AJ** — Accounting Judgment;
- **AUJ** — Audit Judgment;
- **CKR** — CAM/KAM Reasoning;
- **AIV** — AI Verification;
- **ETH** — Ethics & Public Interest;
- **HOR** — Human Override Quality.

Machine-readable schema: [`professional_judgment_passport.schema.json`](./professional_judgment_passport.schema.json)

The Passport is not a professional certification and is not validated for automated employment decisions.

## Professional agent boundaries

### POMELO™
Accounting, assurance, professional intelligence, evidence verification, accounting judgment, standards-aware reasoning and related workflows.

### KIWI™
Audit intelligence focused on Critical Audit Matters, Key Audit Matters, evidence, assertions, risk–procedure alignment, audit quality and CAM/KAM research.

### VERA™
Verifiable Accounting & Auditing Intelligence. Evidence verification, Judgment Graph / GraphRAG validation, Evidence Passport™, Professional Decision DAG™, DAG Watch™, Blind Gold / evaluation, Failure Memory™ and Human Gate verification.

Canonical path: [`../agents/vera/README.md`](../agents/vera/README.md)

### IFRS Agent™
IFRS Accounting Standards, financial reporting, policy/estimate/disclosure judgments, cross-standard reasoning, evidence provenance and human-reviewed decision support.

### PCAOB Agent™
PCAOB public auditing standards/rules/inspection/enforcement evidence; deficiency classification; remediation research; ICFR/audit-quality linkage; governed inspection simulation. It does not represent the PCAOB or imply non-public access.

### ESG Agent
Sustainability reporting, ESG measurement, ESRS/ISSB/GRI-oriented analysis, climate/carbon, assurance, materiality and sustainability research.

### ECONOVA-S™
Economics, finance, data economy, asset pricing, Fama–French, SEC/XBRL/FRED/World Bank/OWID economic evidence, economic Digital Twins and empirical research.

### ICFR & Forensic capabilities
Internal controls/material weaknesses and fraud/anomaly/investigative analytics remain specialist capabilities under the same NAAIL architecture.

## Technology Core simulation and data adapters

The Technology Core may evaluate and admit replaceable adapters such as:

- **Mesa** — general Python agent-based modeling;
- **AgentTorch** — large-population/differentiable agent simulations;
- **SimPy** — discrete-event business-process/workflow simulation;
- **OpenAI Agents SDK** — optional agent orchestration/guardrails/handoffs/tracing;
- **Microsoft Agent Framework** — optional multi-agent workflow/provider abstraction;
- **HARK / Econ-ARK** — heterogeneous-agent economics;
- **ABIDES** — capital-market/exchange-agent simulation;
- **FinRL** — financial reinforcement-learning education/research;
- **RD-Agent** — R&D automation/model-data iteration experiments;
- **OpenBB provider extensions** — optional finance-data provider abstraction while preserving original-provider provenance/terms.

Canonical simulation registry: [`business_school_simulation_technology_registry.json`](./business_school_simulation_technology_registry.json)

Framework/connector inclusion does **not** mean installation, execution, validation, professional authority or admission to the Knowledge Core.

## First dynamic prototype

The first dynamic prototype is **NAAIL Audit & Accounting Digital Twin™**:

[`../digital-twins/audit-accounting/README.md`](../digital-twins/audit-accounting/README.md)

It combines realistic synthetic/public evidence, SEC/XBRL context, macro/market/context evidence through the Data & Evidence Mesh, IFRS issues, internal-control weaknesses, management pressure, CAM/KAM decisions, PCAOB-style public-standards challenge, multi-agent interaction, dynamic decision consequences, student defense, Professional Judgment Passport™ and Human Approval Gate™.

It may reuse validated patterns from Prototype 003, but live-connector and provider-backed dynamic execution remain separate validation milestones.

## Free / open-source simulation and data rule

The deterministic core must remain runnable without a paid model API where feasible. External data should be accessed through source references/APIs/connectors rather than mirrored wholesale into GitHub. Optional external frameworks/providers are admitted only after version pinning, license review, security review, reproducibility testing, data-rights review where applicable and benchmark comparison.

Convenience tools never outrank authoritative evidence. Protected standards text is not bundled merely for convenience. Free/open tooling never implies access to restricted regulator or firm data.

## Shared scientific-discovery layer

All publication-grade work inherits one scientific constitution:

```text
literature grounding
→ competing hypotheses
→ DAG governance
→ ERA empirical conversion
→ real/rights-cleared data + code
→ evaluator-guided model/specification search
→ robustness / OOS
→ adversarial review
→ falsification
→ independent replication
→ Chain-of-Evidence / CoE Audit
→ Human Approval Gate™
```

```text
discovery_claim_allowed_by_agent_alone = false
agent_consensus_is_scientific_truth = false
statistical_significance_is_discovery = false
optimize_for_p_value = false
failed_tests_are_deleted = false
human_gate_required = true
```

## Canonical repository/navigation target

```text
NAAIL-OpenLab/
├── README.md
├── DATA_EVIDENCE_MESH.md
├── architecture/
│   ├── MASTER_PLATFORM_HIERARCHY.md
│   ├── data_evidence_mesh_registry.json
│   ├── professional_judgment_passport.schema.json
│   └── business_school_simulation_technology_registry.json
├── agents/
│   ├── pomelo/
│   ├── kiwi/
│   ├── vera/
│   ├── ifrs/
│   ├── pcaob/
│   ├── econova-s/
│   ├── esg/
│   ├── icfr/
│   └── forensic/
├── digital-twins/
│   └── audit-accounting/
├── simulations/
│   ├── business-school/
│   └── free-stack/
├── scientific-discovery/
├── education/
├── datasets/              # small/synthetic/rights-cleared assets only by default
├── benchmarks/
├── examples/
└── docs/
```

This is a navigation target. Existing links/history/CI paths should be preserved during incremental migration.

## Naming and governance rules

1. Public pages introduce **NAAIL OpenLab™** before specialist agents.
2. The architecture always preserves **exactly two permanent cores**: Knowledge Core™ and Technology Core™.
3. The Data & Evidence Mesh™, Business School Simulation & Digital Twin Layer, Decision–Consequence Engine™ and Professional Judgment Passport™ are supporting capabilities, not cores.
4. KIWI™, POMELO™, VERA™, IFRS Agent™, PCAOB Agent™, ESG Agent and ECONOVA-S™ remain under the NAAIL umbrella.
5. `V2026.3 Multi-Agent Digital Twin` identifies architecture; semantic versions such as `v0.2.3` identify executable releases.
6. External AI systems, simulation frameworks, data providers, regulators, standard setters and firms remain evidence sources, tools, methodological inspirations, providers or benchmarks unless a documented relationship exists.
7. Large third-party datasets should not be committed to GitHub by default; preserve connector/query/version/rights/provenance metadata instead.
8. Shared scientific governance cannot be weakened locally.
9. Human approval remains mandatory for consequential professional, educational-promotion or scientific claims.

## Governance priority

If older repository text conflicts with this document, this hierarchy is the preferred architecture interpretation for future edits. Historical release records should remain historically accurate rather than being silently rewritten.
