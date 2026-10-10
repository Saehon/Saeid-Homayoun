# Paper2Agent / NAAIL — Stage Completion Register
**Last design update:** 2026-10-10. Status is evidence-based; completed software tasks are not empirical findings.

| Stage | Deliverable | Evidence | State |
|---|---|---|---|
| S0 | GitHub branch, draft PR, dedicated Google Drive Paper2Agent archive | PR #164 + canonical Drive folder | DONE |
| S1 | Literature/source inspection: Nature Paper2Agent; Bao JAR; PCAOB AS 3101 | Source and rights manifest | DONE FOR TARGETS; NOT SYSTEMATIC REVIEW |
| S2 | Synthetic A0/A1/A2/A3 software architecture | pilot.py and test_pilot.py | IMPLEMENTED |
| S3 | Local read-only MCP protocol server (initialize/list/call) | mcp_server.py + black-box tests | IMPLEMENTED; NOT HOSTED |
| S4 | Actual integration with mother Lemon and CAM benchmark code | integrated_case.py + integration tests | SYNTHETIC INTEGRATION |
| S5 | Paper/author repo original-code verification gateway | bao_replication_gateway.py + git blob hashes | GATE IMPLEMENTED |
| S6 | Corrected Bao MATLAB replication on authorized real labels | Matlab + author dataset, correction and table reconciliation | BLOCKED: ENVIRONMENT/RIGHTS/DATA |
| S7 | Historical SEC/PCAOB/AAER + ICFR/CAM empirical panel | point-in-time source rights and positive/negative outcome labels | NOT DONE |
| S8 | Preregistered real-data A0–A3/effect estimations | honest holdout/independent verifier | NOT DONE |
| S9 | External expert-auditor trial, scientific falsification and independent replication | signed protocols + blind labels | NOT DONE |
| S10 | Manuscript for JAR/TAR with statistical results | manuscript after S6–S9 | OUTLINE ONLY |
| S11 | Remote MCP deployment / multi-provider Co-Scientist or actual DeepMind AlphaEvolve | provider credentials, hosting, safety review | NOT DONE |

## Engineering acceptance tests
- All `test_*.py` pass in GitHub Actions, and Human Gate assertions remain locked.
- MCP tool call `get_paper_method` returns honest original-code status.
- MCP rejects unknown company identifiers, unexpected parameters and non-whitelisted tool execution.
- Integrated pipeline uses mother repository Lemon and CAM actual imported modules.
- Original Bao reproduction is blocked unless rights, author code SHA, label file and MATLAB are present.
- Do not merge PR before documented human scientific/IP review.

## Deliverables/storage
Google Drive: https://drive.google.com/drive/folders/1iXOWJSYIZFhiXZReULHcp9ajatdSaUAB
GitHub: https://github.com/Saehon/Saeid-Homayoun/pull/164
Legacy master index: https://docs.google.com/document/d/1mA139KFjQX-QVFdaSK-RU96MNFOFuzfmDgLZnDd5OyU/edit
Cross-platform mirrors (Kaggle/Hugging Face) not published; do not imply public dataset packages exist.
