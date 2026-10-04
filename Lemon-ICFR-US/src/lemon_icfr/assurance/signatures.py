"""P14 — Ed25519 human-disposition signatures (ORQ-005). Optional dependency: `cryptography`.

The PRIVATE key lives only in the human approval UI. The agent pipeline holds only the
PUBLIC key, so it can verify but never sign. Enable only if the owner approved the dependency.
"""
from __future__ import annotations

from .errors import SelfApprovalError
from .human_gate import HumanDisposition

try:
    from cryptography.exceptions import InvalidSignature
    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
    AVAILABLE = True
except ImportError:  # dependency not approved / not installed
    AVAILABLE = False


class Ed25519Verifier:
    def __init__(self, public_key_bytes: bytes):
        if not AVAILABLE:
            raise RuntimeError("cryptography not installed; Ed25519 disabled (ORQ-005 pending owner approval)")
        self._pk = Ed25519PublicKey.from_public_bytes(public_key_bytes)

    def verify(self, d: HumanDisposition) -> None:
        try:
            self._pk.verify(bytes.fromhex(d.signature), d.payload())
        except (InvalidSignature, ValueError) as e:
            raise SelfApprovalError("invalid Ed25519 human signature") from e
