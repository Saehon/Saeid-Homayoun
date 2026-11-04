# Decision Record: Benchmark V2 Freeze and Benchmark V3 Deferral

**Decision date:** 2026-10-02  
**Project:** NAAIL Research Assurance MCP  
**Scope:** POC Benchmark V2 / V1.4 Benchmark V3  
**Approved by:** User, 2026-10-02  
**Reviewed by:** Claude (independent review communicated by the user)

## Decision

Benchmark V2 is frozen unchanged as the POC benchmark baseline. Its purpose is to preserve an honest record of what the current detector could and could not detect at the time of the POC.

The V2 falsification suite caught 1 of 9 realistic evasion probes and missed 8 of 9. This is a limitation of the detector, not a failure of Benchmark V2. The misses are recorded as V1 requirements and do not invalidate the POC benchmark criterion.

## Evidence fingerprints

### Frozen benchmark

- Path: `benchmark/adversarial_benchmark_v2.json`
- Git blob SHA on PR #101 branch: `b90ee73073907baa5f577b0534b766ae29ed278b`
- SHA-256 recorded by the P2 manifest for the original unchanged fixture: `6237d06b0fbad0f236446df246d8f4fbdf4ee9256241be4706b7934e0ce06013`

### Derived executable/falsification package

Path: `derived/claude_2026-10-02/p2_executable/`

Git does not assign a file-blob SHA to a directory, so the frozen package is identified by its manifest/input snapshot plus the constituent file fingerprints:

- `MANIFEST_P2.md` — Git blob `15a5354dceca19c1c80f62ebdd44430f265b91fb`
- Manifest input snapshot ZIP SHA-256: `a58f98b684e9ab923c9fd5a1497678506d0b54ecf335b6f0bb1826d58ae0bd94`
- `p2_adversarial_v2_executable.py` — Git blob `bc9e06cb68dedf3308ceb624ce6ff99c6c71a599`; manifest SHA-256 `0e22e75139dc2c827a4badfa66cd888bb3d63ae54fc1651e850e706196bfc1b8`
- `p2_falsification.py` — Git blob `aa2683aff65dd54e31c7fc7c0ffe766030901ccf`; manifest SHA-256 `b7d6f17c85367818d8834c4aacd013858cfc0ac17991a30dcfc407b33eafa8ee`
- `p2_result.json` — Git blob `338a0b3deb3c7aa7f609f609562105d745bb919a`; manifest SHA-256 `c23077e6c37198163753d211a6de36488c9101b4297e2189b50a8f2dfdc90fce`
- `falsification_result.json` — Git blob `3317db51a05ba2990619756e5aec68aa1ee8ebf6`; manifest SHA-256 `a256dbb356ce5f5ea3b266f12021126895f6b4909d5b372df29be12313943877`

## Known limitation carried into V1

`falsification_result.json` records:
- 9 evasion probes;
- 1 caught;
- 8 missed;
- 30 clean packages with 0 packages producing findings;
- deterministic detected taxonomy IDs across reruns.

The eight misses are therefore a documented detector limitation and a V1 engineering requirement, not a POC benchmark defect.

## Anti-overfitting rule: the nine V2 probes are used up

The nine V2 evasion probes are now development examples, not an admissible test set for measuring improved detector capability.

Detector fixes are allowed in V1, including fixes motivated by genuine defects exposed by V2 (for example, an unchecked table N). However:

1. A fix may not be credited as evidence of improved generalization merely because the same V2 probes pass after the fix.
2. Re-running the nine V2 probes is permitted only for development/regression purposes.
3. Any claimed improvement in detector capability must be evaluated on **fresh probes** that are:
   - independently authored by someone who did not design the detector fix;
   - hidden from the detector developer until test time; and
   - held out from tuning and rule construction.

This prevents teaching the detector to the known benchmark answers.

## Benchmark V3 — deferred to V1.4

Benchmark V3 is a V1.4 deliverable, not a POC closure requirement. V3 must add:

1. **Independent authorship:** fixtures authored independently of the detector and kept hidden until evaluation.
2. **External-reference tier:** checks against authoritative outside sources for errors that are internally consistent across files.
3. **Real-world errors:** published corrections, retractions, and other documented research/reporting errors, in addition to designed synthetic mutations.
4. **True blinding:** the evaluator/scorer does not know which errors were planted when scoring outputs.
5. **Human escalation for language-based errors:** semantic issues such as overclaimed significance or causal wording are scored on correct escalation to human review when deterministic rules are insufficient.

## Governance effect

- Benchmark V2 remains unchanged and is the frozen POC baseline.
- The 8/9 missed probes remain visible in the permanent record.
- No detector tuning against the nine V2 probes is admissible as new validation evidence.
- V1 detector fixes must be validated only on fresh, independently authored, held-out probes.
- Benchmark V3 design and execution belongs to V1.4.
- This decision is additive and does not change the current POC gate status.
