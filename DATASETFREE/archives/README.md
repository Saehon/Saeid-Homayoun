# DATASETFREE — consolidated code and data archive

**Canonical Google Drive folder:** https://drive.google.com/drive/folders/19m030UxkJeu36nij7IbRV-OnxcXt33vj

**Drive master index:** https://docs.google.com/document/d/1y1FlD5pDuk13PZBYlt5TwK3YooTjDHe3EN1-0hPDyBo/edit

**GitHub PR (not yet merged):** https://github.com/Saehon/Saeid-Homayoun/pull/154

The FT50 paper catalogue contains **42 selected FT50 papers**, supplemented by **5 non-FT50 AJG4 papers**. These are metadata records, **not** 47 complete downloadable datasets. This archive links their data and code rather than falsely claiming everything is freely reproducible.

## Currently licence-approved code snapshot

The workflow **DATASETFREE licensed code archive** tries to create one provenance-logged CODE ONLY zip using:
- MacAma from https://github.com/YilinYuan/MacAma : MIT license verified.
- Twin-2K-500 code from https://github.com/tianyipeng-lab/Digital-Twin-Simulation : Apache-2.0 license verified.

The script excludes participant personas, raw survey data, notebooks, images, and datasets, and does not execute any third-party code. An execution log and source-commit SHA-256 manifest are retained inside the ZIP. **A requested snapshot does not count as downloaded until an artifact exists and is verified.**

## Restrictions on other sources

- de Kok, LOLA and LLM Peers publicly list code but no root LICENSE was found in the verified repositories. These are linked, not mirrored.
- Babina JFE Mendeley V3 has CC BY 4.0 code/pseudo data; original Cognism/Compustat input cannot be publicly replaced.
- JAR Vol 64 lists academic-use replication materials, some of which rely on restricted original datasets.
- Lopez-Lira & Tang JFE (2026) Mendeley V2 is listed under CC BY 4.0 but the original financial/news input datasets are not confirmed legally free.

**Source-level status:** [UPSTREAM_SOURCE_MANIFEST.csv](UPSTREAM_SOURCE_MANIFEST.csv).

## Platform permissions

GitHub: direct authenticated PR, changes remain on review branch.  
Google Drive: canonical read/write research archive.  
Hugging Face: authenticated as [SADHON](https://huggingface.co/SADHON), read-only; cannot publish new dataset.  
Kaggle: no authenticated Kaggle integration found, cannot upload a user-owned notebook/dataset.

### Reproducibility policy

Store canonical URL, DOI, dataset version, Git SHA, licence, original-versus-synthetic source type, SHA-256, file size, allowed reuse, transfer receipt and execution notes. Avoid copying private profiles, personal CVs, copyrighted article PDFs, subscription CRSP/Compustat/Cognism records or credentials.
