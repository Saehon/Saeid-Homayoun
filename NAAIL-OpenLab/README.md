# NAAIL OpenLab™

**Next-Generation Accounting, Audit & Assurance Intelligence Lab**  
*A Global Evidence-Governed Multi-Agent Digital Twin Platform for Accounting, Audit, Finance, Sustainability and Scientific Discovery*

## V2026.3 Multi-Agent Digital Twin

[![Version](https://img.shields.io/badge/version-0.2.3-blue)](./VERSION)
[![Use](https://img.shields.io/badge/use-research%20%26%20education-green)](./LICENSE.md)
[![Commercial](https://img.shields.io/badge/commercial%20use-not%20licensed-red)](./COMMERCIAL_USE.md)
[![ORCID](https://img.shields.io/badge/ORCID-0000--0002--2536--0446-brightgreen)](https://orcid.org/0000-0002-2536-0446)

**Principal Investigator:** Dr. Saeid Homayoun  
**ORCID:** https://orcid.org/0000-0002-2536-0446

> **NAAIL OpenLab™ is an Evidence-Governed Multi-Agent Business School Digital Twin for Education, Research, Professional Simulation, and Verifiable Human–AI Judgment.**

NAAIL is not positioned as a generic AI tutor or chatbot. It connects **research, authoritative standards, professional competencies, real/public/licensed evidence, Digital Twins, AI agents, reproducibility, sustainability, and accountable human judgment**.

## Start in one minute

1. **[Start Here](./00_START_HERE.md)** — reviewer path and current maturity boundary.
2. **[Data & Evidence Mesh™](./DATA_EVIDENCE_MESH.md)** — SEC/XBRL, FRED/ALFRED, Fama–French, World Bank, OWID, OpenAlex, OpenSanctions and optional OpenBB connectors with Evidence Passport™ governance.
3. **[Business School Simulation & Digital Twin Layer](./BUSINESS_SCHOOL_SIMULATION_DIGITAL_TWIN_LAYER.md)** — dynamic company, audit, regulator, market, accounting, finance, economics, sustainability and governance simulations.
4. **[Global AI Business Education Platform](./GLOBAL_AI_BUSINESS_EDUCATION_PLATFORM.md)** — FT50/AJG research + standards + professional competencies + experiential learning.
5. **[Simulation Evidence Standard](./docs/education/SIMULATION_EVIDENCE_STANDARD.md)** — mandatory Research Evidence Card™ governance.
6. **[Current Project State](./CURRENT_PROJECT_STATE.md)** — what is executed, gated, architecture-only, registry-only or research-prototype status.
7. **[Platform Capability & Maturity Matrix](./architecture/PLATFORM_CAPABILITY_MATRIX.md)** — machine-readable maturity discipline.

---

## Fixed architecture: exactly two permanent cores

**NAAIL OpenLab™ — V2026.3 Multi-Agent Digital Twin** preserves exactly two permanent cores:

1. **Knowledge Core™** — governed standards, research evidence, professional knowledge, ontologies, evidence semantics, jurisdiction packs and authoritative-source mappings.
2. **Technology Core™** — replaceable models, agent frameworks, simulation engines, retrieval infrastructure, tools, sandboxes, orchestration and adapters.

No Business School, Digital Twin, data/evidence mesh, agent, simulation or scientific-discovery capability becomes a third permanent core.

```text
NAAIL OpenLab™ — V2026.3 Multi-Agent Digital Twin
│
├── PERMANENT CORE 1 — Knowledge Core™
├── PERMANENT CORE 2 — Technology Core™
│
├── NAAIL Data & Evidence Mesh™
├── Scientific Discovery & Governance Layer
├── Professional Agent Layer
│   ├── KIWI™
│   ├── POMELO™
│   ├── VERA™
│   ├── IFRS Intelligence Agent™
│   ├── PCAOB Intelligence Agent™
│   ├── ESG Intelligence
│   └── ECONOVA-S™
│
├── Business School Simulation & Digital Twin Layer
├── Decision–Consequence Engine™
├── Professional Judgment Passport™
└── Human Approval Gate™
```

Canonical hierarchy: **[architecture/MASTER_PLATFORM_HIERARCHY.md](./architecture/MASTER_PLATFORM_HIERARCHY.md)**

---

## NAAIL Data & Evidence Mesh™

The Mesh is a **governed supporting layer**, not a third core. It connects real/public/rights-cleared evidence to professional agents and Digital Twins through APIs/connectors, source/version metadata, license/rights controls, hashes/checksums where feasible, reproducible transformations and **Evidence Passport™** records.

Priority source families:

- **SEC EDGAR / XBRL** — filings, submissions and Company Facts evidence;
- **FRED / ALFRED** — macro/financial series with vintage/realtime context;
- **Fama–French** — factor and portfolio research data;
- **World Bank** — macro/development/context indicators;
- **Our World in Data CO₂ / Energy** — climate, emissions and energy context with source-level attribution;
- **OpenAlex** — scholarly metadata, citation/topic graphs and evidence-gap discovery;
- **OpenSanctions** — optional non-commercial/academic sanctions/PEP/entity-risk research;
- **OpenBB** — optional Technology-Core provider abstraction while preserving original-provider terms and provenance.

Large third-party datasets are **not** committed to GitHub by default. NAAIL stores source/connector manifests, IDs, query parameters, versions/vintages, retrieval timestamps, rights metadata, hashes and small rights-cleared/synthetic fixtures instead.

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

- [Data & Evidence Mesh specification](./DATA_EVIDENCE_MESH.md)
- [Machine-readable Mesh registry](./architecture/data_evidence_mesh_registry.json)
- [Broader Free Data Fabric](./FREE_DATA_FABRIC.md)

---

## Professional agent families

| Agent | Role |
|---|---|
| **KIWI™** | Audit / CAM / KAM intelligence and evidence-grounded audit judgment |
| **POMELO™** | Accounting, assurance, forensic/professional intelligence and governed reasoning |
| **VERA™** | Verifiable accounting/auditing intelligence, Evidence Passport, Decision DAG, evaluation and Human Gate |
| **IFRS Intelligence Agent™** | IFRS reporting, recognition/measurement, disclosure and accounting-judgment Digital Twins |
| **PCAOB Intelligence Agent™** | Public audit-standard, inspection, deficiency and remediation Digital Twins |
| **ESG Intelligence** | ESRS/CSRD, ISSB/SASB, GRI, climate, carbon, SDGs and sustainability assurance |
| **ECONOVA-S™** | Finance, economics, asset pricing, market intelligence and data-economy research |

Canonical agent index: **[agents/README.md](./agents/README.md)**

---

## Business School Simulation & Digital Twin Layer

The supporting simulation layer covers:

- **Company Digital Twin** — transactions, estimates, disclosures, incentives, controls and operations;
- **Audit Firm Digital Twin** — planning, risk, evidence, review, CAM/KAM and quality/inspection challenge;
- **Regulator Digital Twin** — public-rule and public-evidence supervisory scenarios;
- **Capital-Market Digital Twin** — valuation, disclosure, investor response, portfolio/risk and market experiments;
- **Sustainability Digital Twin** — climate, carbon, materiality, sustainability reporting and assurance;
- **Accounting Digital Twin** — IFRS-grounded recognition, measurement, estimates and disclosures;
- **Finance Digital Twin** — valuation, financing, investment, credit and risk;
- **Economics Digital Twin** — heterogeneous-agent and policy/data-economy experiments;
- **Governance / Board Digital Twin** — oversight, incentives, audit committee, risk and stakeholder trade-offs.

### Canonical simulation loop

```text
Research-backed learning objective
→ Real / governed evidence
→ Evidence Passport™
→ Digital Twin state t
→ Student + Professional Agents
→ Professional Decision DAG™
→ Decision–Consequence Engine™
→ Digital Twin state t+1
→ Agent Arena™ / Critic / Defender / Falsifier
→ Blind Gold / Evaluation
→ Reproducibility + Falsification
→ Professional Judgment Passport™
→ Human Approval Gate™
```

---

## Decision–Consequence Engine™

Professional decisions can change later synthetic simulation states across:

**business performance · accounting risk · ICFR/control state · audit evidence/scope · CAM/KAM · regulator attention · market confidence · financing/liquidity · ESG/climate credibility · governance outcomes**.

The public reference engine is deterministic and pedagogical. **Synthetic transition rules are not claimed to be real-world causal estimates.**

- [Decision–Consequence Engine](./simulations/business-school/decision_consequence_engine.py)
- [Engine integrity tests](./tests/test_decision_consequence_engine.py)

---

## Professional Judgment Passport™

The Passport records education/research evidence across nine judgment dimensions:

**Evidence Quality · Professional Skepticism · Risk Identification · Accounting Judgment · Audit Judgment · CAM/KAM Reasoning · AI Verification · Ethics/Public Interest · Human Override Quality**.

It is an **educational/research construct**, not an automated hiring score or external professional certification.

- [Machine-readable Passport schema](./architecture/professional_judgment_passport.schema.json)

---

## First dynamic prototype — NAAIL Audit & Accounting Digital Twin™

The first dynamic Business School prototype combines:

- realistic synthetic company evidence plus reproducibly referenced **SEC/XBRL** patterns/context;
- versioned **macro evidence from FRED/ALFRED** where material;
- **market/factor context from Fama–French** where relevant;
- World Bank / OWID sustainability or country context when material;
- IFRS accounting issues;
- internal-control weaknesses;
- management pressure and incentives;
- audit-risk and evidence decisions;
- CAM/KAM reasoning;
- PCAOB-style public-standards challenge;
- KIWI™, POMELO™, VERA™, IFRS/PCAOB/ESG/ECONOVA-S™ interaction;
- Decision–Consequence Engine™ state changes;
- student/researcher defense of professional judgment;
- Professional Judgment Passport™;
- mandatory Human Approval Gate™.

Read: **[digital-twins/audit-accounting/README.md](./digital-twins/audit-accounting/README.md)**

This prototype is distinct from the validated public executable checkpoint described below; live connector/provider execution requires actual run provenance and Evidence Passports.

---

## Current validated executable checkpoint

The current validated public execution checkpoint remains:

**NAAIL OpenLab v0.2.3 · Audit Workspace V0.4 · Prototype 003**

Prototype 003 contains a frozen three-domain synthetic Audit Digital Twin benchmark covering:

| Case | Deterministic finding | Synthetic amount | Human Gate |
|---|---|---:|---|
| Revenue Recognition & Cut-off | `TX-002`, `TX-003` | EUR 190,000 proposed adjustment | `PENDING_HUMAN_APPROVAL` |
| Goodwill Impairment | `GW-DR`, `GW-MAR` | EUR 440,000 estimated adjustment | `PENDING_HUMAN_APPROVAL` |
| ICFR Deficiency | `CTRL-JE-02`, `CTRL-IT-03` | EUR 530,000 estimated exposure | `PENDING_HUMAN_APPROVAL` |

For these deliberately constructed frozen synthetic cases, the deterministic condition produces precision/recall of **1.00 / 1.00**. These are benchmark properties only and **not claims of real-world audit effectiveness**.

- [Prototype 003 public runtime](./Prototype_003/runtime/README.md)
- [Prototype status](./PROTOTYPE_STATUS_V0.4.md)

Provider/model/live-connector conditions remain non-executed unless a real run artifact and Evidence Passport prove otherwise.

---

## Research-backed, standards-grounded, profession-aligned education

Every material simulation promoted as **Research-Backed™**, **Standards-Grounded™** or **Profession-Aligned™** must record:

1. learning objective;
2. directly relevant FT50/AJG evidence or explicit evidence gap;
3. authoritative standard/regulation;
4. professional-body competency mapping;
5. data provenance, version/vintage and rights status;
6. frozen Digital Twin/version;
7. actual AI/connector execution status;
8. assessment criteria;
9. **People × Planet × Society × Sustainable Profit™** reflection where material;
10. **Human Gate™** responsibility.

The architecture may align to public education-quality and competency frameworks from bodies such as AACSB, EFMD/EQUIS, AMBA, IFRS Foundation/IASB/ISSB, PCAOB, IAASB, IFAC/IESBA, EFRAG/ESRS, GRI, AICPA/CPA, CIMA/CGMA, ACCA, IMA/CMA/SMA, IIA/CIA/CRMA, ACFE/CFE, CFA Institute/CFA, ISACA/CISA and GARP/FRM.

**Alignment never implies accreditation, certification, endorsement or partnership.**

- [Global AI Business Education Platform](./GLOBAL_AI_BUSINESS_EDUCATION_PLATFORM.md)
- [Simulation Evidence Standard](./docs/education/SIMULATION_EVIDENCE_STANDARD.md)
- [Research Evidence Card schema](./architecture/simulation_evidence_card.schema.json)

---

## Scientific discovery

Publication-grade NAAIL research inherits the common scientific contract:

```text
Question
→ Literature Validation
→ Competing Hypotheses / Co-Scientist Arena
→ DAG / Identification Governance
→ ERA-style Empirical Design
→ Rights-Cleared Data or Digital Twin
→ Computational Discovery / evaluator-guided search
→ Robustness / Placebo / OOS
→ Critic / Defender / Falsifier
→ Independent Replication
→ Chain-of-Evidence + CoE Audit
→ Evidence Passport™
→ Human Gate™
```

No agent consensus, p-value, benchmark score, provider name, connector name or model output is automatically treated as scientific truth.

- [Scientific Discovery Contract](./SCIENTIFIC_DISCOVERY_CONTRACT.md)
- [Scientific Discovery Start Here](./00_SCIENTIFIC_DISCOVERY_START_HERE.md)
- [FT50/AJG Replication Arena](./benchmarks/ft50_abs4/README.md)

---

## Open-source and public-data integration

External tools are admitted only as governed **Technology Core adapters**, data/evidence sources or research references. They do not become authoritative professional knowledge.

Current integration families include:

- [Data & Evidence Mesh™](./DATA_EVIDENCE_MESH.md)
- [Free Data Fabric™](./FREE_DATA_FABRIC.md)
- [ERP Digital Twin Lab™](./ERP_DIGITAL_TWIN_LAB.md)
- [Audit Analytics Open-Source Pack™](./AUDIT_ANALYTICS_OPEN_SOURCE_PACK.md)
- [Finance Market Intelligence Lab™](./FINANCE_MARKET_INTELLIGENCE_LAB.md)
- [ESG & Sustainability Intelligence Lab™](./ESG_SUSTAINABILITY_INTELLIGENCE_LAB.md)
- [Accounting & Audit Open-Source Pack™](./OPEN_SOURCE_ACCOUNTING_AUDIT_PACK.md)
- [Adversarial Intelligence Fabric™](./ADVERSARIAL_INTELLIGENCE_FABRIC.md)

The Business School Technology Core registry includes governed references for **Mesa, AgentTorch, SimPy, OpenAI Agents SDK, Microsoft Agent Framework, HARK, ABIDES, FinRL and RD-Agent** where they add measurable value. OpenBB provider extensions may be evaluated as optional data connectors while preserving original-provider identity and rights.

- [Technology Core simulation registry](./architecture/business_school_simulation_technology_registry.json)
- [Data & Evidence Mesh registry](./architecture/data_evidence_mesh_registry.json)
- [Open-Source Integration Hub](./OPEN_SOURCE_INTEGRATION_HUB.md)

---

## Permanent invariants

```text
permanent_core_count = 2
knowledge_core_is_permanent = true
technology_core_is_permanent = true
data_evidence_mesh_is_core = false
business_school_simulation_layer_is_core = false
decision_consequence_engine_is_core = false
professional_judgment_passport_is_core = false
large_third_party_dataset_should_be_committed_to_github = false
connector_name_implies_execution = false
technology_core_may_rewrite_knowledge_core = false
external_repo_is_authoritative_truth = false
external_framework_is_authoritative_professional_truth = false
architecture_documented_equals_runtime_executed = false
provider_name_equals_provider_run = false
synthetic_consequence_rule_is_real_world_causal_effect = false
agent_consensus_is_scientific_truth = false
simulation_may_invent_ft50_ajg_support = false
professional_body_alignment_equals_certification = false
student_score_equals_employability_truth = false
optimize_for_p_value = false
human_gate_required = true
```

---

## Public / private boundary

**Public:** research-safe architecture, synthetic benchmarks, education assets, selected reproducibility code, connector/source registries, evidence/governance schemas, maturity maps and citation metadata.

**Private/IP-sensitive:** provider/API credentials, restricted/licensed datasets, unpublished prompts/agent specifications, patent-sensitive orchestration, partner-confidential material and unreleased experimental results.

Third-party software, standards, papers, models, datasets and professional frameworks retain their original ownership and terms.

---

## Canonical navigation

- [Start Here](./00_START_HERE.md)
- [Master Platform Hierarchy](./architecture/MASTER_PLATFORM_HIERARCHY.md)
- [Data & Evidence Mesh](./DATA_EVIDENCE_MESH.md)
- [Business School Simulation & Digital Twin Layer](./BUSINESS_SCHOOL_SIMULATION_DIGITAL_TWIN_LAYER.md)
- [Global AI Business Education Platform](./GLOBAL_AI_BUSINESS_EDUCATION_PLATFORM.md)
- [Current Project State](./CURRENT_PROJECT_STATE.md)
- [Platform Capability Matrix](./architecture/PLATFORM_CAPABILITY_MATRIX.md)
- [Specialist Agent Families](./agents/README.md)
- [Open-Source Integration Hub](./OPEN_SOURCE_INTEGRATION_HUB.md)
- [Scientific Discovery Start Here](./00_SCIENTIFIC_DISCOVERY_START_HERE.md)
- [September 2026 Upgrade Summary](./UPGRADE_2026_09_16.md)

---

## Citation

> **Homayoun, S. (2026).** *NAAIL OpenLab: An Evidence-Governed AI Platform for Business-School Education, Audit Digital Twins, and Reproducible Scientific Discovery* (Version 0.2.3) [Computer software]. GitHub. https://github.com/Saehon/Saeid-Homayoun/tree/main/NAAIL-OpenLab

- [CITATION.cff](./CITATION.cff)
- [CITATION.bib](./CITATION.bib)
- [codemeta.json](./codemeta.json)

---

## Independence

NAAIL OpenLab™ is independent. References to universities, technology providers, Big Four firms, standard setters, regulators, professional bodies, journals, datasets or open-source projects identify public evidence, standards, competencies, methodological inspiration, upstream software or comparison contexts only. They do not imply affiliation, endorsement, sponsorship, accreditation, certification or partnership unless separately documented in writing.

> **Models generate. Agents debate. Real evidence enters through provenance. Research grounds. Standards govern. Professional bodies define competence. Decisions change the Digital Twin. Code tests. VERA verifies. Humans approve. Society benefits.**
