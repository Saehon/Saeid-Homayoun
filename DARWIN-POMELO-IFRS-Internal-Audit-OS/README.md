# DARWIN-POMELO IFRS Internal Audit OS

**Status:** Architecture / MVP build  
**Owner / Principal Investigator:** Saeid Homayoun  
**Version:** v1.0 — 1 October 2026

## Purpose

DARWIN-POMELO IFRS Internal Audit OS is an evidence-governed, provider-neutral architecture for connecting:

**ERP / Business Event → IFRS → Internal Audit → Evidence → Risk / Control → Counterfactual → Value → Decision → Learning**

### Operating roles

- **Google Antigravity:** control plane and multi-agent execution surface.
- **POMELO:** universal task/model/evidence router and cost governor.
- **DARWIN:** decision and sustainable economic-value logic.
- **GPT:** builder, accounting/quant reasoning, coding and reconciliation.
- **Claude:** independent challenger, critic and falsifier.
- **Gemini:** Antigravity-native planner/executor and evidence verifier.
- **IBM Granite / local models:** open/local cheap-first extraction, classification, RAG and first-pass reasoning.
- **Human reviewer:** final authority for material professional judgments.

## Architecture rule

The project preserves the NAAIL two-core constitution:

1. **Stable Knowledge Core**
2. **Replaceable Technology Core**

For implementation, four operational cores are exposed without creating new permanent constitutional cores:

- Knowledge Core
- Science Core
- Technology Core
- Synthetic / GAN / Digital Twin Core

## Open-source-first routing

```text
CACHE
→ deterministic rules / SQL / Python / Arelle
→ retrieval / Knowledge Graph / RAG
→ IBM Granite / local model
→ low-cost hosted model
→ GPT OR Claude
→ GPT + Claude independent review
→ Human Gate
```

Frontier models are called only when task complexity, uncertainty, materiality or disagreement requires them.

## Governance invariants

- No evidence → no material audit conclusion.
- No model or agent may approve its own material work.
- Synthetic evidence is never silently treated as real audit evidence.
- Provider/model changes may not silently rewrite professional or scientific meaning.
- Material conclusions require traceability, uncertainty disclosure and human approval.
- Public material remains non-enabling; patent-sensitive implementation stays private.

## Documents

- [Master Architecture](./MASTER_ARCHITECTURE.md)
- [Roadmap](./ROADMAP.md)
- [Governance](./GOVERNANCE.md)

## Public / private boundary

This public folder documents the high-level architecture, interfaces, governance and execution roadmap. Detailed routing logic, private evaluators, proprietary adapters, unpublished methods, credentials, partner-confidential material and patent-sensitive implementation remain in private `pomelo-core` or other separately governed private assets.
