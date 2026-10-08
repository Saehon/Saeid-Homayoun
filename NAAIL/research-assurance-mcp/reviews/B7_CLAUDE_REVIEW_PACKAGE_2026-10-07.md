# B7 Claude review package — bounded stdio MCP server

Status: **OPERATOR COMPLETE / INDEPENDENT REVIEW REQUIRED**

## Scope

Draft PR #135 adds a Python stdio MCP transport around the six existing P5 functions. It does not change P5 assurance logic, retrieve research data, select cases, author benchmark probes, score evaluation data, or promote an assurance state.

## Git references

- Base: `main` at `d48faf52bd27a6796063f10b73657eb1d9cf384b`
- Branch: `naail/v1-b7-mcp-server-20261007-1114`
- Implementation/CI head: `c699510ef1ce31dd59beb40b4e510c735a0b5fb3`
- Draft PR: `https://github.com/Saehon/Saeid-Homayoun/pull/135`

## Review inventory

| File | Git blob | SHA-256 |
|---|---|---|
| `b7/naail_mcp_server.py` | `14be2a35aa54e9caa94d120271fbcb2ad8188fcc` | `f3414470bbb31fe51b95ba3fd3d5f855675f18db298179358276722e4b0b06d0` |
| `b7/tool_schemas.json` | `ebe8e9dcd4e0773c835894c81553a11b0e3e3a00` | `81c89b2ed59125f6d260f8f99b8a7ac23c2199a642497858a019415bdb15fb63` |
| `b7/test_b7_mcp_server.py` | `75c92d17e211512163e0bf3b8b7090e19db326ae` | `e8a007c819135acfbd58958a73419828e46a18a7a2a3ac7163cb3165ee38c1cf` |
| `b7/README.md` | `f1f2173ae8b0dad86dddc718fa4e6a1876dc8a6e` | `a822945ab5b44d8d8dddc40150f5672702db222a4cffb6e9ed28a121bb8371e0` |
| `derived/OPEN_REPAIR_QUEUE_B7.md` | `96ba25fbf7af320cf87deb28e80fba8f4fab9630` | `851c6010656486c683597ac09a75f58046e442688652722a62fd916a31ff3d13` |
| `.github/workflows/naail_b7_mcp_server.yml` | `1c08a128080f6e9ec703860c1d95d5dd26b58cef` | `03fe6a832e03590a8a00921b67422edb58270daf546b9123b4d9945487537fd1` |

## Transport behavior

- newline-delimited JSON-RPC 2.0 on stdin/stdout;
- MCP `initialize`, `notifications/initialized`, `tools/list`, and `tools/call`;
- explicit input/output schemas for `inspect_package`, `map_table_to_code`, `compare_reported_result`, `trace_provenance`, `score_detection`, and `generate_assurance_report`;
- pre-call input validation and post-call output validation;
- project-root confinement for package inspection;
- structured tool results plus a serialized text representation;
- bounded errors without traceback or research-data disclosure.

## Validation evidence

Local compile plus six unit tests exited 0. The test suite covers all six wrappers, invalid-schema rejection, unexpected-property rejection, project-path escape rejection, initialize/list/call behavior, notification behavior, and a subprocess stdio round trip.

Single authoritative CI:

- run: `37598645682`
- job: `112717303588`
- run number: `1`
- conclusion: `success`
- compile step: `success`
- six-test step: `success`

The workflow triggers only on the PR `opened` event for B7 paths. This review-package commit cannot trigger the B7 guard, and no rerun is authorized.

## Recorded repairs

1. Local validation initially lacked the existing P5 source in the scratch workspace. The failure was recorded before restoring the connector-readable live-main dependency; the materially different second attempt passed all tests.
2. The first GitHub upload orchestration lacked `atob` and failed before any file write. The raw-text sequential upload repaired it without recreating successful content.
3. The first RUN 034 Drive date chip used local midnight and rendered the prior UTC date. A range-local replacement used noon UTC; connector readback shows `Oct 7, 2026`. This affected only Drive presentation, not B7 code, CI, or scientific state.

## Independent review questions

1. Does the stdio/JSON-RPC surface satisfy the intended B7 skeleton boundary without overstating protocol completeness?
2. Are all six wrappers faithful to the existing P5 functions?
3. Are schema validation, finite-number checks, extra-property rejection, path confinement, and exception redaction adequate for this skeleton?
4. Does any response shape or tool description imply scientific validation or autonomous authority that the code does not possess?
5. Is the one-run CI design acceptable under the current governance rule?

## Gate effect

B7 is operator-complete and awaits independent review. This engineering result changes no POC scientific criterion, does not authorize Phase C, and does not change either completion flag.
