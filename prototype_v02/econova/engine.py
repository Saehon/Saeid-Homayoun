from __future__ import annotations
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
import hashlib, json, os
from typing import Any
from .prompts import STABLE_CORE, DISCOVERY, ERA, REDTEAM
from .evidence import retrieve_evidence, format_evidence_cards

@dataclass
class StageRecord:
    name: str
    response_id: str | None
    model: str
    reasoning_effort: str
    output: str

@dataclass
class HumanDecision:
    decision: str
    reviewer: str
    note: str

class EconovaEngine:
    def __init__(self, api_key=None, model=None, reasoning_effort=None,
                 allow_web_search=False, vector_store_id=None):
        self.model = model or os.getenv("ECONOVA_MODEL","gpt-5.6-sol")
        self.reasoning_effort = reasoning_effort or os.getenv("ECONOVA_REASONING","high")
        self.allow_web_search = allow_web_search
        self.vector_store_id = vector_store_id or os.getenv("ECONOVA_VECTOR_STORE_ID","").strip() or None
        try:
            from openai import OpenAI
        except ImportError as exc:
            raise RuntimeError(
                "OpenAI SDK is required only for GPT-backed discovery. "
                "Install dependencies with: pip install -r requirements.txt"
            ) from exc
        self.client = OpenAI(api_key=api_key or os.getenv("OPENAI_API_KEY"))

    def _tools(self):
        tools = []
        if self.allow_web_search:
            tools.append({"type":"web_search_preview"})
        if self.vector_store_id:
            tools.append({"type":"file_search","vector_store_ids":[self.vector_store_id]})
        return tools

    def _call(self, name, prompt):
        kw: dict[str,Any] = {
            "model":self.model,
            "reasoning":{"effort":self.reasoning_effort},
            "instructions":STABLE_CORE,
            "input":prompt,
        }
        tools = self._tools()
        if tools:
            kw["tools"] = tools
        r = self.client.responses.create(**kw)
        return StageRecord(name, getattr(r,"id",None), getattr(r,"model",self.model),
                           self.reasoning_effort, r.output_text)

    def run_design(self, question: str, context: str=""):
        cards = retrieve_evidence(question + " " + context, top_k=5)
        ev = format_evidence_cards(cards)
        d = self._call("hypothesis_tournament", DISCOVERY.format(question=question,context=context or "None",evidence=ev))
        e = self._call("era_design", ERA.format(question=question,discovery=d.output,evidence=ev))
        r = self._call("red_team", REDTEAM.format(question=question,discovery=d.output,era=e.output,evidence=ev))
        return cards, [d,e,r]

def make_evidence_passport(question, context, cards, stages, human,
                           data_manifest=None, empirical_manifest=None):
    data_manifest = data_manifest or {}
    empirical_manifest = empirical_manifest or {}
    content = "\n".join([question,context] + [s.output for s in stages])
    approved = human.decision.upper() == "APPROVE FOR NEXT STAGE"
    real_data = bool(data_manifest.get("real_data",False))
    return {
        "project":"ECONOVA-S",
        "prototype":"v0.2 Real Data + Evidence RAG",
        "created_at_utc":datetime.now(timezone.utc).isoformat(),
        "research_question":question,
        "evidence_cards":[{"id":c["id"],"doi":c["doi"],"url":c["url"]} for c in cards],
        "model_backend":stages[0].model if stages else None,
        "stages":[asdict(s) for s in stages],
        "data_manifest":data_manifest,
        "empirical_manifest":empirical_manifest,
        "gates":{
            "literature_prior":bool(cards),
            "systems_map":bool(stages),
            "independent_red_team":len(stages)>=3,
            "real_data_provenance":real_data and bool(data_manifest.get("source")),
            "construct_validation":bool(empirical_manifest.get("construct_validation",False)),
            "credible_identification":bool(empirical_manifest.get("credible_identification",False)),
            "replication_or_oos":bool(empirical_manifest.get("replication_or_oos",False)),
            "economic_significance":bool(empirical_manifest.get("economic_significance",False)),
            "welfare_validation":bool(empirical_manifest.get("welfare_validation",False)),
            "human_gate":approved,
        },
        "human_decision":asdict(human),
        "discovery_claim_allowed":False,
        "next_stage_allowed":approved,
        "content_sha256":hashlib.sha256(content.encode()).hexdigest(),
    }

def passport_json(x):
    return json.dumps(x,indent=2,ensure_ascii=False)
