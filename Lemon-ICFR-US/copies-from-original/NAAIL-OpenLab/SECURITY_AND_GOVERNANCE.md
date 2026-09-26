# NAAIL OpenLab™ — Security, Privacy & Governance

This public standard defines the minimum controls for NAAIL research and education environments.

## Security principles
- least privilege for every agent and tool;
- deny by default for side-effecting actions;
- separate synthetic/research and future production environments;
- no secrets in source code, prompts, notebooks, logs, or traces;
- explicit data classification and rights checks;
- human approval for high-impact actions;
- trace redaction for sensitive inputs/outputs;
- immutable version/run metadata for material evaluations.

## Threats to test
1. Prompt injection and malicious retrieved content.
2. Tool misuse or privilege escalation.
3. Data exfiltration through model/tool outputs.
4. Cross-agent contamination and unsafe handoffs.
5. Retrieval poisoning and unsupported citations.
6. Model hallucination presented as authoritative evidence.
7. Hidden benchmark leakage.
8. Unauthorized use of licensed/copyrighted material.
9. PII/client/student data entering traces or public artifacts.
10. Model/provider changes causing silent regressions.

## Required controls
- scoped tool allowlists;
- tool input/output validation;
- provenance-aware retrieval;
- citation verification;
- data-rights/licensing metadata;
- secrets management outside source control;
- trace redaction and retention policy;
- model/agent/workflow registries;
- independent review for R2/R3 agents;
- fail-closed behavior for missing mandatory evidence/approval.

## Privacy
The public prototype should remain synthetic and privacy-minimizing. Real student, employee, client, health, financial, or confidential business data must not be introduced without an approved legal/privacy/security design and appropriate institutional controls.

## Professional governance
NAAIL outputs are educational/research artifacts unless separately validated in an authorized professional environment. AI agents do not sign audit opinions, certify compliance, or replace qualified professional judgment.

## Incident handling
Any significant defect should create a Failure Memory record containing the trigger, affected versions, impact, reproduction steps, containment action, repair, regression test, reviewer, and closure decision.
