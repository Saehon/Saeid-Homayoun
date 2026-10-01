# LEMON-SCI Hourly Build Log

Append-only GitHub-side master log for hourly execution evidence.

## Setup record — hourly dual-save logging architecture

- Project: LEMON-SCI / Lemon-ICFR-US
- Authorized branch: `feature/lemon-scientific-compute-reuse`
- Pull request: #76
- Starting HEAD before logging setup: `1efa1e0892619fdd9121441b968e094801e68daf`
- Google Drive folder: `LEMON-SCI — Hourly Build Logs`
- Google Drive folder ID: `1n1B5d772wwgSjcIvWiZ5DCd18y4GVHZ_`
- Google Drive master document: `LEMON-SCI — Hourly Build Master Log`
- Google Drive master document ID: `1SmPAF0G_6hx_mEFzO0VenifSKNYLRv7fdD3pPvlAzaY`
- GitHub protocol: `hourly-build/README.md`
- GitHub schema: `hourly-build/hourly-run.schema.json`
- Required sequence: **15-minute work → GitHub save → Drive save → readback verification → next hour**
- DUAL_SAVE_STATUS vocabulary: `PASS | PARTIAL | BLOCKED`
- ACK2007: retired from active benchmark path; historical provenance preserved.
- Blocker policy: progress-first; LOCAL blockers enter OPEN REPAIR QUEUE and do not stop the overall build.
