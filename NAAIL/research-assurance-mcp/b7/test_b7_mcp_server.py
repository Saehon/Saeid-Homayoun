#!/usr/bin/env python3
"""Unit tests for the B7 stdio MCP transport (stdlib only)."""
from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import naail_mcp_server as server


GRAPH = {
    "graph_id": "test-graph",
    "nodes": [
        {"id": "TABLE_1", "type": "table", "assurance_state": "PARTIAL"},
        {"id": "CODE_1", "type": "code", "assurance_state": "HUMAN_REVIEW"},
    ],
    "edges": [{"from": "TABLE_1", "to": "CODE_1", "relation": "generated_by"}],
}


class SchemaTests(unittest.TestCase):
    def test_all_six_contracts_are_exposed(self) -> None:
        self.assertEqual(set(server.HANDLERS), set(server.SCHEMAS))
        self.assertEqual(len(server.list_tools()), 6)

    def test_invalid_input_is_rejected(self) -> None:
        with self.assertRaises(server.SchemaError):
            server.call_tool("score_detection", {"expected_ids": ["E01"], "detected_ids": [1]})
        with self.assertRaises(server.SchemaError):
            server.call_tool("compare_reported_result", {"reported": 1.0, "regenerated": 1.0, "extra": 1})

    def test_project_path_cannot_escape(self) -> None:
        with self.assertRaises(server.SchemaError):
            server.call_tool("inspect_package", {"root": "../../.."})


class ToolTests(unittest.TestCase):
    def test_existing_assurance_logic_is_wrapped(self) -> None:
        mapped = server.call_tool("map_table_to_code", {"graph": GRAPH, "table_id": "TABLE_1"})
        self.assertEqual(mapped["code_paths"][0]["code"]["id"], "CODE_1")
        trace = server.call_tool("trace_provenance", {"graph": GRAPH, "start_id": "TABLE_1"})
        self.assertEqual([item["id"] for item in trace["nodes"]], ["TABLE_1", "CODE_1"])
        comparison = server.call_tool("compare_reported_result", {"reported": 2.0, "regenerated": 2.0})
        self.assertEqual(comparison["assurance_state"], "CONSISTENT")
        score = server.call_tool("score_detection", {"expected_ids": ["E01"], "detected_ids": ["E01", "E02"]})
        self.assertEqual((score["tp"], score["fp"], score["fn"]), (1, 1, 0))
        report = server.call_tool("generate_assurance_report", {"graph": GRAPH})
        self.assertEqual(report["overall_state"], "PARTIAL")
        inventory = server.call_tool("inspect_package", {"root": "b7"})
        self.assertIn("naail_mcp_server.py", inventory["files"])


class ProtocolTests(unittest.TestCase):
    def test_initialize_list_call_and_errors(self) -> None:
        initialized = server.handle_message({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}})
        self.assertEqual(initialized["result"]["serverInfo"]["name"], server.SERVER_NAME)
        listed = server.handle_message({"jsonrpc": "2.0", "id": 2, "method": "tools/list"})
        self.assertEqual(len(listed["result"]["tools"]), 6)
        called = server.handle_message({
            "jsonrpc": "2.0", "id": 3, "method": "tools/call",
            "params": {"name": "score_detection", "arguments": {"expected_ids": [], "detected_ids": []}},
        })
        self.assertEqual(called["result"]["structuredContent"]["f1"], 1.0)
        invalid = server.handle_message({
            "jsonrpc": "2.0", "id": 4, "method": "tools/call",
            "params": {"name": "score_detection", "arguments": {"expected_ids": "E01", "detected_ids": []}},
        })
        self.assertEqual(invalid["error"]["code"], -32602)
        self.assertIsNone(server.handle_message({"jsonrpc": "2.0", "method": "notifications/initialized"}))

    def test_stdio_round_trip(self) -> None:
        messages = [
            {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}},
            {"jsonrpc": "2.0", "method": "notifications/initialized"},
            {"jsonrpc": "2.0", "id": 2, "method": "tools/list"},
            {"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {
                "name": "compare_reported_result", "arguments": {"reported": 1.0, "regenerated": 1.1, "tolerance": 0.01}
            }},
        ]
        completed = subprocess.run(
            [sys.executable, str(HERE / "naail_mcp_server.py")],
            input="".join(json.dumps(item) + "\n" for item in messages),
            text=True, capture_output=True, check=True,
        )
        responses = [json.loads(line) for line in completed.stdout.splitlines()]
        self.assertEqual([item["id"] for item in responses], [1, 2, 3])
        self.assertEqual(responses[2]["result"]["structuredContent"]["assurance_state"], "FLAGGED")
        self.assertEqual(completed.stderr, "")


if __name__ == "__main__":
    unittest.main(verbosity=2)
