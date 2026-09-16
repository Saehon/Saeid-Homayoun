# NAAIL OpenLab™ — Open-Source Integration Hub

**Next-Generation Accounting, Audit & Assurance Intelligence Lab**  
*A Global Evidence-Governed Multi-Agent Digital Twin Platform for Accounting, Audit, Finance, Sustainability and Scientific Discovery*

**Platform:** NAAIL OpenLab™ — V2026.3 Multi-Agent Digital Twin  
**Permanent cores:** exactly two — **Knowledge Core™ + Technology Core™**  
**Knowledge & RAG Core:** `KRG2026.3` — frozen and governed  
**Purpose:** Canonical navigation for NAAIL public-data/evidence, open-source software, simulation, analytics, finance, ERP, audit, and ESG integrations.

> External repositories, APIs and datasets remain third-party assets under their original licenses and data terms. Registration or adoption in NAAIL does not transfer ownership, create affiliation, prove execution, or make third-party outputs authoritative professional evidence.

## Current integration families

| NAAIL module | Scope | Canonical file | Machine-readable registry |
|---|---|---|---|
| **NAAIL Data & Evidence Mesh™** | runtime/reference routing for SEC EDGAR/XBRL, FRED/ALFRED, Fama–French, World Bank, OWID CO₂/Energy, OpenAlex, OpenSanctions and optional OpenBB connectors | [`DATA_EVIDENCE_MESH.md`](./DATA_EVIDENCE_MESH.md) | [`architecture/data_evidence_mesh_registry.json`](./architecture/data_evidence_mesh_registry.json) |
| **NAAIL Free Data Fabric™** | source discovery/admission governance for SEC, PCAOB, XBRL/ESEF, GLEIF, Nordic data, World Bank, Climate TRACE, OpenAlex, Crossref, Fama–French, Damodaran, FRED | [`FREE_DATA_FABRIC.md`](./FREE_DATA_FABRIC.md) | [`architecture/free_data_source_registry.json`](./architecture/free_data_source_registry.json) |
| **NAAIL ERP Digital Twin Lab™** | ERPNext, Odoo Community, Apache OFBiz, LedgerSMB, iDempiere and additional open ERP references | [`ERP_DIGITAL_TWIN_LAB.md`](./ERP_DIGITAL_TWIN_LAB.md) | [`architecture/erp_open_source_registry.json`](./architecture/erp_open_source_registry.json) |
| **NAAIL Audit Analytics Open-Source Pack™** | audit analytics, ICFR, journal-entry tests, XBRL validation, audit benchmarks | [`AUDIT_ANALYTICS_OPEN_SOURCE_PACK.md`](./AUDIT_ANALYTICS_OPEN_SOURCE_PACK.md) | [`architecture/audit_analytics_open_source_registry.json`](./architecture/audit_analytics_open_source_registry.json) |
| **NAAIL Finance Market Intelligence Lab™** | OpenBB, FinanceToolkit, FinanceDatabase, yfinance, QuantLib, FinRL, PyPortfolioOpt, Riskfolio-Lib | [`FINANCE_MARKET_INTELLIGENCE_LAB.md`](./FINANCE_MARKET_INTELLIGENCE_LAB.md) | [`architecture/finance_open_source_registry.json`](./architecture/finance_open_source_registry.json) |
| **NAAIL ESG & Sustainability Intelligence Lab™** | ESRS/CSRD, EU Taxonomy, VSME, ISSB/SASB, GRI, SDGs, carbon/GHG, climate risk, sustainable finance, ESG assurance | [`ESG_SUSTAINABILITY_INTELLIGENCE_LAB.md`](./ESG_SUSTAINABILITY_INTELLIGENCE_LAB.md) | [`architecture/esg_sustainability_open_source_registry.json`](./architecture/esg_sustainability_open_source_registry.json) |
| **NAAIL Open-Source Accounting & Audit Pack™** | accounting primitives, reconciliation, ledger engines, control gates, SEC parser/tool references | [`OPEN_SOURCE_ACCOUNTING_AUDIT_PACK.md`](./OPEN_SOURCE_ACCOUNTING_AUDIT_PACK.md) | [`architecture/accounting_audit_open_source_registry.json`](./architecture/accounting_audit_open_source_registry.json) |
| **NAAIL Adversarial Intelligence Fabric™** | scientific debate, falsification, replication, red-team and independent review | [`ADVERSARIAL_INTELLIGENCE_FABRIC.md`](./ADVERSARIAL_INTELLIGENCE_FABRIC.md) | [`architecture/adversarial_agent_registry.json`](./architecture/adversarial_agent_registry.json) |

## Canonical architecture

```text
PUBLIC / LICENSED / RIGHTS-CLEARED SOURCES
        ↓
Source discovery + rights/license/provenance governance
        ↓
NAAIL Free Data Fabric™
        ↓
API / connector / reference retrieval
        ↓
NAAIL Data & Evidence Mesh™
        ├── source/version/vintage metadata
        ├── query/request metadata
        ├── rights / redistribution status
        ├── hashes / transformation lineage
        ├── validation / reconciliation
        └── Evidence Passport™
        ↓
FROZEN KNOWLEDGE CORE™ / governed read interfaces
        ↓
KIWI™ · POMELO™ · VERA™ · IFRS · PCAOB · ESG · ECONOVA-S™
        ↓
Business School / Professional Digital Twins
        ↓
Decision–Consequence Engine™
        ↓
Agent Arena™ / Blind Gold / Falsification / Verification
        ↓
Professional Judgment Passport™
        ↓
Human Approval Gate™
```

The Mesh is a **supporting layer**, not a third permanent core. Free Data Fabric governs source discovery/admission; Data & Evidence Mesh governs runtime/reference retrieval, Evidence Passport generation, validation/reconciliation and agent/Digital-Twin routing.

## GitHub data-storage policy

NAAIL uses an **adapter-first / provenance-first** model. GitHub should hold connector/source manifests, schemas, IDs, query examples without secrets, version/vintage metadata, hashes, transformations, tests and small synthetic/rights-cleared fixtures—not large third-party data mirrors by default.

```text
large_third_party_dataset_should_be_committed_to_github = false
credentials_or_api_keys_in_repository = false
connector_name_implies_execution = false
public_access_equals_unrestricted_redistribution = false
```

## Permanent boundary

```text
permanent_core_count = 2
data_evidence_mesh_is_core = false
external_repo_is_authoritative_truth = false
external_dataset_is_authoritative_without_validation = false
api_response_is_authoritative_interpretation = false
software_license_equals_data_license = false
public_access_equals_public_domain = false
third_party_tool_may_modify_knowledge_rag_core = false
vendor_release_changes_canonical_knowledge = false
agent_output_bypasses_human_gate = false
human_gate_required = true
```

## Promotion requirements

Before an upstream repository, dataset, model, API, parser, ERP engine, climate model, market-data adapter, or analytics library moves from reference status to runtime use, NAAIL requires:

1. exact upstream repository/source verification;
2. software-license and separate data-rights review;
3. commit/version/data-period/vintage pinning where applicable;
4. dependency/security review;
5. privacy and data-use review;
6. synthetic or rights-cleared sandbox execution;
7. frozen benchmark and reproducibility evidence;
8. provenance and Evidence Passport™ capture;
9. Failure Memory™ retention for unsuccessful tests;
10. Knowledge/RAG boundary regression test;
11. Human Architecture / Knowledge / Research Gate approval.

## Independence statement

NAAIL OpenLab™ is independent. References to SEC, FRED/ALFRED, Fama–French, World Bank, Our World in Data, OpenAlex, OpenSanctions, OpenBB, GitHub projects, Bloomberg, S&P Global, EFRAG, the European Union, IFRS Foundation, SASB, GRI, the United Nations, PCAOB, universities, professional firms, technology companies, or other organizations identify public technologies, standards, datasets, research references, evidence sources, connector targets or comparison contexts only and do not imply affiliation, endorsement, sponsorship, certification, authorization, execution, or ownership transfer.