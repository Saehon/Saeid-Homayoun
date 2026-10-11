# P14 human-gate signature separation — design note

Status: `PARTIAL / UNREVIEWED / DEVELOPMENT_ONLY`

## Governing decision

`POC_STATE.md` records `owner_approved_cryptography: no`. Therefore this phase does not activate, exercise, or claim approval of Ed25519 or any other new asymmetric-cryptography dependency. The existing HMAC gate remains a development-only compatibility path and is not treated as production separation because a process holding its verification secret can also sign.

## Trust boundary

- The human approval UI is the only permitted future holder of private signing material.
- The agent-side assurance pipeline receives only a verifier and public verification material.
- `HumanSignatureVerifier` exposes `verify(...)` only. It has no `sign(...)` method and no private-key field.
- AI agents cannot create an authorized human disposition, choose a human decision, or bypass reviewer registry, passport binding, evidence/review requirements, or override rules.
- Missing, malformed, forged, wrong-key, wrong-identity, wrong-role, or wrong-passport signatures fail closed.

## Current POC boundary

The existing HMAC test path is used only to demonstrate fail-closed rejection of unsigned, forged, AI-identity, and wrong-key dispositions. This does not resolve ORQ-005 and does not establish production cryptographic separation. The committed Ed25519 verifier module remains dormant under the owner-approval gate and is not invoked in this run.

## Future activation conditions

1. The human owner explicitly changes `owner_approved_cryptography` to `yes`.
2. The approved dependency and version are recorded and reproducibly installed.
3. Private-key generation, storage, rotation, revocation, recovery, and audit logging are implemented only in the separate human UI/service.
4. The agent pipeline is configured with public verification material only.
5. Forgery, tampering, malformed-signature, wrong-key, replay/passport-binding, and absence-of-sign-method tests pass in CI.
6. Independent review and human approval occur before any production claim or merge.

Until all conditions are met, ORQ-005 stays open and P14 stays `PARTIAL`.
