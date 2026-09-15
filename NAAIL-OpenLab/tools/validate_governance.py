#!/usr/bin/env python3
"""Deterministic governance checks for NAAIL OpenLab.

This validator is intentionally secret-free. It checks public repository state
that should remain invariant regardless of whether Codex/provider credentials
are configured.
"""
from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = ROOT.parent


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def read_text(path: Path) -> str:
    require(path.exists(), f"missing required file: {path.relative_to(REPO_ROOT)}")
    return path.read_text(encoding="utf-8")


def main() -> int:
    version = read_text(ROOT / "VERSION").strip()
    require(version == "0.2.3", f"expected public VERSION 0.2.3, found {version!r}")

    governance = read_text(ROOT / "PORTFOLIO_GOVERNANCE.md")
    lineage = read_text(ROOT / "PROTOTYPE_LINEAGE.md")
    p003c_scope = read_text(ROOT / "PROTOTYPE_003C_SEC_SCOPE.md")
    p003c_status = read_text(ROOT / "PROTOTYPE_003C_IMPLEMENTATION_STATUS.md")
    p003c_snapshot = read_text(ROOT / "PROTOTYPE_003C_SEC_EVIDENCE_SNAPSHOT.md")

    registry_path = ROOT / "portfolio_registry.json"
    registry = json.loads(read_text(registry_path))
    repos = registry.get("repositories", [])
    require(len(repos) == 17, f"portfolio registry must contain exactly 17 repositories, found {len(repos)}")

    by_repo = {item.get("repo"): item for item in repos}
    require(len(by_repo) == 17, "portfolio registry contains duplicate repository names")
    require(
        registry.get("canonical_source_of_truth") == "Saehon/Saeid-Homayoun/NAAIL-OpenLab",
        "canonical source of truth changed",
    )
    require(registry.get("umbrella_platform") == "NAAIL OpenLab", "umbrella platform changed")

    require(by_repo.get("Saehon/yfinance", {}).get("classification") == "UPSTREAM_FORK", "yfinance must remain classified as UPSTREAM_FORK")
    require(by_repo.get("Saehon/timesfm", {}).get("classification") == "UPSTREAM_FORK", "timesfm must remain classified as UPSTREAM_FORK")
    require(by_repo.get("Saehon/Saeid-Homayoun", {}).get("classification") == "CORE_PRODUCT_CANONICAL", "canonical public repo classification changed")
    require(by_repo.get("Saehon/Saeid-Homayoun-", {}).get("classification") == "CORE_RND_STAGING", "private staging repo classification changed")

    for module in ("KIWI", "POMELO", "VERA", "ECONOVA-S"):
        require(module in registry.get("specialist_modules", []), f"missing specialist module: {module}")
        require(module in governance, f"portfolio governance does not mention specialist module: {module}")

    for prototype in ("Prototype 002", "Prototype 003", "Prototype 003-C", "Prototype 004"):
        require(prototype in lineage, f"prototype lineage missing {prototype}")

    approved_companies = ("Microsoft", "Alphabet", "Amazon")
    for company in approved_companies:
        require(company in p003c_scope, f"P003-C scope missing approved company {company}")
    require("No fourth" in p003c_scope or "fourth" in p003c_scope.lower(), "P003-C scope must explicitly prohibit a fourth issuer without versioned change")

    for filename, text in {
        "PROTOTYPE_003C_IMPLEMENTATION_STATUS.md": p003c_status,
        "PROTOTYPE_003C_SEC_EVIDENCE_SNAPSHOT.md": p003c_snapshot,
    }.items():
        require("v0.2.3" in text, f"{filename} must identify v0.2.3 as the public release")
        require("v0.2.2 remains the current public release" not in text, f"{filename} contains stale v0.2.2 release language")

    for required_phrase in ("Evidence Passport", "Professional Decision DAG", "Human Gate"):
        require(required_phrase in governance, f"portfolio governance missing {required_phrase}")

    print("NAAIL governance validation: PASS")
    print(f"public_version={version}")
    print(f"portfolio_repositories={len(repos)}")
    print("p003c_issuer_scope=Microsoft,Alphabet,Amazon")
    print("upstream_forks=yfinance,timesfm")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
