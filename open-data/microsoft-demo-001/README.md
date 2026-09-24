# Microsoft Demo 001 — Phase 1 Open Accounting Data Bridge

A compact, reproducible **SEC → GitHub → validation → Kaggle/Hugging Face** accounting-data example.

**Company:** Microsoft Corporation (MSFT)  
**CIK:** 0000789019  
**Fiscal years:** FY2024–FY2026  
**Primary source:** U.S. SEC, Microsoft FY2026 Form 10-K  
**Accession:** 0001193125-26-323660  
**Unit:** USD millions

## Canonical data

| FY | Revenue | Gross profit | Operating income | Net income |
|---:|---:|---:|---:|---:|
| 2024 | 245,122 | 171,008 | 109,433 | 88,136 |
| 2025 | 281,724 | 193,893 | 128,528 | 101,832 |
| 2026 | 331,839 | 225,465 | 155,237 | 133,749 |

Run:

```bash
cd open-data/microsoft-demo-001
python validate.py
python analysis.py
```

FY2026 output: revenue growth **17.79%**, gross margin **67.94%**, operating margin **46.78%**, and GAAP net margin **40.31%**.

The FY2026 filing also reports non-GAAP measures excluding net gains and losses from investments in OpenAI. This Phase-1 dataset deliberately keeps the GAAP statement values separate.

## Refresh from SEC CompanyFacts

```bash
SEC_USER_AGENT="Your Name your-email@example.edu" python fetch_sec.py
python validate.py
```

Automated access must follow SEC fair-access requirements.

## Architecture

```text
SEC EDGAR / CompanyFacts
          ↓
 canonical GitHub dataset
          ↓
 deterministic validation
          ↓
 ┌──────────────────┬──────────────────┐
 ↓                  ↓
Kaggle dataset      Hugging Face dataset
 ↓                  ↓
notebooks           agents / ML
 └────────────┬─────┘
              ↓
        reproducible research
```

**GitHub is the source of truth.** Kaggle and Hugging Face are distribution/execution layers.

## Scientific boundary

Passing validation establishes technical reproducibility of this small dataset. It does not constitute audit assurance, investment advice, causal validation, or professional certification.
