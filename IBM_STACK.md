# IBM Accounting & Audit AI Stack

IBM has been integrated as a replaceable technology layer across the new domain structure.

Start here:
- [IBM integration map](integrations/ibm/README.md)
- [IBM stack configuration](integrations/ibm/stack.yaml)
- [IBM Granite models](models/ibm-granite/README.md)
- [Detailed architecture](docs/IBM_STACK.md)

Domain entry points:
- [Accounting AI](accounting-ai/README.md)
- [Audit AI](audit-ai/README.md)
- [ICFR AI](icfr-ai/README.md)
- [CAM AI](cam-ai/README.md)
- [KAM AI](kam-ai/README.md)
- [IFRS AI](ifrs-ai/README.md)
- [ESG AI](esg-ai/README.md)

Agent flow:
[Auditor](agents/auditor-agent/README.md) → [Reviewer](agents/reviewer-agent/README.md) → [Falsification](agents/falsification-agent/README.md) → Human Gate.

Default research path: Granite + Granite Embeddings + Docling + BeeAI Framework.
Optional enterprise adapters: watsonx.ai, watsonx.governance and IBM OpenPages.
