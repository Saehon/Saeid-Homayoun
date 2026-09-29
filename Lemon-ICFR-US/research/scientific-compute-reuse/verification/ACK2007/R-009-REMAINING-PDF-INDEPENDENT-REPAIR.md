# R-009 — ACK2007 Remaining PDF-Independent Engineering/Provenance Repair

Date: 2026-09-29
Scope: ACK2007 only; PDF-independent engineering/provenance repair.
Scientific upgrade authority: NONE.

## Starting live state
- PR #76: open, not merged.
- Starting HEAD for this mission: a63dcf9b5fb62f91314f1f912c2d02963af8594d.
- R-008 was the latest live Resolution entry at allocation time.
- Exact-head CI at start: run #50 / 36546700008 SUCCESS on a63dcf9b5fb62f91314f1f912c2d02963af8594d.

## Raw-variable status audit — all 14 predictors
No raw predictor is VERIFIED. A complete raw ACK2007 prediction is therefore not scientifically admitted.

| Predictor | Live raw-construction status | R-009 decision |
|---|---|---|
| SEGMENTS | PENDING_TIMING | KEEP / fail closed |
| FOREIGN_SALES | SECONDARY_SOURCE | KEEP / fail closed |
| M&A | PENDING_EXACT_CONSTRUCTION | KEEP / fail closed |
| RESTRUCTURE | PENDING_EXACT_CONSTRUCTION | KEEP / fail closed |
| RGROWTH | PROVENANCE_CONFLICT | KEEP / fail closed |
| INVENTORY | PENDING_TIMING | KEEP / fail closed |
| SIZE | PROVENANCE_CONFLICT | KEEP / fail closed |
| %LOSS | BLOCKED_MISSING_YEAR_RULE | KEEP / fail closed |
| RZSCORE | BLOCKED_RAW_CONSTRUCTION | KEEP / fail closed |
| AUDITOR_RESIGN | PENDING_TIMING | KEEP / fail closed |
| AUDITOR | SECONDARY_SOURCE | KEEP / fail closed |
| RESTATEMENT | PENDING_WINDOW | KEEP / fail closed |
| INST_CON | SECONDARY_SOURCE | KEEP / fail closed |
| LITIGATION | SECONDARY_SOURCE | KEEP / fail closed |

No status was upgraded.

## Problems found

### P-009-01 — P1 / LOCAL engineering boundary
Fresh Codex review of candidate HEAD 2f4f5f9333c90bcd5408860f3f9caa02682a9111 found that callers could bypass the raw-construction gate by calling predict() directly.

Repair:
- public predict() and linear_predictor() now fail closed unless the caller explicitly selects PRECONSTRUCTED_SYNTHETIC_COMPILER_TEST mode;
- the explicit mode is restricted to engineering compiler/schema fixtures;
- no raw/production prediction path is admitted while the construction registry has unresolved gates.

### P-009-02 — P2 / LOCAL fixture integrity
Codex found that the previous checksum pinned rounded prediction output but did not independently pin the exact frozen input bytes.

Repair:
- added SHA-256 of the complete committed frozen-fixtures.csv bytes;
- added fixture-input.sha256 artifact;
- added mutation test showing that a purpose-only input mutation is detected even if model outputs would be unchanged;
- output checksum remains separately pinned.

Frozen fixture content itself was not modified.

### P-009-03 — P2 / LOCAL stale provenance wording
Codex found ESTIMAND-GATE.md still claimed the full coefficient vector/intercept/SE had been cross-checked.

Additional repository audit found stale authority wording in:
- executable-models/ACK2007/README.md
- evidence-passports/ACK2007.md
- variable-ontology/ACK2007-ONTOLOGY-CORRECTION.md

Repair:
- removed active numerical duplication from README;
- marked earlier cross-check claims superseded/non-executable;
- bounded JAR 2009 material as SECONDARY_SOURCE / SECONDARY_FORENSIC_SIGNAL_ONLY;
- retained PENDING_PRIMARY_TABLE / UNKNOWN_ORIGIN / regression_pin_only;
- retained historical evidence without allowing it to override active machine-readable authority.

## Single-source-of-truth result
Active executable authority after R-009:
- Numerical coefficient/intercept engineering pin: executable-models/ACK2007/coefficient-contract.json
- Raw-construction statuses: source-definition-recovery/ACK2007-construction-gates.json
- Compiler code loads the coefficient contract and does not define a second numerical vector.
- ACK2007-SPEC.md and README do not duplicate numerical values as executable truth.
- Historical/secondary records are explicitly non-executable where needed.

## Coefficient contract hardening
Added/reconfirmed rejection or detection for:
- missing predictor
- extra predictor
- renamed predictor
- duplicate predictor
- reordered predictor
- coefficient change
- coefficient zeroing
- coefficient sign flip
- nonnumeric coefficient
- boolean coefficient
- NaN/infinite coefficient
- intercept deletion
- duplicate intercept JSON key
- intercept mutation
- intercept sign flip
- nonnumeric/boolean/NaN/infinite intercept
- changed contract role
- changed coefficient_verification
- changed coefficient_origin
- malformed JSON

No coefficient or intercept value was changed.

## Fail-closed/adversarial boundary
Existing end-to-end construction tests continue to verify that SIZE, RGROWTH, %LOSS, RZSCORE and R-005 secondary-source variables fail before constructors execute.

Adversarial construction claims remain blocked for:
- SIZE log-vs-level, unit, window, missing-year policy
- RGROWTH competing windows, ranking direction/population, missingness
- %LOSS denominator, missing-year handling, alternative construction
- RZSCORE formula/version/ranking direction
- schema drift, unknown/missing predictors and silent exception paths

The model prediction boundary itself now also fails closed outside the explicit synthetic fixture mode.

## Frozen fixture / determinism
frozen-fixtures.csv was NOT changed.
Git blob SHA remains:
438ef1e783e4e32d5b46b58ccd1b6cb29bde83d9

Exact input-byte SHA-256:
e41b2536f8e485bfd4d72cc7f91b49f0640afdcd5e4b96231e6914868b884205

Deterministic output SHA-256:
c420891c605066edc1fe0e895ab5412decd65b648d25a42a1ceaeeb96113dda6

The fixture suite executes the committed fixture into at least two independent clean output directories and requires identical payload/output checksums.

## CI / falsification history
Historical failure evidence is preserved:
- run #34 / 36431534510: FAILURE
- run #48 / 36546388009: FAILURE
- run #51 / 36547857142: FAILURE

Run #51 failure cause:
the hardened runtime error text changed from "finite numeric value" to "finite numeric"; three nonfinite fixture tests correctly raised but their regex was stale. The assertion text was aligned without weakening the nonfinite rejection condition or changing model/fixture/scientific content.

Correction commit:
3081906d494fe621a1e7255e3e6cc00105766773

Run #52 on that candidate completed successfully:
- executable compiler tests: 42 passed
- fail-closed/adversarial + fixture tests: 56 passed
- INPUT_SHA256: e41b2536f8e485bfd4d72cc7f91b49f0640afdcd5e4b96231e6914868b884205
- OUTPUT_SHA256: c420891c605066edc1fe0e895ab5412decd65b648d25a42a1ceaeeb96113dda6

A new exact-head CI run is required after this R-009 record commit; this record must not claim that future run before it is observed.

## Codex
Fresh Codex review of 2f4f5f9333c90bcd5408860f3f9caa02682a9111 produced three findings recorded above and repaired.

A new Codex review must be requested on the final R-009 HEAD after this record commit.
Until that review returns:
CODEX_REVIEW_PENDING.

## Scientific status
SCIENTIFIC_HOLD
NOT_M1_LOCKED
PENDING_PRIMARY_TABLE

Primary-paper verification remains DEPENDENCY_CRITICAL.

## Engineering status
Candidate engineering repairs are implemented.
Final status remains ENGINEERING_HOLD until:
1. exact-head CI for the R-009 record HEAD is observed PASS; and
2. fresh Codex review is requested on that exact final HEAD and any valid findings are dispositioned.

## Boundaries preserved
- No primary-table verification attempted.
- No coefficient/intercept value changed.
- No frozen-fixture content changed or regenerated.
- No scientific definition inferred.
- No scientific status upgraded.
- No main merge attempted.
- ML/holdout/Kaggle/Hugging Face result firewall remains intact.

## NEXT_EXECUTABLE_GATE
Primary: observe exact-head CI and fresh Codex review for the final R-009 HEAD; repair only any valid PDF-independent engineering finding.
If no new engineering finding remains, keep ACK2007 SCIENTIFIC_HOLD and wait for published JAE primary evidence rather than attempting scientific closure.
