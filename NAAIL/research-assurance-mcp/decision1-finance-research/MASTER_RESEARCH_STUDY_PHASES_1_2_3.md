# NAAIL Decision-1 Finance and Audit-Risk Research — Master Study V1.0
**Date:** 2026-10-10 | **Research owner:** Saeid Homayoun | **Project:** NAAIL-Decision1-ICFR-Finance-FT50-2026
**Status:** Research-design and reference-screening phase; code-based synthetic power feasibility only. NO real SEC/price panel estimated, NO Decision-1 API run, NO significant empirical claims.
**Target:** The Journal of Finance (stretch); Journal of Financial Economics / Review of Financial Studies (stretch); Management Science; Journal of Accounting Research / Journal of Accounting and Economics; AJPT or Accounting and Business Research if contribution becomes primarily assurance-focused. Target classification is not a verified AJG ranking.

## Executive decision
**Preferred paper title:** *Unpriced Assurance Risk: Evidence-Verified AI Signals, Model Disagreement, and the Price Discovery of Internal-Control Information*.
**Core contribution:** financial-market information content of **pre-disclosure, independently corroborated accounting/ICFR risk estimates**; not a claim that Microsoft-Decision-1 is an autonomous auditor. Compare specialized decision scoring with Loughran–McDonald, FinBERT, a general LLM, and conventional firm/factor controls. Seek market-economic implications, not only model accuracy.
**Research gate:** If credible firm-security price linking or independent ICFR labels cannot be acquired with valid rights, do NOT call this a Journal of Finance empirical study; pivot to a rigorously benchmarked accounting/auditing outlet.

## Project heritage and boundary
- **Existing public NAAIL/LEMON pilot:** https://github.com/Saehon/Saeid-Homayoun/pull/152 (draft; 18 synthetic cases, initial offline rule model, opt-in hosted Decision-1 adapter and Lemon Human Gate).
- **Existing proprietary POMELO review pilot:** https://github.com/Saehon/pomelo-core/pull/57 (private draft; **do not copy any private code into public repo**).
- **Canonical Drive project folder:** https://drive.google.com/drive/folders/1Y6NqwdwjBlYCqkGObTb9UeRNqiZin6iZ
- **Prior Drive project index:** https://docs.google.com/document/d/1zugMqqio6LW1nhPrDknmjIYkddqin6dH12xrVqG3t5A/edit
- **Hugging Face user:** https://huggingface.co/SADHON (read-only authentication verified on 10 Oct 2026; NO new hub dataset/repository published).
- **Kaggle:** no authenticated account ID verified; project dataset/notebook link UNASSIGNED, not falsely claimed published.
- **Existing Copilot master prompt** (source supplied in conversation): MICROSOFT_COPILOT_MASTER_PROMPT_NAAIL_DECISION1_2026-10-10.md. Preserve unchanged; companion independent instruction in COPILOT_RESEARCH_MASTER_PROMPT.md.
- NAAIL Knowledge Core remains governed; Technology Core is replaceable; all scientific conclusions require independent challenge and human review.

# PHASE I — Literature mapping, systematic review and meta-analysis protocol

## I.1 Sources and screening standard
This is an **initial author-verified scoping evidence map**, NOT a completed PRISMA review or a completed quantitative meta-analysis. Search/screen systematically across Google Scholar, Crossref, Web of Science, Scopus, SSRN, publishers, and GitHub; document date, exact query, search engine, records identified, duplicates, screening disagreements, full-text eligibility and exclusion reasons. Suggested search clauses:
- ("internal control" OR "material weakness" OR ICFR) AND (stock return OR risk premium OR "cost of equity" OR price discovery);
- ("financial disclosure" OR "10-K" OR "10-Q") AND (textual change OR semantic novelty OR earnings OR return prediction);
- (large language model OR agentic OR AI model disagreement OR selective prediction) AND (finance OR auditing OR disclosure);
- ("replication code" OR "data availability") AND ("Journal of Finance" OR "Review of Financial Studies" OR "Management Science" OR "Journal of Accounting Research").
Window: **2020–10 Oct 2026** for technological frontier; add indispensable pre-2020 theory and ICFR benchmarks. Translate to formal PRISMA 2020 protocol: https://www.prisma-statement.org/prisma-2020. For finance, favor verified publisher pages over automatically generated citation sites; journal ratings must be checked against the authoritative AJG edition (no unsupported star claims).

## I.2 Confirmed primary studies and what they rule out
| Verified paper | Journal / year | Relevance | Novelty boundary |
|---|---|---|---|
| Cohen, Malloy & Nguyen, **Lazy Prices**, https://doi.org/10.1111/jofi.12885 | **Journal of Finance**, 2020 | Changes in SEC language and subsequent returns; publisher offers replication code | SEC text predicts returns is **not** itself novel. |
| Jensen, Kelly & Pedersen, **Is There a Replication Crisis in Finance?**, https://doi.org/10.1111/jofi.13249 | **Journal of Finance**, 2023 | Replicable factor themes, multiple-testing discipline and code | Must benchmark against known factors and correct specification searches. |
| Bryzgalova, Lerner, Lettau & Pelger, **Forest Through the Trees**, https://mpelger.people.stanford.edu/data-and-code | **Journal of Finance**, 2025 | Characteristic/portfolio modeling and author-hosted code | Asset pricing predictor innovation must be incremental. |
| Gu, Kelly & Xiu, **Empirical Asset Pricing via Machine Learning**, https://doi.org/10.1093/rfs/hhaa009 | **Review of Financial Studies**, 2020 | Nonlinear return prediction and out-of-sample design | Generic AI return prediction has large prior literature. |
| Chen, Pelger & Zhu, **Deep Learning in Asset Pricing**, https://mpelger.people.stanford.edu/data-and-code | **Management Science**, 2024 | Deep SDF and systematic asset-pricing benchmark with code | Benchmark nonlinearity and transaction costs. |
| Siano, **The News in Earnings Announcement Disclosures**, https://doi.org/10.1287/mnsc.2024.05417 | **Management Science**, online 2025 | LLM captures earnings language and contemporaneous return response | LLM disclosure signal alone is not sufficient innovation. |
| **Can ChatGPT Forecast Stock Price Movements?**, https://doi.org/10.1016/j.jfineco.2026.104335 | **Journal of Financial Economics**, 2026 | LLM headline signal and delayed return response | Must isolate independent accounting-evidence effect. |
| Bali, Kelly, Mörke & Rahman, **Machine Forecast Disagreement**, https://doi.org/10.1093/rfs/hhag042 | **Review of Financial Studies**, 2026 | Forecast-dispersion measure and future stock returns | Generic model disagreement is no longer novel; focus on verified *accounting-risk* disagreement. |
| **Generative AI and Asset Management**, https://doi.org/10.1093/rfs/hhag050 | **Review of Financial Studies**, 2026 | Hedge-fund GenAI adoption and return differences | Adoption/return premium is a separate but overlapping channel. |
| Jensen et al., **Machine Learning and the Implementable Efficient Frontier**, https://doi.org/10.1093/rfs/hhag022 | **Review of Financial Studies**, 2026 | Net transaction cost optimization and public paper-linked GitHub code | Gross alpha/Sharpe is not enough; report net costs. |
| Ashbaugh-Skaife, Collins, Kinney & LaFond, **Effect of SOX Internal Control Deficiencies on Firm Risk and Cost of Equity**, https://doi.org/10.1111/j.1475-679X.2008.00315.x | **Journal of Accounting Research**, 2009 | Fundamental prior evidence ICFR deficiencies and cost of equity | Ordinary ICFR weakness–cost-of-equity hypothesis is already tested. |
| Hammersley, Myers & Shakespeare, **Market Reactions to ICW Disclosures**, https://doi.org/10.1007/s11142-007-9046-z | **Review of Accounting Studies**, 2008 | Weakness specificity and market event response | Generic ICFR market reaction is established. |
| Ghosh, Ikäheimo, Myllymäki & Sihvonen, **Long-Run Stock Returns Following Internal Control Disclosures**, https://doi.org/10.1111/jbfa.70012 | **Journal of Business Finance & Accounting**, online 2025/2026 | Subsequent drift after SOX302 material weakness disclosures | ICFR underreaction is established; test *incremental pre-disclosure verification*. |
| Yuan et al., **MacAma: Multi-AI Agent as a Co-Scientist for Automated Meta-Analysis**, https://doi.org/10.1002/smmd.70045 | **Smart Medicine**, 2026 | Multiagent protocol-constrained evidence synthesis; human-verifiable trace | MacAma is a METHOD ANALOGY from biomedicine, not evidence of finance results. |
| Loughran & McDonald, **Textual Analysis in Accounting and Finance: A Survey**, https://doi.org/10.1111/1475-679X.12095 | **Journal of Accounting Research**, 2016 | Finance dictionary/text provenance | LM dictionary and SEC baseline are mandatory controls. |
| Allena, **Confident Risk Premiums and Investments Using ML Uncertainties**, https://doi.org/10.1093/rfs/hhaf087 | **Review of Financial Studies**, 2026 | Forecast uncertainty/precision and portfolio choices | Confidence-aware ML returns are not intrinsically new. |

**Red flag:** The RFS 2023 study *Man versus Machine Learning: The Term Structure of Earnings Expectations and Conditional Biases* received an **Expression of Concern** in 2026 (https://doi.org/10.1093/rfs/hhag017). Do not import its effect estimate or code as validated without resolving current editorial status.

## I.3 MacAma-style agent protocol
Agent 1 Librarian: retrieve metadata + primary DOI; log search strings and retrieval timestamps.
Agent 2 Screeners A/B: independently decide inclusion based on preregistered PICOS-style criteria, with disagreement logged.
Agent 3 Evidence extractor: record outcome/definition, coefficient, CI/SE, design, identification, population and availability of code.
Agent 4 Statistician: harmonize effect estimands ONLY when comparable (e.g. standardized market reaction or Fisher-z correlation); prohibit pooling incompatible alpha, probability, dollar returns, annual cost-of-equity and diagnostic AUC in one effect.
Agent 5 Replication auditor: check links, stated access rights, data rights, executable status and versioned test reports.
Agent 6 Adversarial falsifier: flag p-hacking, publication bias, overlap, retrained future data, unobservable returns and benchmark leakage.
Agent 7 Human research lead: approves inclusion, analytic decisions and written claims; model consensus does not become a scientific fact.

## I.4 Meta-analysis pre-analysis specification (not yet computed)
Primary *eligible* estimand family A: standardized differences in market price reaction to disclosed ICFR problems. Family B: partial correlations between ICFR risk and future risk/financing outcomes. Family C: paired difference in OOS prediction loss, not pooled with A/B. For each family: n, coefficient, uncertainty, covariance within paper, sample overlap, period, region, objective audit vs model proxy, disclosure-vs-prediction timing and quality appraisal.
Use REML random-effects meta-analysis with Hartung–Knapp intervals when appropriate; heterogeneity I²/tau²; dependent effect-size robust variance estimation or select one primary estimate per paper; sensitivity to study risk of bias and preregistered time windows; trim-and-fill/Egger only if justified with sufficient comparable studies. Narrative synthesis if sparse/incomparable. **No meta-effect, pooled p value or PRISMA count exists yet**. Register protocol before exhaustive screening.

# PHASE II — FT50 / AJG research replication code selection
| Priority | Paper & code (verified source) | Code/data assessment | Reuse in this project |
|---|---|---|---|
| A | Cohen et al. JF 2020 replication attachment: https://onlinelibrary.wiley.com/doi/10.1111/jofi.12885 | Publisher explicitly lists **ReplicationCode.zip**; raw original sample/data NOT confirmed freely accessible | Filing text changes, change-vs-level decomposition, market response, test design. |
| A | Jensen et al. JF 2023: https://github.com/bkelly-lab/jkp-data | Author-maintained Python code; generating raw firm panel requires WRDS; precomputed factors freely browsable at https://www.jkpfactors.com/data | Known-factor controls; multiple-testing protections; factor portfolio design. |
| A | Chen et al. MS 2024: https://mpelger.people.stanford.edu/data-and-code | Author's code/data links exist; inspect separate dataset entitlements | Deep learning/SDF and standard portfolio controls. |
| A | Jensen et al. RFS 2026: https://github.com/theisij/ml-and-the-implementable-efficient-frontier | Direct paper-linked open code; underlying CRSP/Compustat rights and redistribution must be verified | Turnover, trading-cost constraints, net-of-cost evaluation. |
| B | Bryzgalova et al. JF 2025: https://mpelger.people.stanford.edu/data-and-code | Author-linked code and data; individual feed licensing must be checked | Cross-section characteristics and characteristic trees. |
| B | Gu et al. RFS 2020 paper: https://doi.org/10.1093/rfs/hhaa009 ; third-party transparent implementation https://github.com/CttQuantLab/Empirical-Asset-Pricing-via-Machine-Learning | **Third-party recreation**, NOT an official author replication; CRSP may be required | GBRT, elastic net, OOS R² and portfolio sensitivity. |
| B | SRAF McDonald Python: https://sraf.nd.edu/textual-analysis/code/ | Free for **non-commercial academic research**; source terms apply | SEC downloader, parser and LM dictionary baseline. |
| B | Analytext SEC text: https://www.analytext.com/ | Selected SEC parsed data/metrics offered; page indicates shared extraction Python code **available to purchase** for some components | Section/footnote extraction subject to access and license verification; do not claim all code free. |
| C | RFS author Dataverse statement: https://academic.oup.com/rfs | RFS states code deposit now required; item-level availability still requires checking | Literature replication registry, not a dataset itself. |
**Decision:** JF *Lazy Prices* + JKP 2023 + RFS 2026 transaction-cost package = strongest finance replication spine. SRAF / Analytext are text infrastructure, not automatic new hypotheses. Code link existence does NOT imply all data free, original results replicated or MIT licensing. Never copy publisher zip blindly without license review.

# PHASE III — Fee-free data, models and reproducible empirical study

## III.1 Audited source registry
| Source | Link | Inputs | Open/free limitation | Priority |
|---|---|---|---|---|
| SEC EDGAR APIs | https://www.sec.gov/search-filings/edgar-application-programming-interfaces | Company submissions, filing dates/accessions, facts from XBRL/CompanyFacts | Public/no API key; comply with SEC fair-access/User-Agent; companyfacts lacks full ICFR labels and cannot replace Item 9A document coding | Core |
| Notre Dame SRAF | https://sraf.nd.edu/sec-edgar-data/ and https://sraf.nd.edu/textual-analysis/code/ | 10X 1993-2025 summaries/documents, LM sentiment, EDGAR downloader | Noncommercial research terms; substantial storage; baseline 2025 cutoff | Core |
| Analytext | https://www.analytext.com/ | Sections and financial-statement notes from 2008/2009 onward | Validate which tables are free and source code purchase restriction; full data may be gigabytes | Core/conditional |
| Stanford SEFD | https://github.com/Stanford-Advanced-FinTech-Lab-SAFTL/stanford-edgar-filings-dataset | Layout-sensitive SEC parser and SEFD-v1 2022–2025 | Some OCR services/attachments may have cost and data license limits; coverage partly newer | Core/secondary |
| Fama–French factors | https://mba.tuck.dartmouth.edu/pages/Faculty/ken.french/data_library.html | FF3/FF5, momentum, factor portfolios, risk-free rates | Public downloads; **2025 CRSP FIZ→CIZ change**; check return-definition continuity | Core |
| JKP precomputed data | https://www.jkpfactors.com/data | 153 long–short characteristic factors, portfolio returns and selected underlying data | Precomputed factor returns available; generating stock-level file needs WRDS; audit rights on downloadable stock-level rows | Core controls |
| Damodaran | https://pages.stern.nyu.edu/adamodar/New_Home_Page/data.html | Industry risk premia, betas, spreads, corporate finance aggregates (2026 archive) | **No downloadable individual-firm dataset** from licensed vendors; use industry/year only | Industry controls |
| Hugging Face FinBERT | https://huggingface.co/ProsusAI/finbert | Finance sentiment baseline | Code repo Apache-2.0; individual model weight/dataset license review | Benchmark |
| Kaggle Layline SEC metadata | https://www.kaggle.com/datasets/layline/companies ; DOI: https://doi.org/10.7910/DVN/WACGV5 | SEC filing event metadata | Confirm Kaggle dataset availability/terms and coverage before use; authoritative SEC event timestamps take precedence | Exploratory |
| Hugging Face SADHON | https://huggingface.co/SADHON | Project-specific future model/dataset mirror | Account confirmed but no write permission to publish; link to planned repo UNASSIGNED | Future |
| Kaggle personal workspace | UNVERIFIED | Proposed notebook or license-cleared derived statistics | Do not invent Kaggle slug; publish only if authenticated and allowed | Future |

**No WRDS, CRSP, Compustat, TAQ, Audit Analytics, or proprietary data may be described as free simply because research code is public.** Public exchange-traded stock prices from casual APIs are not a replacement for point-in-time delisted/security-matched returns in a JF submission; this is a feasibility gate.

## III.2 Unit of observation and chronology
Panel A: US public companies with **10-K filing timestamp** or 10-Q filing timestamp and SEC CIK and accession. The first credible ICFR label must come from review of management/auditor disclosure text and be double-coded (Item 9A/controls and procedures, management SOX 302/404 and auditor report, year-specific law). A raw mention of "material weakness" is NOT a valid positive label. CAM is not equivalent to material weakness.
Panel B: security-day/month returns linked via **historically correct** CIK↔CUSIP/PERMNO/security mappings; account for delisted firms, multi-share classes, corporate actions, currency, corporate news and overlapping 8-K/earnings announcements.
Panel C: factor and market controls available **as of time t**, including FF5/momentum, industry, size, book-to-market, liquidity, prior momentum, volatility and SRAF LM tone/specificity and paragraph change.
**Timeline:** text for year t becomes available only at actual acceptance/publication time t0; never trade or model events using future filing pages, 2026 retrieval timestamp as a historical signal, future earnings, future CAM, revised labels, SEC restatement discovered after t0 or a current-ticker survivorship sample.

## III.3 Three falsifiable, narrowly differentiated hypotheses — candidate novelty, not certified novel
**H1 — Verification-adjusted assurance surprise and delayed repricing.**
After controlling for observed disclosed ICFR weakness status, LM text change, FinBERT tone, FF factors, conventional accounting risk, and contemporaneous earnings information, a **pre-outcome** independently corroborated *residual assurance-risk surprise* from financial-statement disclosure texts predicts **subsequent** abnormal price adjustment and realized future ICFR outcomes. Expected: more negative subsequent returns for unexpected risk, but can be zero/opposite.
- Treatment variable: ARIS_it = p_verified(MW_{i,t+1}|X_available at t) − p_baseline(MW_{i,t+1}|X_available at t). Both models trained only on earlier periods/firms. Evidence verification is a prespecified intervention; do not select threshold with test set.
- Event windows: public filing day [0,+1], delayed [+2,+21] and [+2,+60] TRADING days; adjust overlap with earnings and earnings announcements (calendar before price).
- Outcome: future market/industry/FF-factor-adjusted return (if quality stock data acquired) and subsequent real weakness as distinct endpoint; never use the outcome for defining the signal.
- Closest threats: Cohen et al. JF 2020, Ghosh et al. JBFA 2026, Ashbaugh-Skaife et al. JAR 2009. **New part is the independently verified residual surprise, not ICFR drift**.

**H2 — Accounting-evidence-conditioned disagreement and investor inattention.**
For the **same pre-event evidence packet**, dispersion between blind specialist-decision, FinBERT/LM, and general-LLM risk **probability** outputs predicts future return dispersion and delayed reaction **only in cases with externally corroborated evidence**; unverified disagreement predicts weaker/nonrobust effects. Expected sign requires preregistered direction.
- D_it = weighted variance of **separately calibrated** scores on the same task/evidence; compare against unconditioned machine forecast disagreement (Bali et al., RFS 2026).
- E_it = independently scored evidence completeness/reliability (blinded reviewers); avoid treating model confidence as evidence.
- Main coefficient: D_it × E_it on post-filing adjusted return or variance, controlling D, E, risk level, LM novelty and limits to arbitrage; test interaction with liquidity/institutional ownership.
- Key falsification: shuffled evidence references, hallucinated source IDs, permuted model identities, post-filing placebo risk packages, random filing non-ICFR sections.
- Model outputs alone are not professionally valid; comparison only after independent label and source verification.

**H3 — Assurance-risk spillovers across accounting exposure networks.**
Verified pre-disclosure ICFR/account-specific risk signals predict risk repricing among **publicly connected peers sharing accounting exposures**, above same-industry returns, and interaction weakens when peer disclosures corroborate low exposure.
- Exposure graph: firms linked using only historical public co-disclosed note topics (revenue, inventory, goodwill, debt), industry/SIC, product sector and public supplier exposure where verifiable; freeze graph at t−1 (not inferred from future realized distress).
- PeerShock_it = weighted leave-one-out sum of independent peer assurance surprises; exclude same-issuer data and future edges.
- Response: peer abnormal return, return comovement/volatility, or future peer ICFR disclosure after source firm's filing; separately report causal limitations.
- Identification: event times of source firms, matched nonexposed peers, risk-set controls, firm/date fixed effects, industry-by-date or industry-time FE as feasible, staggered events and unaffected placebo groups. **Network exposure may be endogenous**; DiD does not automatically solve selection.
- Existing ICFR industry contagion evidence (Bolton et al., *Advances in Accounting* 2016) means **generic spillover is not novel**; contribution is the pre-filing account-exposure graph plus independently verified conditional AI signal.

**Do not assert any hypothesis is "never studied" absent exhaustive search and expert novelty assessment.** The default is *candidate differentiated contribution with documented overlap*.

## III.4 Estimation, identification and economic magnitudes
Baseline panel/event designs:
(1) Risk_it = f(public text topics, 10-K changes, XBRL, lagged variables) estimated by rolling-origin blocked CV; evaluate PR-AUC, calibrated Brier/ECE, sensitivity to first-time MW, false-negative risk, and abstention.
(2) AdjReturn_{i,t+2:t+h} = α + β1 ARIS_it + β2 D_it + β3 E_it + β4 D_it×E_it + β5 PeerShock_it + γ controls + firm/industry/date FE + ε_it. Run hypothesis-specific model with non-collinear FE, ensure outcomes post-date model input; cluster by firm and date or use appropriate two-way clustered inference.
(3) Finance economics: factor alpha, Fama-MacBeth cross-sectional regressions and Newey-West correction where justified; value-weighted and equal-weighted portfolio sorts, rebalancing, bid–ask cost, turnover, market-cap screens, delisting and 2025 FIZ/CIZ factor-break robustness.
(4) Outcomes not requiring licensed stock returns: next-year independently adjudicated ICFR weakness; remediation; filing delay; amended statements; standard SEC finance ratios. These support an auditing/accounting paper, NOT the core JF returns claim.
(5) For remediation causal analysis: identify first remedial changes, simultaneous management decisions, treatment timing, parallel-trends, placebo periods and never-treated comparators. Do not call event-study associations causal by default.

## III.5 Comparison grid and publication acceptance criteria
A0 null/logistic baseline on lagged public data; A1 LM dictionary; A2 FinBERT; A3 generic tree/GBRT; B Decision-1 with verified live schema and documented API charges; C open general LLM on frozen identical evidence; D D1+independent source verification+Human Gate.
Primary comparison OOS calibration, PR-AUC for rare MW, time-to-error detection and incremental economic utility on genuinely frozen holdout. Test B/D against a *realistic* econometric/ML benchmark, not merely an intentionally weak keyword rule. The 18 synthetic pilot examples are ONLY engineering fixtures.
Publish all out-of-sample failures and nulls; present multiple-testing-adjusted p and economic effect sizes with 95% CIs; report model and API price/runtime/seed; author signoff required.

## III.6 Digital Twin and minimum detectable effects (EX ANTE ONLY)
Executable supplemental package: digital_twin_power.py and test_digital_twin.py (numpy, pandas, statsmodels). It fabricates no company facts: simulation assumes effects for H1, H2, H3, runs firm-clustered OLS under NULL_ALL_ZERO and ALTERNATIVE_ASSUMED, reports empirical rejection frequency across simulation seeds. It is a **power planning and pipeline test**, not evidence that any scientific hypothesis is significant.
Example executed in local environment on 10 October 2026: 100 imaginary firms × 4 periods × 80 simulations per scenario, seed 271828. These scenario rejection rates are not actual real-data estimates; inspect DIGITAL_TWIN_SIMULATION_RESULTS.json. Increase 500+ replications, calibrated effect sizes and familywise/FDR adjustments before formal power registration.
**Decision gate:** do not claim JF-level empirical maturity until full real-data sample and independent outcome coding exist.

# Journal-of-Finance positioning and 90-day work plan
**Novelty threshold:** demonstrate new *finance mechanism* (priced vs unpriced independently verified assurance information), not a technology sales comparison. Primary JF audience expects asset-pricing identification, economically interpretable magnitudes, market microstructure controls, robust replication and genuine sample rights.
**Call-for-papers check:** no 2026 Journal of Finance special issue or FT50 call specifically for this exact topic is verified in the searches used for this package; do not invent a CFP or deadline. Submit through confirmed regular journal procedures unless future official call is found.
Days 1–14: freeze Phase I search strategy and 2020–2026 scoping map; double-screen literature, audit license/use terms. Freeze three hypotheses before observing outcome coefficients.
Days 15–30: execute JF *Lazy Prices* replication code with lawful available source inputs; implement SRAF/Analytext/SEFD extraction and manual ICFR gold set; productionize legal data provenance; write reproducibility manifest.
Days 31–60: secure point-in-time security return data feasibility, historical mappings, asset pricing benchmark and 2018–2025 timestamp-safe panel; verify outcome labels; register analysis plan.
Days 61–90: evaluate rolling holdout, agent verification, H1/H2/H3 and sensitivity; publish neutral/null findings and reproducible synthetic code, keep proprietary POMELO private; decide finance vs auditing submission.
**Hard stop:** If security pricing data access and identification cannot be validated, reframe as AJPT/JAR-style audited decision quality study (still high academic value; do not simulate a financial alpha).

## Systematic-study records / provenance
Search date 2026-10-10; selected primary journal/publisher and repository pages checked. This is **not exhaustive**. All journal/corpus availability and link claims must be rechecked before scholarly submission. Record DOI, retrieval date, screenshots/publisher version, code SHA, rights/license, analysis sample and external researcher review. User research hypotheses are not actual findings or guaranteed journal acceptance.
