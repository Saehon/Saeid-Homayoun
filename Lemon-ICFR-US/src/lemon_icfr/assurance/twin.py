"""Minimal ICFR Digital Twin (section 21). Output is ANALYTICAL SIMULATION, not observed evidence."""
from __future__ import annotations

from dataclasses import dataclass, replace
from typing import Callable

EVIDENCE_TYPE = "ANALYTICAL_SIMULATION (not observed real-world evidence)"


@dataclass(frozen=True)
class TwinRisk:
    risk_id: str
    assertion: str
    inherent: float          # 0..1, analyst-specified, not estimated


@dataclass(frozen=True)
class TwinControl:
    control_id: str
    covers: tuple[str, ...]
    effective: bool = True
    evidence_reliability: float = 1.0
    sod: bool = True
    evidence_present: bool = True
    depends_on: tuple[str, ...] = ()
    capacity: int = 10_000


@dataclass(frozen=True)
class TwinModel:
    risks: tuple[TwinRisk, ...]
    controls: tuple[TwinControl, ...]
    override_frequency: float = 0.0
    population: int = 1_000

    def _eff(self, c: TwinControl, seen=frozenset()) -> float:
        if c.control_id in seen:
            return 0.0                     # circular dependency: fail closed
        if not (c.effective and c.sod and c.evidence_present):
            return 0.0
        byid = {x.control_id: x for x in self.controls}
        for dep in c.depends_on:
            if dep not in byid or self._eff(byid[dep], seen | {c.control_id}) == 0.0:
                return 0.0
        e = c.evidence_reliability * (1 - self.override_frequency)
        if self.population > c.capacity:
            e *= c.capacity / self.population
        return max(0.0, min(1.0, e))

    def residual(self) -> dict[str, float]:
        out = {}
        for r in self.risks:
            rem = 1.0
            for c in self.controls:
                if r.risk_id in c.covers:
                    rem *= 1 - self._eff(c)
            out[r.risk_id] = round(r.inherent * rem, 6)
        return out


@dataclass(frozen=True)
class TwinResult:
    scenario: str
    changed: str
    baseline: dict
    result: dict
    delta: dict
    interpretation: str
    evidence_type: str = EVIDENCE_TYPE


def _ctl(m: TwinModel, cid: str, **kw) -> TwinModel:
    return replace(m, controls=tuple(replace(c, **kw) if c.control_id == cid else c for c in m.controls))


SCENARIOS: dict[str, Callable[..., Callable[[TwinModel], TwinModel]]] = {
    "control_failure": lambda cid: lambda m: _ctl(m, cid, effective=False),
    "evidence_removal": lambda cid: lambda m: _ctl(m, cid, evidence_present=False),
    "override_increase": lambda f: lambda m: replace(m, override_frequency=f),
    "population_growth": lambda n: lambda m: replace(m, population=n),
    "sod_removal": lambda cid: lambda m: _ctl(m, cid, sod=False),
    "reliability_change": lambda cid, r: lambda m: _ctl(m, cid, evidence_reliability=r),
    "competing_explanation": lambda rid, inh: lambda m: replace(
        m, risks=tuple(replace(r, inherent=inh) if r.risk_id == rid else r for r in m.risks)),
    "key_control_dependency_failure": lambda cid: lambda m: _ctl(m, cid, effective=False),
}


def run_scenario(model: TwinModel, name: str, *args) -> TwinResult:
    base = model.residual()
    new = SCENARIOS[name](*args)(model).residual()
    delta = {k: round(new[k] - base[k], 6) for k in base}
    worse = [k for k, v in delta.items() if v > 0]
    interp = (f"residual risk increases for {worse} under '{name}'" if worse
              else f"no residual-risk increase under '{name}'")
    return TwinResult(name, f"{name}{args}", base, new, delta, interp)
