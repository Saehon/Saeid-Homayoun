---
title: DARWIN-AuditBERT | Dr. Saeid Homayoun
emoji: 📑
colorFrom: blue
colorTo: indigo
sdk: static
app_file: index.html
pinned: false
license: mit
short_description: CAM/KAM research topic screener (not trained)
---

# DARWIN–AuditBERT — Dr. Saeid Homayoun | Audit Intelligence Research Lab

**Hugging Face account:** [SADHON](https://huggingface.co/SADHON)  
**Independent research-software developer:** Dr. Saeid Homayoun, University of Gävle (Sweden).  
**Current deployable stage:** free-to-host interactive **static HTML/JavaScript** *keyword-based* audit-topic screening demonstration, running exclusively on public/synthetic example disclosures. **This Space does not yet contain new FinBERT or Llama 3.1 fine-tuned weights.**

The deployed static Space runs fully in the user's browser without server GPU or LLM inference. `app.py` and `topic_screening.py` in GitHub are an optional future Gradio implementation that is **not deployed** on this free static Space. This avoids the October 2026 Hugging Face policy requiring PRO for Gradio/Docker Spaces on cpu-basic.

## Research components

1. **Audit matter screening:** explainable accounting-topic vocabulary with US CAM / IFRS KAM framework references. This is a deterministic research demonstrator and does not estimate CAM effectiveness, audit quality, or risk.
2. **Future independent classifier checkpoint:** [SADHON/saeid-finbert-kam-v2](https://huggingface.co/SADHON/saeid-finbert-kam-v2) — repository **created as a private, untrained model-card staging area**, not a trained model.
3. **Future separate generator adapter:** [SADHON/saeid-llama-31-8b-kam-v2](https://huggingface.co/SADHON/saeid-llama-31-8b-kam-v2) — repository *planned/staging only*, not a trained model.
4. **Canonical source of code:** [Saehon GitHub, V2 research branch](https://github.com/Saehon/Saeid-Homayoun/pull/185); source is reviewed there, not edited directly on the Hub.
5. **Source research evidence and prior code:** retained privately in the existing Google Drive archive; no private original notebooks, licensed datasets, training corpus, access tokens or checkpoints are uploaded here.

## Prior collaborative science and attribution
The earlier collaborative working paper, [*AI-Enabled Key Audit Matter Disclosures: A Hybrid LLM Approach to Enhancing Audit Report Transparency*](https://ssrn.com/abstract=7272139), is cited as earlier work. This Space is **new independent software** and does **not** imply sole authorship of that paper or ownership of the two existing Hugging Face repositories [MaRyAm1295/finBERT-KAM](https://huggingface.co/MaRyAm1295/finBERT-KAM) and [MaRyAm1295/Llama-3.1-8B-KAM](https://huggingface.co/MaRyAm1295/Llama-3.1-8B-KAM).

## Replication and governance
This demonstration has no model performance results. For publishable V2 results, reconcile 48 versus 49 topic definitions, verify source rights, use firm-disjoint and forward-year holdouts, compare TF–IDF versus independently tuned FinBERT, and report class-level metrics and uncertainties. Response generation requires licensed training pairs, evaluation of factual grounding and independent expert review.

**Not for audit or assurance decisions.** No assertion of compliance with PCAOB, IAASB or IASB rules is made.


## Linked measured benchmark — 16 October 2026

A separately executed **private-data, TF–IDF + LinearSVC** topic-classification baseline—not the keyword-based code running in this Space—produced the following preliminary issuer-disjoint held-out scores:

| Audit corpus | Unique eligible examples | Test macro-F1 | Test accuracy | Description-only test macro-F1 |
|---|---:|---:|---:|---:|
| US CAM | 36,771 | 0.778623 | 0.867387 | 0.766761 |
| UK-headquartered KAM candidates | 33,724 | 0.756715 | 0.820740 | 0.717099 |

The UK-headquarters proxy is **not verified to be a UK auditor-reporting regime**; country label taxonomies differ, audit-report years are not validated and semantic near-duplicate leakage requires further analysis. The static interactive demo is still **a deterministic keyword screener and is not the trained TF–IDF baseline, FinBERT, or Llama**. No private raw records or trained model weights are hosted by this Space.

[Research implementation, metrics and scientific caveats](https://github.com/Saehon/Saeid-Homayoun/tree/research/saeid-auditbert-v2-20261016/research/saeid-homayoun-auditbert-v2) · [Google Drive source registry](https://docs.google.com/document/d/1YmktPLQ-be1sIFd-Ghlpvd7r156C2boC3y9eofM8p6k/edit) · [Kaggle synthetic demonstration](https://www.kaggle.com/datasets/sadhon/cam-kam-auditbert-public-demo).


## Official DARWIN–AuditBERT project identity and Gemini–Colab workflow

**Formal program name:** **DARWIN–AuditBERT — Cross-Jurisdictional Audit Intelligence, Risk and Disclosure Analytics**. **Research lead:** Dr. Saeid Homayoun, University of Gävle, Sweden. Its components are **AuditBERT–CAM** (US critical audit matters), **AuditBERT–KAM** (UK-headquartered KAM research candidates), **DARWIN–ACRIS** (future separate risk/ICFR empirical track), and **DARWIN–AuditLab** (Google Drive ↔ Colab/Gemini ↔ GitHub ↔ Hugging Face; Kaggle synthetic-only).

**Gemini in Colab:** the authoritative, safety-gated full Gemini assistant execution prompt has been saved in the [EXISTING GitHub master README](https://github.com/Saehon/Saeid-Homayoun/blob/research/saeid-auditbert-v2-20261016/research/saeid-homayoun-auditbert-v2/README.md#gemini-colab-execution-master-prompt--darwin-auditbert-v1), and also *inside* the [existing Colab training notebook](https://colab.research.google.com/github/Saehon/Saeid-Homayoun/blob/research/saeid-auditbert-v2-20261016/research/saeid-homayoun-auditbert-v2/AuditBERT_USUK_Drive_Colab.ipynb). It is intended to be pasted into built-in Colab Gemini chat, not run as Python and not used through a separately billed Gemini API. It requires user approval before training or publishing.

**Data stewardship:** the original user-provided [Claude Drive archive](https://drive.google.com/drive/folders/1NMX2_Ojg_maMyokV1j3rlt55aC3KWNV4) contains the canonical [CAMbERT202610 research data](https://drive.google.com/drive/folders/1dmmYE7GuqUM-jfrOOW3nUwERxvxQDD6m), including a separate US CAM audit-opinion date crosswalk, an existing account-domain codebook and unfilled 260-CAM human coding template. This source material remains *private*; no raw licensed CAM/KAM text or row-level vendor topics are hosted here.

**Reproducibility status as of 16 October 2026:** US and UK-headquarters proxy **CPU TF-IDF+LinearSVC** baselines have documented macro-F1 values 0.778623 and 0.756715. These scores are **NOT** from the static demo, newly trained FinBERT weights, a Llama model, or a common cross-jurisdiction label taxonomy. The full US GPU FinBERT training, UK GPU KAM FinBERT training, human expert coding, and prospective DARWIN–ACRIS regressions are **NOT EXECUTED**. UK headquarters is not independently verified UK auditor-reporting jurisdiction. The original collaborative SSRN 7272139 research and third-party model weights remain separately attributed.

**Canonical update policy:** reuse the existing GitHub branch/PR, Google Drive Doc and model/Space repository; preserve owners' original model card IDs, code history and prior manuscripts. Do not publish any new model weights, raw source disclosures, tokens, or private model scores without approved rights and validation.
