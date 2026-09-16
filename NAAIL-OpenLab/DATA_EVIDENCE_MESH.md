# NAAIL Data & Evidence Mesh™

**Umbrella:** NAAIL OpenLab™ — V2026.3 Multi-Agent Digital Twin  
**Architecture rule:** exactly two permanent cores — **Knowledge Core™** and **Technology Core™**  
**Status:** governed supporting data/evidence layer — **not a third core**

## Purpose

**NAAIL Data & Evidence Mesh™** connects public/rights-cleared evidence to NAAIL Digital Twins and professional agents without turning GitHub into a bulk-data warehouse.

Its canonical objective is:

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

The Mesh uses APIs, lightweight connectors, source manifests, provenance metadata, rights/license metadata, version/period identifiers, retrieval timestamps, hashes/checksums where feasible, and reproducible transformation records. Large third-party datasets should be retrieved from the originating source or an approved cache rather than committed to this repository.

## Relationship to the two permanent cores

The Mesh is a supporting layer between governed evidence sources and the professional/simulation layers.

```text
NAAIL OpenLab™ — V2026.3 Multi-Agent Digital Twin
│
├── PERMANENT CORE 1 — Knowledge Core™
├── PERMANENT CORE 2 — Technology Core™
│
├── NAAIL Data & Evidence Mesh™                 [SUPPORTING]
│   ├── Source Registry
│   ├── API / Connector Adapters
│   ├── Rights / License Gate
│   ├── Provenance / Version Gate
│   ├── Evidence Passport™ Builder
│   ├── Validation / Reconciliation
│   └── Evidence Routing
│
├── Professional Agents
├── Business School Simulation & Digital Twin Layer
├── Decision–Consequence Engine™
├── Professional Judgment Passport™
└── Human Approval Gate™
```

The Mesh does **not** change standards meaning, ontology, RAG semantics, evidence authority, professional judgment rules or Human Gate requirements.

## Relationship to NAAIL Free Data Fabric™

The two components have different jobs:

- **Free Data Fabric™** — source discovery, source classification, rights/provenance requirements, and Knowledge-Core admission governance.
- **Data & Evidence Mesh™** — runtime retrieval/reference, normalization, versioning, Evidence Passport generation, reconciliation, agent routing, and Digital Twin binding.

A source can be registered in the Free Data Fabric without being installed, downloaded, executed, or admitted to the Knowledge Core.

## Priority evidence sources

| Source | Primary NAAIL role | Connector model | Evidence / rights boundary |
|---|---|---|---|
| **SEC EDGAR / XBRL** | issuer filings, company facts, submissions, accounting/audit evidence | direct SEC REST/JSON + filing references | SEC public source; preserve filing/accession/form/period/retrieval metadata; do not treat parsing as authoritative interpretation |
| **FRED / ALFRED** | macro, rates, inflation, labor, financial conditions, vintage/revision-aware evidence | St. Louis Fed API | API credentials may be required; rights can vary by underlying series; preserve series/source/vintage/realtime dates |
| **Fama–French Data Library** | asset-pricing factors and portfolios | versioned TXT/CSV retrieval/reference | academic research source; preserve dataset name/frequency/date and source terms; do not assume unrestricted resale/repackaging |
| **World Bank Indicators API** | country/macro/development/context controls | World Bank V2 API | public API; dataset/source-specific attribution/terms still apply |
| **Our World in Data CO₂** | emissions/climate context | versioned OWID CSV/JSON/codebook reference | OWID-produced material is open with attribution; underlying third-party indicators retain original source terms |
| **Our World in Data Energy** | energy mix/consumption/electricity context | versioned OWID CSV/JSON/codebook reference | preserve codebook, original-source metadata, attribution and third-party rights |
| **OpenAlex** | scholarly metadata, citation/topic graphs, evidence-gap discovery | API/snapshot reference | OpenAlex data are open scholarly metadata; metadata do not prove scientific claims or article validity |
| **OpenSanctions** | sanctions/PEP/entity-risk research and forensic/governance simulation | hosted API or non-commercial bulk reference | non-commercial/academic use conditions apply; hosted API requires authentication; never treat a fuzzy match as a legal conclusion |
| **OpenBB** *(optional)* | provider abstraction / finance-data connector layer | optional provider extensions | Technology-Core convenience connector only; underlying provider licenses/credentials/terms govern each dataset |

## Evidence Passport™ contract

Every retrieved or referenced evidence object should record at least:

```text
passport_id
source_id
source_name
source_authority_type
source_url_or_endpoint
retrieved_at_utc
source_version_or_period
as_of_date
vintage_or_realtime_period
jurisdiction
entity_identifiers
raw_or_derived
query_or_request_parameters
raw_hash_or_response_hash
transformation_chain
connector_name
connector_version
license_or_terms_status
redistribution_status
citation_requirement
source_specific_restrictions
validation_status
knowledge_core_admission_status
agent_access_scope
human_reviewer
```

For APIs returning revised time series, the Passport should preserve the **vintage/realtime context** where available rather than silently substituting later revisions.

## Mesh routing policy

```text
External Source
    ↓
Source / Rights Registry
    ↓
Connector / Retrieval Adapter
    ↓
Raw response reference + hash
    ↓
Normalization / Entity Resolution
    ↓
Evidence Passport™
    ↓
Validation / Reconciliation / Contradiction checks
    ↓
Agent-specific read scope
    ↓
Digital Twin state
    ↓
Decision + consequence ledger
    ↓
VERA™ verification
    ↓
Human Approval Gate™
```

No connector has write authority over the Knowledge Core.

## Agent routing

### KIWI™
SEC filings/XBRL, audit disclosures, macro/market context when material, CAM/KAM evidence, and contradiction checks.

### POMELO™
SEC accounting facts/notes, IFRS issue evidence, company facts, disclosure/accounting transformations and professional reasoning.

### VERA™
Evidence Passport verification, cross-source consistency, missing provenance, unsupported inference detection, version/vintage checks, and Decision DAG verification.

### IFRS Agent™
Consumes company/reporting evidence and authoritative IFRS references; public market/macro data may provide context but cannot alter standards meaning.

### PCAOB Agent™
Consumes public audit/regulatory evidence and engagement simulation evidence; no confidential inspection data is implied.

### ESG Agent
OWID CO₂/Energy, World Bank and issuer sustainability evidence with source-level attribution and rights metadata.

### ECONOVA-S™
FRED/ALFRED, Fama–French, World Bank, SEC/XBRL, OWID and optional OpenBB provider connections for finance/economics research.

### Forensic / Governance capabilities
OpenSanctions may support entity-risk, sanctions/PEP and governance research under applicable non-commercial/academic terms. Matches are research signals requiring verification, not legal determinations.

## First integrated prototype — NAAIL Audit & Accounting Digital Twin™

The first Mesh-enabled prototype binds **Client XYZ** to a reproducible evidence bundle combining:

1. **SEC / XBRL evidence** — public-company-style financial facts, filing structures and disclosure patterns;
2. **FRED / ALFRED evidence** — macro/financial context and vintage-aware information where relevant;
3. **Fama–French evidence** — market/factor context for valuation, risk and capital-market scenarios where relevant;
4. **World Bank / OWID evidence** — macro, country, climate/energy context when material;
5. **OpenAlex evidence** — literature discovery and research-grounding metadata;
6. **OpenSanctions evidence** — optional forensic/governance/entity-risk simulation when justified;
7. **OpenBB connectors** — optional Technology-Core provider abstraction, never a substitute for original-source provenance.

Canonical loop:

```text
SEC + Macro + Market + ESG / Research Evidence
→ Evidence Passport™
→ KIWI™ + POMELO™ + VERA™ + IFRS/PCAOB/ESG/ECONOVA-S™
→ Audit & Accounting Digital Twin state
→ Student / Researcher professional decision
→ Professional Decision DAG™
→ Decision–Consequence Engine™
→ Updated state
→ Agent Arena™ / Blind Gold / Falsification
→ VERA™ verification
→ Professional Judgment Passport™
→ Human Approval Gate™
```

The dynamic prototype specification remains at [`digital-twins/audit-accounting/README.md`](./digital-twins/audit-accounting/README.md).

## Storage policy

### GitHub stores

- source/connector manifests;
- schemas;
- small synthetic fixtures;
- hashes/checksums;
- transformation code;
- tests;
- query examples without secrets;
- Evidence Passport templates;
- small derived outputs where redistribution is allowed;
- source URLs, accessions, series IDs and version metadata.

### GitHub does not store by default

- bulk SEC archives;
- large FRED/ALFRED mirrors;
- full Fama–French archives;
- bulk World Bank/OWID/OpenAlex/OpenSanctions datasets;
- provider credentials/API keys;
- restricted/licensed datasets;
- large third-party extracts whose redistribution rights are uncertain.

Secrets belong in secure environment/secret stores, never repository files.

## Connector status vocabulary

```text
REFERENCE_ONLY
CONNECTOR_SPECIFIED
CONNECTOR_IMPLEMENTED_UNVALIDATED
CONNECTOR_VALIDATED
EXECUTED_WITH_EVIDENCE_PASSPORT
DISABLED_RIGHTS_OR_SECURITY
```

A registry entry or connector name does not imply that data were retrieved in a specific experiment.

## Permanent invariants

```text
permanent_core_count = 2
data_evidence_mesh_is_core = false
large_third_party_dataset_should_be_committed_to_github = false
connector_name_implies_execution = false
api_response_is_authoritative_interpretation = false
public_access_equals_unrestricted_redistribution = false
openbb_provider_equals_original_source = false
opensanctions_match_equals_legal_determination = false
openalex_metadata_proves_research_claim = false
technology_core_may_rewrite_knowledge_core = false
provenance_required = true
version_or_period_required = true
human_gate_required = true
```

## Canonical machine-readable assets

- Source/connector registry: [`architecture/data_evidence_mesh_registry.json`](./architecture/data_evidence_mesh_registry.json)
- Existing broader source registry: [`architecture/free_data_source_registry.json`](./architecture/free_data_source_registry.json)
- Existing Free Data Fabric: [`FREE_DATA_FABRIC.md`](./FREE_DATA_FABRIC.md)

## Independence

NAAIL OpenLab™ is independent. SEC, Federal Reserve Bank of St. Louis/FRED/ALFRED, Kenneth French/Dartmouth, World Bank, Our World in Data, OpenAlex, OpenSanctions, OpenBB and underlying data providers remain independent sources/projects. Inclusion identifies evidence sources or optional connector technologies only and does not imply affiliation, endorsement, sponsorship, certification or transfer of ownership.