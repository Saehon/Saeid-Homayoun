# Run 001 — Deterministic SEC/XBRL Execution

**Benchmark:** Microsoft Customer-Zero v1.0  
**Frozen reference commit:** `e3083348cb4cafc8a4142155074dfb5b5820364b`  
**Condition:** `sec_xbrl_deterministic`  
**Status:** EXECUTION REGISTERED / EMPIRICAL OUTPUT NOT YET RECORDED

This run is the first execution condition after freezing the nine-fact Microsoft FY2026 reference baseline. It must not modify `gold_reference.csv`, the scoring rules, or the registered acceptance gates after observing results.

## Pinned target

- Issuer: Microsoft Corporation
- CIK: 0000789019
- Form: 10-K
- Period end: 2026-06-30
- Accession: 0001193125-26-323660
- Canonical source: SEC filing identified in the frozen benchmark

## Run contract

1. Fetch/parse the pinned filing in a clean environment.
2. Extract only the nine frozen accounting facts without reading benchmark answers into the extraction logic.
3. Preserve raw XBRL/iXBRL concepts, contexts, units, source locators and extraction timestamps.
4. Normalize to USD millions only after preserving raw values.
5. Write candidate output separately from the frozen gold file.
6. Score candidate output using the frozen scorer.
7. Generate claim-level Evidence Passports.
8. Execute registered falsification challenges.
9. Build the Professional Decision DAG from evidence → claim → check → contradiction/falsification → conclusion.
10. Record Human Gate as PENDING until an actual human decision is made.
11. Preserve all missing, failed, contradictory and unsupported outputs.

## Required artifacts

- `run_manifest.json`
- `environment_manifest.json`
- `source_hashes.json`
- `raw_extraction.json`
- `candidate.json`
- `score.json`
- `evidence_passports.jsonl`
- `falsification_results.json`
- `professional_decision_dag.json`
- `human_gate.json`
- `limitations.md`

## Required metrics

Numeric accuracy, completeness, provenance coverage, unsupported-claim rate, contradiction/falsification outcomes, runtime, reproducibility status and cost. Cost for a deterministic/local run should be recorded from actual execution rather than assumed.

## Promotion rule

Do not label this run PASS, EXECUTED_VALIDATED, FALSIFICATION_PASSED or INDEPENDENTLY_REPLICATED until the corresponding evidence exists. Software/CI success alone is not scientific validation.

After a successful original execution, freeze this entire run directory and reproduce it independently from the published/pinned inputs and environment specification.
