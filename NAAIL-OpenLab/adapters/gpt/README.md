# GPT Financial Services Adapter

## Goal

Create a **separate GPT-native implementation** inspired by the workflow patterns in Anthropic's public `financial-services` repository, while keeping NAAIL/PCAOB provider-neutral.

Upstream reference: https://github.com/anthropics/financial-services

Upstream license: Apache-2.0. Any upstream material reused or modified must preserve the applicable copyright/license notices.

## Design principle

We do **not** make Claude a dependency of the GPT implementation.

```
Financial workflow specification
        |
        v
NAAIL provider-neutral task schema
        |
        +--> GPT Adapter (primary)
        |
        +--> Claude Adapter (optional, separate)
        |
        +--> Other model adapters
        |
        v
Reviewer / Falsification
        |
        v
Human Approval
```

## First workflows to translate

The upstream repository includes several useful reference workflows. For accounting/audit research, prioritize:

1. **GL Reconciler** → GPT GL Reconciliation Agent
2. **Month-End Closer** → GPT Close Review Agent
3. **Statement Auditor** → GPT Financial Statement Review Agent
4. **Valuation Reviewer** → GPT Valuation Review Agent
5. **Earnings Reviewer** → GPT Filing/Earnings Review Agent

Then extend independently for the PCAOB research program:

- CAM Inspection Agent
- ICFR Inspection Agent
- Audit Evidence Agent
- PCAOB Standards Agent
- Documentation/Compliance Agent
- Independent Reviewer/Falsification Agent

## GPT adapter contract

Each GPT-native agent should expose a common interface:

- `task`: the inspection/accounting objective
- `evidence`: authorized input documents/data
- `standards`: applicable accounting/auditing/regulatory criteria
- `tools`: explicitly allowed tools
- `output_schema`: structured findings
- `evidence_links`: provenance for every material finding
- `confidence`: calibrated model confidence where appropriate
- `exceptions`: unresolved or conflicting evidence
- `human_gate`: mandatory approval state

## Separation rule

Keep provider-specific code under separate directories:

```
NAAIL-OpenLab/
  adapters/
    gpt/
    claude/
  agents/
    accounting/
    audit/
    pcaob/
  evaluation/
    reviewer/
    falsification/
  provenance/
```

GPT is the initial primary implementation. Claude remains an optional comparison/challenge provider. Provider-neutral schemas sit above both.

## Research controls

- Never allow an agent to approve its own material conclusion.
- Preserve evidence lineage.
- Log model/provider/version and tool calls.
- Require human approval for regulatory/audit conclusions.
- Evaluate false positives and false negatives.
- Use synthetic/public/authorized data only.
- Separate reference code from independently developed PCAOB modules.

## Attribution

This design references workflow concepts made publicly available in Anthropic's `financial-services` repository. The upstream repository is licensed under Apache License 2.0. This file describes an independent GPT-oriented adaptation and does not imply affiliation with or endorsement by Anthropic, OpenAI, PCAOB, or DXC.
