from pathlib import Path
import json
import tempfile
import subprocess
import sys


def write_packet(root: Path):
    tasks = root / "tasks.jsonl"
    evidence = root / "evidence.txt"
    tasks.write_text(
        "\n".join(json.dumps({"task_id": f"P{i:02d}", "prompt": "Test prompt"}) for i in range(1, 22)),
        encoding="utf-8",
    )
    evidence.write_text("Frozen evidence placeholder", encoding="utf-8")
    return tasks, evidence


def test_dry_run_21_tasks():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        tasks, evidence = write_packet(root)
        output = root / "private_outputs"
        cmd = [
            sys.executable, str(Path(__file__).with_name("stage2b_runner.py")),
            "--candidate", "C01",
            "--tasks", str(tasks),
            "--evidence", str(evidence),
            "--output-dir", str(output),
            "--dry-run",
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        assert result.returncode == 0, result.stderr
        manifest = json.loads(result.stdout)
        assert manifest["task_count"] == 21
        assert manifest["scoring_opened"] is False
        assert manifest["gold_key_access"] == "NOT_AVAILABLE_TO_RUNNER"


def test_rejects_gold_fields():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        tasks = root / "tasks.jsonl"
        evidence = root / "evidence.txt"
        rows = [{"task_id": f"P{i:02d}", "prompt": "Test prompt"} for i in range(1, 22)]
        rows[0]["gold_key"] = "should never be present"
        tasks.write_text("\n".join(json.dumps(r) for r in rows), encoding="utf-8")
        evidence.write_text("Evidence", encoding="utf-8")
        cmd = [
            sys.executable, str(Path(__file__).with_name("stage2b_runner.py")),
            "--candidate", "C01",
            "--tasks", str(tasks),
            "--evidence", str(evidence),
            "--output-dir", str(root / "out"),
            "--dry-run",
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        assert result.returncode != 0
        assert "forbidden blind-evaluation fields" in (result.stderr + result.stdout)
