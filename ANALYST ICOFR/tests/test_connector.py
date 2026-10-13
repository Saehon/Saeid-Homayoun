import contextlib
import csv
import io
from pathlib import Path
import tempfile
import types
import unittest
from unittest.mock import patch

import connector


class ConnectorTests(unittest.TestCase):
    def test_escape_and_repo_destinations_are_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary).resolve()
            with self.assertRaises(connector.ConnectorError):
                connector.local_path(root, "../escape.csv")
            with self.assertRaises(connector.ConnectorError):
                connector.private_root(str(connector.REPO / "private"))
            (root / "link").symlink_to(root.parent, target_is_directory=True)
            with self.assertRaises(connector.ConnectorError):
                connector.local_path(root, "link/escape.csv")

    def test_external_failure_does_not_disclose_secrets(self):
        output = io.StringIO()
        with patch.object(connector, "hf_identity", side_effect=RuntimeError("synthetic-token secret-row")):
            with contextlib.redirect_stderr(output):
                result = connector.main(["check", "--provider", "hf"])
        self.assertEqual(result, 1)
        self.assertNotIn("synthetic-token", output.getvalue())
        self.assertNotIn("secret-row", output.getvalue())
        output = io.StringIO()
        with contextlib.redirect_stderr(output):
            result = connector.main(["check", "--provider", "synthetic-private-token"])
        self.assertEqual(result, 1)
        self.assertNotIn("synthetic-private-token", output.getvalue())

    def test_mutable_revision_is_rejected_before_service_call(self):
        args = types.SimpleNamespace(revision="main")
        with patch.object(connector, "dependency") as dependency:
            with self.assertRaises(connector.ConnectorError):
                connector.download_hf(args)
        dependency.assert_not_called()

    def test_classifier_preserves_human_labels_and_is_offline(self):
        loaded = []
        def load(*args, **kwargs):
            loaded.append(kwargs)
            return object()
        transformers = types.SimpleNamespace(
            AutoTokenizer=types.SimpleNamespace(from_pretrained=load),
            AutoModelForSequenceClassification=types.SimpleNamespace(from_pretrained=load),
            pipeline=lambda *a, **k: lambda text, **kw: [{"label": "synthetic-positive", "score": 0.75}])
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "model").mkdir()
            (root / "input.csv").write_text("text,human_label\nexample,reviewed\n", encoding="utf-8")
            args = types.SimpleNamespace(local_root=temporary, model_dir="model", input_csv=str(root / "input.csv"),
                                         text_column="text", output="result.csv")
            # Synthetic fixture only: some runners place all scratch paths in a Git tree.
            with patch.object(connector, "private_root", return_value=root), patch.object(connector, "dependency", return_value=transformers), patch.dict(connector.os.environ), contextlib.redirect_stdout(io.StringIO()):
                connector.classify(args)
                self.assertEqual(connector.os.environ["HF_HUB_OFFLINE"], "1")
            with (root / "result.csv").open() as stream:
                row = next(csv.DictReader(stream))
            self.assertEqual(row["human_label"], "reviewed")
            self.assertEqual(row["predicted_label"], "synthetic-positive")
            self.assertEqual(float(row["model_confidence"]), 0.75)
        self.assertTrue(all(x["local_files_only"] and not x["trust_remote_code"] for x in loaded))
        self.assertTrue(loaded[-1]["use_safetensors"])

    def test_invalid_confidence_does_not_commit_csv(self):
        load = lambda *a, **kw: object()
        transformers = types.SimpleNamespace(
            AutoTokenizer=types.SimpleNamespace(from_pretrained=load),
            AutoModelForSequenceClassification=types.SimpleNamespace(from_pretrained=load),
            pipeline=lambda *a, **kw: lambda *a, **kw: [{"label": "synthetic", "score": float("nan")}])
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "model").mkdir()
            (root / "input.csv").write_text("text\nexample\n", encoding="utf-8")
            args = types.SimpleNamespace(local_root=temporary, model_dir="model", input_csv=str(root / "input.csv"),
                                         text_column="text", output="result.csv")
            with patch.object(connector, "private_root", return_value=root), patch.object(connector, "dependency", return_value=transformers), patch.dict(connector.os.environ):
                with self.assertRaises(connector.ConnectorError):
                    connector.classify(args)
            self.assertFalse((root / "result.csv").exists())
            self.assertFalse(list(root.glob(".classification-*")))


if __name__ == "__main__":
    unittest.main()
