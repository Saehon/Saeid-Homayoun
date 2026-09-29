# LEMON-SCI Canonical Paper-Selection Policy

Version: v2026.09
Status: ACTIVE_POLICY
Scope: all future LEMON-SCI research topics

## 1. Fixed four-slot evidence cell

Every research topic must first be represented by a versioned four-paper evidence cell:

- P1 — Meta-analysis / quantitative synthesis
- P2 — Systematic literature review
- P3 — Modern executable/frontier empirical paper
- P4 — Modern complementary/executable empirical paper

For P3 and P4, prioritize Management Science papers from 2021–2026 with replication code/data or a verifiable replication package.

## 2. Deterministic journal-tier hierarchy

For every required slot, search and screen in this strict order:

1. FT50 / AJG 4* / AJG 4
2. AJG 3
3. AJG 2
4. AJG 1

The selector may descend only when no admissible candidate remains at the higher tier.

A lower-tier paper may not displace an admissible higher-tier paper merely because it has easier data, cleaner code, or a more convenient specification.

## 3. Mandatory admission gates

Before a candidate can occupy a slot it must pass the relevant gates:

- topic and estimand fit;
- primary-evidence sufficiency;
- methodological credibility;
- replication/executability for executable-anchor roles;
- non-duplication and portfolio contribution;
- provenance traceability.

Prestige is a priority constraint, not a substitute for scientific compatibility.

## 4. Mandatory fallback audit trail

Every downgrade from a higher journal tier must be logged with:

- topic;
- slot;
- corpus snapshot date;
- selector version;
- tier searched;
- candidate set;
- exclusion reason codes;
- next tier searched;
- selected fallback tier;
- selected paper;
- DOI;
- replication/code status where relevant.

Journal tier must be verified against the applicable FT50/AJG/ABS source. The system must not infer or invent a journal tier.

## 5. Deterministic reproducibility rule

Same topic + same corpus snapshot + same inclusion/exclusion rules + same tie-break rules = same selected cell version.

New literature never silently overwrites a prior cell. It creates a new version, for example:

- ICFR_C4_v2026.09
- ICFR_C4_v2027.03

## 6. Tie-break order

When multiple candidates at the same admissible tier pass the hard gates, apply the following tie-break order:

1. estimand fit
2. primary-evidence quality
3. replication-package completeness
4. executability
5. methodological credibility
6. recency
7. journal prestige within the same admissible tier

## 7. Scientific firewall

Meta-analysis and systematic-review papers are synthesis evidence, not coefficient sources for M1.

No coefficient, transformation, threshold, model weight, outcome definition, or code path from any selected empirical paper may enter M1 until primary evidence, model lineage, data construction, and replication status are independently verified.

Selection into the four-paper cell is not equivalent to scientific validation.

## 8. Darwin / Co-Scientist role

Darwin-style competition, Co-Scientist reflection/ranking, AlphaEvolve-style portfolio search, and confidence scoring may be used to challenge candidates and generate alternatives.

However, the final paper selection must obey this deterministic policy and preserve a machine-readable audit trail.

## 9. Current ICFR implementation

Current cell:
paper-selection/CANONICAL-4-PAPER-CELL-ICFR.md

Machine-readable manifest:
paper-selection/icfr-canonical-4.json

Existing historical ICFR models such as ACK2007, DGM2007, and RW2012 remain a separate scientific-model-bank stream and are not invalidated by the modern four-paper selection architecture.
