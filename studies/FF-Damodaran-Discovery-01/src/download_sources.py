from __future__ import annotations

import hashlib
import json
import shutil
import urllib.request
import zipfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "config" / "source_registry.json"
RAW = ROOT / "data" / "raw"
MANIFEST = ROOT / "evidence" / "download_manifest.json"
USER_AGENT = "ECONOVA-S-Research-CoScientist/0.1 (+scientific-reproducibility)"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def download(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=120) as response, dest.open("wb") as out:
        shutil.copyfileobj(response, out)


def record(source_id: str, vintage: int | None, url: str, path: Path) -> dict:
    return {
        "source_id": source_id,
        "vintage": vintage,
        "provider_url": url,
        "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
        "local_path": str(path.relative_to(ROOT)),
        "bytes": path.stat().st_size,
        "sha256": sha256(path),
    }


def main() -> None:
    cfg = json.loads(REGISTRY.read_text(encoding="utf-8"))
    RAW.mkdir(parents=True, exist_ok=True)
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    rows: list[dict] = []

    for src in cfg["sources"]:
        sid = src["id"]
        if "download_url" in src:
            dest = RAW / "fama_french" / f"{sid}.zip"
            download(src["download_url"], dest)
            rows.append(record(sid, None, src["download_url"], dest))
            extract_dir = dest.with_suffix("")
            extract_dir.mkdir(parents=True, exist_ok=True)
            with zipfile.ZipFile(dest) as zf:
                zf.extractall(extract_dir)
        else:
            for year in src["archive_years"]:
                yy = str(year)[-2:]
                url = src["archive_template"].format(yy=yy)
                dest = RAW / "damodaran" / sid.lower() / f"{sid}_{year}.xls"
                download(url, dest)
                rows.append(record(sid, year, url, dest))

            year = int(src["current_vintage"])
            dest = RAW / "damodaran" / sid.lower() / f"{sid}_{year}.xls"
            download(src["current_url"], dest)
            rows.append(record(sid, year, src["current_url"], dest))

    manifest = {
        "study_id": cfg["study_id"],
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "raw_files_are_immutable": True,
        "files": rows,
    }
    MANIFEST.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"Wrote {MANIFEST} with {len(rows)} source files")


if __name__ == "__main__":
    main()
