# Optional external validation: FinanceBench (Patronus AI)

Source: https://huggingface.co/datasets/PatronusAI/financebench  
Reference: Islam et al., *FinanceBench: A New Benchmark for Financial Question Answering* (2023), https://arxiv.org/abs/2311.11944  
License of public 150-example set: **CC BY-NC 4.0**. Commercial/portfolio distribution outside these terms requires further legal review.

**No benchmark records or corporate PDFs have been copied into this repository.** This is only an offline evaluator. Download the authorized public sample separately under the license and preserve its attribution.

## Input

Gold: one FinanceBench JSONL record per line, with `financebench_id`, `answer`, optional `question_type`, and `evidence[].evidence_doc_name`.

Model predictions: JSONL records with `financebench_id`, `predicted_answer`, and optional `cited_evidence_doc_names` array.

## Evaluate real predictions (provided separately)

```bash
python -m portfolio_roles.google_finance_eval.financebench_adapter --gold /licensed/financebench_open_source.jsonl --pred "model_A=/results/model_A.jsonl" --pred "model_B=/results/model_B.jsonl" --out /results/financebench_comparison.json
```

**Not included:** the dataset itself, model inference, API keys, proprietary client data, model-generated predictions, or human adjudication.

Metrics: coverage, abstention rate, strict exact string matching across all examples and answered-only, citation-to-reference document-name matching, breakdown by question type. **Strict textual equality is not semantic correctness; matching a gold document name is not proof of grounded reasoning.** An expert review and numeric equivalence protocol are required before publishing substantive model-accuracy claims. Do not claim that Gemini, GPT, Claude or another real model was evaluated until its independently captured predictions are supplied and validated.
