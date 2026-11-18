# Contract-AIVA — Data links and integration registry

This registry **links** US contract datasets and reproducibility code. It does not mirror or install any dataset.

## Hugging Face
- [SEC Exhibit 10 — material agreements, 2001–2024](https://huggingface.co/datasets/yonathanarbel/SEC_Exhibit_10)
- [SEC contracts financial extraction instructions](https://huggingface.co/datasets/TheTokenFactory/sec-contracts-financial-extraction-instructions)
- [LegalBench-RAG](https://huggingface.co/datasets/awinml/legalbench-rag)
- [Search CUAD datasets](https://huggingface.co/datasets?search=CUAD)

## GitHub
- [Official CUAD dataset and code](https://github.com/The-Atticus-Project/cuad)
- [LegalBench-RAG benchmark code](https://github.com/zeroentropy-ai/legalbenchrag)

## Kaggle
- [The Atticus Project](https://www.kaggle.com/theatticusproject)
- [Atticus Open Contract Dataset — beta](https://www.kaggle.com/datasets/theatticusproject/atticus-open-contract-dataset-aok-beta)

## Original public sources
- [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces)
- [Stanford Material Contracts Corpus](https://mcc.law.stanford.edu/)
- [CUAD paper](https://arxiv.org/abs/2103.06268)
- [ContractNLI](https://stanfordnlp.github.io/contract-nli/)

## Reproducible workflow
1. Verify licenses, provenance, document uniqueness and scope before downloading.
2. Download permitted content from original sources; do not commit raw corpora, tokens or credentials.
3. Keep codebooks, data manifests, scripts, accession IDs and checksums in GitHub.
4. Evaluate clause extraction on CUAD, with company/template-held-out splits.
5. Construct a separate SEC Exhibit 10 accounting sample linked to SEC XBRL.
6. Publish only redistributable derived artifacts to Hugging Face or Kaggle.

**Status (2026-11-18):** URLs registered. No external datasets copied, synchronized or installed. No Hugging Face/Kaggle repository created. This is not a claim of validated dataset access or completed empirical analysis.
