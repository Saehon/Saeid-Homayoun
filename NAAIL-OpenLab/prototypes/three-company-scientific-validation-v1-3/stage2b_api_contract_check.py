#!/usr/bin/env python3
from __future__ import annotations

import argparse
import ast
import hashlib
import json
from pathlib import Path

EXPECTED_CANDIDATES = {
    "C01": ("openai", "gpt-6-astra"),
    "C02": ("google", "gemini-3.8-flash"),
    "C03": ("anthropic", "claude-fable-5"),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def kwmap(call: ast.Call):
    return {kw.arg: kw.value for kw in call.keywords if kw.arg is not None}


def is_false(node):
    return isinstance(node, ast.Constant) and node.value is False


def is_empty_list(node):
    return isinstance(node, ast.List) and len(node.elts) == 0


def name_is(node, value):
    return isinstance(node, ast.Name) and node.id == value


def const_is(node, value):
    return isinstance(node, ast.Constant) and node.value == value


def dict_has(node, key, value):
    if not isinstance(node, ast.Dict):
        return False
    for k, v in zip(node.keys, node.values):
        if const_is(k, key) and const_is(v, value):
            return True
    return False


def find_create_call(fn: ast.FunctionDef, chain_suffix: tuple[str, ...]):
    hits = []
    for n in ast.walk(fn):
        if not isinstance(n, ast.Call):
            continue
        attrs = []
        x = n.func
        while isinstance(x, ast.Attribute):
            attrs.append(x.attr)
            x = x.value
        attrs = tuple(reversed(attrs))
        if attrs[-len(chain_suffix):] == chain_suffix:
            hits.append(n)
    if len(hits) != 1:
        raise AssertionError(f"Expected one call ending {chain_suffix}; found {len(hits)}")
    return hits[0]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runner", type=Path, required=True)
    args = ap.parse_args()
    tree = ast.parse(args.runner.read_text(encoding="utf-8"))
    funcs = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
    errors = []
    checks = []

    candidate_node = next(
        (
            n
            for n in tree.body
            if isinstance(n, ast.Assign)
            and any(isinstance(t, ast.Name) and t.id == "CANDIDATES" for t in n.targets)
        ),
        None,
    )
    if candidate_node is None or not isinstance(candidate_node.value, ast.Dict):
        errors.append("CANDIDATES mapping not found")
    else:
        got = {}
        for k, v in zip(candidate_node.value.keys, candidate_node.value.values):
            if not isinstance(k, ast.Constant) or not isinstance(v, ast.Dict):
                continue
            row = {
                kk.value: vv.value
                for kk, vv in zip(v.keys, v.values)
                if isinstance(kk, ast.Constant) and isinstance(vv, ast.Constant)
            }
            got[k.value] = (row.get("provider"), row.get("model"))
        if got != EXPECTED_CANDIDATES:
            errors.append(f"candidate mapping mismatch: {got!r}")
        else:
            checks.append("candidate model IDs match frozen roster")

    try:
        call = find_create_call(funcs["run_openai"], ("responses", "create"))
        kw = kwmap(call)
        required = {"model", "reasoning", "max_output_tokens", "store", "tools", "instructions", "input"}
        missing = required - set(kw)
        if missing:
            errors.append(f"openai missing keywords: {sorted(missing)}")
        if not is_false(kw.get("store")):
            errors.append("openai store must be False")
        if not is_empty_list(kw.get("tools")):
            errors.append("openai tools must be []")
        if not name_is(kw.get("instructions"), "SYSTEM_CONTRACT"):
            errors.append("openai instructions must be SYSTEM_CONTRACT")
        if not name_is(kw.get("input"), "prompt"):
            errors.append("openai input must be prompt")
        if not dict_has(kw.get("reasoning"), "effort", "high"):
            errors.append("openai reasoning effort must be high")
        for forbidden in ("previous_response_id", "conversation", "background"):
            if forbidden in kw:
                errors.append(f"openai forbidden state keyword present: {forbidden}")
        checks.append("OpenAI request is stateless, no-tools, store=false, high-reasoning")
    except Exception as exc:
        errors.append(f"openai contract parse failed: {exc}")

    try:
        call = find_create_call(funcs["run_google"], ("interactions", "create"))
        kw = kwmap(call)
        required = {"model", "system_instruction", "input", "store", "tools", "generation_config"}
        missing = required - set(kw)
        if missing:
            errors.append(f"google missing keywords: {sorted(missing)}")
        if not is_false(kw.get("store")):
            errors.append("google store must be False")
        if not is_empty_list(kw.get("tools")):
            errors.append("google tools must be []")
        if not name_is(kw.get("system_instruction"), "SYSTEM_CONTRACT"):
            errors.append("google system_instruction must be SYSTEM_CONTRACT")
        if not name_is(kw.get("input"), "prompt"):
            errors.append("google input must be prompt")
        gc = kw.get("generation_config")
        if not dict_has(gc, "thinking_level", "high"):
            errors.append("google thinking_level must be high")
        for forbidden in ("previous_interaction_id", "background"):
            if forbidden in kw:
                errors.append(f"google forbidden state keyword present: {forbidden}")
        checks.append("Google request is stateless, no-tools, store=false, high-thinking")
    except Exception as exc:
        errors.append(f"google contract parse failed: {exc}")

    try:
        call = find_create_call(funcs["run_anthropic"], ("messages", "create"))
        kw = kwmap(call)
        required = {"model", "max_tokens", "system", "output_config", "tools", "messages"}
        missing = required - set(kw)
        if missing:
            errors.append(f"anthropic missing keywords: {sorted(missing)}")
        if not is_empty_list(kw.get("tools")):
            errors.append("anthropic tools must be []")
        if not name_is(kw.get("system"), "SYSTEM_CONTRACT"):
            errors.append("anthropic system must be SYSTEM_CONTRACT")
        if not dict_has(kw.get("output_config"), "effort", "high"):
            errors.append("anthropic output_config effort must be high")
        if "thinking" in kw:
            errors.append(
                "anthropic Fable 5 runner should rely on default adaptive thinking; "
                "explicit manual thinking config is not permitted in this lock"
            )
        checks.append(
            "Anthropic request is no-tools and uses Fable 5 high effort without manual thinking budget"
        )
    except Exception as exc:
        errors.append(f"anthropic contract parse failed: {exc}")

    result = {
        "runner": str(args.runner),
        "runner_sha256": sha256(args.runner),
        "status": "PASS" if not errors else "FAIL",
        "checks": checks,
        "errors": errors,
        "provider_calls_executed": False,
        "credentials_loaded": False,
        "scoring_opened": False,
    }
    print(json.dumps(result, indent=2))
    return 0 if not errors else 2


if __name__ == "__main__":
    raise SystemExit(main())
