# IBM Stack for Accounting, Audit, ICFR, CAM/KAM, IFRS and ESG

## Architecture

```
Source evidence
   ↓
Docling
   ↓
Granite Embeddings / retrieval
   ↓
IBM Granite LLM
   ↓
Auditor Agent
   ↓
Reviewer Agent
   ↓
Falsification Agent
   ↓
Human Gate
```

Optional enterprise layer:
- watsonx.ai — managed AI runtime
- watsonx.governance — AI governance and monitoring
- OpenPages Internal Audit Management — audit GRC
- OpenPages Financial Controls Management — ICFR/SOX GRC
- OpenPages ESG risk management — ESG governance

## Why this split

The open-source path supports reproducible university research without a commercial dependency. Enterprise IBM products can be connected when an institution or design partner has the required license.

## Research controls

1. Freeze model revision and prompt/template for each empirical run.
2. Preserve original documents independently of AI-generated outputs.
3. Store evidence lineage from source page/table/XBRL fact to model output.
4. Use independent reviewer and falsification stages.
5. Require human approval for final research labels or professional conclusions.
6. Report model limitations and error rates.

## Upstream references

- https://github.com/ibm-granite
- https://huggingface.co/ibm-granite
- https://github.com/docling-project/docling
- https://github.com/i-am-bee/beeai-framework
- https://www.ibm.com/products/watsonx-ai
- https://www.ibm.com/products/watsonx-governance
- https://www.ibm.com/products/openpages
