from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class AuditConfig:
    approval_threshold: float = float(os.getenv("AUDIT_APPROVAL_THRESHOLD", "10000"))
    large_round_threshold: float = float(os.getenv("AUDIT_LARGE_ROUND_THRESHOLD", "10000"))
    mad_multiplier: float = float(os.getenv("AUDIT_MAD_MULTIPLIER", "6"))
    working_hour_start: int = int(os.getenv("AUDIT_WORKING_HOUR_START", "6"))
    working_hour_end: int = int(os.getenv("AUDIT_WORKING_HOUR_END", "22"))


DEFAULT_CONFIG = AuditConfig()
