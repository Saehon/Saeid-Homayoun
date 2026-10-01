# Error Taxonomy V2

Status: P1_IMPLEMENTED

Machine-readable canonical artifact: `error_taxonomy_v2.json`.

The taxonomy separates six research-assurance error families: Reporting (RPT), Specification (SPC), Data Engineering (DAT), Identification (IDN), Interpretation (INT), and Reproducibility (REP).

## Assurance safeguards
- Taxonomy class and severity are separate.
- Detectability is explicit: deterministic, mixed, or judgment-dependent.
- Missing evidence never becomes VERIFIED.
- CONSISTENT means available artifacts agree; it is not independent reproduction.
- PARTIAL means only a declared subset of the evidence chain is established.
- FLAGGED is an evidence-supported anomaly signal, not automatic methodological invalidity.
- Judgment-dependent findings can require HUMAN_REVIEW even when computation is correct.
- Synthetic benchmark mutations must never be represented as errors made by original authors.

## P2 handoff
Adversarial Benchmark V2 should instantiate clean controls and single, compound, blinded, provenance, version/dependency, dynamic-state, and claim-manipulation cases mapped to taxonomy IDs.
