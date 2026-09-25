# Gold Research Datasets Registry — Accounting, Auditing & Financial Reporting

Purpose: curated reference-data layer for the Scientific Discovery Master Architecture. This registry is additive: it does not replace existing datasets, registries, pilots or benchmarks.

## Admission rule

A dataset enters the Gold Registry only after recording:
- authoritative/academic source;
- coverage and unit of observation;
- access method;
- license/terms where available;
- version/snapshot date;
- identifiers for linkage;
- known limitations;
- research construct;
- validation/benchmark role.

Gold does **not** mean error-free. It means preferred, traceable reference evidence for reproducible research.

## Tier A — SEC / EDGAR / XBRL

### Stanford EDGAR Filings Dataset (SEFD)
Academic/open reference: Stanford Advanced Financial Technologies Lab project with Bettencourt, Ding & Giesecke (2026).
- SEFD-v1: public 152B-token snapshot, filings January 2022–June 2025.
- Larger archive described by the project: 18.5M filings / approximately 550B tokens.
- Layout-faithful MultiMarkdown intended for financial language modeling, reasoning and document understanding.
- Derived benchmarks described in the paper: EDGAR-Forecast and EDGAR-OCR.
- Official project: https://github.com/Stanford-Advanced-FinTech-Lab-SAFTL/stanford-edgar-filings-dataset
- Paper: https://arxiv.org/abs/2606.18192
Role: long-context filing evidence and document benchmark layer.

### SEC EDGAR APIs / CompanyFacts
Authoritative source: U.S. Securities and Exchange Commission.
- Company submissions and extracted XBRL data are available through data.sec.gov without API keys.
- CompanyFacts supplies company-level XBRL facts.
- SEC also provides nightly bulk archives.
- Official API documentation: https://www.sec.gov/search-filings/edgar-application-programming-interfaces
Role: authoritative raw/structured source; use to verify reconstructed/derived datasets.

Recommended pairing:
SEC raw filing + CompanyFacts/XBRL
→ SEFD representation
→ deterministic reconciliation
→ Evidence Graph
→ research benchmark.

## Tier A — PCAOB / Audit Inspection

### PCAOB Firm Inspection Reports — machine-readable datasets
Authoritative source: PCAOB.
- Public inspection-report information is available in downloadable CSV/XML/JSON.
- Firm/audit selection data cover published inspection reports.
- Part I.A / I.B machine-readable datasets cover recent inspection-report findings, with stated coverage beginning in 2018/2019 depending on inspection frequency.
- Official page: https://pcaobus.org/oversight/inspections/firm-inspection-reports
Role: audit-quality, deficiency, inspection and falsification research.

Recommended linkage:
PCAOB firm/report
→ audit firm
→ issuer/engagement evidence where linkable
→ SEC filing
→ CAM
→ ICFR
→ inspection outcome.

## Tier A — Fraud / Misstatement / AAER

### SEC Accounting and Auditing Enforcement Releases
Authoritative source: SEC.
- Official chronological enforcement-release source.
- Official page: https://www.sec.gov/enforcement-litigation/accounting-auditing-enforcement-releases
Role: authoritative enforcement evidence and post-event verification.

### USC AAER Dataset
Academic reference dataset.
- Dataset description reports 4,278 SEC AAERs and 1,816 firm misstatement events from May 1982 through December 2021.
- Includes detail, annual and quarterly files and affected financial-statement accounts.
- Dataset: https://sites.google.com/usc.edu/aaerdataset/home
Role: research-ready fraud/misstatement labels; pair with current SEC AAER source for extensions beyond dataset coverage.

Recommended design:
USC AAER labels
+ SEC original AAER documents
+ SEC filings/SEFD
→ company-isolated and out-of-time benchmark
→ fraud/misstatement agent
→ evidence-grounded falsification.

## Tier A — CAM / KAM

### PCAOB / SEC public audit reports and CAM evidence
Authoritative evidence should be reconstructed from filed auditor reports and linked to SEC filings; PCAOB CAM guidance/inspection evidence is used for standards and validation context.

Research layer:
SEC filing/auditor report
→ CAM text
→ account/topic
→ audit assertion
→ evidence
→ persistence / entry / exit
→ human-coded validation.

Existing project CAM/KAM datasets remain preserved and can be registered as controlled research datasets after provenance/version/license fields are completed.

## Tier A/B — ICFR / Material Weakness

Preferred source stack:
SEC filings / XBRL
→ Item 9A / controls disclosures
→ auditor ICFR opinion where applicable
→ restatement/enforcement evidence
→ PCAOB inspection evidence
→ controlled material-weakness labels.

Research requirement:
Do not treat a model-generated ICFR label as ground truth. Preserve source filing, disclosure date, label construction rule and temporal availability.

## Tier A/B — IFRS / European Digital Reporting

Preferred source stack:
official issuer annual reports
→ ESEF/XHTML/iXBRL filings
→ taxonomy/concept mapping
→ accounting-policy notes
→ IFRS judgment task
→ human expert validation.

Before mirroring any ESEF corpus, verify the relevant source's redistribution terms and snapshot/version. Keep standards text/licensing separate from issuer public evidence.

## Tier A/B — ESG / ESRS / VSME

Preferred source stack:
issuer sustainability reports
→ official EU taxonomy/ESRS/VSME reference structures where permitted
→ structured metrics
→ claim/evidence pairs
→ assurance task
→ human validation.

Existing project candidates such as EU-taxonomy and VSME benchmark resources remain in the Hugging Face registry; they should be promoted to Gold only after license, provenance and benchmark-quality checks.

## Cross-domain Gold Evidence Graph

Company
→ CIK / LEI / ticker
→ SEC/ESEF filing
→ XBRL/iXBRL fact
→ financial-statement account
→ accounting assertion
→ ICFR/control
→ audit opinion
→ CAM/KAM
→ PCAOB inspection
→ AAER/restatement
→ IFRS/ESG disclosure
→ source evidence.

## Research-quality hierarchy

1. **Authoritative raw evidence** — SEC, PCAOB, official filings/regulatory sources.
2. **Academic curated datasets** — e.g., SEFD and USC AAER dataset.
3. **Verified benchmark datasets** — reproducible labels/tasks with documented construction.
4. **Community datasets** — useful discovery/experimentation; require independent verification before Gold promotion.
5. **Synthetic data** — testing/simulation only unless independently validated.

## Required dataset manifest

Every dataset used in an experiment should record:
dataset_id; title; domain; source_owner; source_url; citation/DOI; coverage_start; coverage_end; observation_unit; identifiers; access_date; snapshot_hash; license_or_terms; redistribution_status; construction_method; label_definition; temporal_availability; known_limitations; code_commit; linked_experiment_ids; human_validation_status.

## Integration with Master Architecture

Gold/Reference Data
→ Versioned Evidence Store versioning
→ Evidence Graph
→ FT50/ABS4 replication baseline
→ Co-Scientist competing hypotheses
→ AlphaFold-inspired structure layer
→ AlphaEvolve-style candidate experiments
→ FRANKENSTEIN orchestration
→ OpenAI / Claude / Gemini / Microsoft / open-source agents
→ deterministic verification
→ blind Reviewer/Falsification
→ independent replication
→ human approval
→ publication/learning loop.

## First recommended benchmark

**Microsoft SEC/XBRL Pilot 001**
SEC CompanyFacts + raw filing
→ SEFD representation when matching filing is available
→ fact/document reconciliation
→ Accounting Assertions
→ identical multi-provider evidence package
→ MLflow
→ falsification
→ human validation.

This creates a two-source evidence test: authoritative structured SEC facts versus layout-faithful SEFD filing reconstruction.

_Last curated: 2026-09-25._


## Cross-Platform Dataset Matrix — HF × Kaggle × Research execution layer

This matrix distinguishes authoritative/academic evidence from reproducibility and execution resources. A platform listing does not itself make a dataset Gold.

| Domain | Gold / authoritative anchor | Hugging Face candidates | Kaggle / public benchmark candidates | Research execution layer role/resources | Quality use |
|---|---|---|---|---|---|
| SEC/XBRL | SEC EDGAR/CompanyFacts + Stanford SEFD | Existing registry: financial filings/XBRL candidates; re-verify license/revision before promotion | SEC Financial Statement Extracts | Delta ingestion/versioning + MLflow evaluation | Fact reconciliation, filing QA, assertion tests |
| Audit/ICFR | SEC control disclosures + auditor ICFR opinions + PCAOB inspection data | Audit QA/financial benchmark candidates in HF registry | Enterprise data-quality/audit-agent benchmarks | Evidence tables, temporal labels, model/calibration tracking | MW/ICFR prediction, evidence sufficiency |
| CAM/KAM | Filed auditor reports + project CAM/KAM corpus with provenance | Promote only after verified CAM/KAM source/labels | Build controlled notebook benchmark from licensed/project data | CAM/KAM Delta table + persistence/entry/exit + experiment tracking | Classification, longitudinal change, human agreement |
| Fraud/AAER | SEC AAER + USC AAER dataset | Financial fraud/misstatement candidates only after QA | Fraud/anomaly notebooks as secondary benchmarks | Fraud pipelines, out-of-time/company splits, MLflow | Generalization, FNR/FPR, evidence-grounded detection |
| IFRS/ESEF | ESMA ESEF + issuer iXBRL + applicable IFRS taxonomy resources | Existing IFRS/group-audit candidates; verify provenance/license | Public annual-report/financial-statement notebooks only as secondary evidence | iXBRL normalization, extension-tag tables, evidence graph | IFRS judgment, tagging, notes/policy research |
| ESG/ESRS/VSME | EFRAG ESRS/VSME + issuer sustainability reports | EU-taxonomy/VSME/ESG candidates already indexed; Gold promotion requires QA | ESG starter/public sustainability datasets as benchmark layer | ESG datapoint/evidence tables, assurance evaluation | Disclosure quality, evidence coverage, assurance readiness |

### Platform-specific rule

**Hugging Face:** use for reusable public datasets/models/benchmarks. Record dataset revision, card, source provenance, license and construction. Current candidate resources already catalogued in this project remain candidates until re-verification.

**Kaggle:** use primarily for executable notebooks, benchmark packaging and public reproducibility. SEC Financial Statement Extracts is especially useful as a secondary SEC/XBRL benchmark; authoritative SEC sources remain the verification anchor.

**Research execution layer:** treat primarily as the scalable research execution/governance layer rather than a substitute for authoritative datasets. Use Delta for immutable/versioned evidence tables and MLflow for runs, traces, metrics and evaluation. Industry solution accelerators/examples may inform implementation but must not be treated as academic ground truth.

### SEC DERA reproducibility resource

Add the SEC-maintained `sec-gov/python-for-dera-financial-datasets` repository as a preferred implementation resource for Financial Statement Data Sets and Financial Statement and Notes Data Sets. Because it is maintained under the SEC GitHub organization and designed for SEC DERA datasets, it should sit close to the authoritative SEC evidence layer, while the underlying SEC datasets remain the source of record.

### Promotion gate: Candidate → Gold

Source identity verified
→ original source located
→ license/terms checked
→ dataset revision pinned
→ observation unit documented
→ label construction documented
→ temporal availability documented
→ leakage/duplication tested
→ sample manually reconciled to authoritative evidence
→ benchmark baseline reproduced
→ Gold status approved.

### Cross-platform synchronization key

Every mirrored or derived dataset should retain:
`dataset_id + source_record_id + source_version + snapshot_hash + transformation_commit + platform_revision + experiment_id`.

This lets the same evidence be traced across GitHub, Hugging Face, Kaggle, Google Drive and Research execution layer without assuming the copies are automatically identical.
