# NAAIL OpenLab™ — Prototype Status V0.4

## Prototype 002 — modular Audit Digital Twin baseline

NAAIL OpenLab has progressed from the first deterministic scaffold to **Prototype 002**, a modular, provider-neutral research baseline for a synthetic **Client XYZ — Revenue Recognition & Cut-off** case.

### What Prototype 002 adds

The research-safe public scope now includes:

- an explicit **Materiality Agent**;
- an explicit **Risk Agent**;
- an evidence-linked **Evidence Agent**;
- a reproducible **Evidence Passport™** concept linking case hash, evidence IDs, assertions, adapter identity and limitations;
- a persistent **Professional Decision DAG™** concept linking case → materiality → risk → evidence → judgment → critic → Human Gate;
- a provider-neutral model-adapter contract so deterministic, OpenAI, Gemini, Microsoft/Azure, local/open-model or future adapters can be evaluated against the same frozen case;
- regression tests for frozen exceptions, proposed adjustment, evidence hashing, DAG termination and Human Gate enforcement.

### Frozen baseline result

The synthetic benchmark contains two planted year-end cut-off exceptions. The deterministic control condition identifies both and produces:

- flagged evidence IDs: `TX-002`, `TX-003`;
- proposed adjustment: **EUR 190,000**;
- planning materiality: **EUR 120,000**;
- baseline precision: **1.00**;
- baseline recall: **1.00**;
- false positives: **0**;
- false negatives: **0**;
- final state: **`PENDING_HUMAN_APPROVAL`**.

These values are properties of the frozen synthetic benchmark only. They are not evidence of real-world audit effectiveness.

### NAAIL evaluation metrics

Prototype 002 retains the NAAIL research metrics:

- **RPA** — Risk–Procedure Alignment;
- **AA** — Assertion Alignment;
- **EG** — Evidence Grounding;
- **PS** — Professional Skepticism;
- **DS** — Documentation Sufficiency;
- **DIST** — Decision / Inference Stability;
- precision / recall;
- false-positive / false-negative rates.

### Research engineering rule

The deterministic adapter is the control condition. Future AI/model adapters must consume the same frozen evidence and cannot modify gold labels, bypass evidence/provenance checks, bypass the critic/reviewer stage, or self-approve a high-risk conclusion.

### Public/private boundary

The public repository intentionally discloses the research-safe benchmark design, evaluation logic, governance principles and status only. Detailed orchestration logic, private benchmark extensions, unpublished agent specifications, prompts, patent-candidate mechanisms and pre-commercial implementation remain in the private NAAIL R&D master pending IP review.

### Independence and rights

This prototype is independent research software. It does not reproduce proprietary Big Four platforms, source code, prompts, screenshots, confidential methodology or client data. Firm and client simulations are fictional and synthetic.

### Next milestone — Prototype 003

Expand the benchmark beyond revenue recognition by adding **Goodwill Impairment** and **ICFR Deficiency** cases, then compare deterministic baseline, single-agent, sequential-agent and governed multi-agent orchestration under frozen evidence, the same metrics, Evidence Passport™, Decision DAG™ and Human Gate.
