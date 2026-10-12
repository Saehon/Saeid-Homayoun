# Companies' annual reports — CAM/KAM AuditBERT data-source statement
**Date:** 12 October 2026  
**Status:** Research-owner clarification; source retesting not requested.

## Correct source attribution

The research owner confirmed:
- The CAM/KAM dataset was assembled **from companies' annual reports**.
- SEC EDGAR is a route to obtain annual reports/filings where applicable.
- The observations were organized into a **standardized tabular research format**.

**Project source attribution:** Companies' annual reports. Dataset fields describe the research structure rather than a source provider.

The project may proceed using this source statement. **No additional record-by-record investigation of data origin is required by the project owner.** This statement is not equivalent to an assertion that such an investigation was performed.

## Research tasks that remain necessary

These are **empirical model-design and reproducibility checks**, not challenges to the source statement:

1. Construct the correct historical report-year/company-year panel; use dates in the annual reports or an already available year mapping rather than interpreting contemporary financial snapshots as report dates.
2. Resolve the documented 65,535-row truncated KAM input versus the 86,122-row extract.
3. Reconcile the 48-topic abstract claim against the 49 topic classes in the training notebooks.
4. Establish a consistent unit of observation and treatment of amended reports, repeated opinions and multiple matters per issuer-year.
5. Revoke/sanitize the six reported hard-coded Hugging Face tokens before publicly publishing the source notebooks.
6. Produce transparent empirical estimators, robustness checks, code, and tables; do not claim regression evidence until it is generated.

## Storage and sharing

Google Drive is the canonical archive for the datasets, manuscripts and versions. Public GitHub contains documentation and reproducibility code. Any decision to republish annual-report texts or aggregated data should consider the rights and contents of the particular material; publicly accessible annual reports do not make every possible redistribution automatically permissible.

**No independent source-origin audit is being requested or represented by this note.**
