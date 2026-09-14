# NAAIL OpenLab™ — Public Reference Architecture

NAAIL OpenLab is a research-first, human-led AI platform for business-school education, audit simulation, and reproducible scientific discovery. This public architecture intentionally omits patent-sensitive implementation details.

## Design goal
Build a platform that is:
- evidence-governed;
- model/provider-neutral;
- auditable and reproducible;
- safe for synthetic education/research use;
- explicit about human responsibility;
- testable through frozen benchmarks and Digital Twin scenarios.

## Seven public layers
1. **Experience Layer** — Student, instructor, researcher, auditor, reviewer, and administrator interfaces.
2. **Audit Workspace** — Planning, materiality, risk, controls, analytics, evidence, testing, documentation, review, and reporting.
3. **Agent Mesh** — Specialist agents with explicit roles, scoped tools, handoffs, structured outputs, and human approval points.
4. **Knowledge & Evidence Plane** — Standards references, lawful guidance, FT50/AJG research intelligence, provenance, citations, and Knowledge Graph/GraphRAG services.
5. **Governance & Observability Plane** — Identity/RBAC, registries, run tracing, evaluation, quality monitoring, defect memory, and release controls.
6. **Digital Twin Lab** — Synthetic Client XYZ, fictional Firm Alpha–Delta, regulator/audit-committee roles, and repeatable case environments.
7. **Scientific Discovery Plane** — Hypothesis portfolios, ERA-style empirical conversion, computational discovery, adversarial review, falsification, replication, Chain-of-Evidence, and Human Gate.

## Stable vs replaceable
### Knowledge Core™
Stable professional and scientific knowledge, standards mappings, validated literature, evidence structures, ontologies, and benchmark definitions.

### Technology Core™
Replaceable models, agent runtimes, orchestration frameworks, retrieval components, tools, memory implementations, and deployment infrastructure.

### Adaptive Intelligence Fabric™
A governed bridge that routes tasks, context, evidence, tools, models, policies, and approvals between the two cores.

## Vendor-neutral runtime principle
NAAIL should be able to support different providers and frameworks behind a common internal contract. Provider-specific features may be used through adapters, but business logic, evidence rules, evaluation criteria, and human gates should remain portable.

## V2026.3 implementation profile

The next architecture snapshot formalizes a Google + Microsoft dual-stack pattern while preserving provider neutrality:

```text
Google ADK / Antigravity-style development
        +
Microsoft Agent Framework
        +
A2A + MCP interoperability
        +
Microsoft GraphRAG / evidence graph
        +
NAAIL Digital Twin ontology
        +
Co-Scientist-style hypothesis arena
        +
ERA-style reproducible empirical design
        +
AlphaEvolve-style evaluator search
        +
AlphaFold-inspired latent-structure reasoning
        +
Computational Discovery
        +
Critic / Defender / Replicator / Falsifier
        +
Science One-style Chain-of-Evidence
        +
Professional Decision DAG™
        +
Human Gate
```

A2A and MCP are treated as interoperability layers; GraphRAG is treated as an evidence/relationship layer; and the Digital Twin remains a NAAIL domain abstraction rather than a dependency on any single cloud vendor.

See [V2026.3 Multi-Agent Digital Twin](./versions/V2026.3_MULTI_AGENT_DIGITAL_TWIN.md).

## Digital Twin expansion

V2026.3 extends the Digital Twin Lab beyond engagement simulation to include linked professional and scientific state:

- Organization / Entity Twin;
- Engagement Twin;
- Business Process Twin;
- Account / Assertion Twin;
- Risk / Control / ICFR Twin;
- Transaction / Journal Twin;
- CAM/KAM Twin;
- ESG / Assurance Twin;
- Forensic Investigation Twin;
- Research Study Twin.

Claims should be traceable through a graph such as:

```text
Evidence -> Transformation -> Model/Agent Run -> Result -> Claim
Claim -> Critique -> Replication -> Falsification -> Human Decision
Research Hypothesis -> Empirical Design -> Replication Run -> Evidence Passport
```

## Scientific discovery governance

Every material research workflow should, where applicable, require:

**Literature Validation → Competing Hypotheses → Co-Scientist Critique/Ranking → ERA Empirical Design → Frozen Data Rules → Reproducible Baseline → AlphaEvolve-Style Search → Latent-Structure Analysis → Robustness/Falsification → Temporal/OOS Validation → AI-to-AI Review → Clean-Room Replication → Chain-of-Evidence → DAG Audit → Human Gate.**

Scientific invariants:

```text
agent_consensus_is_truth = false
model_confidence_is_evidence = false
optimize_for_p_value = false
failed_runs_are_deleted = false
train_test_leakage_allowed = false
temporal_leakage_allowed = false
prediction_equals_causality = false
human_gate_required = true
unsupported_discovery_claim_allowed = false
```

## Workflow principle
Use the simplest orchestration pattern that satisfies the task:
- direct tool call;
- single agent;
- specialist delegation;
- explicit sequential/concurrent workflow;
- graph-based workflow;
- long-running checkpointed workflow.

Every material workflow must expose its stages, dependencies, approvals, failure states, and evaluation results.

## Public/private boundary
The public repository describes research-safe interfaces, governance principles, synthetic scenarios, evaluation standards, and educational materials. Detailed orchestration logic, unpublished methods, private datasets, commercial strategy, and patent-candidate mechanisms remain in the private development master.
