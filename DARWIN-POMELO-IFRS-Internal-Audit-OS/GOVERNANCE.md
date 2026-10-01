# Governance — DARWIN-POMELO IFRS Internal Audit OS

## Non-negotiable invariants

```text
human_gate_required = true
agent_self_approval_allowed = false
model_confidence_is_evidence = false
agent_consensus_is_truth = false
synthetic_evidence_equals_real_evidence = false
provider_change_redefines_professional_meaning = false
unsupported_material_claim_allowed = false
contradictory_evidence_may_be_deleted = false
credentials_in_repository = false
```

## Evidence rules

Every material conclusion must preserve source, version/effective date, evidence ID, run ID, tool/model version, uncertainty and human decision state.

## Public/private boundary

Public GitHub content may include:
- high-level architecture;
- non-enabling specifications;
- synthetic examples;
- interfaces/schemas;
- frozen benchmark definitions;
- governance and evaluation methodology.

Private content includes:
- patent-sensitive routing logic;
- proprietary evaluators and scoring functions;
- unpublished methods;
- private data;
- credentials/secrets;
- partner-confidential materials;
- production adapters containing confidential configuration.

## Professional boundary

The project is a research/prototype architecture. A successful run, benchmark result or model agreement is not an audit opinion, regulator approval, IFRS Foundation certification or substitute for qualified professional judgment.
