# Validation Request — 2026-09-14

This branch exists only to trigger an isolated GitHub Actions validation of the frozen `MNSc-FamaFrench-01` study against the official Kenneth R. French July 2024 and July 2025 historical archives.

Required gates:

- offline unit tests pass;
- official archive downloads succeed;
- Tables 1–6 are produced;
- source SHA-256 fingerprints are recorded;
- `evidence_passport.json` is produced;
- `discovery_claim_allowed = false` remains enforced.

No scientific conclusion should be accepted from this branch unless the generated artifacts are reviewed and archived.
