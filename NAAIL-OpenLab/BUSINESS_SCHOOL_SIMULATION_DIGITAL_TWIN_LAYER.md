# NAAIL OpenLab™ — Business School Simulation & Digital Twin Layer

**Umbrella:** NAAIL OpenLab™ — V2026.3 Multi-Agent Digital Twin  
**Canonical identity:** Next-Generation Accounting, Audit & Assurance Intelligence Lab  
**Status:** Governed supporting layer — **not a new permanent core**

## Fixed architecture rule

NAAIL preserves exactly two permanent cores:

1. **Knowledge Core™** — stable, governed standards, research evidence, professional knowledge, ontologies, evidence semantics and jurisdiction-aware knowledge.
2. **Technology Core™** — replaceable models, agent frameworks, simulation engines, orchestration, retrieval infrastructure, sandboxes, tools and adapters.

The **Business School Simulation & Digital Twin Layer** is a governed supporting layer that consumes the two cores. It does not become a third core and cannot rewrite the Knowledge Core.

```text
NAAIL OpenLab™ — V2026.3 Multi-Agent Digital Twin
│
├── PERMANENT CORE 1 — Knowledge Core™
├── PERMANENT CORE 2 — Technology Core™
│
├── Scientific Discovery & Governance Layer
├── Professional Agent Layer
│   ├── KIWI™
│   ├── POMELO™
│   ├── VERA™
│   ├── IFRS Agent™
│   ├── PCAOB Agent™
│   ├── ESG Agent
│   └── ECONOVA-S™
│
├── Business School Simulation & Digital Twin Layer   ← supporting layer
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
├── Decision–Consequence Engine™                     ← supporting service
├── Assessment & Professional Judgment Layer
│   └── Professional Judgment Passport™
└── Human Approval Gate™
```

## Purpose

The layer is designed to make NAAIL an **Evidence-Governed Multi-Agent Business School Digital Twin for Education, Research, Professional Simulation, and Verifiable Human–AI Judgment**.

It is not positioned as a generic AI tutor or chatbot. A NAAIL simulation is expected to expose a learner to evidence, uncertainty, professional standards, competing agent recommendations, consequences, contradictory evidence, professional judgment and accountable human approval.

## Simulation families

### 1. Company Digital Twin

Synthetic or research-safe company operations, transactions, estimates, disclosures, incentives, internal controls, financing choices, operational events and management decisions.

### 2. Audit Firm Digital Twin

Engagement planning, team roles, audit-risk assessment, assertions, procedures, evidence, review, CAM/KAM decisions, independence, quality management and inspection challenge.

### 3. Regulator Digital Twin

Public-rule and public-evidence simulations involving PCAOB, SEC, accounting/sustainability standard setters, supervisory attention and remediation. No confidential regulator information is implied.

### 4. Capital-Market Digital Twin

Investor information, valuation, asset pricing, market reaction, portfolio/risk decisions, disclosure consequences and market microstructure research.

### 5. Sustainability Digital Twin

ESRS/ISSB/GRI-oriented reporting problems, climate/carbon information, materiality, sustainability assurance, transition risk and People × Planet × Society × Sustainable Profit™ consequences.

### 6. Accounting Digital Twin

Recognition, measurement, presentation, disclosure, estimates, impairment, revenue, leases, financial instruments, provisions, tax and other standards-grounded judgments.

### 7. Finance Digital Twin

Valuation, capital structure, investment, portfolio, risk, credit, M&A and financial decision simulations.

### 8. Economics Digital Twin

Heterogeneous agents, macro/household/firm behavior, policy scenarios, data-economy research and ECONOVA-S™ empirical experiments.

### 9. Governance / Board Digital Twin

Board decisions, incentives, risk oversight, audit committee interaction, internal controls, sustainability governance, stakeholder trade-offs and escalation.

## Canonical simulation loop

```text
Research-backed learning objective
        ↓
Authoritative / governed evidence
        ↓
Evidence Passport™
        ↓
Digital Twin state t
        ↓
Student + Professional Agents
        ↓
Professional Decision DAG™
        ↓
Decision–Consequence Engine™
        ↓
Digital Twin state t+1
        ↓
Agent Arena™ / Critic / Defender / Falsifier
        ↓
Blind Gold / Evaluation
        ↓
Reproducibility + Falsification
        ↓
Professional Judgment Passport™
        ↓
Human Approval Gate™
        ↓
Next scenario state / learning feedback
```

## Decision–Consequence Engine™

The engine converts professional decisions into explicit, inspectable state transitions. Consequences can affect:

- business performance and operating risk;
- accounting estimates and misstatement risk;
- internal-control state;
- audit scope, evidence requirements and CAM/KAM decisions;
- regulator/inspection attention;
- investor confidence and market conditions;
- financing/liquidity and risk;
- sustainability/climate metrics and credibility;
- governance and stakeholder outcomes.

The engine must distinguish **pedagogical assumptions** from empirically estimated effects. Synthetic transition rules are never presented as real-world causal estimates.

## Professional Judgment Passport™

Each learner/simulation can produce a portable research/education record of demonstrated judgment dimensions:

1. **Evidence Quality (EQ)** — relevance, reliability, provenance and contradictory-evidence handling.
2. **Professional Skepticism (PS)** — challenge of management and agent assertions.
3. **Risk Identification (RI)** — identification, prioritization and linkage of business/audit/reporting risks.
4. **Accounting Judgment (AJ)** — standards-grounded recognition, measurement, estimate and disclosure judgment.
5. **Audit Judgment (AUJ)** — assertions, procedures, sufficiency/appropriateness and escalation.
6. **CAM/KAM Reasoning (CKR)** — significant-auditor-attention reasoning, specificity and evidence linkage.
7. **AI Verification (AIV)** — checking evidence, hallucinations, unsupported reasoning and model limitations.
8. **Ethics & Public Interest (ETH)** — integrity, objectivity, independence, confidentiality and affected stakeholders.
9. **Human Override Quality (HOR)** — quality of accept/modify/reject/escalate decisions and supporting rationale.

The Passport is an **educational/research construct**, not an automated hiring score or professional certification.

## Shared governance controls

Every material simulation inherits:

- **Evidence Passport™** — source, version, rights, transformations, hashes where feasible and evidence authority.
- **Professional Decision DAG™** — assumptions, evidence, decisions, dependencies and downstream consequences.
- **Agent Arena™** — structured disagreement rather than consensus-as-truth.
- **Blind Gold / Evaluation** — withheld labels/answers where appropriate to reduce contamination and overfitting.
- **Reproducibility** — frozen cases, environment/version capture and repeatable scoring.
- **Falsification** — counter-hypotheses, alternative explanations and failure-seeking tests.
- **Human Approval Gate™** — accountable human accept/modify/reject/request-more-evidence/escalate decision.

## Technology Core adapters

The following open-source technologies may be admitted **only as replaceable Technology Core adapters** after version, license, security, reproducibility and benchmark review:

| Technology | Potential NAAIL role |
|---|---|
| **Mesa** | general agent-based company, governance and classroom simulations |
| **AgentTorch** | large-population / differentiable agent simulations where scale materially adds value |
| **SimPy** | discrete-event business-process, audit-workflow and service/queue simulations |
| **OpenAI Agents SDK** | optional agent orchestration, tools, guardrails, handoffs, tracing and human-in-the-loop paths |
| **Microsoft Agent Framework** | optional provider-neutral/multi-agent workflow orchestration and enterprise integration paths |
| **HARK (Econ-ARK)** | heterogeneous-agent economics / household / policy simulations for ECONOVA-S™ |
| **ABIDES** | capital-market / exchange / trading-agent simulation research |
| **FinRL** | financial reinforcement-learning education and research experiments |
| **RD-Agent** | research-and-development automation experiments, model/data iteration and research workflow benchmarking |

No framework is authoritative professional knowledge. No framework may silently change standards meaning, ontology, evidence authority, causal DAGs or the Human Gate.

## First prototype

The first dynamic prototype is **NAAIL Audit & Accounting Digital Twin™**.

It combines:

- realistic synthetic/public company evidence;
- IFRS accounting issues;
- internal-control weaknesses;
- management pressure/incentives;
- audit-risk and evidence decisions;
- CAM/KAM reasoning;
- PCAOB-style public-standards challenge;
- AI-agent recommendations and disagreement;
- Decision–Consequence Engine™ state changes;
- student defense of professional judgment;
- Professional Judgment Passport™;
- mandatory Human Approval Gate™.

Canonical specification: [`digital-twins/audit-accounting/README.md`](./digital-twins/audit-accounting/README.md)

## Permanent invariants

```text
permanent_core_count = 2
knowledge_core_is_permanent = true
technology_core_is_permanent = true
business_school_simulation_layer_is_core = false
decision_consequence_engine_is_core = false
professional_judgment_passport_is_core = false
technology_core_may_rewrite_knowledge_core = false
external_framework_is_authoritative_professional_truth = false
synthetic_consequence_rule_is_real_world_causal_effect = false
agent_consensus_is_truth = false
student_score_equals_employability_truth = false
human_gate_required = true
```

## Independence

NAAIL OpenLab™ is independent. References to software projects, standard setters, regulators, professional firms, universities or technology providers identify public tools, evidence sources, research contexts or optional adapters only; they do not imply affiliation, endorsement, accreditation, certification or partnership.