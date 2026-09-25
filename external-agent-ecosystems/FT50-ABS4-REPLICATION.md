# FT50 / ABS4 Replication Registry

Curated research replication packages relevant to accounting, auditing, financial reporting, finance, AI/ML/NLP and reproducible research.

> Scope note: journal-list classifications can change by edition. This registry records the journal and replication resource; verify the applicable FT50/AJG edition before using a ranking label in a manuscript.

| Paper | Journal | Open resource | Research use |
|---|---|---|---|
| deHaan, de Kok, Matsumoto & Rodriguez-Vazquez, *How Resilient Are Firms' Financial Reporting Processes?* | Management Science | https://github.com/TiesdeKok/mnsc.2023.4670 | Exemplary raw-data → code → pipeline → output/logs replication architecture; Python/SAS/Stata |
| Law & Shen, *How Does Artificial Intelligence Shape Audit Firms?* | Management Science | https://kelvinlaw.me/ai-fraud/machine-vs-auditors | AI adoption, auditor employment/skills, going-concern and internal-control opinions; replication files linked by authors |
| Huang, Li, Li & Lin, *Local Information Advantage and Stock Returns: Evidence from Social Media* | Contemporary Accounting Research | https://github.com/feng-li/local-information-advantage | Accounting/finance NLP, sentiment, topic analysis and reproducible code |
| Brown, Ma & Tucker, *Financial Statement Similarity* | Contemporary Accounting Research | https://github.com/guang-ma/fss | Reusable financial-statement similarity measure, data and R guidance |
| Breuer & Schütt, *Accounting for Uncertainty: An Application of Bayesian Methods to Accruals Models* | Review of Accounting Studies | https://github.com/hschuett/AccForUncertaintyCode | Bayesian accounting methods; sample data and code |
| Jensen, Kelly & Pedersen, *Is There a Replication Crisis in Finance?* | Journal of Finance | https://github.com/bkelly-lab/ReplicationCrisis | Large-scale finance replication infrastructure; legacy repository |
| Jensen, Kelly & Pedersen – maintained factor/data code | Related maintained resource | https://github.com/bkelly-lab/jkp-data | Maintained Python successor to the legacy ReplicationCrisis codebase |
| Gu, Kelly & Xiu, *Empirical Asset Pricing via Machine Learning* | Journal of Finance | https://github.com/Chamoy-code/empirical_asset_pricing_ml_project | Independent replication/implementation; ML pipeline and out-of-sample evaluation |

## Target research architecture

FT50 / ABS4 papers
→ replication code and data
→ GitHub registry
→ Hugging Face datasets/models
→ Kaggle notebooks/benchmarks
→ SEC/XBRL / PCAOB / IFRS / ESG evidence
→ Claude / OpenAI / Gemini / Microsoft
→ Replication Agent
→ Reviewer / Falsification Agent
→ Human verification
→ new accounting/auditing research

## Registry fields for expansion

For each future paper record:
- Paper, authors, year
- Journal
- DOI
- Research domain
- GitHub / official replication archive
- Data source
- Code language
- Hugging Face resource, if any
- Kaggle resource, if any
- License / reuse constraints
- Reproducibility status
- Validation notes
- Potential accounting/auditing extension

## Priority extensions

1. AI-enabled auditing and audit quality
2. ICFR / material weaknesses
3. CAM / KAM
4. SEC/XBRL and financial-reporting processes
5. Accounting textual analysis / LLMs
6. Fraud / enforcement / AAER
7. IFRS judgments
8. ESG / sustainability assurance
9. Evidence-grounded agent evaluation
10. Cross-provider replication: Claude vs OpenAI vs Gemini vs Microsoft

_Last curated: 2026-09-25._
