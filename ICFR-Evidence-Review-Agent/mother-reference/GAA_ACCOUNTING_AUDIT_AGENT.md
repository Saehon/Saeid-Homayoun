# NAAIL GAA™ — General Adversarial Accounting & Audit Agent

**Platform:** NAAIL OpenLab™ — V2026.3 Multi-Agent Digital Twin  
**Agent:** GAA™ — General Adversarial Accounting & Audit Agent  
**Execution layer:** Technology Core™  
**Evidence layer:** Frozen Knowledge & RAG Core™ `KRG2026.3`  
**Status:** Architecture and evidence-source contract adopted; runtime execution remains gated

> **Authoritative evidence lives in the frozen Knowledge & RAG Core. GAA challenges conclusions, but cannot rewrite the core.**

## Purpose

GAA™ provides a reusable adversarial accounting-and-audit layer for NAAIL Digital Twins. It is designed to attack weak professional judgments, unsupported accounting conclusions, audit-risk assessments, CAM/KAM reasoning, ICFR classifications, fraud hypotheses, and empirical claims.

GAA is not a Generative Adversarial Network. The acronym here means **General Adversarial Accounting & Audit Agent**.

## Core architecture

```text
FROZEN KNOWLEDGE & RAG CORE™ — KRG2026.3
│
├── SEC EDGAR / XBRL evidence
├── SEC AAER enforcement evidence
├── PCAOB inspection evidence
├── PCAOB auditing standards / CAM requirements
├── NAAIL CAM/KAM evidence
├── NAAIL ICFR / controls evidence
├── Evidence Passport™
└── governed provenance + source hierarchy
        │
        │ read-only governed contract
        ▼
Adaptive Intelligence Fabric™
        │
        ▼
GAA™ — TECHNOLOGY CORE
│
├── Accounting Critic
├── Audit Critic
├── Fraud Falsifier
├── CAM/KAM Challenger
├── ICFR Challenger
├── Evidence Auditor
├── Independent Replicator
├── Standards Judge
└── Human Gate™
```

## Adopted free/public evidence sources

### SEC EDGAR / XBRL
Use for public filings, financial statements, structured facts, disclosures, company-year Digital Twins, accounting-policy evidence, and reproducible filing-based benchmarks.

Canonical public source: https://www.sec.gov/edgar/sec-api-documentation

### SEC Accounting and Auditing Enforcement Releases (AAER)
Use as adversarial failure-case evidence for accounting misstatements, fraud, disclosure failures, reporting failures, and accountant/auditor enforcement scenarios.

Canonical public source: https://www.sec.gov/enforcement-litigation/accounting-auditing-enforcement-releases

### PCAOB inspection reports and inspection data
Use as audit-quality and deficiency evidence for adversarial audit Digital Twins and benchmark construction.

Canonical public source: https://pcaobus.org/oversight/inspections/firm-inspection-reports

### PCAOB auditing standards / AS 3101 CAM requirements
Use as authoritative U.S. public-company audit-rule evidence for professional-judgment challenge, especially CAM identification, communication, and documentation.

Canonical public source: https://pcaobus.org/oversight/standards/auditing-standards/details/AS3101

## Open-source accounting/audit Technology-Core references

These projects may inform adapters, tools, benchmark design, or synthetic workflows. They are **not authoritative accounting standards and are not imported into the Knowledge & RAG Core as truth**.

- `Maxed-OSS/maxed-mcp` — accounting-oriented tool/MCP reference; Apache-2.0 license verified in upstream repository.
- `GAJETOso/financeskills` — finance/accounting skill-library reference; use only after version/license review for the exact dependency adopted.
- Existing NAAIL adversarial stack: Microsoft Agent Framework, DMAD, Debate-or-Vote, CAMEL, PyRIT, garak, and promptfoo.

Third-party code remains under its original license and terms. Prefer adapters and pinned external dependencies rather than copying upstream code into NAAIL.

## GAA adversarial protocol

```text
Professional / empirical claim
        ↓
Accounting Critic
        ↓
Audit Critic
        ↓
Fraud / alternative-explanation Falsifier
        ↓
CAM/KAM or ICFR Challenger when relevant
        ↓
Evidence Auditor
        ↓
Independent Replicator
        ↓
Standards Judge
        ↓
Human Gate™
```

The agents may disagree. Disagreement is evidence for review, not a reason to force consensus.

## Initial Digital Twin benchmark families

1. **Revenue recognition / cut-off** — filing facts and disclosures challenged against frozen evidence and assertions.
2. **Accounting fraud / misstatement** — AAER-derived patterns converted into synthetic, non-identifying training cases.
3. **Audit deficiency** — PCAOB inspection findings converted into controlled synthetic audit-review scenarios.
4. **CAM challenge** — CAM reasoning and communication assessed against AS 3101 and NAAIL KIWI™ metrics.
5. **ICFR challenge** — control-deficiency classification attacked for scope, severity, evidence sufficiency, contradictory evidence, and escalation.

Public regulatory material may be used only within its applicable legal/terms constraints. NAAIL synthetic cases should avoid implying regulator endorsement or reproducing restricted third-party datasets.

## GAA invariants

```text
gaa_runs_in_technology_core = true
gaa_may_read_governed_evidence = true
gaa_may_challenge_professional_judgment = true
gaa_may_request_more_retrieval = true
gaa_may_request_falsification = true
gaa_may_request_replication = true

gaa_may_modify_knowledge_rag_core = false
gaa_may_rewrite_pcaob_rules = false
gaa_may_rewrite_sec_evidence = false
gaa_may_change_graphrag_semantics = false
gaa_may_change_benchmark_gold = false
gaa_may_bypass_human_gate = false

agent_consensus_is_truth = false
majority_vote_is_truth = false
statistical_significance_is_discovery = false
predictive_accuracy_is_causality = false
human_gate_required = true
```

## Relationship to NAAIL specialist families

- **KIWI™:** CAM/KAM challenge, RPA/AA/EG/PS/DS/DIST, contradictory evidence, independent audit-review simulation.
- **POMELO™ / VERA™:** accounting-treatment challenge, evidence verification, professional-judgment stress test, Decision DAG review.
- **ICFR Intelligence:** deficiency classification, severity, account/entity-level scope, remediation persistence, contradictory evidence.
- **Forensic Intelligence:** fraud hypotheses, alternative explanations, evidence gaps, enforcement-pattern simulations.
- **ECONOVA-S™:** accounting/finance hypotheses, empirical falsification and replication where filings and market/economic data intersect.

## Machine-readable governance

Evidence/source registry:
- `knowledge/accounting_audit_free_evidence_registry.json`

Validation:
- `tests/test_gaa_accounting_audit_registry.py`

CI:
- `.github/workflows/naail_gaa_accounting_audit.yml`

Parent adversarial architecture:
- `ADVERSARIAL_INTELLIGENCE_FABRIC.md`

Frozen core invariant:
- `FROZEN_KNOWLEDGE_RAG_CORE_INVARIANT.md`

## Current claim boundary

**Adopted now:** GAA architecture, role definitions, public evidence-source registry, Digital Twin benchmark design, Technology-Core separation, and CI validation contract.

**Not claimed yet:** complete ingestion of SEC/PCAOB corpora, production GraphRAG indexing, executed GAA provider runs, superiority over human auditors, production deployment, marketplace certification, or regulator endorsement.

---

## Independent-project notice

NAAIL OpenLab™ is independent. SEC, PCAOB, GitHub projects, vendors, firms, and other third parties referenced here are sources, regulators, technology projects, research inputs, or benchmark targets only. Their mention does not imply affiliation, endorsement, certification, sponsorship, or transfer of ownership.