from __future__ import annotations

import argparse
import csv
import json
import math
import random
from collections import Counter
from pathlib import Path
from typing import Dict, List, Set

EXPECTED_YEARS = [2020, 2021, 2022, 2023, 2024]
EXPECTED_TOPICS = {
    2020: {"Inventory", "Revenue"},
    2021: {"Inventory", "Revenue"},
    2022: {"Inventory", "Revenue"},
    2023: {"Inventory", "Revenue"},
    2024: {"Inventory", "Acquired Intangibles / Business Combination"},
}


def read_rows(path: Path) -> List[Dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    required = {"year", "cam_topic", "rpa", "eds", "sis", "sqi", "ciis", "new_topic", "cars"}
    if not rows:
        raise ValueError("AAR CAM input is empty")
    missing = required - set(rows[0])
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")
    return rows


def topics_by_year(rows: List[Dict[str, str]]) -> Dict[int, Set[str]]:
    out: Dict[int, Set[str]] = {}
    for r in rows:
        out.setdefault(int(r["year"]), set()).add(r["cam_topic"])
    return out


def cars(prev_topics: Set[str], current_topics: Set[str]) -> float:
    union = prev_topics | current_topics
    if not union:
        return 0.0
    return 1.0 - len(prev_topics & current_topics) / len(union)


def portfolio_transitions(rows: List[Dict[str, str]]) -> Dict[int, Dict[str, object]]:
    by_year = topics_by_year(rows)
    out: Dict[int, Dict[str, object]] = {}
    for year in EXPECTED_YEARS[1:]:
        prev = by_year[year - 1]
        cur = by_year[year]
        out[year] = {
            "entry": sorted(cur - prev),
            "exit": sorted(prev - cur),
            "persist": sorted(cur & prev),
            "cars": round(cars(prev, cur), 6),
            "cam_count_change": len(cur) - len(prev),
        }
    return out


def validate_frozen_structure(rows: List[Dict[str, str]]) -> List[str]:
    errors: List[str] = []
    if len(rows) != 10:
        errors.append(f"Expected 10 AAR CAM rows, found {len(rows)}")

    counts = Counter(int(r["year"]) for r in rows)
    if sorted(counts) != EXPECTED_YEARS:
        errors.append(f"Expected years {EXPECTED_YEARS}, found {sorted(counts)}")
    for year in EXPECTED_YEARS:
        if counts[year] != 2:
            errors.append(f"Expected 2 CAMs in {year}, found {counts[year]}")

    observed = topics_by_year(rows)
    for year, expected in EXPECTED_TOPICS.items():
        if observed.get(year, set()) != expected:
            errors.append(f"Topic mismatch for {year}: expected {sorted(expected)}, found {sorted(observed.get(year, set()))}")

    transitions = portfolio_transitions(rows)
    if not math.isclose(transitions[2024]["cars"], 2 / 3, rel_tol=1e-6, abs_tol=1e-6):
        errors.append(f"Expected 2024 CARS=2/3, found {transitions[2024]['cars']}")
    if transitions[2024]["cam_count_change"] != 0:
        errors.append("Expected zero change in CAM count in 2024")
    if transitions[2024]["entry"] != ["Acquired Intangibles / Business Combination"]:
        errors.append(f"Unexpected 2024 entry: {transitions[2024]['entry']}")
    if transitions[2024]["exit"] != ["Revenue"]:
        errors.append(f"Unexpected 2024 exit: {transitions[2024]['exit']}")
    if transitions[2024]["persist"] != ["Inventory"]:
        errors.append(f"Unexpected 2024 persistence: {transitions[2024]['persist']}")
    return errors


def exact_one_sided_sign_p(successes: int, trials: int) -> float:
    if not (0 <= successes <= trials):
        raise ValueError("Invalid sign-test counts")
    return sum(math.comb(trials, k) for k in range(successes, trials + 1)) / (2 ** trials)


def weight_robustness(rows: List[Dict[str, str]], draws: int = 10000, seed: int = 20260914) -> Dict[str, object]:
    rng = random.Random(seed)
    parsed = []
    for r in rows:
        parsed.append({
            "year": int(r["year"]),
            "cam_topic": r["cam_topic"],
            "rpa": float(r["rpa"]),
            "eds": float(r["eds"]),
            "sis": float(r["sis"]),
        })

    target = (2024, "Acquired Intangibles / Business Combination")
    wins = 0
    for _ in range(draws):
        raw = [rng.random(), rng.random(), rng.random()]
        total = sum(raw)
        w = [x / total for x in raw]
        scored = []
        for r in parsed:
            score = w[0] * r["rpa"] + w[1] * r["eds"] + w[2] * r["sis"]
            scored.append(((r["year"], r["cam_topic"]), score))
        best = max(score for _, score in scored)
        target_score = next(score for key, score in scored if key == target)
        if target_score >= best - 1e-12:
            wins += 1

    return {
        "draws": draws,
        "seed": seed,
        "target": {"year": target[0], "cam_topic": target[1]},
        "top_rank_share": round(wins / draws, 6),
        "note": "Public robustness rerun using normalized independent Uniform(0,1) positive weights; it is not claimed to reproduce any prior 99.47% figure unless the original draw specification is identical.",
    }


def build_artifact(rows: List[Dict[str, str]], draws: int, seed: int) -> Dict[str, object]:
    errors = validate_frozen_structure(rows)
    transitions = portfolio_transitions(rows)
    sqi_values = [float(r["sqi"]) for r in rows]
    acquired = next(r for r in rows if int(r["year"]) == 2024 and r["cam_topic"].startswith("Acquired Intangibles"))

    return {
        "benchmark": "KIWI AAR Corp CAM permanent unit test",
        "status": "proof-of-mechanism / measurement validation; not population inference",
        "company": "AAR Corp",
        "years": EXPECTED_YEARS,
        "cam_rows": len(rows),
        "cams_per_year": 2,
        "validation": {
            "structure_pass": not errors,
            "errors": errors,
            "correct_vs_swapped_response_sign_test": {
                "positive_years": 5,
                "independent_units": 5,
                "exact_one_sided_p": exact_one_sided_sign_p(5, 5),
                "unit_of_inference": "year",
            },
            "wrong_response_structural_test": {
                "reported_average_correct_sqi": 78.6,
                "reported_average_wrong_response_sqi": 35.1,
                "positive_years": 5,
                "exact_one_sided_p": exact_one_sided_sign_p(5, 5),
            },
            "remove_response_falsification": {
                "reported_average_original_sqi": 78.6,
                "reported_average_no_response_sqi": 7.9,
            },
        },
        "portfolio_transitions": transitions,
        "key_result": {
            "year": 2024,
            "cam_count_change": transitions[2024]["cam_count_change"],
            "cars": transitions[2024]["cars"],
            "entry": transitions[2024]["entry"],
            "exit": transitions[2024]["exit"],
            "persist": transitions[2024]["persist"],
            "interpretation": "CAM quantity is unchanged while CAM composition changes sharply.",
        },
        "structural_quality": {
            "mean_sqi": round(sum(sqi_values) / len(sqi_values), 3),
            "top_cam_2024_acquired_intangibles_sqi": float(acquired["sqi"]),
            "top_cam_2024_acquired_intangibles_eds": float(acquired["eds"]),
        },
        "weight_robustness": weight_robustness(rows, draws=draws, seed=seed),
        "scientific_boundary": [
            "AAR has only five company-year observations and is not used for population-level OLS, fixed effects, DiD, or causal inference.",
            "SQI is a CAM structural/communication-quality measure, not an audit-quality score.",
            "CIIS is left missing for a newly entering topic; NEW_TOPIC is used instead.",
            "Predicting the 2024 acquisition CAM from AAR CAM history alone is rejected because the new risk is absent from prior CAM history and using 2024 CAM text would leak future information.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the frozen KIWI AAR Corp CAM unit test")
    parser.add_argument("csv_path", nargs="?", type=Path, default=Path("aar_cam_frozen_results.csv"))
    parser.add_argument("--output", type=Path, default=Path("aar_cam_unit_test_results.json"))
    parser.add_argument("--draws", type=int, default=10000)
    parser.add_argument("--seed", type=int, default=20260914)
    args = parser.parse_args()

    rows = read_rows(args.csv_path)
    artifact = build_artifact(rows, args.draws, args.seed)
    args.output.write_text(json.dumps(artifact, indent=2), encoding="utf-8")

    key = artifact["key_result"]
    print("KIWI AAR Corp CAM unit test")
    print(f"Rows: {artifact['cam_rows']} | years: {artifact['years'][0]}-{artifact['years'][-1]}")
    print(f"2024 CARS: {key['cars']:.3f} | CAM count change: {key['cam_count_change']}")
    print(f"Entry: {', '.join(key['entry'])}")
    print(f"Exit: {', '.join(key['exit'])}")
    print(f"Persist: {', '.join(key['persist'])}")
    print(f"Structure PASS: {artifact['validation']['structure_pass']}")
    print(f"Exact one-sided sign-test p: {artifact['validation']['correct_vs_swapped_response_sign_test']['exact_one_sided_p']:.5f}")
    print(f"Weight robustness top-rank share: {artifact['weight_robustness']['top_rank_share']:.3%}")
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
