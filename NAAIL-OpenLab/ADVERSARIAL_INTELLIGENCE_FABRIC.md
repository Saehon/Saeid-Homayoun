# NAAIL Adversarial Intelligence Fabric™

**Platform:** NAAIL OpenLab™ — V2026.3 Multi-Agent Digital Twin  
**Layer:** Technology Core™ only  
**Knowledge & RAG Core:** `KRG2026.3` — frozen and protected  
**Status:** Architecture adopted; runtime integrations remain gated by license, security, benchmark, and Human Gate review

> **Scientific debate, independent review, falsification, replication, and security red teaming — without allowing any external agent framework to rewrite the frozen Knowledge & RAG Core.**

## 1. Purpose

The NAAIL Adversarial Intelligence Fabric™ adds governed adversarial reasoning and red-team capabilities to the NAAIL Technology Core. It is designed to challenge conclusions rather than merely generate them.

The Fabric supports four functions:

1. **Scientific Debate** — competing reasoning strategies, critic–defender exchange, debate-versus-vote comparison.
2. **Independent Review** — reviewer agents that commit judgments independently before seeing other agents' answers.
3. **Falsification & Replication** — explicit attempts to disprove, stress-test, and reproduce claims.
4. **Security Red Team** — attack the AI execution layer for jailbreaks, prompt injection, leakage, unsafe tool use, hallucination, and other model/system weaknesses.

The Fabric never determines scientific truth by agent consensus alone.

## 2. Canonical architecture

```text
FROZEN KNOWLEDGE & RAG CORE™
KRG2026.3
        │
        │ read-only governed interface
        ▼
Adaptive Intelligence Fabric™
        │
        ▼
TECHNOLOGY CORE™
        │
        ├── Orchestration Layer
        │     └── Microsoft Agent Framework
        │
        ├── Scientific Adversarial Layer
        │     ├── DMAD protocol
        │     ├── Debate-or-Vote protocol
        │     ├── CAMEL role-diversity sandbox
        │     └── NAAIL Independent Reviewer protocol
        │
        ├── NAAIL Adversarial Team
        │     ├── Proposer
        │     ├── Critic
        │     ├── Defender
        │     ├── Falsifier
        │     ├── Replicator
        │     ├── Evidence Auditor
        │     └── Judge
        │
        ├── Security Red-Team Layer
        │     ├── Microsoft PyRIT
        │     ├── NVIDIA garak
        │     └── promptfoo
        │
        └── Human Gate™
```

## 3. Adopted upstream projects

NAAIL integrates these projects as **Technology Core references, protocols, adapters, or evaluation tools**. No third-party repository is treated as NAAIL-owned code.

| Upstream project | NAAIL role | Integration state | Runtime claim |
|---|---|---|---|
| `microsoft/agent-framework` | primary orchestration reference for durable adversarial workflows | `ADOPT_ARCHITECTURE` | not yet executed as a NAAIL production runtime |
| `MraDonkey/DMAD` | diverse multi-agent debate protocol | `ADOPT_PROTOCOL` | benchmark/sandbox integration pending |
| `deeplearning-wisc/debate-or-vote` | debate-versus-vote scientific benchmark protocol | `ADOPT_BENCHMARK_PROTOCOL` | benchmark execution pending |
| `camel-ai/camel` | role-playing / role-diversity multi-agent simulation | `SANDBOX_REFERENCE` | execution pending |
| `microsoft/PyRIT` | generative-AI red-team framework | `ADOPT_RED_TEAM_REFERENCE` | execution pending |
| `NVIDIA/garak` | LLM vulnerability scanner | `ADOPT_RED_TEAM_REFERENCE` | execution pending |
| `promptfoo/promptfoo` | provider-neutral evaluation and red-team harness | `ADOPT_EVAL_REFERENCE` | execution pending |

Additional debate frameworks may remain in `REFERENCE_ONLY` status until license, maintenance, security, and scientific-fit review is complete.

## 4. Scientific adversarial team

### Proposer
Produces the initial hypothesis, professional judgment, model specification, or candidate conclusion.

### Critic
Searches for weaknesses in theory, evidence, logic, variable construction, statistical inference, professional standards mapping, and unsupported claims.

### Defender
Responds to the Critic using evidence, not rhetorical persuasion. Unsupported defenses must fail.

### Falsifier
Searches for tests that could overturn the claim, including alternative explanations, placebo tests, negative controls, contradictory evidence, robustness failures, and boundary conditions.

### Replicator
Attempts independent reproduction using frozen evidence, declared transformations, code, seeds/configuration where relevant, and the original evaluation contract.

### Evidence Auditor
Checks provenance, citation fidelity, source hierarchy, rights constraints, Evidence Passport™, and whether the conclusion is supported by the frozen Knowledge & RAG Core.

### Judge
Compares surviving arguments against predefined scientific/professional criteria. The Judge cannot approve a material claim without required evidence gates.

### Human Gate™
A human reviewer retains final authority for material scientific, professional, educational, or enterprise conclusions.

## 5. Debate protocol

```text
Proposer commits answer
        ↓
Independent Critic commits review
        ↓
Independent Falsifier commits attack plan
        ↓
Defender responds with evidence
        ↓
Replicator attempts reproduction
        ↓
Evidence Auditor checks provenance
        ↓
Debate-or-Vote comparison where appropriate
        ↓
Judge evaluates against frozen criteria
        ↓
Human Gate™
```

Agents should commit initial judgments independently before reading peer outputs when independence is material to the experiment.

## 6. Debate is not truth

```text
agent_consensus_is_truth = false
majority_vote_is_truth = false
judge_confidence_is_evidence = false
rhetorical_strength_is_validity = false
statistical_significance_is_discovery = false
predictive_accuracy_is_causality = false
```

Debate is an error-discovery mechanism. Scientific and professional conclusions remain governed by evidence, identification, replication, falsification, provenance, and human review.

## 7. Security red-team layer

Scientific adversarial review and cybersecurity red teaming are separate functions.

### PyRIT
Candidate use: orchestrated attacks, adversarial prompts, risk identification, and controlled red-team campaigns against NAAIL model/provider adapters.

### garak
Candidate use: broad LLM vulnerability scanning for jailbreaks, prompt injection, leakage, hallucination-prone behavior, toxicity, and other known risk classes.

### promptfoo
Candidate use: provider-neutral evaluation, regression tests, adversarial cases, and CI/CD comparison across GPT, Gemini, Claude, local/open models, and future providers.

Red-team findings enter **Failure Memory™** and must not be deleted merely because a newer model performs better.

## 8. Frozen Knowledge & RAG Core firewall

Every adversarial framework sits outside the frozen Knowledge & RAG Core.

It may:
- query governed evidence through approved interfaces;
- challenge a claim;
- request additional retrieval;
- propose a competing interpretation;
- request robustness or replication tests;
- generate red-team cases;
- score Technology Core behavior.

It may not automatically:
- rewrite standards mappings;
- alter the evidence hierarchy;
- change GraphRAG ontology semantics;
- mutate RAG corpus-governance rules;
- change causal DAGs;
- alter benchmark gold definitions;
- change Evidence Passport™ schemas;
- bypass Human Gate™.

```text
adversarial_agent_may_modify_knowledge_rag_core = false
red_team_tool_may_modify_knowledge_rag_core = false
vendor_framework_may_change_scientific_truth = false
human_gate_required = true
```

## 9. Integration rule

NAAIL should prefer **adapters and protocol implementations** over copying third-party source code into the repository.

Before any runtime dependency is promoted from architecture/reference to executable integration, NAAIL requires:

- current upstream repository verification;
- license and terms review;
- pinned version / commit where appropriate;
- dependency/security review;
- privacy and data-use review;
- synthetic sandbox execution;
- frozen benchmark evaluation;
- reproducibility test;
- failure logging;
- Human Architecture Gate approval.

## 10. Evaluation matrix

Every adversarial configuration should be evaluated on more than answer accuracy.

| Dimension | Example measures |
|---|---|
| Error discovery | defects found, unsupported claims caught, contradiction detection |
| Scientific value | falsification quality, replication success, alternative-mechanism discovery |
| Evidence | citation accuracy, provenance fidelity, Evidence Passport completeness |
| Professional quality | standards compliance, escalation quality, reviewer acceptance |
| Diversity | reasoning-strategy diversity, disagreement quality, non-duplicate critiques |
| Robustness | sensitivity to prompts/models/providers/seeds |
| Security | jailbreak resistance, prompt-injection resistance, data-leakage findings |
| Operations | latency, compute/token cost, recovery from failed agents |

## 11. NAAIL domain integration

### KIWI™
CAM/KAM risk → Proposer → Critic → Defender → Evidence Auditor → Falsifier → Replicator → Judge → Human Gate.

### POMELO™ / VERA™
Accounting/assurance judgment → independent evidence review → adversarial interpretation → Decision DAG → verification → Human Gate.

### ECONOVA-S™
Economic/finance hypothesis → competing models → debate-or-vote test → falsification → replication → Evidence Passport → Human Gate.

### ICFR / Controls
Control-risk assessment → adversarial deficiency classification → contradictory evidence search → remediation challenge → Human Gate.

### ESG / Sustainability
Claim → source-rights/evidence audit → greenwashing critic → alternative-measure test → replication / triangulation → Human Gate.

## 12. Repository integration

Canonical machine-readable registry:

- `architecture/adversarial_agent_registry.json`

Validation:

- `tests/test_adversarial_agent_registry.py`

GitHub CI:

- `.github/workflows/naail_adversarial_agent_registry.yml`

Core boundary:

- `FROZEN_KNOWLEDGE_RAG_CORE_INVARIANT.md`
- `architecture/core_boundary_policy.json`

## 13. Current status

**Adopted now:** architecture, role model, registry, protocol mapping, red-team/evaluation positioning, core-boundary rules, and CI validation.

**Not claimed yet:** installed/executed upstream packages, completed provider runs, benchmark superiority, production deployment, marketplace certification, or security certification.

That distinction is mandatory for all future NAAIL releases.

---

## Independent-project and third-party notice

Microsoft, CAMEL-AI, NVIDIA, promptfoo, DMAD, Debate-or-Vote, and other upstream names identify independent open-source projects or research references. Their inclusion does not imply affiliation, endorsement, sponsorship, certification, or transfer of ownership. Third-party code remains subject to its own license and terms. NAAIL-specific architecture, governance, evidence contracts, benchmarks, and integration logic remain separate.