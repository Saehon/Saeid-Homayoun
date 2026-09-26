# 🍋 Lemon-ICFR-US — Mother-Inherited Scientific Agent Architecture

## Mission
Lemon-ICFR-US is an evidence-governed agent system for US Internal Control over Financial Reporting (ICFR), designed for education, research, simulation, benchmarking, and controlled professional experimentation.

## Constitutional inheritance from the Mother
Lemon inherits the Mother repository's frozen **Two-Core Constitution**.

### Permanent Core 1 — Stable Knowledge Core
Contains durable ICFR meaning that must not drift when models or vendors change:
- SEC / SOX 404 / PCAOB / COSO mappings;
- accounts, assertions, processes, risks, controls, evidence, deficiencies and escalation logic;
- professional judgment schemas;
- Evidence Passport, Variable DNA, Chain-of-Evidence, Professional Decision DAG;
- source hierarchy, rights/licensing, provenance and chronology rules;
- scientific validation, replication, falsification and Human Gate rules;
- benchmark definitions and Failure Memory.

### Permanent Core 2 — Replaceable Technology Core
Contains technology that may be upgraded or retired without changing ICFR meaning:
- Claude / OpenAI / Gemini / Microsoft / local models;
- Claude for Financial Services, Financial Analysis, Excel, Claude Code and finance-agent templates;
- agent SDKs and orchestration runtimes;
- MCP / A2A connectors;
- RAG / GraphRAG / KAG implementations;
- code execution, data stores, tracing, observability and evaluation;
- Digital Twin engines;
- GAN / synthetic-data generators;
- UI and marketplace adapters.

**No third permanent core is created.**

## Cross-cutting Lemon layers
Scientific and agentic capabilities are layers/fabrics connecting the two permanent cores:

1. **Knowledge & Evidence Plane** — ICFR ontology, evidence hierarchy, GraphRAG, Evidence Passport, Variable DNA.
2. **Agentic Mesh** — orchestrator and specialist ICFR agents with scoped tools and separation of duties.
3. **Scientific Discovery Plane** — Co-Scientist, ERA-style empirical conversion, AlphaEvolve-inspired search, AlphaFold-inspired latent-structure reasoning, replication and falsification.
4. **Digital Twin & Scenario Lab** — repeatable entity/process/account/control/transaction twins.
5. **GAN / Synthetic-Adversarial Layer** — synthetic populations, rare-failure scenarios and adversarial stress cases. Synthetic outputs are simulations, never primary evidence of a real control failure.
6. **Governance & Observability Plane** — RBAC, run IDs, hashes, traces, cost/latency, quality metrics, privacy, model lineage, release controls and Failure Memory.
7. **Experience / Workflow Layer** — controller, internal audit, external audit, researcher and teaching interfaces.

The **Adaptive Intelligence / AI-to-AI Scientific Fabric** routes governed tasks and evidence across these layers.

## Canonical architecture

```text
                           LEMON-ICFR-US
                                  │
          ┌───────────────────────┴────────────────────────┐
          │                                                │
 STABLE KNOWLEDGE CORE                            REPLACEABLE TECHNOLOGY CORE
 SEC | SOX | PCAOB | COSO                        Claude | GPT | Gemini | MS
 ICFR ontology / judgments                       local/open models
 Evidence Passport                               MCP / A2A / GraphRAG
 Variable DNA / Decision DAG                     runtimes / stores / sandboxes
 Chain-of-Evidence / Failure Memory              Digital Twin / GAN adapters
          │                                                │
          └──────────── Adaptive Intelligence Fabric ───────┘
                                  │
                    Knowledge & Evidence Plane
                                  │
                           Agentic Mesh
                                  │
             Co-Scientist Hypothesis Tournament
     Generation → Reflection → Ranking → Evolution → Meta-review
                                  │
             Professional Decision DAG / Systems Map
                                  │
                  ERA-style Executable ICFR Object
                                  │
              Deterministic Tests + Model-Assisted Tests
                                  │
     AlphaEvolve-inspired Search under Frozen Fitness Function
                                  │
      AlphaFold-inspired Latent Structure / Relationship Search
                                  │
         Digital Twin + GAN/Synthetic-Adversarial Stress Lab
                                  │
                Temporal / OOS / Holdout Validation
                                  │
             Independent Reviewer / Replicator
                                  │
                     Falsification Agent
                                  │
             Science-One-style Chain-of-Evidence
                                  │
                          CoE Audit
                                  │
                        Evidence Passport
                                  │
                          HUMAN GATE
                                  │
                    Decision + Failure Memory
                                  │
                        Controlled Learning
```

## ICFR scientific object
For each material case Lemon should maintain:

`entity → process → account/disclosure → assertion → risk → control objective → control → evidence → test → exception → alternative explanation → deficiency candidate → reviewer → falsifier → human disposition`

Each governed object should also carry:
- source and provenance;
- rights/license status;
- chronology/information-availability status;
- Variable DNA / construct definition where applicable;
- model/tool/configuration versions;
- parent hash / content hash;
- independence class of reviewer;
- contradictions and failure state;
- required next action.

## COSO alignment
Lemon maps material cases to the five COSO components:
1. Control Environment
2. Risk Assessment
3. Control Activities
4. Information & Communication
5. Monitoring Activities

Lemon should also use COSO's 2026 Generative-AI internal-control guidance as a current risk/control reference for AI used inside ICFR workflows, while preserving the 2013 Internal Control—Integrated Framework as the underlying framework.

## Claude finance stack mapping

| Claude capability | Lemon role | Status |
|---|---|---|
| Claude for Financial Services | financial-domain workflow surface | Replaceable Technology |
| Financial Analysis Solution | trend/anomaly/context analysis | Specialist tool |
| Claude for Excel | controlled spreadsheet evidence/review interface | Specialist interface |
| Claude Code | engineering, testing and repository maintenance | Developer plane |
| Financial Services Agents | skills + connectors + subagent design pattern | Agent template layer |
| Claude connectors / MCP | governed access to approved data/tools | Connector layer |

Claude is **not** Lemon's professional authority. No model-generated conclusion becomes trusted evidence solely because a model produced it.

## Scientific discovery contract

### Co-Scientist
Lemon uses specialized functions inspired by multi-agent scientific collaboration:
- generation;
- reflection;
- ranking;
- evolution;
- proximity/redundancy review;
- meta-review.

Ranking is a search heuristic, not truth.

### ERA-style empirical conversion
A surviving hypothesis becomes an executable ICFR object with:
- data/evidence;
- Variable DNA;
- chronology;
- test procedure;
- code;
- frozen metrics;
- robustness/falsification plan;
- replication/OOS plan;
- expected failure modes.

### AlphaEvolve-inspired controlled improvement
Prompts, agent routing, deterministic rules, sampling logic, thresholds and test strategies may evolve only against a **frozen fitness function**. Search cannot optimize merely for a favorable conclusion.

### AlphaFold-inspired structure reasoning
AlphaFold is a biological model and is not an accounting model. Lemon borrows only the general idea of discovering difficult latent structure and subjecting it to rigorous external benchmarking.

### Chain-of-Evidence + CoE Audit
Material claims should trace:

`claim → source/data → transformation → code/test → executed result → robustness/falsification → replication → interpretation → human decision`

CoE Audit checks reference validity, numerical reproducibility, specification integrity, method/code alignment and claim/evidence alignment.

## GAN / Synthetic-Adversarial Layer
GAN or other synthetic generators may be useful for:
- rare control-failure scenarios;
- imbalanced material-weakness classes;
- transaction populations for sampling tests;
- access-control and segregation-of-duties stress cases;
- cut-off, approval and reconciliation exceptions;
- red-team/adversarial scenarios.

Rules:
- synthetic data is explicitly labelled;
- generated cases never masquerade as company evidence;
- provenance includes generator/model/version/seed/configuration;
- synthetic scenarios are separated from blind holdout gold keys;
- promotion from SANDBOX requires frozen-benchmark evidence;
- real professional conclusions require real/authoritative evidence anchors.

## Four-system separation
Where feasible:
1. **Generator** proposes hypotheses/tests.
2. **Evaluator** applies frozen metrics.
3. **Validator** independently replicates, red-teams and falsifies.
4. **Human Authority** approves/rejects the final disposition.

Different prompts to the same model are role separation, not strong independence.

## Technology promotion firewall
Every external technology follows:

`WATCH → EVALUATE → SANDBOX → ADOPT → REPLACE/RETIRE`

Promotion requires evidence on capability, security, privacy, rights, reproducibility, provenance, failure behavior, tool reliability, latency, cost, portability, observability, Human Gate compatibility and regression against frozen Lemon benchmarks.

## Required gates
1. provenance
2. rights/license
3. chronology/information availability
4. ICFR/COSO grounding
5. real-evidence anchor for real-world conclusions
6. evidence sufficiency
7. independent review
8. falsification
9. Chain-of-Evidence / CoE Audit
10. reproducibility / replication where material
11. human approval

## Non-negotiable invariants
```text
agent_consensus_is_truth = false
model_confidence_is_evidence = false
synthetic_data_is_real_evidence = false
prediction_equals_causality = false
optimize_for_favorable_conclusion = false
failed_runs_are_deleted = false
technology_change_rewrites_icfr_meaning = false
uncontrolled_self_improvement_allowed = false
human_gate_required = true
```

AI does not sign an audit opinion, replace management's ICFR assessment, replace auditor professional judgment, or authorize its own material conclusion.
