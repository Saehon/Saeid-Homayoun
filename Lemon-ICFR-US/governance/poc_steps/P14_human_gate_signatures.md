# P14 — Human-gate signatures

## What was done

Read the live governance state and preserved `owner_approved_cryptography: no`. Added a verifier-only protocol with no signing method and a design note defining the human-UI/private-key trust boundary. Did not activate or execute Ed25519. Executed the existing HMAC fail-closed test to demonstrate rejection of unsigned, forged, AI-identity and wrong-key dispositions. ORQ-005 remains open because HMAC does not provide production-grade human/agent key separation.

## Files changed

- `src/lemon_icfr/assurance/signature_interface.py`
- `governance/P14_HUMAN_GATE_SIGNATURE_DESIGN.md`
- `governance/OPEN_REPAIR_QUEUE.md`
- `governance/poc_steps/P14_human_gate_signatures.md`
- `governance/POC_STATE.md`
- `governance/OPERATOR_LOCK.md`
- `governance/poc_runs/2026-10-11_R202610110505-P14.md`

## POC demonstration (command + REAL output excerpt)

With `PYTHONPATH=src`, interface inspection returned `INTERFACE_OK verifier_methods=['verify'] sign_present=False`. `tests.assurance.test_assurance_core.T17_22_HumanGate_Passport.test_17_ai_cannot_self_approve` passed; its four subcases reject an unsigned disposition, a zero-forged signature, an AI reviewer identity, and a wrong-key signature. The passport remains `AWAITING_HUMAN_APPROVAL`. No Ed25519 key was generated and no AI-side signing path was created.

## Tests (command, commit SHA, PASS/FAIL counts)

- Starting authoritative SHA: `ce4b2ffca87410464aff0a7c3daa02367994a713`.
- Targeted HMAC forgery guard: `1 test, 4 subtests`; 0 failures, 0 errors, 0 skipped.
- Full exact-test harness: `84 tests, 33 subtests`; 0 failures, 0 errors, 0 skipped.
- The first two diagnostic commands omitted `PYTHONPATH=src` and failed with `ModuleNotFoundError`; a generic recursive discovery also found zero tests because the nested test directories are not discovery packages. The repaired commands set the repository's documented source path and loaded the unchanged test modules/functions directly. No test or gate was weakened.

## Problems found (ORQ ids, or "none")

`ORQ-005` remains open and is updated to `P14 PARTIAL / OWNER APPROVAL REQUIRED`. The production repair cannot begin while `owner_approved_cryptography=no`.

## Decisions made without review (list every one)

Named the new protocol `HumanSignatureVerifier` and limited it to `verify(...)`. Treated the existing HMAC path only as a development POC. Did not modify the dormant Ed25519 implementation, install a dependency, generate keys, sign a disposition, record human approval, or claim independent review.

## Phase status: PARTIAL

The verifier boundary and forgery-rejection behaviour are demonstrated, but asymmetric cryptographic separation is intentionally not activated. P14 advances under the explicit program rule for `owner_approved_cryptography=no`.

## Labels: UNREVIEWED, DEVELOPMENT_ONLY

UNREVIEWED; DEVELOPMENT_ONLY. ACK2007 remains SCIENTIFIC_HOLD. No production cryptographic separation, human approval, scientific PASS, independent review, or merge is claimed.
