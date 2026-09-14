# NAAIL OpenLab™ — Prototype Status V0.4

## Prototype 003 — three-case Audit Digital Twin benchmark

NAAIL OpenLab has advanced to **Prototype 003**, extending the synthetic Audit Digital Twin from one Revenue Recognition case to a frozen three-domain benchmark:

1. **Revenue Recognition & Cut-off**
2. **Goodwill Impairment**
3. **ICFR Deficiency**

Prototype 003 also defines a common architecture-comparison harness for:

- deterministic baseline;
- single-agent AI;
- sequential-agent AI;
- governed multi-agent AI.

### Scientific-integrity rule

Only the deterministic baseline is currently executed. The three AI architectures are registered but remain **`NOT_EXECUTED_PROVIDER_REQUIRED`** until a real provider/model adapter is configured and run against the same frozen cases. NAAIL does not substitute simulated or placeholder AI outputs for empirical model evidence.

### Frozen deterministic control results

#### Revenue Recognition & Cut-off

- planted exceptions: `TX-002`, `TX-003`;
- proposed adjustment: **EUR 190,000**;
- planning materiality: **EUR 120,000**;
- precision / recall: **1.00 / 1.00**;
- false positives / false negatives: **0 / 0**.

#### Goodwill Impairment

- planted valuation exceptions: `GW-DR`, `GW-MAR`;
- synthetic estimated adjustment: **EUR 440,000**;
- planning materiality: **EUR 150,000**;
- precision / recall: **1.00 / 1.00**;
- false positives / false negatives: **0 / 0**.

#### ICFR Deficiency

- planted control deficiencies: `CTRL-JE-02`, `CTRL-IT-03`;
- synthetic estimated exposure: **EUR 530,000**;
- planning materiality: **EUR 120,000**;
- precision / recall: **1.00 / 1.00**;
- false positives / false negatives: **0 / 0**.

These values are properties of deliberately constructed synthetic cases. They are not evidence of real-world audit effectiveness, impairment measurement, control-deficiency severity, or professional assurance quality.

### Governance preserved across all cases

Prototype 003 preserves:

- Evidence Passport™ with reproducible source hashing;
- case-specific assertions and evidence identifiers;
- Professional Decision DAG™;
- mandatory `PENDING_HUMAN_APPROVAL` Human Gate;
- RPA, AA, EG, PS, DS and DIST;
- precision / recall and false-positive / false-negative tracking;
- provider-neutral model-adapter boundaries;
- frozen regression tests.

The private regression suite contains **7 tests**, all passing at the Prototype 003 validation checkpoint.

### Public/private boundary

The public repository intentionally discloses the research-safe benchmark design, deterministic control results, evaluation logic and governance principles only. Detailed orchestration logic, unpublished provider adapters, private prompts/specifications, benchmark extensions and patent-sensitive implementation remain in the private NAAIL R&D master pending IP review.

### Independence and rights

This prototype is independent research software using fictional clients and synthetic evidence. It does not reproduce proprietary Big Four platforms, source code, prompts, screenshots, confidential methodology or client data.

### Next milestone — Prototype 004

Configure real provider adapters in the private R&D environment and run **blinded, frozen-evidence comparisons** of single-agent, sequential-agent and governed multi-agent architectures. Provider runs must use the same case versions, Evidence Passports, evaluation metrics, Decision DAG controls and Human Gate. Any model comparison must report failures, cost, latency, false positives/negatives and human overrides—not only favorable outputs.
