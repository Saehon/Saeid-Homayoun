# Copy-ready updates for existing Hugging Face and Kaggle research directory

**Owner:** Dr Saeid Homayoun (SADHON / sadhon)  
**Version:** 2026-10-17  
**Purpose:** add original-source links to existing portfolio descriptions. This file contains no imported data and performs no upload.

## Hugging Face: existing registry description addendum

### Free accounting, audit and financial-text data — verified research links

A curated source index for accounting information systems, CAM/KAM, ICFR, financial NLP, valuation and forensic research is published at:
**https://saeid-audit-ai-research-library.vercel.app/sources.html**

The link-only directory cites original providers:
- SEC EDGAR/XBRL: https://www.sec.gov/search-filings/edgar-application-programming-interfaces
- Analytext: https://www.analytext.com/ (CC BY-NC 4.0 website terms; separately check data/code)
- Loughran–McDonald/SRAF: https://sraf.nd.edu/loughranmcdonald-master-dictionary/ (academic-use permission)
- Kenneth R. French Data Library: https://mba.tuck.dartmouth.edu/pages/faculty/Ken.French/data_library.html
- Aswath Damodaran data: https://pages.stern.nyu.edu/~adamodar/New_Home_Page/data.html
- PCAOB inspection reports: https://pcaobus.org/oversight/inspections/firm-inspection-reports
- SEC AAER: https://www.sec.gov/enforcement-litigation/accounting-auditing-enforcement-releases
- World Bank WDI: https://datacatalog.worldbank.org/search/dataset/0037712/world-development-indicators

**Provenance and rights:** Free access is not blanket permission to redistribute, relicense, train, or publish downstream rows. The repository contains metadata only. Source-specific commercial, noncommercial, fairness, and audit restrictions apply. Research prototypes must be independently validated and must not be described as production models or accepted manuscripts.

Suggested existing destination (do not create a duplicate if unnecessary):
https://huggingface.co/datasets/SADHON/accounting-finance-audit-open-registry

## Kaggle: dataset description addendum

**Title:** Free Accounting, Audit & Financial Text Data — Academic Source Registry

**Subtitle:** Official links and rights/replication rules for SEC XBRL, Analytext, Loughran–McDonald, Fama–French, Damodaran, PCAOB, SEC AAER and World Bank.

**Description:** This *original metadata catalogue* supports reproducible accounting information systems and audit analytics studies. It contains no copied source data, quotes from licensed corpora, unpublished audit workpapers, firm-level vendor prices, or trained model weights. Use the official provider URLs and respect source permissions. Related material: https://saeid-audit-ai-research-library.vercel.app/sources.html .

**Files ready after owner review:** `free_data_sources.csv` (metadata only); `free_data_sources.json` (source and pilot audit registry); `PILOT_FREE_DATA_SOURCE_GUIDE.md`.

**Licensing:** Only author-created metadata text may be published under an original-work license selected by the owner. It does NOT grant a license for any linked third-party data. Verify the compatibility of any dataset-level Kaggle licence before publication.

**Kaggle author profile:** https://www.kaggle.com/sadhon

## Publication checklist
1. Confirm Hugging Face repository-write access or manually edit the existing dataset card in the owner's browser.
2. Check whether the intended Kaggle dataset already exists and reuse its existing ID, if so. Do not claim automatic sync.
3. Scan every proposed upload for raw/transformed vendor data, licence breaches, secrets and partial extracts.
4. Update the existing portfolio with links/metadata only after author review.
5. Verify both public pages by readback and record revision/commit URL.
