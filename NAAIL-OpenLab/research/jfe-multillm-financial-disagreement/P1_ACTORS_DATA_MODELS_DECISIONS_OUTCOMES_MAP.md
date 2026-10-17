# P1.1 Actors, Data, Models, Decisions, and Outcomes Map

Status: FROZEN v1.0  
Gate: P1.1  
Date: 2026-10-05  
Scope: NAAIL Trust Finance / Multi-LLM Financial Disagreement

## 1. Purpose and boundary

This map defines the whole research system that may produce and evaluate AI Consensus and AI Disagreement (AID). It identifies actors, evidence/data objects, computational/model components, governed decisions, outcomes, handoffs, and authority boundaries.

P1.1 is a system-design inventory. Inclusion means “in scope or potentially required,” not “obtained,” “licensed,” “executed,” “validated,” or “available.” No external-model output, empirical result, causal claim, or novelty claim is created by this map.

## 2. System objective

The system asks whether disagreement among independently executed, version-logged AI models contains incremental information about future financial outcomes beyond their consensus, under temporal integrity, evidence provenance, development-only construct search, sealed testing, and human approval.

System chain:

`public/authorized evidence → as-of evidence packet → frozen multi-model protocol → raw judgments → parsed scores/confidence → pair representations → consensus/AID → preregistered tests → falsification/OOS → human-reviewed claims`

## 3. Actor register

| Actor ID | Actor / role | Inputs | Authorized actions | Outputs | Human approval / prohibition |
|---|---|---|---|---|---|
| A01 | Principal investigator / human owner | Protocols, evidence, reviews, deviations | Approve protected changes, restricted-data use, sealed opening, claims, release, submission, merge | Approval/rejection records; scientific decisions | Final authority; decision must be recorded |
| A02 | Primary project operator | Canonical plan, development data, code, logs | Bounded build/research, tests, dual-save, ledger/queue maintenance | Versioned artifacts and run records | Cannot self-approve protected decisions or merge main |
| A03 | Independent scientific reviewer | Frozen protocol, code, evidence, results | Challenge theory, identification, measurement, leakage, claims | Review findings and required repairs | Cannot rewrite provenance or turn findings into PASS |
| A04 | Accounting/audit domain reviewer | Evidence packets, model judgments, materiality context | Accept/modify/reject/escalate case judgments | Append-only human-review record | No silent override; raw model output immutable |
| A05 | Econometrics/financial-economics reviewer | Estimands, samples, models, tables | Review design, timing, FE/clustering, inference, economics | Identification/inference assessment | Causal language requires supported design |
| A06 | Data steward / licensing authority | Source terms, classifications, access records | Approve location, retention, redistribution, external processing | Data-use decision and access record | Restricted data never enters public GitHub |
| A07 | Evidence acquisition process | SEC/public APIs/authorized sources | Deterministic retrieval, timestamping, hashing | Immutable raw evidence and acquisition logs | Must obey terms, rate limits, and information cutoff |
| A08 | Evidence extraction / feature process | Immutable evidence | Parse, normalize, create as-of features | Derived evidence with lineage | Cannot use future labels/outcomes |
| A09 | External/hosted model providers | Authorized D0/D1 or approved inputs | Execute frozen prompts when actually available | Raw responses and provider metadata | No fabricated run; non-public input needs approval/terms review |
| A10 | Local/open-model runtime | Authorized evidence and model artifact | Execute versioned local models | Raw responses, environment/model hashes | Exact artifact/version and settings required |
| A11 | Parser/scoring engine | Raw model responses | Deterministic parsing and rubric scoring | Scores, confidence, flags, parse errors | Raw output preserved; parser version logged |
| A12 | Pair/AID engine | Scores, confidence, evidence quality | Produce model×model/evidence×model representations, consensus, AID candidates | Versioned constructs | Candidate evolution confined to development |
| A13 | Co-Scientist discovery roles | Theory/literature/development evidence | Generate, criticize, falsify, rank hypotheses | Candidate hypotheses/mechanisms | Structured roles, not fabricated independent evidence |
| A14 | 100-perspective scientific board | Candidate hypotheses/specifications | 10 councils × 10 structured adversarial evaluations | Scores, objections, meta-review | Perspectives are roles, not 100 independent agents |
| A15 | Reproduction/falsification process | Frozen code/data manifests/results | Clean rerun, negative controls, placebos, adversarial tests | Reproduction and falsification records | Cannot tune on sealed results |
| A16 | Journal readers/referees/regulators/investors | Cleared manuscript/package | Evaluate claims and usefulness | External critique/adoption decisions | Receive only release-approved, lawfully shareable artifacts |

## 4. Data and evidence object register

| Data ID | Object | Candidate source/class | Time key | Use | Required controls |
|---|---|---|---|---|---|
| D01 | SEC 10-K/10-Q/8-K filings and exhibits | SEC EDGAR; D0 public | filing/acceptance datetime | Evidence packets; narrative/accounting risk | accession, filing date, retrieval date, hash, as-of rule |
| D02 | XBRL facts and presentation/linkbase metadata | SEC XBRL; D0 | fact period + filing datetime | Accounting variables and evidence quality | taxonomy/unit/context lineage; amendment handling |
| D03 | Audit reports and CAM disclosures | Public filing exhibits; D0 | report/filing date | Audit-risk topics and outcomes | auditor, CAM text/source offsets, topic mapping version |
| D04 | ICFR disclosures/material weaknesses | Public filings; D0; licensed supplements may be D3 | disclosure/event date | Reporting-control outcome/mechanism | event timing, source, taxonomy, no licensed redistribution |
| D05 | Restatement and enforcement/AAER events | SEC/public; licensed supplements D3 | event/announcement/covered period | Reporting/fraud outcomes | first-public date, covered period, duplicate resolution |
| D06 | Earnings announcements/forecast information | Public IR/SEC; licensed forecasts D3 | announcement/forecast timestamps | Information outcomes | as-of availability, vendor license, surprise definition |
| D07 | Security returns, prices, volume, volatility | Public or licensed market data | exchange timestamp/date | Market outcomes/CAR/volatility | trading calendar, delisting/corporate actions, license |
| D08 | Firm/accounting/governance controls | SEC/XBRL/public; Compustat-like data D3 | fiscal period + release date | Controls/heterogeneity | point-in-time availability, transformations, license |
| D09 | News/textual context | Public/authorized sources; class varies | publication datetime | Replication/comparison evidence | source rights, timestamp, deduplication, cutoff |
| D10 | Model metadata and knowledge cutoffs | Provider/model cards/runtime; D0/D2 logs | model/run datetime | Chronology and reproducibility | alias vs exact version, settings, terms, cutoff uncertainty |
| D11 | Frozen prompts/rubrics/parsers | Project-controlled D2 until release | protocol effective datetime | Comparable model execution | version/hash, change control, no outcome feedback |
| D12 | Raw model outputs | Inherit highest input class; normally D2 | execution datetime | Primary judgment evidence | actual run only, immutable raw text, provider/model/settings |
| D13 | Parsed scores/confidence/errors | Derived; inherits input class | run/parser version | Pair/AID inputs | deterministic lineage to D12; missing/error preserved |
| D14 | Human-review judgments | D2; may become D4 if personal data added | review datetime | Validation/escalation | reviewer role, blinded state, append-only decision |
| D15 | Partition manifests | Metadata D2; restricted values may be D3 | freeze timestamp | Development/validation/sealed firewall | immutable IDs, assignment/version/hash, access approval |
| D16 | Synthetic/pseudo-data | D1 | generation version | Dry runs/reproduction stand-in | clearly labelled; no confidential reconstruction |
| D17 | Literature/replication packages | D0 or license-specific | publication/retrieval date | Theory, benchmarks, novelty map | DOI/source/license/package hash |

Candidate sources are not acquisition claims. P2/P4/P5 gates must verify availability, rights, integrity, and chronology before use.

## 5. Model and computational component register

| Component ID | Component | Function | Inputs → outputs | Freeze / verification point |
|---|---|---|---|---|
| M01 | Retrieval and evidence assembler | Build reproducible as-of packets | D01–D09 → evidence packet | P5 acquisition/passport; source/hash/timing tests |
| M02 | Evidence-quality assessor | Score provenance/completeness/ambiguity without future outcomes | packet metadata → quality fields | Define prospectively; do not tune on sealed outcomes |
| M03 | Frozen prompt/rubric protocol | Make comparable financial judgments | packet + D11 → structured request | P6.1; hash before validation |
| M04 | GPT execution adapter | Execute available logged GPT model | request → D12 | Actual provider/version/time/settings only |
| M05 | Claude execution adapter | Execute available logged Claude model | request → D12 | Actual provider/version/time/settings only |
| M06 | Gemini execution adapter | Execute available logged Gemini model | request → D12 | Actual provider/version/time/settings only |
| M07 | Llama/open-model adapter | Execute exact local/open artifact | request → D12 | Model hash/runtime/environment required |
| M08 | Chronology-safe comparator | BERT/Chrono-compatible benchmark where verified | dated evidence → score | P4.4/P6; label exact method, not assumed ChronoLLM |
| M09 | Parser and scoring engine | Convert raw outputs under frozen rubric | D12 → D13 | Unit tests, parse-error handling, version hash |
| M10 | Pair-representation engine | Create model×model and evidence×model features | D13 + D02 quality → pairs | P7; development-only refinement before freeze |
| M11 | Consensus engine | Aggregate model judgments | D13 → consensus | Definition frozen P8.5 |
| M12 | AID candidate/evolution engine | Generate/evaluate disagreement constructs | D13/pairs → candidates/AID* | P8; development only; complexity penalty/archive |
| M13 | Statistical/econometric engine | Run prespecified descriptive/predictive/inferential tests | frozen panel → estimates/metrics | P10/P11; code/environment/manifest locked |
| M14 | Falsification/reproduction engine | Negative controls, leakage checks, clean reproduction | frozen artifacts → audit results | Independent rerun; sealed outcomes never feed selection |
| M15 | Evidence/Science Discovery graph | Link theory, evidence, hypotheses, tests, anomalies, claims | all metadata → traceability graph | P1.4/P2/P3; append-only lineage/versioning |

“AlphaFold-inspired” applies only to pair representation/confidence/recycling design in M10. “AlphaEvolve-inspired” applies only to development-data construct search in M12. Neither label asserts that biological AlphaFold or Google AlphaEvolve has been executed.

## 6. Decision register

| Decision ID | Decision | Decision maker | Evidence required | Possible states | Downstream effect |
|---|---|---|---|---|---|
| J01 | Admit evidence/source | Operator + data steward where needed | provenance, rights, timing, classification | accept / reject / quarantine | Determines eligible evidence universe |
| J02 | Freeze protocol/object | PI for protected objects | version, hash, acceptance checklist, impact map | freeze / revise / reject | Controls validation eligibility |
| J03 | Authorize external-model input | PI/data steward | data class, provider terms/privacy, minimization | approve / prohibit / condition | Determines permitted model execution |
| J04 | Accept model run as evidence | Operator under frozen protocol | actual run log, model/version/settings, raw output | accept / error / exclude with rule | Populates judgment panel |
| J05 | Resolve parser/error state | Frozen deterministic rule; human review for ambiguity | raw output, parser log, rubric | score / missing / escalate | Prevents silent score invention |
| J06 | Retain/reject AID candidate | Frozen development objective | development metrics, complexity, falsification | retain / mutate / reject | Candidate archive; no validation/test feedback |
| J07 | Freeze AID*/consensus | PI approval | development tournament + protocol hashes | freeze / reject / redesign | Enables confirmatory protocol |
| J08 | Open validation | Authorized protocol role | preregistration B, manifests/hashes | open / deny | One-way diagnostic only |
| J09 | Open sealed test | PI explicit approval | preregistration C and P0.3 checklist | open / deny | Confirmatory raw result bundle |
| J10 | Escalate human review | Prespecified materiality/disagreement rule | evidence, scores, uncertainty | accept / modify / reject / escalate | Human state linked without rewriting raw outputs |
| J11 | Promote gate status | Operator/reviewer under P0.5 | gate-specific evidence and readback | PASS / PARTIAL / BLOCKED / etc. | Canonical progress count |
| J12 | Approve claim/release/submission | PI after independent review | claim-evidence-code-table traceability | approve / narrow / reject | External dissemination boundary |

## 7. Outcome register

| Outcome ID | Outcome family | Examples | Role | Timing requirement | Claim boundary |
|---|---|---|---|---|---|
| O01 | Market response | CAR, subsequent return, volatility, volume/liquidity | Primary/secondary financial outcomes to be preregistered | Strictly after evidence cutoff; trading calendar controlled | Predictive association unless causal design supports more |
| O02 | Information realization | Earnings surprise, forecast error, guidance realization | Tests interpretation difficulty/information content | Forecast/announcement timestamps point-in-time | Vendor definitions/licensing documented |
| O03 | Reporting/control quality | ICFR weakness, restatement, filing delay | Reporting-risk outcomes | First-public event after model evidence | Avoid label leakage from later filings |
| O04 | Audit disclosure | CAM occurrence/topic/persistence/change | Audit-risk alignment/outcome | Auditor report date and covered period | CAM is not automatically audit failure |
| O05 | Enforcement/fraud | AAER/enforcement/fraud event | Rare-event outcome/robustness | Event/public date and misconduct period separated | Enforcement is selected detection, not full fraud population |
| O06 | Human-review outcome | agreement, modification, rejection, escalation, time | Construct/process validation | Reviewer blinding and timestamp logged | Not independent when same evidence/protocol designer reviews |
| O07 | Model-process quality | run variance, parse error, calibration, missingness | Measurement/reproducibility outcome | Run/version specific | Engineering quality is not economic validity |
| O08 | Economic/predictive increment | incremental R², AUC/PR-AUC, Brier, utility/cost | Incremental value beyond consensus/baselines | Genuine held-out evaluation | Metric chosen before sealed access; no cherry-picking |
| O09 | Scientific integrity | falsification nulls, leakage findings, reproduction success | Claim-validity boundary | After frozen protocol; raw audit preserved | Failure remains evidence; not converted to PASS |

Outcome definitions, priorities, transformations, and multiplicity remain future P3/P5/P10/P11 work and are not frozen by this inventory.

## 8. Primary interfaces and handoffs

| Interface | Producer → consumer | Required payload | Failure behavior |
|---|---|---|---|
| I01 Evidence acquisition | A07 → A08/M01 | source ID, timestamps, raw hash, retrieval log, class/license | reject/quarantine missing provenance |
| I02 Evidence packet | M01/M02 → M03/models | as-of evidence IDs, content hashes, quality/missingness, cutoff | block runs on future/unauthorized evidence |
| I03 Model execution | M03/adapters → M09 | protocol/model/settings/input IDs/raw output/error/retry | preserve error; never synthesize output |
| I04 Parsed judgment | M09 → M10–M12 | score/confidence/missing/error + lineage | escalate ambiguous parse; no silent coercion |
| I05 Construct freeze | M10–M12 → M13 | AID*/consensus spec, code/hash, development history | validation/test unavailable until freeze |
| I06 Empirical panel | M01/M13 → analysis | partition manifest, as-of features, outcomes, controls, licenses | quarantine timing/rights/duplicate conflicts |
| I07 Results audit | M13 → M14/reviewers | immutable raw results, code/environment, deviations | no claim promotion before falsification/review |
| I08 Claim release | A03–A06/M14 → A01 → A16 | traceability, limitations, approval, lawful package | narrow/reject if evidence or rights incomplete |

## 9. Authority and feedback boundaries

- Human approval controls sealed opening, protected amendments, restricted-data/model use, claims, submission, and merge.
- Raw evidence and raw model outputs are immutable; corrections create new versions with lineage.
- Development may generate hypotheses and constructs. Validation is a one-way diagnostic. Sealed outcomes never feed discovery or evolution.
- Model providers are computational services, not scientific approvers or independent reviewers.
- Co-Scientist and 100-perspective outputs are structured analyses, not independent observations or votes.
- Market, reporting, audit, and enforcement outcomes cannot enter prompts or evidence packets for earlier prediction dates.
- Public GitHub contains only lawful public/synthetic materials, schemas, hashes, code, and cleared aggregates; restricted data remain controlled.

## 10. Inclusion and exclusion boundaries

In scope: public/authorized corporate evidence; reproducible model executions; pair/consensus/disagreement constructs; financial/reporting/audit/enforcement outcomes; falsification, replication, and human review.

Out of scope unless prospectively added through change control: individualized investment advice, autonomous trading, automated audit opinions, regulatory determinations, unapproved personal/sensitive data, fabricated model personas as observations, biological structure prediction, and optimization on validation/sealed outcomes.

## 11. Machine-readable node schema

```yaml
node_id: A01|D01|M01|J01|O01|I01
node_type: actor|data|model_component|decision|outcome|interface
name: string
version: string
classification: D0|D1|D2|D3|D4|null
owner: string|null
inputs: [node_id]
outputs: [node_id]
authority_required: [node_id]
information_cutoff_rule: string|null
evidence_or_specification: [string]
status: proposed|available|verified|frozen|blocked|retired
limitations: [string]
```

## 12. Acceptance test and conclusion

P1.1 may PASS only if the system map identifies actors and authority; candidate data/evidence and controls; model/computational components; governed decisions; outcome families and timing; primary interfaces; feedback/firewall boundaries; and non-claims.

All mapping elements are present in v1.0. P1.1 is PASS for system inventory and boundary design only. Source availability, dependency criticality, operational graph implementation, model execution, construct validity, and empirical outcomes remain later gates.
