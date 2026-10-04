"""P11 guard — files classified as mock / non-executable / archival can never become evidence."""
from __future__ import annotations

import re
from pathlib import Path
from typing import Mapping, Optional

from .enums import Rights, SourceTier
from .errors import LemonError
from .evidence import EvidenceItem, make_evidence

BLOCKED_CLASSES = {"NON_EXECUTABLE_REFERENCE", "ARCHIVAL_COPY", "DEPRECATED"}
MOCK = re.compile(r"(^|[_\-/.])(mock|fake|dummy|stub)([_\-/.]|$)", re.I)


class InadmissibleSourceError(LemonError): ...


def load_file_evidence(path: Path, *, evidence_id: str, provenance: str, tier: SourceTier, rights: Rights,
                       registry: Optional[Mapping[str, str]] = None, facts=(), **kw) -> EvidenceItem:
    p = Path(path)
    if MOCK.search(p.as_posix()):
        raise InadmissibleSourceError(f"{p.name}: mock/fake/stub artifacts are never evidence")
    cls = (registry or {}).get(p.as_posix())
    if cls in BLOCKED_CLASSES:
        raise InadmissibleSourceError(f"{p.name}: registry class {cls} is not admissible evidence")
    return make_evidence(evidence_id, content=p.read_bytes(), provenance=provenance, tier=tier, rights=rights,
                         facts=facts, source=p.as_posix(), **kw)
