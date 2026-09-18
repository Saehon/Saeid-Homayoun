from __future__ import annotations

import argparse
import hashlib
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("mnsc_famafrench_study", HERE / "run_study.py")
study = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(study)


def _read(path: Path) -> bytes:
    blob = path.read_bytes()
    if not blob:
        raise ValueError(f"Empty archive: {path}")
    return blob


def _record(dataset: str, year: int, path: Path, blob: bytes):
    return study.SourceRecord(
        dataset=dataset,
        archive_year=year,
        url=f"local-file://{path.name}",
        sha256=hashlib.sha256(blob).hexdigest(),
        bytes=len(blob),
    )


def build_local_loader(args):
    paths = {
        args.old_year: (Path(args.old_ff5), Path(args.old_port6)),
        args.new_year: (Path(args.new_ff5), Path(args.new_port6)),
    }

    def load_snapshot(year: int):
        if year not in paths:
            raise ValueError(f"No local archives configured for year {year}")
        ff_path, p_path = paths[year]
        ff_blob = _read(ff_path)
        p_blob = _read(p_path)
        ff = study.parse_ff5(study._zip_text(ff_blob))
        ports = study.parse_port6(study._zip_text(p_blob))
        records = [
            _record("FF5", year, ff_path, ff_blob),
            _record("6_Portfolios_2x3", year, p_path, p_blob),
        ]
        return ff, ports, records

    return load_snapshot


def main() -> None:
    ap = argparse.ArgumentParser(description="Run MNSc-FamaFrench-01 from locally saved official Kenneth French archives.")
    ap.add_argument("--old-year", type=int, default=2024)
    ap.add_argument("--new-year", type=int, default=2025)
    ap.add_argument("--old-ff5", required=True)
    ap.add_argument("--new-ff5", required=True)
    ap.add_argument("--old-port6", required=True)
    ap.add_argument("--new-port6", required=True)
    ap.add_argument("--output", default="artifacts-local")
    args = ap.parse_args()

    for p in [args.old_ff5, args.new_ff5, args.old_port6, args.new_port6]:
        if not Path(p).is_file():
            raise FileNotFoundError(p)

    study.load_snapshot = build_local_loader(args)
    study.write_outputs(args.old_year, args.new_year, Path(args.output))


if __name__ == "__main__":
    main()
