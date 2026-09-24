# NAAIL Research Software Registry

**Researcher:** Saeid Homayoun  
**ORCID:** https://orcid.org/0000-0002-2536-0446  
**Program:** NAAIL OpenLab  
**Registry status:** Canonical portfolio-level identifier registry  
**Last updated:** 2026-09-24

This registry is the canonical index for NAAIL research-software identity, citation, archival status, and persistent identifiers. A DOI or SWHID is recorded here only after it has actually been minted/resolved by the authoritative service. Placeholder or fabricated identifiers are prohibited.

## Canonical products

| Product | Repository / location | Version | Visibility | DOI | Concept DOI | SWHID | ORCID linkage | Release status |
|---|---|---:|---|---|---|---|---|---|
| **NAAIL OpenLab™** | https://github.com/Saehon/Saeid-Homayoun/releases/tag/V2026.4-R3 | V2026.4-R3 | Public | Pending Zenodo minting | Pending | Pending Software Heritage capture | ORCID declared; external work-link pending | Zenodo-ready archival ZIP + checksum published; validated executable checkpoint remains v0.2.3 |
| **ECONOVA-S™ Research Co-Scientist** | https://github.com/Saehon/Saeid-Homayoun | 0.2.0 | Public | Pending Zenodo minting | Pending | Pending Software Heritage capture | ORCID declared; external work-link pending | DOI-ready metadata |
| **AAA — Audit & Accounting AI Laboratory** | https://github.com/Saehon/AAA | 1.0.0 | Public | Pending Zenodo minting | Pending | Pending Software Heritage capture | ORCID declared; external work-link pending | DOI-ready metadata |
| **IFRS-AI Inspector** | https://github.com/Saehon/IFRS-AI-Inspector | 1.0.0 | Public | Pending Zenodo minting | Pending | Pending Software Heritage capture | ORCID declared; external work-link pending | DOI-ready metadata |
| **POMELO IFRS Intelligence Fabric** | https://github.com/Saehon/pomelo-core | 0.4.0 | Private | **HOLD — do not mint publicly before IP review** | Hold | Not applicable while private | ORCID metadata to be standardized | Private / patent-sensitive boundary |
| **PCAOB Inspection Agent** | https://github.com/Saehon/IFRS-PCAOB-AI | Research prototype | Private | **HOLD — do not mint publicly before IP review** | Hold | Not applicable while private | ORCID declared | Private / pre-production boundary |
| **Multi-Agent Accounting AI Framework** | https://github.com/Saehon/Google-Antigravity-using-a-multi-agent-BERT-architecture | 2026.3 | Public | Pending Zenodo minting | Pending | Pending Software Heritage capture | ORCID declared; external work-link pending | DOI-ready metadata |

## Identifier policy

### DOI

For public scholarly releases, use Zenodo or another recognized DOI registration service. Record both:

- **Version DOI** — identifies the exact archived software release used in an empirical study or replication package.
- **Concept DOI** — identifies the software project across versions and is preferred when citing the project generally.

Never invent a DOI and never add `10.5281/zenodo.xxxxx` until Zenodo has actually issued it.

### ORCID

All original NAAIL software records should identify:

**Saeid Homayoun — ORCID 0000-0002-2536-0446**

After a DOI is minted, add the software work to ORCID and link the DOI-backed record to the researcher identity. Repository metadata alone does not mean the work has already been added to the external ORCID record.

### Software Heritage / SWHID

For public source-code releases, request or verify archival by Software Heritage and then record the resolved SWHID here. Prefer an identifier that corresponds to the exact released source state when a paper depends on a specific software version.

A Git commit SHA and a SWHID are not interchangeable. Record the authoritative SWHID only after resolution in the Software Heritage archive.

## Release-to-identifier workflow

```text
Research milestone
    ↓
Rights / IP / privacy review
    ↓
Freeze semantic or project version
    ↓
CITATION.cff validation
    ↓
GitHub release/tag
    ↓
Zenodo archive
    ↓
Version DOI + Concept DOI
    ↓
Software Heritage archival
    ↓
SWHID
    ↓
ORCID software-work linkage
    ↓
Update this registry + README/BibTeX/manuscript
```

## Publication boundary

Public DOI deposition is appropriate only for material intentionally released as scholarly research software. Do **not** publicly deposit private implementation detail, confidential data, restricted standards content, proprietary third-party material, security-sensitive material, or patent-sensitive NAAIL/POMELO architecture without an explicit rights/IP review.

For private systems, a safer publication path is:

**private core → reviewed public research edition / benchmark / technical report → DOI-backed scholarly release**.

## Citation architecture

For each public product maintain, at minimum:

1. `CITATION.cff` as machine-readable GitHub citation metadata;
2. a human-readable citation in the README or `CITATION.md`;
3. BibTeX when useful for manuscripts;
4. DOI and concept DOI after external minting;
5. SWHID after verified Software Heritage archival;
6. ORCID linkage after the external ORCID work record is created;
7. associated paper DOI and dataset DOI when those objects exist.

## Associated scholarly objects

A mature NAAIL product should ultimately support this evidence chain:

**Researcher ORCID → Research software → Version DOI → Concept DOI → SWHID → Dataset DOI → Replication package → Article DOI → Evidence Passport / Chain-of-Evidence**

## Current next external actions

The GitHub metadata layer is prepared, but the following actions require the respective external services/account permissions:

- create/curate a **NAAIL OpenLab Zenodo Community**;
- enable or manually deposit the public products in Zenodo;
- mint real version/concept DOIs;
- request/verify Software Heritage archival and resolve SWHIDs;
- add DOI-backed software works to the external ORCID record;
- update this registry after those identifiers exist.

Until those services return real identifiers, the status must remain **Pending** or **Hold**.
