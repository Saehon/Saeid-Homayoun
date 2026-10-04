# Run 069 — COSO POC freeze-readiness evidence pack

This is a project-local readiness checklist for the Park et al. (2021) COSO noncompliance POC. It is not the shared portfolio table and does not constitute human approval.

| Gate | Status | Evidence |
|---|---|---|
| FR-01 Paper-defined construct recovered | MET | Run 061 primary-archive review: post-2014-12-15 COSO 1992 maps to Noncompliance=1 |
| FR-02 Two-sided public-company evidence | MET | Microsoft FY2015 COSO 2013 and National Instruments FY2015 COSO 1992 filings |
| FR-03 Machine-readable benchmark specification | MET | `benchmark-spec.json` blob `4b1930f6547ec4be5f2329782a395797633c56ff` |
| FR-04 Persisted classifier and base tests | MET | classifier blob `8f9def9dad81f78c80a8030072eea11c61016cec`; base-test blob `7c007450550c0cce744cc41cdf37ee1329bff4ad` |
| FR-05 Baseline/mutation executable evidence | MET | Run 067: both persisted suites exited 0 locally; no CI claim |
| FR-06 Temporal applicability enforced | NOT_MET | F-067-01: classifier lacks `period_end`; repair is `BLOCKED_AFTER_2_ATTEMPTS` |
| FR-07 Evidence scope fails closed | NOT_MET | F-068-01: four negative contexts were falsely classified |
| FR-08 Repair contract and adversarial catalog | MET | `evidence-input-contract-v0.1.json` and 16-case `adversarial-case-catalog-v0.1.json` persisted/read back |
| FR-09 Repaired implementation passes catalog twice | NOT_MET | Design cases are not yet wired to a repaired classifier |
| FR-10 Exact-head CI | NOT_MET | No workflow runs or combined statuses observed for current COSO commits |
| FR-11 Independent review closes blocking findings | PARTIAL | Independent Codex review completed; F-067-01 and F-068-01 remain open |
| FR-12 Human POC baseline freeze | NOT_MET | No human approval; `POC_V1_STATUS=NOT_FROZEN` |

Verified count for this checklist: **6 MET / 1 PARTIAL / 5 NOT_MET**.

## Run 069 artifacts

- `evidence-input-contract-v0.1.json`: section-bounded, provenance-preserving input contract with 10 fail-closed reasons.
- `adversarial-case-catalog-v0.1.json`: 16 unique cases; 3 expected classifications and 13 expected fail-closed outcomes.
- Both JSON artifacts passed structural readback checks: every required contract field is defined, all 16 case IDs are unique, and acceptance count equals catalog count.

## Repair-sweep entry criteria

The dedicated repair sweep may reopen F-067-01 only by explicitly recording that reason. The repair must implement the evidence contract, preserve the full two-failure history, and add the 16 cases as executable tests. Promotion requires 16/16 twice at one exact HEAD, deterministic output, exact-head CI, fresh independent review, and explicit human approval.

## Current decision

`ENGINEERING_STATUS=PARTIAL`  
`SCIENTIFIC_STATUS=PARTIAL`  
`GATE_STATUS=HOLD`  
`CODEX_STATUS=FINDINGS_OPEN`  
`POC_V1_STATUS=NOT_FROZEN`
