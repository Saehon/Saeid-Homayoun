# NAAIL ESG & Sustainability Intelligence Lab™

**Platform:** NAAIL OpenLab™ — V2026.3 Multi-Agent Digital Twin  
**Specialist family:** ESG & Sustainability Intelligence™  
**Knowledge & RAG Core:** `KRG2026.3` — frozen and governed  
**Layer:** Standards mapping / ESG data / Carbon & Climate / SDGs / Sustainable Finance / ESG Assurance  
**Status:** Open-source and public-source architecture adopted; runtime integrations remain gated

> **NAAIL does not reproduce copyrighted ESRS, IFRS Sustainability / SASB, GRI, or other proprietary standards text. Canonical standards remain external authoritative sources. NAAIL stores governed metadata, mappings, version identifiers, evidence links, research annotations, and rights-cleared derived structures.**

## Purpose

The NAAIL ESG & Sustainability Intelligence Lab™ provides a research-safe architecture for sustainability reporting, carbon accounting, climate risk, SDG analytics, sustainable finance, ESG assurance, and digital sustainability reporting.

## Priority open-source projects and datasets

| Project / source | License / status | NAAIL role | Adoption |
|---|---|---|---|
| `EFRAG-EU/Digital-Template-to-XBRL-Converter` | MIT verified | Official EFRAG digital reporting tooling; VSME / XBRL / XBRL-JSON conversion and validation reference | `ADOPT_PRIORITY` |
| `os-climate/physrisk` | Apache-2.0 verified | Physical climate-risk modelling using public climate hazard data | `ADOPT_PRIORITY` |
| `Klimatbyran/garbo` | Apache-2.0 verified | Nordic company GHG extraction and validation from sustainability reports | `ADOPT_PRIORITY` |
| `open-sdg/open-sdg` | MIT verified | SDG indicator collection, publication, metadata and dashboard workflows | `ADOPT_SDG_REFERENCE` |
| `HiveGuard-AI/taxonomy4good` | MIT verified | ESG / EU Taxonomy / SDG / sustainability taxonomy and NLP mapping | `ADOPT_TAXONOMY_REFERENCE` |
| `AltioremLibrary/altiorem-data` | CC0-1.0 verified | Sustainability research metadata, ESG categories, SDGs and SASB sector-classification research support | `ADOPT_KNOWLEDGE_DATA_REFERENCE` |
| `OntoSustain/RSO` | license review required before code reuse | GRI / ESRS sustainability ontology and semantic mapping reference | `REFERENCE_LICENSE_REVIEW` |
| `Open-Earth-Foundation/OpenClimate` | source and data terms review required | Climate-action data graph / API reference for entities, targets and emissions | `REFERENCE_DATA_RIGHTS_REVIEW` |
| `owid/co2-data` | source-level data terms must be preserved | CO2 / GHG empirical research data and codebook | `ADOPT_DATA_REFERENCE_WITH_SOURCE_RIGHTS` |
| `owid/energy-data` | source-level data terms must be preserved | Energy, electricity mix, renewables and transition metrics | `ADOPT_DATA_REFERENCE_WITH_SOURCE_RIGHTS` |
| `mlco2/codecarbon` | license/version review required before vendoring | AI/computing carbon-footprint measurement | `ADOPT_REFERENCE_RUNTIME_GATED` |
| `SEI-LA-SDGs/SAPIENT` | license review required before code reuse | SDG and EU Taxonomy text/project mapping research reference | `SANDBOX_REFERENCE` |
| `SFObservatory/Data.SFO` | research data terms review required | Sustainable-finance survey and EU-investor research data | `ADOPT_RESEARCH_DATA_REFERENCE` |
| Open Sustainable Finance Taxonomy mappings | upstream/version/rights review required | TCFD / EBA / ISSB / sustainable-finance taxonomy mapping reference | `REFERENCE_MAPPING_LAYER` |

## Standards and authoritative-source policy

NAAIL may index and map the following domains, but must preserve canonical-source authority and copyright/licensing boundaries:

- **European Sustainability Reporting Standards (ESRS) / CSRD** — EFRAG / EU legal sources;
- **EU Taxonomy** — EU legal and delegated-act sources;
- **VSME** — EFRAG canonical source and official digital templates/tooling;
- **ISSB / IFRS S1 and IFRS S2** — IFRS Foundation canonical source;
- **SASB Standards** — IFRS Foundation canonical source; do not publicly reproduce copyrighted standard text without permission;
- **GRI Standards** — GRI canonical source; do not publicly reproduce protected standards text without permission;
- **UN Sustainable Development Goals (SDGs)** — UN canonical goals, indicators and metadata;
- **GHG / carbon accounting frameworks** — only rights-cleared/public metadata and mappings may be mirrored.

### Regulatory status gate

For every ESRS / EU sustainability rule used in professional or empirical work:

```text
check_current_legal_status = true
check_official_journal_or_authoritative_source = true
store_version_and_effective_date = true
supersede_previous_rule_automatically = false
human_knowledge_gate_required = true
```

A proposed or revised standard must not silently replace a currently effective rule in `KRG2026.3` merely because a draft, consultation paper, GitHub tool, vendor release, or news item exists.

## Canonical architecture

```text
AUTHORITATIVE / PUBLIC / RIGHTS-CLEARED SOURCES
EU / EFRAG + IFRS Foundation + GRI + UN SDGs
Climate / carbon / energy public datasets
        ↓
Rights + version + provenance review
        ↓
NAAIL Free Data Fabric™ + Evidence Passport™
        ↓
Frozen Knowledge & RAG Core™ — KRG2026.3
        ↓ read-only governed contract
ESG & SUSTAINABILITY INTELLIGENCE LAB™
        ├── ESRS / CSRD Agent
        ├── EU Taxonomy Agent
        ├── VSME / Digital Reporting Agent
        ├── ISSB / SASB Mapping Agent
        ├── GRI Mapping Agent
        ├── SDG Intelligence Agent
        ├── Carbon / GHG Accounting Agent
        ├── Climate Risk Agent
        ├── Sustainable Finance Agent
        └── ESG Assurance Agent
        ↓
Critic → Falsifier → Evidence Auditor → Replicator
        ↓
Human Gate™
```

## Core research/data capabilities

### Sustainability reporting and XBRL
- EFRAG digital templates and XBRL conversion;
- ESRS / VSME disclosure mapping;
- digital reporting validation;
- XBRL / XBRL-JSON transformation;
- entity-level disclosure completeness and consistency checks.

### Carbon and GHG
- Scope 1 / 2 / 3 research mappings where supported by rights-cleared evidence;
- corporate sustainability-report GHG extraction;
- country and sector emissions;
- energy-transition indicators;
- carbon-intensity and emissions-trend analytics;
- AI-compute carbon-footprint experiments.

### Climate risk
- physical-risk scenario analysis;
- asset / location hazard mapping;
- exposure, vulnerability and resilience research;
- climate-risk-to-accounting / valuation / audit linkage;
- temporal and scenario uncertainty logging.

### SDGs and sustainable finance
- SDG goal / target / indicator mapping;
- EU Taxonomy activity classification research;
- sustainability taxonomy NLP;
- sustainable-finance survey research;
- sector / topic / activity mapping;
- sustainability research evidence graph.

## ESG assurance integration

The ESG Assurance Agent must distinguish:

```text
authoritative_requirement
professional_guidance
academic_evidence
entity_disclosure
public_dataset
third_party_model_output
synthetic_digital_twin_evidence
```

No model-generated ESG classification, score, taxonomy mapping, emission estimate, or assurance conclusion becomes authoritative evidence without provenance and Human Gate review.

## Data and copyright invariants

```text
public_access_equals_public_domain = false
software_license_equals_data_license = false
standards_text_may_be_republished_by_default = false
third_party_esg_score_equals_ground_truth = false
estimated_emission_equals_reported_emission = false
sdg_mapping_equals_causal_impact = false
climate_scenario_equals_forecast = false
external_repo_may_modify_knowledge_rag_core = false
human_gate_required = true
```

## Relationship to NAAIL

- **POMELO™:** sustainability reporting, ESG assurance and professional judgment;
- **GAA™:** adversarial ESG/accounting/audit challenge;
- **KIWI™:** ESG-related CAM/KAM risk-procedure-evidence alignment;
- **ECONOVA-S™:** climate finance, valuation and sustainable-finance analysis;
- **Free Data Fabric™:** governed ESG/climate/SDG data acquisition;
- **ERP Digital Twin Lab™:** transaction/activity data for carbon and sustainability simulations;
- **Scientific Discovery Platform:** hypotheses, empirical tests, robustness, falsification and replication.

## Promotion gates

Before runtime promotion of any ESG/sustainability integration:

1. verify upstream repository/source and current version;
2. verify software license and separate data/standards rights;
3. preserve attribution and source-level terms;
4. record effective dates for regulatory/standards material;
5. pin dependencies and run security review;
6. test on synthetic or rights-cleared Client XYZ evidence;
7. create Evidence Passport™ and transformation lineage;
8. run standards/status checks and contradictory-evidence tests;
9. benchmark on frozen tasks and retain Failure Memory™;
10. require Human Architecture / Knowledge / Research Gate approval.

NAAIL OpenLab™ is independent. References to EFRAG, the European Union, IFRS Foundation, SASB, GRI, the United Nations, OS-Climate, Our World in Data, GitHub projects, universities, or other organizations do not imply affiliation, endorsement, certification, sponsorship, or ownership transfer.
