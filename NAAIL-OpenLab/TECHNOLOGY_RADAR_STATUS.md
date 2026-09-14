# NAAIL OpenLab™ — Technology Radar Status

**Platform:** NAAIL OpenLab™  
**Knowledge Core:** `K2026.3`  
**Technology Core design state:** `T2026.9-design`  
**Status:** Public architecture/evaluation registry — not a claim of production integration

> **Knowledge should be durable. Technology should be replaceable.**

## Core separation

NAAIL maintains two independently governed cores:

- **Knowledge Core™** — accounting, auditing, assurance, CAM/KAM, ICFR, ESG, finance/economics, theory, causal DAGs, identification, evidence rules, benchmarks, replication, Chain-of-Evidence, Evidence Passport™, and Human Gate™.
- **Technology Core™** — foundation models, agent SDKs, orchestration, retrieval, MCP/A2A, memory, tool calling, sandboxes, observability, evaluation tooling, UI adapters, and deployment infrastructure.

The **Adaptive Intelligence Fabric™** connects them so technology can change without silently changing scientific or professional meaning.

## Current provider radar

| Provider / technology | Current NAAIL state | Candidate role | Production claim? |
|---|---|---|---|
| **OpenAI Agents SDK** | EVALUATE | orchestration, handoffs, guardrails, tracing, sandbox workflows | No |
| **Google ADK** | EVALUATE | multi-agent workflows, evaluation, interoperability, sandboxed execution | No |
| **Gemini CLI** | EVALUATE | repository/developer workflow experiments and low-cost prototyping | No |
| **Anthropic Claude Agent SDK** | EVALUATE | evidence workspace, long-document/repository review, subagents, permissions | No |
| **MCP** | EVALUATE | provider-neutral tool/evidence connectivity | No |
| **Microsoft Agent Framework** | EVALUATE | enterprise workflow orchestration, checkpointing, Human Gate patterns | No |
| **A2A** | EVALUATE | cross-agent interoperability | No |
| **Local / open models** | WATCH / EVALUATE | research baseline, privacy-sensitive and cost-controlled experiments | No |

No row above means a provider is endorsed, integrated in production, approved for marketplace release, or superior to another provider.

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
- regression against frozen NAAIL benchmarks.

## Knowledge Core firewall

A provider or model upgrade must never automatically change:

- professional standards mappings;
- causal DAGs;
- construct definitions;
- benchmark gold definitions;
- evidence hierarchy;
- replication requirements;
- falsification requirements;
- Human Gate rules.

```text
provider_release_changes_scientific_truth = false
model_upgrade_changes_causal_DAG_automatically = false
new_framework_bypasses_human_gate = false
new_model_bypasses_replication = false
optimize_for_vendor_lock_in = false
```

## Update cadence

### Monthly technology scan
Review material changes from OpenAI, Google, Anthropic/Claude, Microsoft, and selected open-model ecosystems. Classify each as WATCH / EVALUATE / SANDBOX / ADOPT / RETIRE.

### Quarterly benchmark review
Rerun selected frozen NAAIL cases when executable adapters exist and compare evidence quality, reliability, reproducibility, cost, latency, and human-review acceptance.

### Knowledge Core updates
Update separately, only when justified by authoritative standards/regulation, validated research, benchmark evidence, or approved ontology/governance changes.

## Canonical references

- [Knowledge Core, Technology Core & AI Technology Radar](./CORE_ARCHITECTURE_AND_TECHNOLOGY_RADAR.md)
- [Public Reference Architecture](./ARCHITECTURE.md)
- [Scientific Discovery Platform](./SCIENTIFIC_DISCOVERY_PLATFORM.md)
- [Scientific Discovery Contract](./SCIENTIFIC_DISCOVERY_CONTRACT.md)
- [Business-School Open Agent Pack](./BUSINESS_SCHOOL_OPEN_AGENT_PACK.md)
- [Marketplace Edition](./MARKETPLACE_EDITION.md)

## Independent-project notice

OpenAI, Google, Anthropic, Microsoft, and other third-party names are referenced as technology providers, interoperability targets, research inputs, or comparison benchmarks only. Their inclusion does not imply partnership, endorsement, certification, sponsorship, marketplace approval, or production integration.
