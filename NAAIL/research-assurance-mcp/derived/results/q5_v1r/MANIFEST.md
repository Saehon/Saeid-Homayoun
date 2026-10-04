# Q5 v1-R Authoritative Run Manifest

Status: evidence preservation record only. No scientific interpretation is made here.

## Authoritative workflow run

- workflow: NAAIL Microsoft COVID v1-R Re-derivation
- run_id: 37204180146
- job_id: 111441813447
- event: workflow_dispatch
- run_attempt: 1
- actor: Saehon
- triggering_actor: Saehon
- created_at_utc: 2026-10-04T13:02:01Z
- run_started_at_utc: 2026-10-04T13:02:01Z
- completed/updated_at_utc: 2026-10-04T13:02:20Z
- conclusion: success
- main_head_sha_at_dispatch: d48faf52bd27a6796063f10b73657eb1d9cf384b
- checked_out_instrument_sha: 7b23810af2f4a38fdefa54b242600593c804ea91
- runner_image: ubuntu-24.04
- runner_image_version: 20260927.320
- workflow exit_code: 0

This is the only observed run of this workflow. Do not dispatch it again.

## Pre-network fingerprint evidence from job log

- expected_rule_blob=d7760b4909ae84896cae8797fb8536f59d36053c
- actual_rule_blob=d7760b4909ae84896cae8797fb8536f59d36053c
- expected_protocol_blob=83af7a6859b2d44b782b5d838420f07717ea79d3
- actual_protocol_blob=83af7a6859b2d44b782b5d838420f07717ea79d3
- expected_scanner_blob=5b0b31de72f67fd14439875db58cab7f6427f5a1
- actual_scanner_blob=5b0b31de72f67fd14439875db58cab7f6427f5a1

## GitHub Actions artifact

- artifact_id: 11303563139
- artifact_name: msft-covid-v1r-evidence
- artifact_size_bytes: 3174
- artifact_zip_sha256: 039c1479793f95b06072735e511e8cce35dcd60ec0447904491284969603c7e3
- artifact_expires_at_utc: 2027-01-02T13:02:02Z
- contained file: msft_covid_rederivation_v1r_result.json
- contained result size_bytes: 29102
- contained result sha256: b45257ac53a1ca83db5eabd0dda5744d720aaeb2d9009b087315f40c47ee9d53
- exact Git object created from the unchanged result bytes: 7fe507dce4f6ac3a21c956bcb275c1aae9c2647e

## Internal result fingerprints

The unchanged result JSON records:

- scanner_git_blob: 5b0b31de72f67fd14439875db58cab7f6427f5a1
- protocol_git_blob: 83af7a6859b2d44b782b5d838420f07717ea79d3
- base_rule_git_blob: d7760b4909ae84896cae8797fb8536f59d36053c

## Permanent Google Drive mirror

Exact raw JSON file:

https://drive.google.com/file/d/1WjoO1TXc0uhMGitsCwlsoIJc1jsPIn2F/view?usp=drivesdk

Drive folder:

https://drive.google.com/drive/folders/1q_gpvOrfhW-b8ISCVlD4JxH_bn_Dwkbo

Live Drive readback:
- filename: msft_covid_rederivation_v1r_result.json
- MIME: application/json
- size_bytes: 29102
- parent folder: 1q_gpvOrfhW-b8ISCVlD4JxH_bn_Dwkbo
- SHA-256 after live readback: b45257ac53a1ca83db5eabd0dda5744d720aaeb2d9009b087315f40c47ee9d53

## GitHub result-file publication status

The exact result bytes were successfully materialized as Git object
`7fe507dce4f6ac3a21c956bcb275c1aae9c2647e`.

The connected GitHub write safety layer blocked attaching that result payload to the PR branch path during this session. Therefore this manifest does **not** claim that
`derived/results/q5_v1r/msft_covid_rederivation_v1r_result.json`
is present in the branch.

The authoritative unchanged copies remain:
1. GitHub Actions artifact 11303563139.
2. Google Drive raw JSON above, with matching SHA-256.

No rerun is permitted to work around this publication limitation.

## Scientific gate

No result is labeled VERIFIED by this manifest.
Independent Claude snippet review remains required.
POC_COMPLETE = FALSE.
