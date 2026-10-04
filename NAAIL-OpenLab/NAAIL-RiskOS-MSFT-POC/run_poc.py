from pathlib import Path
import json
from risk_engine import load_case, RiskOSOrchestrator

HERE = Path(__file__).resolve().parent
case = load_case(HERE / "microsoft_case.json")
result = RiskOSOrchestrator(case).run()
(HERE / "poc_run_result.json").write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(result, indent=2, ensure_ascii=False))
