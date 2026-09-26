# NAAIL OpenLab™ — Open-Source Accounting & Audit Pack

**Platform:** NAAIL OpenLab™ — V2026.3 Multi-Agent Digital Twin  
**Parent agent:** GAA™ — General Adversarial Accounting & Audit Agent  
**Boundary:** Frozen Knowledge & RAG Core™ `KRG2026.3` remains protected; external software belongs to the Technology Core™ or ingestion/tooling perimeter.  
**Status:** Curated external integrations/references adopted; runtime execution remains gated.

> **Use open-source software as replaceable tooling. Keep authoritative accounting/audit meaning, provenance, ontology, standards mappings, and evidence governance in the frozen Knowledge & RAG Core.**

## Adopted free/open-source repositories

| Repository | Verified license | NAAIL role | State | Code copied into NAAIL? |
|---|---|---|---|---|
| `Stanford-Advanced-FinTech-Lab-SAFTL/stanford-edgar-filings-dataset` | MIT | SEC/EDGAR filing parser and layout-faithful ingestion reference for Digital Twin evidence pipelines | `ADOPT_INGESTION_REFERENCE` | No |
| `Maxed-OSS/maxed-mcp` | Apache-2.0 | Agent-callable deterministic accounting/MCP tools | `ADOPT_ACCOUNTING_TOOL_REFERENCE` | No |
| `FoundrySoftHQ/agent-for-accounting` | MIT | Reconciliation, close workflow, exception/human-decision benchmark reference | `ADOPT_RECONCILIATION_REFERENCE` | No |
| `cynco-labs/ai-accounting-skills` | MIT | Agent-native accounting skills, bookkeeping hard gates, review-oriented workflow reference | `ADOPT_SKILL_REFERENCE` | No |
| `johnkozan/clawcounting` | MIT | Deterministic double-entry accounting engine, immutable journal, agent-facing accounting primitives | `ADOPT_LEDGER_REFERENCE` | No |
| `esploro-group/closegate` | Apache-2.0 | Finance-control policy gate, segregation-of-duties, HITL approval, append-only audit log, adversarial evaluation reference | `ADOPT_CONTROL_GATE_REFERENCE` | No |

## Why these six

### 1. Stanford EDGAR Filings Dataset parser

Repository: `https://github.com/Stanford-Advanced-FinTech-Lab-SAFTL/stanford-edgar-filings-dataset`

Use in NAAIL:
- convert heterogeneous SEC filings into model-friendly structured text;
- preserve tables/layout cues for accounting and audit reasoning;
- support SEC-filing Digital Twins and reproducible evidence retrieval;
- feed a governed ingestion pipeline before evidence is admitted to the Knowledge & RAG Core.

**Boundary rule:** the parser is Technology Core / ingestion tooling. Parsed output is not automatically authoritative. Before admission to the Knowledge & RAG Core it must retain filing identity, source URL/accession, hash/provenance, filing date/form, transformation metadata, and validation status.

### 2. Maxed MCP

Repository: `https://github.com/Maxed-OSS/maxed-mcp`

Use in NAAIL:
- deterministic accounting utilities callable by agents;
- accounting document / money-math / validation tool patterns;
- MCP-oriented interface design for POMELO™, GAA™, and accounting Digital Twins.

### 3. Agent for Accounting

Repository: `https://github.com/FoundrySoftHQ/agent-for-accounting`

Use in NAAIL:
- bank-to-ledger reconciliation benchmark;
- exception routing and human-decision workflow;
- close/checklist patterns;
- tests where GAA challenges reconciliation conclusions and unresolved lines.

### 4. AI Accounting Skills

Repository: `https://github.com/cynco-labs/ai-accounting-skills`

Use in NAAIL:
- skill structure for intake, journals, trial-balance construction, reconciliation, and review;
- hard-gate patterns that reduce fabricated accounting outputs;
- education/simulation references for Student Agent Academy scenarios.

### 5. ClawCounting

Repository: `https://github.com/johnkozan/clawcounting`

Use in NAAIL:
- deterministic double-entry ledger primitives;
- balanced-entry invariant testing;
- immutable journal and correction-by-reversal patterns;
- controlled ledger Digital Twin substrate for GAA falsification cases.

### 6. closegate

Repository: `https://github.com/esploro-group/closegate`

Use in NAAIL:
- policy chokepoint between autonomous agents and financial actions;
- segregation-of-duties controls;
- human-in-the-loop approval envelopes;
- tamper-aware/append-only audit-log patterns;
- adversarial robustness evaluation for close/reconciliation/AP workflows.

## Canonical integration architecture

```text
AUTHORITATIVE / GOVERNED EVIDENCE
SEC EDGAR · SEC AAER · PCAOB · NAAIL validated evidence
                      │
                      ▼
FROZEN KNOWLEDGE & RAG CORE™ — KRG2026.3
                      │
              read-only contracts
                      │
                      ▼
Adaptive Intelligence Fabric™
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
   GAA™ Adversarial Layer   Accounting Tool Layer
          │                       │
   Critic / Falsifier       Stanford parser
   Evidence Auditor         Maxed MCP
   Replicator               Agent-for-Accounting
   Standards Judge          AI Accounting Skills
          │                 ClawCounting
          │                 closegate
          └───────────┬───────────┘
                      ▼
                 Human Gate™
```

## Integration policy

NAAIL adopts these repositories primarily by **reference, adapters, pinned dependencies, benchmark interfaces, or clean-room protocol implementations**. Third-party source code is not copied into NAAIL by default.

Before runtime activation, each repository must pass:

- license/NOTICE verification for the exact version or commit;
- dependency and vulnerability review;
- data privacy / data-use review;
- sandbox execution on synthetic Client XYZ data;
- frozen benchmark tests;
- reproducibility tests;
- failure logging to Failure Memory™;
- compatibility test with the frozen Knowledge & RAG Core boundary;
- Human Architecture Gate approval.

## Digital Twin use cases

### Revenue / cut-off
Stanford parser supplies filing context → GAA critic challenges accounting treatment → deterministic ledger engine checks entry logic → Evidence Auditor verifies filing provenance → Human Gate.

### Bank reconciliation
Agent-for-Accounting / accounting skill patterns generate reconciliation candidates → GAA searches unmatched/duplicate/timing errors → closegate-style policy gate prevents unauthorized posting → Human Gate.

### Journal-entry fraud
ClawCounting-style immutable ledger creates controlled entries → GAA Fraud Falsifier attacks unusual journals → Evidence Auditor traces source/evidence → Human Gate.

### Month-end close / ICFR
Accounting skill pipelines + closegate control patterns → GAA ICFR Challenger tests SoD, approvals, evidence completeness, and override risk → Human Gate.

## Non-negotiable boundary

```text
external_repo_is_authoritative_accounting_truth = false
external_repo_may_rewrite_knowledge_rag_core = false
parsed_output_is_authoritative_without_validation = false
agent_generated_journal_is_posted_without_gate = false
third_party_code_is_naail_owned = false
human_gate_required = true
```

## Machine-readable registry

See: `architecture/accounting_audit_open_source_registry.json`

Validation: `tests/test_accounting_audit_open_source_registry.py`

CI: `.github/workflows/naail_accounting_audit_open_source_registry.yml`

Parent GAA architecture: `GAA_ACCOUNTING_AUDIT_AGENT.md`

---

## Third-party notice

All named repositories remain independent upstream projects. Their names identify external open-source sources and do not imply partnership, endorsement, sponsorship, certification, or transfer of ownership. Each project remains governed by its own license and terms. NAAIL-specific architecture, adapters, evaluation contracts, Digital Twin cases, evidence governance, and Human Gate logic remain separate.