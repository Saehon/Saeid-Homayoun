# NAAIL OpenLab — Executable Demos

This directory contains small, recruiter-friendly and research-friendly proof-of-work artifacts. Each demo should be runnable, measurable, reproducible, and explicit about its limitations.

## Primary audit demo

### [KIWI™ AAR Corp CAM Unit Test](./aar-cam-unit-test/)

The canonical one-company CAM benchmark for NAAIL/KIWI. It uses **AAR Corp only**: 10 CAM observations across 2020–2024, two CAMs per year. The demo freezes the observed transition from `Inventory + Revenue` to `Inventory + Acquired Intangibles / Business Combination` in 2024 and verifies **CARS = 0.667 with zero change in CAM count**.

It includes:

- AAR CAM metadata and company-year transformation tables;
- frozen RPA / EDS / SIS / SQI / CIIS / CARS pilot measures;
- correct-vs-swapped-response falsification logic;
- year-level exact sign-test inference;
- positive-weight robustness testing;
- regression tests and machine-readable output;
- explicit rejection of population inference from five company-years.

**Rule:** future KIWI CAM scoring models should reproduce the AAR benchmark before being scaled to larger U.S. CAM samples.

## Secondary generic prototype

### [CAM/KAM Agentic Audit Intelligence benchmark](./cam-kam-agent-benchmark/)

A generic deterministic Python baseline for prototype dimensions such as RPA, AA, EG, PS, DS, and DIST. It remains useful as an engineering sandbox, but the AAR unit test is the preferred CAM research benchmark.

## Demo standard

Every NAAIL public demo should provide:

- a concrete research/professional problem;
- a minimal runnable implementation;
- sample or legally usable data;
- explicit evaluation metrics;
- tests or reproducibility checks;
- machine-readable output;
- limitations and non-claims;
- clear distinction between original work and upstream dependencies;
- human-review boundary for professional/scientific conclusions.

The purpose is to demonstrate engineering and empirical discipline, not to inflate architecture claims.
