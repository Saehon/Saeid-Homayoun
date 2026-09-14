# NAAIL OpenLab™ — Agent Governance Standard

NAAIL agents are governed software components, not autonomous authorities. Every agent must have a documented purpose, owner, risk class, allowed tools, evidence requirements, evaluation set, and human-approval rule.

## Required Agent Card
Each agent must define:
- `agent_id` and semantic version;
- role and professional scope;
- intended users;
- approved model/provider classes;
- allowed tools and data classes;
- prohibited actions;
- required evidence sources;
- input/output schema;
- handoff targets;
- human-approval conditions;
- failure behavior;
- evaluation datasets and metrics;
- known limitations;
- change history.

## Risk classes
- **R0 — Educational helper:** synthetic/non-sensitive explanation and tutoring.
- **R1 — Analytical assistant:** analysis with no professional conclusion.
- **R2 — Professional-support agent:** produces evidence or recommendations requiring reviewer approval.
- **R3 — High-impact specialist:** material audit judgments, controls conclusions, fraud flags, CAM/KAM recommendations, or similar outputs; mandatory independent review and Human Gate.

## Educational Proxy Agent

The **Educational Proxy Agent** is the canonical NAAIL mechanism for university–industry teaching partnerships. It is a research-safe teaching approximation and **must not be represented as a replica of a professional firm's proprietary production AI system**.

An Educational Proxy Agent normally operates at **R0** and may enter **R1** for structured analytical exercises. It must not be promoted to R2/R3 merely because a case simulates professional judgment.

Each proxy-agent card must additionally define:

- partner status: `INDEPENDENT_SIMULATION`, `PARTNER_REVIEWED`, or `FORMALLY_SPONSORED`;
- permitted branding and attribution;
- synthetic/licensed dataset scope;
- learning objectives;
- planted teaching errors, if any;
- instructor key/version;
- student challenge/override requirements;
- prohibited claims about partner endorsement or production-system equivalence;
- student-data and recruitment-data rules.

By default, partner names/logos may not be used and the public simulation should use neutral labels such as **Firm Alpha**, **Firm Beta**, or **Industry Partner**.

## Student interaction contract

For material teaching tasks, the agent should expose enough structure for a student to test it. Recommended fields include:

- risk statement;
- affected assertions;
- suggested procedures;
- evidence IDs;
- contradictory evidence IDs, where identified;
- uncertainties;
- alternative explanations;
- limitations;
- required human review.

The student decision layer should support at least:

- `ACCEPT_AGENT`
- `MODIFY_AGENT`
- `REJECT_AGENT`
- `REQUEST_MORE_EVIDENCE`
- `ESCALATE_TO_HUMAN`

A student must be able to disagree with the agent without being penalized merely for disagreement; evaluation should focus on evidence, reasoning, professional skepticism, and documentation.

## Runtime rules
1. Least-privilege tool access.
2. Structured inputs/outputs for material tasks.
3. Evidence links for material assertions.
4. Guardrails at user-input, tool, and final-output boundaries where appropriate.
5. Explicit handoffs rather than hidden responsibility transfer.
6. No agent may approve its own material conclusion.
7. R2/R3 outputs require independent validation.
8. Failed validation must stop or downgrade the workflow, not be silently ignored.
9. Every material run must be traceable to agent/model/tool versions.
10. Synthetic education/research environments remain separate from any future production environment.
11. Educational proxy agents may not receive confidential client data or proprietary firm methodology unless a separately governed environment and written authorization explicitly permit it.
12. Recruitment decisions must not be automated from NAAIL student scores.
13. Academic grading and recruitment pathways should remain separable.
14. Individual student performance may be disclosed to a partner only with explicit student consent and appropriate institutional/privacy approval.

## 37-role Audit Digital Twin
The canonical Audit Digital Twin contains 36 operational roles plus an Audit Scientific Supervisor. The supervisor observes and evaluates the system; it does not replace the human engagement/research owner.

The student-learning layer may expose a safe subset of those roles through proxy agents. It should not expose private orchestration logic, unpublished prompts, restricted benchmarks, or proprietary partner methods.

## Agent lifecycle
`proposal → sandbox → unit tests → frozen evals → adversarial tests → Digital Twin benchmark → human review → approved research release → monitored use → periodic re-evaluation → retirement`

For educational proxy agents, add:

`learning-objective review → instructor-key validation → student pilot → aggregate learning evaluation → curriculum/partner review`

## Provider neutrality
NAAIL may implement adapters for OpenAI, Google, Microsoft, local/open models, or future providers. An agent's professional definition and evaluation contract must not depend on a single model vendor.

## Open-source educational agent adapters

NAAIL may use third-party open-source agent frameworks through a governed adapter boundary. The current v0.2.4 target registry includes a core education stack of **Google ADK, Microsoft Agent Framework, CAMEL-AI, Hugging Face smolagents, Haystack, MCP Python SDK, and Ollama**, plus an extended comparison ecosystem including LlamaIndex, OpenAI Agents SDK, GPT Researcher, Browser Use, OpenHands, MetaGPT, and CrewAI.

For every open-source framework used in a NAAIL run, record where applicable:

- upstream repository;
- exact release, package version, or commit;
- current upstream license review state;
- model/provider and model identifier;
- tool permissions;
- evidence corpus/version;
- agent role and risk class;
- handoff trace;
- failed-run state;
- evaluation output;
- Human Gate state.

Registry inclusion is **not** proof that a framework has been installed, executed, benchmarked, security-reviewed, or validated. No comparative-superiority claim may be made without frozen tasks, equivalent evidence access, declared versions, prespecified metrics, retained failed/null results, robustness analysis, and Human Gate review.

Upstream project licenses, trademarks, hosted APIs, model weights, and release-specific obligations remain external to the NAAIL license. Do not copy or relicense third-party code into NAAIL merely because it is used in a teaching or research workflow.

Canonical specification: [OPEN_SOURCE_AGENT_STACK.md](./OPEN_SOURCE_AGENT_STACK.md)  
Machine-readable registry: [integrations/open_source_agents/registry.json](./integrations/open_source_agents/registry.json)

## Related education specifications

- [NAAIL Big Four Student Agent Academy™](./docs/education/NAAIL_BIG4_STUDENT_AGENT_ACADEMY.md)
- [Digital Twin Student Simulation™](./docs/education/DIGITAL_TWIN_STUDENT_SIMULATION.md)
- [Open-Source Student Agent Lab](./docs/education/OPEN_SOURCE_AGENT_LAB.md)