# GitHub Copilot Instructions — Saeid-Homayoun / NAAIL OpenLab

## Project identity
This repository is the main public research hub for Saeid Homayoun (ORCID: 0000-0002-2536-0446), ECONOVA-S™, and NAAIL OpenLab. Treat it as research software and scientific infrastructure, not as a generic app repository.

## Scientific protocol
For research changes, follow this sequence:
1. literature validation;
2. competing hypotheses and critique;
3. ERA-style empirical design with explicit variables, estimands, identification and data provenance;
4. computational/model comparison using frozen evaluation criteria;
5. latent-structure analysis only with interpretable validation;
6. robustness, falsification and temporal/OOS tests;
7. AI-to-AI critic/defender/replicator review;
8. Chain-of-Evidence and DAG dependency checks;
9. Human Gate before any discovery claim.

Never optimize for p-values, treat agent consensus as truth, or present model confidence as evidence.

## Coding rules
- Prefer clear, modular, testable Python/R/Stata-compatible research workflows.
- Keep deterministic preprocessing separate from model inference.
- Record random seeds, software versions, data transformations and run manifests.
- Add tests for data leakage, schema drift, missingness, temporal splits and metric calculations.
- Do not silently change variable definitions or sample filters.
- Keep outputs reproducible from documented inputs.

## Research integrity
- Distinguish descriptive, predictive and causal claims.
- Cite authoritative sources and peer-reviewed literature where claims depend on them.
- Preserve failed or negative runs when scientifically relevant.
- Do not fabricate data, citations, results, DOI values, validation claims or affiliations.

## IP and licensing
- Do not expose private POMELO/VERA implementation details, patent-sensitive mechanisms, credentials, restricted datasets or licensed standards text.
- Public GitHub publication is not a patent filing.
- Respect all third-party licenses and attribution requirements.
- Do not imply affiliation with OpenAI, Google, Microsoft, Big Four firms, regulators or standard setters.

## Documentation
When adding a research study, include or update README, CITATION.cff, data provenance, methods, limitations, reproducibility instructions and human-review status where applicable.
