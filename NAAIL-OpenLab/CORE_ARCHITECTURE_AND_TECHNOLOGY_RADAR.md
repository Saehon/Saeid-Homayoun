# NAAIL OpenLab™ — Knowledge Core, Technology Core & AI Technology Radar

**Platform:** NAAIL OpenLab™ — V2026.3 Multi-Agent Digital Twin  
**Status:** Canonical core-separation and technology-refresh policy  
**Date:** 14 September 2026

> **Knowledge should be durable. Technology should be replaceable. Evidence and human governance should survive both.**

## 1. Architectural rule

NAAIL OpenLab separates the platform into two independently governed cores connected through the **Adaptive Intelligence Fabric™**.

```text
                    NAAIL OpenLab™
                          │
        ┌─────────────────┴─────────────────┐
        │                                   │
  KNOWLEDGE CORE™                    TECHNOLOGY CORE™
  Slow-moving                         Fast-moving
  Domain/science governed             Engineering/vendor governed
        │                                   │
        └──────── Adaptive Intelligence ────┘
                    Fabric™
                          │
                 Evidence + Human Gate
```

The Knowledge Core must never be silently rewritten because a model, SDK, cloud platform, agent runtime, or provider changes.

The Technology Core must never become permanently tied to a single provider.

---

## 2. Knowledge Core™ — durable professional and scientific meaning

The Knowledge Core contains the parts of NAAIL that should remain stable across model generations and vendors.

### Professional knowledge
- accounting and financial-reporting concepts;
- auditing and assurance concepts;
- CAM/KAM structures;
- ICFR and controls logic;
- ESG / sustainability concepts;
- forensic and fraud concepts;
- finance, economics, valuation, and asset-pricing concepts;
- professional assertions, risks, procedures, evidence, judgments, and escalation logic.

### Scientific knowledge
- theory;
- literature validation;
- construct definitions;
- causal DAGs;
- identification strategies;
- econometrics and statistical inference;
- ML/AI evaluation rules;
- robustness and falsification;
- temporal / out-of-sample validation;
- replication requirements;
- Chain-of-Evidence;
- Human Gate requirements.

### Evidence structures
- Evidence Passport™;
- Variable DNA™;
- provenance rules;
- source hierarchy;
- rights and licensing rules;
- Knowledge Graph / GraphRAG ontology;
- benchmark definitions;
- Failure Memory™;
- professional decision schemas.

### Knowledge Core change triggers
The Knowledge Core changes only when justified by evidence such as:
- new or amended standards / regulation;
- high-quality peer-reviewed research;
- validated benchmark findings;
- documented professional-practice change;
- corrected ontology / taxonomy;
- reproducible scientific evidence;
- approved governance decision.

A vendor model release is **not** by itself a reason to change the Knowledge Core.

---

## 3. Technology Core™ — replaceable AI and engineering capability

The Technology Core contains components that may change rapidly:

- foundation models and multimodal models;
- agent SDKs and runtimes;
- orchestration frameworks;
- model routers;
- MCP / A2A implementations;
- tool-calling systems;
- code-execution sandboxes;
- retrieval / RAG / GraphRAG implementations;
- memory systems;
- vector / graph stores;
- observability and tracing;
- evaluation tooling;
- cloud deployment;
- local/open-model backends;
- UI / marketplace adapters;
- authentication / secrets infrastructure.

Every Technology Core component must sit behind a NAAIL adapter or contract where feasible.

---

## 4. Four-provider Technology Radar — September 2026

The Technology Radar tracks external capabilities that may improve NAAIL. Inclusion means **evaluate**, not automatically adopt.

### OpenAI
Current relevant capabilities include:
- OpenAI Agents SDK;
- agents-as-tools and handoffs;
- guardrails;
- sessions;
- human-in-the-loop patterns;
- sandbox agents;
- built-in tracing;
- MCP server tools;
- Responses API integration.

**NAAIL candidate uses:** orchestrator baseline, specialist handoffs, guardrail experiments, trace capture, sandbox research workflows, provider-comparison benchmarks.

Official references:
- https://openai.github.io/openai-agents-python/
- https://openai.github.io/openai-agents-python/tracing/
- https://openai.github.io/openai-agents-python/mcp/

### Google AI
Current relevant capabilities include:
- Agent Development Kit (ADK);
- Agents CLI;
- automated evaluation workflows;
- MCP documentation connectivity;
- agent runtime / sandboxed code execution;
- multi-agent examples and tooling;
- A2A interoperability ecosystem;
- Gemini / Google Cloud deployment paths.

**NAAIL candidate uses:** ADK workflow experiments, evaluation automation, sandboxed empirical analysis, repository development, A2A tests, provider-neutral benchmarking.

Official references:
- https://google.github.io/adk-docs/
- https://google.github.io/adk-docs/tutorials/coding-with-ai/
- https://google.github.io/agents-cli/guide/getting-started/

### Anthropic / Claude
Current relevant capabilities include:
- Claude Agent SDK for Python / TypeScript;
- Claude Code agentic development workflows;
- MCP integration;
- subagents;
- sessions;
- permissions and tool-use controls;
- long-form evidence / repository workflows.

**NAAIL candidate uses:** evidence-workspace agents, repository-review agents, long-document critique, permissioned tool workflows, MCP-based professional evidence access, independent AI-to-AI reviewer.

Official references:
- https://github.com/anthropics/claude-agent-sdk-python
- https://github.com/anthropics/claude-agent-sdk-typescript
- https://github.com/anthropics/claude-code

### Microsoft AI
Current relevant capabilities include:
- Microsoft Agent Framework;
- graph-based workflows;
- agents inside workflows;
- checkpointing / resuming;
- human-in-the-loop;
- middleware;
- RAG / tools / memory;
- Azure Foundry integration;
- durable enterprise hosting patterns.

**NAAIL candidate uses:** enterprise workflow orchestration, durable audit/research workflows, checkpointed Human Gates, identity/governance patterns, Microsoft 365 / enterprise distribution preparation.

Official references:
- https://learn.microsoft.com/en-us/agent-framework/
- https://learn.microsoft.com/en-us/agent-framework/concepts/workflows/

---

## 5. Technology adoption states

Every external technology should receive one of five NAAIL statuses:

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

### WATCH
Interesting development; no NAAIL integration claim.

### EVALUATE
Architecture, license, security, privacy, cost, interoperability, and scientific fit are reviewed.

### SANDBOX
Tested only on synthetic/frozen cases with no production dependency.

### ADOPT
Allowed behind a governed NAAIL adapter after passing evaluation gates.

### REPLACE / RETIRE
Removed when obsolete, unsafe, too costly, insufficiently reproducible, license-incompatible, or materially inferior to a tested alternative.

---

## 6. Technology adoption gates

A new model, SDK, agent framework, or provider capability must not enter the adopted Technology Core merely because it is new.

Required checks should include:

- capability improvement;
- license / terms compatibility;
- data-use and privacy review;
- security / permissions review;
- reproducibility;
- evidence fidelity;
- citation / provenance behavior;
- hallucination / failure behavior;
- tool-use reliability;
- latency;
- compute / token / monetary cost;
- portability;
- observability;
- human-control compatibility;
- regression against frozen NAAIL benchmarks.

For scientific workflows, the new technology must not weaken:
- literature validation;
- causal DAG governance;
- data provenance;
- robustness;
- falsification;
- replication;
- Chain-of-Evidence;
- Human Gate.

---

## 7. Provider-neutral adapter boundary

```text
                     NAAIL Technology Core™
                              │
                      Provider Contract
                              │
      ┌───────────────┬───────┼────────┬───────────────┐
      │               │       │        │               │
 OpenAI Adapter   Google ADK  Claude   Microsoft    Local/Open
                               Adapter  Adapter       Adapter
      │               │       │        │               │
      └───────────────┴───────┼────────┴───────────────┘
                              │
                         MCP / A2A
                              │
                   Tools / Evidence / Data
                              │
                      Knowledge Core™
```

The same professional or scientific case should be runnable through multiple adapters where feasible.

---

## 8. Frozen benchmark before technology promotion

Technology promotion should rely on controlled comparison, not demonstrations.

Suggested common benchmark families:
- IFRS / financial reporting;
- PCAOB / assurance;
- CAM/KAM;
- ICFR;
- ESG / sustainability;
- finance / ECONOVA-S™;
- research co-scientist tasks;
- code / reproducibility tasks.

Common measures:
- evidence accuracy;
- citation accuracy;
- professional-rule compliance;
- hallucination / unsupported-claim rate;
- tool-selection accuracy;
- reproducibility;
- robustness;
- latency;
- cost;
- human-review acceptance;
- cross-provider disagreement;
- failure recovery.

A provider may be best for one workflow and not another. NAAIL should support **task-specific routing** rather than declaring one universal winner.

---

## 9. Technology Radar update cadence

### Monthly
- scan official OpenAI, Google, Anthropic, and Microsoft agent / model / SDK releases;
- record relevant changes;
- classify each as WATCH / EVALUATE / SANDBOX / ADOPT / RETIRE.

### Quarterly
- rerun selected frozen NAAIL benchmarks;
- compare adopted providers and emerging candidates;
- review cost, latency, security, observability, and evidence quality;
- update provider adapter priorities.

### Major release trigger
A new NAAIL release may be justified when a technology change materially improves one or more of:
- evidence quality;
- reproducibility;
- agent orchestration;
- professional safety;
- scientific validity;
- user experience;
- cost efficiency;
- interoperability.

---

## 10. Knowledge Core update cadence

The Knowledge Core should not follow the Technology Radar cadence.

### Standards / regulatory update
Update only after authoritative change and mapping review.

### Research update
Update after validated literature / replication review.

### Ontology update
Require documented schema change, migration note, and regression tests.

### Benchmark update
Preserve historical benchmark versions so longitudinal comparisons remain possible.

---

## 11. Core-version independence

NAAIL should version the two cores independently.

Example:

```text
Knowledge Core:   K2026.3
Technology Core:  T2026.9
Platform Release: NAAIL v0.2.4
```

A Technology Core upgrade should therefore not imply that the accounting/audit/scientific Knowledge Core changed.

Likewise, a new IFRS/PCAOB/scientific update should not force a model-provider change.

---

## 12. Technology-change firewall

```text
New vendor capability
        ↓
Technology Radar
        ↓
Evaluation / Sandbox
        ↓
Frozen NAAIL Benchmark
        ↓
Security + Rights + Cost Review
        ↓
Regression against Knowledge Core rules
        ↓
Human Architecture Gate
        ↓
Adapter promotion
```

No vendor release may bypass this firewall.

---

## 13. Scientific invariants

```text
provider_release_changes_scientific_truth = false
model_upgrade_changes_causal_DAG_automatically = false
new_agent_framework_bypasses_human_gate = false
new_model_bypasses_replication = false
optimize_for_vendor_lock_in = false

knowledge_core_versioned = true
technology_core_replaceable = true
provider_adapters_required = true
frozen_benchmark_before_promotion = true
human_architecture_gate_required = true
```

---

## 14. Recommended NAAIL operating principle

> **The Knowledge Core defines what NAAIL must know and how claims are governed. The Technology Core defines how NAAIL executes today. The Adaptive Intelligence Fabric lets the execution technology change without silently changing professional or scientific meaning.**

This separation allows NAAIL OpenLab to continuously absorb advances from OpenAI, Google AI, Anthropic/Claude, Microsoft AI, local/open models, and future providers while preserving reproducibility, evidence governance, domain integrity, and human responsibility.

---

## Independent-project notice

OpenAI, Google, Anthropic, Microsoft, and other third-party names are referenced as technology providers, interoperability targets, research inputs, or comparison benchmarks only. Their inclusion does not imply partnership, endorsement, certification, sponsorship, or marketplace approval. External technologies remain subject to their own licenses, terms, APIs, pricing, security requirements, and release cycles.
