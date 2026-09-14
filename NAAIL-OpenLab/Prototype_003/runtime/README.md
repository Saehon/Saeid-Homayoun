# NAAIL OpenLab — Prototype 003 Public Runtime

**Status:** executable public research checkpoint  
**Architecture target:** V2026.3  
**Current public release:** v0.2.3 / Prototype 003  
**Next milestone:** Prototype 004 — real-provider blinded architecture comparison

This directory implements the research-safe public runtime for Prototype 003 under the frozen rule:

> **Same case. Same evidence. Same gold labels. Same evaluator. Different execution architecture.**

## Scientific-integrity boundary

Prototype 003 registers four architecture conditions:

1. deterministic baseline — **executed**;
2. single-agent AI — **`NOT_EXECUTED_PROVIDER_REQUIRED`**;
3. sequential-agent AI — **`NOT_EXECUTED_PROVIDER_REQUIRED`**;
4. governed multi-agent AI — **`NOT_EXECUTED_PROVIDER_REQUIRED`**.

The public runtime **does not simulate AI outputs** and does not replace missing Gemini, Microsoft/Azure, OpenAI, local-model, or other provider runs with deterministic placeholders. A provider/model result becomes empirical evidence only after an actual adapter is configured and run against the same frozen case/evidence/gold/evaluator state.

## Three-case Prototype 003 registry

The public case registry records the validated synthetic benchmark checkpoint:

| Case | Deterministic result | Synthetic amount | Public detailed runtime |
|---|---|---:|---|
| Revenue Recognition & Cut-off | `TX-002`, `TX-003` | EUR 190,000 | Yes — research-safe migration included here |
| Goodwill Impairment | `GW-DR`, `GW-MAR` | EUR 440,000 | No — detailed implementation remains private pending IP review |
| ICFR Deficiency | `CTRL-JE-02`, `CTRL-IT-03` | EUR 530,000 | No — detailed implementation remains private pending IP review |

All three remain synthetic benchmark cases with mandatory `PENDING_HUMAN_APPROVAL`. The amounts and labels are benchmark properties, not claims about real entities, auditors, accounting failures, control failures, or assurance quality.

## What runs publicly now

The Revenue Recognition migration (`P003-B-REV-001`) reproduces the deterministic frozen benchmark with:

- planted exceptions `TX-002` and `TX-003`;
- proposed adjustment EUR 190,000;
- planning materiality EUR 120,000;
- Evidence Passport with hashes;
- Professional Decision DAG;
- RPA, AA, EG, PS, DS and DIST engineering-test fields;
- precision / recall and FP/FN tracking;
- mandatory Human Gate.

The other three architecture modes are emitted only as registered, non-executed conditions until a real provider is configured.

## Run

```bash
cd NAAIL-OpenLab/Prototype_003/runtime
python prototype003.py
```

The runner writes `outputs/latest_results.json` and reports the deterministic result plus explicit provider-required statuses.

## Test

```bash
python -m unittest discover -s tests -v
```

The current public test suite checks:

- v0.2.3 three-case registry state;
- frozen Revenue gold labels and adjustment;
- deterministic replay stability;
- frozen input hashes;
- Evidence/Human-Gate governance;
- bounded evaluator outputs;
- prohibition on fabricated AI results;
- no superiority/discovery claim.

No third-party Python package is required for this public scaffold.

## Governance invariants

```text
same_case_across_architectures = true
same_evidence_across_architectures = true
same_gold_labels_across_architectures = true
same_evaluator_across_architectures = true
human_gate_required = true
benchmark_leakage_allowed = false
simulated_ai_result_substitution_allowed = false
unsupported_discovery_claim_allowed = false
```

## Prototype 004 target

The next defensible step is to configure **real provider adapters in the private R&D environment** and run blinded frozen-evidence comparisons for single-agent, sequential-agent and governed multi-agent architectures. Each run must preserve provider/model/version metadata, Evidence Passport, Decision DAG, Human Gate, identical benchmark inputs, cost/latency, failures, false positives/negatives and human overrides.

Provider/runtime technology can change. The scientific contract may not silently change with it.

See also:

- `../../PROTOTYPE_STATUS_V0.4.md`
- `../../PROTOTYPE_003_EXECUTION_SPEC.md`
- `../../CURRENT_PROJECT_STATE.md`
- `../../versions/V2026.3_MULTI_AGENT_DIGITAL_TWIN.md`
