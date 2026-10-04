"""P02 — Span-provenanced fact extraction (ORQ-006).

Every extracted fact points to an exact character span in an exact, hashed text
artifact. Character offsets refer to the DERIVED TEXT file (produced by
html_to_text), which is itself stored and hashed in the evidence manifest.

Extraction rules are deliberately conservative:
- several conflicting matches are ALL returned (support logic then reports CONTRADICTED);
- absence of a phrase is never turned into a "false"/"absent" fact;
- the generic definition sentence "A material weakness is a deficiency..." present in
  most 10-Ks is NOT a disclosure and is not flagged.
"""
from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from html.parser import HTMLParser
from typing import Callable, Optional

from .errors import IntegrityError, LemonError
from .evidence import Fact


class ExtractionError(LemonError):
    """A fact cannot be traced to a verifiable span."""


def _h(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


@dataclass(frozen=True)
class SpanFact:
    entity: str
    period_end: str
    predicate: str
    value: str
    source_evidence_id: str
    accession: str
    section: str
    char_start: int
    char_end: int
    span_sha256: str
    source_sha256: str
    method: str

    def to_fact(self) -> Fact:
        return Fact(self.entity, self.period_end, self.predicate, self.value)

    def excerpt(self, text: str, max_words: int = 25) -> str:
        words = text[self.char_start:self.char_end].split()
        return " ".join(words[:max_words]) + (" …" if len(words) > max_words else "")


def make_span_fact(text: str, source_bytes: bytes, start: int, end: int, *, entity: str, period_end: str,
                   predicate: str, value: str, source_evidence_id: str, accession: str, section: str,
                   method: str) -> SpanFact:
    if not (0 <= start < end <= len(text)):
        raise ExtractionError("span out of range")
    if text != decode_text(source_bytes):
        raise ExtractionError("text does not match source bytes")
    return SpanFact(entity, period_end, predicate, value, source_evidence_id, accession, section, start, end,
                    _h(text[start:end].encode("utf-8")), _h(source_bytes), method)


def decode_text(b: bytes) -> str:
    return b.decode("utf-8", errors="strict")


REQUIRED_PROVENANCE = ("entity", "period_end", "predicate", "value", "source_evidence_id", "accession",
                       "section", "span_sha256", "source_sha256", "method")


def verify_span_fact(f: SpanFact, load_source: Callable[[str], Optional[bytes]]) -> None:
    """Raises unless the fact is traceable to an unaltered span of an unaltered source."""
    missing = [k for k in REQUIRED_PROVENANCE if not getattr(f, k)]
    if missing:
        raise ExtractionError(f"fact lacks provenance: {missing}")
    src = load_source(f.source_evidence_id)
    if src is None:
        raise ExtractionError(f"source {f.source_evidence_id} not found")
    if _h(src) != f.source_sha256:
        raise IntegrityError(f"source {f.source_evidence_id} hash changed")
    text = decode_text(src)
    if not (0 <= f.char_start < f.char_end <= len(text)):
        raise ExtractionError("span out of range")
    if _h(text[f.char_start:f.char_end].encode("utf-8")) != f.span_sha256:
        raise IntegrityError("span text altered")


# ---------------------------------------------------------------- HTML → text (deterministic)
class _TextParser(HTMLParser):
    BLOCK = {"p", "div", "br", "tr", "li", "h1", "h2", "h3", "h4", "h5", "h6", "table", "section"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts, self._skip = [], 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self._skip += 1
        elif tag in self.BLOCK:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style") and self._skip:
            self._skip -= 1
        elif tag in self.BLOCK:
            self.parts.append("\n")

    def handle_data(self, data):
        if not self._skip:
            self.parts.append(data)


def html_to_text(html: str) -> str:
    p = _TextParser()
    p.feed(html)
    p.close()
    text = "".join(p.parts).replace("\xa0", " ")
    lines = [re.sub(r"[ \t]+", " ", ln).strip() for ln in text.splitlines()]
    out, blank = [], False
    for ln in lines:
        if not ln:
            if not blank:
                out.append("")
            blank = True
        else:
            out.append(ln)
            blank = False
    return "\n".join(out).strip() + "\n"


# ---------------------------------------------------------------- conservative 10-K extractors
_DATE = re.compile(r"\b(January|February|March|April|May|June|July|August|September|October|November|December)"
                   r"\s+(\d{1,2}),\s+(\d{4})\b")
_MONTHS = {m: i for i, m in enumerate(("January", "February", "March", "April", "May", "June", "July", "August",
                                        "September", "October", "November", "December"), 1)}


def _iso(m: re.Match) -> str:
    return f"{int(m.group(3)):04d}-{_MONTHS[m.group(1)]:02d}-{int(m.group(2)):02d}"


def _sentence_bounds(text: str, s: int, e: int) -> tuple[int, int]:
    a = max(text.rfind(". ", 0, s), text.rfind("\n", 0, s))
    b_dot, b_nl = text.find(". ", e), text.find("\n", e)
    cands = [x for x in (b_dot, b_nl) if x != -1]
    b = min(cands) if cands else len(text)
    return (a + 1 if a != -1 else 0), (b + 1 if b < len(text) else len(text))


_MGMT = re.compile(r"internal control over financial reporting\s+(?:was|is)\s+(not\s+)?effective", re.I)
_AUD = re.compile(r"(has\s+not\s+maintained|did\s+not\s+maintain|maintained),?\s+in\s+all\s+material\s+respects,?\s+"
                  r"effective\s+internal\s+control\s+over\s+financial\s+reporting", re.I)
_AUD_NAME = re.compile(r"/s/\s*([A-Z][A-Z&.,' ]{2,80}?LLP)")
_MW = re.compile(r"\b(identified|identification\s+of|existence\s+of|disclosed)\s+(?:a\s+|two\s+|three\s+)?"
                 r"material\s+weakness(?:es)?\b", re.I)
_NEG = re.compile(r"\b(no|not|did not|has not|have not|were not|was not)\b[^.]{0,40}$", re.I)


def extract_10k_facts(text: str, source_bytes: bytes, *, entity: str, source_evidence_id: str,
                      accession: str) -> list[SpanFact]:
    out: list[SpanFact] = []
    kw = dict(entity=entity, source_evidence_id=source_evidence_id, accession=accession)

    for m in _MGMT.finditer(text):
        s, e = _sentence_bounds(text, m.start(), m.end())
        sent = text[s:e]
        if "concluded" not in sent.lower() or "management" not in sent.lower():
            continue
        d = _DATE.search(sent)
        if not d:
            continue
        out.append(make_span_fact(text, source_bytes, s, e, period_end=_iso(d),
                                  predicate="management_icfr_conclusion",
                                  value="not_effective" if m.group(1) else "effective",
                                  section="Item 9A", method="regex:mgmt_icfr_v1", **kw))

    for m in _AUD.finditer(text):
        s, e = _sentence_bounds(text, m.start(), m.end())
        sent = text[s:e]
        if "in our opinion" not in sent.lower():
            continue
        d = _DATE.search(sent)
        if not d:
            continue
        val = "effective" if m.group(1).lower() == "maintained" else "adverse"
        out.append(make_span_fact(text, source_bytes, s, e, period_end=_iso(d),
                                  predicate="auditor_icfr_opinion", value=val,
                                  section="Report of Independent Registered Public Accounting Firm",
                                  method="regex:auditor_icfr_v1", **kw))

    periods = sorted({f.period_end for f in out})
    m = _AUD_NAME.search(text)
    if m and len(periods) == 1:
        out.append(make_span_fact(text, source_bytes, m.start(1), m.end(1), period_end=periods[0],
                                  predicate="auditor_name", value=" ".join(m.group(1).split()),
                                  section="Auditor signature", method="regex:auditor_name_v1", **kw))

    for m in _MW.finditer(text):
        before = text[max(0, m.start() - 60):m.start()]
        if _NEG.search(before):
            continue
        s, e = _sentence_bounds(text, m.start(), m.end())
        d = _DATE.search(text[s:e])
        if not d:
            continue
        out.append(make_span_fact(text, source_bytes, s, e, period_end=_iso(d),
                                  predicate="material_weakness_disclosed", value="disclosed",
                                  section="Item 9A", method="regex:mw_disclosure_v1", **kw))
    return out
