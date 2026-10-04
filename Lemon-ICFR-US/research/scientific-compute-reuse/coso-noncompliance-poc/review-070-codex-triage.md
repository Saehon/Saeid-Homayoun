# Run 070 post-Codex triage

Observed at 2026-10-04T18:08:05+02:00 after the initial run-070 machine record was persisted.

## Reviewed head

- Codex reviewed `c6600bfc241eb9af9daabba84ee7254acc20bb6a`.
- Scientific ending head remains `bf0c3e15ab5e0a9a7a4264e195279b4443c49b1d`; the later change only updated the readiness document.
- No GitHub Actions workflow run and no combined status were observed for `bf0c3e15ab5e0a9a7a4264e195279b4443c49b1d`.

## Findings and repair queue

| Queue ID | Severity | Evidence | State | Persistent failures |
|---|---:|---|---|---:|
| F-070-01 | P1 | PR comment 4178375922: caller-controlled excerpt hash is not bound to the referenced SEC filing | OPEN | 0 |
| F-070-02 | P1 | PR comment 4178375925: scope, speaker, polarity and quotation labels are trusted rather than validated | OPEN | 0 |
| F-070-03 | P2 | PR comment 4178375929: the full 16-case catalog is not executed and payload-compared twice inside the persisted test/CI | OPEN | 0 |
| F-070-04 | P2 | PR comment 4178375932: pull_request checkout may test a synthetic merge ref rather than the exact PR head | OPEN | 0 |

The earlier local closure of F-067-01/F-068-01 is falsified by the two P1 findings. Historical failure counts are preserved; none of the four new repairs was attempted in this correction.

## Corrected readiness

- Verified project-local gate count: **7 MET / 1 PARTIAL / 4 NOT_MET**.
- Engineering: PARTIAL.
- Scientific: PARTIAL.
- Gate: HOLD.
- Dual save: PARTIAL because the canonical GitHub hourly-build-log backfill remains BLOCKED_AFTER_2_ATTEMPTS.
- POC v1: NOT_FROZEN.
- Independent review: FINDINGS_OPEN.
- Human approval: absent.

## Exact next task

Repair F-070-01 first by defining and enforcing an independently validated, filing-backed extraction record that binds issuer CIK, accession, reporting period, section coordinates and excerpt digest. Then repair F-070-02 against that trusted bounded source. After those P1 repairs pass twice at one exact head, address F-070-03 and F-070-04, request a new independent review, and preserve NOT_FROZEN until CI and explicit human approval exist.
