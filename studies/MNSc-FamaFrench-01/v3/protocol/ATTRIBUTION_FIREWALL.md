# Attribution Firewall — MNSc–FamaFrench–01 V3

## Why this firewall exists

The study compares two official historical archive snapshots: July 2024 (FIZ-era) and July 2025 (CIZ-era). The FIZ→CIZ methodology transition is a documented change in the return-construction system, but the two archives may also differ because of ordinary data revisions, corrections, reclassifications, or other archive maintenance.

Therefore the observed archive difference

`ΔX_t = X_t^(July 2025 archive) − X_t^(July 2024 archive)`

is interpreted as **archive / construction-regime sensitivity**, not automatically as the pure causal effect of FIZ→CIZ.

## Allowed language

- measurement sensitivity across the FIZ→CIZ transition;
- archive sensitivity;
- data-construction / revision sensitivity;
- conclusion sensitivity or conclusion reversal under alternative official vintages;
- empirical stability across official vintages.

## Prohibited language unless separately identified

- “FIZ→CIZ caused the entire observed difference”;
- “the treatment effect of CIZ is …”;
- any causal decomposition that assumes ordinary archive revisions are zero.

## Identification upgrade required for causal attribution

A stronger causal decomposition should benchmark the transition-year archive difference against ordinary annual archive revisions, for example using FIZ-era placebo pairs (e.g., July 2023→July 2024) and CIZ-era placebo pairs (e.g., July 2025→July 2026 where comparable archives are available), plus component-level return-construction evidence where feasible.

## Damodaran layer

The Damodaran / NYU Stern industry regressions are a **complementary external benchmark**. They do not validate or identify the FIZ→CIZ archive transition. Any legacy filename containing `external_validation` is retained only for package compatibility and must not be interpreted as causal validation of the transition.

## Scientific status

`identification_gate = false`

`discovery_claim_allowed = false`
