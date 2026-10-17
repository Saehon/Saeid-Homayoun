# TAR empirical completion protocol (2026-10-11)

## Status
The accompanying 400-case demonstration is **synthetic**. No practicing auditors, firm-year records, or causal treatment effects were observed. Do not label the manuscript submission-ready.

## Core experimental design
Randomly assign practicing auditors or advanced audit trainees to:
1. Conventional LLM answer (baseline).
2. LLM answer with linked citations.
3. Evidence-governed agent with provenance, rights, COSO mapping, independent challenge, falsification, reproducibility and mandatory human approval.

Cross-randomize ICFR evidence conflict and weakness severity. Preregister primary outcome: fraction of unsupported recommendations accepted. Secondary outcomes: correct material-weakness classification, contradictions detected, confidence calibration, completion time, false-rejection rate. Expert reviewers should be blinded to treatment. Report sample-size power calculations before recruitment, attrition, balance, ITT effects, clustered uncertainty and multiple-testing corrections.

## Archival extension
Build reproducible firm-year data from SEC EDGAR 10-K/10-K-A and publicly available audit opinions, with clearly defined ICFR weaknesses, filing lag, subsequent remediation and restatements. Document accession IDs, amendments, fiscal years, CIK mapping, missingness and outcome timing. Archival associations do not identify causal effects of agent adoption.

## Research integrity
- Do not reuse synthetic results as empirical evidence.
- Verify FT50 references, exact article titles, DOIs, licenses and access conditions.
- No real-person simulations treated as human participants.
- Retain original code, data provenance, versions, and reviewer dispositions.
- The GitHub pull request must be reviewed before merging to protected main.

## Repository source
Lemon-ICFR-US/src/lemon_icfr/orchestrator.py (public main branch inspected 2026-10-11).
