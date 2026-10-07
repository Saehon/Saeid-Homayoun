# B6 Claude Review Package — Pilot Comparison Protocol

Date: 2026-10-07  
Status requested: independent review of a pilot-comparison protocol and metric specification frozen before data.

PR: pending creation  
Validated commit: pending single guard run  
Base: `main` at `d48faf52bd27a6796063f10b73657eb1d9cf384b`

## Boundary

This package contains only the comparison protocol, metric specification, freeze manifest, human-readable summary, invariant test, and narrow CI. It contains no holdout probes, candidates, case selection, evaluation inputs, ground-truth labels, predictions, scoring outputs, detector changes, or scientific claims.

## Prior exposure

The operator has seen the detector and the disclosed Benchmark V2 development probes and results, including the 8-of-9 missed-probe limitation. The operator has not seen Benchmark V3 probes or ground truth and has not seen real-case evaluation labels. No evaluation data, arm output, or result existed when B6 was frozen.

## Frozen fingerprints

| File | SHA-256 |
| --- | --- |
| `pilot_comparison_protocol_v1.json` | `128e1d3f385435a2181b79a0432f884071322effcae49b097d6368b3955e9081` |
| `pilot_comparison_metrics_v1.json` | `150eb820a0461d8d74faf1c5af162dac90018c0321aa188af4d602556b3948bb` |

## Design requiring review

- Arms: frozen NAAIL system, blinded human evaluation coders, and a deterministic always-no-error baseline.
- Strata: independently authored sealed Benchmark V3 holdout and predefined real-case assessment units, reported separately.
- Primary metrics: raw confusion counts plus precision, recall, and F1 under a frozen zero-denominator convention.
- Secondary outputs: taxonomy micro/macro metrics, exact-set matches, abstentions, missing outputs, and item-level disagreement.
- Paired evidence: prespecified arm deltas, exact McNemar tests, and a paired item bootstrap; none is an automatic gate.
- Exactly one scoring invocation after all inputs, outputs, code, environment, exposures, and approvals are frozen and hashed.

## Validation

- Local Python compile: exit 0.
- Local freeze-hash and invariant suite: exit 0, `B6 pilot comparison protocol invariants: PASS`.
- A subsequent glob-based packaging hash command returned exit 1 only because it encountered the generated `__pycache__` directory. The test was not rerun. The materially different file-only hash command exited 0; the exact failure and repair are preserved in `derived/OPEN_REPAIR_QUEUE.md` as `NAAIL-B6-LOCAL-HASH-ENUMERATION-001`.
- Single authorized CI: pending PR creation; workflow accepts only the pull-request `opened` event.

## Required review

1. Does the always-no-error baseline provide a sufficiently bounded, leakage-free comparator?
2. Are human evaluation coders adequately separated from probe authorship, ground truth, and adjudication?
3. Are precision, recall, F1, zero-denominator, abstention, missing-output, and paired-comparison rules fully prespecified?
4. Does the one-run rule prevent result selection while preserving a failed invocation as evidence?
5. Are the Phase C execution dependencies complete and correctly human-gated?

`POC_COMPLETE = FALSE`; `V1_COMPLETE = FALSE`.
