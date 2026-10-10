"""Black-box MCP/JSON-RPC protocol tests: no paid keys, network, external models."""
import json
import subprocess
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).parent
def call_server(messages):
    lines="\n".join(json.dumps(m) for m in messages)+"\n"
    proc=subprocess.run([sys.executable,str(ROOT/"mcp_server.py")],
       input=lines,text=True,capture_output=True,timeout=15,cwd=ROOT)
    if proc.returncode:
        raise AssertionError(proc.stderr)
    return [json.loads(line) for line in proc.stdout.splitlines()]
def req(id_,method,params=None):
    return {"jsonrpc":"2.0","id":id_,"method":method,
            **({"params":params} if params is not None else {})}

class McpProtocolTest(unittest.TestCase):
    def test_full_mcp_handshake_and_tools(self):
        msg=[req(1,"initialize",{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"unit-test","version":"1"}}),
             {"jsonrpc":"2.0","method":"notifications/initialized"},
             req(2,"tools/list"),
             req(3,"tools/call",{"name":"get_paper_method","arguments":{}}),
             req(4,"tools/call",{"name":"inspect_synthetic_case","arguments":{"case_id":"SYN-2024-00"}}),
             req(5,"tools/call",{"name":"get_assurance_policy","arguments":{}})]
        out=call_server(msg)
        self.assertEqual(len(out),5)
        self.assertIn("tools",out[1]["result"])
        self.assertEqual(len(out[1]["result"]["tools"]),4)
        original=json.loads(out[2]["result"]["content"][0]["text"])
        self.assertEqual(original["execution_status"],"ORIGINAL_AUTHOR_MODEL_NOT_REPRODUCED")
        case=json.loads(out[3]["result"]["content"][0]["text"])
        self.assertEqual(case["source_type"],"SYNTHETIC")
        self.assertFalse(case["audit_failure_claim_allowed"])
        policy=json.loads(out[4]["result"]["content"][0]["text"])
        self.assertTrue(policy["no_autonomous_human_approval"])
    def test_benchmark_in_mcp(self):
        output=call_server([req(1,"tools/call",{"name":"run_architecture_benchmark","arguments":{}})])
        data=json.loads(output[0]["result"]["content"][0]["text"])
        self.assertFalse(data["scientific_discovery_claim_allowed"])
        self.assertEqual(data["splits"]["test_n"],20)
    def test_invalid_arguments_and_no_execution(self):
        out=call_server([
          req(1,"tools/call",{"name":"inspect_synthetic_case","arguments":{"case_id":"MSFT"}}),
          req(2,"tools/call",{"name":"arbitrary/execution"}),
          req(3,"tools/call",{"name":"run_architecture_benchmark","arguments":{"file":"/etc/passwd"}})
        ])
        self.assertTrue(out[0]["result"]["isError"])
        self.assertEqual(out[1]["error"]["code"],-32601)
        self.assertTrue(out[2]["result"]["isError"])
    def test_invalid_json(self):
        p=subprocess.run([sys.executable,str(ROOT/"mcp_server.py")],
                         input="{ invalid json }\n",text=True,capture_output=True,timeout=15)
        self.assertEqual(json.loads(p.stdout)["error"]["code"],-32700)

if __name__=="__main__":
    unittest.main()
