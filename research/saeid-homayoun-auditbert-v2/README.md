# Dr. Saeid Homayoun | AuditBERT V2: Independent CAM–KAM Research Extension

**Principal developer / new research extension:** Dr. Saeid Homayoun, University of Gävle (Sweden)  
**Verified deployment (16 October 2026):** Free public Hugging Face static research demo and TWO private model-card repositories have been created under ID `SADHON`. All model checkpoints are **untrained**, no original data were released, and no new validation score is claimed.

## Scope
A separately attributable research-extension project for accounting-topic classification and eventual evidence-grounded CAM/KAM response generation. This repository is the **canonical public code**. Confidential/possibly licensed source spreadsheets and unpublished manuscripts remain in Google Drive. Reuse the existing canonical synthetic reproducibility package instead of duplicating data.

- **Prior collaborative paper (cite, do not re-issue as sole-author work):** Homayoun, S., Rezaee, N., Rezaee, Z., & Khosravian, M. *AI-Enabled Key Audit Matter Disclosures: A Hybrid LLM Approach to Enhancing Audit Report Transparency*. SSRN 7272139, https://doi.org/10.2139/ssrn.7272139.
- **Related collaboration and pre-existing replicability package:** [CAM–KAM AuditBERT](../cam-kam-auditbert-maryam/README.md). Prior contributions and original model repositories remain attributed to their respective authors/owners.
- **Original third-party checkpoints for comparison only:** [MaRyAm1295/finBERT-KAM](https://huggingface.co/MaRyAm1295/finBERT-KAM) and [MaRyAm1295/Llama-3.1-8B-KAM](https://huggingface.co/MaRyAm1295/Llama-3.1-8B-KAM). **Their weights are not owned or copied by this extension.**
- **FinBERT base for new training:** [yiyanghkust/finbert-tone](https://huggingface.co/yiyanghkust/finbert-tone), with original-base citation and applicable license verified before distribution.

## Linked identities and storage
| Surface | Canonical use | Link |
|---|---|---|
| GitHub | Source code, tests, provenance | https://github.com/Saehon/Saeid-Homayoun |
| Hugging Face | Public **static** CAM/KAM demonstration created; two **private, untrained** model-card repositories created | https://huggingface.co/spaces/SADHON/dr-saeid-homayoun-auditbert-v2 |
| Google Drive | Private source workbooks, draft paper, research registry; **not publicly synchronized** | https://docs.google.com/document/d/1YmktPLQ-be1sIFd-Ghlpvd7r156C2boC3y9eofM8p6k/edit |
| Kaggle | Reuse the [existing synthetic dataset publishing workflow](../../.github/workflows/kaggle-cam-kam-auditbert-sync.yml), do not publish private training data | https://www.kaggle.com/datasets/sadhon/cam-kam-auditbert-public-demo |
| SSRN | Existing collaborative preprint; V2 requires new findings and appropriate authorship decision | https://ssrn.com/abstract=7272139 |


## Existing original code located in Google Drive — authoritative archive (verified 16 Oct 2026)

The earlier project **already has executable research notebooks in Google Drive**. These are original collaborative-project assets, not V2 code newly invented here. Maintain and inspect the existing Drive archive rather than duplicating it. The independent V2 scripts in this draft are optional extensions/comparators and **must be reconciled against the original notebooks and their provenance before any research claim or model training**.

**Canonical original paper-code ZIP:** [KAM-Paper-Code.zip](https://drive.google.com/file/d/1cqb2wNWyEn0DJJYCJnCaLN8b-kZxPpO3/view), within the [existing research archive](https://drive.google.com/drive/folders/1dmmYE7GuqUM-jfrOOW3nUwERxvxQDD6m). Its downloaded archive was inspected without executing cells. SHA-256: `0d9936250c0d8a55b721990e6795f72ac34c1d56160868d9533166013fa267be`. It contains **seven research notebooks**: one dataset-info notebook, three topic-classification/model-comparison notebooks, and three response-generation/fine-tuning/comparison notebooks.

| Original Drive notebook | Intended prior-code role |
|---|---|
| [KAM_finBERT_Topic_Classifier.ipynb](https://drive.google.com/file/d/1Ckx9s6ts1oHUIGn75GmUkYaik7ry4ia0/view) | Historical FinBERT topic-training implementation |
| [KAM_finText_Topic_Classifier.ipynb](https://drive.google.com/drive/folders/1sYHv5lc5GdM9jmc6UCpPnybO6HhYVA40) | Historical financial-text topic-classification baseline |
| [KAM_finBERT_vs_models_comparison.ipynb](https://drive.google.com/file/d/1sgHrxvRTh5xdLPpX5t9Via9k7mlcgxQo/view) | Historical classifier comparisons |
| [Fine_Tuning_KAM_on_Llama3-1_8B.ipynb](https://drive.google.com/file/d/1JVAllEeQbPozVe76frEYzcARbMu3fJtA/view) | Historical Llama 3.1 8B supervised fine-tuning code |
| [KAM_Response_Generator.ipynb](https://drive.google.com/file/d/1ZxySHiHvby4X3qByVzDqVQKGy5GVOgiu/view) | Historical audit-response generation |
| [KAM-Llama3-1_vs_models_comparison.ipynb](https://drive.google.com/file/d/1YirnMNDbhTIRexA6NQviIoQhWcnxZYCZ/view) | Historical response-generator evaluation |
| dataset_info.ipynb | Data profiling; also inside the canonical ZIP |

**Security inspection:** The archived notebook code contains patterns resembling embedded Hugging Face access tokens. Because these might be active credentials, **do not publish or copy any original notebook directly to public GitHub, Kaggle or Hugging Face**. Audit/sanitize the notebooks, revoke and rotate potentially exposed credentials, clean notebook outputs and paths, check redistributable rights, and retain the unmodified originals privately. This scan does not establish that any credential remains valid or that any repository was compromised. No tokens or source code from this ZIP have been committed here.

**Decision:** Original paper's methods/code = archived Google Drive as source; GitHub = reviewed, sanitized, attributable reproduction and *new* Dr. Saeid Homayoun V2 implementation. Differences in splits, topic labels, data-cleaning decisions, hyperparameters and metric calculations require a documented comparison before merging or SSRN release. No assertion that the V2 scripts reproduce the prior paper's reported metrics.

## Private Drive source references (no automatic export or replication)
- `SOURCE — US CAM — CAMs for US firms.xlsx`
- `kam (uk)2023.xlsx` and associated UK KAM workbooks
- `AuditBERT_KAMs_Maryam_Khosravian_Revised_2026-06-07.docx`
- `ssrn-7272139.pdf`

These are references to identified assets, not claims that their observations were read, downloaded, licensed for release, or trained on in V2.

## Published Hugging Face assets (verified 16 October 2026)

- [Public no-cost static Space: Dr. Saeid Homayoun AuditBERT Lab](https://huggingface.co/spaces/SADHON/dr-saeid-homayoun-auditbert-v2). Fully browser-side keyword-screening demonstrator; **not yet a model inference or trained classifier**. The Python Gradio variant is staged in GitHub only because free Hugging Face Gradio/Docker cpu-basic hosting currently requires PRO.
- [Private model-card staging: Saeid-FinBERT-KAM-V2](https://huggingface.co/SADHON/saeid-finbert-kam-v2). Repository created with a documented future independent training plan; **no weights/real-world performance**.
- [Private model-card staging: Saeid-Llama-3.1-8B-KAM-V2](https://huggingface.co/SADHON/saeid-llama-31-8b-kam-v2). Repository created; **no adapter weights or response metrics**.
- [Verified successful GitHub-to-Hugging Face publishing run](https://github.com/Saehon/Saeid-Homayoun/actions/runs/38866593916). Hub write access was provided by the existing `HF_TOKEN` GitHub Actions secret; no credential value was disclosed or copied to this code.

**Important:** Hugging Face **account ID remains SADHON**; the research project appears under the name **Dr. Saeid Homayoun**. Changing the Hub profile display name itself is a distinct account-settings action and was not performed.

## Architecture
```text
PRIVATE GOOGLE DRIVE (CAM/KAM + provenance + right-to-use check)
    | authorized manual runtime export only; no GitHub upload of raw data
    v
Schema + text quality + duplicate checks + company and year identifiers
    |-- GitHub canonical source/test protocol
    |-- FinBERT V2: NEW fine-tuning of yiyanghkust/finbert-tone
    |     company-disjoint OR forward-in-time 3-way test split
    |     macro/weighted F1 + per-class supports + independent test
    |-- TF–IDF + LinearSVC classifier benchmark (source code added, CPU executable)
    |-- External checkpoint comparator (only where license/access permits)
    |-- Independent KAM-Llama-8B QLoRA SFT trainer (source code added; not executed)
    v
Human evidence review, disclosure-specificity/error audit, provenance
    |-- Hugging Face SADHON: model weights/cards after real training and rights review
    |-- Kaggle: only approved synthetic/redistribution-safe data
    v
New research paper / SSRN submission with distinct research question/results
```

## Reproducible execution (no local-PC requirement)
Use a hosted Google Colab or Kaggle notebook with authorized access to Google Drive. **Never commit the mounted Drive data, credentials or model checkpoints to a public GitHub repository.**

Install:
```bash
pip install pandas openpyxl scikit-learn torch transformers accelerate
```
Dry-run against the existing synthetic sample (checks input, **does not train**):
```bash
python research/saeid-homayoun-auditbert-v2/train_finbert_topic.py \
  --input research/cam-kam-auditbert-maryam/synthetic_cam_kam_sample.csv --dry-run
```
Real **private** training from an approved Drive export (CSV or XLSX):
```bash
python research/saeid-homayoun-auditbert-v2/train_finbert_topic.py \
  --input /content/drive/MyDrive/approved_canonical_cam_kam_export.csv \
  --output /content/drive/MyDrive/auditbert_v2_private_model \
  --split company --epochs 3 --seed 42
```
For forward-time robustness, use `--split year --cutoff 2022` (train through 2021; validate 2022; test 2023 onwards). Ensure the given dataset covers each period. The script aborts rather than silently train on unsupported classes.

Optional independently authored **8B response-generation SFT adapter** (requires authorized `response` column, Meta Llama access and Colab/Kaggle CUDA GPU):
```bash
pip install datasets peft trl bitsandbytes
python research/saeid-homayoun-auditbert-v2/train_llama_response_qlora.py \\
  --input /content/drive/MyDrive/approved_canonical_cam_kam_export.csv \\
  --output /content/drive/MyDrive/auditbert_v2_private_qlora --split company
```
This produces a private research adapter and held-out evaluation loss, **not** a measured BERTScore/F1 or an audit opinion; human source-grounded tests remain mandatory.

To run the **TF–IDF baseline** with the same company/time split:
```bash
python research/saeid-homayoun-auditbert-v2/benchmark_tfidf.py \\
  --input /content/drive/MyDrive/approved_canonical_cam_kam_export.csv \\
  --output /content/drive/MyDrive/auditbert_v2_tfidf_report.json --split company
```
Do not interpret metrics from the synthetic three-row example as empirical results.

**Minimal-file policy:** keep using the same canonical Drive workbook with new stage tabs; do not create per-run spreadsheets. In GitHub, modify the canonical code in place, use commits/history, and link to the prior collaboration rather than copy its assets.

## Evaluation and publication gates
1. Reconcile 48 vs 49 taxonomy classes; archive exact label mapping, data license and sample-flow reconciliation. Prior manuscript's 65,192 records is **not** verified as V2 training data.
2. Retain issuer-disjoint and forward-time holdouts; run fixed seeds and compare TF–IDF, base FinBERT, fine-tuned FinBERT V2, and prior model (per permission).
3. Report macro/micro/weighted F1, support, confidence intervals and audited errors. Do not conflate **classifier macro F1 83.20%** with **generation BERTScore F1 83.95%** reported in the prior manuscript.
4. Separate topic classification from response generation; generated audit procedures must cite their source text and be reviewed by an auditor.
5. Publish a new checkpoint on `SADHON` only when training genuinely completed, licenses are cleared and the model card includes trained-on data description, group/time split, metrics, limitations, and attribution.
6. A new SSRN paper must be materially original and use accurate authorship; repository ownership, supervisory status or seniority alone do not settle authorship.

## References
- Homayoun, S., Rezaee, N., Rezaee, Z., & Khosravian, M. (2026). *AI-Enabled Key Audit Matter Disclosures: A Hybrid LLM Approach to Enhancing Audit Report Transparency*. SSRN. https://doi.org/10.2139/ssrn.7272139
- Huang, A. H., Wang, H., & Yang, Y. (2023). FinBERT: A large language model for extracting information from financial text. *Contemporary Accounting Research*. https://doi.org/10.1111/1911-3846.12832
- Yang, Y., Uy, M. C. S., & Huang, A. (2020). FinBERT: A pretrained language model for financial communications. https://arxiv.org/abs/2006.08097
- Loughran, T., & McDonald, B. (2011). When is a liability not a liability? Textual analysis, dictionaries, and 10-Ks. *Journal of Finance*, 66(1), 35–65. https://doi.org/10.1111/j.1540-6261.2010.01625.x

**Research integrity:** This is an independently authored software extension; it makes no claim to sole authorship of the source publication, to preexisting MaRyAm1295 weights, or to new model performance.
