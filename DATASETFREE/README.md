# DATASETFREE — Open Professional & Executive Data Registry

**Version:** 2026-10-10 · **Status:** Source discovery and governance, no third-party data mirrored  
**Google Drive master project index:** https://docs.google.com/document/d/18ujpZr_ni_1iuFG5u0XqCQfbIq-W-udrSv1toL9y3jc/edit  
**Canonical Drive folder:** https://drive.google.com/drive/folders/17QYKaBRVkg2Wr-slwrM0gWd_o6EYdUD7

## Purpose
Research registry of legally accessible free datasets for professional careers, CEO/CFO experience, board expertise, auditing, governance, finance and AI-assisted text analysis. These resources are **not** equivalent to Cognism's commercial B2B contact verification and enrichment.

## Track A: CVs, qualifications, skills and career histories

| Dataset | Approximate content | Key uses | Access and caution |
|---|---|---|---|
| [JobHop v2](https://huggingface.co/datasets/aida-ugent/JobHop) | 355,315 pseudonymized career trajectories, 1,993,291 work entries and 923,981 education entries | Longitudinal occupational mobility; ESCO classifications | CC BY 4.0; predominantly Dutch, cannot link to named executives |
| [DatasetMaster Resumes](https://huggingface.co/datasets/datasetmaster/resumes) | 4,817 normalized mixed real/synthetic résumés | NLP skill and experience extraction | Labelled MIT; underlying real-resume provenance and privacy need review |
| [Candidate Matching Synthetic](https://huggingface.co/datasets/michaelozon/candidate-matching-synthetic) | 10,000 synthetic résumés, 2,500 jobs, 2,500 match records | Controlled model evaluation | MIT; no real-world hiring inference |
| [Kaggle Resume Dataset](https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset) | More than 2,400 occupation-tagged résumés | Classification and document parsing | Verify redistribution terms |
| [Resume Corpus](https://github.com/florex/resume_corpus) | Text résumés labelled with occupations | Multi-label occupational prediction | Verify license and personal-data provenance |
| [SyntheticResumeData](https://github.com/jijunhao/SyntheticResumeData) | 2,994 synthetic PDF resumes and annotated layout ground truth | Document extraction benchmarking | Inspect LICENSE before use |

**Reference:** Johary, I., Bied, G., Mara, A. C., & De Bie, T. (2026), [JobHop v2](https://arxiv.org/abs/2607.11715).

## Track B: Executive biographies, boards and financial reporting

| Source | Fields | Research linkage | Caveat |
|---|---|---|---|
| [SEC EDGAR](https://www.sec.gov/search-filings/edgar-application-programming-interfaces) | DEF 14A executive/board bios, annual filings and structured financial facts | CIK × fiscal year -> ICFR, reporting and governance studies | Executive career fields must be extracted and independently verified |
| [UK Companies House](https://find-and-update.company-information.service.gov.uk/) | Appointments, resignations and directorships | Company-number and person/role date matches | Identity matching and personal-data obligations |
| [ORCID Public API](https://info.orcid.org/documentation/integration-and-api-faq/) | Public academic employment/education | Academic labour-market research | Self-reported incomplete profiles |

## Preliminary FT50/ABS4-style empirical study directions
1. **Occupational transitions and skill accumulation**: job sequence features and next-role probabilities from JobHop.
2. **CFO accounting/audit expertise and ICFR**: lagged CFO experience measures built from SEC DEF 14A, linked by CIK-year to filing outcomes, controlling for firm and year effects and selection threats.
3. **Board financial expertise and disclosure/audit risk**: proxy-biography expertise measures and director networks, with temporally appropriate outcome variables.

These are *research designs*, not tested hypotheses. No claim of novelty or significant results.

## Reproducibility / governance checklist
- Verify original source, dataset version/commit and actual usage licence.
- Record record count, observation unit, years, geography, variables, missingness and duplicate share.
- Distinguish synthetic, anonymized, and identifiable person data.
- Do not mirror third-party CV files or personal contact information to public GitHub.
- Evaluate GDPR lawful basis, data minimization, retention and access restrictions.
- Human-validate LLM-extracted experience and professional expertise; log provenance and error rates.
- Pre-register or freeze joining rules, treatment timing and robustness designs before inference.

## Registry schema
`dataset_id, source, url, accessed_on, version, record_count, unit, years, geography, variables, license_claim, rights_verified, pii_risk, firm_linkable, citation, status, limitations`

## Platform connections
- **Google Drive:** canonical source of truth (above).
- **GitHub:** version-controlled documentation and future code (this directory).
- **Hugging Face / Kaggle:** links to external sources above; project-owned datasets and notebooks have **not** yet been published.
