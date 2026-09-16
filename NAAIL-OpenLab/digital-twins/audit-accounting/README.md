# NAAIL Audit & Accounting Digital Twin™ — Prototype 001

**Parent architecture:** NAAIL OpenLab™ — V2026.3 Multi-Agent Digital Twin  
**Layer:** Business School Simulation & Digital Twin Layer  
**Data layer:** NAAIL Data & Evidence Mesh™ — supporting layer, not a core  
**Status:** Research/education prototype specification; dynamic consequence engine published separately; real-data connectors are registry/specification level unless an Evidence Passport records execution.

## Objective

Create a realistic, evidence-governed business-school simulation in which accounting and audit judgments evolve over time and can be grounded in reproducible public evidence.

Canonical flow:

```text
Real Data
→ Evidence Passport™
→ Multi-Agent Analysis
→ Audit & Accounting Digital Twin
→ Student / Research Decision
→ Professional Decision DAG™
→ Decision–Consequence Engine™
→ Updated Digital Twin State
→ Verification / Agent Arena™ / Blind Gold
→ Professional Judgment Passport™
→ Human Approval Gate™
```

The learner must analyze company evidence, apply IFRS reasoning, identify internal-control weaknesses, respond to management pressure, evaluate CAM/KAM issues, challenge AI agents, withstand a PCAOB-style public-standards review, and defend the final professional judgment before a Human Approval Gate™.

## Canonical scenario

**Client:** Client XYZ — synthetic public-company-style reporting entity.  
**Audit firm:** Firm Alpha — fictional audit firm.  
**Period:** multi-stage year-end reporting/audit cycle.  
**Evidence:** synthetic case evidence plus reproducibly referenced public/rights-cleared evidence retrieved through the Data & Evidence Mesh where applicable.  
**Gold labels:** withheld from students/agents where Blind Gold evaluation is used.

The prototype does not pretend that Client XYZ is a real SEC issuer. Public evidence is used to create context, comparators, macro/market conditions, research grounding and reproducible professional exercises while preserving the synthetic identity of the simulated client.

## NAAIL Data & Evidence Mesh™ binding

The first prototype may combine:

| Evidence family | Prototype role |
|---|---|
| **SEC EDGAR / XBRL** | issuer/filing structures, Company Facts patterns, accounting ratios, disclosure evidence and public-company comparators |
| **FRED / ALFRED** | macroeconomic, rates, inflation, labor, credit and vintage-aware context |
| **Fama–French** | factor/portfolio market context for valuation, risk and capital-market consequences where relevant |
| **World Bank** | country/macro/development context and external-validity variables |
| **OWID CO₂ / Energy** | climate, emissions, energy and sustainability context when material |
| **OpenAlex** | literature discovery, citation/topic metadata and research-evidence mapping |
| **OpenSanctions** | optional sanctions/PEP/entity-risk research for forensic/governance scenarios under applicable non-commercial/academic terms |
| **OpenBB** | optional Technology-Core provider abstraction; original provider provenance/terms always remain controlling |

Canonical Mesh specification: [`../../DATA_EVIDENCE_MESH.md`](../../DATA_EVIDENCE_MESH.md)  
Machine-readable source registry: [`../../architecture/data_evidence_mesh_registry.json`](../../architecture/data_evidence_mesh_registry.json)

### Real-data storage rule

Large third-party datasets are **not** committed to GitHub by default. The repository stores connector/source manifests, query parameters, IDs, timestamps, hashes, transformation code, small rights-cleared fixtures and Evidence Passport metadata.

## Evidence Passport™ for public evidence

Each public-data contribution to a scenario should preserve:

- source/source authority class;
- endpoint or canonical URL;
- retrieval timestamp;
- period/as-of/vintage date;
- entity/series/dataset identifiers;
- query/request parameters;
- raw/response hash where feasible;
- transformation lineage;
- rights/license/redistribution status;
- validation/reconciliation status;
- agent access scope;
- human reviewer.

For FRED/ALFRED-style revised time series, the simulation should preserve the information vintage available at the simulated decision date where feasible rather than silently using later revisions.

## Core evidence package

The first prototype should include, at minimum:

- trial balance and selected general-ledger entries;
- revenue transactions around period end;
- management estimates and impairment assumptions;
- board/audit-committee minutes;
- internal-control narratives and deficiency evidence;
- management representation / pressure signals;
- selected IFRS issue cards and official-source references;
- audit planning/risk assessment records;
- proposed procedures and evidence results;
- draft CAM/KAM reasoning;
- public PCAOB-style standards/inspection challenge prompts;
- sustainability/ESG facts where material to reporting or risk;
- AI-agent recommendations with explicit evidence references;
- selected SEC/macro/market/context Evidence Passports where relevant to the case.

## Professional agents

```text
Student / Learner
      ↓
NAAIL Data & Evidence Mesh™
      ↓
POMELO™ — accounting / assurance reasoning
KIWI™ — CAM/KAM / audit evidence
VERA™ — verification / evidence challenge
IFRS Agent™ — accounting standards judgment
PCAOB Agent™ — public-regulatory challenge
ESG Agent — sustainability / climate relevance
ECONOVA-S™ — finance / economics / market context
      ↓
Agent Arena™ / Critic / Defender / Falsifier / Replicator
      ↓
Professional Judgment Passport™
      ↓
Human Approval Gate™
```

## Dynamic scenario phases

### Phase 0 — Evidence freeze / independent baseline

Freeze the synthetic case package and any public-evidence references/Evidence Passports used in the run. The student records an independent judgment before AI exposure.

### Phase 1 — Financial reporting pressure

Management proposes accounting treatments/estimates under performance pressure. The learner evaluates evidence and IFRS implications.

### Phase 2 — Internal-control weakness

New evidence reveals control design or operating-effectiveness concerns. Audit scope, risk assessment and evidence requirements can change.

### Phase 3 — Macro / market / context update

Where relevant, the simulation introduces versioned macro, market or ESG context from the Data & Evidence Mesh. Examples include a rate change, economic slowdown, factor-market stress or material climate/energy condition. Context affects the synthetic scenario only through explicit rules; correlation/context is not automatically causality.

### Phase 4 — AI-agent intervention

Specialist agents issue evidence-linked recommendations. The student may accept, modify, reject, request more evidence or escalate.

### Phase 5 — CAM/KAM decision

The student evaluates whether matters required significant auditor attention and whether the rationale is entity-specific, evidence-grounded and professionally defensible.

### Phase 6 — PCAOB-style challenge

A public-standards inspection simulation challenges risk assessment, evidence sufficiency, documentation, supervision and CAM reasoning. No confidential PCAOB data is used or implied.

### Phase 7 — Decision–Consequence transition

The learner's prior choices change the next Digital Twin state. Examples:

- requesting more evidence may reduce evidence uncertainty but increase time/cost;
- accepting a weak estimate may increase synthetic misstatement and inspection risk;
- escalating a control deficiency may increase remediation effort but reduce residual control risk;
- designating a CAM may improve transparency while increasing documentation/review requirements;
- overriding an unsupported AI recommendation may improve evidence integrity if the override is well justified;
- ignoring contradictory macro/market evidence may reduce the quality of the student's risk rationale when that evidence is material.

These are **pedagogical state-transition rules**, not causal estimates of real-world effects unless a specific transition is explicitly calibrated and documented.

### Phase 8 — Verification / adversarial evaluation

VERA™ and the Agent Arena™ inspect source provenance, unsupported inferences, cross-source contradictions, versions/vintages, Decision DAG dependencies and whether agent claims exceed the evidence.

### Phase 9 — Student defense

The student must defend the final judgment using:

- Evidence Passport™;
- Professional Decision DAG™;
- standards references;
- contradictory evidence;
- agent disagreements;
- consequence ledger;
- Professional Judgment Passport™.

### Phase 10 — Human Approval Gate™

Instructor/reviewer selects APPROVE / MODIFY / REJECT / REQUEST_MORE_EVIDENCE / ESCALATE and records rationale.

## Professional Judgment Passport™ dimensions

| Code | Dimension | Example evidence |
|---|---|---|
| EQ | Evidence Quality | source reliability, relevance, provenance, contradictory evidence |
| PS | Professional Skepticism | challenge of management/agent claims |
| RI | Risk Identification | linked business/reporting/audit risks |
| AJ | Accounting Judgment | IFRS-grounded reasoning |
| AUJ | Audit Judgment | assertions, procedures, sufficiency, escalation |
| CKR | CAM/KAM Reasoning | significant attention, specificity, evidence linkage |
| AIV | AI Verification | unsupported output/hallucination/model-limit checks |
| ETH | Ethics & Public Interest | independence, integrity, stakeholder effects |
| HOR | Human Override Quality | quality of accept/modify/reject/escalate rationale |

Schema: [`../../architecture/professional_judgment_passport.schema.json`](../../architecture/professional_judgment_passport.schema.json)

## Decision–Consequence Engine™ state vector

A minimal prototype state may track:

```text
company.performance_pressure
accounting.misstatement_risk
accounting.estimate_uncertainty
controls.deficiency_severity
audit.audit_risk
audit.evidence_gap
audit.cam_candidate
market.investor_confidence
market.volatility
macro.financial_conditions
regulatory.scrutiny
esg.reporting_credibility
education.time_cost
```

Each student decision creates a **consequence ledger entry** containing previous state, decision, applied rule, new state, rationale and whether the effect is synthetic or empirically calibrated.

## Evaluation design

The prototype should compare, when execution is available:

1. HUMAN_ONLY;
2. AI_ASSISTANT;
3. SINGLE_AGENT;
4. SEQUENTIAL_AGENTS;
5. GOVERNED_MULTI_AGENT.

Primary educational/professional measures can include RPA, AA, EG, PS, DS, DIST, AIV, CER, HOR, ESC plus Professional Judgment Passport™ dimensions.

Provider/model names or connector names alone do not count as execution. A provider-backed or live-data condition requires run metadata, model/version or connector/version, inputs/outputs, evidence-access boundary and Evidence Passport™.

## Research support

The simulation inherits the NAAIL Simulation Evidence Standard™. Each material case records directly relevant FT50/AJG 4*/4 research where available, applicable authoritative standards, professional competency mappings, data provenance, limitations, and an explicit evidence gap where top-journal research is not directly transferable.

OpenAlex metadata may help discover research, but metadata/citation counts never prove a scientific claim.

## Technology Core candidates

Potential optional adapters include Mesa, AgentTorch, SimPy, OpenAI Agents SDK, Microsoft Agent Framework, HARK, ABIDES, FinRL, RD-Agent and optional OpenBB provider connectors. They are replaceable implementation tools, not professional authorities.

Simulation registry: [`../../architecture/business_school_simulation_technology_registry.json`](../../architecture/business_school_simulation_technology_registry.json)

## Relationship to existing NAAIL checkpoints

This dynamic prototype can reuse evidence patterns and evaluation logic from the existing validated synthetic Prototype 003, but it adds two requirements:

1. student decisions must alter subsequent scenario conditions through explicit consequence rules; and
2. public-data context must be bound through versioned Evidence Passports rather than untracked copy/paste.

Therefore:

```text
Prototype_003_validated_checkpoint = preserved
Audit_Accounting_Digital_Twin_dynamic_design = adopted
Data_Evidence_Mesh_binding = adopted
Decision_Consequence_Engine_code_published = true
live_connector_execution_validated = false
provider_backed_dynamic_execution_validated = false
human_gate_required = true
```

## Independence and safeguards

- Client XYZ and Firm Alpha are synthetic.
- No Big Four equivalence or partnership is implied.
- No confidential PCAOB inspection information is used.
- Protected IFRS text is not republished without rights.
- Public/free access does not imply unrestricted redistribution.
- OpenSanctions matches are research signals, not legal determinations.
- Optional OpenBB access does not replace original-provider provenance/terms.
- Student scores are educational/research constructs, not automated hiring scores.
- Human approval remains mandatory.
