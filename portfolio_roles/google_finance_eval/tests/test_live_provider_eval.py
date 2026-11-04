import unittest
from types import SimpleNamespace
from tempfile import TemporaryDirectory
from pathlib import Path
import json
from unittest.mock import patch
from portfolio_roles.google_finance_eval.live_provider_eval import normalize_response, evaluate, load_cases, preflight, request_payload

class TestLiveProviderEval(unittest.TestCase):
    def test_openai_usage(self):
        answer,i,o=normalize_response("openai",{"output":[{"type":"message","content":[{"type":"output_text","text":"20"}]}],"usage":{"input_tokens":10,"output_tokens":4}})
        self.assertEqual((answer,i,o),("20",10,4))
    def test_anthropic_usage(self):
        answer,i,o=normalize_response("anthropic",{"content":[{"type":"text","text":"ok"}],"usage":{"input_tokens":5,"output_tokens":2}})
        self.assertEqual((answer,i,o),("ok",5,2))
    def test_gemini_thought_tokens_counted(self):
        a,i,o=normalize_response("gemini",{"candidates":[{"content":{"parts":[{"text":"ok"}]}}],"usageMetadata":{"promptTokenCount":7,"candidatesTokenCount":2,"thoughtsTokenCount":3}})
        self.assertEqual((a,i,o),("ok",7,5))
    def test_missing_usage_blocks(self):
        with self.assertRaises(ValueError):
            normalize_response("openai",{"output":[]})
    def test_data_transfer_not_implicit(self):
        cfg=SimpleNamespace(max_cases=2,max_output_tokens=100,model="my-model",
            input_usd_per_million=1.,output_usd_per_million=2.,max_usd=1.,
            execute=True,authorize_data_transfer=False)
        with self.assertRaises(ValueError):
            preflight(cfg,[{"prompt":"Synthetic text"}],True)
    def test_missing_key_blocks(self):
        cfg=SimpleNamespace(max_cases=2,max_output_tokens=100,model="my-model",
            input_usd_per_million=1.,output_usd_per_million=2.,max_usd=1.,
            execute=True,authorize_data_transfer=True)
        with self.assertRaises(ValueError):
            preflight(cfg,[{"prompt":"Synthetic text"}],False)
    def test_invalid_model_blocks(self):
        cfg=SimpleNamespace(max_cases=2,max_output_tokens=100,model="../secret",
            input_usd_per_million=1.,output_usd_per_million=2.,max_usd=1.,
            execute=False,authorize_data_transfer=False)
        with self.assertRaises(ValueError):
            preflight(cfg,[{"prompt":"Synthetic text"}],False)
    def test_no_api_called_in_dry_run(self):
        with TemporaryDirectory() as tmp:
            data=Path(tmp)/"synthetic.jsonl"
            data.write_text(json.dumps({"case_id":"SYN-1","prompt":"What is 2+2?",
                                        "gold_answer":"4","evidence_text":"2+2=4."})+"\n")
            cfg=SimpleNamespace(cases=str(data),schema="synthetic",provider="openai",
                model="mock-model",max_cases=1,max_output_tokens=100,
                input_usd_per_million=1.,output_usd_per_million=2.,max_usd=1.,
                price_source="test only",execute=False,authorize_data_transfer=False)
            with patch("portfolio_roles.google_finance_eval.live_provider_eval.call_provider",
                       side_effect=AssertionError("network called")):
                report=evaluate(cfg)
            self.assertEqual(report["execution"],"dry_run_no_api_calls")
    def test_missing_case_evidence_for_financebench_blocks(self):
        with TemporaryDirectory() as tmp:
            f=Path(tmp)/"fb.jsonl"
            f.write_text(json.dumps({"financebench_id":"SYN-1","question":"test","evidence":[]})+"\n")
            with self.assertRaises(ValueError):
                load_cases(f,"financebench")

if __name__ == "__main__":
    unittest.main()
