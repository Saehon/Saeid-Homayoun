# 08 — Latent-Structure Protocol

## Status

**Planned extension; not yet executed.**

`latent_structure_validation = false`

## Question

Does the effective factor dimension inferred from the same historical period change when the factor/portfolio data vintage changes from the July-2024 FIZ-era archive to the July-2025 CIZ-era archive?

## Methodological role

This is an AlphaFold-inspired **hidden-structure reasoning** layer only in the methodological sense: infer a latent economic structure, compare competing representations, and require external/OOS validation. ECONOVA-S does not claim to run AlphaFold for economics.

## Planned implementation

- reduced-rank factor-dimension estimator anchored to the pre-specified Management Science literature;
- identical sample and variable definitions across vintages;
- identical tuning/evaluation rule across vintages;
- no tuning against desired dimension changes;
- comparison against simpler PCA/eigenvalue baselines where appropriate;
- stability checks across subperiods and additional portfolio families.

## Required outputs before interpretation

- `K_star_old` and `K_star_new`;
- uncertainty / stability analysis;
- baseline comparison;
- economic interpretation of any dimension change;
- independent replication;
- red-team assessment of weak-factor and test-asset sensitivity.

No latent-structure result may be promoted to a scientific claim until the method is frozen, executed, replicated, and the latent-structure gate is explicitly changed to true.
