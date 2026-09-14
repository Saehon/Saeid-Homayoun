# NAAIL OpenLab — External Research Integrations

Owner: Saeid Homayoun  
ORCID: https://orcid.org/0000-0002-2536-0446

## Purpose
NAAIL integrates selected external open-source and research repositories through adapters rather than by claiming upstream code as original NAAIL IP. Each dependency keeps its original authorship, license, and terms.

## Priority integrations

### 1. AuditData-API → AuditDataAdapter
Repository: https://github.com/Saehon/AuditData-API
Use: structured audit-data ingestion for general ledger, trial balance, receivables, payables, inventory, entity and user data.
Primary targets: KIWI™, POMELO™/VERA™, IFRS-AI-Inspector, audit digital twin.

### 2. TimesFM → TimesFMAdapter
Repository: https://github.com/Saehon/timesfm
Use: time-series forecasting, ICFR risk trajectories, going-concern indicators, control-risk forecasting, temporal holdouts and predictive audit analytics.
Primary targets: ICFR/TimesFM, KIWI™, POMELO™/VERA™.
Note: preserve the upstream source and model-weight license boundaries.

### 3. yfinance → MarketDataAdapter
Repository: https://github.com/Saehon/yfinance
Use: market prices and related market data for event studies, abnormal returns, volatility, CAM/KAM market-response research and finance/economics demonstrations.
Primary targets: ECONOVA-S™, CAM/KAM empirical research, financial NLP studies.
Note: respect upstream software license and Yahoo data-use terms.

### 4. Financial Sentiment / BERT / FinBERT → FinancialNLPAdapter
Repository: https://github.com/Saehon/Financial-Sentiment-Analysis-and-Classification-Deep-Learning-Models
Use: reference and replication methods for sentiment, uncertainty, tone and financial-text classification.
Primary targets: KIWI™, ECONOVA-S™, CAM/KAM and disclosure research.
Note: retain original article authorship and repository attribution.

### 5. fg-data-synthetic → SyntheticDataAdapter
Repository: https://github.com/Saehon/fg-data-synthetic
Use: synthetic tabular and time-series data for privacy-safe demonstrations, digital twins, audit simulations, rare-event stress tests and teaching.
Primary targets: KIWI™ Digital Twin, POMELO™ simulation, NAAIL education layer.

## Canonical architecture

External Source → Adapter → Schema Validation → Evidence Passport → Model/Agent Layer → Evaluation → Human Gate

## IP and license boundary
NAAIL original methods, orchestration, evaluation, evidence governance, scoring systems and professional-intelligence architecture remain separate from upstream projects. External code or models must not be relabeled as NAAIL inventions. Where practical, use package/API dependencies rather than vendoring entire upstream codebases.
