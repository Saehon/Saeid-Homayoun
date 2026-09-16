# NAAIL OpenLab™ — Platform Capability & Maturity Matrix

> **PATENT RIGHTS RESERVED — PATENT APPLICATION PREPARATION IN PROGRESS**

## Constitutional status

**NAAIL OpenLab™ — V2026.3 Multi-Agent Digital Twin** is governed by the **[Two-Core Constitution](../TWO_CORE_CONSTITUTION.md)**.

Exactly two permanent cores exist: **Stable Knowledge Core™** and **Replaceable Technology Core™**. No third permanent core is permitted.

## Status vocabulary

| Status | Meaning |
|---|---|
| `EXECUTED_VALIDATED` | Reproducible execution evidence exists for the stated validated scope. |
| `IMPLEMENTED_EXECUTION_GATED` | Infrastructure exists, but required execution evidence is not yet established. |
| `ARCHITECTURE_ADOPTED` | High-level public design/governance is adopted. |
| `REGISTRY_ADOPTED` | Third-party tools/data are catalogued; registration is not execution. |
| `RESEARCH_PROTOTYPE` | A bounded research prototype exists with executed elements but without independent validation. |
| `PUBLIC_EDUCATION_DESIGN` | Public teaching/research design, not production deployment. |
| `PATENT_HOLD_NON_ENABLING` | Name/high-level role public; enabling implementation withheld pending filing review. |

## Capability matrix

| Capability | Public asset | Status | Core? |
|---|---|---|---|
| **Two-Core Constitution** | [`../TWO_CORE_CONSTITUTION.md`](../TWO_CORE_CONSTITUTION.md) | `ARCHITECTURE_ADOPTED` | constitutional rule |
| Stable Knowledge Core™ | [`MASTER_PLATFORM_HIERARCHY.md`](./MASTER_PLATFORM_HIERARCHY.md) | `ARCHITECTURE_ADOPTED` | **YES** |
| Replaceable Technology Core™ | [`MASTER_PLATFORM_HIERARCHY.md`](./MASTER_PLATFORM_HIERARCHY.md) | `ARCHITECTURE_ADOPTED` | **YES** |
| **Microsoft Golden Anchor POC V1** | [`../prototypes/microsoft-poc-v1/MICROSOFT_POC_V1.md`](../prototypes/microsoft-poc-v1/MICROSOFT_POC_V1.md) | **`RESEARCH_PROTOTYPE`** | NO |
| NAAIL Data & Evidence Mesh™ | [`../DATA_EVIDENCE_MESH.md`](../DATA_EVIDENCE_MESH.md) | `PATENT_HOLD_NON_ENABLING` | NO |
| FT50 / AJG Evidence Graph™ | [`../TWO_CORE_CONSTITUTION.md`](../TWO_CORE_CONSTITUTION.md) | `ARCHITECTURE_ADOPTED` | NO |
| Nobel Theory-to-Evidence & AI Experiment Engine™ | [`../NOBEL_THEORY_TO_EVIDENCE_AI_EXPERIMENT_ENGINE.md`](../NOBEL_THEORY_TO_EVIDENCE_AI_EXPERIMENT_ENGINE.md) | `PATENT_HOLD_NON_ENABLING` | NO |
| Behavioral Decision Science & Human–AI Experimentation Layer™ | [`../BEHAVIORAL_DECISION_SCIENCE_HUMAN_AI_LAYER.md`](../BEHAVIORAL_DECISION_SCIENCE_HUMAN_AI_LAYER.md) | `PATENT_HOLD_NON_ENABLING` | NO |
| Innovation & Entrepreneurship Evidence Layer™ | [`../INNOVATION_ENTREPRENEURSHIP_EVIDENCE_LAYER.md`](../INNOVATION_ENTREPRENEURSHIP_EVIDENCE_LAYER.md) | `PATENT_HOLD_NON_ENABLING` | NO |
| Management Accounting & AI Cost Intelligence Layer™ | [`../MANAGEMENT_ACCOUNTING_AI_COST_INTELLIGENCE_LAYER.md`](../MANAGEMENT_ACCOUNTING_AI_COST_INTELLIGENCE_LAYER.md) | `PATENT_HOLD_NON_ENABLING` | NO |
| Open Model Benchmark & Cost Intelligence Layer™ | [`../OPEN_MODEL_BENCHMARK_COST_INTELLIGENCE_LAYER.md`](../OPEN_MODEL_BENCHMARK_COST_INTELLIGENCE_LAYER.md) | `PATENT_HOLD_NON_ENABLING` | NO |
| Visualization & Decision Intelligence Layer™ | [`../VISUALIZATION_DECISION_INTELLIGENCE_LAYER.md`](../VISUALIZATION_DECISION_INTELLIGENCE_LAYER.md) | `PATENT_HOLD_NON_ENABLING` | NO |
| Business School Simulation & Digital Twin Layer™ | [`../BUSINESS_SCHOOL_SIMULATION_DIGITAL_TWIN_LAYER.md`](../BUSINESS_SCHOOL_SIMULATION_DIGITAL_TWIN_LAYER.md) | `PATENT_HOLD_NON_ENABLING` | NO |
| Knowledge RAG / GraphRAG / KAG Layer™ | [`../TWO_CORE_CONSTITUTION.md`](../TWO_CORE_CONSTITUTION.md) | `ARCHITECTURE_ADOPTED` | NO |
| Professional Education & Question Bank Layer™ | [`../TWO_CORE_CONSTITUTION.md`](../TWO_CORE_CONSTITUTION.md) | `PUBLIC_EDUCATION_DESIGN` | NO |
| Decision–Consequence Engine™ | [`../simulations/business-school/decision_consequence_engine.py`](../simulations/business-school/decision_consequence_engine.py) | `PATENT_HOLD_NON_ENABLING` | NO |
| Professional Judgment Passport™ | [`professional_judgment_passport.schema.json`](./professional_judgment_passport.schema.json) | `PATENT_HOLD_NON_ENABLING` | NO |
| KIWI™ / POMELO™ / VERA™ / IFRS / PCAOB / ESG / ECONOVA-S™ | [`../agents/`](../agents/) | mixed research statuses | NO |
| CCCMP™ | [`../CCCMP_PROJECT_COST_CONTRACT_CLAIMS_PROGRAMME.md`](../CCCMP_PROJECT_COST_CONTRACT_CLAIMS_PROGRAMME.md) | `PATENT_HOLD_NON_ENABLING` | NO |
| Prototype 003 | [`../Prototype_003/runtime/`](../Prototype_003/runtime/) | `EXECUTED_VALIDATED` | NO |
| Prototype 004 provider harness | [`../PROTOTYPE_004_PROVIDER_EXECUTION.md`](../PROTOTYPE_004_PROVIDER_EXECUTION.md) | `IMPLEMENTED_EXECUTION_GATED` | NO |

## Microsoft POC V1 boundary

Microsoft V1 contains executed SEC/XBRL facts, financial calculations, CAM mapping, bounded text analytics, R&D/GitHub innovation measures, a synthetic Microsoft-like ABC/TDABC/AI-cost example, Evidence Passport, publication-only Human Gate and a four-test local unit suite.

It does **not** yet contain an executed participant experiment, Microsoft Fama–French regression, aggregate patent analysis, or live comparative model-quality validation. Therefore it remains `RESEARCH_PROTOTYPE` and does not replace Prototype 003's `EXECUTED_VALIDATED` status.

## Governance inherited everywhere

Every layer/prototype/programme must use, where applicable: provenance, license controls, Evidence Passport™, causal/decision DAGs, versioning, reproducibility, replication, falsification, red-team/adversarial review and Human Approval Gate™.

## Fixed validation boundary

`EXECUTED_VALIDATED` remains limited to **v0.2.3 / Audit Workspace V0.4 / Prototype 003**. Microsoft V1 is an important end-to-end proof of concept, but architecture/module execution is not equivalent to independent scientific validation.

## Patent-first interpretation

```text
permanent_core_count = 2
third_permanent_core_allowed = false
microsoft_poc_v1_is_core = false
microsoft_poc_v1_status = RESEARCH_PROTOTYPE
prototype_003_status = EXECUTED_VALIDATED
architecture_documented != runtime_executed
module_executed != independent_scientific_validation
human_gate_required = true
```
