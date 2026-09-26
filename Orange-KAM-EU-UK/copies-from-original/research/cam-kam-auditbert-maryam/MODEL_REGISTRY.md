# Model Registry

This registry links the CAM/KAM AuditBERT research package to the model repositories explicitly named in the revised manuscript.

## Topic classifier

**Hugging Face:** https://huggingface.co/MaRyAm1295/finBERT-KAM

- Task: text classification
- Architecture: BERT / AutoModelForSequenceClassification
- Parameters: approximately 109.8M
- Base model: `yiyanghkust/finbert-tone`
- Research role: classify CAM/KAM disclosures into accounting-topic categories.

## Response generator

**Hugging Face:** https://huggingface.co/MaRyAm1295/Llama-3.1-8B-KAM

- Task: text generation
- Architecture: Llama / AutoModelForCausalLM
- Parameters: approximately 8.17B
- Base model: `meta-llama/Llama-3.1-8B-Instruct`
- Training/deployment tags indicate SFT, 4-bit quantization, and bitsandbytes.
- Research role: generate context-aware responses to audit matters.

## Reproducibility boundary

These model repositories are external to the Saehon GitHub account and are owned by the Hugging Face account `MaRyAm1295`. The GitHub package therefore links to them as research dependencies rather than claiming ownership or mirroring model weights.

## Evaluation mapping from the revised manuscript

| Component | Metric | Reported value |
|---|---|---:|
| Topic classifier | Macro precision | 85.15% |
| Topic classifier | Macro recall | 82.08% |
| Topic classifier | Macro F1 | 83.20% |
| Topic classifier | Weighted precision | 88.98% |
| Topic classifier | Weighted recall | 89.03% |
| Topic classifier | Weighted F1 | 88.92% |
| Response generator | BERTScore precision | 84.19% |
| Response generator | BERTScore recall | 83.75% |
| Response generator | BERTScore F1 | 83.95% |

Do not interchange the classifier F1 values with the response-generation BERTScore values.
