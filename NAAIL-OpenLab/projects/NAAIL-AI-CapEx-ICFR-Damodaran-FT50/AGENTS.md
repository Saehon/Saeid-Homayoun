# Codex / VS Code instructions — project subtree

You are supporting an academic finance/accounting research project designed for transparent, replicable analysis.

Rules:
1. Never fabricate data, results, p-values, publication claims, citations, sample sizes, or repository links.
2. Before using AI CapEx, produce evidence-backed definitions and manually audit ambiguous disclosures. Total capex is not AI-specific capex.
3. Preserve accession IDs, CIK, fiscal dates, acceptance timestamps, revision time, source span, and extraction versions.
4. Prevent leakage across chronological splits. No filing or post-event text may predict an event earlier than its public availability.
5. Separate causal claims from predictive associations; preregister estimands and exclusion rules before assessing results.
6. Implement transparent econometric / ML baselines; test model calibration, uncertainty, cost-sensitive actionability, and robustness.
7. Only use synthetic sample fixtures inside open-source tests. Real or restricted datasets remain in controlled Google Drive.
8. Build small, documented Python functions with type hints, exceptions, deterministic tests, and recorded dependencies.
9. Never push API keys, restricted material, private manuscripts or personally identifying information to the public umbrella repository.
10. Human review is required before merging, releasing datasets, making public research claims, or submitting manuscripts.

When asked to implement a new module, first create an issue-like task definition: objective, input specification, as-of date, expected output, data rights, tests, assumptions and explicit done criteria.


## New PCAOB / CAM module directives
- Read research/PCAOB_CAM_INTEGRATION.md before modeling PCAOB or CAM.
- PCAOB Part I.A anonymous issuer letters CANNOT be joined to CIK. Only link public auditor-firm findings via registered firm ID and confirmed Form AP/issuer associations.
- Enforce timezone-aware "public as-of" cutoffs; inspect report publication and Part II release separately.
- Independently calculate pre-CAM account risk; CAM must not enter the scoring rule. High risk/no CAM does not imply auditor misconduct.
- Respect CAM eligibility and staggered implementation by fiscal year and filer category.
- Preserve selected-audit denominators, risk-based sampling caveats, and missing public report flags.
- Unit tests may use synthetic data but never present synthetic results as evidence. Confirm statistical power for audit-firm heterogeneity before high-dimensional specifications.
