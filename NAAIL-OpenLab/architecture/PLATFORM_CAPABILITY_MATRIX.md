# NAAIL OpenLab™ — Platform Capability & Maturity Matrix

**Next-Generation Accounting, Audit & Assurance Intelligence Lab**  
*A Global Evidence-Governed Multi-Agent Digital Twin Platform for Accounting, Audit, Finance, Sustainability and Scientific Discovery*

This matrix is the canonical public maturity map for major NAAIL capabilities. It separates validated execution from implemented infrastructure, architecture, integration registries, and methodological references.

## Status vocabulary

| Status | Meaning |
|---|---|
| `EXECUTED_VALIDATED` | A reproducible public or research-safe execution artifact exists and has been validated for the stated scope. |
| `IMPLEMENTED_EXECUTION_GATED` | Code/infrastructure exists, but the relevant provider/data/benchmark run is not yet evidenced. |
| `ARCHITECTURE_ADOPTED` | The design, interfaces, governance and role boundaries are adopted; runtime implementation may be partial or absent. |
| `REGISTRY_ADOPTED` | Upstream tools/data are catalogued with governance and rights boundaries; registration is not execution. |
| `RESEARCH_PROTOTYPE` | A bounded research prototype or empirical project exists; scope is narrower than production use. |
| `PUBLIC_EDUCATION_DESIGN` | Research/teaching design is public; it is not a production professional system. |
| `REFERENCE_ONLY` | Used as methodological inspiration, benchmark or optional provider/upstream reference. |

## Capability matrix

| Capability | Canonical asset | Status | Evidence boundary |
|---|---|---|---|
| Global NAAIL identity | [`../BRAND_IDENTITY.md`](../BRAND_IDENTITY.md) | `ARCHITECTURE_ADOPTED` | Branding/governance only; no scientific result implied. |
| Audit Digital Twin Prototype 003 | [`../Prototype_003/runtime/`](../Prototype_003/runtime/) | `EXECUTED_VALIDATED` | Deterministic frozen synthetic checkpoint only. |
| Prototype 004 provider harness | [`../PROTOTYPE_004_PROVIDER_EXECUTION.md`](../PROTOTYPE_004_PROVIDER_EXECUTION.md) | `IMPLEMENTED_EXECUTION_GATED` | Provider/model comparison requires real credential-gated run artifacts. |
| Scientific Discovery Contract | [`../SCIENTIFIC_DISCOVERY_CONTRACT.md`](../SCIENTIFIC_DISCOVERY_CONTRACT.md) | `ARCHITECTURE_ADOPTED` | Governance contract; not evidence that external systems executed. |
| Google-inspired science orchestration | [`../GOOGLE_SCIENTIFIC_DISCOVERY_ORCHESTRATION.md`](../GOOGLE_SCIENTIFIC_DISCOVERY_ORCHESTRATION.md) | `ARCHITECTURE_ADOPTED` | Google/DeepMind systems are references/optional targets unless evidenced. |
| Digital Twin science-link registry | [`digital_twin_science_link_registry.json`](./digital_twin_science_link_registry.json) | `REGISTRY_ADOPTED` | Maps existing repo assets to applicable research phases. |
| IFRS Intelligence Agent™ | [`../agents/ifrs/`](../agents/ifrs/) | `RESEARCH_PROTOTYPE` | Research-safe standards/reporting Digital Twin; no IFRS Foundation affiliation. |
| PCAOB Intelligence Agent™ | [`../agents/pcaob/`](../agents/pcaob/) | `RESEARCH_PROTOTYPE` | Public/synthetic inspection research; no confidential PCAOB access. |
| KIWI™ | [`../agents/kiwi/`](../agents/kiwi/) | `RESEARCH_PROTOTYPE` | CAM/KAM/audit-intelligence research scope. |
| POMELO™ | [`../agents/pomelo/`](../agents/pomelo/) | `RESEARCH_PROTOTYPE` | Public architecture; sensitive implementation may remain private. |
| ECONOVA-S™ | [`../agents/econova-s/`](../agents/econova-s/) | `RESEARCH_PROTOTYPE` | Finance/economics/data-economy studies; study-level evidence required. |
| ESG Intelligence | [`../agents/esg/`](../agents/esg/) | `RESEARCH_PROTOTYPE` | Sustainability research; standards rights remain external. |
| ICFR Intelligence | [`../agents/icfr/`](../agents/icfr/) | `RESEARCH_PROTOTYPE` | Controls/material-weakness research and forecasting. |
| Forensic Intelligence | [`../agents/forensic/`](../agents/forensic/) | `RESEARCH_PROTOTYPE` | Investigative/forensic simulation and public-evidence research. |
| Free Data Fabric™ | [`../FREE_DATA_FABRIC.md`](../FREE_DATA_FABRIC.md) | `REGISTRY_ADOPTED` | Free access does not equal authority or unrestricted redistribution. |
| ERP Digital Twin Lab™ | [`../ERP_DIGITAL_TWIN_LAB.md`](../ERP_DIGITAL_TWIN_LAB.md) | `REGISTRY_ADOPTED` | Adapter-first; third-party ERP output is not authoritative evidence. |
| Audit Analytics Open-Source Pack™ | [`../AUDIT_ANALYTICS_OPEN_SOURCE_PACK.md`](../AUDIT_ANALYTICS_OPEN_SOURCE_PACK.md) | `REGISTRY_ADOPTED` | Upstream software remains third-party. |
| Finance Market Intelligence Lab™ | [`../FINANCE_MARKET_INTELLIGENCE_LAB.md`](../FINANCE_MARKET_INTELLIGENCE_LAB.md) | `REGISTRY_ADOPTED` | Software/data rights separated; Bloomberg/S&P IP not reproduced. |
| ESG & Sustainability Intelligence Lab™ | [`../ESG_SUSTAINABILITY_INTELLIGENCE_LAB.md`](../ESG_SUSTAINABILITY_INTELLIGENCE_LAB.md) | `REGISTRY_ADOPTED` | Standards text/copyright boundaries preserved. |
| Accounting & Audit Open-Source Pack™ | [`../OPEN_SOURCE_ACCOUNTING_AUDIT_PACK.md`](../OPEN_SOURCE_ACCOUNTING_AUDIT_PACK.md) | `REGISTRY_ADOPTED` | Parser/agent output requires validation and Human Gate. |
| Adversarial Intelligence Fabric™ | [`../ADVERSARIAL_INTELLIGENCE_FABRIC.md`](../ADVERSARIAL_INTELLIGENCE_FABRIC.md) | `ARCHITECTURE_ADOPTED` | Debate/red-team roles do not create truth by consensus. |
| FT50/AJG Replication Arena | [`../benchmarks/ft50_abs4/`](../benchmarks/ft50_abs4/) | `IMPLEMENTED_EXECUTION_GATED` | Exact commit pinning/environment reconstruction and real replication required. |
| SEC EDGAR Education Lab™ | [`../SEC_EDGAR_EDUCATION_LAB.md`](../SEC_EDGAR_EDUCATION_LAB.md) | `PUBLIC_EDUCATION_DESIGN` | SEC remains the authoritative source. |
| Student Agent Academy | [`../docs/education/NAAIL_BIG4_STUDENT_AGENT_ACADEMY.md`](../docs/education/NAAIL_BIG4_STUDENT_AGENT_ACADEMY.md) | `PUBLIC_EDUCATION_DESIGN` | No Big Four partnership implied without written agreement. |
| Open-source agent stack | [`../OPEN_SOURCE_AGENT_STACK.md`](../OPEN_SOURCE_AGENT_STACK.md) | `REGISTRY_ADOPTED` | Framework inclusion does not mean installed/benchmarked/validated. |

## Permanent interpretation rules

```text
architecture_documented != runtime_executed
registry_entry != dependency_installed
provider_named != provider_run
public_data != unrestricted_redistribution
open_source_software != authoritative_professional_evidence
prediction != causality
agent_consensus != scientific_truth
human_gate_required = true
```

## Knowledge / technology separation

The matrix inherits the frozen `KRG2026.3` boundary:

- Knowledge & RAG semantics remain governed and versioned.
- Replaceable models, frameworks, ERP engines, vector stores, agent runtimes and provider services operate outside the frozen core unless explicitly admitted through governance.
- Technology changes cannot silently change ontology, evidence meaning, causal DAGs, standards interpretation, or authoritative-source status.

Machine-readable companion: [`platform_capability_registry.json`](./platform_capability_registry.json).