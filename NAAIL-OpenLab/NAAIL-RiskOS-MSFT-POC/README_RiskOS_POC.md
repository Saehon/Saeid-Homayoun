# NAAIL-RiskOS-MSFT-POC v0.2 — Multi-Agent Audit Risk Prototype

**Company:** Microsoft Corporation (FY2026)  
**Maturity:** RESEARCH_PROTOTYPE  
**Core audit-risk spine:** `AR = IR × CR × DR`

This version upgrades the earlier RiskOS dashboard into a deterministic, multi-agent proof of concept modeled after a modern professional conversational workspace.

## Agents

1. **RiskOS Orchestrator** — routes the case and composes the final state.
2. **Applicability Agent** — determines US GAAP/IFRS, CAM/KAM and jurisdiction boundaries.
3. **Inherent Risk Agent** — maps CAM/accounting judgment, business/financial pressure, disclosure, forensic/cyber/ESG inputs to IR.
4. **Control Risk Agent** — maps ICFR, ITGC, control design/operation and governance to CR.
5. **Detection Risk Agent** — maps procedure coverage, evidence sufficiency, sampling, model risk and review to DR.
6. **Evidence Agent** — checks Evidence Passport, source status and missing modules.
7. **Independent Challenger** — falsifies unsupported aggregation and claim boundaries.
8. **Human Gate** — permits research demonstration only and blocks production claims.

## Current illustrative output

- IR index: **0.6525**
- CR index: **0.3650**
- DR index: **0.3775**
- AR index: **0.0899**
- User-selected target AR index: **0.0500**
- Allowed DR index at that target: **0.2099**
- Current state: **MORE_AUDIT_ASSURANCE_REQUIRED**

These are **illustrative, uncalibrated normalized indices**, not literal probabilities or professional audit conclusions.

## Run

```bash
python run_poc.py
```

Run tests:

```bash
pytest -q test_risk_engine.py
```

## Files

- `naail_riskos_multiagent_msft_poc.html` — Claude-like interactive front end.
- `microsoft_case.json` — company evidence and transparent illustrative inputs.
- `risk_engine.py` — multi-agent engine and orchestration.
- `run_poc.py` — executes one full multi-agent review.
- `poc_run_result.json` — generated example output.
- `test_risk_engine.py` — basic invariants.
- `METHODOLOGY.md` — AR/IR/CR/DR formulation and NAAIL mapping.

## Scientific boundary

Research prototype only. No production approval, audit opinion, fraud determination, regulator finding, investment recommendation or calibrated audit-failure probability is claimed.
