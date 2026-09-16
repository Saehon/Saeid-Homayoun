# NAAIL OpenLab™ — Platform Capability & Maturity Matrix

> **PATENT RIGHTS RESERVED — PATENT APPLICATION PREPARATION IN PROGRESS**

## Constitutional status

**NAAIL OpenLab™ — V2026.3 Multi-Agent Digital Twin** is governed by the **[Two-Core Constitution](../TWO_CORE_CONSTITUTION.md)**.

Exactly two permanent cores exist:

- **Stable Knowledge Core™**
- **Replaceable Technology Core™**

No third permanent core is permitted.

## Status vocabulary

| Status | Meaning |
|---|---|
| `EXECUTED_VALIDATED` | Reproducible execution evidence exists for the stated scope. |
| `IMPLEMENTED_EXECUTION_GATED` | Infrastructure exists, but required execution evidence is not yet established. |
| `ARCHITECTURE_ADOPTED` | High-level public design/governance is adopted. |
| `REGISTRY_ADOPTED` | Third-party tools/data are catalogued; registration is not execution. |
| `RESEARCH_PROTOTYPE` | A bounded research prototype exists. |
| `PUBLIC_EDUCATION_DESIGN` | Public teaching/research design, not production deployment. |
| `PATENT_HOLD_NON_ENABLING` | Name/high-level role public; enabling implementation withheld pending filing review. |

## Capability matrix

| Capability | Public asset | Status | Core? |
|---|---|---|---|
| **Two-Core Constitution** | [`../TWO_CORE_CONSTITUTION.md`](../TWO_CORE_CONSTITUTION.md) | `ARCHITECTURE_ADOPTED` | constitutional rule |
| Stable Knowledge Core™ | [`MASTER_PLATFORM_HIERARCHY.md`](./MASTER_PLATFORM_HIERARCHY.md) | `ARCHITECTURE_ADOPTED` | **YES** |
| Replaceable Technology Core™ | [`MASTER_PLATFORM_HIERARCHY.md`](./MASTER_PLATFORM_HIERARCHY.md) | `ARCHITECTURE_ADOPTED` | **YES** |
| NAAIL Data & Evidence Mesh™ | [`../DATA_EVIDENCE_MESH.md`](../DATA_EVIDENCE_MESH.md) | `PATENT_HOLD_NON_ENABLING` | NO |
| FT50 / AJG Evidence Graph™ | [`../TWO_CORE_CONSTITUTION.md`](../TWO_CORE_CONSTITUTION.md) | `ARCHITECTURE_ADOPTED` | NO |
| Nobel Theory-to-Evidence & AI Experiment Engine™ | [`../NOBEL_THEORY_TO_EVIDENCE_AI_EXPERIMENT_ENGINE.md`](../NOBEL_THEORY_TO_EVIDENCE_AI_EXPERIMENT_ENGINE.md) | `PATENT_HOLD_NON_ENABLING` | NO |
| Behavioral Decision Science & Human–AI Experimentation Layer™ | [`../BEHAVIORAL_DECISION_SCIENCE_HUMAN_AI_LAYER.md`](../BEHAVIORAL_DECISION_SCIENCE_HUMAN_AI_LAYER.md) | `PATENT_HOLD_NON_ENABLING` | NO |
| Innovation & Entrepreneurship Evidence Layer™ | [`../INNOVATION_ENTREPRENEURSHIP_EVIDENCE_LAYER.md`](../INNOVATION_ENTREPRENEURSHIP_EVIDENCE_LAYER.md) | `PATENT_HOLD_NON_ENABLING` | NO |
| **Management Accounting & AI Cost Intelligence Layer™** | [`../MANAGEMENT_ACCOUNTING_AI_COST_INTELLIGENCE_LAYER.md`](../MANAGEMENT_ACCOUNTING_AI_COST_INTELLIGENCE_LAYER.md) | `PATENT_HOLD_NON_ENABLING` | NO |
| **Open Model Benchmark & Cost Intelligence Layer™** | [`../OPEN_MODEL_BENCHMARK_COST_INTELLIGENCE_LAYER.md`](../OPEN_MODEL_BENCHMARK_COST_INTELLIGENCE_LAYER.md) | `PATENT_HOLD_NON_ENABLING` | NO |
| **Visualization & Decision Intelligence Layer™** | [`../VISUALIZATION_DECISION_INTELLIGENCE_LAYER.md`](../VISUALIZATION_DECISION_INTELLIGENCE_LAYER.md) | `PATENT_HOLD_NON_ENABLING` | NO |
| Business School Simulation & Digital Twin Layer™ | [`../BUSINESS_SCHOOL_SIMULATION_DIGITAL_TWIN_LAYER.md`](../BUSINESS_SCHOOL_SIMULATION_DIGITAL_TWIN_LAYER.md) | `PATENT_HOLD_NON_ENABLING` | NO |
| Knowledge RAG / GraphRAG / KAG Layer™ | [`../TWO_CORE_CONSTITUTION.md`](../TWO_CORE_CONSTITUTION.md) | `ARCHITECTURE_ADOPTED` | NO |
| Professional Education & Question Bank Layer™ | [`../TWO_CORE_CONSTITUTION.md`](../TWO_CORE_CONSTITUTION.md) | `PUBLIC_EDUCATION_DESIGN` | NO |
| Decision–Consequence Engine™ | [`../simulations/business-school/decision_consequence_engine.py`](../simulations/business-school/decision_consequence_engine.py) | `PATENT_HOLD_NON_ENABLING` | NO |
| Professional Judgment Passport™ | [`professional_judgment_passport.schema.json`](./professional_judgment_passport.schema.json) | `PATENT_HOLD_NON_ENABLING` | NO |
| KIWI™ / POMELO™ / VERA™ / IFRS / PCAOB / ESG / ECONOVA-S™ | [`../agents/`](../agents/) | mixed research statuses | NO |
| CCCMP™ | [`../CCCMP_PROJECT_COST_CONTRACT_CLAIMS_PROGRAMME.md`](../CCCMP_PROJECT_COST_CONTRACT_CLAIMS_PROGRAMME.md) | `PATENT_HOLD_NON_ENABLING` | NO |
| Prototype 003 | [`../Prototype_003/runtime/`](../Prototype_003/runtime/) | `EXECUTED_VALIDATED` | NO |
| Prototype 004 provider harness | [`../PROTOTYPE_004_PROVIDER_EXECUTION.md`](../PROTOTYPE_004_PROVIDER_EXECUTION.md) | `IMPLEMENTED_EXECUTION_GATED` | NO |

## Management Accounting & AI Cost boundary

Stable Knowledge Core™ contains the scientific/professional meaning of BSC/Strategy Maps, ABC, TDABC, budgeting, responsibility accounting, variance analysis, cost-driver theory, profitability, capacity and performance measurement.

The three new public layers apply or support that knowledge but remain non-core:

- Management Accounting & AI Cost Intelligence Layer™;
- Open Model Benchmark & Cost Intelligence Layer™;
- Visualization & Decision Intelligence Layer™.

NAAIL-developed AI Activity-Based Costing™, TTD-AIC and Cost-to-Value research are experimental extensions. They do not rewrite established BSC/ABC/TDABC theory and are not represented as original Kaplan frameworks.

## Placement rule

```text
stable_when_vendor_or_model_changes -> Stable Knowledge Core
replaceable_implementation -> Replaceable Technology Core or modular layer
BSC_ABC_TDABC_theory -> Stable Knowledge Core
benchmark_finops_observability_visualization -> Replaceable Technology Core or modular layer
new_domain -> supporting layer/programme, never core
new_dataset -> Data & Evidence Mesh, never core
new_model_or_framework -> Replaceable Technology Core, never core
```

## Governance inherited everywhere

Every layer/programme must use, where applicable: provenance, license controls, Evidence Passport™, causal/decision DAGs, versioning, reproducibility, replication, falsification, red-team/adversarial review and Human Approval Gate™.

For AI cost/model comparison, price and benchmark observations must be timestamped and provenance-controlled. Cost minimization cannot override required evidence, reliability, reproducibility or professional judgment.

## Fixed validation boundary

The validated public executable checkpoint remains **v0.2.3 / Audit Workspace V0.4 / Prototype 003**. The new Management Accounting & AI Cost layers do not themselves establish executed validation.

## Patent-first interpretation

```text
patent_sensitive_name_public != implementation_public
two_core_constitution_frozen = true
permanent_core_count = 2
third_permanent_core_allowed = false
management_accounting_ai_cost_layer_is_core = false
open_model_benchmark_cost_layer_is_core = false
visualization_decision_intelligence_layer_is_core = false
bsc_is_new_core = false
abc_is_new_core = false
tdabc_is_new_core = false
ai_finops_is_new_core = false
cost_minimization_overrides_quality_evidence_or_governance = false
benchmark_rank_equals_truth = false
architecture_documented != runtime_executed
public_access != unrestricted_redistribution
human_gate_required = true
```
