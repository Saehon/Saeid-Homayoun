"""Diagnostic guard: fails if the legacy Boolean gates still exist anywhere in src/.

EXPECTED on current main: UNKNOWN (Claude could not inspect the repository). If this
test fails, the legacy pipeline has not yet been rewired to the assurance core (R2).
"""
import re
import unittest
from pathlib import Path

SRC = Path(__file__).resolve().parents[2] / "src"
PATTERNS = [re.compile(p) for p in (
    r"=\s*bool\(\s*hypothes", r"=\s*bool\(\s*challenge", r"coso_context_supplied\s*=\s*True",
    r"reviewer_ok\s*=\s*True", r"falsification_ok\s*=\s*True")]


class NoFakeGates(unittest.TestCase):
    def test_no_boolean_review_or_falsification_gates(self):
        hits = []
        for f in SRC.rglob("*.py"):
            for n, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
                if any(p.search(line) for p in PATTERNS):
                    hits.append(f"{f.relative_to(SRC)}:{n}: {line.strip()}")
        self.assertEqual(hits, [], "legacy fake gates present:\n" + "\n".join(hits))


if __name__ == "__main__":
    unittest.main()
