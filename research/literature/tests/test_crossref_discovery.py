import copy
import json
import unittest

from research.literature.crossref_discovery import (
    BASE, collect, request_url, result_to_candidate, validate_scope
)

class DiscoveryScopeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.scope = json.loads((BASE/"crossref_journal_search_scope.json").read_text("utf-8"))
        cls.journal = cls.scope["journal_candidates"][0]

    def test_all_ajg_groups_have_seed_candidate_journals(self):
        validate_scope(self.scope)
        tiers = {j["ajg_2024_secondary_candidate"] if "ajg_2024_secondary_candidate" in j else
                 j["ajg_2024_secondary"] for j in self.scope["journal_candidates"]}
        self.assertTrue({"4*", "4", "3", "2", "1"}.issubset(tiers))

    def test_invalid_issn_blocks(self):
        bad=copy.deepcopy(self.scope)
        bad["journal_candidates"][0]["issn"]="attacker/path"
        with self.assertRaises(ValueError): validate_scope(bad)

    def test_duplicate_issn_blocks(self):
        bad=copy.deepcopy(self.scope)
        bad["journal_candidates"].append(copy.deepcopy(bad["journal_candidates"][0]))
        with self.assertRaises(ValueError): validate_scope(bad)

    def test_request_url_is_https_and_date_scoped(self):
        url=request_url("0021-8456","fine-tuning",10)
        self.assertTrue(url.startswith("https://api.crossref.org/journals/"))
        self.assertIn("until-pub-date%3A2026-10-31",url)
        self.assertIn("rows=10",url)

    def test_bad_row_limit_rejected(self):
        with self.assertRaises(ValueError): request_url("0021-8456","LLM",101)

    def test_duplicate_doi_deduplicated(self):
        items=[{"DOI":"10.1111/1475-679x.70050",
                "title":["Generative AI in Financial Reporting"],
                "published":{"date-parts":[[2026,4,7]]}}]
        target={}
        collect(items,self.journal,"generative AI",target)
        collect(items,self.journal,"large language models",target)
        self.assertEqual(len(target),1)
        self.assertEqual(len(next(iter(target.values()))["search_terms_matched"]),2)

    def test_no_result_claim_of_inclusion_or_rating_authentication(self):
        item={"DOI":"10.1111/1475-679x.70050", "title":["GAI and Reports"]}
        candidate=result_to_candidate(item,self.journal,"LLM")
        self.assertEqual(candidate["manual_inclusion_review"],"PENDING")
        self.assertTrue(candidate["rank_not_authenticated_by_crossref"])

    def test_bad_doi_ignored(self):
        self.assertIsNone(result_to_candidate({"DOI":"malformed","title":["Text"]},
                                               self.journal,"LLM"))


if __name__ == "__main__":
    unittest.main()
