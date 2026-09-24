# NAAIL OpenLab — Cross-Platform Publication Manifest

Canonical source: `Saehon/Saeid-Homayoun/NAAIL-OpenLab`

## Platform roles

| Platform | Target | Role |
|---|---|---|
| GitHub | `Saehon/Saeid-Homayoun/NAAIL-OpenLab` | canonical code, architecture, provenance |
| Hugging Face | `SADHON/NAAIL-OpenLab` | public datasets/models and model-facing artifacts |
| Kaggle | `NAAIL-OpenLab` | benchmark datasets and reproducible notebooks |

## Publish set

The cross-platform package should expose only public, redistributable artifacts. Priority material:
- project README / START HERE documentation
- architecture and agent specifications
- `agents/` and `audit_agents/`
- `benchmarks/`
- `demos/`
- `digital-twins/`
- `prototypes/`
- `simulations/`
- citation metadata (`CITATION.cff`, `CITATION.bib`, `codemeta.json`)
- authorship, license, limitations, provenance, and release metadata

## Governance gate

Do not mirror private, confidential, licensed third-party, credential-bearing, or non-redistributable material. External dependencies remain references unless their licenses explicitly permit redistribution.

## Verification

A platform is marked **published** only after its public repository/dataset URL resolves and its visible file inventory has been compared with this manifest. GitHub is the source of truth; Hugging Face and Kaggle are distribution surfaces, not independent masters.
