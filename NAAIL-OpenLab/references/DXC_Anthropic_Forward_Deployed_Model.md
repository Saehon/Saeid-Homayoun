# DXC–Anthropic Forward-Deployed Model — Reference for NAAIL / PCAOB Research

## Purpose

This note records the DXC Technology–Anthropic collaboration as an external reference architecture for the NAAIL OpenLab and Embedded PCAOB Inspection Agent research.

It does **not** copy or claim to implement DXC OASIS. It extracts publicly described deployment principles and translates them into a provider-neutral regulatory-inspection research architecture.

## Public industry reference

DXC Technology and Anthropic announced a global alliance in 2026 around Claude-enabled enterprise systems. DXC describes DXC OASIS as an AI-native orchestration platform and describes the use of Claude-certified Forward-Deployed Engineers to work with customers.

Official sources:
- DXC announcement: https://dxc.com/newsroom/06112026-dxc-and-anthropic-announce-multi-year-global-alliance-to-bring-ai-into-mission-critical-enterprise-systems
- Anthropic: https://www.anthropic.com/news/dxc-anthropic-alliance
- DXC partner ecosystem: https://dxc.com/about-us/partner-ecosystem

No claim is made here that DXC OASIS is open source or that its proprietary implementation is included in this repository.

## Reference operating logic

AI platform / foundation model
→ Forward-Deployed team
→ Customer environment
→ Real workflow/problem
→ Authorized data and tools
→ Customized agents
→ Testing
→ Human review
→ Production deployment
→ Measurement
→ Improvement
→ Reusable solution components

## Translation to the PCAOB inspection research architecture

Provider-neutral AI layer
→ PCAOB Forward-Deployed Inspection Team
→ Authorized audit-firm / engagement environment
→ High-risk inspection workflow
→ Audit evidence + documentation + execution traces
→ PCAOB Standards-as-Code / inspection logic
→ Specialized inspection agents
→ Independent Reviewer / Falsification Agent
→ Human PCAOB inspector review and approval
→ Controlled inspection deployment
→ Accuracy + evidence coverage + exception detection + FP/FN measurement
→ Iterative refinement
→ Provider-neutral reusable inspection modules

## Proposed NAAIL modules

- Evidence and lineage adapter
- PCAOB standards/rules knowledge layer
- CAM inspection agent
- ICFR inspection agent
- Risk-assessment inspection agent
- Documentation-compliance agent
- AI-to-AI Reviewer / Falsification agent
- Digital-twin test environment
- Human approval gate
- Evaluation and audit-trace layer

## Research distinction

The proposed PCAOB model is a research architecture for independent regulatory inspection. Its contribution is not DXC's enterprise managed-services product. The research question is how forward-deployed, provider-neutral agentic inspection can operate across heterogeneous audit platforms while preserving evidence lineage, independent challenge, reproducibility, and final human regulatory judgment.

## Status

Concept/reference only. Any implementation should use public APIs, synthetic or authorized data, and independently developed code. Proprietary DXC or audit-firm software is not incorporated.
