# NAAIL AI Developer — Five Products × FT50 Research
One-page development decision | 10 October 2026 | Proposed, not deployed

## 1. EVIDENCEGATE — AUDIT AGENT EVALUATOR [START FIRST]
Product: provider-neutral OpenAI/Claude/Gemini MCP harness with evidence provenance, independent challenge and Human Gate.
Pilot: 120 synthetic/public accounting queries tested at three levels: direct tool, standalone agent, and product harness; score unsupported claims, factual pass rates, stability, latency and cost.
Empirical design: preregistered randomized human–AI auditor judgment experiment, evidence passport × independent challenger; power calculation based on pilot. FT50: The Accounting Review / Management Science.

## 2. LEMON-ICFR SENTINEL — PRE-DISCLOSURE RISK
Product: point-in-time SEC XBRL + narrative-based internal-control risk monitor; compare conventional ML with LLM and possibly TimesFM-3.
Pilot: 200 historical public filings; preserve availability dates and independent truth labels; report PR-AUC, calibration and missed material weaknesses.
Empirical design: firm-panel tests of subsequent ICFR disclosures, reporting correction and incremental market responses. FT50: Journal of Accounting Research / Journal of Accounting and Economics.

## 3. KIWI CAM COMPASS — AUDITOR ATTENTION
Product: seven-topic pre-report account-risk scores, CAM entry/persistence/exit and evidence trails.
Pilot: repair auditor-report dates and rerun existing 50-firm measurement checkpoint, with CAM text excluded from risk construction.
Empirical design: firm-year-topic models with auditor/year effects and temporal falsification; predict CAM reallocation, not just CAM count. FT50: The Accounting Review / Journal of Accounting Research.

## 4. AI CAPEX MARKET RADAR — FINANCIAL CONSEQUENCES
Product: SEC filing classifier distinguishing AI investment, operating expenditure, accounting changes and unsupported management rhetoric.
Pilot: hand-code 50 dated events with reconciled financial disclosures; link permitted public prices and Fama–French factors.
Empirical design: panel/event tests of verified AI investment vs earnings–cash-flow divergence and subsequent returns, controlling existing text signals. FT50: Journal of Financial Economics / Management Science (stretch).

## 5. TOKENCOST & CARBON TWIN — MANAGEMENT ACCOUNTING
Product: provider-neutral activity-based costing and carbon scenarios for token inference, compute, assurance and human review.
Pilot: 20 synthetic workloads, reconciled unit economics, sensitivity/scenario tests.
Empirical design: randomized manager choice experiment, token-only pricing vs full-cost/evidence dashboard; external firm validation needed. FT50: Management Science (stretch).

## Recommendation & Boundaries
Build EvidenceGate first; integrate it into the existing LEMON-ICFR workflow, then advance KIWI once its date-validation gate passes. Existing Decision-1 work has 18 synthetic/offline cases, not live model evidence. Drive is canonical; GitHub holds code/PRs; Kaggle/Hugging Face only public rights-cleared releases. No causal or significant-result claims without independent labels, time splits, preregistration, and credible identification. Targets are publication ambitions, not predictions.

## Selected Verifiable Anchors
OpenAI harness-aware plugin evals (2026): https://developers.openai.com/cookbook/examples/partners/harness_aware_plugin_evals/harness_aware_plugin_evals
Google Research AI and professional learning (2026): https://research.google/blog/does-better-work-always-mean-better-workers/
DeepMind AlphaEvolve (2025): https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/
Cohen et al. (2020), Journal of Finance: https://doi.org/10.1111/jofi.12885
Gu et al. (2020), Review of Financial Studies: https://doi.org/10.1093/rfs/hhaa009
Babina et al. (2024), Journal of Financial Economics: https://doi.org/10.1016/j.jfineco.2023.103745


**Canonical Google Drive folder:** https://drive.google.com/drive/folders/1Bt296IlFWL1aEuwfgNv5S3hgkdmefQW4

**Canonical one-page memo:** https://docs.google.com/document/d/1Ql_ns50UUrkhyTWL37LRCEoiS-jPzrAvtIHzwlPtoYQ/edit

**Status note:** This file documents product definitions and research protocols, not completed software, model runs, or publishable empirical findings. Existing ICFR/CAM prototypes are separate governed projects; do not merge them without review.
