# Research and software evidence policy

This portfolio treats **reproducibility, provenance and transparent uncertainty** as conditions of credible scientific claims.

## Levels of evidence

| Label | Meaning | Minimum supporting artifact |
|---|---|---|
| CONCEPT | Scientific question, proposal or architecture | dated research rationale and references |
| IMPLEMENTED | Source code for a method exists | versioned exact commit and clear license |
| TESTED | Automated tests ran on specified data | GitHub Actions run or reproducible local log |
| MEASURED | Real observations or model predictions processed | lawful data source, input hash, exact model/version, protocol, output and score |
| INDEPENDENTLY REVIEWED | Non-author reviewer verified the claim | reviewer identity, conflicts, review/decision record |
| PUBLISHED | Public scholarly result | independently verifiable article/DOI record |

A passing unit test on hand-written synthetic cases establishes only internal consistency. It must not be presented as 100% AI accuracy, clinical/accounting compliance, peer review or professional certification.

## Model evaluation controls

1. Source admissibility and license rights, document currency, company reporting period and evidence identifiers.
2. Written scoring contract: exact numeric tolerance, abstention policy, evidence-citation requirements, domain-specific failure classes.
3. Holdout management: frozen case IDs; no gold labels in model prompts; verify training/holdout overlap when identifiers are available.
4. Reproducibility: `model_id`, version, prompt hash, token usage/cost where recorded, input hashes, software version and evaluation date.
5. Scientific validity: missingness, denominators, sector/group heterogeneity, human label agreement, error costs, uncertainty and alternative explanations.
6. Human review: evaluator independence and explicit approval before operational, causal or policy claims.

## Attribution and ownership

- **Original work:** code developed for a clearly documented project with attributable commits.
- **Adapted work:** modifications to an identified upstream with its exact source license and attribution.
- **External reference:** unmodified upstream, forked vendor code, or published benchmark used for comparison.
- **Confidential materials:** private/proprietary code, restricted standards or non-public data remain excluded.

AI-assisted code and documentation must be independently inspected by the responsible investigator before being presented as externally validated research.

## Release gate

Do not merge, tag as independently validated, publicly release data, or claim empirical results unless all applicable scientific, legal, security and IP permissions have been verified. *The module in this PR is an educational/research scaffold with synthetic data.*
