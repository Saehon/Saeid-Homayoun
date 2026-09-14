# NAAIL OpenLab™ — Open-Source Agent Education Stack

**Status:** v0.2.4 target capability  
**Scope:** non-commercial research and education  
**Validated public software release remains:** v0.2.3 / Prototype 003

## Purpose

This layer gives NAAIL OpenLab a provider-neutral way to compare and teach open-source agent frameworks without copying or claiming ownership of upstream projects. Each upstream framework remains third-party software governed by its own repository, license, trademarks, release cycle, security posture, and model/API requirements.

The NAAIL integration pattern is:

```text
Student / Researcher
        ↓
NAAIL Educational Proxy Agent
        ↓
Framework Adapter Boundary
        ↓
Open-Source Agent Framework
        ↓
NAAIL Evidence Contract
        ↓
Evidence Passport™ + Professional Decision DAG™
        ↓
RPA + AA + EG + PS + DS + DIST
+ AIV + CER + HOR + ESC
        ↓
Adversarial Review / Falsification
        ↓
Human Gate
```

No framework is treated as professional authority, and no agent may approve its own material conclusion.

## Priority upstream stack

| Tier | Upstream project | NAAIL role | Upstream repository | Integration status |
|---|---|---|---|---|
| Core | Google Agent Development Kit (ADK) | Code-first agent orchestration and teaching labs | https://github.com/google/adk-python | Reference/adapter target |
| Core | Microsoft Agent Framework | Enterprise-style orchestration and comparative education | https://github.com/microsoft/agent-framework | Reference/adapter target |
| Core | CAMEL-AI | Multi-agent role simulation, debate, auditor/client/regulator experiments | https://github.com/camel-ai/camel | Reference/adapter target |
| Core | Hugging Face smolagents | Lightweight student agents and code/tool exercises | https://github.com/huggingface/smolagents | Reference/adapter target |
| Core | Haystack | Evidence-grounded RAG, retrieval, routing and evaluation | https://github.com/deepset-ai/haystack | Reference/adapter target |
| Core | Model Context Protocol Python SDK | Standardized tool/resource interoperability | https://github.com/modelcontextprotocol/python-sdk | Reference/adapter target |
| Core | Ollama | Local-model runtime for low-cost/offline-compatible teaching | https://github.com/ollama/ollama | Reference/adapter target |
| Extended | LlamaIndex | Data/RAG interfaces and knowledge-base experiments | https://github.com/run-llama/llama_index | Reference target |
| Extended | OpenAI Agents SDK | Lightweight handoffs, tools and multi-agent comparison | https://github.com/openai/openai-agents-python | Reference target |
| Extended | GPT Researcher | Autonomous research workflow experiments | https://github.com/assafelovic/gpt-researcher | Reference target |
| Extended | Browser Use | Browser-based evidence collection experiments | https://github.com/browser-use/browser-use | Reference target |
| Extended | OpenHands | Coding/data-science agent experiments | https://github.com/OpenHands/OpenHands | Reference target |
| Extended | MetaGPT | Role-based multi-agent team simulation | https://github.com/FoundationAgents/MetaGPT | Reference target |
| Extended | CrewAI | Accessible role/task multi-agent teaching exercises | https://github.com/crewAIInc/crewAI | Reference target |

The machine-readable registry is maintained at [`integrations/open_source_agents/registry.json`](./integrations/open_source_agents/registry.json).

## NAAIL educational profiles

### Profile A — Zero/low-cost classroom

Recommended starting combination:

```text
Ollama + compatible local model
        +
smolagents
        +
MCP tools
        +
NAAIL synthetic Client XYZ evidence
```

Purpose: make basic agentic-AI assignments possible without requiring every student to purchase a commercial API subscription. Model licenses, hardware requirements, and institutional IT policies must still be checked separately.

### Profile B — Enterprise orchestration comparison

```text
Google ADK
vs.
Microsoft Agent Framework
vs.
NAAIL provider-neutral evaluation contract
```

Purpose: teach students how orchestration choices affect evidence grounding, handoffs, traceability, latency, failure modes, and Human Gate compliance without claiming that the educational proxy reproduces proprietary professional-firm systems.

### Profile C — Multi-agent audit simulation

```text
CAMEL / MetaGPT / CrewAI
        ↓
Planner → Auditor → Specialist → Critic → Reviewer
        ↓
Synthetic Client XYZ
        ↓
Evidence Passport™
        ↓
Human Gate
```

Purpose: controlled experiments on professional skepticism, contradictory evidence, role separation, and agent-to-agent error propagation.

### Profile D — Evidence and RAG laboratory

```text
Haystack / LlamaIndex
        ↓
Authorized public/licensed evidence
        ↓
Retrieval + provenance + contradiction checks
        ↓
NAAIL Evidence Passport™
```

Purpose: compare retrieval architectures while preserving rights/licensing controls and source provenance.

### Profile E — Research and coding laboratory

```text
GPT Researcher / Browser Use / OpenHands
        ↓
Research question / public data / reproducible code
        ↓
ERA-style empirical design
        ↓
Replication + falsification + Human Gate
```

Purpose: train students to move from AI-generated research ideas to reproducible empirical tests rather than accepting generated reports as scientific evidence.

## Adapter contract

Any framework adapter accepted into NAAIL should expose, where applicable:

- `framework_name`
- `framework_version`
- `upstream_repository`
- `upstream_commit_or_release`
- `model_provider`
- `model_id`
- `agent_role`
- `tool_permissions`
- `evidence_ids_used`
- `evidence_ids_rejected`
- `handoff_trace`
- `uncertainty`
- `limitations`
- `run_timestamp`
- `run_manifest_hash`
- `human_gate_state`

For material research/professional simulations, an adapter must not silently fabricate missing provider output. Unavailable executions must remain explicitly unexecuted.

## Rights and dependency policy

1. NAAIL does **not** vendor or relicense upstream projects merely because they are referenced in this stack.
2. Before installing, redistributing, modifying, or packaging an upstream dependency, verify its **current upstream license and release-specific terms**.
3. Model weights and hosted APIs have separate terms from the orchestration framework and must be reviewed independently.
4. Public NAAIL examples should use synthetic, public, or properly licensed evidence.
5. Third-party names are used descriptively and do not imply affiliation, sponsorship, endorsement, certification, or compatibility guarantees.
6. Patent-sensitive NAAIL orchestration details, private benchmarks, credentials, and proprietary adapters remain outside the public repository.

## Student assignment pattern

A canonical exercise is:

> Evaluate the same synthetic audit case with two agent frameworks under the same frozen evidence and agent-role specification. Record every evidence ID used, rejected, or invented; score RPA, AA, EG, PS, DS, DIST, AIV, CER, HOR, and ESC; perform an adversarial critique; then require a human decision before any professional conclusion.

Students are evaluated on evidence use, reproducibility, professional skepticism, reasoning, documentation, and appropriate escalation—not on agreement with the agent.

## Scientific comparison rule

NAAIL must not report one framework as superior based on anecdotal demonstrations. Comparative claims require frozen tasks, equivalent evidence access, declared model/provider versions, repeated runs where stochasticity matters, failure retention, prespecified metrics, robustness analysis, and Human Gate review.

## Related NAAIL documents

- [`AGENTS.md`](./AGENTS.md)
- [`ARCHITECTURE.md`](./ARCHITECTURE.md)
- [`EVALUATION_STANDARD.md`](./EVALUATION_STANDARD.md)
- [`docs/education/NAAIL_BIG4_STUDENT_AGENT_ACADEMY.md`](./docs/education/NAAIL_BIG4_STUDENT_AGENT_ACADEMY.md)
- [`docs/education/OPEN_SOURCE_AGENT_LAB.md`](./docs/education/OPEN_SOURCE_AGENT_LAB.md)
- [`versions/V2026.3_MULTI_AGENT_DIGITAL_TWIN.md`](./versions/V2026.3_MULTI_AGENT_DIGITAL_TWIN.md)

## Release integrity

This document publishes an integration architecture and educational registry. It does **not** claim that all listed frameworks have been installed, executed, benchmarked, security-reviewed, or validated inside NAAIL. Those states must be demonstrated by version-pinned executable runs and retained evaluation artifacts.