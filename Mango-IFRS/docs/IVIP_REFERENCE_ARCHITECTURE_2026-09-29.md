# IVIP — IFRS Value Intelligence Platform

**Reference Architecture — 29 September 2026**

![IVIP architecture and RACI matrix](../assets/IVIP_IFRS_Value_Intelligence_Architecture_Matrix_2026-09-29.svg)

## Architecture

**Evidence → Economic Event → IFRS Truth → Accounting Consequence → Economic Consequence → Six-Capital Value → Risk & Assurance → Human Decision → ERP Action → Realized Value → Learning**

| Component | Primary role |
|---|---|
| Google ADK | Master runtime orchestration, routing, parallel execution, state, security, HITL and deployment |
| Gemini | Event detection, document/data ingestion and multimodal evidence structuring |
| IFRS GraphRAG | Authoritative, versioned IFRS retrieval and grounding |
| Claude | IFRS technical judgment, professional skepticism and independent challenge |
| Rules Engine | Deterministic calculations, journal logic, validation and controls |
| GPT | Economic reasoning, scenario analysis, value intelligence, six-capital mapping and evaluation |
| Human Gate | Final approval, governance and accountability |
| Antigravity / Codex | Development, testing and maintenance; not accounting authority |

## Core design rule

IFRS and accounting truth remain separate from value intelligence. Value analysis evaluates the consequences of a compliant accounting treatment but does not alter the treatment itself.

## Original PNG

The original generated PNG is archived in Google Drive under **05 — DARWIN IFRS Integrated Value Brain** as `IVIP_IFRS_Value_Intelligence_Architecture_Matrix_2026-09-29.png`.
