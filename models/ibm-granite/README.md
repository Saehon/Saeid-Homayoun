# IBM Granite Models

IBM Granite is the default IBM model family for this research layer.

## Recommended roles

- **Granite 4.x language models** — accounting/audit extraction, classification, structured JSON, RAG synthesis and agent tool use.
- **Granite Embedding R2** — semantic retrieval over annual reports, audit reports, CAM/KAM text, control narratives, IFRS/ESG documents and research evidence.
- **Granite time-series models** — optional experiments for financial/economic forecasting where a time-series foundation model is methodologically appropriate.

## Reproducibility rule

Record the exact model repository, revision/commit, tokenizer, prompt/template, generation settings and date of access for every empirical run. Never silently replace a model during a study.

## Example research pipeline

`Docling → cleaned evidence → Granite Embeddings → retrieval → Granite LLM → Reviewer Agent → Falsification Agent → Human Gate`

Official model hub: https://huggingface.co/ibm-granite
