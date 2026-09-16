# NAAIL Simulation Evidence Standard™

**Applies to:** material public NAAIL education/professional simulations  
**Parent:** [Global AI Business Education & Professional Simulation Platform](../../GLOBAL_AI_BUSINESS_EDUCATION_PLATFORM.md)  
**Machine-readable schema:** [`../../architecture/simulation_evidence_card.schema.json`](../../architecture/simulation_evidence_card.schema.json)

## Purpose

The standard prevents NAAIL Digital Twin exercises from becoming unsupported AI demos. A simulation must show what it teaches, what research supports it, which authoritative requirements apply, which professional competencies it develops, what evidence it uses, what AI actually ran, how learning is evaluated, and who remains responsible for the final decision.

## Evidence classes

A simulation carries one of four research-grounding states:

- `FT50_AJG4_RESEARCH_BACKED` — directly relevant FT50 and/or AJG 4*/4 research is recorded and verified.
- `PEER_REVIEWED_EVIDENCE_BACKED` — strong directly relevant peer-reviewed evidence exists, but the top-journal threshold is not met.
- `STANDARDS_PROFESSIONAL_BACKED` — the exercise is primarily standards/competency based and top-journal research is not material to the learning objective.
- `EVIDENCE_GAP_DECLARED` — the simulation is retained for learning/research exploration, but the evidence gap is explicitly disclosed.

A journal label alone never upgrades the simulation; the actual paper must be relevant to the simulated claim/task.

## Required Research Evidence Card™ fields

### 1. Identity

- simulation ID;
- title;
- version;
- domain;
- target learner;
- course/module;
- status.

### 2. Learning contract

- learning outcomes;
- prerequisite knowledge;
- professional judgment expected;
- institutional/AACSB-alignment note where applicable.

### 3. Research grounding

For every research anchor:

- paper title;
- authors/year;
- journal;
- FT50 status where verified;
- AJG rating/year where verified;
- DOI or authoritative publisher URL;
- research design type;
- population/context/period;
- simulation construct/mechanism supported;
- limitations on transfer to the simulated setting.

If no suitable research anchor exists, record `EVIDENCE_GAP_DECLARED` and explain why.

### 4. Standards / regulation grounding

- jurisdiction;
- organization/standard setter/regulator;
- standard/rule identifier;
- effective/version period;
- official source URL;
- authority class;
- copyright/redistribution note.

Examples include IFRS Foundation/IASB, ISSB, EFRAG/ESRS/EU, PCAOB, IAASB, IESBA, SEC, GRI/GSSB, The IIA, and jurisdiction-specific authorities.

### 5. Professional competency mapping

Record only public competency alignment. NAAIL does not claim certification equivalence.

Potential mappings include:

- AICPA / CPA;
- CIMA / CGMA;
- ACCA;
- IMA / CMA / SMA;
- IIA / CIA / CRMA;
- ACFE / CFE;
- CFA Institute / CFA;
- ISACA / CISA;
- GARP / FRM;
- other relevant professional bodies.

### 6. Evidence/Data Passport

- source name/provider;
- source URL or repository path;
- period/version;
- public/licensed/synthetic classification;
- raw/derived status;
- rights/license status;
- hash where feasible;
- transformation chain;
- leakage/contamination check;
- authoritative-source status.

### 7. Digital Twin contract

- Digital Twin ID;
- repository path;
- fictional/real/public-evidence basis;
- frozen case/version;
- evidence boundary;
- gold-label visibility rule where applicable.

### 8. AI execution condition

Allowed conditions include:

- `HUMAN_ONLY`;
- `AI_ASSISTANT`;
- `SINGLE_AGENT`;
- `SEQUENTIAL_AGENTS`;
- `GOVERNED_MULTI_AGENT`.

For an executed AI condition record:

- provider/model;
- model/version identifier;
- run timestamp or artifact reference;
- tool permissions;
- evidence access;
- prompts/configuration provenance as permitted;
- actual execution status.

Naming a provider/system without a real run is `NOT_EXECUTED` or `NOT_EXECUTED_PROVIDER_REQUIRED`.

### 9. Assessment

Select domain-relevant measures such as:

- RPA — Risk–Procedure Alignment;
- AA — Assertion Alignment;
- EG — Evidence Grounding;
- PS — Professional Skepticism;
- DS — Documentation Sufficiency;
- DIST — Decision Integrity/Stability;
- AIV — AI Verification;
- CER — Contradictory Evidence Recognition;
- HOR — Human Override Reasoning;
- ESC — Escalation Judgment;
- standards application;
- ethics;
- communication;
- calibration;
- reproducibility;
- decision quality;
- learning retention.

Proposed educational constructs require validity evidence before high-stakes use.

### 10. Sustainability / value reflection

For major business cases, record material consequences across:

- `people`;
- `planet`;
- `society`;
- `sustainable_profit`.

A dimension may be `NOT_MATERIAL` only with a short rationale.

### 11. Human Gate™

Record:

- responsible reviewer role;
- allowed decisions: approve / modify / reject / request_more_evidence / escalate;
- decision status;
- rationale/evidence reference.

No model or agent can self-approve a consequential professional conclusion.

## Accreditation / professional-body boundary

NAAIL may map simulations to AACSB-related educational outcomes and to public professional competency frameworks. It must not state that a simulation is AACSB-accredited, EQUIS-accredited, AMBA-accredited, CPA-approved, ACCA-approved, CIMA-approved, CMA-approved, CIA-approved, CFE-approved, CFA-approved, or otherwise certified unless a formal written relationship explicitly establishes that status.

## Copyright boundary

Official standards should be linked and versioned; protected full standard text is not reproduced merely to make a simulation self-contained. NAAIL records citations, identifiers, mappings and rights status while preserving source ownership.

## Invariants

```text
simulation_without_learning_objective = prohibited
simulation_without_data_provenance = prohibited
simulation_without_human_gate = prohibited
simulation_may_invent_ft50_ajg_support = false
journal_rank_is_truth = false
professional_body_alignment_equals_certification = false
standard_setter_reference_equals_endorsement = false
external_system_name_implies_execution = false
student_score_equals_employability_truth = false
research_overrides_authoritative_standard = false
```

## Promotion rule

A draft exercise may exist without a complete card. It may not be promoted as **NAAIL Research-Backed™ / Standards-Grounded™ / Profession-Aligned™** until the applicable card fields pass review.
