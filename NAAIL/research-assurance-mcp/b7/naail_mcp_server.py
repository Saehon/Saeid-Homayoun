#!/usr/bin/env python3
"""Bounded stdio MCP server for the existing NAAIL P5 POC functions.

This transport layer validates tool inputs and outputs. It does not alter the
assurance logic, execute research data, or promote assurance states.
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from typing import Any, Callable, Dict

PROJECT_ROOT = Path(__file__).resolve().parents[1]
P5_ROOT = PROJECT_ROOT / "p5"
sys.path.insert(0, str(P5_ROOT))

from naail_mcp_poc import (  # noqa: E402
    compare_reported_result,
    generate_assurance_report,
    inspect_package,
    map_table_to_code,
    score_detection,
    trace_provenance,
)

SERVER_NAME = "naail-research-assurance-mcp"
SERVER_VERSION = "0.1.0-b7"
PROTOCOL_VERSION = "2025-06-18"
SCHEMAS = json.loads((Path(__file__).with_name("tool_schemas.json")).read_text(encoding="utf-8"))["tools"]


class SchemaError(ValueError):
    """Raised when a tool input or output violates its frozen JSON schema."""


def _matches_type(value: Any, expected: str) -> bool:
    if expected == "null":
        return value is None
    if expected == "object":
        return isinstance(value, dict)
    if expected == "array":
        return isinstance(value, list)
    if expected == "string":
        return isinstance(value, str)
    if expected == "boolean":
        return isinstance(value, bool)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)
    return False


def validate(instance: Any, schema: Dict[str, Any], path: str = "$") -> None:
    """Validate the JSON-Schema subset used by the frozen B7 contracts."""
    declared = schema.get("type")
    expected = declared if isinstance(declared, list) else [declared]
    if declared is not None and not any(_matches_type(instance, item) for item in expected):
        raise SchemaError(f"{path}: expected {declared}")
    if "enum" in schema and instance not in schema["enum"]:
        raise SchemaError(f"{path}: value is not in enum")
    if isinstance(instance, (int, float)) and not isinstance(instance, bool):
        if "minimum" in schema and instance < schema["minimum"]:
            raise SchemaError(f"{path}: value is below minimum")
    if isinstance(instance, dict):
        properties = schema.get("properties", {})
        for key in schema.get("required", []):
            if key not in instance:
                raise SchemaError(f"{path}.{key}: required property missing")
        if schema.get("additionalProperties") is False:
            extra = sorted(set(instance) - set(properties))
            if extra:
                raise SchemaError(f"{path}: unexpected properties {extra}")
        for key, value in instance.items():
            if key in properties:
                validate(value, properties[key], f"{path}.{key}")
    if isinstance(instance, list) and "items" in schema:
        for index, value in enumerate(instance):
            validate(value, schema["items"], f"{path}[{index}]")


def _project_path(raw: str) -> Path:
    candidate = (PROJECT_ROOT / raw).resolve()
    try:
        candidate.relative_to(PROJECT_ROOT.resolve())
    except ValueError as exc:
        raise SchemaError("$.root: path must stay within the research-assurance-mcp project") from exc
    if not candidate.is_dir():
        raise SchemaError("$.root: directory does not exist")
    return candidate


def _inspect(arguments: Dict[str, Any]) -> Dict[str, Any]:
    root = _project_path(arguments["root"])
    result = inspect_package(root)
    result["root"] = str(root.relative_to(PROJECT_ROOT)) or "."
    return result


def _map(arguments: Dict[str, Any]) -> Dict[str, Any]:
    return map_table_to_code(arguments["graph"], arguments["table_id"])


def _compare(arguments: Dict[str, Any]) -> Dict[str, Any]:
    return compare_reported_result(
        arguments["reported"], arguments["regenerated"], arguments.get("tolerance", 1e-9)
    )


def _trace(arguments: Dict[str, Any]) -> Dict[str, Any]:
    return trace_provenance(arguments["graph"], arguments["start_id"])


def _score(arguments: Dict[str, Any]) -> Dict[str, Any]:
    return score_detection(arguments["expected_ids"], arguments["detected_ids"])


def _report(arguments: Dict[str, Any]) -> Dict[str, Any]:
    return generate_assurance_report(arguments["graph"])


HANDLERS: Dict[str, Callable[[Dict[str, Any]], Dict[str, Any]]] = {
    "inspect_package": _inspect,
    "map_table_to_code": _map,
    "compare_reported_result": _compare,
    "trace_provenance": _trace,
    "score_detection": _score,
    "generate_assurance_report": _report,
}


def list_tools() -> list[Dict[str, Any]]:
    return [
        {
            "name": name,
            "description": contract["description"],
            "inputSchema": contract["inputSchema"],
            "outputSchema": contract["outputSchema"],
        }
        for name, contract in SCHEMAS.items()
    ]


def call_tool(name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
    if name not in HANDLERS:
        raise SchemaError(f"unknown tool: {name}")
    contract = SCHEMAS[name]
    validate(arguments, contract["inputSchema"])
    result = HANDLERS[name](arguments)
    validate(result, contract["outputSchema"])
    return result


def _success(request_id: Any, result: Dict[str, Any]) -> Dict[str, Any]:
    return {"jsonrpc": "2.0", "id": request_id, "result": result}


def _error(request_id: Any, code: int, message: str) -> Dict[str, Any]:
    return {"jsonrpc": "2.0", "id": request_id, "error": {"code": code, "message": message}}


def handle_message(message: Any) -> Dict[str, Any] | None:
    if not isinstance(message, dict) or message.get("jsonrpc") != "2.0":
        return _error(message.get("id") if isinstance(message, dict) else None, -32600, "Invalid Request")
    request_id, method = message.get("id"), message.get("method")
    if method == "notifications/initialized":
        return None
    if method == "initialize":
        return _success(
            request_id,
            {
                "protocolVersion": PROTOCOL_VERSION,
                "capabilities": {"tools": {"listChanged": False}},
                "serverInfo": {"name": SERVER_NAME, "version": SERVER_VERSION},
            },
        )
    if method == "tools/list":
        return _success(request_id, {"tools": list_tools()})
    if method == "tools/call":
        params = message.get("params", {})
        try:
            result = call_tool(params.get("name"), params.get("arguments", {}))
        except SchemaError as exc:
            return _error(request_id, -32602, str(exc))
        except Exception as exc:  # defensive transport boundary; no traceback or data leakage
            return _error(request_id, -32603, f"Tool execution failed: {type(exc).__name__}")
        return _success(
            request_id,
            {
                "content": [{"type": "text", "text": json.dumps(result, sort_keys=True)}],
                "structuredContent": result,
                "isError": False,
            },
        )
    return _error(request_id, -32601, "Method not found")


def main() -> int:
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            message = json.loads(line)
        except json.JSONDecodeError:
            response = _error(None, -32700, "Parse error")
        else:
            response = handle_message(message)
        if response is not None:
            sys.stdout.write(json.dumps(response, separators=(",", ":")) + "\n")
            sys.stdout.flush()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
