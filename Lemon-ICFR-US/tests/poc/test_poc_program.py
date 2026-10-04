"""LEMON POC program v3 — tests for every phase's tooling (P00–P19). Synthetic data only, no network."""
import json
import shutil
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[2] / "tools"
sys.path.insert(0, str(TOOLS))

import benchmark_registry, build_final_review, build_hypotheses, check_doc_links, check_matrix  # noqa: E402
import extract_msft, human_review_sheet, improvement_gate, operator_lock, poc_state  # noqa: E402
import run_poc_pipeline, run_twin, sec_fetch, step_file, value_metrics, verify_manifest  # noqa: E402

from lemon_icfr.assurance.claim import Claim, Proposition  # noqa: E402
from lemon_icfr.assurance.entity_scope import NOT_PUBLICLY_OBSERVABLE, EntityScope, entity_level_support, \
    validate_entity_scope  # noqa: E402
from lemon_icfr.assurance.enums import HumanDecision, Rights, SourceTier, SupportClass  # noqa: E402
from lemon_icfr.assurance.errors import IntegrityError, SelfApprovalError  # noqa: E402
from lemon_icfr.assurance.evidence import EvidenceStore, Fact, make_evidence  # noqa: E402
from lemon_icfr.assurance.evidence_loader import InadmissibleSourceError, load_file_evidence  # noqa: E402
from lemon_icfr.assurance.export import export_passport, validate_passport_json  # noqa: E402
from lemon_icfr.assurance.extract import ExtractionError, extract_10k_facts, html_to_text, \
    make_span_fact, verify_span_fact  # noqa: E402
from lemon_icfr.assurance.human_gate import HumanDisposition  # noqa: E402
from lemon_icfr.assurance import signatures  # noqa: E402
from lemon_icfr.assurance.structure import Edge, GraphError, Node, StructureGraph  # noqa: E402

SYN_10K = """<html><body>
<h2>Item 9A. Controls and Procedures</h2>
<p>A material weakness is a deficiency, or a combination of deficiencies, in internal control over financial reporting.</p>
<p>Based on this assessment, management concluded that, as of June 30, 2025, our internal control over financial reporting was effective.</p>
<h2>Report of Independent Registered Public Accounting Firm</h2>
<p>In our opinion, the Company maintained, in all material respects, effective internal control over financial reporting as of June 30, 2025, based on criteria established in Internal Control - Integrated Framework (2013).</p>
<p>/s/ SYNTHETIC AUDIT LLP</p>
</body></html>"""

SYN_ADVERSE = """<html><body>
<p>Management identified a material weakness as of June 30, 2025 related to IT general controls.</p>
<p>Based on this assessment, management concluded that, as of June 30, 2025, our internal control over financial reporting was not effective.</p>
<p>In our opinion, because of the effect of the material weakness, the Company has not maintained, in all material respects, effective internal control over financial reporting as of June 30, 2025.</p>
</body></html>"""

STEP_OK = """# P02
## What was done
built extractor
## Files changed
extract.py
## POC demonstration (command + REAL output excerpt)
python tools/extract_msft.py → facts=3
## Tests (command, commit SHA, PASS/FAIL counts)
pytest -q abc123 66 passed
## Problems found (ORQ ids, or "none")
none
## Decisions made without review
regex v1 patterns
## Phase status: COMPLETE
## Labels: UNREVIEWED, DEVELOPMENT_ONLY
"""


def text_and_bytes(html):
    t = html_to_text(html)
    return t, t.encode("utf-8")


class P00_P01_Mechanics(unittest.TestCase):
    def setUp(self):
        self.d = Path(tempfile.mkdtemp())

    def tearDown(self):
        shutil.rmtree(self.d)

    def test_state_roundtrip_and_advance(self):
        p = self.d / "POC_STATE.md"
        s = poc_state.template()
        poc_state.save(s, p)
        s2 = poc_state.load(p)
        self.assertEqual(s2["current_phase"], "P00")
        poc_state.set_status(s2, "P00", "COMPLETE")
        self.assertEqual(poc_state.advance(s2), "P01")
        poc_state.save(s2, p)
        self.assertEqual(poc_state.load(p)["phase_status"]["P00"], "COMPLETE")
        with self.assertRaises(ValueError):
            poc_state.set_status(s2, "P01", "DONE")

    def test_lock(self):
        p = self.d / "LOCK.md"
        t = datetime(2026, 10, 4, 12, tzinfo=timezone.utc)
        self.assertTrue(operator_lock.acquire("R1", "P00", t, p))
        self.assertFalse(operator_lock.acquire("R2", "P00", t + timedelta(minutes=30), p))
        self.assertTrue(operator_lock.acquire("R2", "P00", t + timedelta(minutes=91), p))   # stale
        operator_lock.release("R2", p)
        self.assertTrue(operator_lock.acquire("R3", "P00", t + timedelta(minutes=92), p))

    def test_step_file_validation(self):
        errs, st = step_file.validate(STEP_OK)
        self.assertEqual((errs, st), ([], "COMPLETE"))
        errs, _ = step_file.validate(STEP_OK.replace("## Labels: UNREVIEWED, DEVELOPMENT_ONLY", "## Labels: ok"))
        self.assertTrue(errs)
        errs, _ = step_file.validate(STEP_OK.replace("## Decisions made without review\nregex v1 patterns\n", ""))
        self.assertIn("missing section: Decisions made without review", errs)


class P02_Extraction(unittest.TestCase):
    def test_conservative_extraction(self):
        t, b = text_and_bytes(SYN_10K)
        facts = {(f.predicate, f.value, f.period_end) for f in
                 extract_10k_facts(t, b, entity="DEMO", source_evidence_id="E1", accession="A1")}
        self.assertIn(("management_icfr_conclusion", "effective", "2025-06-30"), facts)
        self.assertIn(("auditor_icfr_opinion", "effective", "2025-06-30"), facts)
        self.assertIn(("auditor_name", "SYNTHETIC AUDIT LLP", "2025-06-30"), facts)
        self.assertFalse(any(p == "material_weakness_disclosed" for p, _, _ in facts),
                         "definition sentence must not be read as a disclosure")

    def test_adverse_detection(self):
        t, b = text_and_bytes(SYN_ADVERSE)
        facts = {(f.predicate, f.value) for f in extract_10k_facts(t, b, entity="D", source_evidence_id="E", accession="A")}
        self.assertIn(("management_icfr_conclusion", "not_effective"), facts)
        self.assertIn(("auditor_icfr_opinion", "adverse"), facts)
        self.assertIn(("material_weakness_disclosed", "disclosed"), facts)

    def test_span_verification(self):
        t, b = text_and_bytes(SYN_10K)
        f = extract_10k_facts(t, b, entity="DEMO", source_evidence_id="E1", accession="A1")[0]
        verify_span_fact(f, lambda i: b)
        with self.assertRaises(IntegrityError):
            verify_span_fact(f, lambda i: b.replace(b"effective", b"EFFECTIVE"))
        with self.assertRaises(ExtractionError):
            verify_span_fact(f, lambda i: None)
        import dataclasses
        with self.assertRaises(ExtractionError):
            verify_span_fact(dataclasses.replace(f, accession=""), lambda i: b)
        with self.assertRaises(ExtractionError):
            make_span_fact(t, b, 0, 10**7, entity="D", period_end="x", predicate="p", value="v",
                           source_evidence_id="E", accession="A", section="s", method="m")


class P03_EntityScope(unittest.TestCase):
    def test_control_claim_insufficient_and_no_invented_controls(self):
        c = Claim("C", "control ok", "D", "2025-06-30", "entity_level_icfr",
                  (Proposition("control_operating_effective", "effective"),), ("E1",))
        self.assertIs(entity_level_support(c, EvidenceStore()).classification, SupportClass.INSUFFICIENT_EVIDENCE)
        s = EntityScope("D", "2025-06-30", ("PCAOB AS 2201",))
        self.assertEqual(validate_entity_scope(s), [])
        import dataclasses
        self.assertTrue(validate_entity_scope(dataclasses.replace(s, control="K-17 three-way match")))
        self.assertEqual(s.control, NOT_PUBLICLY_OBSERVABLE)


class P04_P07_EndToEnd(unittest.TestCase):
    """Fake EDGAR → manifest → facts → hypotheses → pipeline → passport → review sheet → metrics."""

    def setUp(self):
        self.d = Path(tempfile.mkdtemp())
        self.evid, self.poc = self.d / "evid", self.d / "poc"
        self.sub = {"filings": {"recent": {
            "accessionNumber": ["0001-25-000001", "0001-24-000001", "0001-25-000009", "0001-25-000010"],
            "form": ["10-K", "10-K", "8-K", "8-K"], "filingDate": ["2025-07-30", "2024-07-30", "2025-01-10", "2025-02-01"],
            "reportDate": ["2025-06-30", "2024-06-30", "", ""], "primaryDocument": ["k25.htm", "k24.htm", "e1.htm", "e2.htm"],
            "items": ["", "", "2.02,9.01", "4.02"]}}}
        self.calls = []

        def fetch(url, headers):
            self.calls.append(url)
            assert "@" in headers["User-Agent"]
            if url.endswith(".json") and "submissions" in url:
                return json.dumps(self.sub).encode()
            if "companyfacts" in url:
                return b'{"facts": {}}'
            if url.endswith("k25.htm"):
                return SYN_10K.encode()
            if url.endswith("k24.htm"):
                return SYN_10K.replace("2025", "2024").encode()
            return b"<html><p>8-K body</p></html>"
        self.fetch = fetch

    def tearDown(self):
        shutil.rmtree(self.d)

    def test_full_chain(self):
        client = sec_fetch.EdgarClient("LEMON test test@example.com", fetch_fn=self.fetch, min_interval=0)
        m = sec_fetch.acquire(client, self.evid)
        kinds = sorted(e["evidence_id"] for e in m)
        self.assertIn("MSFT-10-K-0001-25-000001-text", kinds)
        self.assertIn("MSFT-8-K-0001-25-000010-raw", kinds)          # 4.02 8-K selected
        self.assertNotIn("MSFT-8-K-0001-25-000009-raw", kinds)       # non-4.0x 8-K skipped
        n = len(self.calls)
        sec_fetch.acquire(client, self.evid)
        self.assertEqual(len(self.calls), n, "second acquisition must be fully cached")
        self.assertTrue(all(ok for _, ok, _ in verify_manifest.verify(self.evid / "manifest.json")))

        facts = extract_msft.run(self.evid, self.poc / "facts.json")
        self.assertEqual(facts["rejected"], [])
        info = build_hypotheses.build(self.poc / "facts.json", self.poc)
        self.assertEqual(info["period_end"], "2025-06-30")
        self.assertEqual(sorted(info["unrebutted"]), ["A3", "A4"])

        run_poc_pipeline.POC, run_poc_pipeline.EVID = self.poc, self.evid
        self.assertEqual(run_poc_pipeline.main(), 1)                 # writes config template, NOT_RUN
        cfg = json.loads((self.poc / "config.json").read_text())
        cfg["created_at"] = "2026-10-04T00:00:00+00:00"
        cfg["repro"] = {"code_version": "c1", "repo_commit": "abc", "data_version": "d1", "config_hash": "h1",
                        "environment": "py3"}
        (self.poc / "config.json").write_text(json.dumps(cfg))
        self.assertEqual(run_poc_pipeline.main(), 0)
        s = json.loads((self.poc / "pipeline_summary.json").read_text())
        self.assertEqual(s["h1"]["support"], "SUPPORTED")
        self.assertEqual(s["h1"]["independence"], "LOW")
        self.assertEqual(s["h1"]["falsification"], "INCONCLUSIVE")   # A3/A4 unrebutted: honest
        self.assertEqual(s["h1"]["final_status"], "AWAITING_HUMAN_APPROVAL")
        self.assertTrue(s["h1"]["deterministic"])
        self.assertEqual(s["control"]["support"], "INSUFFICIENT_EVIDENCE")

        pj = json.loads((self.poc / "passports" / "h1_run1.json").read_text())
        self.assertEqual(validate_passport_json(pj), [])
        bad = dict(pj, final_status="APPROVED_BY_AI")
        self.assertTrue(validate_passport_json(bad))

        sheet = human_review_sheet.build(self.poc / "passports" / "h1_run1.json")
        self.assertIn(pj["content_hash"], sheet)
        sp = self.d / "sheet.md"
        sp.write_text(sheet.replace("reviewing: ____", "reviewing: 25"))
        mets = value_metrics.collect(self.poc, sp)
        self.assertEqual(mets["human_review_minutes"]["value"], 25)
        self.assertEqual(mets["api_cost_usd"]["value"], 0)
        self.assertTrue(all(v["source"] for v in mets.values()))

    def test_user_agent_and_rate_limit(self):
        with self.assertRaises(ValueError):
            sec_fetch.EdgarClient("no-email")
        t = [0.0]
        slept = []
        c = sec_fetch.EdgarClient("x a@b.c", fetch_fn=lambda u, h: b"", min_interval=0.15,
                                  clock=lambda: t[0], sleep=lambda s: slept.append(s))
        c.get("u1")
        c.get("u2")
        self.assertAlmostEqual(slept[0], 0.15)


class P08_P09_TwinGraph(unittest.TestCase):
    def test_twin_template_all_scenarios(self):
        d = Path(tempfile.mkdtemp())
        p = d / "twin_assumptions.json"
        p.write_text(json.dumps(run_twin.TEMPLATE))
        rows = run_twin.run(p)
        self.assertEqual(len(rows), 8)
        self.assertTrue(all("ANALYTICAL_SIMULATION" in r["evidence_type"] for r in rows))
        self.assertTrue(all(r["delta"]["R-ENTITY"] > 0 for r in rows))
        shutil.rmtree(d)

    def test_graph_never_validates_without_evidence(self):
        s = EvidenceStore()
        s.add(make_evidence("E1", content=b"x", provenance="p"))
        s.add(make_evidence("E2", content=b"y", provenance="", rights=Rights.UNKNOWN))
        g = StructureGraph(s)
        g.add_node(Node("A", "account", "Revenue"))
        g.add_node(Node("V", "evidence", "10-K"))
        base = dict(src="A", dst="V", relation="supported_by", confidence=0.6, evidence_required="10-K note",
                    provenance="P09 builder")
        g.add_edge(Edge(**base))
        for bad in ({"status": "VALIDATED"}, {"status": "VALIDATED", "evidence_ids": ("E2",)},
                    {"status": "VALIDATED", "evidence_ids": ("E1",), "contradiction": "OPEN"},
                    {"confidence": 1.5}):
            with self.subTest(bad=bad), self.assertRaises(GraphError):
                g.add_edge(Edge(**{**base, **bad}))
        g.add_edge(Edge(**{**base, "status": "VALIDATED", "evidence_ids": ("E1",)}))
        self.assertIn("AlphaFold is not used", g.to_json())


class P11_P13_Benchmarks(unittest.TestCase):
    def test_mock_never_evidence(self):
        d = Path(tempfile.mkdtemp())
        mock = d / "mock_case_002_microsoft_response.json"
        mock.write_text("{}")
        real = d / "case_002_microsoft_sec_2026.json"
        real.write_text("{}")
        kw = dict(provenance="p", tier=SourceTier.SEC_FILING, rights=Rights.PUBLIC_DOMAIN)
        with self.assertRaises(InadmissibleSourceError):
            load_file_evidence(mock, evidence_id="M", **kw)
        with self.assertRaises(InadmissibleSourceError):
            load_file_evidence(real, evidence_id="R", registry={real.as_posix(): "ARCHIVAL_COPY"}, **kw)
        self.assertEqual(load_file_evidence(real, evidence_id="R", **kw).evidence_id, "R")
        shutil.rmtree(d)

    def test_registry_classifies_and_finds_duplicates(self):
        d = Path(tempfile.mkdtemp())
        for rel in ("organized/benchmarks/a.json", "copies-from-original/a.json", "kaggle/mock_x.csv"):
            (d / rel).parent.mkdir(parents=True, exist_ok=True)
            (d / rel).write_text("same" if rel.endswith(".json") else "m")
        r = benchmark_registry.scan(d)
        cls = {e["path"]: e["class"] for e in r["entries"]}
        self.assertEqual(cls["organized/benchmarks/a.json"], "CANONICAL_CANDIDATE")
        self.assertEqual(cls["copies-from-original/a.json"], "ARCHIVAL_COPY")
        self.assertEqual(cls["kaggle/mock_x.csv"], "NON_EXECUTABLE_REFERENCE")
        self.assertEqual(len(r["duplicates"]), 1)
        shutil.rmtree(d)

    def test_improvement_gate(self):
        base = {"benchmark_sha": "F", "provenance_ok": True, "replay_hashes": ["h", "h"], "gate_regressions": 0,
                "fn": 5, "fp": 10, "metrics": {"recall": 0.40, "precision": 0.30}}
        self.assertEqual(improvement_gate.decide(base, base, "F")[0], "REJECT")             # self ≠ improvement
        worse = {**base, "fn": 7, "metrics": {"recall": 0.35, "precision": 0.30}}
        self.assertEqual(improvement_gate.decide(base, worse, "F")[0], "REJECT")
        sneaky = {**base, "gate_regressions": 1, "metrics": {"recall": 0.60, "precision": 0.40}}
        self.assertEqual(improvement_gate.decide(base, sneaky, "F")[0], "REJECT")
        better = {**base, "fn": 4, "metrics": {"recall": 0.45, "precision": 0.31}}
        self.assertEqual(improvement_gate.decide(base, better, "F")[0], "ACCEPT_DEVELOPMENT_ONLY")
        self.assertEqual(improvement_gate.decide(base, {**better, "benchmark_sha": "X"}, "F")[0], "REJECT")


@unittest.skipUnless(signatures.AVAILABLE, "cryptography not installed (ORQ-005 pending)")
class P14_Ed25519(unittest.TestCase):
    def test_forgery_rejected(self):
        from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
        from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
        human_key = Ed25519PrivateKey.generate()                  # lives only in the human UI
        pub = human_key.public_key().public_bytes(Encoding.Raw, PublicFormat.Raw)
        d = HumanDisposition("owner", "owner", HumanDecision.APPROVED, "t", "", ("F",), ("E",), "", (), "hash")
        import dataclasses
        signed = dataclasses.replace(d, signature=human_key.sign(d.payload()).hex())
        v = signatures.Ed25519Verifier(pub)
        v.verify(signed)
        attacker = Ed25519PrivateKey.generate()
        for bad in (dataclasses.replace(d, signature=attacker.sign(d.payload()).hex()),
                    dataclasses.replace(signed, decision=HumanDecision.REJECTED), dataclasses.replace(d, signature="zz")):
            with self.subTest(), self.assertRaises(SelfApprovalError):
                v.verify(bad)
        self.assertFalse(hasattr(v, "sign"))


class P15_P19_DocsAndPackage(unittest.TestCase):
    def setUp(self):
        self.d = Path(tempfile.mkdtemp())

    def tearDown(self):
        shutil.rmtree(self.d)

    def test_matrix_check(self):
        for n in ("src", "tests", "README.md"):
            (self.d / n).mkdir() if "." not in n else (self.d / n).write_text("x")
        (self.d / "governance").mkdir()
        mx = self.d / "governance" / "PUBLIC_PRIVATE_MATRIX.md"
        mx.write_text("| `src/` | public |\n| `tests/` | public |\n| `README.md` | public |\n")
        self.assertEqual(check_matrix.missing(self.d, mx), ["governance"])

    def test_doc_links(self):
        (self.d / "src").mkdir()
        (self.d / "README.md").write_text("See `src/` and `benchmarks/` and [arch](ARCHITECTURE.md) and `pytest -q`.")
        (self.d / "ARCHITECTURE.md").write_text("ok")
        self.assertEqual(check_doc_links.broken(self.d), ["README.md: benchmarks/"])

    def test_final_package_split_and_decisions(self):
        steps = self.d / "governance" / "poc_steps"
        steps.mkdir(parents=True)
        for i in range(3):
            (steps / f"P0{i}_x.md").write_text(STEP_OK.replace("regex v1 patterns", f"decision {i}") + "x" * 400)
        build_final_review.ROOT, build_final_review.STEPS, build_final_review.LIMIT = self.d, steps, 900
        paths = build_final_review.build()
        self.assertGreater(len(paths), 1)
        joined = "".join(p.read_text() for p in paths)
        for i in range(3):
            self.assertIn(f"decision {i}", joined)


if __name__ == "__main__":
    unittest.main()
