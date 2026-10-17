# P2.2 Official Replication Packages and Public-Data Inventory

Version: 1.0  
Gate: P2.2 — Inventory official replication packages and public data  
Verification date: 2026-10-07  
Status: FROZEN INVENTORY — NO REPLICATION EXECUTED

## Scope and classification

This inventory covers the eight verified P2.1 seed records. A resource is treated as
official only when it is linked by the publisher, the published article, an author or
an author-controlled research page. Third-party reproductions are not substitutes.

| Class | Meaning |
|---|---|
| PUBLIC_PACKAGE | Versioned package with public download and explicit license |
| PUBLIC_PARTIAL | Public code and/or sample/synthetic data; original inputs incomplete or restricted |
| AUTHOR_RESOURCES | Author-controlled code/data/model links, but package/license completeness is not established |
| SUPPLEMENT_ONLY | Publisher supplement or appendix without a verified executable package |
| INTEGRITY_HOLD | Resource exists, but scientific reliance is quarantined by an unresolved integrity notice |

Inventory PASS means access conditions and gaps are recorded. It does not mean the
code runs, results reproduce, dependencies remain available, licenses permit
redistribution, or the paper's findings are accepted.

## Resource inventory

| Literature ID | Official/author-controlled resources verified | Availability class | License and data boundary | Reproduction disposition |
|---|---|---|---|---|
| LIT-JFE-001 — Babina et al. | Publisher record states that data and code are published; Mendeley Data V2, DOI [10.17632/s26kxvspn7.2](https://doi.org/10.17632/s26kxvspn7.2), published 2023-10-25; author data page identifies firm-level AI measures for U.S. firms, 2010–2018. | PUBLIC_PACKAGE | Mendeley metadata states CC BY 4.0. Package-level identity is verified; individual file manifest/hash was not downloaded in this gate. | Eligible for P4 planning after file-level manifest, dependency and checksum audit. |
| LIT-JFE-002 — Lopez-Lira & Tang | Mendeley Data V2, DOI [10.17632/f39x226htv.2](https://doi.org/10.17632/f39x226htv.2), published 2026-06-15; package page provides download and README reproduction instructions. | PUBLIC_PACKAGE | CC BY 4.0; two approximately 502 MB ZIP entries were listed by the indexed package record. CRSP, TAQ, RavenPack and model/API access may remain separately licensed or time/version constrained even when code/package files are public. | Highest-priority P4.2 candidate; first pin V2, enumerate files, verify hashes, licenses and model chronology. |
| LIT-JF-001 — Fuster et al. | Author repository [paulgp/ml-credit](https://github.com/paulgp/ml-credit) contains analysis code and synthetic data plus construction instructions. | PUBLIC_PARTIAL | Repository states the principal analysis file is proprietary and substitutes simulated data. Original construction requires Federal Reserve RADAR and underlying McDash/Federal Reserve inputs. Repository license was not verified in the visible record. | Synthetic execution may test plumbing only; it cannot reproduce published estimates. Original-data replication remains access-controlled. |
| LIT-RFS-001 — Gu, Kelly & Xiu | Author-controlled Dacheng Xiu page links the paper, GitHub, “Empirical Data (UPDATED June 2021),” SAS/Python data code and supplemental material. | AUTHOR_RESOURCES | Public links are verified, but an explicit package license and stable file hashes were not established. Underlying CRSP/Compustat-style source data may carry separate restrictions; processed-data terms must be audited before redistribution. | Eligible for a bounded P4 benchmark only after snapshot/hash/environment and upstream-license review. |
| LIT-RFS-002 — van Binsbergen, Han & Lopez-Lira | Oxford article supplies an Internet Appendix; no clean, publisher-certified executable package was verified in this gate. Oxford issued an Expression of Concern, DOI [10.1093/rfs/hhag017](https://doi.org/10.1093/rfs/hhag017), on 2026-03-01 while an investigation is pending. | INTEGRITY_HOLD | Findings reliability is under journal investigation. Inputs described in the article include commercial financial databases; access/licensing remain unresolved. | **STOP_RELIANCE.** Preserve as adverse evidence. Do not use as a clean benchmark or pass-dependent input until the journal resolves the notice and P4 performs an independent audit. |
| LIT-RFS-003 — Jha, Liu & Manela | Published RFS article states replication code is in Harvard Dataverse, DOI [10.7910/DVN/ZRSGXQ](https://doi.org/10.7910/DVN/ZRSGXQ); author pages also link data/code. Indexed catalog describes replication code with short sample data. | PUBLIC_PARTIAL | Code and short sample are public; full multilingual corpora and external validation inputs are not assumed public. Dataverse terms and each upstream corpus license require file-level review. | Candidate for P4.3 workflow reconstruction; short sample can validate mechanics, not reproduce all published estimates. |
| LIT-MS-001 — de Kok | Author companion repository [TiesdeKok/chatgpt_paper](https://github.com/TiesdeKok/chatgpt_paper) contains environment file, code examples and datasets in Stata/Parquet; publisher page links supplemental material with full paper code. | PUBLIC_PARTIAL | Public repository/package verified. No explicit repository license was visible in the checked record. Re-execution can require paid APIs, model versions, conference-call inputs and provider terms; current model outputs are not equivalent to historical outputs. | Highest-priority P4.1 workflow candidate after license, environment, API/model-version and raw-input audit. |
| LIT-MS-002 — Chen, Pelger & Zhu | Author repository [LouisChen1992/Deep_Learning_in_Asset_Pricing](https://github.com/LouisChen1992/Deep_Learning_in_Asset_Pricing) provides FFN/GAN/linear notebooks and links to pretrained models and data; Markus Pelger's author page links code/data. | AUTHOR_RESOURCES | Code and resource links are public, but no explicit repository license was visible and data-link persistence/redistribution terms were not established. Source equity and macro data may have third-party restrictions. | Candidate for architecture/OOS benchmark after snapshot, environment, data-license and leakage audit; reported README metrics are not treated as reproduced. |

## Inventory counts

| Availability class | Count |
|---|---:|
| PUBLIC_PACKAGE | 2 |
| PUBLIC_PARTIAL | 3 |
| AUTHOR_RESOURCES | 2 |
| SUPPLEMENT_ONLY | 0 |
| INTEGRITY_HOLD | 1 |
| **TOTAL** | **8** |

These counts describe resource availability, not scientific gate completion or result
validity.

## Public-data and dependency map

| Dependency family | Records affected | Control |
|---|---|---|
| Licensed market/microstructure data (for example CRSP/TAQ/RavenPack) | JFE-002; likely RFS-001/MS-002 | Do not redistribute; record entitlement, vintage and extraction instructions |
| Restricted mortgage/RADAR inputs | JF-001 | Synthetic data are plumbing-only; published-result replication requires authorized access |
| Commercial earnings/analyst/fundamental databases | RFS-002 and potentially related workflows | Integrity hold plus access/license review |
| Text corpora and multilingual source material | RFS-003 | Preserve corpus provenance, copyright and sample/full-data distinction |
| LLM/API version and paid service dependency | JFE-002; MS-001 | Pin provider/model/date/settings; historical outputs cannot be silently regenerated with a newer model |
| Mutable author repositories or file hosts | RFS-001; MS-001; MS-002 | Snapshot commit/file identities and SHA-256 hashes before execution |

## Falsification and audit checks

| Check | Result |
|---|---|
| All eight P2.1 records inventoried | PASS |
| Resource provenance classified | PASS |
| Public package distinguished from public code/sample only | PASS |
| Explicit licenses recorded only when observed | PASS |
| Proprietary/restricted inputs identified | PASS |
| Expression of Concern checked for current status | PASS — investigation pending as of 2026-10-07 |
| Package downloaded or code executed | NOT DONE — outside P2.2 |
| Published result reproduced | NOT DONE — no reproduction claim |
| Third-party reproduction treated as official | PASS — prohibited |

## Gate conclusion

P2.2 is PASS for a source-backed access, package and licensing inventory. Two records
have versioned CC BY 4.0 packages; five have partial or author-controlled resources
requiring additional license/data/environment work; one remains on integrity hold.
No restricted input was copied to public GitHub, no model was run, and no published
result was reproduced.

## Exact next actions

1. P2.3: encode the eight literature nodes, resource nodes, data dependencies,
   licensing edges and the integrity-hold anomaly in the Science Discovery graph.
2. P4 planning: snapshot and hash only the admissible package files before any run.
3. LIT-RFS-002: recheck DOI 10.1093/rfs/hhag017 only when new journal evidence appears
   or during the final repair sweep; do not repeatedly probe the same unresolved notice.
