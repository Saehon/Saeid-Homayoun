from pathlib import Path
import csv
import json

BASE = Path(__file__).resolve().parent
DATA = BASE / "synthetic_cam_kam_sample.csv"

required = {
    "record_id","jurisdiction","matter_type","company","fiscal_year",
    "title","description","response","conclusion","topic","source_type"
}

with DATA.open(newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fields = set(reader.fieldnames or [])
    missing = required - fields
    if missing:
        raise SystemExit(f"Missing required columns: {sorted(missing)}")
    rows = list(reader)

if len(rows) != 3:
    raise SystemExit(f"Expected 3 synthetic rows, found {len(rows)}")

if any(r["source_type"] != "SYNTHETIC" for r in rows):
    raise SystemExit("Public demo must contain synthetic rows only")

print(json.dumps({
    "status":"PASS",
    "rows":len(rows),
    "topics":sorted({r["topic"] for r in rows}),
    "matter_types":sorted({r["matter_type"] for r in rows})
}, indent=2))
