# NAAIL OpenLab™ — V1.3 Stage 2A Blind Benchmark Packet Freeze

**Artifact maturity:** `RESEARCH_PROTOTYPE`  
**Stage 2A design outcome:** `REVISED_AFTER_CHALLENGE`  
**Candidate-model execution:** `REGISTERED_NOT_EXECUTED`  
**CVPO numeric result:** `NOT_EXECUTED`  

> **PATENT RIGHTS RESERVED — PATENT APPLICATION PREPARATION IN PROGRESS**

## Executive finding

The original V1.3 12-task benchmark packet is preserved, but it is no longer treated as promotion-grade blind evidence. Its task prompts are already public in GitHub and Google Drive, and all 12 tasks are concentrated in factor-robustness retrieval/inference. That makes the packet useful for development/calibration, but it does not satisfy the broader V1.3 Phase 2 contract for blind professional accounting/audit evaluation across CAM classification, assertion mapping, ICFR reasoning, accounting judgment, evidence retrieval, contradiction detection and explanation quality.

The design has therefore been revised after challenge rather than silently overwritten.

## Public 12-task packet

The existing files remain unchanged in the audit trail:

- `blind_professional_benchmark_holdout_tasks_v1_3.csv`
- `blind_benchmark_scoring_schema_v1_3.csv`

Their new governance role is **public development/calibration set only**. They must not be used as the sole promotion-grade blind benchmark.

## Replacement promotion-grade design

A new **private V1.3B 21-task packet** has been frozen in Google Drive only. The packet contains exactly seven professional domains for each of the three benchmark companies:

1. CAM classification;
2. assertion mapping;
3. ICFR reasoning;
4. accounting judgment;
5. evidence retrieval;
6. contradiction detection;
7. explanation quality.

This yields **21 tasks = 7 domains × 3 companies**. Candidate-model prompts and the gold key are intentionally excluded from public GitHub until candidate responses are frozen.

The private packet includes four controlled tabs:

- `Tasks` — 21 private prompts with evidence-source IDs and task status;
- `Gold_Key` — private answers/rubrics and evidence anchors;
- `Evidence_Manifest` — public-source artifact names and Git blob SHAs;
- `Run_Control` — isolation, gold-key access, failure preservation, telemetry and promotion rules.

## Frozen evidence sources

The private benchmark packet references the following public evidence anchors by exact Git blob SHA:

| ID | Artifact | Git blob SHA | Scope |
|---|---|---|---|
| E1 | `MICROSOFT_POC_V1.md` | `2e84a012da7e611e1639fd48afdf4fdc52b48a29` | MSFT audit/CAM/ICFR, finance, innovation and historical status boundaries |
| E2 | `executed_company_features_2026_09_17.csv` | `56aecefec2cde5565101a5a4608f5d861b12641c` | Three-company financial/CAM/ICFR/market features |
| E3 | `bounded_cam_text_features_2026_09_17.csv` | `3d28ab85a4b48f68d4eaa7f194b0ae98bfbdf53d` | CAM counts/topics and bounded metadata |
| E4 | `evidence_passports_wmt_jpm_2026_09_17.json` | `ab476376a99026bec45febd84ef827c101f544bb` | WMT/JPM provenance, results and limitations |
| E5 | `initial_falsification_register_wmt_jpm_2026_09_17.md` | `91635d307e28a07b99dbd8fd222804e2d9b3a7d2` | Contradictory/revised/request-more-evidence cases |
| E6 | `synthetic_abc_tdabc_microcases_2026_09_17.csv` | `3731cdd33b193e090e62caa261f36a5ab99b2c7b` | Synthetic management-accounting boundary cases |
| E7 | `factor_robustness_diagnostics_v1_3.csv` | `489ba1d9cd7e7242da0df500330c38898b36c3c9` | HC3/HAC(3), influence and leave-one-out diagnostics |
| E8 | `ff5_robustness_summary_v1_3.csv` | `68c634b8406ebcc5720cbd03a45541c94cfc2ccc` | Compact FF5 robustness evidence |

## Public scoring and run-control artifacts

Two new non-secret public files are added:

- `blind_benchmark_scoring_schema_v1_3b.csv`
- `blind_benchmark_run_manifest_template_v1_3b.csv`

The V1.3B scoring system reports per-task normalized scores, company scores, domain scores and an overall score that **equal-weights the seven professional domains**. It separately preserves grounding, contradiction handling and explanation quality. Raw response hashes must be frozen before opening the gold key.

## Blind-run controls

Promotion-grade candidate runs must satisfy these controls:

1. same frozen evidence packet and task order for every candidate;
2. separate fresh session/run for each model;
3. no candidate response shared with another candidate;
4. gold key inaccessible to candidate context until all candidate responses are frozen;
5. browsing disabled where controllable; otherwise the tool-access condition is recorded and not silently pooled with closed-evidence runs;
6. raw response plus SHA-256 frozen before scoring;
7. provider/model/version, timestamp, inference settings, latency, token counts, API cost and price provenance recorded;
8. refusals, failed calls, missing outputs, nulls and contradictions retained as observations;
9. prospective human-verification minutes captured for CVPO rather than backfilled after the fact.

## Stage boundary

Stage 2A infrastructure/design work is now frozen. **No candidate model has been run under this V1.3B packet in this record.** Therefore:

- Phase 2 is not promoted;
- Professional AI Benchmark remains `REGISTERED_NOT_EXECUTED` for promotion-grade evidence;
- numeric Cost per Verified Professional Output™ remains `NOT_EXECUTED`;
- no Human Gate status changes;
- no independent-replication status changes;
- no Phase 3 or Phase 4 promotion follows from this design freeze.

The next dependent work package is **Stage 2B — independent blind model runs**. It may start only with independently invokable candidate models and preserved run telemetry.
