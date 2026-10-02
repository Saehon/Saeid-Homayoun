# Derived artifacts — Claude independent review, 2026-10-02

Target path in repo: NAAIL/research-assurance-mcp/derived/claude_2026-10-02/
Input snapshot analysed: Saeid-Homayoun-naail-research-assurance-case-001.zip
  sha256 a58f98b684e9ab923c9fd5a1497678506d0b54ecf335b6f0bb1826d58ae0bd94 (branch naail/research-assurance-case-001, pre-PR #92 state)
Environment: Python 3.12.3, Linux, no network, pytest not installed (stdlib runner used).
Originals were NOT modified.

| File | sha256 | Evidence class |
|---|---|---|
| msft_filinglag_independent_check.json | 84228cfdb32b1a7111b822a4be14ed6ddb3663ffda805a29adcefd55d281c731 | INDEPENDENTLY_REGENERATED |
| msft_filinglag_independent_check_v2.json | 2933ad5ec7e1d1bff11f43469b969966f8f869d820baa855a100a94b15757fc7 | INDEPENDENTLY_REGENERATED |
| p2_candidate_msft_mutations.py | 51f4478b8ef9f199de5e8f8ab1c8690483ce5c4c6a0013f405b4796a08f49e68 | SYNTHETIC_MUTATION |
| p2_candidate_msft_mutation_results.json | e823299c5a3bed917847a4790fcebb31c9ef0083435d80757e17bcf7414bdb10 | SYNTHETIC_MUTATION |
| p7_regression_v2.py | 698a6db34d6f03a7dca8cf571d8f3df3317f61f63ee4ff50eb2da288c6b01f74 | n/a — test harness / run log (not an evidence class in taxonomy V2) |
| p7_regression_v2_result.json | 99c0af79576f210cacf947b6b959dcb420fec4c6e41086b1d0cecb248ba11d66 | n/a — test harness / run log (not an evidence class in taxonomy V2) |

Intake check: the four files listed in derived/CLAUDE_ARTIFACT_INTAKE_MANIFEST_2026-10-02.md match their expected hashes exactly.

Re-run: python3 p7_regression_v2.py <repo>/NAAIL/research-assurance-mcp <this folder>
