# Zenodo / DOI Readiness — NAAIL OpenLab™ V2026.4-R2

**Release:** V2026.4-R2  
**Release date:** 2026-09-24  
**DOI status:** NOT YET MINTED

## Current constraint

`Saehon/Saeid-Homayoun` is an umbrella repository. Its root `CITATION.cff` describes ECONOVA-S™, not NAAIL. Zenodo's GitHub integration reads repository-root metadata, so the umbrella repository is not a clean NAAIL-specific automatic-deposit target.

## Preferred path

Create a dedicated `Saehon/NAAIL-OpenLab` repository, put NAAIL `CITATION.cff` at its root, then enable that repository in Zenodo and create releases from there.

## Safe interim path

Create a separate NAAIL software deposit in Zenodo using the metadata in this release directory and the public release archive. After Zenodo actually mints a DOI, record the real version DOI and concept DOI in the NAAIL identifier files.

## Metadata files

- `CITATION.cff`
- `CITATION.bib`
- `ZENODO_METADATA_TEMPLATE.json`
- `RELEASE.md`

Never invent or pre-populate a DOI that has not been issued.
