# OPEN REPAIR QUEUE — B7 branch-local additive record

## NAAIL-B7-LOCAL-DEPENDENCY-001 — REPAIRED

- UTC: 2026-10-07T09:10:00Z
- Item: B7 local compile and unit test.
- Exact command: `python -m py_compile NAAIL/research-assurance-mcp/b7/naail_mcp_server.py NAAIL/research-assurance-mcp/b7/test_b7_mcp_server.py && python NAAIL/research-assurance-mcp/b7/test_b7_mcp_server.py`
- Exact error: `ModuleNotFoundError: No module named 'naail_mcp_poc'` while importing the existing P5 core; no B7 unit test executed.
- Likely root cause: the transient scratch workspace contained the new B7 files but not the upstream live-main P5 dependency.
- Attempted repair: none before recording this failure.
- Affected dependencies: local validation only. GitHub main contains P5 blob `163ddd476238b07ac9024759069767b8cdb32fe9`; no scientific evidence or assurance state was affected.
- Materially different repair: restored the connector-readable live-main P5 source in the local workspace and ran `git hash-object NAAIL/research-assurance-mcp/p5/naail_mcp_poc.py && python -m py_compile NAAIL/research-assurance-mcp/b7/naail_mcp_server.py NAAIL/research-assurance-mcp/b7/test_b7_mcp_server.py && python NAAIL/research-assurance-mcp/b7/test_b7_mcp_server.py` once.
- Resolution evidence: exit code 0; six B7 unit tests passed, including stdio initialize/list/call, schema rejection, path confinement, and all six P5 wrappers. The local connector-rendered P5 file hashed as Git blob `fded7c331aed0c3064cacf559feb242b45d65234`; live GitHub main remains authoritative at blob `163ddd476238b07ac9024759069767b8cdb32fe9` and will be used by branch/CI.
- Future action if the repair fails in CI: record the authoritative CI failure once and repair the B7 import boundary without changing P5 assurance logic; never rerun the failed CI to select a result.

## NAAIL-B7-GITHUB-UPLOAD-001 — REPAIRED

- UTC: 2026-10-07T09:16:00Z
- Item: upload the six prepared B7 files to branch `naail/v1-b7-mcp-server-20261007-1114`.
- Exact failed action: read each local file with `base64 -w0`, decode in the orchestration isolate with `atob`, then call GitHub `create_file` sequentially.
- Exact error: `ReferenceError: atob is not defined` before the first GitHub `create_file` call.
- Likely root cause: the orchestration isolate does not expose the browser `atob` global.
- Attempted repair: none before recording; the branch exists at the unchanged main base and contains no B7 file from this attempt.
- Affected dependencies: GitHub save only; local compile and six unit tests remain PASS. No CI was triggered and no scientific state changed.
- Next materially different repair: read each UTF-8 file directly through a bounded shell output and pass the returned text to sequential GitHub `create_file` calls without base64 decoding.
- Resolution evidence: the materially different raw-text path created all six B7 files sequentially; branch head after the workflow file was `d2326cb3f02c8409445aad345ee08aa25585f196`.
- Future action if a readback fails: fetch only the affected branch file and compare its Git blob/content; do not recreate successful files or open an overlapping PR.

## NAAIL-B7-DRIVE-DATE-CHIP-001 — REPAIRED

- UTC: 2026-10-07T09:13:00Z
- Item: RUN 034 semantic date in the Drive master log.
- Persistent failure count: 1 of 2.
- Exact failed write: `insertDate` at index `42970` with timestamp `2026-10-07T00:00:00+02:00`, locale `en`, date format `DATE_FORMAT_MONTH_DAY_YEAR_ABBREVIATED`, and time disabled.
- Exact readback defect: the provider normalized the timestamp to `2026-10-06T22:00:00Z` and rendered `Oct 6, 2026`.
- Likely root cause: a midnight local timestamp crossed the UTC date boundary before the date-only display was resolved.
- Materially different repair: delete only the date-element range `42970:42971` at the live revision, then insert a noon UTC timestamp `2026-10-07T12:00:00Z` at the same index.
- Resolution evidence: connector readback at revision `ANLCKQlzYXaTI0tvGOX8Rosp_i5x80mw8IdUAhEjfpUJw1t_Bh1ZUiICACZWU6A8fbV6WPcYQEtRra5fOVaFhkdg5Rduq_uGMy3KrvlOug0` reports `dateCount = 10`, last date range `42970:42971`, and display text `Oct 7, 2026`.
- Affected dependencies: Drive presentation of the RUN 034 date only; GitHub artifacts, CI, scientific states, and run text were unaffected.
- Future action if a date-only chip is needed: use a noon UTC timestamp and verify the connector-visible display text before claiming readback success.
