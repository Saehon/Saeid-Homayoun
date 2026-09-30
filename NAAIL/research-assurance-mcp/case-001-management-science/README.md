# NAAIL Research Assurance MCP — Case 001

Reference: deHaan, de Kok, Matsumoto & Rodriguez-Vazquez, "How Resilient Are Firms' Financial Reporting Processes?", Management Science (2023), DOI 10.1287/mnsc.2023.4670.

Purpose: validate Manuscript -> Claim -> Table -> Output -> Code -> Data -> Provenance.

The authors' package uses Python, SAS and Stata. Raw licensed data are not copied into NAAIL. The original source remains immutable; controlled errors are applied only to fixtures/copies.

Assurance states: VERIFIED, CONSISTENT, PARTIAL, FLAGGED, HUMAN_REVIEW.

V0.1 tools: inspect_replication_package; map_table_to_code; parse_stata_log; parse_sas_log; compare_reported_result; check_method_code_consistency; trace_result_provenance; inject_controlled_error; score_detection; generate_assurance_report.
