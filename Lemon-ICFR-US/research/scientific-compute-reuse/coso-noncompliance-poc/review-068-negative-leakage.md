# Run 068 — Negative-context and leakage review

## Scope

Independent engineering/adversarial review of the persisted Park et al. (2021) COSO noncompliance classifier at branch HEAD `4329eb135bf712734b85b010f6fb969b66d76386`.

Persisted inputs reviewed:

- `classifier.py` blob `8f9def9dad81f78c80a8030072eea11c61016cec`
- `benchmark-spec.json` blob `4b1930f6547ec4be5f2329782a395797633c56ff`
- `test_classifier.py` blob `7c007450550c0cce744cc41cdf37ee1329bff4ad`
- `test_mutation_determinism.py` blob `ff3e6d3841b5a59f1ae102c6d6020f14ff75e71d`

## Executed falsification matrix

The persisted classifier logic was executed locally without modification.

| Case | Expected | Actual | Result |
|---|---:|---:|---|
| Management ICFR, explicit 1992 | 1 | 1 | PASS |
| Management ICFR, explicit 2013 | 0 | 0 | PASS |
| Historical-only 1992 reference | null | 1 | FAIL |
| Bibliography-only 2013 reference | null | 0 | FAIL |
| Auditor-only 1992 reference | null | 1 | FAIL |
| Quoted other-company 2013 reference | null | 0 | FAIL |
| Management ICFR, unversioned | null | null | PASS |

Summary: **3/7 PASS; 4/7 FAIL**.

The seven-case matrix was executed twice at the same persisted classifier content. Both result payloads had SHA-256 `c73a7276a2048730c36d84e61d67232d52fa1e142c73baa2ac5ece3e7d185e31`; determinism passed, while scientific correctness remained 3/7.

## Findings

### F-068-01 — Evidence-scope leakage

The classifier searches the entire supplied text for version strings. It does not establish that the matched phrase is management's own ICFR framework disclosure. Historical discussion, bibliography, auditor-only text, or a quotation from another company can therefore generate a false noncompliance label.

Severity: scientific-contract defect. The current implementation is not suitable for unrestricted filing text.

### F-068-02 — Temporal applicability remains unenforced

The prior Run 067 finding remains open. The benchmark requires fiscal-year end after 2014-12-15, but the classifier has no `period_end` input and cannot enforce the cutoff.

### F-068-03 — Existing green tests are incomplete

The two persisted suites validate version-token behavior and determinism, but do not test evidence scope, speaker/section identity, historical references, citations, quotations, or temporal applicability. Their exit-code-zero evidence must not be interpreted as end-to-end scientific validity.

## Required repair acceptance criteria

The dedicated repair sweep should require all of the following before this gate can leave HOLD:

1. Require a parseable ISO `period_end`; return `None` when missing, invalid, or on/before 2014-12-15.
2. Accept only a bounded management ICFR assessment excerpt or structured evidence object whose source section is explicitly verified.
3. Fail closed for historical-only references, bibliography/citations, auditor-only passages, quoted third-party text, both versions, unversioned text, negated/non-adopted framework statements, and empty input.
4. Preserve deterministic 1992→1 and 2013→0 behavior for eligible, explicit management ICFR disclosures.
5. Add executable boundary tests for 2014-12-15 and 2014-12-16 plus the four failed negative-context cases above.
6. Run the repaired suites twice at the same exact HEAD; then obtain exact-head CI and fresh independent review.

## Decision

`ENGINEERING_STATUS = PARTIAL`  
`SCIENTIFIC_STATUS = PARTIAL`  
`GATE_STATUS = HOLD`  
`CODEX_STATUS = FINDINGS_OPEN`  
`POC_V1_STATUS = NOT_FROZEN`

No classifier patch was attempted because the cutoff-aware patch is already `BLOCKED_AFTER_2_ATTEMPTS` in the persistent repair queue. This review advances falsification evidence without resetting that counter.
