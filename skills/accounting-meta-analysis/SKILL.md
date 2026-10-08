---
name: accounting-meta-analysis
description: Use for systematic reviews, meta-analyses, meta-regressions, evidence syntheses, and publication-bias assessments in accounting, auditing, finance, economics, and management, including text measures and mixed empirical designs. Use when studies must be located, screened, extracted, converted to comparable effects, combined, and documented without inventing evidence.
---

# Accounting Meta-Analysis

## Purpose

Design an auditable evidence synthesis from a research question through extraction, effect-size harmonization, dependence handling, heterogeneity analysis, moderator tests, and reproducible reporting. The unit of evidence is a study or reported estimate with a traceable source—not a sentence in an abstract.

## Non-negotiable rules

- Freeze the question, eligibility criteria, search sources, cutoff date, and protocol before interpreting pooled results. Record amendments.
- Keep study identification, screening, extraction, analysis, and interpretation distinct. Use two-pass or independent checks for high-impact fields when possible.
- Never invent an effect size, sample size, standard error, journal status, or “significant” result. Mark unavailable fields as missing and explain how they affect inference.
- Preserve the original reported statistic and every conversion. Do not mix standardized mean differences, correlations, odds ratios, log odds, and regression coefficients without a defensible scale.
- Treat multiple estimates from one paper as dependent unless the design proves otherwise. Do not count a paper’s robustness table as independent studies.
- Report uncertainty, heterogeneity, selection, and the limits of the evidence—not only a pooled point estimate.

## Workflow

### 1. Protocol and study map

Write the question as `population/setting → exposure or treatment → comparator → outcome → estimand → time horizon`. Define eligible designs, languages, years, journal/repository status, minimum information, and exclusion reasons. Maintain a search log with query, source, date, result count, deduplication rule, and screening disposition.

Build a study map with `study_id`, DOI/URL, paper version, sample period, unit, country/market, design, treatment, outcome, model, covariates, estimator, reported statistic, and data/code availability.

### 2. Extraction and measurement audit

Use a codebook with separate fields for:

- construct and operational measure;
- estimand and direction;
- statistic and its uncertainty;
- sample size and dependence cluster;
- specification and fixed effects;
- timing and information set;
- subgroup/moderator labels;
- source page/table/figure and extraction confidence.

Audit whether similar labels represent the same construct. For accounting text, distinguish dictionary counts, embeddings, classifier probabilities, human-coded measures, and financial outcomes. Construct similarity is not measurement equivalence.

### 3. Effect-size conversion

Choose the target scale before pooling. Common conversions include:

- correlations `r` with Fisher `z` for sampling calculations;
- odds ratios with `log(OR)`;
- two-group means with standardized mean difference and small-sample correction;
- regression `t`, `z`, or standard errors only when the coefficient’s scale and target estimand are compatible.

Store `reported_effect`, `reported_se`, `conversion_formula`, `target_effect`, `target_se`, assumptions, and source location. Do not convert a causal coefficient into a correlation merely to increase the pool. When conversion is not defensible, synthesize narratively or stratify.

### 4. Dependence, pooling, and heterogeneity

Use random-effects or multilevel/robust-variance methods when study effects differ and estimates are dependent. Pre-specify how to select one estimate, aggregate outcomes, or model nested effects. Report `k` studies, `m` estimates, weighting, estimator, confidence interval, `tau²`, `I²` where appropriate, and a prediction interval. Explain the practical meaning of heterogeneity instead of treating a low p-value as a verdict.

### 5. Moderators and robustness

Pre-specify moderators such as journal/period, regime, country, sample construction, design, outcome definition, text measure, data source, and estimator. Separate confirmatory moderators from exploratory ones. Run leave-one-study-out or influence checks, alternative effect scales, dependence specifications, and reasonable missing-data scenarios. Avoid “researcher degrees of freedom” disguised as a large moderator table.

### 6. Selective reporting and interpretation

Use funnel plots, small-study diagnostics, Egger-type tests, PET-PEESE, trim-and-fill, or selection models only with their assumptions and low power stated. These are diagnostics, not automatic corrections. Compare published, working-paper, dissertation, registry, and replication sources where eligible; do not treat unpublished work as inferior by default.

### 7. Text and economics extensions

For SRAF, AnalyText, EDGAR/XBRL, or similar text sources, freeze the dictionary/model version, document human validation, and test whether the text construct is stable across periods and industries. For Ken French or Damodaran variables, align dates and definitions to the study’s estimand; do not use later-released or post-treatment information. Report source roles and licenses separately from the statistical result.

## Deliverables

Return a protocol, search/screening log, study-level extraction sheet, conversion ledger, analysis script/notebook, pooled-results table, heterogeneity/moderator table, bias diagnostics, and limitations. Every table should be regenerable from the ledger. Provide a “not estimable” section when the evidence cannot support a pooled result.

## Reference

Use `references/effect-size-and-bias.md` for a compact conversion and diagnostic checklist.
