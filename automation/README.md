# ECONOVA-S™ Automation Developer Guide

This folder contains the provider-neutral AI-to-AI scientific automation runtime.

## Components

- `orchestrator.py` — role routing, chain hashes, failure propagation, independence classification, and scientific safety invariants.
- `ai_handoff.schema.json` — machine-readable handoff contract.
- `validate_handoff.py` — single-handoff schema/hash validation.
- `test_orchestrator.py` — orchestration, hash-chain, and failure-containment tests.
- `RELIABILITY_STANDARD.md` — reliability, observability, least-privilege, and Human Gate requirements.
- `sample_handoff.json` — canonical example handoff.

## Runtime roles

1. Explorer / Hypothesis Agent
2. Theory & Causal DAG Agent
3. Empirical Design Agent
4. Independent Replicator
5. Scientific Red-Team
6. Welfare & Economic Value Reviewer
7. Evidence Passport Agent
8. Human Gate — external to autonomous agents

## Run offline

```bash
python automation/orchestrator.py \
  --question "Does AI improve measured productivity?" \
  --output automation/artifacts/demo_chain.json

python -m pytest -q automation/test_orchestrator.py
python automation/validate_handoff.py automation/sample_handoff.json
```

The deterministic adapter exists only to validate orchestration mechanics. It does not simulate scientific competence.

## Adding a live model adapter

Implement the `AgentAdapter` interface from `orchestrator.py`:

```python
class MyAdapter:
    name = "my-provider-or-model"
    version = "pinned-version"

    def run(self, role: str, payload: dict) -> AgentResult:
        # 1. consume only the authorized payload
        # 2. call the model/tool
        # 3. return structured AgentResult
        # 4. never authorize scientific discovery
        ...
```

Then pass a role-to-adapter map to `Orchestrator(adapters=...)`.

For publication-grade independence, do not route Generator, Replicator, and Red-Team roles through identical hidden context and identical configurations. The runtime records whether independence is role-only or role+tool.

## Security and least privilege

- Do not hard-code API keys.
- Do not commit secrets or proprietary data.
- Public CI uses only deterministic offline execution.
- Live model execution must use explicitly authorized secret storage.
- Keep model/tool permissions narrower than repository permissions.
- Do not let an agent merge, publish, release, or authorize a scientific claim automatically.

## Required observability

A production run should retain:

- task/run identifiers;
- stage sequence;
- model/tool/version;
- evidence/provenance;
- assumptions and contradictions;
- failure reasons and risk flags;
- handoff parent/content hashes;
- final chain hash;
- Human Gate decision.

## Promotion criteria

A live adapter is experimental until it passes:

- deterministic contract tests;
- provenance completeness;
- secret-leakage checks;
- failure-containment tests;
- independent reconstruction tests;
- benchmark/gold-set evaluation;
- red-team challenge;
- human review.

## Scientific invariant

```text
agent_consensus_is_scientific_truth = false
human_gate_required = true
discovery_claim_allowed = false
```

ECONOVA-S automates scientific execution and verification workflows; it does not automate scientific authority.
