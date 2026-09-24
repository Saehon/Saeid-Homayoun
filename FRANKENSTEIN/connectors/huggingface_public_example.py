"""FRANKENSTEIN Phase 1: public Hugging Face connector.

Downloads a very small public sample and writes a provenance manifest.
No Hugging Face token is required.

Source:
https://huggingface.co/datasets/lmassaron/FinancialPhraseBank

This is a research/education demonstration only. The upstream dataset license
and attribution requirements remain in force.
"""

from __future__ import annotations

import csv
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

DATASET = "lmassaron/FinancialPhraseBank"
CONFIG = "default"
SPLIT = "train"
SAMPLE_ROWS = 5

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "data_registry" / "phase1_huggingface"
OUT_DIR.mkdir(parents=True, exist_ok=True)

META_URL = f"https://huggingface.co/api/datasets/{DATASET}"
ROWS_URL = "https://datasets-server.huggingface.co/first-rows?" + urlencode(
    {"dataset": DATASET, "config": CONFIG, "split": SPLIT}
)


def get_json(url: str) -> dict:
    req = Request(url, headers={"User-Agent": "FRANKENSTEIN-Research-Connector/0.1"})
    with urlopen(req, timeout=30) as response:
        return json.load(response)


meta = get_json(META_URL)
rows_payload = get_json(ROWS_URL)

rows = [item.get("row", {}) for item in rows_payload.get("rows", [])[:SAMPLE_ROWS]]
sample_path = OUT_DIR / "financialphrasebank_sample.csv"

fieldnames = sorted({key for row in rows for key in row.keys()})
with sample_path.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

sha256 = hashlib.sha256(sample_path.read_bytes()).hexdigest()

manifest = {
    "project": "FRANKENSTEIN",
    "phase": 1,
    "source_platform": "Hugging Face",
    "dataset": DATASET,
    "dataset_url": f"https://huggingface.co/datasets/{DATASET}",
    "api_metadata_url": META_URL,
    "api_rows_url": ROWS_URL,
    "config": CONFIG,
    "split": SPLIT,
    "sample_rows": len(rows),
    "sample_file": str(sample_path.relative_to(ROOT)),
    "sample_sha256": sha256,
    "license": meta.get("cardData", {}).get("license") or meta.get("license"),
    "upstream_last_modified": meta.get("lastModified"),
    "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
    "purpose": "Public-data connection demonstration; not a production data warehouse.",
    "redistribution_note": (
        "Upstream license and attribution requirements remain applicable. "
        "Use the source dataset page as the authoritative license reference."
    ),
}

manifest_path = OUT_DIR / "manifest.json"
manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

print(f"Wrote {sample_path}")
print(f"Wrote {manifest_path}")
