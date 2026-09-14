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

## 37-role Audit Digital Twin
The canonical Audit Digital Twin contains 36 operational roles plus an Audit Scientific Supervisor. The supervisor observes and evaluates the system; it does not replace the human engagement/research owner.

## Agent lifecycle
`proposal → sandbox → unit tests → frozen evals → adversarial tests → Digital Twin benchmark → human review → approved research release → monitored use → periodic re-evaluation → retirement`

## Provider neutrality
NAAIL may implement adapters for OpenAI, Google, Microsoft, local/open models, or future providers. An agent's professional definition and evaluation contract must not depend on a single model vendor.
