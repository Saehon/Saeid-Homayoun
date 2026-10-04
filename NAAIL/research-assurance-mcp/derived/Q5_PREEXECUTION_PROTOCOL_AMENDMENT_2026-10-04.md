# Q5 Pre-Execution Protocol Amendment — Prior SEC-Text Exposure — 2026-10-04

Author: GPT repair operator
Scope: additive protocol record only
Scientific rule modified: NO
Scanner modified by this record: NO
R3 dispatched: NO

## Trigger for this amendment

Claude's 2026-10-04 independent-review rule states that the updated scanner should be REJECTED if either scanner version or any other process had already retrieved or looked at Microsoft filing text for the same 10 accessions before the scanner change. In that circumstance, a clean preregistration is no longer defensible and any future confirmatory protocol must be separately versioned while preserving v1.

## Newly reconstructed historical evidence

The repository's Microsoft final artifacts predate the Q5 frozen rule/scanner pair and already contain COVID-text outcomes for all 10 Microsoft observations.

### Historical final CSV / JSON / report

Creation commits on 2026-10-01 UTC:

- `msft_one_company_final.csv`: commit `6dd3f0f30e851a13713d3c4ed6e48e3ee413611e`, 2026-10-01T09:12:54Z.
- `msft_one_company_final.json`: commit `bc783cef59b35e58b278544c14704cb248648d50`, 2026-10-01T09:12:57Z.
- `FINAL_REPORT.md`: commit `53b25b530e0dccb1c2677eae1ba3e8b5a5cec7b8`, 2026-10-01T09:12:59Z.

The final report explicitly states:
- official SEC EDGAR filing metadata **and filing text** were the public-data source;
- the four 2019 matched filings had no COVID reference in the SEC text checks;
- each matched filing from Q1-2020 through Q2-2021 contained COVID/coronavirus discussion;
- the table contains `COVID present` values for all 10 observations.

The final JSON likewise records:
`"covid_presence": "binary presence of covid/corona in SEC filing text; 2019 matched filings=0, 2020-Q2 2021 matched filings=1"`.

Therefore, on the available repository evidence, Microsoft SEC filing text for the same 10 observations had already been inspected before the Q5 preregistration.

## Later Q5 freeze

The Q5 v1 rule/scanner pair was added later:

- commit `2b278315a1ca38f67bab6e97b265e57ce28c3a5e`
- timestamp `2026-10-02T12:13:34Z`
- rule blob `d7760b4909ae84896cae8797fb8536f59d36053c`
- original scanner blob `1b65c3cc60b0305aed244a642923ea50c95b0045`

This is later than the 2026-10-01 historical COVID-text findings.

## Scanner amendment

The scanner was modified once:

- commit `054dbecd0a7d511fabc054f7135b9d616d072a9f`
- timestamp `2026-10-04T11:32:16Z`
- author `Saeid Homayoun`
- old blob `1b65c3cc60b0305aed244a642923ea50c95b0045`
- new blob `4602d71d9a1db84405a17470fea03638a8595758`

The code delta adds retrieval/run provenance and changes an all-match automated assurance state from `VERIFIED` to `HUMAN_REVIEW`. It does not change the frozen regex, accessions, document scope, match threshold, or filing set.

## GitHub Actions execution evidence

### Run 37003148170 / job 110825211903 — 2026-10-02

- Workflow: NAAIL Research Assurance P7
- Head: `a1e0ea7b449d90a0d4821e45a6c63d1182cdbe3a`
- Scanner step was invoked.
- `EDGAR_IDENTITY` was empty.
- The scanner raised before reading the frozen rule or calling `submission_index()`.
- Exit code: 1.
- Therefore this workflow run did **not** retrieve SEC metadata or filing text.

### Runs 37003872890 and 37004149967

- Their logs do not invoke `msft_covid_scan.py`.
- No Q5 SEC-text execution is evidenced.

### PR #103 Codex review runs

- 37005586281: review job failure, no scanner/SEC invocation in logs.
- 37199079225: skipped.
- 37199297404: skipped.
- 37199350740: skipped.
- 37200092162: skipped.

No repository `workflow_dispatch` event named `NAAIL Microsoft COVID Scan` was observed before this amendment. GPT did not dispatch R3 after PR #104 merged because the scanner fingerprint failed the independent-review gate.

## Local/manual execution evidence

No timestamped project run record was found that identifies the exact local/manual process which produced the 2026-10-01 COVID binary fields. Therefore its execution environment, command, run ID, and exit code cannot be reconstructed from the current records.

However, the 2026-10-01 final artifacts themselves are direct evidence that SEC filing text was inspected before the Q5 v1 freeze. Absence of a recoverable local run ID does not erase that data exposure.

## Operator conclusion

Under Claude's stated decision rule, the evidence does **not** support `APPROVE_NEW_FINGERPRINT` for a clean preregistered v1 test.

Recommended independent-review disposition:

`SCANNER_DECISION = REJECT`

Reason: same-observation SEC filing-text outcomes were already observed before the v1 rule/scanner freeze.

Recommended next protocol:
- preserve `covid_rule_v1.json` and both v1 scanner blobs as historical records;
- do not call a later run of v1 a blind/preregistered confirmation;
- design a separately versioned protocol (e.g. v2) with a genuinely unobserved holdout or different confirmatory target;
- obtain independent review before any v2 execution.

## Additional implementation note

The current scanner result JSON records rule ID/path and execution provenance but does **not** record the scanner Git blob and rule Git blob inside the result payload. If a future version is created, explicit scanner/rule fingerprints should be included in its output contract before execution.

POC_COMPLETE remains FALSE.
COVID_R3_STATUS = BLOCKED_PROTOCOL_VALIDITY.
