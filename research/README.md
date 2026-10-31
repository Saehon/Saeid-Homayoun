# Research Portfolio | Saeid Homayoun

**Accounting, auditing, financial reporting and responsible artificial intelligence**  
University of Gävle, Sweden · [ORCID](https://orcid.org/0000-0002-2536-0446) · [Google Scholar](https://scholar.google.com/citations?user=1PKckooAAAAJ&hl=en)

I study how **large language models (LLMs), financial NLP, machine learning, multi-agent systems and evidence-based AI governance** can strengthen the reliability of accounting information, professional judgment and assurance. My research combines accounting theory and empirical analysis with reproducible software experiments, source provenance, falsification and human oversight.

This is an **independent academic research and education portfolio**. Model providers, universities, professional bodies, audit firms and standards setters mentioned in scientific literature are not implied to sponsor or endorse this repository.

## Research highlights and work in progress

[**Explore the featured research programmes, current scientific status, and access boundaries**](RESEARCH_HIGHLIGHTS_AND_ONGOING_PROJECTS.md).

**Research status and primary working material:** The featured programmes remain under active development. Their primary working documents and substantive research materials are maintained in a private, access-controlled personal Google Drive. The public GitHub repository contains selected research outputs, versioned software and open methodology rather than the full working archive.

## Research themes

| Theme | Scientific questions and methods | Research materials |
|---|---|---|
| **LLM evaluation for finance and accounting** | When are financial answers correct, source-grounded and reproducible? Numerical rubrics, abstention, adversarial cases, evaluation leakage checks | [Reproducible evidence-based evaluation demonstration](ai_evidence_evaluation/README.md) |
| **AI-enabled auditing and assurance** | How should CAM/KAM, ICFR, audit responses and inspection evidence be measured and challenged? | [KIWI research](../NAAIL-OpenLab/KIWI/README.md) · [IFRS-AI Inspector](https://github.com/Saehon/IFRS-AI-Inspector) |
| **Agentic AI and human governance** | How can multiple models collaborate without replacing professional authority? Evidence passports, decision traceability, reviewer/falsification gates | [NAAIL architecture](../NAAIL-OpenLab/README.md) · [Portfolio governance](../NAAIL-OpenLab/PORTFOLIO_GOVERNANCE.md) |
| **Financial disclosure and sustainability** | Financial reporting judgment, IFRS/ISSB, ESG, disclosure quality and measurement validity | [Academic research index](../ACADEMIC_PORTFOLIO_INDEX.md) |
| **Data and financial analytics** | SEC/XBRL, missing data, cost behavior, financial predictions, transparent panels and temporal integrity | [Research integrations](../research-integrations/ft50-github-replication-2023-2026/README.md) (where available) |

## Inspectable code and validation

- [**Financial AI and evidence evaluation**](ai_evidence_evaluation/README.md) — executable Python, synthetic unit tests and reproducibility artifacts.
- [**Run provenance and model-neutral metadata**](ai_evidence_evaluation/PROVENANCE_VALIDATION.md) — file hashes, model/version declarations, costs and timestamps, without claiming API attestation.
- [**Methodological benchmark comparison**](LLM_BENCHMARKS_AND_EVALUATION.md) — published evaluation practices for model reliability and professional judgment.

This public code provides a **testable research infrastructure**, not evidence that GPT, Claude or Gemini has been benchmarked on a statistically validated sample.

## Research method: evidence before claims

```mermaid
flowchart LR
    A[Research question] --> B[Authoritative or permitted source]
    B --> C[Evidence and temporal provenance]
    C --> D[Model or statistical analysis]
    D --> E[Deterministic checks and adversarial cases]
    E --> F[Replication and independent review]
    F --> G[Human interpretation and scientific reporting]
```

**Reproducibility policy.** Distinguish (1) a research proposal, (2) implemented code, (3) tests executed on synthetic examples, (4) measured experiments on permitted real data, (5) independently reviewed findings, and (6) peer-reviewed publications. None is interchangeable. Version model identifiers, prompts, sampling rules, source-rights information, monetary costs and known limitations where they apply.

## Transparent model evaluation standards

[**LLM Benchmark and Evaluation Methods**](LLM_BENCHMARKS_AND_EVALUATION.md) — a source-linked methodological crosswalk covering OpenAI, Claude, Google Gemini, FinanceBench, Inspect AI, HELM and lm-evaluation-harness. The guide distinguishes benchmark frameworks from completed empirical evaluations, licensing rights and independent assurance.

## Evidence-grounding and human-review research

[**Double-annotation, disagreement and adjudication protocol**](ANNOTATION_AND_ADJUDICATION_PROTOCOL.md) — an executable, synthetic calibration of the distinction between numerical agreement, evidence support and qualified human judgment. This demonstration does **not** claim independent human annotations or empirical scores for any model provider.

## Executable research demonstration

The [Evidence-Grounded Financial AI Evaluation](ai_evidence_evaluation/README.md) module includes an **offline, deterministic Python evaluator**, a small synthetic corpus, documented scoring contracts, negative tests, and a CI workflow. It is designed as a foundation for proper evaluation studies; it **does not invoke any AI model or claim empirical model accuracy**. Human-labelled/appropriately licensed corpora and real model outputs must be separately supplied before empirical claims.

## Publications and open-science identity

**[Selected peer-reviewed research and Routledge book — bibliographic sources](SELECTED_PUBLICATIONS.md)**

Research publications, their verified bibliographic records and citation indicators should be consulted directly through [Google Scholar](https://scholar.google.com/citations?user=1PKckooAAAAJ&hl=en) and [ORCID](https://orcid.org/0000-0002-2536-0446). Avoid treating citation totals in a README as permanently current or asserting DOI metadata that has not been verified.

## Source code and intellectual-property boundaries

Some public repositories under this GitHub account are **external forks/reference sources**, not original software. In particular, `financebench` originates with Patronus AI, `inspect_ai` with the UK AI Security Institute, and `timesfm` with Google Research. Their upstream authors and licenses remain distinct from original NAAIL contributions.

Private research and unpublished methods (including proprietary POMELO work) must not be copied into public repositories. Licensed financial datasets, identifiable individuals, internal institutional records, confidential standards text, prompts/secrets and unreviewed commercially sensitive methods remain excluded.

## How to explore

Begin with the executable module and its tests, then examine the scientific architecture and research-index links. For independent academic collaboration, cite the published work directly and refer to exact commits or released artifacts rather than asserting unverified system maturity.

*Research documentation maintained in English; substantive scientific findings require supporting evidence and independent professional judgment.*
