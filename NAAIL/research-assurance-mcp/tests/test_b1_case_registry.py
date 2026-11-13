from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from validate_case_registry import RegistryError, normalize_doi, validate_registry  # noqa: E402


REGISTRY = ROOT / "registry" / "cases.yaml"
RUN021_FIXTURE = ROOT / "tests" / "fixtures" / "b1_run021_duplicate_cases.yaml"
VALIDATOR = SCRIPTS / "validate_case_registry.py"


def test_canonical_registry_has_only_case_001() -> None:
    parsed = validate_registry(REGISTRY)
    assert len(parsed["cases"]) == 1
    case = parsed["cases"][0]
    assert case["case_id"] == "CASE-001"
    assert case["normalized_doi"] == "10.1287/mnsc.2023.4670"


def test_doi_normalization_is_prefix_and_case_invariant() -> None:
    assert normalize_doi(" DOI:10.1287/MNSC.2023.4670 ") == "10.1287/mnsc.2023.4670"
    assert normalize_doi("https://doi.org/10.1287/MNSC.2023.4670") == "10.1287/mnsc.2023.4670"


def test_run021_duplicate_fixture_hard_fails() -> None:
    try:
        validate_registry(RUN021_FIXTURE)
    except RegistryError as exc:
        message = str(exc)
        assert "duplicate normalized DOI 10.1287/mnsc.2023.4670" in message
        assert "CASE-001 and CASE-002" in message
    else:
        raise AssertionError("RUN 021 duplicate fixture was not rejected")

    completed = subprocess.run(
        [sys.executable, str(VALIDATOR), str(RUN021_FIXTURE)],
        check=False,
        capture_output=True,
        text=True,
    )
    assert completed.returncode == 1
    assert "CASE_REGISTRY_INVALID" in completed.stderr


if __name__ == "__main__":
    test_canonical_registry_has_only_case_001()
    test_doi_normalization_is_prefix_and_case_invariant()
    test_run021_duplicate_fixture_hard_fails()
    print("B1 case-registry invariants: PASS")
