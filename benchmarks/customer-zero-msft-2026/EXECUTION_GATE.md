# Customer-Zero 001 — Microsoft Execution Gate

**Status:** REGISTERED / NOT YET EXECUTED  
**Anchor commit:** `3bfef2391e5bb5a050be4ec0ab0d7f37bbb1198a`  
**Scope:** Microsoft FY2026 Customer-Zero benchmark

## Scientific rule
Do not tune the benchmark, scoring contract, evidence definitions, or acceptance gates after execution begins. Preserve successful, failed, null, contradictory, and unavailable results. A passing software test is not, by itself, scientific validation.

## Execution sequence
1. Freeze benchmark v0: filing identity, manifest, evidence schema, code, dependency versions, source/input hashes, and environment manifest.
2. Execute deterministic SEC/XBRL baseline first.
3. Execute each registered adapter in an isolated, pinned environment: sec-data; edgar-mcp; sec-10-k-structured-extraction; verified-credit-research-agent.
4. Normalize outputs without overwriting source facts.
5. Generate claim-level Evidence Passports.
6. Measure cross-tool agreement and preserve disagreements.
7. Run falsification/adversarial checks.
8. Build the Professional Decision DAG.
9. Submit material conclusions to Human Gate.
10. Perform an independent clean-room rerun from the frozen package.
11. Compare original and independent runs before release-readiness promotion.

## Required metrics
- filing identity
- numeric accuracy
- completeness
- provenance coverage
- cross-tool agreement
- unsupported-claim rate
- contradiction detection
- reproducibility
- runtime
- cost per task
- cost per correct output
- cost per verified professional output
- Human-Gate disagreement/outcome

## Required evidence package
Source/input hashes; exact code SHA; dependency/environment manifests; raw and normalized adapter outputs; claim-level Evidence Passports; disagreement matrix; falsification record; Professional Decision DAG; metric table; Human Gate decision; clean-room replication manifest/outputs; limitations and retained failures.

## Status gates
`BASELINE_CREATED` → `FROZEN_FOR_EXECUTION` → `EXECUTED` → `HUMAN_GATE_EVALUATED` → `FALSIFICATION_PASSED` → `INDEPENDENTLY_REPLICATED` → `EXECUTED_VALIDATED`

No status may be promoted merely because documentation, code, CI, or an adapter exists.

## Publication and accountability
Kaggle/Hugging Face synchronization remains after-pass. Mirrors preserve provenance and are not independent replication. Material accounting/audit conclusions require Human Approval; Human approval is distinct from independent scientific validation.

## Next empirical milestone
**Customer-Zero 001 — Microsoft: EXECUTED + INDEPENDENTLY REPRODUCED**

This is the priority before adding another NAAIL architecture, model family, agent, or release version.
