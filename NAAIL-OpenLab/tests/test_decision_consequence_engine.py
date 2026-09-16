import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ENGINE = ROOT / "NAAIL-OpenLab" / "simulations" / "business-school" / "decision_consequence_engine.py"


def load_engine():
    module_name = "decision_consequence_engine"
    spec = importlib.util.spec_from_file_location(module_name, ENGINE)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def test_public_engine_is_intentional_patent_hold_stub():
    assert ENGINE.exists()
    m = load_engine()
    assert m.PATENT_HOLD is True
    assert m.PUBLIC_STATUS == "NON_ENABLING_STUB"
    assert m.implementation_status() == "NON_ENABLING_STUB"
    assert not hasattr(m, "RULES")
    assert not hasattr(m, "apply_decision")
