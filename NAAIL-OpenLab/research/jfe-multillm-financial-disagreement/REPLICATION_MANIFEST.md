# Replication Manifest — NAAIL Multi-LLM Financial Risk Project

## Objective
Test whether disagreement among frontier LLMs contains incremental information about future financial outcomes.

## Core public replication foundations
1. de Kok (2025), *Management Science*: author GitHub for generative-LLM textual analysis.
2. Lopez-Lira & Tang (2026), *Journal of Financial Economics*: official Mendeley Data replication package.
3. Jha, Liu & Manela (2026), *Review of Financial Studies*: Harvard Dataverse code/data.
4. He, Lv, Manela & Wu (forthcoming), *Journal of Financial Economics*: Mendeley replication package plus ChronoBERT/ChronoGPT models.
5. Eisfeldt et al. (forthcoming), *Journal of Finance*: author data repository.

## Reproducibility rules
- Freeze prompt templates before outcome testing.
- Record exact model name/version, provider, date, temperature and other generation parameters.
- Run identical evidence packets across models.
- Preserve raw model outputs.
- Separate development probes from held-out evaluation probes.
- Use chronological models or post-cutoff samples to diagnose look-ahead bias.
- Maintain evidence citations and source hashes where possible.
- Do not report a PASS unless the underlying test actually passes.
- Human approval is required for high-risk/high-disagreement cases.

## Main variables
- AIConsensus: mean standardized model score.
- AIDisagreement: cross-model standard deviation.
- PairwiseDisagreement: absolute score differences for model pairs.
- EvidenceStrength: source-quality / citation-completeness measure.
- HumanOverride: reviewer rejection or material modification.
- Outcomes: abnormal returns, volatility, earnings surprises, restatements, ICFR weaknesses, CAM/KAM outcomes, fraud/AAER outcomes.

## JFE alignment
Accepted JFE empirical papers must make data, programs, and detailed replication instructions available, with documented exceptions and pseudo-data for restricted data.
