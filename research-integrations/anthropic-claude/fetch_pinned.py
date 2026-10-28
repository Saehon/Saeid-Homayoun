#!/usr/bin/env python3
"""Safely download pinned Anthropic repositories into an isolated local directory.
No installation, pip execution, CI activation or agent permissions are performed.
"""
import argparse
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent
manifest = json.loads((ROOT / "upstreams.lock.json").read_text(encoding="utf-8"))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--destination", required=True)
    parser.add_argument("--include", nargs="+", required=True, help="Explicit repository names")
    parser.add_argument("--execute", action="store_true", help="Actually clone (otherwise dry run)")
    args = parser.parse_args()
    dest = pathlib.Path(args.destination).expanduser().resolve()
    entries = {x["name"]: x for x in manifest["repositories"]}
    for name in args.include:
        if name not in entries:
            parser.error("Unknown repository: " + name)
        item = entries[name]
        if not item["install_approved"]:
            parser.error("License/reuse gate blocks " + name)
        target = dest / name
        if target.exists():
            parser.error("Refusing to overwrite: " + str(target))
        print("Pinned fetch:", item["source"], item["commit"], "->", target)
        if args.execute:
            dest.mkdir(parents=True, exist_ok=True)
            subprocess.run(["git", "clone", "--no-checkout", item["source"], str(target)], check=True)
            subprocess.run(["git", "-C", str(target), "checkout", "--detach", item["commit"]], check=True)
    if not args.execute:
        print("Dry run only. Pass --execute to fetch selected repositories.")

if __name__ == "__main__":
    main()
