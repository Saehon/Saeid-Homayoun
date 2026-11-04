"""Benchmark integrity (sections 14-15). Development evidence never becomes confirmatory."""
from __future__ import annotations

from dataclasses import dataclass, replace
from typing import Optional

from .errors import LeakageError

CLASSIFICATIONS = ("CANONICAL", "DERIVED_COPY", "ARCHIVAL_COPY", "EXTERNAL_EXPORT",
                   "DEPRECATED", "NON_EXECUTABLE_REFERENCE")
DESIGNATIONS = ("DEVELOPMENT", "SPENT_PROBE", "HOLDOUT")


@dataclass(frozen=True)
class BenchmarkArtifact:
    name: str
    path: str
    classification: str
    dataset_version: str
    sha256: str
    labels_sha256: str
    eval_code_version: str
    environment: str
    provenance: str
    rights: str

    def __post_init__(self):
        if self.classification not in CLASSIFICATIONS:
            raise ValueError(self.classification)


@dataclass(frozen=True)
class BenchmarkCase:
    case_id: str
    content_sha256: str
    designation: str
    author: str
    frozen_at: Optional[str] = None
    inspected_by: tuple[str, ...] = ()


class BenchmarkRegistry:
    def __init__(self):
        self.artifacts: dict[str, list[BenchmarkArtifact]] = {}
        self.cases: dict[str, BenchmarkCase] = {}
        self.log: list[str] = []

    def add_artifact(self, a: BenchmarkArtifact) -> None:
        existing = self.artifacts.setdefault(a.name, [])
        if a.classification == "CANONICAL" and any(x.classification == "CANONICAL" for x in existing):
            raise LeakageError(f"second CANONICAL source for benchmark {a.name!r}")
        existing.append(a)

    def executable(self, name: str) -> BenchmarkArtifact:
        canon = [a for a in self.artifacts.get(name, []) if a.classification == "CANONICAL"]
        if len(canon) != 1:
            raise LeakageError(f"benchmark {name!r} has {len(canon)} canonical sources; need exactly 1")
        return canon[0]

    def add_case(self, c: BenchmarkCase) -> None:
        if c.designation not in DESIGNATIONS:
            raise ValueError(c.designation)
        if c.case_id in self.cases:
            raise LeakageError(f"case {c.case_id} already registered; designations cannot be rewritten")
        self.cases[c.case_id] = c
        self.check_leakage()

    def inspect(self, case_id: str, by: str) -> None:
        c = self.cases[case_id]
        new = "SPENT_PROBE" if c.designation == "HOLDOUT" else c.designation
        self.cases[case_id] = replace(c, designation=new, inspected_by=c.inspected_by + (by,))
        self.log.append(f"{case_id} inspected by {by}: {c.designation} -> {new}")

    def relabel(self, case_id: str, designation: str) -> None:
        order = {"HOLDOUT": 0, "DEVELOPMENT": 1, "SPENT_PROBE": 2}
        c = self.cases[case_id]
        if order[designation] < order[c.designation]:
            raise LeakageError(f"cannot relabel {c.designation} -> {designation}: development evidence never becomes holdout")
        self.cases[case_id] = replace(c, designation=designation)

    def check_leakage(self) -> None:
        dev = {c.content_sha256 for c in self.cases.values() if c.designation != "HOLDOUT"}
        hold = {c.content_sha256 for c in self.cases.values() if c.designation == "HOLDOUT"}
        if dev & hold:
            raise LeakageError(f"holdout content identical to development content: {sorted(dev & hold)[:3]}")

    def assert_confirmatory(self, case_ids, implementer: str, executed_at: str) -> None:
        self.check_leakage()
        for cid in case_ids:
            c = self.cases[cid]
            if c.designation != "HOLDOUT":
                raise LeakageError(f"{cid} is {c.designation}, not a holdout")
            if c.inspected_by:
                raise LeakageError(f"{cid} was inspected during development")
            if not c.frozen_at or c.frozen_at >= executed_at:
                raise LeakageError(f"{cid} not frozen before execution")
            if c.author == implementer:
                raise LeakageError(f"{cid} authored by the implementer; not independent")
