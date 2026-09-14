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

### 7. FT50 / AJG 4* external benchmark tests
Selected public replication repositories from FT50 and AJG/ABS 4* journals may be registered as external scientific benchmarks. They are not treated as NAAIL-owned code by default.

Each external benchmark must pass the applicable controls in the **NAAIL Scientific Replication Arena™**:
- source/publication verification;
- rights and license review;
- exact Git commit pinning before execution;
- environment reconstruction;
- original-result replication;
- independent/clean-room reproduction where feasible;
- specification robustness;
- causal or ML/AI diagnostics as appropriate;
- adversarial Critic–Defender review;
- temporal/out-of-sample validation;
- cross-dataset or Digital Twin testing where appropriate;
- complete Chain-of-Evidence;
- Human Gate.

Canonical resources:
- `benchmarks/ft50_abs4/registry.json`
- `benchmarks/ft50_abs4/BENCHMARK_PROTOCOL.md`
- `benchmarks/ft50_abs4/validate_registry.py`
- `tests/SCIENTIFIC_REPLICATION_ARENA.md`
- `external/FT50_ABS4_SOURCE_POLICY.md`

External benchmark publication status must never substitute for reproducibility, identification validity, falsification, provenance, or evidence quality.

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
