"""Offline integrity check for the NAAIL research portfolio navigation.

This validates documentation contracts, not external job availability, authorship
of upstream code, current PR review state, or model-performance claims.
"""
from __future__ import annotations
import json
import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent
PROJECTS_REQUIRED = 9
REPO_PATTERN = re.compile(r"^Saehon/[A-Za-z0-9_.-]+$")
PR_PATTERN = re.compile(r"^https://github\.com/(Saehon/[A-Za-z0-9_.-]+)/pull/([1-9][0-9]*)$")
MARKDOWN = ["README.md", "PROFILE_README_READY.md",
            "PROJECT_EVIDENCE_MATRIX.md", "REPOSITORY_AUDIT_2026-10-31.md"]

def verify_catalog(catalog):
    problems = []
    projects = catalog.get("projects", [])
    if catalog.get("account") != "Saehon":
        problems.append("unexpected account")
    if len(projects) != PROJECTS_REQUIRED:
        problems.append("project count differs from reviewed snapshot")
    seen_ids, seen_priorities = set(), set()
    for item in projects:
        slug = item.get("slug")
        pr_url = item.get("pr_url", "")
        repo = item.get("repo", "")
        match = PR_PATTERN.fullmatch(pr_url)
        if not slug or slug in seen_ids:
            problems.append("empty or duplicate slug")
        seen_ids.add(slug)
        if not REPO_PATTERN.fullmatch(repo):
            problems.append("invalid owner/repo identifier")
        if not match or match.group(1) != repo or int(match.group(2)) != item.get("pr"):
            problems.append("PR URL does not match item metadata")
        if item.get("priority") in seen_priorities:
            problems.append("duplicate priority")
        seen_priorities.add(item.get("priority"))
        if item.get("visibility") not in {"public", "private"}:
            problems.append("unknown visibility for " + str(slug))
        if item.get("evidence_level") != "synthetic_protocol_ci_only":
            problems.append("unsupported evidence maturity claim for " + str(slug))
        for field in ("merged_to_default_branch", "real_provider_inference_verified",
                      "independent_review_approved"):
            if item.get(field) is not False:
                problems.append("unverified positive claim for " + str(slug) + " / " + field)
    if seen_priorities != set(range(1, PROJECTS_REQUIRED + 1)):
        problems.append("nonconsecutive priorities")
    return problems

def verify_markdown():
    errors = []
    for name in MARKDOWN:
        p = ROOT / name
        if not p.is_file():
            errors.append("missing document: " + name)
            continue
        content = p.read_text(encoding="utf-8")
        if not content.strip().startswith("# "):
            errors.append("missing level-1 heading: " + name)
        if "http://github.com/" in content:
            errors.append("insecure GitHub URL in " + name)
        # Follow local relative Markdown links only, not URLs, image assets or anchors.
        for target in re.findall(r"(?<!!)\[[^]]+\]\(([^)]+)\)", content):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            local = (p.parent / target.split("#", 1)[0]).resolve()
            if not local.is_relative_to(ROOT.parent.parent):
                errors.append("local path escapes repository: " + target)
            elif not local.exists():
                errors.append("broken relative link in " + name + ": " + target)
    return errors

def main():
    catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    errors = verify_catalog(catalog) + verify_markdown()
    print(f"Portfolio catalog: {len(catalog.get('projects', []))} roles, "
          f"{len(MARKDOWN)} documents, {len(errors)} integrity issue(s)")
    for issue in errors:
        print("ERROR:", issue)
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
