# 01 — Research Goal

## Working title
**When Data Construction Changes Asset Pricing: Measurement Stability Across the FIZ–CIZ Transition in Fama–French Data**

## Primary question
How sensitive are factor realizations, portfolio returns, asset-pricing alphas, statistical conclusions, and inferred factor structure when the same historical calendar is evaluated using the official July-2024 FIZ-era versus July-2025 CIZ-era Fama–French archive snapshots?

## Primary estimand
For each series `j` and common month `t`:

`ΔX_{j,t} = X_{j,t}^{2025 archive} − X_{j,t}^{2024 archive}`

Primary measurement sensitivity:

`DCS_j = mean_t |ΔX_{j,t}|`

reported in basis points per month together with mean difference, maximum absolute difference, vintage correlation, and conclusion-reversal indicators.

## Interpretation boundary
The primary estimand is **archive / construction-regime sensitivity**. It is not a pure causal treatment effect of CIZ because ordinary archive revisions may also contribute to differences between vintages. See `ATTRIBUTION_FIREWALL.md`.

## Primary empirical objects
- Fama–French 5-factor series and RF;
- six value-weighted Size × Book-to-Market portfolios;
- CAPM, FF3, and FF5 alphas with HAC/Newey–West inference;
- Data Construction Sensitivity (DCS);
- sign and frozen-5%-threshold Conclusion Reversal;
- FDR-adjusted inference for families of revision tests;
- frozen subperiod robustness.

## Planned extensions
- reduced-rank factor-dimension comparison across vintages;
- ordinary-revision placebo archive pairs;
- additional Fama–French portfolio families;
- independent Python/Stata replication and AI-to-AI red-team review.

## Pre-result status
This protocol is frozen before any new real-data output is interpreted under this discovery package.

`discovery_claim_allowed = false`
