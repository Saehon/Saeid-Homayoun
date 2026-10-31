# Evidence-Grounded AI Evaluation for Accounting and Finance

**Research demonstration · standard-library Python · offline · synthetic data only**

This small module illustrates how to **separate the accuracy of a financial answer from the presence of an admissible evidence identifier**. It supports research methods involving LLM outputs and professional review, without making unsupportable model-performance claims.

### Benchmark design and model-neutral comparability

The documented methodology follows [OpenAI, Anthropic, Google, FinanceBench, Inspect AI, HELM and EleutherAI evaluation practices](../LLM_BENCHMARKS_AND_EVALUATION.md). The repository contains **no real provider outputs** or copied third-party benchmark questions.

### Research workflow, evidence and provenance

| Component | Public evidence | Validation boundary |
|---|---|---|
| Financial answer evaluator | [`evaluate.py`](evaluate.py), synthetic data and regression tests | Numeric/error/citation-ID contracts only |
| Paired result comparator | [`compare_runs.py`](compare_runs.py), hand-authored alternative predictions | Illustrative paired comparisons, not model rankings |
| **Provider-neutral run provenance validator** | [`validate_run.py`](validate_run.py), [protocol](PROVENANCE_VALIDATION.md) and negative tests | Verifies local digests and declared metadata; **never attests model execution** |
| Model/benchmark methodology | [OpenAI, Anthropic, Gemini and independent benchmark crosswalk](../LLM_BENCHMARKS_AND_EVALUATION.md) | Framework references, not affiliation or completed benchmarks |

Actual GPT, Claude or Gemini outputs can be evaluated **only after** collection with lawful data rights, contemporaneous model/run records and independent review. This public repository contains *no such empirical outputs*.

### Human evidence-grounding protocol

The [annotation and adjudication protocol](../ANNOTATION_AND_ADJUDICATION_PROTOCOL.md) adds a two-reviewer *synthetic simulation* with an explicit rubric, confusion matrix, disagreement flags and adjudication coverage. Its reviewer IDs are simulated; an empirical use would require real, independent expert raters and source-document entailment assessment.

### Reproduce

Python 3.10+ from repository root:

```bash
python -m research.ai_evidence_evaluation.evaluate --out reports/financial_evidence_synthetic.json
python -m unittest discover -s research/ai_evidence_evaluation/tests -v
```

Expected demonstration: five manually authored synthetic reference cases and five synthetic prediction records (including intentionally wrong or ungrounded answers and abstentions). No model API is invoked, no provider predictions are asserted, and no financial filing or restricted content is distributed.

### Inputs and metrics

- `examples/synthetic_gold.jsonl` — case ID, domain, question, answer type, gold answer, numeric tolerance, evidence IDs, source rights and label provenance
- `examples/synthetic_predictions.jsonl` — predicted answer, status (`answered` or `abstained`), citation IDs
- `--dev-ids` — optional JSON array of identifiers for detection of basic development/holdout overlap
- `--out` — a JSON report with counts, answer correctness, grounded-correct rates, citation ID checks, coverage, abstention, error taxonomy and two input SHA-256 digests

A gold citation-ID match is **not** source-text entailment or an audit conclusion. Text scoring is strict after whitespace/case normalization; numeric scoring uses `decimal.Decimal` with a predefined *absolute* tolerance. Handwritten gold labels are not independent annotations.

### Validation needed for empirical use

1. Obtain approved, properly licensed and dated accounting documents; record filing, issuer, jurisdiction, currency, fiscal period and source IDs.
2. Collect blinded human reference answers, with independent reviewers and disagreement reconciliation.
3. Ensure the question and source excerpt (not the gold answer) is presented to the model and freeze prompts/model versions.
4. Supply real predictions in the JSONL format and record provider usage/cost separately; this demonstration deliberately does not call an API.
5. Evaluate semantic/financial equivalence and citation-text entailment by an expert independent of the system builders.
6. Assess leakage, sample representativeness, uncertainty, sector heterogeneity, error costs and reproducibility before interpreting effects.

### Scientific reference and rights

The Patronus AI [FinanceBench paper](https://arxiv.org/abs/2311.11944) is an external example of the financial-QA evaluation problem; its [public sample](https://huggingface.co/datasets/PatronusAI/financebench) has a CC BY-NC 4.0 license and is **not included here**. OpenAI's [evaluation guidance](https://developers.openai.com/api/docs/guides/evals) and Anthropic's [evaluation engineering](https://job-boards.greenhouse.io/anthropic/jobs/5198255008) highlight the importance of measurable, reproducible performance monitoring. These are methodological references, **not affiliations**.

### Authorship and review

This educational scaffold was prepared with AI coding assistance for an independent academic research repository. It requires investigator review and independent validation before being described as a scientifically verified research instrument. No private POMELO/VERA methods or data are included.

See [Research evidence policy](../RESEARCH_EVIDENCE_POLICY.md).
