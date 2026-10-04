# Disagreement Among Large Language Models and Financial Information: Evidence-Governed Multi-Model Signals

**Saeid Homayoun — University of Gävle**  
**JFE working-paper draft — October 4, 2026**

> Research-design manuscript with a public-data proof of concept. No large-sample results are fabricated.

## Abstract
Large language models (LLMs) are increasingly used to interpret corporate disclosures, news, and financial statements, yet empirical research typically treats the output of a single model as the relevant signal. This paper develops a multi-model framework in which identical, time-stamped financial evidence is evaluated independently by frontier and open-weight LLMs. We introduce **AI Disagreement (AID)**, the cross-model dispersion in standardized financial judgments, and ask whether disagreement contains incremental information about future returns, volatility, earnings surprises, financial reporting failures, and audit-risk outcomes after controlling for average AI consensus and conventional predictors.

The design integrates three safeguards that are especially important for finance: evidence-level provenance, chronological integrity to address look-ahead contamination, and falsification-oriented human review. A transparent Microsoft FY2026 proof of concept illustrates the pipeline using public 10-K evidence on revenue recognition, uncertain tax positions, and internal control. The proposed large-sample tests combine SEC filings, earnings disclosures, market data, audit reports, restatements, ICFR weaknesses, and enforcement outcomes.

## Research gap
Existing studies establish that LLMs can:
1. extract financially relevant information from news and disclosures;
2. construct new textual and uncertainty measures;
3. improve or complement human financial analysis; and
4. affect asset-management performance and firm valuation.

The open question is different: **when capable AI models receive the same evidence, does their disagreement itself contain economically useful information?**

## Main constructs
For firm i, information event t, and model m:

`AIConsensus_it = (1/M) Σ_m S_it^(m)`

`AIDisagreement_it = SD(S_it^(1), …, S_it^(M))`

Additional measures include pairwise absolute disagreement, sign disagreement, rank disagreement, evidence strength, and human override.

## Hypotheses
**H1 — Incremental information.** Conditional on AI Consensus and conventional controls, greater cross-model disagreement is associated with larger subsequent absolute market reactions and/or forecast errors.

**H2 — Underreaction.** High AID predicts stronger post-disclosure return drift when information is complex, negative, or difficult to map into valuation.

**H3 — Reporting risk.** High AID is positively associated with subsequent restatements, ICFR weaknesses, CAM/KAM changes, and enforcement outcomes.

**H4 — Evidence quality and governance.** The predictive association between AID and adverse outcomes is stronger when evidence quality is weak and weaker in highly standardized disclosure settings. Human review should add the most value in the high-disagreement/high-materiality quadrant.

## Empirical design
Baseline:

`Outcome_i,t+1 = α + β1 AIConsensus_it + β2 AIDisagreement_it + γ'Controls_it + FirmFE_i + TimeFE_t + ε_it`

Candidate outcomes:
- cumulative and absolute abnormal returns;
- realized volatility;
- earnings surprises;
- financial restatements;
- ICFR material weaknesses;
- CAM/KAM selection and change;
- AAER / SEC enforcement outcomes;
- firm value and related risk outcomes.

Incremental predictive value will be evaluated out of sample using R², AUC, PR-AUC, Brier score, calibration, and recall-at-k as appropriate.

## Chronological integrity
Historical finance applications are vulnerable to LLM training leakage. The project therefore uses:
- ChronoGPT / ChronoBERT where feasible;
- post-knowledge-cutoff subsamples;
- time-stamped evidence packets;
- frozen prompt versions;
- raw output preservation;
- held-out probes not reused after prompt/model development.

## Microsoft FY2026 POC
Microsoft's FY2026 10-K was filed July 29, 2026. Deloitte identified two critical audit matters: **Revenue Recognition** and **Income Taxes — Uncertain Tax Positions**. Deloitte also expressed an unqualified opinion on Microsoft's ICFR as of June 30, 2026.

The POC uses these public disclosures to demonstrate the workflow:
**Evidence → Multi-LLM Review → Consensus/Disagreement → Verification → Human Decision.**

Illustrative screening scores:
- Revenue recognition: 78 / High
- Uncertain tax positions: 82 / High
- AI infrastructure / margin: 55 / Medium
- ICFR: 18 / Low
- Liquidity: 22 / Low

These values are demonstration rules, not empirical findings or audit conclusions.

## Reproducibility
The project is organized to match JFE's data-and-code standard:
- code from raw evidence to final analytical data;
- table/figure scripts;
- software/package versions;
- frozen prompts and model identifiers;
- generation parameters and seeds;
- pseudo-data for restricted/licensed inputs;
- public evidence provenance;
- clear separation between exact and procedural reproducibility for proprietary LLMs.

## Contribution
The proposed contribution is a new financial-information construct: **disagreement across machine agents given an identical evidence set**. Unlike analyst disagreement, the researcher can hold information constant while varying the information-processing system. If AID predicts realized outcomes conditional on the mean AI signal, model disagreement becomes an economically meaningful signal rather than only a quality-control statistic.

## Core references
- de Kok (2025), *Management Science*, 71(9), 7888–7906. DOI: 10.1287/mnsc.2023.03253.
- Lopez-Lira & Tang (2026), *Journal of Financial Economics*, 184, 104335. DOI: 10.1016/j.jfineco.2026.104335.
- Jha, Liu & Manela (2026), *Review of Financial Studies*, 39(5), 1227–1266. DOI: 10.1093/rfs/hhaf012.
- He, Lv, Manela & Wu (forthcoming), *Journal of Financial Economics*, Chronologically Consistent Large Language Models.
- Cao et al. (2024), *Journal of Financial Economics*, 160, 103910.
- Siano (2025), *Management Science*, 71(11), 9831–9855.
- Eisfeldt et al. (forthcoming), *Journal of Finance*, Generative AI and Firm Values.
- Sheng et al. (2026), *Review of Financial Studies*, Generative AI and Asset Management.
- Audrino, Maly & Stalder (forthcoming), *Journal of Finance*, Quantifying Uncertainty.
- García-Llorente & Olmeda (2026), *Finance Research Letters*, 108, 110440.

## Full Word version
The 15-page Word manuscript with the embedded research figure, tables, references, frozen-prompt appendix, and planned replication-package structure is stored in Google Drive. See `WORD_AND_DRIVE_LINKS.md`.
