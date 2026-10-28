import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parent

class TestManifest(unittest.TestCase):
    def test_pinned_and_unique(self):
        items = json.loads((ROOT / "upstreams.lock.json").read_text())["repositories"]
        self.assertEqual(len(items), 10)
        self.assertEqual(len({x["name"] for x in items}), len(items))
        for item in items:
            self.assertEqual(len(item["commit"]), 40)
            self.assertTrue(all(c in "0123456789abcdef" for c in item["commit"]))
            self.assertTrue(item["source"].startswith("https://github.com/anthropics/"))
            self.assertFalse(item["enabled"])
    def test_restricted(self):
        items = {x["name"]: x for x in json.loads((ROOT / "upstreams.lock.json").read_text())["repositories"]}
        for name in ("skills", "claude-code", "courses"):
            self.assertFalse(items[name]["install_approved"])

if __name__ == "__main__":
    unittest.main()
