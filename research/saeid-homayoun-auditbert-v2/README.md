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


---

## MASTER TRAINING PLAN — AuditBERT-USUK-DARWIN V1 (16 October 2026)

**Status: PLANNED, NOT TRAINED.** This plan is grounded in the verified 12–13 October 2026 data-quality report in the user's existing CAMbERT202610 Google Drive archive. Developer branding: **Dr. Saeid Homayoun**; keep earlier collaborative SSRN authorship and MaRyAm1295 checkpoints separately attributed.

### A. Actual existing source evidence, not estimated samples

Main archive: https://drive.google.com/drive/folders/1dmmYE7GuqUM-jfrOOW3nUwERxvxQDD6m

Dated data audit: https://drive.google.com/file/d/1sxaoy-3jzZN3pyEwv74ha6Oxz9gegowt/view

Canonical asset inventory: https://drive.google.com/file/d/1FzQTrZVcrKiHJUuU7O4nFwas82CMlJM5/view

| Canonical Drive file | Source-verified inventory | Role and critical restriction |
|---|---|---|
| [CAM.csv](https://drive.google.com/file/d/1O0XqTgVCJHcQnjQ5Jkg2_IumY8k1JLhd/view) | US CAM: 45,924 matter records, 262 fields, 6,671 companies, 32,859 audit opinions, 55 TOPIC_NAME categories; 45,920 nonempty descriptions | Train US model after authorized data-use check, issuer split, report-year verification |
| [KAM.csv](https://drive.google.com/file/d/1Izr6_ymOJbFUFgAmV-oUw5k9C15tqBWZ/view) | EUROPE-WIDE KAM: 86,122 matters, 76 fields, 5,520 entities, 35,567 opinions, 59 TOPIC values; 86,070 nonempty descriptions; 35,886 matters from UK-headquartered companies | Strict UK cohort must be verified by actual auditing/reporting jurisdiction; other Europe reserved for external tests |
| [kam (uk)2023.xlsx](https://docs.google.com/spreadsheets/d/1cfsb0x_pVllTh4cFIa0TCEBgOI34XLLb/edit) | UK-focused workbook 28,826 rows, 28,764 keyed matters overlap with KAM.csv | Source triangulation only: never blindly concatenate |
| [KAM20240505.csv](https://drive.google.com/file/d/1-ImPDxzWbFPzpup4yM7g9KpzlE3Z0ZxJ/view) | Original paper file exactly 65,535 matters; 49 topics / 65,192 rows after paper's >=100-frequency filter | Reproduce historical KAMBERT before improvement, NOT an independent new sample |
| [KAM-Paper-Code.zip](https://drive.google.com/file/d/1cqb2wNWyEn0DJJYCJnCaLN8b-kZxPpO3/view) | Seven original FinBERT, FinText, Llama classification/generation notebooks | Compare methods, respect coauthors; unsanitized notebooks contain six distinct embedded HF-token strings in multiple copies, so they must not be exported or executed with those credentials |

Combined CAM plus Europe-wide KAM matter rows = 132,046 before filtering, de-duplication, and validation. **Never call all 86,122 KAMs UK KAMs.** The UK-headquarters count is 35,886, not a verified audit-regime classification. The 2020–2024 US dated research subset of 16,171 CAMs / 11,988 audit opinions is independent auxiliary evidence; its date-based selection is biased toward firms with recognizable report-year text. Do not silently substitute it for all CAMs.

### B. Hard scientific gates: halt training if failed

**G0 Rights/security.** Confirm rights to the underlying public audit disclosures, private vendor-formatted extracts, vendor-assigned topic labels, derived weights, and intended outputs. Public annual-report accessibility does not automatically settle licensed extraction and model release terms. Audit/revoke the **six original HF tokens** before any notebook reuse, and never put notebook outputs/secrets in GitHub, Colab shared links, Hugging Face or Kaggle. Record credential remediation without storing credential values.

**G1 Exact time and opinion-link keys.** CAM.csv and KAM.csv have NO verified original audit-report year, date or signature-date column. Do not use MR_FILE_DATE, FISCAL_YE, FISCAL_YEAR_END, market-cap snapshot date or latest fees as audit report date. Secure the audit-opinion table, join on AUDIT_OPINION_FKEY, verify US SEC EDGAR and corresponding UK report/date. Record unmatched and conflicting keys. **Do not run or advertise forward-time holdouts before this gate passes.** Preserve issuer-company crosswalk with zero-padded US CIK; UK ENTITY_MAP_FKEY, CAM COMPANY_FKEY, and audit matter unique keys need stable type-safe handling.

**G2 UK versus US country/regime.** US_CAM requires true PCAOB/US audited CAM text. UK_KAM requires true UK audit-report regime (ISA (UK) 701 as applicable) and a verified company/auditor report, not an HQ-country-only proxy. Log UK headquarters, filing venue, auditor location, consolidated reporting framework (IFRS versus UK GAAP) and report year independently with UNKNOWN permitted. IFRS 15 must be applied ONLY if IFRS reporting is verified; US ASC 606 for relevant US GAAP revenue cases.

**G3 Deduplication and leakage.** Keep one record per authoritative CAM key CRITICAL_AUDIT_MATTER_KEY or KAM key AO_KEY_AUDIT_MATTER_KEY. Use the opinion FKEY to identify reissues and keep report versions distinct until reviewed. Check exact normalized-text SHA-256 and near-verbatim MinHash/embedding clusters over titles, descriptions and auditor responses. Exclude duplicated UK workbook items and archival ZIP copies. Split by stable issuer/corporate group and audit opinion, not random individual matter. Zero overlaps by issuer/matter/opinion and no unresolved exact/near-text leakage in final partitions.

**G4 Distinct source taxonomies.** US has 55 vendor CAM topic labels; Europe has 59 KAM labels. The historical KAMBERT fine-tuning code trains 49 KAM labels after dropping support below 100; the prior paper's abstract states 48 inconsistently. Create versioned (a) raw-US55, (b) raw-UK labels with documented rare class/OTHER logic, (c) human-adjudicated harmonized high-level accounting domains. Do not call identical topic names equivalent without review. Explicit UNKNOWN; CAM/ICFR effectiveness never inferred from presence/absence.

**G5 Human-gold annotations.** Double-code stratified samples by country, industry, opinion year, auditor, long narratives and rare labels. Independently adjudicate disagreement; report Cohen kappa or Krippendorff alpha and label-confidence coverage. Freeze dictionary mapping, quality rules and heldout split IDs before experimenting.

### C. Recommended model architecture: train in scientifically meaningful stages

**Model 1 — AuditBERT-US-CAM-v1:** independently fine-tune FinBERT-based encoder for US CAM topic classification (native 55 labels with explicit rare-label protocol), then harmonized accounting domains. Use matter TITLE + DESCRIPTION, no response as a default feature, because RESPONSE belongs to a distinct generation/response-content task.

**Model 2 — KAMBERT-UK-KAM-v1:** independently fine-tune same base encoder on verified UK KAM-only labels; compare raw 59-taxonomy with frozen 49-label historical reproduction and rare-class protocol. Retain omitted rare-topic support in all inventory reports, not silently discard the records.

**Model 3 — AuditBERT-USUK-Joint-v1:** shared encoder with explicit jurisdiction embedding/marker and jurisdiction-specific 55/59 fine-label heads or adapters, plus an adjudicated harmonized domain head. Compare pooled versus separate training on *identical, frozen group-disjoint splits*. Keep unverified European KAMs in external testing, never opportunistically leak them into joint training.

**Model 4 — Optional AuditBERT-DAPT:** additional masked-language-model adaptation using only authorized training-partition texts (never future test corpus in a prospective temporal analysis). Use fixed wordpiece windows (suggest 384 tokens, overlap logged) and aggregate chunk predictions at full-matter level. BERT training FROM SCRATCH is not the default: established FinBERT fine-tuning is much more defensible and economical on these data. Continue domain adaptation only if it beats directly fine-tuned FinBERT out of sample.

**Separate optional Model 5 — AuditLlama-USUK-response (8B QLoRA):** only with verified, permitted auditor-response pairs, gated source retrieval, and independent audit-expert assessment. Do not equate generator BERTScore with classifier macro-F1 or assume generated output is an audit opinion. Meta Llama terms, GPUs, hallucination audit and dataset rights must be checked.

### D. Locked comparisons and tests

| E | Frozen comparison | Required outcomes |
|---|---|---|
| E0 | KAMBERT paper's 65,535/49-class replication versus cleaned full KAM input | Explicit truncation bias, company distribution, differences in text and methodology |
| E1 | US TF-IDF + LinearSVC against US FinBERT | issuer-group macro-F1, weighted F1, class precision/recall/support, balanced accuracy |
| E2 | UK TF-IDF + LinearSVC against UK FinBERT | same metrics; rare UK categories and calibration |
| E3 | Separate US/UK encoders versus joint shared encoder | US, UK, pooled, and jurisdiction performance gaps, not only overall mean |
| E4 | Verified dated forward-year split (after G1) | prospective heldout scores, issuer/near-duplicate leakage checks |
| E5 | Non-UK continental European KAM holdout | out-of-jurisdiction transfer and OOD abstention |
| E6 | 256/512 tokens versus hierarchical long-text chunks | truncation share, token costs, speed, error types |
| E7 | Optional Llama responses: prompt only/RAG versus trained adapter | grounded audit procedure fidelity, unsupported claims, expert ratings, BERTScore |

Use validation for model selection; seal test labels/sets. Report at least 3 seeds where feasible, per-topic supports, class and country calibration (ECE and Brier for probability models), clustered bootstrap 95% confidence intervals at issuer, and errors by industry, auditor, issuer size and report year. No target F1 improvement or FT50 statistical significance can be assumed before actual runs.

### E. DARWIN scientific-coordinator protocol

**Discover** — read original source manifests and schema, reconstruct dates and UK reporting regime; read actual labels and text lengths; reconcile sources, counts and duplicated ZIP assets.

**Adversarial reviewer** — challenge each assumption: Is the UK cohort real? Is year valid? Could the model memorize boilerplate? Are response texts leaking topic? Are previous-paper labels attributable and rights-cleared? Does apparent accuracy persist with issuer isolation, date holdout and rare classes?

**Reconcile** — freeze approved taxonomy, gold sample, split ID hashes, sources, training flags and reproducible Git commit; every failed gate enters existing OPEN REPAIR QUEUE after two attempts, with **no false PASS**.

**Validate** — multiple independent baselines, leakage and sensitivity ablations, honest null or negative findings, external-country holdout and review by domain experts before publication/model release. No invented scores.

### F. Sustainable Google Drive × GitHub × GPT execution

**Drive = authoritative originals.** Do not create copies of CAM.csv/KAM.csv and other archives. Maintain the same Drive research registry and use any existing canonical experiment workbook with these *additional tabs*, as needed: SOURCE_MANIFEST, UK_COHORT, OPINION_YEAR_JOIN, TOPIC_ONTOLOGY, SPLITS, RUNS, EVALUATION, ERROR_AUDIT, RELEASE_GATES. Only generate temporary private normalized data inside a mounted Colab runtime for authorized compute. Save model checkpoints in the existing project folder rather than proliferating workbooks.

**GitHub = reusable source, not data.** Extend and repair the existing V2 train_finbert_topic.py and benchmark_tfidf.py on PR #185; add source-specific schema adapters, company/entity split guard, UK reporting-regime verification gates, duplicate checks, combined-domain multihead models and smoke tests only when needed. Keep historical collaborative notebooks private until token sanitation and authorship review. GitHub Actions runs synthetic-only unit tests, no private dataset or token logging.

**Colab = user-authenticated compute.** Sign in and mount the verified Google Drive folder. First run only schema inventory/rights/gates. Run matched CPU TF-IDF baselines, then 1k–5k eligible matter FinBERT pilot, then full US and UK separately, then joint and optional DAPT if GPU availability allows. Resume checkpoints safely with existing canonical project paths. Free-tier GPU availability is not guaranteed. Hosted Colab notebook must not save credential content or licensed extracts to open notebook outputs.

**Hugging Face = deployment layer.** Account SADHON already has the private untrained model-card repositories:
- https://huggingface.co/SADHON/saeid-finbert-kam-v2
- https://huggingface.co/SADHON/saeid-llama-31-8b-kam-v2
and a public, clearly labeled STATIC keyword research demo: https://huggingface.co/spaces/SADHON/dr-saeid-homayoun-auditbert-v2 .
Release actual weights only after training, data-rights and independent evaluation gates. Existing static free Space is not an inference endpoint.

**ChatGPT = scientific planner and quality critic, not background trainer.** It can maintain schema/config/code, cross-examine assumptions, inspect readbacks, write results to existing Drive research registry and review GitHub PRs. User-authorized Colab runtime executes compute; chat alone does not mount a private Google Drive dataset into a GPU.

**Actionable go/no-go sequence:**
0. Revoke/rotate old HF tokens and confirm source/data-use rights (BLOCKING).
1. Profile real CAM/KAM schemas, checksums, text and UK country markers with read-only Colab.
2. Recover/report year with opinion-key join and validate UK auditor-report regime (temporal evaluation BLOCKED until verified).
3. Deduplicate, map native and harmonized topics, double-code human gold, freeze issuer split hashes.
4. Estimate E1/E2 TF-IDF models. Record real outcomes, no prewritten significance.
5. Run 1k–5k pilot and scale full eligible CAM/UK KAM FinBERT; freeze untouched heldout set.
6. Evaluate joint encoder, optional DAPT, Europe OOD; optional separate QLoRA generation only after gated evaluation.
7. Publish rights-cleared checkpoint to existing private HF account, write verified metrics and model card, and review manuscript relevance.

**Evidence standard:** Actual trained counts and scores depend on schema/readback and authorized Colab execution; all new artifacts must link back to original Drive sources, and no training or model improvement is claimed in advance.
