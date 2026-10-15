"""Jev-family accounting benchmark: dependency-free, no model installation required.

Evaluate independently obtained model probabilities from a CSV. This script does
NOT call TypeSafe/Jev/OpenJev and does not assert model compatibility.
"""
import argparse
import csv
import json
import math
from collections import defaultdict

VARIANTS = {
    "openjev_rlcd": {"source": "https://github.com/ZimmyGao/openjev-rlcd",
                     "role": "calibration/RLCD research; requires separate GPU training"},
    "openjev_verdict": {"source": "https://github.com/Heman10x-NGU/openJev-verdict-2.0",
                        "role": "candidate typed-decision classifier; separate model setup"},
    "openjevx": {"source": "https://github.com/muthuishere/openjevx",
                 "role": "local inference service; separate install and credentials"},
    "logistic_baseline": {"source": "user-trained calibrated baseline",
                          "role": "control comparator, not supplied by this script"},
}
ICFR = {"effective", "ineffective", "unknown"}
DOMAINS = {"revenue", "inventory", "goodwill", "tax", "other"}
def evaluate(rows, threshold=0.5):
    groups = defaultdict(list)
    for row in rows:
        if row["icfr_status"] not in ICFR:
            raise ValueError("ICFR status must be effective/ineffective/unknown")
        p = float(row["p_event"])
        if not math.isfinite(p) or not 0 <= p <= 1:
            raise ValueError("Probability must be finite and in [0,1]")
        if row["label"] not in ("0", "1", ""):
            raise ValueError("label must be 0, 1, or blank")
        if row["label"] == "":
            continue  # unknown outcome never treated as negative
        y = int(row["label"])
        groups[(row["variant"], row["industry"], row["domain"])].append((p, y))
    output = []
    for (variant, industry, domain), data in sorted(groups.items()):
        n = len(data)
        brier = sum((p-y)**2 for p,y in data)/n
        tp = sum(p >= threshold and y == 1 for p,y in data)
        fp = sum(p >= threshold and y == 0 for p,y in data)
        fn = sum(p < threshold and y == 1 for p,y in data)
        output.append(dict(variant=variant, industry=industry, domain=domain,
                           n=n, brier=round(brier, 6),
                           precision=round(tp/(tp+fp), 6) if tp+fp else None,
                           recall=round(tp/(tp+fn), 6) if tp+fn else None))
    return output

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="CSV with variant,industry,domain,icfr_status,label,p_event")
    parser.add_argument("--threshold", type=float, default=0.5)
    parser.add_argument("--variants", action="store_true")
    args = parser.parse_args()
    if args.variants:
        print(json.dumps(VARIANTS, indent=2))
        return
    if not args.input:
        parser.error("--input is required unless --variants is supplied")
    if not 0 <= args.threshold <= 1:
        parser.error("threshold must be in [0,1]")
    with open(args.input, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        required = {"variant", "industry", "domain", "icfr_status", "label", "p_event"}
        if not required.issubset(reader.fieldnames or []):
            parser.error("Missing CSV columns: " + ", ".join(sorted(required-set(reader.fieldnames or []))))
        results = evaluate(reader, args.threshold)
    print(json.dumps({"results": results, "caveat": "Descriptive only; no statistical inference or model run"}, indent=2))

if __name__ == "__main__":
    main()
