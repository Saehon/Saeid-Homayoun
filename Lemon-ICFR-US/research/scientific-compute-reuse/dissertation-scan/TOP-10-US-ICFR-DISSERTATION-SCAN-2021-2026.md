# ICFR Doctoral Dissertation Scan — Leading U.S. Accounting PhD Programs (2021–2026)

Status: INITIAL_OPEN_REPOSITORY_PASS
Scan date: 2026-09-29
Scope: dissertations from 2021–2026 with direct or material relevance to ICFR, SOX 404, material weaknesses, financial-reporting process controls, or internal-control audit mechanisms.

## Screening set
This is an operational set of ten leading U.S. accounting/business doctoral programs, not a claim of a single official ranking:
Chicago Booth; Wharton; Stanford GSB; Harvard Business School; MIT Sloan; Columbia Business School; NYU Stern; Michigan Ross; Texas McCombs; UNC Kenan-Flagler.

## Screening results

| University | Candidate | Year | Dissertation | ICFR relevance | Open dissertation/table access | Decision |
|---|---|---:|---|---|---|---|
| Chicago Booth | Maria Alexandra Khrakovsky | 2025 | Disrupting Consistency in Accounting | HIGH: material weaknesses are embedded in error/accounting-change outcomes; direct and spillover tests concern financial-reporting-process disruption | Repository PDF/indexed tables available | ADMIT — dissertation evidence layer |
| Wharton | Irina Luneva | 2024 | Explaining Debt Covenant Amendments: A Structural Approach | LOW: cites ICW literature but ICFR is not the focal construct | Open dissertation | EXCLUDE from ICFR thesis core |
| Stanford GSB | — | 2021–2026 | No direct qualifying open-repository hit in initial pass | — | — | CONTINUE SEARCH |
| Harvard Business School | — | 2021–2026 | No direct qualifying open-repository hit in initial pass | — | — | CONTINUE SEARCH |
| MIT Sloan | — | 2021–2026 | No direct qualifying dissertation hit in initial pass | Adjacent MIT working papers exist | — | CONTINUE SEARCH |
| Columbia Business School | Anthony Le | 2026 | Accounting Rules and the Labor Market for Accountants | LOW/BOUNDARY: accountant supply can affect ICFR but ICFR is not focal | Published dissertation-based paper available | EXCLUDE from ICFR thesis core |
| NYU Stern | — | 2021–2026 | No direct qualifying dissertation hit in initial pass | Direct ICFR working papers exist but are not dissertations | — | CONTINUE SEARCH |
| Michigan Ross | — | 2021–2026 | No direct qualifying open-repository hit in initial pass | — | — | CONTINUE SEARCH |
| Texas McCombs | — | 2021–2026 | No direct qualifying open-repository hit in initial pass | — | — | CONTINUE SEARCH |
| UNC Kenan-Flagler | — | 2021–2026 | No direct qualifying open-repository hit in initial pass | — | — | CONTINUE SEARCH |

## Admitted dissertation extraction — Khrakovsky (Chicago Booth, 2025)

### Research setting
The dissertation examines whether implementation of major accounting standards disrupts established accounting routines and leads firms to disclose errors and update legacy accounting policies before adoption.

### ICFR-relevant outcome construction
The dissertation defines accounting changes/errors to include:
- restatements;
- out-of-period adjustments;
- material weaknesses in internal controls;
- material changes in accounting estimates;
- changes in accounting principles;
- material impairments.

The Error Disclosure indicator includes restatements, out-of-period adjustments, and material weaknesses in internal controls.

### Core model
For standard s in {Revenue Recognition, Leases}, the direct-effect specification is an OLS design of the form:

AccountingChange_{fqt}^s = firm FE + firm-quarter/fiscal-quarter/topic FE + DirectlyTreated_t^s + IMPL_{fq}^s + DirectlyTreated_t^s × IMPL_{fq}^s + controls + error.

### Table-extraction matrix

| Dissertation table | Outcome | Key treatment | Key reported effect | FE / design | LEMON-SCI use |
|---|---|---|---|---|---|
| Table 3 | Descriptive firm variables | Standard implementation exposure | Revenue-recognition sample includes 3,689 firms for implementation-period variables; complexity and IT-investment measures reported | Descriptive | data/variable passport |
| Table 4 | Accounting Change / Disclosure of Error / Update to Legacy Policies | Directly Treated × IMPL | Revenue-recognition interaction: 0.009 for Accounting Change; 0.003 for Disclosure of Error; 0.007 for policy update, each reported significant at 1% | OLS with firm or firm-quarter plus topic/time FE | direct disruption model |
| Table 5 | Same three outcomes | Adjacently Treated × IMPL | Revenue-recognition spillover interaction: 0.012 for Accounting Change; 0.002 for Disclosure of Error; 0.011 for policy update | OLS with controls and FE | spillover / cross-account mechanism |
| Appendix B | Variable definitions | — | Material weakness explicitly included in Any Change and Error Disclosure constructs | ontology | variable mapping |
| Table 14 | Update Firm Indicator | lagged firm characteristics | Log assets +; ROA −; revenues +; returns −; Amihud −; share turnover − | Logistic regression, 40,381 observations | matching/admissibility benchmark |

## Boundary dissertations outside the strict 2021–2026 window
These are scientifically relevant but excluded from the five-year core:
- Lisa Yao Liu, University of Chicago, 2020, Do Auditors Help Prevent Data Breaches? — direct internal-control/audit-IT mechanism; later became a Management Science paper.
- Steven A. Mitsuda, Stanford, 2020, The Effect of Chief Accounting Officers on Financial Reporting Quality — uses internal control weaknesses as a financial-reporting-quality outcome.

## Extension candidates outside the ten-school screen
High-relevance recent dissertations found during discovery and worth a second-layer corpus:
- Eric Gelsomin, Boston College, 2022 — Accounting Standards Updates, Investments in Accounting Information Systems, and Firms’ Internal Information Environments. Uses SOX 302 control-change disclosures and studies information-system investment/control effects.
- Shuo Li, Singapore Management University, 2024 — Accounting Function Hierarchies and Financial Reporting Quality. Finds accounting-function hierarchy associated with fewer internal-control weaknesses.
- Ying Zhang, Syracuse University, 2022 — A More Efficient and Effective Objective Measure of Financial Disclosure Quality. Explicitly tests ICWs and restatements.
- Sang Woo Sohn, Emory University, 2023 — CEO-Employee Political Alignment and Financial Reporting Outcomes. Includes internal-control weaknesses and restatements as outcomes.

## Governance
1. A dissertation enters the ICFR thesis core only if ICFR/material weakness/control quality is an outcome, treatment, mechanism, or material model input.
2. Mere citation of ICFR literature is insufficient.
3. Exact regression tables are converted into machine-readable model passports only when the full thesis/table is accessible.
4. Dissertation evidence remains separate from peer-reviewed M1 until publication/provenance status is established.
5. No coefficients are promoted to M1 without primary-source verification and human approval.
