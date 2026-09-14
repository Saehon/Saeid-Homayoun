# NAAIL OpenLab™ — Evaluation & Benchmark Standard

NAAIL follows an eval-first research engineering discipline: changes to agents, models, prompts, tools, retrieval, or workflows are accepted only when they pass prespecified tests.

## Evaluation layers
### 1. Component tests
- schema validity;
- deterministic utilities;
- retrieval/citation resolution;
- tool permission checks;
- data-rights checks.

### 2. Agent tests
- task completion;
- tool-call correctness;
- evidence grounding;
- citation validity;
- professional-scope compliance;
- refusal/escalation behavior;
- latency and cost.

### 3. Audit-quality metrics
- **RPA** — Risk–Procedure Alignment;
- **AA** — Assertion Alignment;
- **EG** — Evidence Grounding;
- **PS** — Professional Skepticism;
- **DS** — Documentation Sufficiency;
- **DIST** — Decision/Inference Stability;
- false-positive and false-negative rates;
- human override rate and reason.

### 4. Workflow tests
- handoff accuracy;
- dependency completion;
- checkpoint/resume behavior;
- guardrail enforcement;
- human-gate enforcement;
- trace completeness;
- failure recovery.

### 5. Digital Twin benchmarks
The same frozen synthetic case should run across Firm Alpha–Delta architectures using the same evidence. Compare risk identification, procedures, evidence use, conclusions, CAM/KAM recommendations, documentation, cost, latency, and stability.

### 6. Scientific-discovery tests
- literature novelty validation;
- identification validity;
- robustness;
- falsification;
- temporal/out-of-sample validation where appropriate;
- independent replication;
- complete Chain-of-Evidence;
- explicit human approval.

## Frozen benchmark policy
Keep separate:
- development cases;
- validation cases;
- Blind Gold cases;
- adversarial/red-team cases;
- temporal holdouts.

Never optimize directly against the Blind Gold set. Never select models or specifications solely because they produce lower p-values or more favorable conclusions.

## Release decision
A new component must show **no material regression** on critical safety/evidence metrics. Improvements in speed or cost cannot compensate for unacceptable deterioration in evidence quality, professional judgment, reproducibility, or safety.

## Evaluation manifest
Every benchmark run should record:
- run ID/date;
- dataset/case version;
- agent/model/tool/workflow versions;
- prompts/instructions version;
- configuration;
- metrics;
- failures;
- reviewer decision;
- approval status.
