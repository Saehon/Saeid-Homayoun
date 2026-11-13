# B6 Claude Review Package — Pilot Comparison Protocol

Date: 2026-10-07  
Status requested: independent review of a pilot-comparison protocol and metric specification frozen before data.

PR: [#133](https://github.com/Saehon/Saeid-Homayoun/pull/133)  
Validated commit: `7c566826f4b49b9ad7e9ca890ef6198e5309a0e8`  
Base: `main` at `d48faf52bd27a6796063f10b73657eb1d9cf384b`

## Boundary

This package contains only the comparison protocol, metric specification, freeze manifest, human-readable summary, invariant test, and narrow CI. It contains no holdout probes, candidates, case selection, evaluation inputs, ground-truth labels, predictions, scoring outputs, detector changes, or scientific claims.

## Prior exposure

The operator has seen the detector and the disclosed Benchmark V2 development probes and results, including the 8-of-9 missed-probe limitation. The operator has not seen Benchmark V3 probes or ground truth and has not seen real-case evaluation labels. No evaluation data, arm output, or result existed when B6 was frozen.

## Frozen fingerprints

| File | Git blob | SHA-256 |
| --- | --- | --- |
| `pilot_comparison_protocol_v1.json` | `311984dd3a0cd266bc79ed587f5c208a2f38bdf5` | `128e1d3f385435a2181b79a0432f884071322effcae49b097d6368b3955e9081` |
| `pilot_comparison_metrics_v1.json` | `52262a31646ce1a222ced3953b415f74ed639d66` | `150eb820a0461d8d74faf1c5af162dac90018c0321aa188af4d602556b3948bb` |
| `pilot_comparison_protocol_freeze_manifest_v1.json` | `c0ab6590fcb85712bc194af80d535ad4f9876324` | `4df28f179c56cbe8cb6a0506f5dae895b52c7d61c27e4e50f8e491413f12e8e3` |
| `PILOT_COMPARISON_PROTOCOL_V1.md` | `2034602e2f19196c09a03ad5b569bf7e2cd0a0d8` | `26203c2be773168ae6bf960d03513804adc4f26845f7c158b91d865ff2b15082` |
| `test_b6_pilot_comparison_protocol.py` | `83187998489549158e18e5e408648b0ad74ff743` | `cc3d816c44ae6b77137f934f8e3c24250a42e4b076718d254e0ee3a2ce772ccd` |
| `naail_v1_b6_pilot_comparison_protocol.yml` | `f9054c86565e6a3855faf09418a45533358ab1ab` | `4957eb4ce24ed17f9cafc3aefd5f6512013f3576dff38142d1e3b1314ac803a2` |

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
- Single authorized CI: [run 37569522474](https://github.com/Saehon/Saeid-Homayoun/actions/runs/37569522474), run number 1, `success`.
- Job `112624753796`, `b6-pilot-comparison-protocol-guard`, `success`; compile and invariant steps both succeeded.
- The workflow accepts only the pull-request `opened` event. This package finalization cannot trigger the guard because `synchronize` is excluded. No rerun is authorized.

## Required review

1. Does the always-no-error baseline provide a sufficiently bounded, leakage-free comparator?
2. Are human evaluation coders adequately separated from probe authorship, ground truth, and adjudication?
3. Are precision, recall, F1, zero-denominator, abstention, missing-output, and paired-comparison rules fully prespecified?
4. Does the one-run rule prevent result selection while preserving a failed invocation as evidence?
5. Are the Phase C execution dependencies complete and correctly human-gated?

`POC_COMPLETE = FALSE`; `V1_COMPLETE = FALSE`.
