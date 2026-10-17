"""Canonical-path enforcement: no traversal, no symlinks, hash-what-you-use (no TOCTOU)."""
from __future__ import annotations

import hashlib
import os
from pathlib import Path

from .errors import IntegrityError, PathSecurityError


def read_canonical(base: Path, rel: str, expected_sha256: str) -> bytes:
    rp = Path(rel)
    if rp.is_absolute() or ".." in rp.parts:
        raise PathSecurityError(f"non-canonical path {rel!r}")
    base = Path(base).resolve(strict=True)
    cur = base
    for part in rp.parts:
        cur = cur / part
        if cur.is_symlink():
            raise PathSecurityError(f"symlink in canonical path: {cur}")
    target = cur.resolve(strict=True)
    if base not in target.parents:
        raise PathSecurityError("path escapes canonical root")
    fd = os.open(target, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0))
    try:
        chunks = []
        while True:
            b = os.read(fd, 1 << 20)
            if not b:
                break
            chunks.append(b)
    finally:
        os.close(fd)
    data = b"".join(chunks)
    if hashlib.sha256(data).hexdigest() != expected_sha256:
        raise IntegrityError(f"checksum mismatch for {rel}")
    return data    # callers must use THESE bytes; never re-open the file
