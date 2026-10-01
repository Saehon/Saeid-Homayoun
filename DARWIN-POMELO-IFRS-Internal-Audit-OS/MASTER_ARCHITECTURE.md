# DARWIN-POMELO IFRS Internal Audit OS
## Master Architecture & Execution Blueprint

**Architecture:** Antigravity-native · Multi-model · Evidence-governed · Open-source-first  
**Version:** 1.0  
**Date:** 1 October 2026

## 1. North Star

Convert every IFRS-triggered business event into an **evidence-grounded, independently challenged, value-aware and human-approved decision**.

```text
ERP / Event
→ IFRS
→ Internal Audit
→ Evidence
→ Risk / Control
→ Counterfactual
→ Value
→ Decision
→ Learning
```

## 2. Canonical architecture

```text
HUMAN AUTHORITY
  CAE / CFO / IFRS Expert / Audit Committee / Reviewer
                         ▲
                  HUMAN DECISION GATE
                         │
DARWIN DECISION & VALUE LAYER
  APPROVE | MODIFY | ESCALATE | REJECT | OPTIMIZE
                         ▲
AGENTIC AGENCY LAYER
  Planner | IFRS | Internal Audit | Control | Evidence | Quant | Value
  Challenger | Falsifier | Replicator | Digital Twin | Reviewer
                         ▲
POMELO UNIVERSAL ROUTER + COST GOVERNOR
           ┌─────────────┼─────────────┐
           ▼             ▼             ▼
          GPT          Claude        Gemini
     Builder/Quant     Challenge     Executor
           └─────────────┬─────────────┘
                         ▼
            IBM GRANITE / LOCAL OPEN MODELS
                         ▼
              DETERMINISTIC TOOLS / RULES

Stable-Meaning Side                    Replaceable-Technology Side
┌──────────────────────┐               ┌──────────────────────┐
│ Knowledge Core       │               │ Technology Core      │
│ IFRS/IAS/IIA/COSO    │               │ Antigravity/ADK/MCP  │
└──────────▲───────────┘               └──────────▲───────────┘
           │                                      │
┌──────────┴───────────┐               ┌──────────┴───────────┐
│ Science Core         │               │ Synthetic/GAN Core   │
│ DAG/replication/OOS  │               │ Twin/fraud/scenario  │
└──────────────────────┘               └──────────────────────┘
                         │
                 DATA & EVIDENCE MESH
 Contracts | PO | SO | Invoice | GL | XBRL | ERP | Workpapers
```

## 3. Constitutional mapping

NAAIL keeps exactly **two permanent cores**. The four operational cores below are implementation boundaries.

| Operational core | Contents | Constitutional placement |
|---|---|---|
| Knowledge Core | IFRS/IAS, IIA, COSO, assertions, RCM, professional ontology and judgment schemas | Stable Knowledge Core |
| Science Core | Theory, causal DAGs, hypotheses, econometrics, replication, falsification, OOS validation | Stable Knowledge Core |
| Technology Core | Antigravity, ADK, GPT/Claude/Gemini/Granite adapters, MCP, A2A, RAG, databases | Replaceable Technology Core |
| Synthetic/GAN Core | Synthetic ERP, digital twins, anomaly/fraud cases and counterfactual simulation | Replaceable Technology Core / supporting layer |

## 4. Knowledge Core

The Knowledge Core preserves professional meaning independently of model/provider changes.

### Governed objects

- IFRS / IAS: recognition, measurement, presentation, disclosure, judgment, estimates and effective dates.
- Internal Audit / IIA: governance, risk, controls, assurance, engagement planning, findings and recommendations.
- COSO / ICFR: risk, control objective, control activity, owner, frequency, evidence and deficiency.
- Assertions: existence, completeness, accuracy, valuation, rights/obligations, cut-off and presentation.
- Value logic: relevant cost, opportunity cost, EVA/capital charge and decision economics.
- Professional judgment: materiality, uncertainty, escalation and abstention.

**Rule:** LLMs may propose changes; they may not silently update canonical knowledge.

## 5. Science Core

```text
Literature Grounding
→ Competing Hypotheses
→ Hypothesis Tournament
→ Causal / Decision DAG
→ Variable DNA
→ Empirical Design
→ Reproducible Baseline
→ Model / Algorithm Search
→ Robustness
→ Falsification
→ Temporal / OOS Validation
→ Independent Replication
→ Chain of Evidence
→ Evidence Passport
→ Human Scientific Gate
```

Scientific invariants:

- agent consensus is not truth;
- prediction is not automatically causality;
- statistical significance is not discovery;
- failed runs and contradictory evidence are retained.

## 6. Technology Core

| Layer | Preferred technology | Role |
|---|---|---|
| Control plane | Google Antigravity | Multi-agent execution, lifecycle, sandboxing, hooks, telemetry |
| Orchestration | Google ADK | Sequential/parallel/loop workflows |
| Agent interoperability | A2A | Cross-agent and cross-framework handoff |
| Tool interoperability | MCP | Standardized tools/resources |
| OpenAI adapter | OpenAI Agents SDK / API | GPT specialist agents |
| Anthropic adapter | Claude Agent SDK / Claude Code | Independent challenge/red-team |
| Google adapter | Gemini | Antigravity-native planning/execution/verification |
| IBM adapter | Granite family | Local/open first-pass reasoning, embeddings and guardrails |
| Local runtime | Ollama or equivalent | Offline/low-cost execution |
| Evidence graph | GraphRAG / graph DB / vector DB | Relationship-aware retrieval |

## 7. Synthetic / GAN / Digital Twin Core

Use synthetic ERP/GL, contracts, revenue, inventory, CapEx, fraud/AML scenarios and counterfactual simulations for controlled tests.

Mandatory evidence classes:

```yaml
evidence_class:
  - REAL
  - PUBLIC
  - LICENSED
  - SYNTHETIC
  - SIMULATED
  - MODEL_GENERATED
```

**Synthetic Evidence ≠ Audit Evidence.**

## 8. Agentic Agency Layer

| Level | Authority |
|---|---|
| A0 — Observe | Read-only |
| A1 — Analyze | Extract, classify, analyze |
| A2 — Recommend | Propose treatment, control or action |
| A3 — Sandbox Execute | Run code, tests or simulations in isolated environments |
| A4 — Enterprise Action | Modify a real system; explicit human approval required |

No agent may approve its own material conclusion.

## 9. Model separation

| Model/system | Primary role |
|---|---|
| Gemini / Antigravity | Planning, orchestration, native execution, evidence verification |
| GPT | Builder, IFRS/accounting/quant reasoning, coding, reconciliation |
| Claude | Independent challenger, contradiction detection, red-team and falsification |
| IBM Granite | Local/open extraction, classification, low-cost RAG and first-pass reasoning |
| Deterministic engine | Arithmetic, reconciliations, XBRL validation and thresholds |
| Human | Material accounting/audit decision and approval |

## 10. POMELO Universal Router & Cost Governor

Before a frontier-model call, POMELO asks:

1. Can deterministic code solve it?
2. Can retrieval or the Knowledge Core answer it?
3. Can a local/open model answer it within quality thresholds?
4. Is frontier reasoning actually required?
5. Is independent challenge required because of materiality, uncertainty or disagreement?

### Routes

| Route | Use case | Preferred execution |
|---|---|---|
| GREEN | Reconciliation, arithmetic, XBRL validation, rule checks | Python / SQL / Arelle / deterministic tools |
| BLUE | Classification, extraction, summarization, simple retrieval | Docling + Granite/local model |
| AMBER | Moderate IFRS/internal-audit judgment | Retrieval + one frontier model + deterministic check |
| RED | Material/high-uncertainty professional judgment | GPT + Claude independent review + Gemini verification + Human Gate |

## 11. Token and cost architecture

```text
CACHE
↓ miss
Deterministic Rules / SQL / Python
↓ insufficient
BM25 / Knowledge Graph / RAG
↓ insufficient
IBM Granite / Local Model
↓ low confidence
Low-cost Hosted Model
↓ uncertainty or materiality
GPT OR Claude
↓ disagreement / high risk
GPT + Claude Independent Review
↓ material decision
Human Gate
```

```text
AI Cost =
Token Cost
+ Compute Cost
+ Latency Cost
+ Human Review Cost
+ Error Cost
```

Optimize cost only subject to quality, evidence, reliability, reproducibility and governance thresholds.

## 12. Open-source / IBM stack

Primary reusable components already tracked in the Saehon ecosystem:

- IBM Granite / Granite Embeddings / Granite Guardian
- Docling / Docling MCP
- Arelle
- CPA Skills
- FinanceSkills
- Closegate
- FinBERT / FinGPT
- Ollama
- Microsoft FinanceBenchmark
- IBM financial-agent output-drift / assurance harness
- Google ADK
- Microsoft Agent Framework
- SEC EDGAR / ESEF connectors

## 13. Data & Evidence Mesh

Every material claim should carry:

```text
Claim ID
Evidence ID
Source / Authority
Source Version / Effective Date
Transaction / Contract / Account ID
Timestamp
Evidence Class
Owner / Custodian
Reliability
Transformation History
Model / Tool Used
Contradictory Evidence
Run ID / Parent Hash
Human Decision State
```

**No evidence → no material audit conclusion.**

## 14. IFRS + Internal Audit workflow

```text
ERP / Contract / PO / SO / Invoice / GL Event
→ Parser / Docling
→ Evidence Mesh
→ Applicable IFRS / IAS
→ Accounting Judgment
→ Financial Statement Assertion
→ Inherent / Residual Risk
→ Control Objective
→ Control Activity / Owner / Frequency
→ Audit Test
→ Evidence Evaluation
→ Finding / Exception
→ Root Cause
→ Economic Consequence
→ Counterfactual Alternatives
→ Internal Audit Recommendation
→ Independent Challenge / Falsification
→ Evidence Passport
→ Human Approval
→ Outcome Learning
```

## 15. Priority IFRS MVP

1. IFRS 15 — revenue.
2. IFRS 16 — leases.
3. IAS 2 — inventory.
4. IAS 16 — PPE / CapEx.
5. IAS 36 — impairment.
6. IAS 37 — provisions and contingencies.

## 16. Pre-Transaction Decision Gate

```text
Business Event / Proposed Transaction
→ IFRS implications
→ Risk & control assessment
→ Evidence sufficiency
→ Alternative scenarios
→ Economic value / opportunity cost
→ Challenge & verification
→ APPROVE | APPROVE WITH CONTROL | MODIFY | ESCALATE | REJECT
```

Blocking real transactions requires an authorized human policy and approval path.

## 17. Evidence-governed multi-model protocol

```text
CREATE      → GPT
CHALLENGE   → Claude
VERIFY      → Gemini + deterministic tools
SIMULATE    → Digital Twin
VALUE       → DARWIN
REPLICATE   → independent tool/agent
DECIDE      → Human
LEARN       → expected vs actual + failure memory
```

## 18. Existing GitHub assets and placement

| Asset | Role |
|---|---|
| Saehon/Saeid-Homayoun | Public umbrella, registry and governance |
| NAAIL-OpenLab | Science, evidence, digital twins and benchmark layer |
| pomelo-core | Private canonical runtime, router and orchestration |
| IFRS-AI-Inspector | IFRS specialist service |
| IFRS-PCAOB-AI | Regulatory/external inspection specialist |
| Lemon-ICFR-US | ICFR specialist |
| Apple-CAM-US | US CAM specialist |
| Orange-KAM-EU-UK | KAM specialist |
| Google-Antigravity-using-a-multi-agent-BERT-architecture | Antigravity experimental sandbox |
| AuditData-API | Structured audit/accounting data API |
| sec-edgar-downloader / openesef | Public reporting evidence connectors |
| timesfm | Temporal forecasting adapter |
| ganlab / fg-data-synthetic | Synthetic-data / teaching references |

## 19. Recommended private POMELO runtime structure

```text
pomelo-core/
  00_constitution/
  01_antigravity_control_plane/
  02_router/
     task_router/
     model_router/
     evidence_router/
     materiality_router/
     token_budget/
     cost_governor/
  03_operational_cores/
     knowledge_core/
     science_core/
     technology_core/
     synthetic_gan_core/
  04_agentic_agency/
  05_provider_adapters/
     google/
     openai/
     anthropic/
     ibm/
     local/
  06_tool_mesh/
  07_evidence_mesh/
  08_digital_twins/
  09_counterfactual_value/
  10_deterministic_engine/
  11_memory_cache/
  12_evals_benchmarks/
  13_observability/
  14_security/
  15_human_gate/
```

## 20. Public/private boundary

This public specification is intentionally non-enabling. Patent-sensitive router logic, scoring/evaluation functions, proprietary data, credentials, private provider adapters and partner-confidential implementation stay outside this public folder.
