# Claude Artifact Intake Manifest — 2026-10-02

External derived artifacts referenced by the independent handoff have now been received, byte-hash checked, and committed without modifying originals.

| File | Expected SHA-256 | Verified SHA-256 | Status |
|---|---|---|---|
| msft_filinglag_independent_check.json | 84228cfdb32b1a7111b822a4be14ed6ddb3663ffda805a29adcefd55d281c731 | 84228cfdb32b1a7111b822a4be14ed6ddb3663ffda805a29adcefd55d281c731 | VERIFIED / COMMITTED |
| msft_filinglag_independent_check_v2.json | 2933ad5ec7e1d1bff11f43469b969966f8f869d820baa855a100a94b15757fc7 | 2933ad5ec7e1d1bff11f43469b969966f8f869d820baa855a100a94b15757fc7 | VERIFIED / COMMITTED |
| p2_candidate_msft_mutations.py | 51f4478b8ef9f199de5e8f8ab1c8690483ce5c4c6a0013f405b4796a08f49e68 | 51f4478b8ef9f199de5e8f8ab1c8690483ce5c4c6a0013f405b4796a08f49e68 | VERIFIED / COMMITTED |
| p2_candidate_msft_mutation_results.json | e823299c5a3bed917847a4790fcebb31c9ef0083435d80757e17bcf7414bdb10 | e823299c5a3bed917847a4790fcebb31c9ef0083435d80757e17bcf7414bdb10 | VERIFIED / COMMITTED |

Primary Claude package:
- supplied inside user upload `3files.zip` as `derived_claude_2026-10-02.zip`
- nested ZIP SHA-256: `04bd8d3228fe855e25753ee640d4ec87c1371149e1804339158bf46063e2f30f`
- seven non-directory files present
- all six payload hashes listed in its `MANIFEST.md` match exactly
- repository target: `NAAIL/research-assurance-mcp/derived/claude_2026-10-02/`
- commit: `8e1eb135bfdbf34484824f265d0754d0d5bffe23`

Additional verified primary-package files:
- `p7_regression_v2.py` SHA-256 `698a6db34d6f03a7dca8cf571d8f3df3317f61f63ee4ff50eb2da288c6b01f74`
- `p7_regression_v2_result.json` SHA-256 `99c0af79576f210cacf947b6b959dcb420fec4c6e41086b1d0cecb248ba11d66`
- `MANIFEST.md` SHA-256 `804a05177f18f26247e52eae0dfd0d9f3b3c1e583a5bea2a79b5ee56f9a98eed`

A second supplied package, `derived_claude_2026-10-02_p2.zip`, was also inspected separately. Its internal manifest hashes match, but its P2 executable files are not represented here as part of the original seven-file intake gate and have not been silently substituted for the primary package.

Governance:
- originals remain unchanged;
- derived evidence is stored under a dedicated Claude-derived path;
- hash verification is byte-level against the supplied ZIP contents;
- historical records remain additive and immutable.
