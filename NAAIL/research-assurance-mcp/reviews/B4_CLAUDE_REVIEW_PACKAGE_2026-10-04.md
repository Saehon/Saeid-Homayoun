# B4 Claude review package — Benchmark V3 holdout specification

Date: 2026-10-04  
PR: #121  
Branch: `naail/v1-b4-holdout-spec-2026-10-04`  
Specification head before this review-only packet: `492d8eaa6dbbbbabef78a41a09c80fdcb94da8b9`

## Review request

Review the protocol only. No probes, ground truth, evaluation data, detector changes, or scientific results exist in this scope.

Please assess:

1. whether the independence firewall is sufficient;
2. whether the 48-package allocation is scientifically defensible;
3. whether seal-before-score prevents leakage and post-result editing;
4. whether the metrics, uncertainty treatment, thresholds, and one-run rule are adequate;
5. whether execution is correctly blocked until human POC approval and independent authorship.

## Prior-exposure declaration

The GPT operator has seen the detector source/rules, Benchmark V2 results, and the nine disclosed V2 probes. The operator is permanently disqualified from authoring, editing, suggesting, previewing, or approving V3 probes or ground truth. This packet contains protocol text only.

## Frozen file fingerprints

| File | Git blob | SHA-256 |
|---|---|---|
| `v1-preparation/b4/benchmark_v3_holdout_spec_v1.json` | `80f0391b9746833cd47b3878a9a91b553f1ff4a8` | `3aac3ca725fc4c5afb48cc7e8bfcfaeb01025509aa19f62ab74706aadb03680b` |
| `v1-preparation/b4/BENCHMARK_V3_HOLDOUT_SPECIFICATION_V1.md` | `a66386871e0120fae97b1fc16776e5c71613e0a5` | `b7639494db3c2f953d0db5f15c52e5856ce13e04c4381d0d33405cd589b51842` |
| `v1-preparation/b4/test_benchmark_v3_holdout_spec.py` | `47344248a65b2344b7f8ae8c4aa418cdc02863ed` | `4300364fda7f334c386182a805c91391e9efaffda9fcb7a12198cf47c7bd948b` |
| `.github/workflows/naail_v1_b4_holdout_spec.yml` | `e9fef6f99649ebe14e0ec0b9b74d2f736ee617ba` | `7cc16157251cb21e16bc287c72f26bd3148cb5c2da11f85d808ba00b7d18cea8` |

The fingerprints above bind the candidate specification before any V3 probe or result exists. This review packet is outside the B4 CI path and does not alter those fingerprints.

## Validation evidence

- Local `py_compile`: exit 0.
- Local invariant test: exit 0.
- Local JSON parse: exit 0.
- Local YAML parse: exit 0.
- Single authoritative CI run: `37236679704`.
- CI job: `111537066229`.
- Compile step: success.
- Specification-invariant step: success.
- CI conclusion: success.
- CI URL: https://github.com/Saehon/Saeid-Homayoun/actions/runs/37236679704

## Frozen scientific boundaries

- Benchmark V2 remains the POC baseline and retains its 8-of-9 missed-probe limitation.
- V3 probes must be independently authored by an eligible human or separate agent.
- The operator will not author probes.
- No case selection or data retrieval is authorized.
- There will be one authoritative scoring run.
- Raw detector output is frozen before ground truth is released.
- Observed outcomes must be reported without tuning or replacement.
- V3 execution remains locked until human POC approval and Claude approval.

## Requested disposition

Return one of:

- `APPROVE_SPECIFICATION`;
- `CHANGES_REQUIRED`, with exact protocol corrections; or
- `REJECT_INDEPENDENCE_DESIGN`, with the reason.

This operator packet does not approve the specification and does not change any POC gate.
