# NAAIL OpenLab™ — Remediation Status

**Date:** 2026-09-15  
**Public release:** v0.2.3  
**GitHub:** canonical source of truth  
**Google Drive:** mirror/archive

## Resolved in this remediation pass

### Codex governance
- Added NAAIL-specific Codex repository instructions.
- Added pull-request Codex review for NAAIL changes.
- Replaced the earlier portfolio-review workflow with the hardened `Codex Portfolio Review v2`.
- Removed the superseded portfolio-review workflow to avoid competing definitions.
- Added preflight failure messaging for a missing `OPENAI_API_KEY`.
- Preserved read-only Codex execution and `drop-sudo` safety.

### Portfolio attribution and architecture
- Added `PORTFOLIO_GOVERNANCE.md` as the canonical human-readable portfolio policy.
- Added `portfolio_registry.json` covering all 17 connected repositories.
- Froze `Saehon/Saeid-Homayoun/NAAIL-OpenLab` as the public source of truth.
- Froze NAAIL OpenLab as the umbrella platform and specialist agents/labs as modules.
- Explicitly classified `yfinance` and `timesfm` as upstream forks.
- Marked uncertain reference/dependency provenance for review rather than inferring ownership.
- Documented mixed default branches (`main`, `master`, `dev`) without rewriting upstream/dependency branches merely for cosmetic consistency.

### Prototype/release-state drift
- Added `PROTOTYPE_LINEAGE.md`.
- Separated software version numbering from prototype numbering.
- Prototype 003 = three-case synthetic benchmark; deterministic condition executed.
- Prototype 003-C = Microsoft/Alphabet/Amazon SEC-anchored evidence extension; scaffold implemented, live evidence pipeline not yet complete.
- Prototype 004 = real-provider execution infrastructure; empirical provider results remain credential/artifact dependent.
- Public Prototype 003-C status files were aligned to v0.2.3.

### Prototype 003-C scope and scientific firewall
- Issuer universe is frozen to Microsoft, Alphabet, and Amazon only.
- Real evidence layer is restricted to SEC EDGAR / Form 10-K / iXBRL.
- Fourth-issuer rejection and real-evidence/synthetic-gold separation are implemented in the private scaffold.
- Source manifest and CI checks exist.
- Controlled benchmark transformations cannot be presented as real-company audit, impairment, ICFR, management-estimate, or audit-quality findings.

## Not yet truthfully complete

### Codex portfolio-review execution
Repository-side workflow installation is complete, but no successful Codex portfolio-review run/issue has yet been observed in the available GitHub Actions feed. Therefore no Codex-generated findings are being fabricated or claimed.

External prerequisites:
1. GitHub Actions enabled for the repository.
2. Repository Actions secret `OPENAI_API_KEY` configured.
3. `Codex Portfolio Review v2` executes successfully.
4. The resulting review is published as a real GitHub issue.

### Prototype 003-C empirical evidence pipeline
Still required before P003-C can be called complete:
- live raw SEC retrieval;
- persisted raw-source SHA-256 hashes;
- normalized evidence tables;
- live Evidence Passport™ records;
- controlled SEC-anchored scenarios;
- frozen scenario gold labels;
- complete case × architecture matrix;
- reproducibility/falsification and Human Gate review.

### Prototype 004 empirical provider runs
Infrastructure exists, but an empirical provider condition requires a real run artifact with provider/model/version metadata, frozen inputs, outputs, evaluator results, latency/cost, and applicable Human Gate review.

## Next execution order

1. Activate and complete `Codex Portfolio Review v2`.
2. Convert the real Codex findings into tracked fixes; preserve the review issue as evidence.
3. Execute the three-company SEC ingestion and preserve raw hashes.
4. Build normalized P003-C evidence tables and Evidence Passports.
5. Freeze controlled scenarios and gold labels.
6. Run deterministic, single-agent, sequential-agent, and governed-multi-agent conditions under the same evidence/evaluator contract.
7. Preserve failed, null, and unfavorable results.
8. Update GitHub first; mirror validated checkpoints to Google Drive.

## Scientific rule

**Models generate. Agents debate. Code tests. Evidence decides. Humans approve.**
