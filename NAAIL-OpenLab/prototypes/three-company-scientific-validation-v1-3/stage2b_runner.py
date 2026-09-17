#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import os
import platform
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

CANDIDATES = {
    "C01": {"provider": "openai", "model": "gpt-6-astra", "api_key_env": "OPENAI_API_KEY"},
    "C02": {"provider": "google", "model": "gemini-3.8-flash", "api_key_env": "GEMINI_API_KEY"},
    "C03": {"provider": "anthropic", "model": "claude-fable-5", "api_key_env": "ANTHROPIC_API_KEY"},
}

FORBIDDEN_TASK_KEYS = {
    "answer", "answers", "gold", "gold_key", "gold_answer", "expected_answer",
    "reference_answer", "rubric", "scoring_rubric", "score_key"
}

SYSTEM_CONTRACT = """You are participating in a blind professional accounting and auditing benchmark.
Use only the evidence and task supplied in this request.
Do not use browsing, external tools, external files, prior conversation, or unstated outside facts.
If the evidence is insufficient, say REQUEST_MORE_EVIDENCE and explain the missing evidence.
Preserve contradictions and uncertainty rather than forcing a conclusion.
Return only the answer to the benchmark task; do not discuss benchmark scoring or speculate about a gold key."""


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def sha256_bytes(data: bytes):
    return hashlib.sha256(data).hexdigest()


def file_sha256(path: Path):
    return sha256_bytes(path.read_bytes())


def is_within(child: Path, parent: Path):
    child = child.resolve()
    parent = parent.resolve()
    try:
        child.relative_to(parent)
        return True
    except ValueError:
        return False


def find_git_root(path: Path):
    p = path.resolve()
    if p.is_file():
        p = p.parent
    for candidate in [p, *p.parents]:
        if (candidate / ".git").exists():
            return candidate
    return None


def load_tasks(path: Path):
    tasks = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        obj = json.loads(line)
        if not obj.get("task_id") or not obj.get("prompt"):
            raise ValueError(f"{path}:{line_no} requires task_id and prompt")
        leaked = FORBIDDEN_TASK_KEYS.intersection({str(k).lower() for k in obj})
        if leaked:
            raise ValueError(
                f"{path}:{line_no} contains forbidden blind-evaluation fields: {sorted(leaked)}"
            )
        tasks.append(obj)
    if len(tasks) != 21:
        raise ValueError(f"Expected 21 tasks for V1.3B; found {len(tasks)}")
    ids = [str(t["task_id"]) for t in tasks]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate task_id values are not allowed")
    return tasks


def package_version(name):
    try:
        return importlib.metadata.version(name)
    except importlib.metadata.PackageNotFoundError:
        return None


def safe_model_dump(obj):
    if obj is None:
        return None
    if hasattr(obj, "model_dump"):
        return obj.model_dump()
    if hasattr(obj, "to_dict"):
        return obj.to_dict()
    if hasattr(obj, "dict"):
        return obj.dict()
    return str(obj)


def run_openai(model, prompt):
    from openai import OpenAI

    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    start = time.perf_counter()
    response = client.responses.create(
        model=model,
        reasoning={"effort": "high"},
        max_output_tokens=16000,
        store=False,
        tools=[],
        instructions=SYSTEM_CONTRACT,
        input=prompt,
    )
    return {
        "text": getattr(response, "output_text", None),
        "provider_response": safe_model_dump(response),
        "usage": safe_model_dump(getattr(response, "usage", None)),
        "latency_ms": round((time.perf_counter() - start) * 1000, 3),
    }


def run_google(model, prompt):
    from google import genai

    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    start = time.perf_counter()
    response = client.interactions.create(
        model=model,
        system_instruction=SYSTEM_CONTRACT,
        input=prompt,
        store=False,
        tools=[],
        generation_config={"thinking_level": "high", "max_output_tokens": 16000},
    )
    return {
        "text": getattr(response, "output_text", None),
        "provider_response": safe_model_dump(response),
        "usage": safe_model_dump(getattr(response, "usage", None)),
        "latency_ms": round((time.perf_counter() - start) * 1000, 3),
    }


def run_anthropic(model, prompt):
    import anthropic

    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    start = time.perf_counter()
    response = client.messages.create(
        model=model,
        max_tokens=16000,
        system=SYSTEM_CONTRACT,
        output_config={"effort": "high"},
        tools=[],
        messages=[{"role": "user", "content": prompt}],
    )
    text_parts = [
        getattr(block, "text", "")
        for block in getattr(response, "content", [])
        if getattr(block, "type", None) == "text"
    ]
    return {
        "text": "\n".join(text_parts),
        "provider_response": safe_model_dump(response),
        "usage": safe_model_dump(getattr(response, "usage", None)),
        "latency_ms": round((time.perf_counter() - start) * 1000, 3),
    }


RUNNERS = {"openai": run_openai, "google": run_google, "anthropic": run_anthropic}


def build_prompt(evidence, task):
    return (
        "<FROZEN_EVIDENCE>\n" + evidence + "\n</FROZEN_EVIDENCE>\n\n"
        "<BENCHMARK_TASK>\n" + str(task["prompt"]) + "\n</BENCHMARK_TASK>"
    )


def enforce_preflight(a, candidate):
    if not a.tasks.exists() or not a.tasks.is_file():
        raise ValueError(f"Task file not found: {a.tasks}")
    if not a.evidence.exists() or not a.evidence.is_file():
        raise ValueError(f"Evidence file not found: {a.evidence}")

    tasks_hash = file_sha256(a.tasks)
    evidence_hash = file_sha256(a.evidence)

    if a.expected_tasks_sha256 and tasks_hash.lower() != a.expected_tasks_sha256.lower():
        raise ValueError("Task packet SHA-256 does not match the registered frozen hash")
    if a.expected_evidence_sha256 and evidence_hash.lower() != a.expected_evidence_sha256.lower():
        raise ValueError("Evidence packet SHA-256 does not match the registered frozen hash")

    for sensitive_name, path in (("tasks", a.tasks), ("evidence", a.evidence)):
        lower = str(path).lower()
        if "gold_key" in lower or "gold-key" in lower:
            raise ValueError(f"{sensitive_name} path appears to point to a gold-key artifact")

    git_root = find_git_root(a.output_dir)
    if git_root and is_within(a.output_dir, git_root) and not a.allow_output_in_git_worktree:
        raise ValueError(
            f"Refusing to write private run outputs inside Git worktree {git_root}. "
            "Use a private directory outside the repository."
        )

    if not a.dry_run:
        if not a.confirm_blind:
            raise ValueError("Live execution requires --confirm-blind")
        env_name = candidate["api_key_env"]
        if not os.environ.get(env_name):
            raise ValueError(f"Missing required environment variable: {env_name}")

    return tasks_hash, evidence_hash


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--candidate", choices=sorted(CANDIDATES), required=True)
    p.add_argument("--tasks", type=Path, required=True)
    p.add_argument("--evidence", type=Path, required=True)
    p.add_argument("--output-dir", type=Path, required=True)
    p.add_argument("--packet-version", default="V1.3B_PRIVATE_21_TASK")
    p.add_argument("--expected-tasks-sha256")
    p.add_argument("--expected-evidence-sha256")
    p.add_argument("--price-source", default="UNAVAILABLE")
    p.add_argument("--input-price-per-m", type=float)
    p.add_argument("--output-price-per-m", type=float)
    p.add_argument("--confirm-blind", action="store_true")
    p.add_argument("--allow-output-in-git-worktree", action="store_true")
    p.add_argument("--dry-run", action="store_true")
    a = p.parse_args()

    candidate = CANDIDATES[a.candidate]
    tasks_hash, evidence_hash = enforce_preflight(a, candidate)
    tasks = load_tasks(a.tasks)
    evidence = a.evidence.read_text(encoding="utf-8")

    run_id = f"{a.candidate}-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}"
    run_dir = a.output_dir / run_id
    run_dir.mkdir(parents=True, exist_ok=False)

    pre = {
        "run_id": run_id,
        "candidate_id": a.candidate,
        "provider": candidate["provider"],
        "model": candidate["model"],
        "packet_version": a.packet_version,
        "started_utc": utc_now(),
        "tasks_sha256": tasks_hash,
        "evidence_sha256": evidence_hash,
        "task_count": len(tasks),
        "browsing_mode": "DISABLED_BY_REQUEST_DESIGN",
        "tool_access": "NONE_SUPPLIED",
        "session_design": "STATELESS_REQUEST_PER_TASK",
        "provider_storage_request": "DISABLED_WHERE_API_SUPPORTS_STORE_FALSE",
        "reasoning_setting": "HIGH",
        "max_output_tokens_per_task": 16000,
        "gold_key_access": "NOT_AVAILABLE_TO_RUNNER",
        "price_source": a.price_source,
        "input_price_per_m": a.input_price_per_m,
        "output_price_per_m": a.output_price_per_m,
        "python_version": sys.version,
        "platform": platform.platform(),
        "sdk_versions": {
            "openai": package_version("openai"),
            "google-genai": package_version("google-genai"),
            "anthropic": package_version("anthropic"),
        },
        "dry_run": a.dry_run,
        "scoring_opened": False,
    }
    (run_dir / "pre_manifest.json").write_text(json.dumps(pre, indent=2), encoding="utf-8")

    if a.dry_run:
        print(json.dumps(pre, indent=2))
        return 0

    runner_fn = RUNNERS[candidate["provider"]]
    records = []
    for task in tasks:
        task_id = str(task["task_id"])
        rec = {"task_id": task_id, "started_utc": utc_now(), "status": "STARTED"}
        try:
            rec.update(runner_fn(candidate["model"], build_prompt(evidence, task)))
            rec["status"] = "EXECUTED"
        except Exception as exc:
            rec.update(
                {
                    "status": "FAILED_CALL",
                    "error_type": type(exc).__name__,
                    "error_message": str(exc),
                }
            )
        rec["finished_utc"] = utc_now()

        raw = json.dumps(rec, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()
        path = run_dir / f"{task_id}.json"
        path.write_bytes(raw)
        digest = sha256_bytes(raw)
        (run_dir / f"{task_id}.sha256").write_text(
            f"{digest}  {path.name}\n", encoding="utf-8"
        )
        rec["response_artifact"] = path.name
        rec["response_sha256"] = digest
        records.append(rec)

    index = [
        {
            "task_id": r["task_id"],
            "status": r["status"],
            "response_artifact": r["response_artifact"],
            "response_sha256": r["response_sha256"],
            "latency_ms": r.get("latency_ms"),
        }
        for r in records
    ]
    index_raw = json.dumps(index, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()
    index_path = run_dir / "response_freeze_index.json"
    index_path.write_bytes(index_raw)

    final = {
        **pre,
        "finished_utc": utc_now(),
        "run_status": (
            "EXECUTED"
            if all(r["status"] == "EXECUTED" for r in records)
            else "EXECUTED_WITH_FAILURES"
        ),
        "executed_count": sum(r["status"] == "EXECUTED" for r in records),
        "failed_count": sum(r["status"] != "EXECUTED" for r in records),
        "response_freeze_index": index_path.name,
        "response_freeze_index_sha256": sha256_bytes(index_raw),
        "scoring_opened": False,
    }
    final_raw = json.dumps(final, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()
    manifest_path = run_dir / "run_manifest.json"
    manifest_path.write_bytes(final_raw)
    manifest_digest = sha256_bytes(final_raw)
    (run_dir / "run_manifest.sha256").write_text(
        f"{manifest_digest}  {manifest_path.name}\n", encoding="utf-8"
    )
    print(json.dumps(final, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
