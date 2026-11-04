# PR A — Q1 + Q2 + Q4 evidence record (2026-10-02)

Scope: engineering and record corrections only. Q5 Microsoft COVID rule/scan is explicitly excluded from this PR.

## Q1 — Claude P2 intake
- ZIP SHA-256: `fedaa45c26709311a06b44b8bcd52beeb26653f0980534371216b719e0a026cd`
- `MANIFEST_P2.md`: `7eaae82ed09d6beac7c9ff6c4d56c90ab97437e8d3e9e3ed64a4100cb453b398`
- `p2_adversarial_v2_executable.py`: `0e22e75139dc2c827a4badfa66cd888bb3d63ae54fc1651e850e706196bfc1b8`
- `p2_falsification.py`: `b7d6f17c85367818d8834c4aacd013858cfc0ac17991a30dcfc407b33eafa8ee`
- `p2_result.json`: `c23077e6c37198163753d211a6de36488c9101b4297e2189b50a8f2dfdc90fce`
- `falsification_result.json`: `a256dbb356ce5f5ea3b266f12021126895f6b4909d5b372df29be12313943877`
- Four payload hashes match `MANIFEST_P2.md`; originals unchanged.
- Working-branch source intake commit: `edf36ae54f752fc9d951c0160961d99eacf458ad`.
- Clean PR-A integration commit: `bdd9b0af2caf75f22547a582175a4c2732a3bd77`.

## Q2 — four-step CI
CI-EVIDENCE: run `37004149967`, job `110828395512`, CPython `3.12.14`, conclusion `success`.

| Step | Exit code | Conclusion |
|---|---:|---|
| Original P7 integration harness | 0 | success |
| Claude P7 regression v2 | 0 | success |
| Executable P2 adversarial benchmark | 0 | success |
| P2 falsification suite | 0 | success |

P2 executable benchmark: 19/19 designed synthetic fixtures met their outcome rules. This is engineering evidence only, not real-world detection performance.

Falsification suite: 30 clean packages, 0 packages with findings; 1/9 evasion probes caught and 8/9 missed; detected taxonomy IDs were deterministic across reruns.

## Q4 — consistency fixes
- Canonical corrected graph: `evidence-graph/evidence_graph_v1_1_case001.json`.
- FilingLag claim separated as `VERIFIED`; Microsoft COVID claim remains `PARTIAL`.
- Author-output 264/264 summary remains `PARTIAL` until Q6 provides inspectable per-cell paper/log evidence.
- `phase_register.json` records `microsoft_sec_one_company = PARTIAL` and retains `POC criteria met = 7 of 10`.
- Legacy labels are mapped in `derived/NONCANONICAL_ASSURANCE_LABEL_MAPPING_2026-10-02.md` without rewriting immutable originals.

## Q5 boundary / secret status
Q5 is excluded from PR A. A prior attempted Q5 workflow run `37003148170` showed `EDGAR_IDENTITY` as empty and failed before any SEC scan with: `EDGAR_IDENTITY is required and must be supplied by the CI secret.`
Therefore the latest executable evidence is that the secret was not available to that workflow. No Q5 scientific result is claimed.

POC criteria met: 7 of 10.
POC_COMPLETE = FALSE.
V1_COMPLETE = FALSE.
