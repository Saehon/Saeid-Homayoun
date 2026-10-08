---
name: accounting-text-economics-data
description: Use to integrate accounting, auditing, finance, or disclosure text measures with economic, market, valuation, audit, ICFR, CAM/KAM, ESG, or restatement outcomes. Covers SRAF, AnalyText, EDGAR/XBRL, Ken French, Damodaran, Kaggle, GitHub, and Hugging Face source mapping, identifier/date alignment, NLP validation, leakage controls, and reproducible joins.
---

# Accounting Text + Economics Data

## Purpose

Design a leakage-safe, construct-valid pipeline that connects text to economic outcomes. Separate source discovery from evidence, measurement from inference, and association from causation. Public availability of a dataset or model does not establish its quality, license, or relevance.

## Operating contract

- Freeze the text construct, dictionary/model version, tokenization, language, window, and human-validation plan before testing outcomes.
- Record the information date of every text and economic variable. A filing date, fiscal year, announcement date, and data-release date are not interchangeable.
- Join on stable identifiers and documented crosswalks; never merge on company name alone.
- Treat SRAF, AnalyText, EDGAR/XBRL, Ken French, Damodaran, Kaggle, GitHub, and Hugging Face as source roles to verify at run time. Record URL, access date, version/commit, license, and transformations.
- Keep discovery, feature engineering, outcome construction, sample selection, and analysis in separate steps so leakage and post-treatment conditioning can be audited.

## Workflow

### 1. Define construct and estimand

Write a measurement card:

`construct → text unit → population → time window → measure → validation → hypothesized channel → economic estimand → outcome date`.

Distinguish tone, uncertainty, readability, specificity, risk, boilerplate, disclosure presence, and semantic similarity. Choose whether the estimand is predictive, associational, or causal. State what would falsify the interpretation.

### 2. Map sources and identifiers

Build a source table with `source | role | coverage | unit | release date | identifier | license/access | version | known bias | transformation`. Typical roles:

- text and filings: EDGAR/XBRL or a verified project-specific corpus;
- text features: SRAF/AnalyText or a documented dictionary/model output;
- market returns/factors: Ken French or another cited factor source;
- valuation and cost-of-capital inputs: Damodaran or a cited alternative;
- code/model/data supplements: GitHub, Hugging Face, Kaggle, or the project’s own release.

Then build crosswalks for issuer identifier, CIK/ticker, fiscal year, filing accession, announcement date, and industry. Retain unmatched rows and explain attrition.

### 3. Construct text features

Start with an interpretable baseline: counts/rates, section-specific measures, readability, or a validated dictionary. If using FinBERT, Llama, embeddings, or another model, freeze model/tokenizer versions, prompt or fine-tuning data, truncation/chunking, aggregation, and calibration. Validate on human-coded examples across industries and time; report agreement, calibration, class balance, and drift. Do not call a generic sentiment score “risk” without construct evidence.

### 4. Align timing and prevent leakage

Create a timing table for every feature and outcome. Use only information available at the prediction or event date. Apply temporal train/validation/test splits, lag text when the research design requires it, and exclude later revisions or restatements unless the question explicitly studies them. Test look-ahead by shuffling dates, using pre-event windows, and comparing real-time versus revised data where available.

### 5. Test the economic link

Choose outcomes that match the mechanism and timing:

- event returns: CAR/abnormal returns with a stated event and estimation window;
- factor-adjusted returns: FF-style alpha or other documented factor model;
- valuation/cost of capital: clearly defined inputs, horizon, and sensitivity to assumptions;
- audit outcomes: fees, report lag, going-concern, restatement, ICFR material weakness, or CAM/KAM disclosure with selection and timing addressed;
- ESG or sustainability outcomes: construct, provider, rating date, and disagreement documented.

Pre-specify fixed effects, clustering level, controls, winsorization, missingness, and multiple-testing treatment. Do not control for a post-text mediator when estimating the total association.

### 6. Diagnose merges and selection

Report row counts after each join, duplicate keys, unmatched identifiers, date gaps, missingness by group, sample attrition, and selection into filings or disclosures. Compare included and excluded observations. Use clustered or panel-appropriate uncertainty and document any class imbalance or rare-event correction.

### 7. Robustness and replication

Vary dictionary/model, text section, window, identifier crosswalk, factor specification, industry/time controls, and reasonable outlier rules. Add placebo dates, negative controls, pretrends, temporal holdouts, and alternative outcomes. Preserve all branches in a decision log; do not select the branch with the most favorable p-value after inspection.

## Deliverables

Return a data map, identifier/date crosswalk, feature codebook, source/license ledger, merge-quality report, leakage tests, analysis specification, robustness matrix, and reproducible run instructions. Link every released feature to its source version and every economic result to its outcome construction.

## Reference

Use `references/source-and-join-map.md` for source roles, joins, and common failure modes.
