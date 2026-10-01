# Case 001 — Author-Output Consistency Verification V0.1

## Reference
deHaan, de Kok, Matsumoto & Rodriguez-Vazquez (2023), *How Resilient Are Firms’ Financial Reporting Processes?*, Management Science 69(4), 2536–2545. DOI: 10.1287/mnsc.2023.4670.

## Scope
This verification compares the published article against author-provided replication artifacts. It is **not** an independent end-to-end reproduction from raw licensed data.

## Evidence used
- Published article PDF: `EBSCO-FullText-2026-10-01.pdf`
- Main Stata log: `3_output/logs/c_2a_run_regressions_main.smcl`
- Main Stata code: `1_code/c_2a_run_regressions_main.do`
- Python narrative-statistics notebook: `1_code/c_3_generate_narrative_statistics.ipynb`

## Main result
**264 / 264 published regression cells checked matched the author-provided Stata output at the article's published precision.**

Coverage:
- Table 2 Panels B and C
- Table 3 Panels A and B
- Table 4 Panels A, B and C
- Table 5 Panels B, C and D

For each applicable model the check covers coefficient(s), t-statistic(s), observations, and adjusted R². Table 5D additionally checks UE, Post, and UE×Post coefficients and t-statistics.

## Descriptive panels
Stored author outputs are also consistent with:
- Table 1 Panel A — descriptive statistics
- Table 1 Panel B — economic-event means
- Table 1 Panel C — filing-characteristic results in the stored Python notebook
- Table 2 Panel A — late-filer counts/rates
- Table 2 Panel D — Q1-2020 late-filer characteristics
- Table 4 Panel D — Q1-2020 large-EA-delay characteristics
- Table 5 Panel A — reporting-quality averages

## Important correction
The uploaded replication package **does contain the expected Stata/SAS logs under `3_output/logs`**. Earlier public-tree inspection did not expose those files. The uploaded replication package resolves that issue.

## Assurance classification
| Dimension | Status |
|---|---|
| Table-to-code structural mapping | **VERIFIED** |
| Published table ↔ author output consistency | **VERIFIED** |
| Author-provided code/log provenance | **CONSISTENT** |
| Independent end-to-end reproduction | **PARTIAL** |
| Methodological validity | **HUMAN_REVIEW** |

## Why FULL_REPRODUCTION is not claimed
Several source datasets are external/licensed. Matching published tables to author-provided logs does not establish that an independent party can regenerate those logs from raw source data without required data access and environment.

## Interpretation
This establishes that the checked published regression values are internally consistent with author-provided computational output. It does **not** establish independent reproduction from raw data, correctness of every upstream transformation, methodological/causal validity, or absence of untested errors.

**Current Case 001 state: AUTHOR_OUTPUT_CONSISTENCY_VERIFIED / FULL_REPRODUCTION_PARTIAL.**
