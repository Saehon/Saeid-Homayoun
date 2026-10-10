# DATASETFREE — FT50/ABS4/ABS3 replication and open-data research plan

**Research date:** 2026-10-10. **Status:** Evidence map and *untested* hypothesis design; not completed replication/meta-analysis/empirical estimation.  
**Canonical Google Drive report:** https://docs.google.com/document/d/1MTTPoKlb64CN2oIlMROaHQz6XVmP-MPq4UcVCcJmtac/edit  
**Project master:** https://drive.google.com/drive/folders/17QYKaBRVkg2Wr-slwrM0gWd_o6EYdUD7

## Bottom line

Proposed paper: **The AI Capability–Disclosure Gap: Innovation, Internal-Control Risk, and Financial-Market Pricing.**

Use Babina et al. (2024, JFE) as an *economic framing and code template* only. Its [Mendeley V3 package](https://data.mendeley.com/datasets/s26kxvspn7/3) states that proprietary inputs including Compustat are replaced with **pseudo-data**. Actual Cognism records and proprietary finance data are **not** freely reconstructed by executing this package. Full legal reproduction requires original licensing.

## Phase 1 — literature review and meta-analysis protocol (not yet run)
Use ScienceDirect, JFE, JAR, JAE, Management Science, accounting/finance/economics journal sites, Emerald, Mendeley, openICPSR and cited/forward citations. Apply date/language/publication constraints transparently. Include journal rankings only after confirming the specific AJG and FT50 edition.

**Close published predecessors and novelty limits:**
- Babina et al. (2024), *Artificial Intelligence, Firm Growth, and Product Innovation*, JFE, DOI: https://doi.org/10.1016/j.jfineco.2023.103745
- *Unlocking operational efficiency: How AI human capital investment enhances data processing efficiency?*, Economics Letters, https://www.sciencedirect.com/science/article/pii/S0165176524006311 — AI workforce investment, earnings timing and reporting weaknesses.
- *Accounting-employee flows and financial reporting quality*, 2026, https://www.sciencedirect.com/science/article/pii/S0278425426000530 — employee flow and ICFR/misstatements/filing delays.
- Basnet et al. (2025), *Analyzing the market's reaction to AI narratives in corporate filings*, IRFA, https://doi.org/10.1016/j.irfa.2025.104378 — actionable versus speculative AI disclosure, valuation and patenting.
- Li (2026), *Artificial intelligence innovation and financial report quality*, IREF, https://doi.org/10.1016/j.iref.2025.104832.
- Chen, Kim and Peng (2026), *The real effects of AI: Evidence from corporate investment efficiency*, J Empirical Finance, https://doi.org/10.1016/j.jempfin.2026.101730.
- *New product announcements, innovation disclosure, and future firm performance*, Review of Accounting Studies, https://link.springer.com/article/10.1007/s11142-024-09820-0.
- Emerald *Risk disclosure complexity and report readability*, Journal of Financial Reporting and Accounting (2026), https://doi.org/10.1108/JFRA-02-2026-0105.
- Emerald *Digital technologies and the evolution of the management accounting profession*, Meditari Accountancy Research (2024), https://doi.org/10.1108/MEDAR-07-2023-2097.
- Emerald *Corporate digital transformation and financing cost of green bond*, Managerial Finance (2026), https://doi.org/10.1108/MF-12-2025-1015 — CSMAR/CNRDS proprietary.
- *The pricing of audit services: evidence from South Africa*, Journal of Accounting in Emerging Economies (2025), https://www.emerald.com/jaee/article/15/5/1029/1275525/ — IRESS subscription data.

**MacAma adaptation**: [Yuan et al. 2026, DOI](https://doi.org/10.1002/smmd.70045), [MIT GitHub code](https://github.com/YilinYuan/MacAma). Original methods use medical research standardized mean differences; redesign for financial panel coefficients. Agents: retrieval; eligibility; provenance/licensing; human-verified extraction; finance effect-size conversion; synthesis; novelty/falsification; reproducible code; human sign-off. Protocol = PECOS and PRISMA 2020, dual screening, coded exclusion reasons, extraction of coefficient/SE/sample/identification; random-effects pooling **only** for comparable outcomes with verified SE, paper-clustered/multilevel robust variance where estimates are dependent. Assess heterogeneity/publication bias. **No meta-analytic coefficients or significance calculated yet.**

## Phase 2 — empirical replication package audit
| Journal/package | Public link | What is provided | Gate |
|---|---|---|---|
| JFE AI investment, innovation (Babina et al.) | [Mendeley V3](https://data.mendeley.com/datasets/s26kxvspn7/3) | Code + pseudo proprietary inputs | Computational template only |
| JFE Great Recession Babies (Bias & Ljungqvist) | [Mendeley V2](https://data.mendeley.com/datasets/kj65wmpbft/2) | Data/code claims all figures/tables | Check package dependencies |
| JFE Innovation Booms / Human Capital | [Mendeley V1](https://data.mendeley.com/datasets/8bksxrcpbs/1) | Replication kit | Audit licences / contents |
| JFE Patents that match your standards | [Mendeley V1](https://data.mendeley.com/datasets/2vyv7vwypr/1) | README + code/data | Audit execution |
| JFE Colour of Finance Words | [Mendeley V2](https://data.mendeley.com/datasets/37x3jsf488/2) | Text sentiment package | Validate source completeness |
| JFE Co-Pricing Factor Zoo | [Mendeley V1](https://data.mendeley.com/datasets/sxrmkvt3k8/1) | 14 CSV + 1 RDS and open [GitHub](https://github.com/Alexander-M-Dickerson/co-pricing-factor-zoo) | Promising free economic pipeline, not a stock-price panel |
| JFE ESG preferences | [Mendeley V2](https://data.mendeley.com/datasets/8ddvm3kwzj/2) | Analysis-ready data and code claim | Audit |
| JFE Chronologically Consistent LLMs | [Mendeley V2](https://data.mendeley.com/datasets/s6yt64mrwb/2) | Derived exhibits, CRSP/Dow Jones synthetic stand-ins | Partial only |
| JFE China Walls | [Mendeley V1](https://data.mendeley.com/datasets/tf6xbw5x9z/1) | Synthetic data permit code to run | NOT original estimates |
| JFE Appropriated Growth | [Mendeley V3](https://data.mendeley.com/datasets/stfk3cj3nc/3) | Random subsample due to licences | Not full sample |
| Management Science de Kok (2025) | [GitHub](https://github.com/TiesdeKok/chatgpt_paper) | Code examples, earnings-call data | Strong text classification template |
| Text as Data in Economic Analysis | [openICPSR V2](https://www.openicpsr.org/openicpsr/project/228102/version/V2/view) | Extensive code/derived files | Large files, some proprietary dependences |

**Reading the table:** metadata verified; no script run or numeric original-table replication claimed.

## Phase 3 — free datasets / GitHub / Hugging Face / Kaggle
| Data and code | Use | Important access/validation caveat |
|---|---|---|
| [SEC financial statements 2009–2026](https://www.sec.gov/dera/data/financial-statement-data-sets.html) | Company financial outcomes by CIK/date | XBRL filings as-filed, not cleaned Compustat |
| [SEC financial statement notes](https://www.sec.gov/data-research/sec-markets-data/financial-statement-notes-data-sets) | Income taxes, goodwill, leases, contingencies and impairment text | Complex schema/large volume |
| [SEC APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces) | DEF 14A management bios, 10-K, 8-K and company facts | Executive expertise must be extracted and manually reviewed |
| [SRAF Notre Dame](https://sraf.nd.edu/) | Loughran-McDonald sentiment, SEC textual tools | Academic, noncommercial terms |
| [Analytext](https://www.analytext.com/) | Parsed SEC Item 1/1A/7 and footnotes 2008+, 32 accounting-note topics | Registration for downloads; source mentions Python code available **to purchase** |
| [USPTO datasets / PatentsView / AIPD](https://www.uspto.gov/ip-policy/economic-research/research-datasets) | Independent AI patent capability proxy | Fuzzy firm assignee match must be manually assessed |
| [USPTO trademark cases](https://www.uspto.gov/ip-policy/economic-research/research-datasets/trademark-case-files-dataset) | New product trademark/class innovation | Bulk data large; ownership name changes |
| [Kenneth French factors](https://mba.tuck.dartmouth.edu/pages/faculty/Ken.french/data_library.html) | FF3/FF5/RF/industry portfolio and asset pricing controls | Does NOT provide single security returns |
| [Damodaran current data](https://pages.stern.nyu.edu/adamodar/New_Home_Page/datacurrent.html) | 2026 **industry** WACC / beta and cost capital | Company data NOT freely redistributed |
| [JobHop v2](https://huggingface.co/datasets/aida-ugent/JobHop) | Occupational transitions, skill trajectory validation | Anonymized; not firm/executive joinable |
| [O*NET 31.0](https://www.onetcenter.org/database.html) | Occupation AI skill intensities | Occupation taxonomy, NOT actual firm hires |
| [ESCO](https://esco.ec.europa.eu/en/use-esco/download) | European occupation-skill crosswalk | Multilingual, licenced terms to check |
| [Financial PhraseBank](https://huggingface.co/datasets/takala/financial_phrasebank) | Financial tone benchmark | CC BY-NC-SA 3.0; non-commercial |
| [ProsusAI FinBERT](https://huggingface.co/ProsusAI/finbert) | Financial text sentiment | Separate weights/data licence review |
| [Kaggle resume sample](https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset) | CV extraction benchmark | Platform CC0, scraped from LiveCareer: source rights and PII unresolved |
| [MacAma MIT GitHub](https://github.com/YilinYuan/MacAma) | Audited multi-agent meta-research skeleton | Medical effect statistics need adaptation |

## Observable constructs and joining strategy
**Grain** CIK-fiscal-year, initial US listed firms, SEC years with comparable filing sections. Split future periods chronologically; reserve independent human-labeled text validation set.

- `AI_CLAIM`: implementation-specific AI filing narratives (Item 1/1A/7), coded separately from boilerplate/speculation.
- `AI_CAPABILITY`: AI patent/assignee matched indicators, cumulative count + category-weighted portfolio; patenting is incomplete because licensed AI may lack patents.
- `GAP`: standardized industry-year residual of AI_CLAIM after explaining independent AI_CAPABILITY. This is a *measurement mismatch*, NOT proof of managerial deception.
- `OUTPUT_INNOV`: new trademark filings and product-class diversification, with forward dates.
- `ICFR`: Item 9A disclosed material weaknesses, validated from full filing text; 8-K Item 4.02 separate non-reliance outcome and filing timeliness.
- `ACCOUNTING`: SEC XBRL net income, cash flows, R&D, capex, intangibles, accrual-related measures.
- `MARKET`: event CAR only if lawful validated firm prices/adjustments/delistings obtained; Kenneth French factors alone insufficient.

## Three candidate hypotheses — NOT verified original
**H1.** Higher unexplained AI disclosure–capability gap at *t* predicts worse next-year financial-reporting outcomes than otherwise similar aligned firms, controlling for disclosure volume, firm and industry-year factors. Null/reversal plausible where AI is licensed or outsourced.

**H2.** Independently observable AI capability paired with specific implementation claims predicts greater subsequent patent-to-trademark/product-class conversion than capability without implementable disclosure (or claims without capability), controlling for investment and innovation baseline. This *interaction* must be separately differentiated from Babina and Basnet.

**H3.** Higher ex-ante AI disclosure–capability gap predicts stronger pricing reversals at adverse accounting-disclosure events, conditional on a public lawful price panel and event dates. Consider alternative that investors correctly price outsourced AI deployment.

**Models:** firm/year or industry-year FE, company-clustered uncertainty; PPML for counts; logit/LPM robustness for rare ICFR events; placebo years, lagged predictors and event-study timing. Do not interpret coefficient as causal from ordinary FE; shocks or IV require exclusion and pretrend validation. Address multiple tests and source-matching error.

## Digital twin, model criticism, and reproducibility

Simulate firm size, AI deployment, disclosure error, patent propensities and rare ICFR events; evaluate Type I error, detection power, false matching, estimator bias and 95% CI coverage. Synthetic pilots can reject bad designs and validate code, **not manufacture/establish real-world significant results**. 
Stage gates: literature novelty -> rights -> CIK & assignee QA -> annotation -> chronological data freeze -> synthetic falsification -> real-data analysis -> human scientific sign-off. Maintain version/hash, effective sample counts, model specifications and all negative findings.

**Do not commit, mirror or scrape identifiable third-party resumes or Cognism profiles without legally appropriate rights.**

Google Drive is the authoritative archive, GitHub is code/provenance. Future Kaggle/HF releases require verified source licences and human approval.
