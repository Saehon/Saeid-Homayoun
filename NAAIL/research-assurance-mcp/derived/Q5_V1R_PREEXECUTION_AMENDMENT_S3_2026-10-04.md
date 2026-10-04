# Q5 v1-R Pre-Execution Amendment — S3 Diagnostic Reclassification — 2026-10-04

Author: GPT repair operator  
Status: additive pre-execution amendment  
SEC retrieval under v1-R before this amendment: **NONE**  
Historical v1 rule modified: **NO**

## Independent-review decision

Claude reviewed v1-R candidate protocol blob `4851cbac193eb222f7bccd6c02c46e396b91f003` and scanner blob `ffb3f6401fa45491aec400ee92147f1a8d84a5b6`.

Decision:

- `V1R_PROTOCOL_DECISION = CHANGES_REQUIRED`
- `V1R_SCANNER_DECISION = CHANGES_REQUIRED`
- `GPT_MAY_PROCEED_WITH_V1R_REDERIVATION = NO`

## Reason for amendment

The candidate S3 sensitivity set added the generic term `pandemic`. That term measures broader pandemic-risk language rather than COVID-19 specifically. In the independent reviewer's offline mocked test, generic pre-COVID wording such as "affected by a pandemic, war or natural disaster" caused all four 2019 filings, including Q4-2019, to match.

That is a construct-validity defect in S3 as a deciding sensitivity set. It is not a data-driven repair to observed v1-R SEC results because no v1-R SEC retrieval has occurred.

## Amended term-set roles

### Deciding sets

- `PRIMARY`
- `S1`
- `S2`

All three explicitly name the disease or virus.

### Broad diagnostic

- `S3`

S3 remains frozen and executed, but it is reclassified as `BROAD_DIAGNOSTIC` and is **not** part of the automated agreement rule.

## Amended decision rule

1. Any disagreement among PRIMARY/S1/S2 for any filing → `FLAGGED`.
2. Any PRIMARY/S1/S2 match in Q4-2019 → `FLAGGED`.
3. If PRIMARY/S1/S2 are all zero but S3 is one for a filing, that filing is `S3_ONLY`.
4. S3-only does not automatically FLAG the run. Automated state remains `HUMAN_REVIEW`.
5. For every S3-only filing, **all S3 match snippets are retained with no count cap**, each snippet limited to ≤15 words.
6. Independent reviewer must classify every S3-only snippet as either:
   - COVID reference without an explicit virus/disease term → final claim remains subject to review and may be `FLAGGED`; or
   - generic pandemic-risk language → no effect on the bounded COVID-term claim.
7. VERIFIED ceiling remains unavailable to automation. It requires:
   - PRIMARY/S1/S2 agreement on all 10 filings;
   - no PRIMARY/S1/S2 match in Q4-2019; and
   - independent Claude classification of every S3-only snippet.

## Preservation

The candidate protocol/scanner remain in Git history. The historical `covid_rule_v1.json` and both historical v1 scanner blobs remain unchanged.

This amendment precedes any v1-R SEC retrieval.
