# NAAIL OpenLab™ — Frozen Knowledge & RAG Core Invariant

**Status:** Canonical architectural invariant  
**Effective date:** 14 September 2026  
**Applies to:** NAAIL OpenLab™, KIWI™, POMELO™, ECONOVA-S™, ESG Intelligence, ICFR Intelligence, Forensic Intelligence, education, marketplace, and scientific-discovery workflows

> **The Knowledge & RAG Core is fixed as the durable semantic foundation. The Technology Core may evolve, but it must never silently rewrite, merge with, or redefine the Knowledge & RAG Core.**

## 1. Non-negotiable separation

```text
                         NAAIL OpenLab™
                               │
               ┌───────────────┴───────────────┐
               │                               │
      KNOWLEDGE & RAG CORE™              TECHNOLOGY CORE™
      Canonical / durable                Replaceable / fast-moving
      Evidence + semantics               Models + runtimes + tooling
               │                               │
               └──── Adaptive Intelligence ────┘
                         Fabric™
                               │
                       Human Gate™
```

The two cores are related but **not interchangeable**.

The Technology Core may read from and operate on the Knowledge & RAG Core through governed contracts. It may not automatically change the canonical knowledge, evidence meaning, ontology, graph semantics, scientific rules, or professional rules.

## 2. Frozen Knowledge & RAG Core™

The frozen core contains the durable professional, scientific, and evidence meaning of NAAIL.

### Canonical professional knowledge
- accounting and financial-reporting concepts;
- auditing and assurance concepts;
- IFRS / accounting-standard mappings;
- PCAOB / audit-regulatory mappings;
- CAM/KAM structures;
- ICFR and controls logic;
- ESG / sustainability concepts;
- forensic and fraud concepts;
- finance, economics, valuation, and asset-pricing concepts;
- assertions, risks, procedures, evidence, judgments, and escalation logic.

### Canonical scientific knowledge
- theory and literature logic;
- construct definitions;
- causal DAGs;
- identification rules;
- econometric and statistical principles;
- robustness and falsification requirements;
- temporal / out-of-sample validation rules;
- replication requirements;
- Chain-of-Evidence;
- Human Gate requirements.

### Canonical RAG / GraphRAG knowledge structures
- approved evidence sources and source hierarchy;
- evidence objects and Evidence Passport™ semantics;
- canonical document / evidence identifiers;
- knowledge ontology;
- knowledge-graph entity and relation semantics;
- GraphRAG schema and semantic relationships;
- professional taxonomy;
- benchmark definitions and gold labels;
- Variable DNA™;
- Failure Memory™;
- professional decision schemas;
- rights / licensing / provenance metadata.

These canonical semantic objects belong to the Knowledge & RAG Core even when a replaceable technology is used to index, retrieve, embed, rank, cache, or display them.

## 3. Replaceable Technology Core™

The Technology Core contains execution technology only, including:

- foundation and multimodal models;
- OpenAI / Google / Anthropic / Microsoft / local model adapters;
- agent SDKs and runtimes;
- orchestration frameworks;
- model routers;
- MCP / A2A implementations;
- tool-calling systems;
- code-execution sandboxes;
- embedding models;
- vector-search engines;
- graph-database engines;
- search / ranking algorithms;
- retrieval engines;
- caches and indexes;
- memory implementations;
- observability and tracing;
- evaluation tooling;
- UI / marketplace adapters;
- cloud / local deployment infrastructure;
- authentication and secrets infrastructure.

Technology may change without changing the canonical meaning of the Knowledge & RAG Core.

## 4. Critical RAG boundary

NAAIL distinguishes **RAG knowledge** from **RAG technology**.

```text
RAG KNOWLEDGE — FROZEN / GOVERNED
---------------------------------
Evidence corpus definition
Canonical source IDs
Ontology
Graph semantics
Entity / relation definitions
Provenance
Rights metadata
Evidence hierarchy
Benchmark gold definitions
Professional meaning
Scientific meaning

RAG TECHNOLOGY — REPLACEABLE
----------------------------
Embedding model
Vector database
Graph database engine
Retriever
Reranker
Chunk index
Cache
Query planner
Agent runtime
LLM
Cloud provider
```

Changing an embedding model, vector database, GraphRAG engine, LLM, agent framework, or cloud provider must not silently alter the canonical evidence set or knowledge semantics.

## 5. Read-only-by-default rule

Technology Core access to canonical knowledge should be **read-only by default**.

Any write to the Knowledge & RAG Core requires a governed knowledge-update process.

```text
Technology output
      ↓
Proposed knowledge change
      ↓
Evidence / provenance review
      ↓
Ontology / schema impact review
      ↓
Regression test
      ↓
Human Knowledge Gate
      ↓
Versioned Knowledge Core update
```

No autonomous agent, model, vendor SDK, retrieval engine, or marketplace adapter may bypass this process.

## 6. Vendor-change firewall

```text
OpenAI / Google / Claude / Microsoft / Local update
                     ↓
               Technology Radar
                     ↓
              Sandbox evaluation
                     ↓
             Frozen benchmark test
                     ↓
        Security / rights / cost review
                     ↓
       Compatibility with frozen Knowledge
               & RAG Core
                     ↓
            Human Architecture Gate
                     ↓
       Technology adapter may be updated
```

The Knowledge & RAG Core remains unchanged unless a separate knowledge-governance trigger exists.

## 7. Permitted Knowledge & RAG Core change triggers

The frozen core is **stable, not permanently immutable**. It changes only through governed evidence-based updates such as:

- authoritative standard or regulatory change;
- validated peer-reviewed research;
- verified correction to an ontology or mapping;
- approved benchmark revision;
- reproducible evidence that an existing knowledge rule is wrong or incomplete;
- documented professional-practice change;
- Human Knowledge Gate approval.

A new GPT, Gemini, Claude, Microsoft model, SDK, framework, retriever, vector database, or graph engine is **not** a knowledge-change trigger.

## 8. Independent versioning

```text
Knowledge & RAG Core:  KRG2026.3
Technology Core:       T2026.9
Platform Release:      NAAIL v0.2.4
```

Technology versions may change frequently while the Knowledge & RAG Core version remains fixed.

## 9. Regression requirement

Every Technology Core upgrade must pass regression tests showing that it does not silently change:

- source provenance;
- evidence identifiers;
- ontology semantics;
- graph relations;
- causal DAG definitions;
- professional-rule mappings;
- benchmark gold definitions;
- citation requirements;
- replication requirements;
- Human Gate rules.

If the technology produces different interpretations, those differences are treated as model/technology behavior to evaluate—not as automatic changes to canonical knowledge.

## 10. Permanent architectural invariants

```text
technology_core_may_rewrite_knowledge_core = false
technology_core_may_rewrite_rag_semantics = false
vendor_release_changes_canonical_knowledge = false
embedding_change_changes_evidence_meaning = false
vector_db_change_changes_ontology = false
llm_upgrade_changes_causal_DAG_automatically = false
agent_framework_bypasses_human_gate = false

knowledge_rag_core_governed = true
technology_core_replaceable = true
read_only_by_default = true
knowledge_write_requires_human_gate = true
independent_versioning_required = true
regression_test_before_technology_promotion = true
```

## 11. Canonical operating principle

> **NAAIL may continuously replace how it computes, retrieves, orchestrates, and serves intelligence. It must not silently replace what the evidence means, what the professional knowledge means, or what the scientific governance requires.**

This invariant overrides future architectural convenience. If a future vendor technology requires merging the Technology Core with the canonical Knowledge & RAG Core in a way that breaks this separation, that technology should not be adopted without an explicit architecture-governance decision and versioned migration.

---

**Independent-project notice:** external model and technology providers remain subject to their own licenses, terms, pricing, privacy, and release cycles. Their technologies may be evaluated or adopted as replaceable execution components but do not govern NAAIL's canonical professional or scientific knowledge.