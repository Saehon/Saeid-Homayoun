# NAAIL OpenLab™ — Open-Source Student Agent Lab

**Target:** NAAIL OpenLab v0.2.4  
**Audience:** bachelor, master, doctoral, executive/professional education  
**Primary environment:** synthetic Client XYZ / public or properly licensed evidence only

## Learning objective

Students learn to build, compare, challenge, document, and govern agentic AI systems in accounting, auditing, assurance, finance, sustainability, and empirical research. The objective is not to teach blind automation. The objective is to teach evidence-grounded professional judgment, reproducibility, model skepticism, and appropriate human escalation.

## Supported framework families

The lab can use one or more of the following upstream open-source projects through a NAAIL adapter boundary:

- Google Agent Development Kit (ADK)
- Microsoft Agent Framework
- CAMEL-AI
- Hugging Face smolagents
- Haystack
- Model Context Protocol Python SDK
- Ollama
- LlamaIndex
- OpenAI Agents SDK
- GPT Researcher
- Browser Use
- OpenHands
- MetaGPT
- CrewAI

See [`../../OPEN_SOURCE_AGENT_STACK.md`](../../OPEN_SOURCE_AGENT_STACK.md) and the machine-readable [`../../integrations/open_source_agents/registry.json`](../../integrations/open_source_agents/registry.json).

## Recommended first classroom implementation

### Lab 1 — Local educational audit agent

Use:

```text
Ollama + compatible local model + smolagents + synthetic Client XYZ
```

Student task:
1. inspect the frozen synthetic evidence;
2. identify the audit risk and affected assertions;
3. propose procedures;
4. cite evidence IDs;
5. disclose uncertainty;
6. identify contradictory evidence;
7. choose ACCEPT_AGENT, MODIFY_AGENT, REJECT_AGENT, REQUEST_MORE_EVIDENCE, or ESCALATE_TO_HUMAN;
8. submit a reproducible run manifest.

### Lab 2 — Framework comparison

Run the same frozen case under two orchestration frameworks, for example:

```text
Google ADK vs Microsoft Agent Framework
```

Hold constant, to the extent technically feasible:
- case evidence;
- learning objective;
- agent role specification;
- model/provider class;
- temperature/sampling policy;
- tool permissions;
- output schema;
- evaluation rubric.

Compare:
- evidence grounding;
- invented evidence;
- risk–procedure alignment;
- assertion alignment;
- handoff quality;
- reproducibility;
- latency/cost where applicable;
- error propagation;
- Human Gate compliance.

### Lab 3 — Multi-agent professional skepticism

Use CAMEL-AI, MetaGPT, CrewAI, or another approved multi-agent framework to implement:

```text
Planner → Auditor → Specialist → Critic → Reviewer
```

Require the Critic to search for contradictory evidence and the Reviewer to reject any unsupported conclusion. No agent may approve its own material output.

### Lab 4 — Evidence/RAG comparison

Use Haystack and/or LlamaIndex to compare retrieval strategies over an instructor-approved evidence corpus. Require source provenance and explicit evidence IDs. Retrieval quality is evaluated separately from answer fluency.

### Lab 5 — Research co-scientist

Use GPT Researcher, Browser Use, OpenHands, or related approved tools to convert a research question into:

```text
Question → literature/evidence → competing hypotheses → ERA-style design → data/code → empirical test → robustness/falsification → replication package → Human Gate
```

Generated literature summaries or code are not treated as scientific findings until independently checked.

## Common NAAIL evaluation rubric

Every material lab should score, where relevant:

- **RPA** — Risk–Procedure Alignment
- **AA** — Assertion Alignment
- **EG** — Evidence Grounding
- **PS** — Professional Skepticism
- **DS** — Documentation Sufficiency
- **DIST** — Distortion / unsupported-claim control
- **AIV** — AI Verification
- **CER** — Contradictory Evidence Recognition
- **HOR** — Human Override Reasoning
- **ESC** — Escalation Judgment

Instructors may add standard predictive or information-retrieval metrics where appropriate, but those metrics do not replace professional/evidence evaluation.

## Student submission package

Each student/team should submit:

```text
README.md
agent_card.yaml or equivalent
run_manifest.json
framework_version.txt
evidence_manifest.json
prompt_or_role_specification/
outputs/
evaluation/
limitations.md
human_gate_decision.md
```

The package should record the framework, framework version or commit, model/provider, tool access, evidence corpus version, seeds/sampling settings where available, failed runs, and known limitations.

## Academic integrity and privacy

- Students must disclose material AI assistance according to course/university rules.
- Synthetic, public, or properly licensed evidence should be used by default.
- Confidential client data and proprietary audit-firm methods are prohibited unless a separately governed environment and written authorization exist.
- Individual student performance is not automatically shared with industry partners.
- Academic grading and recruitment use remain separable.
- Recruitment decisions may not be automated from NAAIL scores.

## Framework/license rule

Framework inclusion in NAAIL is not a license grant from NAAIL. Before a course distributes, modifies, or bundles an upstream project, the instructor or technical owner must verify the current upstream license, version-specific obligations, model-weight terms, API terms, and institutional IT/security requirements.

## Research design opportunities

The lab can support publishable education/research questions such as:

- Do governed multi-agent workflows improve evidence grounding relative to single-agent workflows?
- Does requiring evidence IDs reduce unsupported audit conclusions?
- Do critic–reviewer role separations improve contradictory-evidence recognition?
- Does local-model deployment materially change audit reasoning quality, reproducibility, or student learning?
- Which orchestration characteristics predict Human Gate escalation quality?
- Does framework choice matter after holding model, evidence, prompts, and tool access constant?

These are research questions, not pre-committed superiority claims.

## Release boundary

This document is a public teaching design. A framework is considered **executed in NAAIL** only when a version-pinned run exists with retained inputs, outputs, evaluation artifacts, and Human Gate state. Registry inclusion alone is not execution or validation.