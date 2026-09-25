# European IFRS, ESG/ESRS/VSME & Student Research Data Layer

This registry extends the Gold Research Datasets Registry. It is additive and does not remove or replace prior resources.

## A. EU IFRS / ESEF

### ESMA ESEF Taxonomy
Authoritative European electronic-reporting reference.
- Official taxonomy page: https://www.esma.europa.eu/electronic-reporting/esef-taxonomy
- ESEF Taxonomy 2025 includes IAS 1 and IFRS 18 entry points/definitions and multilingual taxonomy resources.
- Use: listed-company iXBRL/ESEF filings, taxonomy mapping, extension analysis, accounting-policy and note-disclosure research.
- Governance: record taxonomy year/version; IFRS taxonomy materials have specific copyright/database-right conditions, so do not mirror or redistribute without checking applicable rights.

Research pipeline:
EU issuer annual report → ESEF/iXBRL → IFRS taxonomy/concepts → financial statements + notes → accounting characteristics → assertions → KAM → agent evaluation → falsification → human validation.

Suggested research tables:
eu_issuer; esef_filing; ifrs_fact; extension_tag; note_disclosure; accounting_policy; audit_report; kam; evidence_link.

## B. EU ESG / ESRS

Preferred Gold source hierarchy:
1. EFRAG/European authoritative standards, taxonomies and datapoint structures.
2. Issuer sustainability/annual reports.
3. Verified structured ESG datasets.
4. Community datasets after provenance/license QA.
5. Synthetic reports for testing only.

Research pipeline:
Issuer sustainability report → ESRS structure/datapoint → claim/metric → evidence → assurance assertion → agent → evidence verification → falsification → human validation.

Core research constructs:
disclosure extent; disclosure quality; materiality; comparability; quantitative/narrative balance; evidence coverage; consistency; assurance readiness; hallucination/unsupported-claim rate.

## C. VSME — Student Research Gold Track

### EFRAG VSME Digital Template & XBRL Taxonomy
Authoritative source: EFRAG.
- Official page: https://www.efrag.org/en/vsme-digital-template-and-xbrl-taxonomy
- Digital Template v1.3.0 and VSME XBRL Taxonomy package were published 11 June 2026.
- EFRAG states materials are being updated following the European Commission's Voluntary Standard publication of 3 July 2026, with updated materials scheduled for Q4 2026.
- The taxonomy supports Inline XBRL, XBRL-JSON and XBRL-CSV.
- EFRAG's converter is open-source under MIT; verify the version used in every study.

Student pipeline:
Swedish SME → annual/sustainability disclosure → VSME datapoint mapping → disclosure present/absent → disclosure-quality coding → firm characteristics → validation sample → statistical/AI analysis → human review.

Minimum student dataset:
company_id; org_number_hash_or_public_identifier; year; industry; size variables; report_source; vsme_module; vsme_datapoint_id; disclosed; quantitative; narrative; evidence_quote_location; evidence_page; quality_score; coder; ai_coder; disagreement; validation_status.

Recommended design:
Pilot 10–20 firms
→ refine codebook
→ freeze codebook
→ larger sample
→ double-code validation subset
→ inter-rater/AI-human agreement
→ firm-characteristic tests
→ robustness/falsification.

## D. Student Research Dataset Standard

Every thesis/research project should create four linked artifacts:

1. DATA MANIFEST
- research question
- population/sample
- observation unit
- sources
- collection dates
- versions
- licenses/terms
- exclusions
- identifiers/linkage

2. CODEBOOK
- construct
- variable
- definition
- source
- transformation
- expected type/range
- missing-data rule

3. EVIDENCE TABLE
- observation ID
- claim/label
- source document
- page/section/XBRL fact
- evidence locator
- coder/model
- confidence
- validation status

4. REPLICATION MANIFEST
- code commit
- dataset hash/version
- software/environment
- model/provider/version
- prompt/config hash
- random seed where relevant
- output tables/figures
- deviations from preregistered/frozen design.

## E. Integration with Master Scientific Architecture

European IFRS/ESG/VSME Evidence
→ versioned research dataset
→ Databricks/Delta
→ Evidence Graph
→ FT50/ABS4 theoretical anchor
→ Co-Scientist competing hypotheses
→ AlphaFold-inspired structure reasoning
→ AlphaEvolve-style candidate experiments
→ FRANKENSTEIN orchestration
→ multi-provider agents
→ deterministic verification
→ blind Reviewer/Falsification
→ human validation
→ GitHub/Hugging Face/Kaggle outputs where licensing permits
→ manuscript/student thesis
→ learning loop.

## F. Quality Gate

No dataset is promoted to Gold solely because it is public.
Require: provenance PASS → version PASS → terms/license PASS → construct mapping PASS → evidence traceability PASS → leakage check PASS → validation sample PASS.

_Last curated: 2026-09-25._
