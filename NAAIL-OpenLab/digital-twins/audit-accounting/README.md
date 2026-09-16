# NAAIL Audit & Accounting Digital Twin™ — Prototype 001

**Parent architecture:** NAAIL OpenLab™ — V2026.3 Multi-Agent Digital Twin  
**Layer:** Business School Simulation & Digital Twin Layer  
**Status:** Research/education prototype specification; dynamic consequence engine published separately; not yet a validated provider-backed execution claim.

## Objective

Create a realistic, evidence-governed business-school simulation in which accounting and audit judgments evolve over time. The learner must analyze company evidence, apply IFRS reasoning, identify internal-control weaknesses, respond to management pressure, evaluate CAM/KAM issues, challenge AI agents, withstand a PCAOB-style public-standards review, and defend the final professional judgment before a Human Approval Gate™.

## Canonical scenario

**Client:** Client XYZ — synthetic public-company-style reporting entity.  
**Audit firm:** Firm Alpha — fictional audit firm.  
**Period:** multi-stage year-end reporting/audit cycle.  
**Evidence:** synthetic evidence plus rights-cleared/public source patterns where appropriate.  
**Gold labels:** withheld from students/agents where Blind Gold evaluation is used.

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
- AI-agent recommendations with explicit evidence references.

## Professional agents

```text
Student / Learner
      ↓
POMELO™ — accounting / assurance reasoning
KIWI™ — CAM/KAM / audit evidence
VERA™ — verification / evidence challenge
IFRS Agent™ — accounting standards judgment
PCAOB Agent™ — public-regulatory challenge
ESG Agent — sustainability / climate relevance
ECONOVA-S™ — finance / economics / market context when relevant
      ↓
Critic / Defender / Falsifier / Replicator
      ↓
Human Approval Gate™
```

## Dynamic scenario phases

### Phase 0 — Independent baseline

Student receives the initial frozen evidence package and records an independent judgment before AI exposure.

### Phase 1 — Financial reporting pressure

Management proposes accounting treatments/estimates under performance pressure. The learner evaluates evidence and IFRS implications.

### Phase 2 — Internal-control weakness

New evidence reveals control design or operating-effectiveness concerns. Audit scope, risk assessment and evidence requirements can change.

### Phase 3 — AI-agent intervention

Specialist agents issue evidence-linked recommendations. The student may accept, modify, reject, request more evidence or escalate.

### Phase 4 — CAM/KAM decision

The student evaluates whether matters required significant auditor attention and whether the rationale is entity-specific, evidence-grounded and professionally defensible.

### Phase 5 — PCAOB-style challenge

A public-standards inspection simulation challenges risk assessment, evidence sufficiency, documentation, supervision and CAM reasoning. No confidential PCAOB data is used or implied.

### Phase 6 — Decision–Consequence transition

The learner's prior choices change the next Digital Twin state. Examples:

- requesting more evidence may reduce evidence uncertainty but increase time/cost;
- accepting a weak estimate may increase synthetic misstatement and inspection risk;
- escalating a control deficiency may increase remediation effort but reduce residual control risk;
- designating a CAM may improve transparency while increasing documentation/review requirements;
- overriding an unsupported AI recommendation may improve evidence integrity if the override is well justified.

These are **pedagogical state-transition rules**, not causal estimates of real-world effects.

### Phase 7 — Student defense

The student must defend the final judgment using:

- Evidence Passport™;
- Professional Decision DAG™;
- standards references;
- contradictory evidence;
- agent disagreements;
- consequence ledger;
- Professional Judgment Passport™.

### Phase 8 — Human Approval Gate™

Instructor/reviewer selects APPROVE / MODIFY / REJECT / REQUEST_MORE_EVIDENCE / ESCALATE and records rationale.

## Professional Judgment Passport™ dimensions

| Code | Dimension | Example evidence |
|---|---|---|
| EQ | Evidence Quality | source reliability, relevance, contradictory evidence |
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

Provider/model names alone do not count as execution. A provider-backed condition requires run metadata, model/version, inputs/outputs, evidence-access boundary and Evidence Passport™.

## Research support

The simulation should inherit the NAAIL Simulation Evidence Standard™. Each material case records directly relevant FT50/AJG 4*/4 research where available, applicable authoritative standards, professional competency mappings, data provenance, limitations, and an explicit evidence gap where top-journal research is not directly transferable.

## Technology Core candidates

Potential optional adapters include Mesa, AgentTorch, SimPy, OpenAI Agents SDK, Microsoft Agent Framework, HARK, ABIDES, FinRL and RD-Agent. They are replaceable implementation tools, not professional authorities.

Registry: [`../../architecture/business_school_simulation_technology_registry.json`](../../architecture/business_school_simulation_technology_registry.json)

## Relationship to existing NAAIL checkpoints

This dynamic prototype can reuse evidence patterns and evaluation logic from the existing validated synthetic Prototype 003, but it adds a new requirement: **student decisions must alter subsequent scenario conditions through explicit consequence rules**.

Therefore:

```text
Prototype_003_validated_checkpoint = preserved
Audit_Accounting_Digital_Twin_dynamic_design = adopted
Decision_Consequence_Engine_code_published = true
provider_backed_dynamic_execution_validated = false
human_gate_required = true
```

## Independence and safeguards

- Client XYZ and Firm Alpha are synthetic.
- No Big Four equivalence or partnership is implied.
- No confidential PCAOB inspection information is used.
- Protected IFRS text is not republished without rights.
- Student scores are educational/research constructs, not automated hiring scores.
- Human approval remains mandatory.
