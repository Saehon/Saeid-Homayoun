# NAAIL OpenLab™ Provider-Neutral API Contract

## Purpose

This contract defines the public capability boundary between NAAIL OpenLab Core™ and marketplace-specific adapters. It is intentionally provider-neutral so OpenAI, Google, and Microsoft distribution layers can call the same governed research service.

## Design rules

- Tools are task-specific, not unrestricted shell/browser/database access.
- Every tool receives a request ID and user/tenant context from the authenticated adapter.
- Every material result returns provenance, execution status, limitations, and Human-Gate state.
- Restricted/private implementation details remain server-side.
- Tool failure is explicit; it is never converted into a fabricated successful result.

## Canonical response envelope

```json
{
  "request_id": "uuid",
  "tool": "tool_name",
  "status": "SUCCEEDED | FAILED | NOT_EXECUTED | REQUIRES_HUMAN_APPROVAL",
  "result": {},
  "evidence": [],
  "limitations": [],
  "human_gate": "NOT_REQUIRED | PENDING_HUMAN_APPROVAL | APPROVED | REJECTED"
}
```

## Public tool boundary

### `frame_research_question`
Converts a user problem into a bounded research question, constructs, unit of analysis, time horizon, and candidate evidence requirements.

### `generate_competing_hypotheses`
Generates multiple falsifiable hypotheses with theoretical mechanisms and explicit alternatives. Consensus is not treated as proof.

### `retrieve_evidence_metadata`
Returns rights-cleared evidence metadata and citations/provenance needed for the active task. It must not redistribute restricted full text without permission.

### `build_empirical_design`
Creates variables, sample definition, identification strategy, estimators, expected tables/figures, robustness tests, falsification tests, and reproducibility requirements.

### `run_reproducible_analysis`
Executes only approved analytical workflows against user-authorized or rights-cleared data and returns code/run metadata sufficient for reproducibility where feasible.

### `evaluate_robustness`
Runs or specifies robustness, placebo, sensitivity, alternative-measure, out-of-sample, or adversarial checks relevant to the design.

### `build_chain_of_evidence`
Builds a traceable map from question → theory → evidence → data → variables → model → result → robustness → interpretation → limitations.

### `request_human_gate`
Packages material conclusions and unresolved limitations for human approval/rejection. The tool itself does not self-approve.

### `export_research_artifact`
Exports an approved research artifact, preserving provenance, model/tool identifiers, limitations, and approval status.

## High-risk actions

The public adapter must not autonomously:

- submit manuscripts or professional reports on behalf of a user without explicit confirmation;
- sign audit/accounting/assurance opinions;
- alter source datasets without a recoverable transformation record;
- expose credentials or secrets;
- bypass data-use restrictions;
- present AI-generated or simulated values as observed empirical evidence;
- override the Human Gate.

## Versioning

Marketplace adapters should declare the NAAIL API contract version they support. Breaking changes require a new contract version and regression testing across all provider adapters.
