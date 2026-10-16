# DARWIN–AuditBERT | Dr. Saeid Homayoun | Independent US CAM and UK KAM Research

**Principal developer / new research extension:** Dr. Saeid Homayoun, University of Gävle (Sweden)  
**Verified execution (16 October 2026):** Two real-data **TF–IDF + LinearSVC** baselines have been trained and held-out evaluated on private Google Drive CAM/KAM source data. No independently trained FinBERT/Llama neural weights exist; no new neural accuracy is claimed. The public static Space and two private untrained neural model-card repositories remain under SADHON.

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


### Read-only first Colab step — new executable corpus preflight

**Stage: code staged; synthetic self-test only. No private CAM/KAM file was opened by GitHub CI, and no model was trained.** After the user mounts their authorized existing Drive folder in Google Colab, run this code with the actual mounted original CSV paths:

~~~bash
python research/saeid-homayoun-auditbert-v2/large_corpus_preflight.py \
  --cam "/content/drive/MyDrive/<existing-folder>/CAM.csv" \
  --kam "/content/drive/MyDrive/<existing-folder>/KAM.csv"
~~~

Optional: inspect its reported country candidate header names, then run with '--kam-country-column EXACT_HEADER_NAME' for **UK-headquarters candidates only**. Do not treat this count as verified UK audit jurisdiction.

Preflight code: [large_corpus_preflight.py](large_corpus_preflight.py). Processes selected CSV columns in chunks, preserves leading-zero issuer IDs, outputs aggregate vendor-topic counts, rows, complete-text availability, distinct opinion/issuer/matter counts, duplicate identifier/text-hash diagnostics, and source SHA-256. Does not export row-level text, train, publish, or silently invent report years. Date, country reporting standard, source-rights, and leakage approval statuses remain UNVERIFIED until independent checks. First run synthetic smoke test with '--self-test'; it is included in CI. Do not paste original dataset text into GitHub Issues or Hugging Face.



## EXECUTION LOG: actual private CAM and UK-HQ KAM CPU benchmark (16 October 2026)

The numbers below are **actual full-source TF-IDF + balanced LinearSVC topic-classification experiments**, not synthetic CI tests, not FinBERT or Llama training. Source: existing CAMbERT202610 Google Drive folder. The experiment read the real CSVs in a private temporary runtime, and only aggregate results/source hashes were recorded in the existing [Google Drive CAM-KAM research registry](https://docs.google.com/document/d/1YmktPLQ-be1sIFd-Ghlpvd7r156C2boC3y9eofM8p6k/edit). The [GitHub native source adapter](real_corpus_tfidf.py) follows the same preprocessing/splitting and classifier protocol; its CI is synthetic-only.

| Metric / count | US CAM | UK-headquartered KAM (proxy) |
|---|---:|---:|
| Raw source matter rows | 45,924 | 35,886 UK HQ from 86,122 pan-European |
| Valid rows (source IDs + topic + description >=30 characters) | 45,919 | 35,806 |
| Exact normalized text duplicate rows observed | 8,956 | 2,007 |
| Conflicting-label exact-text clusters excluded | 192 (588 affected rows) | 75 (244 affected rows) |
| Deduplicated, nonconflicting eligible texts | 36,771 | 33,724 |
| Train / validation / test matter counts | 25,774 / 5,349 / 5,648 | 23,576 / 4,960 / 5,188 |
| Issuer counts in train / validation / test | 4,637 / 994 / 994 | 1,353 / 290 / 291 |
| Topic classes with training support >=100, plus OTHER_RARE | 36 + 1 | 37 + 1 |
| Validation macro-F1 | 0.808179 | 0.733128 |
| Test macro-F1 | **0.778623** | **0.756715** |
| Test accuracy | **0.867387** | **0.820740** |
| Test weighted-F1 | 0.863112 | 0.817095 |
| Test balanced accuracy | 0.775495 | 0.762652 |
| True report-year and UK auditor-report regime verified? | NO | NO |
| Semantic near-duplicate leakage and external human annotation audit done? | NO | NO |

**Data source SHA-256**: CAM.csv = 36b964fd8946f831d55a9459f5648e2af464e14788d8a2c93ca48cd441d08d28; KAM.csv = 963b22c8377b7e7b51d962040a7d37d407d2b3ca9e3d42914f4091a4b0ff4c8a. Experimental environment: Python 3.13.5, scikit-learn 1.8.0, TF-IDF word unigrams/bigrams up to 50,000 features, sublinear TF, balanced LinearSVC, random seed 42, issuer-disjoint approximate 70/15/15. Text = TITLE + DESCRIPTION. Exact duplicate text deduplicated globally; ambiguous identical-text groups assigned multiple vendor topic labels were excluded.

**Correction of the preliminary benchmark**: Initial US macro-F1 0.792415 and UK-HQ macro-F1 0.759398 are now superseded by 0.778623 and 0.756715 respectively after stricter removal of ambiguous identical-text groups. These are INTERNAL preliminary results only. The countries have different topic taxonomies; score comparison is not causal, matched-label or publication-ready. The UK cohort is headquarters based, not verified ISA (UK) auditor reports. Original CSVs lack verified audit-report years; time-forward evaluation is blocked.

**FinBERT execution path**: [AuditBERT_USUK_Drive_Colab.ipynb](AuditBERT_USUK_Drive_Colab.ipynb) has been staged to use authenticated Google Drive and a user-selected Colab GPU. It imports the [same source-specific cleaner and issuer grouping protocol](real_corpus_tfidf.py) and the existing [FinBERT training script](train_finbert_topic.py) for independent US CAM and UK-HQ proxy models. It includes explicit stop switches for permitted private data use, old notebook token revocation and GPU authorization. No user Colab runtime was authenticated/started from this chat; hence no claim of FinBERT training.

**Model publication gate**: The existing private Hugging Face SADHON model repositories contain model cards only, not trained neural weights. Source content, older notebook credentials and proprietary labels have not been uploaded. Do not publish neural model weights or F1 until actual trained checkpoints exist and source/model redistribution rights, human validation and independent data-split leakage tests pass.


### Verified additional feature ablation: description-only against title-plus-description

Runs below used the actual private CAM.csv/KAM.csv and the **same cleaned issuer-disjoint partition, class frequency threshold, labels, and seed 42** as the corrected baseline. Cleaning and exact-text deduplication remained based on the combined TITLE+DESCRIPTION before removing the title input. Therefore additional DESCRIPTION-only exact/semantic cross-issuer leakage checks are still pending.

| Heldout feature comparison | US CAM (test n=5,648) | UK-headquartered KAM proxy (test n=5,188) |
|---|---:|---:|
| Title + description macro F1 | 0.778623 | 0.756715 |
| Description-only macro F1 | 0.766761 | 0.717099 |
| Macro F1 attributable to adding title in this paired experiment | +0.011863 | +0.039616 |
| Description-only accuracy | 0.858888 | 0.792406 |
| Description-only weighted F1 | 0.853953 | 0.788329 |

Methodological warning: **title wording carries a substantial part of predictable vendor accounting-topic information**, especially for the UK-headquarters subset. Before any FT50/editorial claim, run the title-only negative control, true audit jurisdiction/year verification, boilerplate and semantic near-duplicate checks, and human expert labels. The ablation is associative and does not establish causal improvement or demonstrate FinBERT training. It is reproduced by the new [--text-mode description_only option in the canonical real_corpus_tfidf.py](real_corpus_tfidf.py) using the same original Drive input and source verification. The detailed ablation results were appended to the same existing Google Drive research registry; no separate raw data or duplicate workbook was created.



## ADDENDUM — user-provided Claude Drive archive reviewed (16 October 2026)

**Source:** [Claude user-provided folder](https://drive.google.com/drive/folders/1NMX2_Ojg_maMyokV1j3rlt55aC3KWNV4). Its relevant existing children are [CAMbERT202610](https://drive.google.com/drive/folders/1dmmYE7GuqUM-jfrOOW3nUwERxvxQDD6m), the independent [DARWIN-ACRIS execution plan](https://docs.google.com/document/d/1SNDHIwXGo5B85h7mcuzCGlKLmkhjfcnQeVkWW5K97ro/edit), [ACRIS working manuscript](https://docs.google.com/document/d/1ska5iCKCplH0mARlTy5ZVn4v22nWp3ktAEcom90Nqt0/edit), and an unestimated prospective DARWIN CAR manuscript. Originals remain unchanged; **cross-reference, do not copy or blend model training or results**.

### Significant new data discovery: separately verified US CAM opinion dates

The [Phase 1 CAM dated-opinion table `OPINION_DATES.csv`](https://drive.google.com/file/d/1sYJEzNMfHr9DUxVun7ezrvYXEh-gsBtg/view), under [`PHASE_1_CAM/03_CAM_CLEANED_DATASET`](https://drive.google.com/drive/folders/1-P1-kETSaDn7sHMpTpKPO0qDo_7OEWIt), is **distinct from the original undated CAM.csv**. Actual connector readback found 32,859 opinion records, one per unique `AUDIT_OPINION_FKEY` subject to independent join verification:

| Reported / observed status | Opinions | Proposed handling |
|---|---:|---|
| `VERIFIED_TEXT_AND_FORM_AP` | 19,264 | Primary candidate for time-forward training and prior-to-report economic variables, subject to final source verification |
| `ALIGNED_FORM_AP_UNIQUE` | 2,635 | Date-aligned sensitivity cohort only after assessing estimated 95.8% masked-year accuracy and misclassification |
| `ALIGNED_AMBIGUOUS` | 4,263 | UNKNOWN; exclude from point-in-time treatment until reconciled |
| `UNDATED` | 6,697 | UNKNOWN; never assign a guessed reporting year |
| `date_usable=True` in the existing opinion table | **21,899** | Includes both first two groups; this is **opinion-level**, not unique CAM matter count |

The linked [Phase 1 validation report](https://drive.google.com/file/d/1sjR7rzVpK-RPk2w2O4_h1OsmY8EFkn3Y/view) lists **27,605 CAM matters** within `VERIFIED_TEXT_AND_FORM_AP`, **3,462** `ALIGNED_FORM_AP_UNIQUE`, **5,323** ambiguous and **9,534** undated. These are *matter-level* counts that must not be confused with the 32,859 opinion-level statuses. Not all verified temporal data were available in the original raw CSV; join on `AUDIT_OPINION_FKEY` and separately validate `CIK`, `report_date`, `fpe`, multi-CAM opinions, and audit-firm identity before time splitting. **The CAM.csv `FISCAL_YE` is an MMDD fiscal-year-end fragment, not YYYY; do not treat it as a year or merge on it without validated dates.** UK KAM audit years and UK auditor reporting regime remain unverified; do not transfer the US Form AP dates to UK KAM observations.

### Existing human-validation and scientific artifacts, to reuse—not regenerate

- [Phase 1 CAM topic codebook](https://drive.google.com/file/d/1UBPhRsHfcYJuPvf8oJ4Zo9l_jnCtK-BK/view) describes **13 account categories**, including `REVENUE`, `INVENTORY`, `RECEIVABLES`, `GOODWILL_IMPAIRMENT`, `INCOME_TAXES`, `LEASES`, `FINANCING_DEBT`, `PROVISIONS_CONTINGENCIES`, `PPE`, `INTANGIBLES`, `EQUITY`, `IT_CONTROLS`, and `OTHER`. It crosswalks the 55 US provider topic labels into multiple domain indicators, with automated title rules; **automated agreement is not human annotation**. Separate 59 KAM source topics and historical 49 KAM classifier labels cannot be presumed equivalent.
- [Existing human coding sample of 260 CAMs](https://drive.google.com/file/d/1b22bfuKXywhCEDUK80yEHu0Svj0Cx9vg/view) has **EMPTY independent human coder columns** per [source validation report](https://drive.google.com/file/d/1sjR7rzVpK-RPk2w2O4_h1OsmY8EFkn3Y/view); no claim of expert-validated ground truth until double-coding/adjudication and agreement scores exist.
- [Existing CAM text measure codebook](https://drive.google.com/file/d/1A48fxemJxIQJQMMUf3_MIqYhwYyV7dqc/view) and [CAM_TEXT_MEASURES.csv](https://drive.google.com/file/d/1f5p9PcwwYywDnMC17Nnx-PONyCEHxxdE/view) already cover response procedures, standards/numbers, domain boilerplate, novelty and readability; use the existing measurements, without claiming audit effectiveness from their mere values. Source report gives 45,924 measured CAM records and `novelty_vs_prior_year` on 18,267 CAMs.
- [Existing independent DARWIN V9 RISK-INDEX provenance code](https://github.com/Saehon/RISK-INDEX/blob/main/replication_code/DARWIN_V9_source_provenance.py) and [Colab research notebook](https://github.com/Saehon/RISK-INDEX/blob/main/notebooks/DARWIN_V9_TAR_FinBERT_Colab.ipynb) can be cross-referenced for **economic/ICFR analysis later**; no need to duplicate that notebook or imply its manuscript outcomes were re-estimated.

### Revised Google Colab research execution (CAM → UK KAM → optional risk/ICFR)

1. **G0 security and rights:** original KAM notebooks contain historical HF token strings; verify all revoked/rotated. Do not upload licensed raw records to public Kaggle or public Spaces. Keep authenticated Google Drive canonical and isolate scratch data in Colab runtime.
2. **G1 frozen baseline:** preserve completed US CAM and UK-HQ KAM TF-IDF result protocol and previously measured scores, with issuer-disjoint splits and global duplicate/conflicting-label removal. Do not revise test sets after reviewing test performance.
3. **G2 dates + labels:** create read-only aggregate preflight of original `OPINION_DATES.csv` and validate one-to-many CAM/opinion joins; support a *separate* US temporal holdout limited primarily to `VERIFIED_TEXT_AND_FORM_AP` (sensitivity for `ALIGNED_FORM_AP_UNIQUE`), without pretending the raw CAM.csv or KAM.csv has report-year fields. Benchmark 55 vendor source classes separately from the expert-reviewed 13 multi-label account categories.
4. **G3 GPU/FinBERT:** independent US CAM classifier first, UK-HQ KAM next, each against the same **within-cohort** TF-IDF and pretrained FinBERT comparators. Add title-only and description-only negatives, near-verbatim/boilerplate challenge sets and issuer-level uncertainty. Log hardware, seed, Hugging Face base revision and no-raw-text outputs. GPU is **not launched by merely opening notebooks**.
5. **G4 expert validation:** fill existing 260 human CAM coder slots with two genuinely independent auditors and adjudication. Keep UNKNOWN/MIXED/ENTITY and multi-topic assignments. Then evaluate model validity beyond vendor labels; do not claim the existing empty coding sample is a gold set.
6. **G5 OPTIONAL FT50 economic separate track, not part of FinBERT training:** after owner authorization, run [DARWIN-ACRIS](https://docs.google.com/document/d/1SNDHIwXGo5B85h7mcuzCGlKLmkhjfcnQeVkWW5K97ro/edit) with independent pre-report-date account risk, auditor RESPONSE specificity (not CAM title labels), and future account-matched ICFR. Verified ICFR categories **effective/ineffective/unknown × industry × accounting/control domain**; US revenue uses ASC 606, IFRS 15 only where applicable to IFRS reporters. Separate CAM occurrence/selection from content, and account risk from text-derived apparent risk. Audit manuscript novelty and overlap with existing MS/AJPT/CAR work. Existing ACRIS H1-H3 are *planned, not newly estimated*.
7. **G6 minimal-file reproducibility:** keep this canonical GitHub README/Colab notebook, the existing private Google Drive research registry and any preexisting tracking workbook; add tabs to the existing workbook when suitable. No source copies or orphan spreadsheets. Distinguish `SOURCE_REPORTED` vs `EXECUTED` vs `BLOCKED` vs `PENDING`; retain nulls and unknowns and preserve author credit for the prior collaborative KAM paper.

**Decision:** The linked Claude folder **materially improves** the training and publication plan because it reveals a date crosswalk, existing account-topic domain codebook, nonhuman validation blocker, auditor response measures and nonredundant ACRIS replication assets. It does *not* justify saying the planned FinBERT neural GPU training or econometric regressions have already been run.

## OFFICIAL PROJECT IDENTITY — DARWIN–AuditBERT

**Full title:** DARWIN–AuditBERT — Cross-Jurisdictional Audit Intelligence, Risk and Disclosure Analytics.  
**Research lead:** Dr. Saeid Homayoun, University of Gävle, Sweden.  
**Repository identifier (suggested alias, not a new repository):** `darwin-auditbert-usuk`.  
**Program architecture:** AuditBERT–CAM (US critical audit matters) → AuditBERT–KAM (UK-headquartered KAM research candidates) → DARWIN–ACRIS (separate, optional account-risk and ICFR economics research) → DARWIN–AuditLab (Google Drive ↔ Colab/Gemini ↔ GitHub ↔ Hugging Face; Kaggle synthetic-only).  
**Project storage policy:** Keep existing canonical Drive files and the existing research branch; do not rename or fork the repository or copy licensed source data to public services. The original collaborative KAM paper and third-party model ownership remain attributed to their authors.  
**Model status:** Real TF-IDF + LinearSVC baselines previously executed; **NO newly trained neural FinBERT or Llama model weights** until authenticated GPU runs and independent verification.

## GEMINI COLAB EXECUTION MASTER PROMPT — DARWIN-AuditBERT V1

**Use:** Open [the existing Colab notebook](https://colab.research.google.com/github/Saehon/Saeid-Homayoun/blob/research/saeid-auditbert-v2-20261016/research/saeid-homayoun-auditbert-v2/AuditBERT_USUK_Drive_Colab.ipynb), click the built-in **Gemini spark icon** in the Colab footer, and paste the following into the Colab Gemini chat. It is an AI-assistant instruction, **not executable Python** and **does not require a Gemini API key** in the built-in Colab chat. Do not paste it into a Python code cell.

```text
You are Gemini, the coding and data-science assistant inside my authenticated Google Colab notebook. Act as the DARWIN–AuditBERT scientific engineering co-pilot for Dr. Saeid Homayoun (University of Gävle). Project full title: Cross-Jurisdictional Audit Intelligence, Risk and Disclosure Analytics. Preferred GitHub identifier: darwin-auditbert-usuk, but DO NOT create or rename any repository or folder. Reuse the existing project.

MY AUTHORITATIVE PROJECT LOCATIONS
- GitHub source branch: https://github.com/Saehon/Saeid-Homayoun/tree/research/saeid-auditbert-v2-20261016/research/saeid-homayoun-auditbert-v2
- The notebook currently open is AuditBERT_USUK_Drive_Colab.ipynb on that branch. Existing PR: https://github.com/Saehon/Saeid-Homayoun/pull/185
- Private Google Drive original-source root: https://drive.google.com/drive/folders/1NMX2_Ojg_maMyokV1j3rlt55aC3KWNV4 (Claude folder), with existing CAMbERT202610 folder ID 1dmmYE7GuqUM-jfrOOW3nUwERxvxQDD6m. Identify the REAL mounted path after I authorize Drive. Try MyDrive/Claude/CAMbERT202610 and MyDrive/CAMbERT202610; do not fabricate a file path or copy the corpus to public locations.
- Existing research registry, UPDATE IN PLACE: https://docs.google.com/document/d/1YmktPLQ-be1sIFd-Ghlpvd7r156C2boC3y9eofM8p6k/edit
- Private original US CAM.csv Drive ID 1O0XqTgVCJHcQnjQ5Jkg2_IumY8k1JLhd; private pan-European KAM.csv ID 1Izr6_ymOJbFUFgAmV-oUw5k9C15tqBWZ.
- Separate dated US audit-opinion lookup OPINION_DATES.csv ID 1sYJEzNMfHr9DUxVun7ezrvYXEh-gsBtg, under PHASE_1_CAM/03_CAM_CLEANED_DATASET. Historical KAM notebooks under KAMBERT2026 are REFERENCE ONLY and contain previously exposed Hugging Face tokens.
- Hugging Face owner SADHON: existing PRIVATE untrained model-card repos SADHON/saeid-finbert-kam-v2 and SADHON/saeid-llama-31-8b-kam-v2; public keyword-only static Space SADHON/dr-saeid-homayoun-auditbert-v2. Do NOT publish weights/source text or pretend trained models exist.
- Kaggle existing synthetic-only dataset sadhon/cam-kam-auditbert-public-demo, NOT the private research corpus.

SCIENTIFIC SCOPE AND VALIDATED STARTING NUMBERS
- US CAM: 45,924 source matters, 55 provider topic labels, 32,859 audit opinions. Existing TF-IDF + LinearSVC issuer-disjoint baseline cleaned 36,771 unique eligible texts, test n=5,648, macro-F1=0.778623 and accuracy=0.867387; description-only macro-F1=0.766761.
- KAM.csv is EUROPE-WIDE (86,122 matters, 59 provider topics), not UK-only. 35,886 are UK-HEADQUARTERED candidate matters; cleaned UK-HQ corpus previously 33,724 unique texts, test n=5,188, macro-F1=0.756715 and accuracy=0.820740; description-only macro-F1=0.717099. UK headquarters is NOT a verified UK ISA audit-reporting jurisdiction.
- The two TF-IDF results were already computed in an earlier CPU run. Identify them as prior EXECUTED baseline results, not a fresh Colab reproduction and not FinBERT scores. Country label spaces differ; no unadjusted cross-country ranking.
- Original CAM.csv FISCAL_YE is MMDD, not YYYY. Original large CAM/KAM CSVs do NOT contain verified report years. A separate US OPINION_DATES.csv has 32,859 OPINION rows: 19,264 VERIFIED_TEXT_AND_FORM_AP; 2,635 ALIGNED_FORM_AP_UNIQUE; 4,263 ALIGNED_AMBIGUOUS; 6,697 UNDATED. date_usable True for 21,899 opinions. A verified report-year CAM matter cohort requires a many-to-one join by AUDIT_OPINION_FKEY and independent issuer/report-date checks. Never impute dates to UNKNOWN; UK reporting year is still unresolved.
- Existing 13-domain CAM topic codebook: under PHASE_1_CAM/04_CAM_TOPIC_CLASSIFICATION/CAM_TOPIC_CODEBOOK.md. The human double-coding candidate sample has 260 CAMs, but coder fields are EMPTY. Never label automated two-method agreement as human validation.
- The separate DARWIN–ACRIS project is an OPTIONAL later accounting-risk/ICFR research track, not FinBERT benchmark data. Before merging ICFR, verify effective/ineffective/unknown × industry × accounting/control domain; US revenue ASC 606 and IFRS 15 only for actual IFRS reporters. Never treat CAM absence as audit failure or observed CAM wording as independent pre-CAM risk.

REQUIRED CONTROLLED WORKFLOW
STEP 0 — FIRST RESPOND WITH a concise execution plan, current notebook/code audit, risk/permission checks, actual Drive path inventory, and an explicit RUN/STOP table. Do not change source files or turn training switches True without my explicit approval. Use Colab's built-in Gemini assistant; do NOT demand or silently generate a separate GEMINI_API_KEY or paid Gemini API call. Acknowledge that Gemini can propose notebook edits, but training itself runs on the Colab Python runtime.
STEP 1 — After I authorize Drive, verify the EXACT originals, sizes, SHA-256 if feasible, required raw columns and dataset provenance. Use issuer/opinion IDs as STRING to preserve leading zeroes, validate nulls, unique keys and duplicate/opinion fanout. Prevent selecting similarly named archive copies. Print only aggregate summaries; never disclose licensed narrative examples in chat, logs, GitHub, Hugging Face or Kaggle.
STEP 2 — Run strictly read-only baseline/preflight and unit tests first. Identify existing Python/Transformers/torch/CUDA and GPU memory; report whether free GPU exists. Inspect the current notebook and train_finbert_topic.py CLI for compatibility, bugs and dataset leakage. Propose minimal in-place patches and review before applying. No silent changes to original archived scripts.
STEP 3 — Freeze grouped train/validation/test splits using issuer/company groups, exact normalized-text globally deduplicated, conflicting identical-text topics excluded, with NO issuer overlap. Check near-verbatim cross-issuer boilerplate and group/opinion leakage. Report title-only and DESCRIPTION-only ablations and tokenizer truncation. Never learn rare class membership from held-out labels. Save reproducible RANDOM_SEED, configs and pseudonymous/hashes-only split manifests. Time-forward US evaluation must be a separate cohort from the original issuer holdout and only from independently verified opinion-year matches.
STEP 4 — Produce a small user-approved ~2,000-record US CAM FinBERT pilot with checkpoint saving to the existing PRIVATE Drive project folder; use existing base checkpoint yiyanghkust/finbert-tone and its verified revision/licensing. If source-use rights, token revocation, Drive authorization or GPU availability are not approved/verified, STOP here and report BLOCKED. Do not guess that a credential has been revoked. For pilot outputs distinguish pilot validation from held-out final testing.
STEP 5 — Only after my explicit approval and a successful pilot, train the independent full US CAM FinBERT model on the frozen clean split. Compare against the exact same issuer-disjoint TF-IDF baseline. Evaluate macro-F1, weighted-F1, accuracy, balanced accuracy, per-class precision/recall/F1, error cases, and issuer-bootstrap uncertainty. Then train a SEPARATE UK-HQ KAM FinBERT on its own 59-topic-source taxonomy/appropriate rare-label mapping, flagged UK-HQ proxy (NOT UK auditor regime). Preserve minority and OTHER_RARE/UNKNOWN labels. Do not call historical KAM-BERT's 49-class benchmark an identical test.
STEP 6 — Confirm all outputs from real executed runs before stating PASS: inspect saved checkpoints, their label maps, per-cohort metrics JSON, test sample counts, source hashes, software/library versions, GPU type, seed, experiment split mode, rights status, provenance and zero-leakage checks. Never invent F1, p-values, journal contributions or completion. Report SOURCE_REPORTED / EXECUTED / BLOCKED / PENDING separately. Any failure: maximum TWO attempts, then add an OPEN REPAIR QUEUE note and continue safe independent checks.
STEP 7 — Save results ONLY to existing canonical private Google Drive project assets, extending the existing tracker workbook by worksheet/tab when appropriate; version source code in the SAME GitHub PR branch; save model weights privately in Drive until redistribution rights and independent validation pass. For GitHub/HF/Kaggle share only source code, sanitized configurations, aggregate results and synthetic examples after my explicit approval. NEVER upload original CAM.csv, KAM.csv, personal identifiers, licensed disclosure text, notebooks with legacy HF tokens, unreleased manuscripts, API tokens, training checkpoints or proprietary row-level topic labels to public repos.
STEP 8 — Research track order: (A) US CAM topic model; (B) independent UK KAM topic model; (C) separate DARWIN–ACRIS/account-level CAM response specificity × independently timed risk × future ICFR only after I authorize the separate economics phase. Preserve alternative and null outcomes; avoid duplicate FT50 submissions and retain prior collaborative KAM paper/third-party model attribution (SSRN 7272139).

OUTPUT FORMAT I REQUIRE: (1) current gate/status matrix; (2) minimal code changes proposed; (3) source hashes/counts/schema and provenance confidence; (4) reproducible execution record after an actual run; (5) frozen within-cohort baseline-versus-FinBERT result tables and ablations; (6) failures/open repair queue; (7) exact existing Drive/GitHub/HF/Kaggle destination links and verified readbacks. If you cannot access authenticated resources, show the exact permission obstacle and pause—do not fabricate a result. Start NOW with STEP 0, inspect the notebook and mounted files actually accessible, and ask for my approval BEFORE any new training or file modification.
```

**No new GPU experiment was run by recording this master prompt.** The approved pilot and full-sample checkpoints remain future actions.


## Engineering completion sprint — frozen FinBERT training and guarded private Hugging Face release

**Research owner:** Dr. Saeid Homayoun. **Status:** CODE + SYNTHETIC CI VALIDATED; US CAM and UK-HQ KAM neural GPU jobs **NOT YET RUN**. Original TF-IDF+LinearSVC scores (US macro-F1 0.778623; UK-HQ proxy 0.756715) remain historical reference benchmarks, NOT new model F1. The source [Claude Drive folder](https://drive.google.com/drive/folders/1NMX2_Ojg_maMyokV1j3rlt55aC3KWNV4) and current project registry remain authoritative and private.

### Fixed research-critical training defect

The original Colab notebook created issuer-disjoint train/validation/test assignments but called `train_finbert_topic.py --split company`, **re-partitioning** the cleaned data. The corrected notebook writes the explicit `split` column to ephemeral private temporary CSV, then invokes `--split frozen`. [Updated training CLI](train_finbert_topic.py) checks issuer separation, rejects exact-title+description cross-split duplicates, preserves zero-padded issuer IDs with `dtype=string`, preserves empty titles when description exists, and fails on unseen validation/test class labels rather than silently remapping. All completed heldout TF-IDF comparisons remain the previous historical results pending actual fresh same-split reproduction.

### Compute discipline: pilot → full independently trained US CAM → full independent UK KAM → optional expert/ACRIS

- **Default notebook flags all FALSE:** `RUN_GPU_FINBERT`, `RUN_FULL_AFTER_PILOT`, `EVALUATE_FINAL_HELDOUT`, and `RUN_HF_PRIVATE_UPLOAD`. Legal rights and old credential revocation flags also remain FALSE. Opening Colab or copying the Gemini prompt never trains or publishes by itself.
- **First user-approved GPU trial:** `RUN_GPU_FINBERT=True`, with source-use/secret-remediation attestations independently verified, triggers a **2,000-training-example US CAM pilot** only. It trains on frozen issuer split and evaluates **validation only**, saving a separate checkpoint in the existing private Drive folder. No unsealed test score or claims of a complete model.
- **After pilot review:** `RUN_FULL_AFTER_PILOT=True` runs the fully eligible US CAM and separate UK-HQ KAM candidate models on their own frozen partitions, still **validation only** unless `EVALUATE_FINAL_HELDOUT=True` is deliberately approved. Never treat UK headquarters as actual UK ISA auditor-report jurisdiction or compare different label taxonomies directly.
- **Hugging Face release:** [`publish_private_checkpoint.py`](publish_private_checkpoint.py) supports `--self-test` and a **local DRY RUN by default**; it refuses pilots, missing real heldout evaluation evidence, non-frozen splits, unauthorized weights, unexpected checkpoint files, wrong account, or public repo. The owner must separately authorize derived-weight redistribution and transfer to a PRIVATE repository, supplying a secret via Colab Secrets. A private upload is not automatic after training. The standalone [US CAM private card](https://huggingface.co/SADHON/saeid-finbert-cam-v2) and existing [UK KAM private card](https://huggingface.co/SADHON/saeid-finbert-kam-v2) are distinct **UNTRAINED PLACEHOLDERS** until a verified private upload.

### Exact links and commands

[Open current Colab with built-in Gemini master prompt](https://colab.research.google.com/github/Saehon/Saeid-Homayoun/blob/research/saeid-auditbert-v2-20261016/research/saeid-homayoun-auditbert-v2/AuditBERT_USUK_Drive_Colab.ipynb).

For source-safe synthetic-only local CI:

```bash
python research/saeid-homayoun-auditbert-v2/real_corpus_tfidf.py --self-test
python research/saeid-homayoun-auditbert-v2/publish_private_checkpoint.py --self-test
```

For an owner-approved **post-training, local-only dry run** of a verified US CAM FULL final checkpoint saved in private Drive (replace placeholder with ACTUAL authorized Drive mounted path):

```bash
python research/saeid-homayoun-auditbert-v2/publish_private_checkpoint.py \
  --checkpoint /content/drive/MyDrive/Claude/CAMbERT202610/private_auditbert_v2_checkpoints/us_cam/full \
  --cohort us_cam
```

This **does not upload anything**. Flags `--rights-attested --approve-private-upload` are deliberately absent and must never be auto-added by CI or Gemini. Existing GitHub Actions publish sanitized *MODEL CARDS ONLY*, not trained model weights.

### Acceptance gates — do not mark the project complete until each has observed evidence

(1) owner confirms private-source use and revokes 6 legacy HF tokens; (2) original CAM/KAM source identity and permissions verified; (3) source/report-date and UK jurisdiction caveats reflected in sample/labels; (4) frozen issuer-disjoint train/validation/test and near-duplicate checks; (5) genuine Colab GPU pilot with saved model/config/report readback; (6) separate full FinBERT runs and sealed test comparisons against same-split TF-IDF baselines; (7) class-level error and expert review of existing 260 unfilled CAM coder fields; (8) model/data license verification before private HF checkpoint publication, if desired; (9) in-place private Drive research registry update; (10) independent economics/FT50 overlap checks before the optional DARWIN–ACRIS stage. Nulls, blockers and status must be documented; no invented tests, model weights or GPU usage.
