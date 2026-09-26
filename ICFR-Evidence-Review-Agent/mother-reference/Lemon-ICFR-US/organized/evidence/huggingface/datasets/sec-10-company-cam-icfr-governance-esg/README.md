---
license: other
tags:
- accounting
- auditing
- cam
- icfr
- governance
- esg
- sec
- pcaob
- reproducibility
---

# SEC 10-Company CAM + ICFR + Governance + ESG Research Layer

Phase 3 extends the 10-company accounting panel with four research modules.

## Included

- `cam_latest.csv` — latest-year CAM counts, topics and auditors.
- `icfr_latest.csv` — management ICFR assessment, auditor ICFR opinion and material-weakness flag.
- `governance_source_registry.csv` — SEC DEF 14A source locators and target variables.
- `esg_source_registry.csv` — public ESG source locators and target dimensions.

## Canonical source

https://github.com/Saehon/Saeid-Homayoun/tree/main/open-data/sec-10-company-phase3

GitHub is the source of truth. This Hugging Face dataset is a validated distribution layer.

## Boundary

Governance and ESG are currently source registries rather than completed scores. No missing governance or ESG metric is silently imputed.
