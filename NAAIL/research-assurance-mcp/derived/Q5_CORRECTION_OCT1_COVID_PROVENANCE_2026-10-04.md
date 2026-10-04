# Q5 Correction — October 1 COVID Provenance — 2026-10-04

This is an additive correction. The original October 1 Microsoft artifacts remain unchanged.

## Affected historical artifact

`case-001-management-science/reexecution/sec_one_company_msft/msft_one_company_final.json`

Historical field:

`assurance_state.covid_presence_binary = "VERIFIED"`

## Correction

The October 1 binary COVID-presence result did not have a recoverable method specification, executable code path, run ID, or per-document inspection record sufficient to support the project assurance state `VERIFIED`.

Current governance classification:

- evidence class: `EXTERNAL_CLAIM`
- provenance state: `UNRECOVERABLE_PROVENANCE`
- assurance treatment for POC recovery: `PARTIAL`
- original artifact: preserved unchanged

This does **not** assert that the October 1 0/1 values are false. It states that the available repository record cannot establish how those values were produced or independently reproduce the exact historical method.

## Prior exposure

The October 1 CSV, JSON, and final report record COVID outcomes for the same 10 Microsoft observations before `covid_rule_v1.json` was frozen on 2026-10-02. Therefore v1 is rejected as a clean preregistered confirmation.

## Approved recovery design

Claude independent decision:

`Q5_PROTOCOL_DECISION = REJECT_V1_PREREGISTRATION`

For the POC, use a separately reviewed retrospective re-derivation protocol:

`derived/covid_rederivation_protocol_v1r.json`

The v1 rule and both historical scanner fingerprints remain unchanged.

A genuinely unobserved/preregistered holdout is deferred to V1.
