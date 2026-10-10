# NAAIL Audit Scientific Discovery — Paper2Agent × Co-Scientist × AlphaEvolve
**Status: DEMO / research infrastructure, not verified empirical evidence.**  
**Created:** 2026-10-10. **Maintainer:** Saeid Homayoun.  
**Canonical Paper2Agent Drive folder:** https://drive.google.com/drive/folders/1iXOWJSYIZFhiXZReULHcp9ajatdSaUAB

## What was actually built
A dependency-free, executable *synthetic* architecture benchmark comparing:
- **A0:** frozen illustrative risk heuristic (NOT Bao's RUSBoost implementation).
- **A1:** identical predictor with provenance / evidence review gate.
- **A2:** Co-Scientist-*inspired* competing-model tournament, chosen on training only.
- **A3:** bounded AlphaEvolve-*inspired* parameter search chosen on a fixed validation split.

This demonstrates a governed workflow with a **local read-only MCP stdio server** and real module-level integration to existing Lemon and CAM toy pipelines, **not** the upstream full Paper2Agent host conversion, real Google Co-Scientist, DeepMind AlphaEvolve, hosted MCP deployment, live external LLM use, professional fraud detection, or reproduction of Bao's model. No claims of A3 superiority are warranted from synthetic observations.

## Run
```bash
cd NAAIL-OpenLab/research/audit-scientific-discovery-paper2agent
python pilot.py --demo --out results/pilot_results.json
python -m unittest discover -v -p 'test_*.py'
```
Python 3.10+; standard library only. The output contains temporal splits, candidate lineage, holdout metrics, evidence coverage, high-risk/no-CAM research triage, and Human Gate status. Expected cohort sizes: train 50 (2018–22), validation 10 (2023), test 20 (2024–25).

## External data interface (not automatically certified)
```bash
python pilot.py --csv /authorized/path/to/firm_year.csv --out results/external_unverified.json
```
CSV fields: `case_id, year, revenue_growth, accrual_ratio, control_exception, cam_present, fraud_label, evidence_id, evidence_complete`. Ratios are normalized to [0,1], binary fields are 0/1. Caller must verify genuine ground truth, date availability, PCAOB applicability, SEC provenance, legally permitted use, and feature validity before scientific interpretation. Do not substitute a clean ICFR opinion as a fraud label.

## Original research / reproducibility anchors
1. Bao, Y., Ke, B., Li, B., Yu, Y. J., & Zhang, J. (2020). *Detecting Accounting Fraud in Publicly Traded U.S. Firms Using a Machine Learning Approach*. **Journal of Accounting Research**. https://doi.org/10.1111/1475-679X.12292 ; authors' code: https://github.com/JarFraud/FraudDetection ; examine its 2022 correction: https://doi.org/10.1111/1475-679X.12454.
2. Burke et al. (2023), *The Accounting Review*: expected CAM and disclosure alignment; exact measures must be independently checked before implementation.
3. Miao et al. (2026), *Nature*, *Reimagining research papers as interactive and reliable AI agents*. https://doi.org/10.1038/s41586-026-11044-y ; Paper2Agent: https://github.com/jmiao24/Paper2Agent.
4. Existing NAAIL components: `Lemon-ICFR-US`, `Apple-CAM-US`, `NAAIL-OpenLab/agents/pcaob`, `NAAIL-OpenLab/benchmarks/ft50_abs4`, and ECONOVA-S `poc/`.

## Roadmap / mandatory gates
- **G0 (this change):** independent synthetic A0–A3 benchmark + reproducibility smoke tests.
- **G1:** verify author licenses / commit hashes; run corrected Bao MATLAB RUSBoost with *authorized* underlying data; compare published metrics and document failures.
- **G2:** build point-in-time SEC/PCAOB fraud, CAM and ICFR panel; keep CAM text out of *pre-report* risk construction; document horizon, controls and case labels.
- **G3:** adapters to existing Lemon, Apple-CAM, PCAOB and ECONOVA-S interfaces, replacing illustrative calculations; genuine agent logs and decision traces.
- **G4:** run a registered model/agent study with train/validation/test separation, uncertainty and confidence calibration, expert labels, falsification and independent replication.
- **G5:** optional Paper2Agent MCP interface with read-only tools `get_method`, `run_replication`, `run_sensitivity`, `get_evidence_passport` behind rights and human-approval gates.
- **G6:** scientific manuscript preparation only after verified real-data results; no guaranteed FT50 publication.

## Governance
No autonomous audit opinion, regulator assessment, material-weakness conclusion, or approval. Synthetic cohort only. A high-risk/no-CAM flag is **not** evidence of audit failure; AS 3101 CAM criteria are more specific. Do not copy third-party code into NAAIL without license review. No private POMELO logic or confidential audit evidence. Only model-specification adaptation with frozen scientific fitness, full rejected-candidate trace and sealed final test data.

**Owner's goal:** build an evidence-governed, falsifiable, reproducible auditing scientific-agent platform; not merely a paper chatbot.

## Read-only paper-agent tool interface (not deployed MCP)
```bash
python paper_tools.py --tool list_tools
python paper_tools.py --tool get_paper_method
python paper_tools.py --tool run_architecture_benchmark
python paper_tools.py --tool inspect_synthetic_case --case-id SYN-2024-00
```
`paper_tools.py` exposes functions suitable for a *future* verified MCP adapter. It currently performs no RAG, web retrieval, external LLM call or real-money audit. Tests are in `test_paper_tools.py`.

## Updated implementation — executable components
- `mcp_server.py`, `test_mcp_server.py`: local JSON-RPC MCP stdio server with initialize, tools/list, tools/call, ping; four bounded read-only tools, strict synthetic-only input and security tests.
- `integrated_case.py`, `test_integrated_case.py`: **real Python module imports** from the existing `Lemon-ICFR-US/src/lemon_icfr/orchestrator.py` and `NAAIL-OpenLab/demos/cam-kam-agent-benchmark/benchmark.py` on artificial evidence; human gate intentionally blocks approval.
- `bao_replication_gateway.py`, `test_bao_replication_gateway.py`: verifies published MATLAB author files against pinned Git blobs; produces blocked or executed-pending-verification status; never copies author dataset to GitHub.
- `USAGE.md`: MCP server setup.
- `DATA_RIGHTS_AND_REPLICATION.md`: pinned original author sources and correction/data provenance.
- `STAGE_GATES.md`: every engineering and scientific stage, accurate blockers.
- `MANUSCRIPT_OUTLINE.md`: preliminary research framing, no fabricated findings.

**Operational verification:** GitHub Actions runs all `test_*.py`; successful software tests are not independent scientific replication. The canonical Google Drive Paper2Agent folder includes the linked master index and separate source, usage, stage-gate and manuscript Docs.

**Important:** The origin of paper2agent is Nature/Miao et al. (2026). Local NAAIL server is an independently authored, safer subset inspired by the original and is not described as the upstream package.
