# B3 Claude Review Package — Case-Selection Protocol

Date: 2026-10-05  
Status requested: independent review of a case-selection protocol frozen before search.

PR: [#130](https://github.com/Saehon/Saeid-Homayoun/pull/130)  
Validated commit: `ff749f13bb55da4e97be650e04c9b4837c07c15c`  
Base: `main` at `d48faf52bd27a6796063f10b73657eb1d9cf384b`

## Boundary

This package contains only the protocol, blank record template, freeze manifest, invariant test, and narrow CI. It contains no candidates, candidate search results, article or package retrieval, rankings, case selection, replication, or scientific claim.

## Prior exposure

The operator has seen Case 001 and the invalid RUN 021/022 duplicate. The protocol declares that no new candidate search, candidate evidence retrieval, scoring, or selection occurred before freeze.

## Frozen fingerprints

| File | Git blob | SHA-256 |
| --- | --- | --- |
| `case_selection_protocol_v1.json` | `2b56d32125de97e823587b835fa0b3deac537223` | `110ea61a4bd0505c24a257d20b423a2ff00f8643873d1dd453dd145d3b2bbac1` |
| `case_selection_record_template_v1.json` | `78edf1d3f429358edbcd73f90fb9e68b76b9d033` | `681ab62ad1ed6876d0f72271b539cc016c258e897b51ba53dae610cdc7d07ee5` |
| `case_selection_protocol_freeze_manifest_v1.json` | `621277a5bb7b70213e951f8f52b9b17fbabd1276` | `136b437809f6fde0f21930bc27e792e8868987e3ab93383c174289f3927f3bd3` |
| `CASE_SELECTION_PROTOCOL_V1.md` | `9983b6013dba1bbab59a7b5447afcfa1b08b1bc9` | `86595e91dbe5fd09fec44467c39b2fd4a36cde5cbfae2738f1d5b0f6d994b310` |
| `test_b3_case_selection_protocol.py` | `c3a9ddcfc361e8efb49d44b16c2689fc675f986a` | `b7031eec97de5cc50d5ddda1826f844c23927a84e9190b1f2cfe37e054af59fc` |
| `naail_v1_b3_case_selection_protocol.yml` | `3d49fd2e4aae4c3953df3fb23067902b8fd2d4fe` | `21c3233119cb5d0c1a15cbef215ad04c1e4b9821b743ee2c663c467e80e5314a` |

## Validation

- Local Python compile: exit 0.
- Local freeze-hash and invariant suite: exit 0, `B3 case-selection protocol invariants: PASS`.
- Single authorized CI: [37320371025](https://github.com/Saehon/Saeid-Homayoun/actions/runs/37320371025), run number 1, `success`.
- Job: `111797606058`, `b3-case-selection-protocol-guard`, `success`.
- Successful CI steps: compile protocol guard; validate freeze hashes and protocol invariants.

## Required review

1. Are all seven eligibility criteria scientifically and operationally bounded?
2. Does the public-data path prevent licensed-data substitution?
3. Does the authority boundary reserve selection for the human after POC approval?
4. Does the blank template capture sufficient provenance, execution, exposure, and limitation evidence?

The workflow accepts only the pull request `opened` event. This package finalization cannot trigger the guard because `synchronize` is excluded. No rerun is authorized.

`POC_COMPLETE = FALSE`; `V1_COMPLETE = FALSE`.
