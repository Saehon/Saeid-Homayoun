# NAAIL Free Data Fabric™

**Platform:** NAAIL OpenLab™ — V2026.3 Multi-Agent Digital Twin  
**Knowledge & RAG Core:** `KRG2026.3` — frozen and governed  
**Layer:** Evidence acquisition, rights/provenance control, and source admission  
**Status:** Source registry and governance architecture adopted; bulk ingestion/runtime execution remain gated

> **Free data is not automatically trusted data. NAAIL preserves source identity, rights, provenance, temporal applicability, transformation lineage, and Human Gate review before evidence enters the frozen Knowledge & RAG Core.**

## 1. Purpose

The NAAIL Free Data Fabric™ organizes high-value free/public data for accounting, auditing, assurance, corporate governance, finance, economics, sustainability, forensics, Nordic research, and scientific discovery.

It separates three things that must not be confused:

1. **Authoritative/public evidence sources** — regulators, official statistics, standards/regulatory publications, public filings, and official registries.
2. **Open research/metadata sources** — scientific metadata, factor libraries, research data, and public research resources.
3. **Technology/ingestion tools** — parsers, APIs, SDKs, and open-source software used to retrieve or transform evidence.

A parser, model, repository, or API client is never treated as authoritative evidence merely because it is open source.

## 2. Canonical architecture

```text
PUBLIC / FREE SOURCE SYSTEMS
│
├── Accounting & Disclosure
│   ├── SEC Financial Statement Data Sets
│   ├── SEC Financial Statement & Notes Data Sets
│   └── filings.xbrl.org / ESEF / UKSEF
│
├── Audit & Assurance
│   ├── PCAOB AuditorSearch / Form AP
│   ├── PCAOB Inspection Data
│   └── SEC AAER
│
├── Governance / Entity Graph
│   ├── SEC Insider Transactions
│   ├── SEC Form 13F
│   ├── SEC Form ADV / IAPD
│   ├── GLEIF LEI / parent relationships
│   └── Stanford Rock Center public research
│
├── Nordic
│   ├── Statistics Sweden (SCB)
│   ├── Sveriges Riksbank
│   └── Brønnøysundregistrene
│
├── ESG / Sustainability
│   ├── Climate TRACE
│   └── World Bank
│
├── Finance / Economics
│   ├── Fama–French Data Library
│   ├── Damodaran data
│   ├── FRED
│   └── World Bank
│
└── Scientific Evidence
    ├── OpenAlex
    └── Crossref
        │
        ▼
SOURCE ADAPTER / INGESTION PERIMETER
        │
        ├── license / terms check
        ├── source ID + retrieval timestamp
        ├── raw snapshot hash
        ├── transformation lineage
        ├── jurisdiction + period
        ├── raw vs derived flag
        ├── rights / redistribution status
        └── Evidence Passport™
        │
        ▼
KNOWLEDGE-CORE ADMISSION GATE
        │
        ▼
FROZEN KNOWLEDGE & RAG CORE™ — KRG2026.3
        │
        │ read-only governed interfaces
        ▼
POMELO™ · KIWI™ · GAA™ · ICFR · ESG · ECONOVA-S™
        │
        ▼
Adversarial review + replication + Human Gate™
```

## 3. Accounting & disclosure sources

### SEC Financial Statement Data Sets
Use for structured financial statement facts extracted from public-company XBRL filings.

NAAIL uses:
- company-year financial Digital Twins;
- accounting-ratio construction;
- disclosure and filing consistency tests;
- longitudinal accounting measurement;
- reproducible SEC-based assignments and research.

### SEC Financial Statement and Notes Data Sets
High-priority source for structured numeric and textual footnote/disclosure information.

Use for:
- accounting-policy and note analysis;
- audit-risk and CAM/KAM evidence;
- footnote NLP / RAG;
- disclosure-change detection;
- accounting-estimate and judgment research.

### filings.xbrl.org
Use for public ESEF/UKSEF/Inline XBRL filing access and European reporting Digital Twins.

Use for:
- European/Nordic issuer filings;
- IFRS-tagged evidence;
- cross-jurisdiction reporting comparisons;
- XBRL/iXBRL retrieval experiments.

## 4. Audit & assurance sources

### PCAOB AuditorSearch / Form AP
High-priority audit evidence source.

Use for:
- engagement-partner and audit-firm mapping;
- participating-firm networks;
- auditor-change and partner-level research;
- KIWI™ / GAA™ Digital Twins;
- audit-network and supervisory-attention studies.

### PCAOB inspection data
Use for public inspection findings, deficiency patterns, audit-quality benchmarking, recurrence/remediation analysis, and adversarial audit-review scenarios.

### SEC AAER
Use for accounting/auditing enforcement cases, misstatement/fraud patterns, failure-memory examples, forensic Digital Twins, and red-team benchmark design.

## 5. Governance and entity graph sources

### SEC Insider Transactions
Use Forms 3/4/5 for director, officer, and beneficial-owner transaction research.

### SEC Form 13F
Use institutional holdings for ownership concentration, institutional monitoring, governance, and ECONOVA-S™ research.

### SEC Form ADV / IAPD
Use public investment-adviser registrations and disciplinary/business information for governance, compliance, forensic, and financial-institution research.

### GLEIF
Use Legal Entity Identifiers, legal names, jurisdictions, addresses, and direct/ultimate parent relationships for entity resolution and GraphRAG.

Recommended graph role:

```text
LEI entity
  ↓
legal entity identity
  ↓
parent / ultimate parent
  ↓
issuer / filing / auditor / jurisdiction links
  ↓
NAAIL Entity Graph™
```

### Stanford Rock Center for Corporate Governance
Use as a public governance **research/knowledge source**, not as a bulk authoritative company dataset. Link and index only within applicable rights and source-specific terms.

## 6. Nordic free-data layer

### Statistics Sweden (SCB)
Use official Swedish statistics for company/economic context, industry comparisons, demographics, labor, prices, national accounts, and ESG/economic controls.

Where CC0 applies, preserve the source identifier and retrieval date even though attribution may not be legally required.

### Sveriges Riksbank
Use official Swedish interest-rate, exchange-rate, monetary and financial-system time series for ECONOVA-S™ and Nordic Digital Twins.

### Brønnøysundregistrene
Use Norwegian organization data and public organizational-role information for Nordic entity resolution, governance, and cross-border business-school research under applicable Norwegian open-data terms.

## 7. ESG / sustainability sources

### Climate TRACE
Use public emissions estimates and facility/asset-level information for ESG Digital Twins, emissions-risk benchmarking, transition-risk studies, and greenwashing/adversarial tests.

### World Bank
Use country, development, governance, climate/economic and macro indicators as contextual controls and external-validity data.

Dataset-specific rights must still be checked because individual World Bank datasets can carry source-specific terms.

## 8. Finance / economics sources

### Fama–French Data Library
Use factors and portfolio returns for ECONOVA-S™ research and replication. Treat as a research source; do not assume unrestricted redistribution rights for every downstream use.

### Damodaran data
Use valuation, equity-risk-premium, country-risk, industry beta, margin, multiple, and related research data subject to the source's stated use conditions. NAAIL should not resell or repackage the data as its own commercial dataset.

### FRED
Use macro/financial series selectively. Rights can vary by series, so NAAIL should maintain a series-level whitelist rather than mirroring FRED indiscriminately.

### World Bank
Use country-level economic and development indicators for cross-country controls, valuation context, sovereign/macro risk, and external-validation exercises.

## 9. Scientific evidence sources

### OpenAlex
High-priority scientific metadata source.

Use for:
- literature discovery;
- author/institution/topic networks;
- citation graphs;
- SDG/topic mapping;
- evidence-gap identification;
- scientific co-scientist literature validation.

OpenAlex metadata is treated as metadata evidence, not proof that a paper's claims are correct.

### Crossref
Use DOI and scholarly metadata for bibliographic identity, references, funder metadata, ORCID/ROR links where supplied, retraction/update metadata, and provenance reconciliation.

## 10. Evidence Passport™ for every source

Every admitted source record should preserve at least:

```text
source_id
source_name
source_url
source_authority_type
retrieval_timestamp
source_version_or_period
jurisdiction
raw_or_derived
raw_hash
transformation_chain
license_or_terms_status
redistribution_status
citation_requirement
source_specific_restrictions
knowledge_core_admission_status
validation_status
human_reviewer
```

## 11. Admission states

```text
DISCOVERED
  ↓
RIGHTS_REVIEWED
  ↓
PROVENANCE_VERIFIED
  ↓
SANDBOX_INGESTED
  ↓
VALIDATED
  ↓
ADMITTED_TO_KNOWLEDGE_RAG_CORE
  ↓
VERSIONED / RETIRED
```

No free/public source bypasses this sequence merely because access is free.

## 12. Source classes

### A. Authoritative public evidence
Examples: SEC filings, SEC enforcement releases, PCAOB public standards/data, official statistics, official registries.

### B. Open/public metadata and research resources
Examples: OpenAlex, Crossref, Fama–French, Damodaran, research-center publications.

### C. Contextual public data
Examples: World Bank, Climate TRACE, FRED, Riksbank.

The source class determines how strongly a downstream agent may rely on the information.

## 13. NAAIL routing

- **POMELO™:** SEC financials/notes, XBRL/ESEF, accounting treatment and disclosure evidence.
- **KIWI™:** PCAOB AuditorSearch, inspections, SEC filings, CAM/KAM evidence.
- **GAA™:** adversarial challenge using SEC/PCAOB evidence; it cannot rewrite admitted evidence.
- **ICFR Intelligence:** SEC filings, AAER, inspection evidence, control-risk context.
- **Forensic Intelligence:** AAER, insider transactions, Form ADV/IAPD, filing anomalies.
- **ESG Intelligence:** Climate TRACE, World Bank, issuer filings.
- **ECONOVA-S™:** Fama–French, Damodaran, FRED, World Bank, Riksbank, 13F, SEC filings.
- **Scientific Co-Scientist:** OpenAlex + Crossref for literature discovery, provenance, and evidence mapping.

## 14. Machine-readable governance

Canonical registry:
- `architecture/free_data_source_registry.json`

Validation:
- `tests/test_free_data_source_registry.py`

CI:
- `.github/workflows/naail_free_data_fabric.yml`

Related accounting/audit registries:
- `knowledge/accounting_audit_free_evidence_registry.json`
- `architecture/accounting_audit_open_source_registry.json`

## 15. Core invariants

```text
free_access_means_authoritative = false
free_access_means_unrestricted_redistribution = false
api_output_is_knowledge_without_validation = false
parser_output_is_authoritative = false
metadata_record_proves_scientific_claim = false
technology_tool_may_rewrite_knowledge_rag_core = false
source_terms_must_be_preserved = true
provenance_required = true
human_gate_required = true
```

## 16. Current claim boundary

**Adopted now:** source architecture, source registry, rights/provenance fields, Knowledge-Core admission states, routing to specialist NAAIL agents, machine-readable validation, and CI guard.

**Not claimed yet:** complete ingestion of every source, unrestricted redistribution rights, production GraphRAG indexing, complete historical coverage, commercial-data equivalence, or regulator/provider endorsement.

---

## Independent-source notice

NAAIL OpenLab™ is independent. SEC, PCAOB, XBRL International, GLEIF, Statistics Sweden, Sveriges Riksbank, Brønnøysundregistrene, World Bank, Climate TRACE, OpenAlex, Crossref, Fama–French, Damodaran, FRED, Stanford University/Rock Center, and other third parties remain independent sources. Inclusion identifies public/free evidence, metadata, research material, or technology inputs only and does not imply affiliation, endorsement, sponsorship, certification, or transfer of ownership.