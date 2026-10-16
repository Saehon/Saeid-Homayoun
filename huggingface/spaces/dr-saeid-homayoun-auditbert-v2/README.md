---
title: Dr. Saeid Homayoun | AuditBERT CAM-KAM Lab
emoji: 📑
colorFrom: blue
colorTo: indigo
sdk: static
app_file: index.html
pinned: false
license: mit
short_description: CAM/KAM research topic screener (not trained)
---

# Dr. Saeid Homayoun — AuditBERT CAM–KAM Research Lab

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
