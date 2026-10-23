# Pilot-study free-data source registry — original source links (17 October 2026)

**Dr Saeid Homayoun** · Accounting, Auditing & Information Systems research. This is a *metadata-only* register for the 15 canonical research projects, their pilots and four supporting research tracks.

## Publication boundary

- This register includes **only source metadata and authoritative URLs**, not third-party data or text.
- Analytext reports **CC BY-NC 4.0** for website content; the website also mentions **paid Python extraction code**. Do not apply a generic "free and open" licence to all its resources.
- Loughran–McDonald SRAF resources are **free for academic research**, with separate commercial licensing. Do not relicense the dictionary as MIT or CC0.
- French factors are freely downloadable but built with licensed CRSP inputs; link original factors and record historical releases. **January 2025** CRSP FIZ→CIZ methodology shift is important.
- Damodaran provides **industry-level** benchmarks and archives; explicitly disallows sharing many underlying individual company observations from his third-party vendors.
- SEC CompanyFacts is numeric/structured **XBRL** data, not an API for extracting complete auditor CAM text; filings are a separate source. SEC fair access typically caps automated requests at **10 per second** and requires a descriptive User-Agent.
- PCAOB official datasets largely describe auditor/inspection firm reports. An issuer-level attribution needs separate evidence.
- SEC AAER listing does not cover all misstatement/fraud events and requires independent label work.
- World Bank WDI is CC BY 4.0 subject to specific source exceptions and attribution.

## Recommended references
1. **SEC EDGAR XBRL CompanyFacts** — Free API / no key; Structured finance. Financial statement ratios, ICFR/CapEx, audit-risk ex-ante measures. **Publishing:** Link API; any public derived file requires field/date and rights review. [Original provider](https://www.sec.gov/search-filings/edgar-application-programming-interfaces).
2. **SEC EDGAR filings / 10-K / 10-Q** — Free public filings; Financial text. Risk factors, auditor report, CAM narrative, internal controls, AI spending disclosure. **Publishing:** Link original filings; new text datasets only after extraction/provenance and legal review. [Original provider](https://www.sec.gov/edgar/search/).
3. **SEC Financial Statement Data Sets** — Free quarterly downloads; Structured finance. Panel accounting facts and reconciliation to XBRL. **Publishing:** Source link + verified code/small independently prepared examples. [Original provider](https://catalog.data.gov/dataset/financial-statement-data-sets).
4. **Analytext financial textual repository** — Public free research resources; Financial text. 10-K/10-Q notes and sections, 32 accounting topics, human capital/footnote metrics. **Publishing:** External-link first; check CC BY-NC 4.0 and file-specific terms; never assume paid extraction code is free. [Original provider](https://www.analytext.com/).
5. **Loughran–McDonald Master Dictionary** — Free for academic research; Financial text. Financial tone, negative words, uncertainty, litigiousness, complexity/reproducible lexicons. **Publishing:** External-link first; request separate commercial licence where applicable. [Original provider](https://sraf.nd.edu/loughranmcdonald-master-dictionary/).
6. **SRAF textual analysis resources** — Free academic resources; Financial text. Financial NLP preprocessing, dictionary methods, stopwords and code. **Publishing:** Links/code metadata first; assess each resource separately. [Original provider](https://sraf.nd.edu/textual-analysis/).
7. **Kenneth French Data Library** — Free public CSV/TXT downloads; Asset pricing. Fama–French 3/5 factor, industry peers, momentum and asset-pricing benchmarks. **Publishing:** Link original factor files; verify redistribution rights for CRSP-derived inputs before mirroring. [Original provider](https://mba.tuck.dartmouth.edu/pages/faculty/Ken.French/data_library.html).
8. **Aswath Damodaran valuation and industry data** — Free current/archival Excel & web data; Asset pricing. Valuation, cost of capital, industry beta, capex/FCF benchmarks and risk premia. **Publishing:** Link published industry aggregates; company-level vendor-derived data not for republication. [Original provider](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/data.html).
9. **PCAOB public firm inspection reports** — Public reports + CSV/XML/JSON; Audit enforcement. Audit firm inspections, auditor oversight and quality signals. **Publishing:** Link to report and official public structured files; source-level rights check before mirror. [Original provider](https://pcaobus.org/oversight/inspections/firm-inspection-reports).
10. **SEC Accounting & Auditing Enforcement Releases** — Free public enforcement index; Audit enforcement. Forensic accounting, future reporting enforcement, independent outcomes. **Publishing:** Link to original enforcement orders; independently label outcomes and as-of dates. [Original provider](https://www.sec.gov/enforcement-litigation/accounting-auditing-enforcement-releases).
11. **World Development Indicators** — Free public dataset/API; Macro / ESG. Macroeconomic control variables in risk, valuation and sustainable investment. **Publishing:** Candidate for a verified CC BY 4.0 credited extract; check each indicator's specific terms. [Original provider](https://datacatalog.worldbank.org/search/dataset/0037712/world-development-indicators).

## Selected source-audited pilot examples
1. **Three-company Fama–French factor pilot** (source_reported_executed). 31 monthly observations per MSFT/WMT/JPM from 2024-01 to 2026-07; factor library documented; IEX via Alpaca price feed is not redistributable CRSP data; no rows approved for public upload. Source: THREE_COMPANY_FAMA_FRENCH_V1_2.md.
2. **Ten-firm Damodaran-style AI CapEx pilot** (exploratory_source_reported). 30 firm-fiscal-year values, manually transcribed from StockAnalysis standardized statements citing S&P Global Market Intelligence; do not mirror vendor rows; full SEC reconciliation still incomplete; AI-specific CapEx not measured. Source: 10_Firm_Damodaran_AI_CapEx_Cash_Flow_Pilot_RESULTS_V1_2026-10-10.
3. **KIWI CAM Compass 50-firm checkpoint** (planned_or_repair). Proposed 50-firm repair checkpoint; independently verify auditor report dates and ex-ante features. No new public CAM extraction is authorized. Source: NAAIL AI Developer — Five Products and FT50 Pilot Map — 2026-10-10.
4. **LEMON-ICFR Sentinel 200-filings pilot** (proposed). Pilot proposal only. ICFR effective/ineffective/unknown labels must be validated independently; absence of MW disclosure is not verified effectiveness. Source: NAAIL AI Developer — Five Products and FT50 Pilot Map — 2026-10-10.
5. **EvidenceGate 120-question simulation** (proposed). Synthetic/public accounting questions proposed; proposed N is not an execution result. Source: NAAIL AI Developer — Five Products and FT50 Pilot Map — 2026-10-10.
6. **TokenCost & Carbon Twin 20-workload pilot** (proposed). Synthetic token/TDABC scenarios proposed; no public evidence of 20 externally validated workloads. Source: NAAIL AI Developer — Five Products and FT50 Pilot Map — 2026-10-10.
7. **DARWIN JEV–Risk–CAM synthetic starter** (existing_hf_synthetic_dataset). An existing public synthetic dataset exists. Public listing does not validate scientific performance, privacy clearance or right to redistribute new materials. Source: https://huggingface.co/datasets/SADHON/darwin-jev-risk-cam-synthetic-replication.

## Intended integration
- Free website navigation page: `sources.html`.
- HF existing dataset: https://huggingface.co/datasets/SADHON/accounting-finance-audit-open-registry . A versioned update requires actual Hugging Face write authorization, absent from ChatGPT's current connector.
- Kaggle owner: https://www.kaggle.com/sadhon . An update requires user-authorized Kaggle publishing; there is no authenticated Kaggle writer app in the current session.
- Canonical existing GitHub open-data portfolio: https://github.com/Saehon/Saeid-Homayoun/tree/main/open-source/accounting-finance-audit .
- GitHub reviewed static site: https://github.com/Saehon/Saeid-Homayoun/pull/187 .

## No auto-publishing or new source-data downloads
Do NOT move CAM/KAM/licensed audit opinions, Analytext files, L-M dictionaries, CRSP/IEX market data, StockAnalysis vendor rows or previously downloaded Google Drive files to public accounts based on this register.

## Provenance and evidence statuses
'Source-reported executed' is not an independent replication. 'Exploratory' and 'proposed' remain distinctly labeled. 'Existing HF dataset' does not mean new upload was approved.
