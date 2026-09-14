# NAAIL OpenLab™ — Technology Radar Status

**Platform:** NAAIL OpenLab™  
**Knowledge & RAG Core:** `KRG2026.3`  
**Technology Core design state:** `T2026.9-design`  
**Status:** Public architecture/evaluation registry — not a claim of production integration

> **Knowledge and RAG semantics stay governed and stable. Technology stays replaceable.**

## Frozen core boundary

NAAIL maintains two independently governed cores:

- **Knowledge & RAG Core™** — accounting, auditing, assurance, CAM/KAM, ICFR, ESG, finance/economics, theory, causal DAGs, identification, evidence rules, source hierarchy, provenance, ontology, GraphRAG semantics, benchmark definitions, replication, Chain-of-Evidence, Evidence Passport™, and Human Gate™.
- **Technology Core™** — foundation models, agent SDKs, orchestration, embedding models, vector/graph engines, retrievers, rerankers, caches, indexes, MCP/A2A implementations, memory implementations, tool calling, sandboxes, observability, evaluation tooling, UI adapters, deployment infrastructure, and the **NAAIL Adversarial Intelligence Fabric™**.

The **Adaptive Intelligence Fabric™** connects them so technology can change without silently changing scientific, professional, or evidence meaning.

**Canonical invariant:** Technology Core components may read and operate on the Knowledge & RAG Core through governed contracts, but they may not silently rewrite, merge with, or redefine it.

Read the frozen invariant: [FROZEN_KNOWLEDGE_RAG_CORE_INVARIANT.md](./FROZEN_KNOWLEDGE_RAG_CORE_INVARIANT.md)

## Current provider radar

| Provider / technology | Current NAAIL state | Candidate role | Production claim? |
|---|---|---|---|
| **OpenAI Agents SDK** | EVALUATE | orchestration, handoffs, guardrails, tracing, sandbox workflows | No |
| **Google ADK** | EVALUATE | multi-agent workflows, evaluation, interoperability, sandboxed execution | No |
| **Gemini CLI** | EVALUATE | repository/developer workflow experiments and low-cost prototyping | No |
| **Anthropic Claude Agent SDK** | EVALUATE | evidence workspace, long-document/repository review, subagents, permissions | No |
| **MCP** | EVALUATE | provider-neutral tool/evidence connectivity | No |
| **Microsoft Agent Framework** | ADOPT_ARCHITECTURE / runtime gated | orchestration reference for durable adversarial and enterprise workflows | No |
| **A2A** | EVALUATE | cross-agent interoperability | No |
| **Local / open models** | WATCH / EVALUATE | research baseline, privacy-sensitive and cost-controlled experiments | No |

No row above means a provider is endorsed, integrated in production, approved for marketplace release, or superior to another provider.

## Adversarial Intelligence Fabric™

NAAIL now adopts a governed adversarial layer inside the **Technology Core only**.

### Scientific adversarial stack
- **DMAD** — `ADOPT_PROTOCOL` for diverse multi-agent debate;
- **Debate-or-Vote** — `ADOPT_BENCHMARK_PROTOCOL` for testing whether debate or voting is superior under frozen cases;
- **CAMEL** — `SANDBOX_REFERENCE` for role diversity and multi-agent simulation;
- **NAAIL Independent Reviewer protocol** — independent initial judgments before peer exposure when independence is material.

### Security red-team stack
- **Microsoft PyRIT** — `ADOPT_RED_TEAM_REFERENCE`;
- **NVIDIA garak** — `ADOPT_RED_TEAM_REFERENCE`;
- **promptfoo** — `ADOPT_EVAL_REFERENCE` for provider-neutral evaluation and red-team CI.

### NAAIL adversarial team

```text
Proposer
  ↓
Critic
  ↓
Defender
  ↓
Falsifier
  ↓
Replicator
  ↓
Evidence Auditor
  ↓
Judge
  ↓
Human Gate™
```

Architecture adoption does **not** claim that these upstream packages have already been installed, executed, benchmarked, certified, or deployed in production.

Canonical references:
- [NAAIL Adversarial Intelligence Fabric™](./ADVERSARIAL_INTELLIGENCE_FABRIC.md)
- [Adversarial Agent Registry](./architecture/adversarial_agent_registry.json)
- [Adversarial Registry Test](./tests/test_adversarial_agent_registry.py)

## Technology lifecycle

```text
WATCH
  ↓
EVALUATE
  ↓
SANDBOX
  ↓
ADOPT
  ↓
REPLACE / RETIRE
```

Promotion requires frozen benchmark evidence rather than a successful demonstration alone.

## Promotion gates

A technology may move from EVALUATE toward SANDBOX/ADOPT only after review of:

- license / terms compatibility;
- privacy and data-use rules;
- security and permissions;
- evidence accuracy;
- citation/provenance fidelity;
- hallucination / unsupported-claim behavior;
- tool-use reliability;
- reproducibility;
- latency;
- token / compute / monetary cost;
- observability and traceability;
- portability / vendor lock-in risk;
- Human Gate compatibility;
- regression against frozen NAAIL benchmarks;
- compatibility with the frozen Knowledge & RAG Core.

## Knowledge & RAG Core firewall

A provider, model, embedding, vector database, graph engine, retriever, adversarial framework, red-team tool, or agent-framework upgrade must never automatically change:

- canonical evidence sources or source IDs;
- professional standards mappings;
- ontology semantics;
- GraphRAG entity/relation semantics;
- causal DAGs;
- construct definitions;
- benchmark gold definitions;
- evidence hierarchy;
- replication requirements;
- falsification requirements;
- Human Gate rules.

```text
technology_core_may_rewrite_knowledge_rag_core = false
adversarial_agent_may_modify_knowledge_rag_core = false
red_team_tool_may_modify_knowledge_rag_core = false
provider_release_changes_scientific_truth = false
embedding_change_changes_evidence_meaning = false
vector_db_change_changes_ontology = false
model_upgrade_changes_causal_DAG_automatically = false
new_framework_bypasses_human_gate = false
new_model_bypasses_replication = false
optimize_for_vendor_lock_in = false
```

## Update cadence

### Monthly technology scan
Review material changes from OpenAI, Google, Anthropic/Claude, Microsoft, selected open-model ecosystems, and adopted adversarial/red-team upstream projects. Classify each as WATCH / EVALUATE / SANDBOX / ADOPT / RETIRE.

### Quarterly benchmark review
Rerun selected frozen NAAIL cases when executable adapters exist and compare evidence quality, adversarial error discovery, reliability, reproducibility, cost, latency, red-team findings, and human-review acceptance.

### Knowledge & RAG Core updates
Update separately and only through governed evidence-based change control: authoritative standards/regulation, validated research, verified ontology corrections, benchmark revisions, or other approved knowledge-governance decisions.

A vendor technology release is not a Knowledge & RAG Core update trigger.

## Canonical references

- [Frozen Knowledge & RAG Core Invariant](./FROZEN_KNOWLEDGE_RAG_CORE_INVARIANT.md)
- [NAAIL Adversarial Intelligence Fabric™](./ADVERSARIAL_INTELLIGENCE_FABRIC.md)
- [Knowledge Core, Technology Core & AI Technology Radar](./CORE_ARCHITECTURE_AND_TECHNOLOGY_RADAR.md)
- [Public Reference Architecture](./ARCHITECTURE.md)
- [Scientific Discovery Platform](./SCIENTIFIC_DISCOVERY_PLATFORM.md)
- [Scientific Discovery Contract](./SCIENTIFIC_DISCOVERY_CONTRACT.md)
- [Business-School Open Agent Pack](./BUSINESS_SCHOOL_OPEN_AGENT_PACK.md)
- [Marketplace Edition](./MARKETPLACE_EDITION.md)

## Independent-project notice

OpenAI, Google, Anthropic, Microsoft, CAMEL-AI, NVIDIA, promptfoo, DMAD, Debate-or-Vote, and other third-party names are referenced as technology providers, open-source projects, interoperability targets, research inputs, or comparison benchmarks only. Their inclusion does not imply partnership, endorsement, certification, sponsorship, marketplace approval, production integration, or transfer of ownership. Third-party code remains subject to its own license and terms.
