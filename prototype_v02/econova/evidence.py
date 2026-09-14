from __future__ import annotations
from pathlib import Path
import json
import re
from typing import Iterable

DEFAULT_REGISTRY = Path(__file__).resolve().parents[1] / "evidence" / "registry.json"

def load_registry(path: str | Path = DEFAULT_REGISTRY) -> list[dict]:
    return json.loads(Path(path).read_text(encoding="utf-8"))

def _tokens(text: str) -> set[str]:
    return {x for x in re.findall(r"[a-zA-Z0-9]+", text.lower()) if len(x) > 2}

def retrieve_evidence(query: str, registry: list[dict] | None = None, top_k: int = 5) -> list[dict]:
    registry = registry or load_registry()
    q = _tokens(query)
    scored = []
    for card in registry:
        hay = " ".join([
            card.get("title",""), card.get("journal",""), card.get("note",""),
            " ".join(card.get("domains",[])), card.get("evidence_role","")
        ])
        t = _tokens(hay)
        overlap = len(q & t)
        phrase_bonus = sum(2 for d in card.get("domains",[]) if d.lower() in query.lower())
        scored.append((overlap + phrase_bonus, card))
    scored.sort(key=lambda x: (x[0], x[1].get("year",0)), reverse=True)
    positive = [c for s,c in scored if s > 0]
    return (positive or [c for _,c in scored])[:top_k]

def format_evidence_cards(cards: Iterable[dict]) -> str:
    return "\n".join(
        f"[{c['id']}] {c['authors']} ({c['year']}). {c['title']}. {c['journal']}. "
        f"DOI: {c['doi']}. Role: {c['evidence_role']}. URL: {c['url']}. Note: {c['note']}"
        for c in cards
    )
