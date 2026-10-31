import json
import unittest
from pathlib import Path
from importlib.util import spec_from_file_location, module_from_spec

HERE = Path(__file__).resolve().parents[1]
spec = spec_from_file_location("portfolio_checker", HERE / "check_portfolio.py")
module = module_from_spec(spec)
spec.loader.exec_module(module)

class CatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = json.loads((HERE / "catalog.json").read_text(encoding="utf-8"))
    def test_catalog_snapshot(self):
        self.assertEqual(module.verify_catalog(self.catalog), [])
    def test_malformed_claim_blocks(self):
        data = json.loads(json.dumps(self.catalog))
        data["projects"][0]["real_provider_inference_verified"] = True
        self.assertTrue(module.verify_catalog(data))
    def test_wrong_pull_request_link_blocks(self):
        data = json.loads(json.dumps(self.catalog))
        data["projects"][0]["pr_url"] = "https://github.com/another/repo/pull/1"
        self.assertTrue(module.verify_catalog(data))
    def test_relative_markdown_links(self):
        self.assertEqual(module.verify_markdown(), [])

if __name__ == "__main__":
    unittest.main()
