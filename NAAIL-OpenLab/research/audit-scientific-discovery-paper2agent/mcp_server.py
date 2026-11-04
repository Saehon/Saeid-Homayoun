#!/usr/bin/env python3
"""NAAIL Paper2Agent read-only MCP stdio server (JSON-RPC 2.0).

Implements MCP initialize, tools/list, tools/call, ping, and resources/list.
All research operations are explicitly synthetic. No remote API, data upload,
autonomous professional recommendation, dynamic command execution, or writes.
Compatible with MCP stdio JSON-line framing; never print logs on stdout.
"""
from __future__ import annotations
import json
import sys
from paper_tools import get_paper_method, run_architecture_benchmark, inspect_synthetic_case

VERSION="0.3.0"
DEFAULT_PROTOCOL="2025-06-18"
TOOLS=[
 {"name":"get_paper_method","description":"Return Bao (2020) citation, original-code link, and blocked real-data replication state (no actual original model execution).","inputSchema":{"type":"object","properties":{},"additionalProperties":False}},
 {"name":"run_architecture_benchmark","description":"Run deterministic A0–A3 synthetic architecture demonstration; outputs are not scientific findings.","inputSchema":{"type":"object","properties":{},"additionalProperties":False}},
 {"name":"inspect_synthetic_case","description":"Inspect a SYN-* artificial audit case; no real company assessments.","inputSchema":{"type":"object","properties":{"case_id":{"type":"string","pattern":"^SYN-[0-9]{4}-[0-9]{2}$"}},"required":["case_id"],"additionalProperties":False}},
 {"name":"get_assurance_policy","description":"Read the immutable scientific / audit assurance and independent verification rules.","inputSchema":{"type":"object","properties":{},"additionalProperties":False}},
]
POLICY={
 "no_real_company_analysis":True,
 "no_audit_opinion":True,
 "no_regulator_decision":True,
 "no_claim_of_bao_replication":True,
 "no_autonomous_human_approval":True,
 "synthetic_mode_only":True,
 "cam_interpretation":"High predicted risk without a CAM is NOT evidence of audit failure; apply PCAOB AS 3101.",
 "source_policy":"SEC filings, official PCAOB public material, authorized sources; no proprietary dataset redistribution.",
 "evidence_passport_required":True,
 "scientific_discovery_claim_allowed":False,
 "references":["https://pcaobus.org/oversight/standards/auditing-standards/details/AS3101",
               "https://github.com/JarFraud/FraudDetection",
               "https://github.com/jmiao24/Paper2Agent"]
}
def result(id_,value):
    return {"jsonrpc":"2.0","id":id_,"result":value}
def error(id_,code,message):
    return {"jsonrpc":"2.0","id":id_,"error":{"code":code,"message":message}}
def tool_result(data,is_error=False):
    return {"content":[{"type":"text","text":json.dumps(data,sort_keys=True,ensure_ascii=False)}],
            "isError":is_error}
def dispatch(msg):
    if not isinstance(msg,dict):
        return error(None,-32600,"Invalid Request")
    method=msg.get("method")
    has_id="id" in msg
    reqid=msg.get("id")
    if msg.get("jsonrpc")!="2.0" or not isinstance(method,str):
        return error(reqid,-32600,"Invalid Request")
    if not has_id:
        # Inbound notifications are never replied to; untrusted requests cannot
        # invoke research tools without ids.
        return None
    params=msg.get("params") or {}
    if not isinstance(params,dict):
        return error(reqid,-32602,"Invalid params")
    if method=="initialize":
        return result(reqid,{
           "protocolVersion":DEFAULT_PROTOCOL,"capabilities":{"tools":{"listChanged":False}},
           "serverInfo":{"name":"naail-audit-paper2agent","version":VERSION},
           "instructions":"Scientific/educational synthetic-only tool server. Not a professional audit opinion or reproduction of Bao (2020). Human Approval required."
        })
    if method=="ping":
        return result(reqid,{})
    if method=="tools/list":
        return result(reqid,{"tools":TOOLS})
    if method=="resources/list":
        return result(reqid,{"resources":[]})
    if method=="tools/call":
        name=params.get("name")
        args=params.get("arguments") or {}
        if not isinstance(args,dict):
            return result(reqid,tool_result({"error":"arguments must be object"},True))
        if name=="get_paper_method" and not args:
            return result(reqid,tool_result(get_paper_method()))
        if name=="run_architecture_benchmark" and not args:
            return result(reqid,tool_result(run_architecture_benchmark()))
        if name=="get_assurance_policy" and not args:
            return result(reqid,tool_result(POLICY))
        if name=="inspect_synthetic_case" and set(args)=={"case_id"}:
            try:
                case_id=args["case_id"]
                if not isinstance(case_id,str) or len(case_id)>24:
                    raise ValueError("Invalid synthetic ID")
                return result(reqid,tool_result(inspect_synthetic_case(case_id)))
            except ValueError:
                return result(reqid,tool_result({"error":"Unknown or invalid synthetic case"},True))
        return result(reqid,tool_result({"error":"Unknown tool or invalid arguments"},True))
    return error(reqid,-32601,"Method not found")

def main():
    for line in sys.stdin:
        try:
            if len(line)>256000:
                response=error(None,-32600,"Frame too large")
            else:
                response=dispatch(json.loads(line))
        except (ValueError,TypeError,KeyError,json.JSONDecodeError):
            response=error(None,-32700,"Parse error or invalid input")
        except Exception as e:
            print(f"Internal MCP error: {type(e).__name__}",file=sys.stderr)
            response=error(None,-32603,"Internal error")
        if response is not None:
            sys.stdout.write(json.dumps(response,separators=(",",":"),ensure_ascii=False)+"\n")
            sys.stdout.flush()

if __name__=="__main__":
    main()
