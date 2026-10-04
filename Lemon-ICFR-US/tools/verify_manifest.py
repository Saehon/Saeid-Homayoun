"""P04 POC — re-hash every manifest entry.  Usage: python tools/verify_manifest.py [manifest.json]"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from _common import ROOT, sha256_bytes

DEFAULT = ROOT / "organized" / "evidence" / "msft" / "manifest.json"


def verify(manifest_path: Path) -> list[tuple[str, bool, str]]:
    base, out = manifest_path.parent, []
    for e in json.loads(manifest_path.read_text()):
        p = base / e["path"]
        if not p.exists():
            out.append((e["evidence_id"], False, "missing file"))
        else:
            ok = sha256_bytes(p.read_bytes()) == e["sha256"]
            out.append((e["evidence_id"], ok, "OK" if ok else "HASH MISMATCH"))
    return out


if __name__ == "__main__":
    res = verify(Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT)
    for eid, ok, msg in res:
        print(f"{'OK  ' if ok else 'FAIL'} {eid} {msg}")
    sys.exit(0 if res and all(ok for _, ok, _ in res) else 1)
