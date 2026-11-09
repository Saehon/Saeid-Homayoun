import unittest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from validation_gate import verify, batch, retry

class FailClosedTests(unittest.TestCase):
    def test_empty_record_not_done(self):
        self.assertTrue(verify({}))
    def test_missing_original_sec_blocks(self):
        self.assertIn("SEC original pointer", verify({"cik10":"0001018724","accession":"0001018724-24-000001"}))
    def test_duplicate_blocks(self):
        rows=[{"cik10":"0001018724","fiscal_year_end":"2024-12-31","accession":"0001018724-24-000001"}]*2
        self.assertTrue(all("duplicate key" in r["issues"] for r in batch(rows)))
    def test_submitter_cik_may_differ(self):
        issues = verify({"cik10":"0001018724","accession":"0000950170-24-000001",
            "sec_original_url":"https://www.sec.gov/Archives/edgar/data/1018724/000095017024000001/example.htm"})
        self.assertNotIn("CIK/accession mismatch", issues)
        self.assertNotIn("SEC archive issuer CIK mismatch", issues)
    def test_archive_issuer_must_match(self):
        issues = verify({"cik10":"0001018724","accession":"0000950170-24-000001",
            "sec_original_url":"https://www.sec.gov/Archives/edgar/data/12345/000095017024000001/example.htm"})
        self.assertIn("SEC archive issuer CIK mismatch", issues)
    def test_invalid_cik_does_not_crash(self):
        issues = verify({"cik10":"invalid","accession":"0000950170-24-000001",
            "sec_original_url":"https://www.sec.gov/Archives/edgar/data/1018724/000095017024000001/example.htm"})
        self.assertIn("CIK10", issues)
    def test_retry_limit(self):
        self.assertEqual(retry(3), "needs_manual_review")
    def test_no_pit_without_evidence(self):
        self.assertIn("PIT clock", verify({}))
    def test_ai_capex_requires_source(self):
        self.assertIn("AI-specific CapEx evidence",verify({"ai_capex":123}))
if __name__ == "__main__":
    unittest.main()
