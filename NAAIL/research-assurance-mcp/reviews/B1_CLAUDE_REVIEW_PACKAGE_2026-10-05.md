# B1 Claude Review Package — DOI-Keyed Case Registry

Date: 2026-10-05  
Status requested: independent review of a V1-preparation registry and duplicate guard.  
Scientific boundary: no case search, candidate evaluation, case selection, data retrieval, replication, or scientific claim.

PR: [#126](https://github.com/Saehon/Saeid-Homayoun/pull/126)  
Validated commit: `9d3a1388e4627701648f512008311ceb26ddb3c7`  
Base: `main` at `d48faf52bd27a6796063f10b73657eb1d9cf384b`

## Scope

B1 creates a constrained `registry/cases.yaml` keyed by normalized DOI. It contains only the existing canonical Case 001, DOI `10.1287/mnsc.2023.4670`. The entry does not select or create a Case 002.

The validator:

1. trims outer whitespace and lowercases DOI text;
2. removes `doi:`, `doi.org`, or `dx.doi.org` prefixes;
3. rejects internal whitespace and invalid DOI syntax;
4. hard-fails duplicate normalized DOI values;
5. hard-fails duplicate or malformed `CASE-NNN` identifiers; and
6. requires the complete case-record field set.

## Historical duplication test

`tests/fixtures/b1_run021_duplicate_cases.yaml` is explicitly synthetic and additive. It reconstructs the RUN 021 failure mode by assigning Case 002 the same DOI as Case 001 using a different case/prefix representation. The test requires both the Python API and command-line process to reject it. Historical RUN 021/022 records are not edited.

Expected rejection:

`duplicate normalized DOI 10.1287/mnsc.2023.4670: CASE-001 and CASE-002`

## File fingerprints

| File | Git blob | SHA-256 |
| --- | --- | --- |
| `registry/cases.yaml` | `eaa55466862adb3e029a18afbccf2dc08e454764` | `0e746a6bac1a42311b33cb62d584ca6d29f461c8c545303fb09a544b8ae4a30b` |
| `scripts/validate_case_registry.py` | `c88320cb33cac945a6bce705be6d3c6b8f96e425` | `6e4652048a91d86b8aee9fa0d6d8907faad481892ea83c136a364d8cac35c8bf` |
| `tests/fixtures/b1_run021_duplicate_cases.yaml` | `6202ba0acecada209b8af5148cdc604f295ccf9a` | `088b08e6d3d474f205ea81293917b8700267ff8759f465dfbba62aa4e900c4bd` |
| `tests/test_b1_case_registry.py` | `fb751a15cdba777d2d690b1444d6cd9a56de2369` | `043b4852f83c381fed9269b3de7aa6a389df3ead3fd87c4313da0b76343e44f0` |
| `.github/workflows/naail_v1_b1_case_registry.yml` | `b19064ad6d7cecb854b5b501373fc3e21eccd79b` | `2e8afefc4e22043cc41ce690e96e2114675dfe7705fb129ca43e76ab17eb055b` |

## Local validation

- Python compile: exit 0.
- Canonical registry: `CASE_REGISTRY_VALID: 1 unique case(s)`.
- Invariant suite: `B1 case-registry invariants: PASS`.
- Duplicate fixture CLI: required nonzero exit observed by the invariant suite.

## Authoritative CI evidence

- Single authorized run: [37260197347](https://github.com/Saehon/Saeid-Homayoun/actions/runs/37260197347), attempt 1, `success`.
- Job: `111605611427`, `b1-case-registry-guard`, `success`.
- Validated commit: `9d3a1388e4627701648f512008311ceb26ddb3c7`.
- Successful steps: compile validator/test; validate canonical registry; prove RUN 021-style duplicate DOI hard fails.

## One-run control

The proposed CI workflow listens only for the pull request `opened` event. It does not listen for `synchronize`, `reopened`, `push`, or `workflow_dispatch`. This prevents documentation or review-package commits from repeating the B1 test after the single opening run.

This package update occurs after the opening run but cannot trigger the workflow because `synchronize` is not an enabled event. No CI rerun is authorized to improve or select a result.

## Review questions

1. Does the DOI normalization avoid both false distinction and silent mutation?
2. Does the reconstructed RUN 021 fixture prove the required hard-fail behavior without rewriting history?
3. Is the registry boundary sufficiently clear that it cannot be interpreted as human selection of Case 002/003?
4. Are any additional fields required before this DRAFT registry can later be frozen?

`POC_COMPLETE = FALSE`; `V1_COMPLETE = FALSE`.
