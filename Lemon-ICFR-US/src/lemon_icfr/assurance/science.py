"""Scientific HOLD protection (section 12). Engineering reproducibility != construct validity.

No ACK2007 coefficient values or variable definitions are embedded here. They must be
loaded from the canonical, checksummed contract in the repository.
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from types import MappingProxyType
from typing import Mapping, Optional

from .enums import HumanDecision, ScientificStatus, VariableStatus
from .errors import IntegrityError, PromotionError, ScientificHoldError
from .human_gate import HumanDisposition
from .paths import read_canonical


@dataclass(frozen=True)
class PrimarySourceCitation:
    evidence_id: str
    is_primary_publication: bool
    definition_locator: str          # e.g. page/table in the original paper
    construction_rule_locator: str   # where the sample/missing-year rule is stated


class VariableRegistry:
    def __init__(self, statuses: Mapping[str, VariableStatus]):
        self._s = dict(statuses)
        self.log: list[str] = []

    def status(self, name: str) -> VariableStatus:
        return self._s.get(name, VariableStatus.UNVERIFIED)

    def executable(self, name: str) -> bool:
        return self.status(name) is VariableStatus.VERIFIED

    def promote(self, name: str, to: VariableStatus, *, citation: Optional[PrimarySourceCitation],
                accepted_disposition: Optional[HumanDisposition]) -> None:
        if to is VariableStatus.VERIFIED:
            if citation is None or not citation.is_primary_publication:
                raise PromotionError(f"{name}: VERIFIED requires a primary-source citation")
            if not citation.definition_locator or not citation.construction_rule_locator:
                raise PromotionError(f"{name}: definition AND construction rule must be located in the primary source")
            if accepted_disposition is None or accepted_disposition.decision is not HumanDecision.APPROVED:
                raise PromotionError(f"{name}: VERIFIED requires a gate-accepted human APPROVED disposition")
        self.log.append(f"{name}: {self.status(name)} -> {to}")
        self._s[name] = to


def load_coefficient_contract(base: Path, rel: str, sha: str, expected_names: tuple[str, ...]) -> Mapping[str, float]:
    data = json.loads(read_canonical(base, rel, sha))
    coefs = data.get("coefficients")
    if not isinstance(coefs, dict):
        raise IntegrityError("contract lacks 'coefficients' object")
    if set(coefs) != set(expected_names):
        raise IntegrityError(f"coefficient set mismatch: missing={sorted(set(expected_names) - set(coefs))} "
                             f"extra={sorted(set(coefs) - set(expected_names))}")
    if not all(isinstance(v, (int, float)) and not isinstance(v, bool) for v in coefs.values()):
        raise IntegrityError("non-numeric coefficient")
    if data.get("scale") != "raw":
        raise IntegrityError("coefficient scale must be declared 'raw'")
    return MappingProxyType(dict(coefs))


class ScientificModel:
    """The ONLY entry point to prediction. There is no other path from raw input to output."""

    def __init__(self, name: str, variables: VariableRegistry, required_vars: tuple[str, ...],
                 status: ScientificStatus = ScientificStatus.SCIENTIFIC_HOLD):
        self.name, self.variables, self.required = name, variables, required_vars
        self.__status = status

    @property
    def status(self) -> ScientificStatus:
        return self.__status

    def predict(self, row: Mapping[str, float]):
        if self.__status not in (ScientificStatus.VERIFIED, ScientificStatus.CONFIRMATORY_PASS):
            raise ScientificHoldError(f"{self.name} is {self.__status}; public prediction disabled")
        blocked = [v for v in self.required if not self.variables.executable(v)]
        if blocked:
            raise ScientificHoldError(f"non-executable variables: {blocked}")
        raise NotImplementedError("prediction implementation lives in the reviewed model module")

    def promote_status(self, to: ScientificStatus, *, accepted_disposition: Optional[HumanDisposition],
                       confirmatory_evidence_id: str = "") -> None:
        if to in (ScientificStatus.VERIFIED, ScientificStatus.CONFIRMATORY_PASS):
            blocked = [v for v in self.required if not self.variables.executable(v)]
            if blocked:
                raise PromotionError(f"cannot promote {self.name}: unverified variables {blocked}")
            if not confirmatory_evidence_id:
                raise PromotionError("promotion requires confirmatory (non-development) evidence")
            if accepted_disposition is None or accepted_disposition.decision is not HumanDecision.APPROVED:
                raise PromotionError("promotion requires a gate-accepted human APPROVED disposition")
        self.__status = to


def fixture_arithmetic(base: Path, fixture_rel: str, fixture_sha: str,
                       coefs: Mapping[str, float], intercept_name: str) -> dict:
    """Reproduces arithmetic on the FROZEN fixture only. Result is DEVELOPMENT_ONLY."""
    rows = json.loads(read_canonical(base, fixture_rel, fixture_sha))
    out = []
    for r in rows:
        xb = coefs[intercept_name] + sum(coefs[k] * r[k] for k in coefs if k != intercept_name)
        out.append(round(xb, 10))
    return {"status": ScientificStatus.DEVELOPMENT_ONLY.value, "linear_predictor": out,
            "note": "engineering reproduction of fixture arithmetic; NOT scientific validation"}
