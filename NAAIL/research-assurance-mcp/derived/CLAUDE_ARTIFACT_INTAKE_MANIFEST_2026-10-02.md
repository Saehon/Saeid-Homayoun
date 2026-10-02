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

Second Claude package intake is VERIFIED:
- `derived_claude_2026-10-02_p2.zip` SHA-256 `fedaa45c26709311a06b44b8bcd52beeb26653f0980534371216b719e0a026cd`
- four payload hashes match `MANIFEST_P2.md`; the manifest itself is hashed separately
- five files committed under `claude_2026-10-02/p2_executable/`
- P2 intake commit: `edf36ae54f752fc9d951c0160961d99eacf458ad`
- READBACK-VERIFIED: all seven primary and all five P2 files match their ZIP bytes on GitHub
- READBACK-VERIFIED: both ZIPs and all twelve extracted files downloaded from Drive and SHA-256 matched
- Primary ZIP Drive ID: `1U87PYduZywQZfVnecOliacdZEjd9-fp0`; P2 ZIP Drive ID: `1BArLCJKl6HAb2ppx1Ke9wINqYLiUkdPN`
- extracted-file Drive folder: `1wRoMgmOq_CNq_oDA3hoGtz0P7wRCAKQO`

| File | GitHub readback SHA-256 | Drive readback SHA-256 | State |
|---|---|---|---|
| MANIFEST.md | 804a05177f18f26247e52eae0dfd0d9f3b3c1e583a5bea2a79b5ee56f9a98eed | 804a05177f18f26247e52eae0dfd0d9f3b3c1e583a5bea2a79b5ee56f9a98eed | VERIFIED |
| msft_filinglag_independent_check.json | 84228cfdb32b1a7111b822a4be14ed6ddb3663ffda805a29adcefd55d281c731 | 84228cfdb32b1a7111b822a4be14ed6ddb3663ffda805a29adcefd55d281c731 | VERIFIED |
| msft_filinglag_independent_check_v2.json | 2933ad5ec7e1d1bff11f43469b969966f8f869d820baa855a100a94b15757fc7 | 2933ad5ec7e1d1bff11f43469b969966f8f869d820baa855a100a94b15757fc7 | VERIFIED |
| p2_candidate_msft_mutation_results.json | e823299c5a3bed917847a4790fcebb31c9ef0083435d80757e17bcf7414bdb10 | e823299c5a3bed917847a4790fcebb31c9ef0083435d80757e17bcf7414bdb10 | VERIFIED |
| p2_candidate_msft_mutations.py | 51f4478b8ef9f199de5e8f8ab1c8690483ce5c4c6a0013f405b4796a08f49e68 | 51f4478b8ef9f199de5e8f8ab1c8690483ce5c4c6a0013f405b4796a08f49e68 | VERIFIED |
| p7_regression_v2.py | 698a6db34d6f03a7dca8cf571d8f3df3317f61f63ee4ff50eb2da288c6b01f74 | 698a6db34d6f03a7dca8cf571d8f3df3317f61f63ee4ff50eb2da288c6b01f74 | VERIFIED |
| p7_regression_v2_result.json | 99c0af79576f210cacf947b6b959dcb420fec4c6e41086b1d0cecb248ba11d66 | 99c0af79576f210cacf947b6b959dcb420fec4c6e41086b1d0cecb248ba11d66 | VERIFIED |
| p2_executable/MANIFEST_P2.md | 7eaae82ed09d6beac7c9ff6c4d56c90ab97437e8d3e9e3ed64a4100cb453b398 | 7eaae82ed09d6beac7c9ff6c4d56c90ab97437e8d3e9e3ed64a4100cb453b398 | VERIFIED |
| p2_executable/falsification_result.json | a256dbb356ce5f5ea3b266f12021126895f6b4909d5b372df29be12313943877 | a256dbb356ce5f5ea3b266f12021126895f6b4909d5b372df29be12313943877 | VERIFIED |
| p2_executable/p2_adversarial_v2_executable.py | 0e22e75139dc2c827a4badfa66cd888bb3d63ae54fc1651e850e706196bfc1b8 | 0e22e75139dc2c827a4badfa66cd888bb3d63ae54fc1651e850e706196bfc1b8 | VERIFIED |
| p2_executable/p2_falsification.py | b7d6f17c85367818d8834c4aacd013858cfc0ac17991a30dcfc407b33eafa8ee | b7d6f17c85367818d8834c4aacd013858cfc0ac17991a30dcfc407b33eafa8ee | VERIFIED |
| p2_executable/p2_result.json | c23077e6c37198163753d211a6de36488c9101b4297e2189b50a8f2dfdc90fce | c23077e6c37198163753d211a6de36488c9101b4297e2189b50a8f2dfdc90fce | VERIFIED |

2026-10-02 changelog: completed Q1 second-package intake and byte-level dual-system readback; original Claude package bytes unchanged.

Governance:
- originals remain unchanged;
- derived evidence is stored under a dedicated Claude-derived path;
- hash verification is byte-level against the supplied ZIP contents;
- historical records remain additive and immutable.
