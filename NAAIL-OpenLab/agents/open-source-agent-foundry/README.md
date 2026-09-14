# Open-Source Academic Agent Foundry

This directory contains the **public, research-safe integration boundary** between NAAIL OpenLab™ and selected open-source academic agent frameworks.

The design goal is to use mature open-source components where appropriate while keeping NAAIL-specific professional ontologies, Digital Twins, evidence governance, evaluation metrics, and Human Gate controls independent and provider-neutral.

## Components

- `registry.json` — machine-readable upstream registry with role, license, status, and integration mode.
- `requirements.txt` — optional Python dependencies for executable adapters.
- `naail_agent_foundry.py` — dependency/status checker and provider-neutral NAAIL Professional Swarm™ planning scaffold.

## Integration policy

1. **Do not vendor/copy upstream code by default.** Prefer normal package installation or a separately pinned upstream dependency.
2. **Preserve upstream licenses and attribution.** A permissive upstream license does not convert third-party code into NAAIL-owned IP.
3. **Pin versions/commits for research runs.** Replication artifacts must record dependency versions and, where relevant, Git commit SHAs.
4. **No unsupported affiliation claims.** Stanford, MIT, Hugging Face, Big Four firms, banks, regulators, and technology vendors are external reference points unless a written agreement states otherwise.
5. **Human Gate remains mandatory.** No external framework bypasses NAAIL evidence, professional-review, privacy, security, or scientific-validation controls.
6. **No confidential client data in public examples.** Use synthetic Client XYZ and neutral fictional firms.

## Recommended execution roles

### Hugging Face smolagents

Preferred lightweight execution candidate for tool-using and managed agents. Typical NAAIL mapping:

- `CodeAgent` → quantitative/data-analysis specialist in a sandboxed environment;
- `ToolCallingAgent` → controlled standards/evidence lookup specialist;
- managed agents → specialist delegation under a NAAIL supervisor.

### Stanford DSPy

Preferred optimization/evaluation layer for:

- structured LM programs;
- RAG and evidence workflows;
- evaluator-driven optimization;
- controlled comparison of prompts/modules/specifications.

NAAIL must optimize against **frozen professional or scientific evaluation criteria**, never p-values or favorable conclusions alone.

### Stanford STORM / Co-STORM

Preferred research/knowledge-curation reference for:

- multi-perspective questioning;
- evidence discovery and synthesis;
- expert/moderator discussion;
- human participation in knowledge curation.

NAAIL extensions add authoritative-professional evidence hierarchy, contradiction tracking, Evidence Passport™, Professional Decision DAG™, falsification, and Human Gate.

### MIT SceneSmith and Murakkab

These are currently treated as **research inspirations**, not runtime dependencies:

- SceneSmith → compositional, simulation-ready Digital Twin design principles;
- Murakkab → adaptive workflow planning, parallel/sequential execution decisions, and resource-aware orchestration.

## Professional Swarm execution contract

Every material NAAIL swarm run should preserve:

```text
run_id
study_or_case_id
student_or_researcher_initial_judgment
selected_agents
agent_roles
model/provider identifiers
source/evidence identifiers
tool calls
inter-agent handoffs
critic/defender disagreements
falsification checks
evaluation metrics
Professional Decision DAG
Evidence Passport
Human Gate status
limitations
```

## Current status

This public package is **integration scaffolding**. It does not claim that Stanford DSPy, STORM/Co-STORM, smolagents, SceneSmith, or Murakkab have been fully benchmarked inside NAAIL against the frozen professional benchmark suite yet.

A capability moves from `ADAPTER_READY` to `VALIDATED` only after reproducible execution, frozen evaluation, failure analysis, regression testing, and Human Gate review.
