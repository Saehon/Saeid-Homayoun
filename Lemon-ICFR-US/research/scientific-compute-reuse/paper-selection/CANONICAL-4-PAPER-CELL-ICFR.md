# LEMON-SCI Canonical 4-Paper Cell — ICFR v2026.09

Status: PAPER_SELECTION_LOCK_V1
Scope: ICFR / internal-control-over-financial-reporting scientific-compute reuse
Selection date: 2026-09-29

## Deterministic cell rule

For every research topic, LEMON-SCI should build a fixed-role evidence cell before model extraction:

1. P1 — Meta-analysis / quantitative synthesis anchor
2. P2 — Systematic literature review anchor
3. P3 — Modern executable/frontier anchor, prioritizing Management Science 2021–2026 with replication materials
4. P4 — Modern complementary/executable anchor, prioritizing Management Science 2021–2026 with replication materials

Same topic + same corpus snapshot + same inclusion/exclusion rules + same tie-break rules => same cell version.

The cell is versioned rather than overwritten when the literature universe changes.

## Selected ICFR cell

### P1 — Meta-analysis / quantitative synthesis
Bilal, Chen, and Komal (2018), “Audit committee financial expertise and earnings quality: A meta-analysis,” Journal of Business Research, 84, 253–270.
DOI: 10.1016/j.jbusres.2017.11.048

Role:
- quantitative synthesis scaffold for governance/financial-reporting-quality mechanisms;
- includes internal-control weakness among the earnings-quality outcomes considered and evaluates SOX as a moderator;
- NOT claimed to be FT50/AJG4 or a direct ICFR-only meta-analysis;
- used because the screening pass did not identify a stronger direct ICFR meta-analysis in the preferred FT50/AJG4 universe.

### P2 — Systematic literature review
Chalmers, Hay, and Khlif (2019), “Internal control in accounting research: A review,” Journal of Accounting Literature, 42, 80–103.
DOI: 10.1016/j.acclit.2018.03.002

Role:
- direct ICFR/internal-control knowledge-map anchor;
- synthesizes determinants, consequences, governance, audit, stakeholder effects, measurement approaches, and international evidence;
- NOT treated as an executable empirical model.

### P3 — Management Science executable/frontier anchor
deHaan, de Kok, Matsumoto, and Rodriguez-Vazquez (2023), “How Resilient Are Firms’ Financial Reporting Processes?” Management Science 69(4):2536–2545.
DOI: 10.1287/mnsc.2023.4670
Replication repository: https://github.com/TiesdeKok/mnsc.2023.4670

Role:
- executable-replication benchmark for paper-to-code-to-output compilation;
- public package contains Python, SAS, and Stata code, pipeline structure, output logs, and raw-data acquisition instructions;
- used to validate LEMON-SCI’s Scientific Model Compiler and provenance architecture.

### P4 — Management Science AI/audit-quality anchor
Law and Shen (2025), “How Does Artificial Intelligence Shape Audit Firms?” Management Science 71(5):3641–3666.
DOI: 10.1287/mnsc.2022.04040

Role:
- modern AI/audit frontier anchor;
- directly evaluates internal-control-opinion accuracy as an audit-quality outcome;
- INFORMS-hosted full replication package is reported by the authors;
- used for AI-enabled audit-quality, ICFR-opinion, and modern replication-package ingestion.

## Selection constraints

- Prestige never overrides estimand incompatibility.
- Meta-analysis and review papers are synthesis evidence, not coefficient sources for M1.
- Management Science papers are not automatically ICFR prediction models; they enter only for their admissible mechanism, estimand, and executable-replication role.
- No coefficient, transformation, threshold, or outcome from these papers may enter an executable M1 contract until its primary evidence and replication lineage are independently verified.
- Existing ACK2007/DGM2007/RW2012 work remains a separate historical model-bank stream; this Canonical 4-Paper Cell upgrades the literature-selection architecture and does not replace unresolved primary-paper gates.

## Future versioning

Example:
- ICFR_C4_v2026.09 = this locked selection
- ICFR_C4_v2027.xx = future re-screen with a frozen new corpus snapshot

A future version may replace P1 or P2 if a stronger direct ICFR meta-analysis/systematic review appears, or P3/P4 if newer Management Science/FT50 executable papers dominate under the same deterministic rules.


## Mandatory journal-tier fallback hierarchy

For each required slot, the selector searches in the following strict order:

1. FT50 / AJG 4* / AJG 4
2. AJG 3
3. AJG 2
4. AJG 1

The selector may move to a lower tier only when no admissible candidate remains at the higher tier after the mandatory scientific gates are applied.

Mandatory gates:
- estimand/topic fit;
- primary-evidence sufficiency;
- methodological credibility;
- replication/executability for executable-anchor roles;
- non-duplication and portfolio contribution.

Every fallback must be auditable. The manifest must record:
- tier searched;
- candidate set;
- exclusion reason codes;
- selected fallback tier;
- selected paper;
- corpus snapshot date;
- selector version.

Journal tier must be verified against the applicable AJG/ABS edition; the system must not infer or invent a tier.

Management Science remains the preferred modern executable source for P3/P4 in the 2021–2026 window when an admissible paper exists.
