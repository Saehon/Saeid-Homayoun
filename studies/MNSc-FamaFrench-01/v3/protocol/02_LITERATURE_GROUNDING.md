# 02 — Literature Grounding

## Purpose

This study is positioned as a measurement-stability and empirical-reliability contribution in asset pricing, not as a claim that an archive transition is itself a randomized treatment.

## Methodological anchors already incorporated in the executable package

- **He, Huang, Li & Zhou — reduced-rank factor-dimension methods (Management Science):** motivates the planned comparison of inferred factor dimension across data vintages.
- **Andrew Chen — statistical-reliability / multiple-testing logic (Management Science):** motivates multiplicity-aware interpretation and FDR controls.
- **Feng, Giglio & Xiu — factor-zoo discipline (Journal of Finance):** motivates disciplined factor evaluation and avoiding data-mined conclusions.
- **Giglio, Xiu & Zhang — test assets and weak factors (Journal of Finance):** motivates sensitivity to test-asset design and factor strength.
- **Gu, Kelly & Xiu — machine-learning asset pricing (Review of Financial Studies):** informs out-of-sample and predictive validation principles.
- **Hou, Xue & Zhang — anomaly replication (Review of Financial Studies):** motivates replication-first design and robustness to data construction.

The executable v3 package preserves DOI metadata for these anchors in its literature artifact. Before manuscript submission, the CoE Audit must re-verify each bibliographic record against the publisher/DOI registry.

## Data-construction prior

The Kenneth R. French Data Library is the authoritative primary source for this study. The study uses official historical archive snapshots and records source URLs and SHA-256 fingerprints at execution time.

## Competing explanations preserved ex ante

Observed vintage differences may arise from:

1. the documented FIZ→CIZ return-construction change;
2. ordinary historical-data revisions/corrections;
3. security or portfolio reclassification;
4. changes in upstream CRSP inputs or archive maintenance;
5. parser/alignment error (a falsifiable implementation failure).

The design therefore treats vintage differences as measurement/construction-regime sensitivity unless a later identification design separates these channels.

## Literature gate

The literature gate is marked complete for **research-design grounding**, but reference-by-reference verification must be repeated in `13_COE_AUDIT.json` before any publication-grade scientific claim.
