"""P09 — Structure discovery graph. "AlphaFold-inspired" = structural analogy only.

Edges are CANDIDATE by default. VALIDATED requires linked admissible evidence and
no open contradiction. The graph never upgrades its own edges.
"""
from __future__ import annotations

import json
from dataclasses import asdict, dataclass

from .errors import LemonError
from .evidence import EvidenceStore

KINDS = ("process", "account", "assertion", "risk", "control", "evidence")
ALLOWED = {("process", "account"), ("account", "assertion"), ("assertion", "risk"), ("risk", "control"),
           ("control", "evidence"), ("account", "evidence"), ("assertion", "evidence")}
STATUSES = ("CANDIDATE", "VALIDATED", "REJECTED")


class GraphError(LemonError): ...


@dataclass(frozen=True)
class Node:
    node_id: str
    kind: str
    label: str


@dataclass(frozen=True)
class Edge:
    src: str
    dst: str
    relation: str
    confidence: float
    evidence_required: str
    provenance: str
    evidence_ids: tuple[str, ...] = ()
    status: str = "CANDIDATE"
    contradiction: str = "NONE"


class StructureGraph:
    def __init__(self, store: EvidenceStore):
        self.store, self.nodes, self.edges = store, {}, []

    def add_node(self, n: Node) -> None:
        if n.kind not in KINDS:
            raise GraphError(f"unknown node kind {n.kind}")
        self.nodes[n.node_id] = n

    def add_edge(self, e: Edge) -> None:
        if e.src not in self.nodes or e.dst not in self.nodes:
            raise GraphError("edge endpoints must exist")
        pair = (self.nodes[e.src].kind, self.nodes[e.dst].kind)
        if pair not in ALLOWED:
            raise GraphError(f"relation {pair} not allowed")
        if not 0.0 <= e.confidence <= 1.0:
            raise GraphError("confidence must be in [0,1]")
        if e.status not in STATUSES:
            raise GraphError(f"unknown status {e.status}")
        if not e.provenance or not e.evidence_required:
            raise GraphError("edge needs provenance and an evidence requirement")
        if e.status == "VALIDATED":
            if not e.evidence_ids:
                raise GraphError("VALIDATED edge without evidence")
            for i in e.evidence_ids:
                ev = self.store.get(i)
                if ev is None or ev.admissibility_issues():
                    raise GraphError(f"VALIDATED edge cites inadmissible/missing evidence {i}")
            if e.contradiction != "NONE":
                raise GraphError("VALIDATED edge with open contradiction")
        self.edges.append(e)

    def to_json(self) -> str:
        return json.dumps({"analogy_note": "structural analogy only; AlphaFold is not used",
                           "nodes": [asdict(n) for n in self.nodes.values()],
                           "edges": [asdict(e) for e in self.edges]}, sort_keys=True, indent=2)
