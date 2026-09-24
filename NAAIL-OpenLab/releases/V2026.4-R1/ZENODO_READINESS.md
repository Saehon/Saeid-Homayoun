# Zenodo / DOI Readiness — NAAIL OpenLab™ V2026.4-R1

**Release:** V2026.4-R1  
**Release date:** 2026-09-24  
**GitHub release:** https://github.com/Saehon/Saeid-Homayoun/releases/tag/V2026.4-R1  
**DOI status:** NOT YET MINTED

## Important repository-boundary note

The GitHub repository `Saehon/Saeid-Homayoun` is an umbrella repository. Its root `CITATION.cff` currently describes ECONOVA-S™, while NAAIL OpenLab™ is maintained under `NAAIL-OpenLab/`.

For that reason, do **not** rely on the umbrella repository's root citation metadata when minting a NAAIL-specific DOI.

Preferred archival options:

1. create a dedicated `Saehon/NAAIL-OpenLab` repository and use its root `CITATION.cff` for future GitHub→Zenodo automatic releases; or
2. create a separate Zenodo software deposit for the public NAAIL release package and use the release-specific metadata in this directory.

## Release-specific metadata

This directory contains:

- `CITATION.cff` — release-specific Citation File Format metadata;
- `CITATION.bib` — BibTeX citation;
- `ZENODO_METADATA_TEMPLATE.json` — metadata template for a NAAIL-specific Zenodo deposit;
- `RELEASE.md` — frozen public release record.

## DOI rule

Never invent, reserve-looking, or pre-populate a DOI unless it has actually been issued by Zenodo/DataCite or another authoritative DOI registration service.

After a real DOI is minted, update:

1. this release citation metadata;
2. `NAAIL-OpenLab/RESEARCH_IDENTIFIERS.md`;
3. the NAAIL Research Software Registry;
4. the human-readable citation;
5. the ORCID work record where appropriate.

## Recommended citation before DOI minting

Homayoun, S. (2026). *NAAIL OpenLab™ V2026.4-R1: Open Research Infrastructure Release* [Computer software]. GitHub. https://github.com/Saehon/Saeid-Homayoun/releases/tag/V2026.4-R1
