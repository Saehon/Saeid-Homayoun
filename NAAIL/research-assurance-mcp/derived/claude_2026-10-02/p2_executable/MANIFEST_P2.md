# P2 executable layer — derived, Claude, 2026-10-02
Target path: NAAIL/research-assurance-mcp/derived/claude_2026-10-02/p2_executable/
Original fixtures (unchanged): benchmark/adversarial_benchmark_v2.json sha256 6237d06b0fbad0f236446df246d8f4fbdf4ee9256241be4706b7934e0ce06013
Input snapshot: ZIP sha256 a58f98b684e9ab923c9fd5a1497678506d0b54ecf335b6f0bb1826d58ae0bd94. Python 3.12.3, stdlib only.

| File | sha256 |
|---|---|
| p2_adversarial_v2_executable.py | 0e22e75139dc2c827a4badfa66cd888bb3d63ae54fc1651e850e706196bfc1b8 |
| p2_falsification.py | b7d6f17c85367818d8834c4aacd013858cfc0ac17991a30dcfc407b33eafa8ee |
| p2_result.json | c23077e6c37198163753d211a6de36488c9101b4297e2189b50a8f2dfdc90fce |
| falsification_result.json | a256dbb356ce5f5ea3b266f12021126895f6b4909d5b372df29be12313943877 |

Note: result JSON bytes vary between runs only in REP-03 evidence values (unseeded bootstrap by design);
detected taxonomy IDs per fixture are deterministic (falsification F3).
Run: python3 p2_adversarial_v2_executable.py <mcp> p2_result.json ; python3 p2_falsification.py <mcp> falsification_result.json
All data synthetic. Generator and detector share one author (see limitations in p2_result.json).
