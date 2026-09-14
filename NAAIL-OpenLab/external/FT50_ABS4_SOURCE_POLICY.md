# NAAIL OpenLab™ — External FT50 / AJG 4* Source Policy

## Scope
This policy governs how NAAIL OpenLab™ references and tests external replication repositories associated with FT50 and AJG/ABS 4* research.

## Default mode
External repositories are treated as **scientific benchmark sources**, not as NAAIL-owned code. The default integration mode is metadata/reference + adapter + isolated execution or clean-room reproduction.

## Mandatory controls
Before executing or reusing external code:
1. verify the repository and its relationship to the published study;
2. record the exact Git commit SHA;
3. inspect and record the code license;
4. inspect data licenses and redistribution restrictions separately from the code license;
5. identify proprietary or confidential dependencies;
6. run in an isolated environment where feasible;
7. preserve original attribution and citation requirements;
8. keep external code outside the NAAIL proprietary core unless its license explicitly permits the intended reuse;
9. never commit credentials, WRDS passwords, API keys, confidential data, or licensed raw datasets;
10. record all transformations and outputs in the NAAIL Chain-of-Evidence.

## Clean-room preference
When the scientific method can be reimplemented from the paper and documentation, NAAIL should prefer an independent implementation for robustness testing. This separates verification of the scientific idea from dependence on the authors' exact software implementation.

## Data boundary
A public GitHub repository does not imply that every required dataset is public or redistributable. WRDS, CRSP, Compustat, Audit Analytics, IBES, confidential author data, and similar inputs must remain subject to their own access and license conditions.

## Scientific use
Publication in a top journal is evidence of peer review, not an exemption from replication, falsification, leakage checks, causal diagnostics, or out-of-sample testing. NAAIL may report replication failures or sensitivity transparently when supported by evidence.

## Human Gate
No third-party benchmark is classified as reproduced, validated, failed, or scientifically generalized until the run manifest, rights/provenance record, results, and caveats have been reviewed by a human researcher.
