"""Read-only agent tool contract tests; no real AI or financial data."""
import unittest
from paper_tools import get_paper_method, run_architecture_benchmark, inspect_synthetic_case, TOOL_CONTRACTS

class ToolTests(unittest.TestCase):
    def test_paper_metadata_does_not_imply_replication(self):
        p=get_paper_method()
        self.assertEqual(p["execution_status"],"ORIGINAL_AUTHOR_MODEL_NOT_REPRODUCED")
        self.assertIn("github.com/JarFraud",p["author_code"])
    def test_contracts(self):
        self.assertEqual(len(TOOL_CONTRACTS),3)
        self.assertTrue(all(x["name"] for x in TOOL_CONTRACTS))
    def test_synthetic_gate(self):
        r=inspect_synthetic_case("SYN-2024-00")
        self.assertFalse(r["audit_failure_claim_allowed"])
        self.assertIn("SIM-",r["source_evidence_id"])
    def test_reject_unknown_company(self):
        with self.assertRaises(ValueError):
            inspect_synthetic_case("MSFT")
    def test_benchmark_human_gate(self):
        r=run_architecture_benchmark()
        self.assertFalse(r["scientific_discovery_claim_allowed"])
        self.assertEqual(len(r["arms"]),4)

if __name__=="__main__":
    unittest.main()
