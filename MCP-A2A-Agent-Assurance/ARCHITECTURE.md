# Architecture

## 1. Protocol layers

| Layer | Function | Examples |
|---|---|---|
| Model clients | Reasoning/generation | Claude, GPT, Gemini, Mistral |
| MCP | Tool and data access | SEC/XBRL, ICFR, IFRS, CAM/KAM |
| A2A | Agent discovery, delegation and handoffs | specialist-agent collaboration |
| AP2/UCP | Authorized economic actions | agentic procurement/payments |
| A2UI/MCP Apps | Interactive professional UI | evidence review, approvals, dashboards |
| NAAIL Assurance | Independent validation | evidence, replication, falsification, controls |
| Human Gate | Accountability | review, exception handling, sign-off |

## 2. Specialist agents

- SEC/XBRL retrieval agent
- ICFR control-evidence agent
- IFRS treatment and judgment agent
- CAM/KAM disclosure agent
- Finance and operations audit agent
- ESG/ESRS/VSME agent
- PCAOB-style inspection agent
- Research assurance agent

## 3. Assurance loop

```text
Task
 -> Specialist agent
 -> Evidence package
 -> Independent reviewer
 -> Falsifier/challenger
 -> Rule/calculation replication
 -> Model-disagreement check
 -> Risk-based escalation
 -> Human approval
 -> Signed result + audit trail
```

## 4. Evidence Passport

Each material result should capture:
- task and user authority;
- source identifiers and retrieval time;
- model/provider/version;
- tool calls and deterministic calculations;
- applicable accounting/audit/control criteria;
- intermediate conclusions;
- reviewer and challenger outputs;
- unresolved conflicts;
- human decision;
- final output hash/version.

## 5. Independence principle

The architecture must not treat multiple agents that share the same hidden state, prompt, data leakage or developer-known benchmark as independent validation. Independence is an experimental and governance property, not a label.

## 6. Minimum viable architecture

The first production-oriented path is:

```text
SEC/XBRL MCP -> LEMON ICFR MCP -> Evidence Passport
             -> independent reviewer/falsifier
             -> human approval
```

A2A should be added after at least two specialist MCPs have passed independent benchmark gates.
