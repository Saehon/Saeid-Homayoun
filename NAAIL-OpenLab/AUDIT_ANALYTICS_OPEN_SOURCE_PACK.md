# NAAIL OpenLab™ — Audit Analytics Open-Source Pack

**Platform:** NAAIL OpenLab™ — V2026.3 Multi-Agent Digital Twin  
**Knowledge & RAG Core:** `KRG2026.3` — frozen and governed  
**Layer:** Technology / Research / Benchmark / Education  
**Status:** Curated external references adopted; runtime execution remains gated

> **NAAIL does not replicate or claim access to proprietary Audit Analytics data. This pack uses public GitHub projects, public regulatory data, synthetic benchmarks, and governed adapters.**

## Priority repositories

| Repository | License / status | NAAIL role | Adoption |
|---|---|---|---|
| `westland/auditanalytics` | No repository LICENSE file verified at adoption review | Audit Analytics code/data research reference; R-based audit analytics examples | `REFERENCE_ONLY_NO_CODE_COPY` |
| `cpahyungnamkim/internal-control-audit-analytics` | MIT verified | ICFR analytics, journal-entry testing, Benford, SOD, duplicate tests, control assessment | `ADOPT_TECHNOLOGY_REFERENCE` |
| `ajrngn/auditagent-bench` | MIT verified | Public ICFR benchmark for deficiency classification, control design and standards-citation evaluation | `ADOPT_BENCHMARK_REFERENCE` |
| `busera/applying_data_analysis_in_internal_audit` | MIT verified | Internal-audit analytics methodology, evidence-quality gates, synthetic examples and reproducibility | `ADOPT_METHODOLOGY_REFERENCE` |
| `EffortlessMetrics/xbrlkit` | AGPL-3.0 verified | XBRL/iXBRL/SEC validating processor and deterministic receipts; use isolated/reference-first | `REFERENCE_ISOLATED_AGPL` |
| `jonlinca/auditanalytics` | GPL-3.0; archived | Source for *Audit Analytics with R*; education/research reference | `REFERENCE_ARCHIVED_GPL` |

## Why these fit NAAIL

### Westland Audit Analytics
Use as a research reference for audit-data analytics workflows and educational comparison. Because no repository license file was verified, do not copy or redistribute code/data into NAAIL unless rights are clarified.

### Internal Control & Audit Analytics
Strong fit for GAA™, ICFR Intelligence and Student Agent Academy because it exposes auditable Python analytics for journal-entry testing and internal-control analysis. MIT-licensed upstream code may be reused subject to attribution/license requirements, but NAAIL still prefers adapters and pinned dependencies.

### AuditAgent Bench
Use as an external benchmark for ICFR reasoning, deficiency classification, control design assessment and standards citation. Benchmark scores are evidence of task performance only; they are not proof of audit competence or regulator acceptance.

### Applying Data Analysis in Internal Audit
Use for translating audit objectives, risks and controls into reproducible analytical questions, evidence-quality gates and communication protocols.

### xbrlkit
Use for XBRL/iXBRL validation concepts, SEC profile packs and deterministic receipts. Because the upstream license is AGPL-3.0, keep it isolated/reference-first unless NAAIL intentionally accepts the corresponding AGPL obligations.

### Audit Analytics with R
Useful for education and research comparison, but the repository is archived and GPL-3.0. Keep it as an external reference rather than vendoring it into the main NAAIL codebase.

## Canonical NAAIL audit-analytics architecture

```text
PUBLIC / GOVERNED EVIDENCE
SEC EDGAR + XBRL + SEC Notes + AAER + PCAOB + Form AP
        ↓
NAAIL Free Data Fabric™ + Evidence Passport™
        ↓
Frozen Knowledge & RAG Core™ — KRG2026.3
        ↓ read-only governed contract
AUDIT ANALYTICS TECHNOLOGY / BENCHMARK LAYER
        ├── Audit Analytics research references
        ├── ICFR / control analytics
        ├── Journal-entry tests
        ├── XBRL validation
        ├── AuditAgent benchmark
        └── Internal-audit methodology
        ↓
KIWI™ + GAA™ + ICFR Intelligence + POMELO™ + Forensic Intelligence
        ↓
Critic → Falsifier → Evidence Auditor → Replicator
        ↓
Human Gate™
```

## Initial analytics library for Client XYZ

NAAIL should benchmark at least:

1. journal-entry anomaly tests;
2. Benford / digit-distribution diagnostics;
3. duplicate and near-duplicate transactions;
4. segregation-of-duties conflicts;
5. unusual manual entries and period-end postings;
6. revenue cut-off and reversal patterns;
7. AP three-way-match / duplicate-payment exceptions;
8. AR aging, allowance and reconciliation anomalies;
9. ICFR deficiency classification and contradictory-evidence tests;
10. XBRL/iXBRL validation and filing-to-ledger reconciliation;
11. CAM/KAM risk-to-procedure alignment;
12. audit evidence coverage and traceability.

## Permanent boundaries

```text
proprietary_audit_analytics_data_is_included = false
external_repo_is_authoritative_audit_truth = false
external_repo_may_modify_knowledge_rag_core = false
benchmark_score_equals_audit_competence = false
agent_output_is_audit_evidence_without_provenance = false
license_unknown_means_code_copy_allowed = false
agpl_project_is_vendored_by_default = false
human_gate_required = true
```

## Promotion gates

Before runtime use: verify exact repository/ref, license, dependencies, security, privacy, data rights, synthetic Client XYZ execution, frozen benchmark results, reproducibility, Failure Memory™, Knowledge/RAG boundary compliance and Human Architecture Gate approval.

## Relationship to existing NAAIL modules

- **Free Data Fabric™:** authoritative/public evidence acquisition and provenance.
- **GAA™:** adversarial accounting/audit challenge.
- **KIWI™:** CAM/KAM analytics and risk-procedure-evidence alignment.
- **ICFR Intelligence:** controls, deficiencies and remediation.
- **ERP Digital Twin Lab™:** transaction/process generation for synthetic Client XYZ.
- **POMELO™ / VERA™:** evidence verification and professional judgment.

## Publication synchronization

**GitHub:** public canonical research/documentation source.  
**Google Drive:** working mirror maintained in the `NAAIL OpenLab` folder.  
**Sync recorded:** 2026-09-14.

The Google Drive mirror is a working copy and does not change the repository's licensing, provenance, or Knowledge/RAG Core governance rules.

NAAIL OpenLab™ is independent. References to Audit Analytics, universities, regulators and GitHub projects do not imply affiliation, endorsement, certification or ownership transfer.
