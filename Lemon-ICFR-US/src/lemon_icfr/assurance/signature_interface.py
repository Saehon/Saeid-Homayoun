"""P14 verifier-only interface while asymmetric cryptography is not owner-approved.

The agent-side assurance pipeline may verify a human disposition, but this
interface deliberately exposes no signing operation or private-key material.
"""
from __future__ import annotations

from typing import Protocol

from .human_gate import HumanDisposition


class HumanSignatureVerifier(Protocol):
    """Minimal agent-side contract for an out-of-band human signature verifier."""

    def verify(self, disposition: HumanDisposition) -> None:
        """Raise when the disposition signature is absent, forged, or invalid."""

