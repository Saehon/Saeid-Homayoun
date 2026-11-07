"""Reproduce v2 three-way screening partition from frozen 424-row file.

Provisional industry roles; DO NOT identify 119 names as confirmed AI investors.
No network, dependencies, or underlying dataset changes required.
"""
from __future__ import annotations
import csv
import argparse
from pathlib import Path

INPUT="INITIAL_424_NONFINANCIAL_FIRMS_2026-10-09.csv"
FIELDS_V2=["research_partition_v2","AI_INDIVIDUAL_CAPEX_VERIFIED",
           "CAM_AS3101_ELIGIBLE_VERIFIED","ICFR_ORIGINAL_LABEL_VERIFIED",
           "PCAOB_PUBLIC_ASOF_VERIFIED","BUYER_SUPPLIER_ACTUAL_ROLE_VERIFIED"]
PRIORITY={"BUILDER_ANCHOR_CASE","SUPPLIER_ANCHOR_CASE",
          "INFRASTRUCTURE_SUPPLY_CANDIDATE_UNVERIFIED",
          "TECH_ADOPTION_CANDIDATE_UNVERIFIED"}
OUT=[
    ("V2_PRIORITY_119_TECH_SUPPLY_CANDIDATES.csv","PRIORITY_119_NOT_TREATMENT"),
    ("V2_COMPARATOR_244_GENERAL_NONFINANCIAL.csv","GENERAL_244_AI_STATUS_UNKNOWN"),
    ("V2_SPECIAL_61_UTILITIES_REAL_ESTATE.csv","SPECIAL_61_SEPARATE_ONLY")
]
def partition(rows:list[dict])->list[list[dict]]:
    if len(rows)!=424 or len({r["cik"] for r in rows})!=424:
        raise ValueError("source must hold 424 unique issuer CIK")
    groups=[[],[],[]]
    for r in rows:
        if r["analysis"]=="SEPARATE_INFRA_SPECIAL":
            i=2
        elif r["role"] in PRIORITY:
            i=0
        elif r["role"]=="OTHER_NONFINANCIAL_UNVERIFIED":
            i=1
        else:raise ValueError(f"Unassigned stratum: {r['ticker']}")
        d={**r,"research_partition_v2":OUT[i][1]}
        d.update({k:"PENDING" for k in FIELDS_V2[1:]})
        groups[i].append(d)
    if [len(g) for g in groups]!=[119,244,61]:
        raise ValueError("cohort partition counts changed")
    if sum(x["role"]=="BUILDER_ANCHOR_CASE" for x in groups[0])!=5:
        raise ValueError("builder anchors changed")
    if sum(x["role"]=="SUPPLIER_ANCHOR_CASE" for x in groups[0])!=5:
        raise ValueError("supplier anchors changed")
    return groups

def main(folder:Path):
    with (folder/INPUT).open(encoding="utf-8",newline="") as f:
        reader=csv.DictReader(f);rows=list(reader);fields=reader.fieldnames or []
    groups=partition(rows)
    for (fn,_),data in zip(OUT,groups):
        with (folder/fn).open("w",encoding="utf-8",newline="") as f:
            w=csv.DictWriter(f,fieldnames=fields+FIELDS_V2)
            w.writeheader();w.writerows(data)
    print("Verified 424 CIKs: 119 candidates / 244 unknown comparators / 61 special sector.")

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("folder",type=Path,help="Directory containing frozen INITIAL_424...csv")
    main(p.parse_args().folder)
