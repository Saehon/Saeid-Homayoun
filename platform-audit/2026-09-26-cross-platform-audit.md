# Cross-Platform Engineering Audit — 2026-09-26

Non-destructive audit. No repositories, datasets, models, issues, or historical evidence were deleted.

## GitHub triage
Open work requiring engineering attention:
- Saeid-Homayoun PR #59: benchmark smoke runner lacked expected-value assertions. Patched on its existing branch so metric regressions now fail.
- pomelo-core PR #12: release readiness can be reported without actually evaluating all gates; Blind Gold handling conflicts with restricted-vault design; run-id collision can overwrite frozen evidence.
- pomelo-core PR #41: standard-title parser can greedily join multiple standards; release artifact can be emitted while post-gate findings remain.
- pomelo-core PR #22: compatible multi-label standards can be rejected as ambiguity; treatment-safe schema can admit Gold-derived fields.
- pomelo-core PR #24: machine-readable GraphRAG contract lacks required relationship vocabulary.
- pomelo-core PR #20: reported test count/revision and execution chronology need reconciliation; Gold commitment exists while external Gold payload is the missing item.
- IFRS-PCAOB-AI PR #2: promotion thresholds are weaker than locked holdout protocol; candidate identity is not bound strongly enough; sealed scoring/human approval/non-finite metrics need fail-closed validation.
- IFRS-PCAOB-AI PR #1: release gates need enforceable true booleans; agent manifests need required fields; PCAOB finding contract needs normalization/alignment.

These are not auto-closed: several are scientific/professional gates and require evidence after code repair.

## Hugging Face cross-link
Public profile: https://huggingface.co/SADHON
Observed public inventory: 0 public models, 10 datasets, 3 Spaces, 1 bucket.
Current datasets include:
- kimi-deepseek-accounting-finance-audit
- accounting-finance-audit-open-registry
- github-public-research-data
- aws-free-accounting-audit-finance-registry
- NAAIL-OpenLab
- sec-10-company-cam-icfr-governance-esg
- taming-modern-prometheus-assurance
- sec-10-company-accounting-panel
- frankenstein-phase4-accounting-audit-benchmark
- microsoft-accounting-demo

Known data-quality issue: sec-10-company-accounting-panel currently has a DatasetGenerationCastError because CSV files expose inconsistent schemas. Preserve the files; fix by separating configurations or harmonizing schemas in a future HF write-enabled session.

## Kaggle
No authenticated Kaggle write connector is available in this session. Do not claim synchronization. GitHub remains the canonical provenance hub until Kaggle publishing is authenticated.

## Cross-platform rule
GitHub = canonical code/provenance.
Hugging Face = eligible datasets/models/Spaces.
Kaggle = eligible datasets/notebooks/benchmarks.
Google Drive = controlled documentation/snapshot.

Never mirror an external artifact without checking license and redistribution rights. Every mirror should retain canonical source URL, owner, license, version/date, research purpose, and redistribution status.

## Notification policy
Do not create repetitive bot comments merely to retrigger reviews. Resolve substantive review findings in code/evidence first. GitHub supports configuring Actions notifications to failed workflows only; account-level notification settings should be changed by the account owner if desired.

## Next engineering queue
P0: fail-closed promotion/evaluation gates in IFRS-PCAOB-AI and pomelo-core.
P1: reconcile PR #20 empirical report with exact commit/test suite.
P1: repair HF sec-10-company-accounting-panel schema without deleting source files.
P2: establish authenticated Kaggle publishing and cross-link metadata.
