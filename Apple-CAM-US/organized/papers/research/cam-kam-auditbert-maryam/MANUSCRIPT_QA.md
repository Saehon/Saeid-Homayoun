# Manuscript QA — Items to Reconcile Before Submission

This file records internal consistency issues identified in the revised manuscript supplied by Maryam Khosravian. It does not change the manuscript; it flags items that should be reconciled by the authors.

## 1. Topic count

- Abstract: **48 distinct accounting topics**
- Dataset/methodology: **49 distinct accounting topics**

Choose one taxonomy count and use it consistently in the abstract, methodology, tables, confusion matrix, label encoder, and model configuration.

## 2. Raw versus cleaned sample

The methodology describes:
- **65,535** raw CAM/KAM entries
- **65,192** observations after cleaning
- **4,208** public companies
- coverage from **2012–2024**

The abstract should make clear whether 65,192 is the final analytical sample rather than presenting it as the unqualified total dataset size.

## 3. Classifier versus generator F1

The manuscript reports different F1 measures for different tasks:

**Topic classifier**
- Macro F1: **83.20%**
- Weighted F1: **88.92%**

**Response generator**
- BERTScore F1: **83.95%**

The abstract currently uses 83.95% in wording that can be read as a topic-classification result. Separate the two tasks explicitly.

## 4. Model naming

The manuscript uses “AuditBERT” both as:
1. a topic-classification framework based on FinBERT/BERT, and
2. a broader hybrid framework that also includes LLaMA 3.1 response generation.

Define the unit of analysis clearly. A useful convention would be:
- **AuditBERT-Classifier** for the FinBERT-based classifier.
- **AuditBERT-Generator** or **KAM-LLaMA** for response generation.
- **AuditBERT Framework** for the integrated system.

## 5. Existing Hugging Face repositories

The manuscript identifies:
- `MaRyAm1295/finBERT-KAM`
- `MaRyAm1295/Llama-3.1-8B-KAM`

These repositories have been verified as existing Hugging Face model repositories. Their model cards should be aligned with the final paper's sample definition, topic taxonomy, training split, hyperparameters, evaluation tables, authorship, license, and citation.

## 6. Data-source wording

The manuscript describes a dual-source design involving U.S. SEC/EDGAR material and European Audit Analytics data. Public replication materials should distinguish:
- source-traceable public SEC/EDGAR material, and
- licensed data that cannot be redistributed without permission.

## 7. Response-generator split

The response-generator section reports:
- 60,270 fine-tuning samples
- 1,231 out-of-sample test samples

Total: **61,501 observations**.

Explain why this response-generation sample differs from the 65,192 cleaned topic-classification sample (for example, missing RESPONSE fields), and report the exclusion rule explicitly.
