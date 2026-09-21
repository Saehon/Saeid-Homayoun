# FRANKENSTEIN Portfolio Integration Map

| Portfolio asset | FRANKENSTEIN role | Current status |
|---|---|---|
| `Saehon/AAA` | Source/reference for Finance & Operations audit design; deterministic logic is independently ported here | Executable local port |
| `Saehon/IFRS-AI-Inspector` | standards-aware reporting and verification | Adapter boundary |
| `Saehon/AuditData-API` | audit-data ingestion and evidence APIs | Adapter boundary |
| Multi-Agent BERT repository | text classification and NLP risk signals | Adapter boundary |
| Financial Sentiment repository | narrative/disclosure signals | Adapter boundary |
| `Saehon/timesfm` | temporal forecasting and anomaly baselines | Adapter boundary |
| `Saehon/ganlab` | adversarial scenario generation | Adapter boundary |
| `Saehon/fg-data-synthetic` | synthetic audit/control populations | Adapter boundary |
| NAAIL OpenLab | governance home, evidence rules and Human Gate | Active governance |

An adapter is not represented as integrated until code, a data contract and a reproducible test demonstrate the connection.

Target normalized evidence record:

```text
evidence_id
source_system
source_reference
timestamp
test_or_model
observed_value
risk_signal
confidence_or_threshold
limitations
provenance
```
