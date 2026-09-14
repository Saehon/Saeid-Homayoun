# NAAIL ERP Digital Twin Lab™

**Platform:** NAAIL OpenLab™ — V2026.3 Multi-Agent Digital Twin  
**Knowledge & RAG Core:** `KRG2026.3` — frozen and governed  
**Layer:** Technology / Simulation / ERP Adapter Layer  
**Status:** Open-source ERP integration architecture adopted; runtime deployments remain gated

> **ERP systems generate and expose business-process evidence. They do not define accounting, audit, ICFR, or scientific truth. Canonical meaning remains in the frozen Knowledge & RAG Core.**

## Purpose

The NAAIL ERP Digital Twin Lab™ provides open-source enterprise systems that can be used to build controlled accounting, audit, ICFR, forensic, procurement, inventory, payroll, manufacturing, and financial-close Digital Twins.

## Canonical architecture

```text
FROZEN KNOWLEDGE & RAG CORE™ — KRG2026.3
│  IFRS / PCAOB / SEC / accounting ontology / audit ontology / ICFR
│
└── read-only governed contract
        ↓
NAAIL ERP DIGITAL TWIN LAB™ — TECHNOLOGY / SIMULATION LAYER
        │
        ├── ERPNext / Frappe
        ├── Odoo Community
        ├── Apache OFBiz
        ├── LedgerSMB
        ├── iDempiere
        ├── Dolibarr
        ├── Tryton
        ├── metasfresh
        ├── Axelor Open Suite
        ├── inoERP
        ├── FrontAccounting
        ├── webERP
        └── ERP5
        │
        ↓
Synthetic Client XYZ
        │
        ├── Order-to-Cash
        ├── Purchase-to-Pay
        ├── Record-to-Report
        ├── Inventory
        ├── Payroll
        ├── Fixed Assets
        ├── Manufacturing
        ├── Revenue
        ├── Journal Entries
        └── Internal Controls
        │
        ↓
POMELO™ + KIWI™ + GAA™ + ICFR Intelligence + Forensic Intelligence
        │
Critic → Falsifier → Evidence Auditor → Replicator → Human Gate™
```

## Priority engines

1. **ERPNext / Frappe** — primary modern ERP sandbox for accounting, GL, AR/AP, inventory, procurement, manufacturing, assets, projects and HR.
2. **LedgerSMB** — accounting-first benchmark for double-entry, purchasing, inventory and audit/control simulations.
3. **Apache OFBiz** — permissively licensed enterprise-process engine for ERP/CRM/e-commerce/supply-chain/MRP workflows.
4. **Odoo Community** — broad enterprise benchmark; only Community/open-source components are in scope unless separate rights exist.
5. **iDempiere** — complex ERP/CRM/MFG/SCM/POS workflow and ICFR/control benchmark.

## Additional reference engines

Dolibarr, Tryton, metasfresh, Axelor Open Suite, inoERP, FrontAccounting, webERP and ERP5 remain valuable comparison/sandbox systems. Their exact version, license and redistribution obligations must be re-verified before runtime promotion or code redistribution.

## Adapter-first integration rule

NAAIL should prefer APIs, exported ledgers, event logs, database views, CSV/JSON fixtures, MCP-style connectors, or isolated containers over copying ERP source code into the NAAIL repository.

```text
third_party_erp_is_knowledge_authority = false
third_party_erp_may_modify_knowledge_rag_core = false
erp_transaction_is_valid_without_control_checks = false
erp_output_is_audit_evidence_without_provenance = false
erp_generated_journal_is_posted_without_gate = false
human_gate_required = true
```

## Digital Twin benchmark families

- Order-to-Cash: customer → sales order → shipment → invoice → revenue → cash.
- Purchase-to-Pay: vendor → purchase order → receipt → invoice → payment.
- Record-to-Report: journal → posting → close → trial balance → financial statements.
- Inventory: receipt → movement → count → valuation → write-down.
- Fixed Assets: acquisition → capitalization → depreciation → impairment → disposal.
- Payroll: employee master → payroll run → liabilities → payment → reconciliation.
- ICFR: access, segregation of duties, approval limits, master-data changes, journal controls, exception logs.
- Forensic: override, unusual journals, duplicate payments, related parties, cutoff manipulation, suspicious vendor/customer patterns.

## NAAIL agent integration

- **POMELO™ / VERA™:** accounting treatment, posting logic, close, reconciliation and evidence verification.
- **KIWI™:** CAM/KAM and audit-procedure simulations using ERP-derived evidence.
- **GAA™:** adversarial attack on journals, controls, estimates, reconciliations and evidence sufficiency.
- **ICFR Intelligence:** control design, operating effectiveness, segregation-of-duties and remediation testing.
- **Forensic Intelligence:** anomaly, override and fraud-pattern simulation.
- **Student Agent Academy™:** synthetic ERP cases without exposing proprietary firm systems.

## Machine-readable governance

- `architecture/erp_open_source_registry.json`
- `tests/test_erp_open_source_registry.py`
- `.github/workflows/naail_erp_digital_twin_lab.yml`

## Current claim boundary

**Adopted now:** architecture, registry, roles, license-aware status, benchmark families, adapter-first rule, core-boundary protections and CI validation contract.

**Not claimed yet:** installed production ERP instances, completed ERP-to-NAAIL adapters, full transaction ingestion, production security certification, audit effectiveness, or vendor endorsement.

---

NAAIL OpenLab™ is independent. ERP project names identify third-party open-source projects and do not imply affiliation, endorsement, sponsorship, certification, or ownership. Third-party code remains subject to its own license and terms.