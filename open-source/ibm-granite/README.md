# IBM Granite Open-Source Integration

This folder connects the Saeid-Homayoun research repository to IBM's open Granite model ecosystem without copying large model weights into GitHub.

## Recommended models

| Role | Model | Why |
|---|---|---|
| **Default practical model** | `ibm-granite/granite-4.0-h-tiny` | 7B total / ~1B active; long-context, instruction following, RAG and tool-calling with relatively low inference cost |
| **Flagship reference model** | `ibm-granite/granite-4.0-h-small` | 32B total / ~9B active; IBM's workhorse Granite 4.0 model for enterprise RAG and agent workflows |
| **Document/financial-report vision** | `ibm-granite/granite-4.0-3b-vision` | Table, chart and document extraction; useful for annual reports and audit evidence |
| **Speech / meeting transcription** | `ibm-granite/granite-4.0-1b-speech` | Lightweight multilingual speech recognition for meetings/interviews |

Granite 4.0 language models are released under Apache-2.0. Always verify the individual model card and license before redistribution or production use.

## Research use in this repository

Suggested accounting/auditing pipeline:

```text
SEC / XBRL / IFRS / CAM-KAM / ICFR evidence
                |
                v
        retrieval / document layer
                |
                v
 Granite-4.0-H-Tiny (default agent)
                |
        +-------+-------+
        |               |
        v               v
 Granite Vision     reviewer / tests
        |               |
        +-------+-------+
                |
                v
          Human approval
```

Potential tasks:
- financial-report summarisation and extraction
- CAM/KAM classification and comparison
- ICFR risk narratives
- IFRS/ESG evidence-grounded RAG
- agent tool-calling
- chart/table extraction from annual reports
- research demonstrations and reproducible teaching examples

## Hugging Face links

- IBM Granite organization: https://huggingface.co/ibm-granite
- Granite 4.0 H Tiny: https://huggingface.co/ibm-granite/granite-4.0-h-tiny
- Granite 4.0 H Small: https://huggingface.co/ibm-granite/granite-4.0-h-small
- Granite 4.0 Vision: https://huggingface.co/ibm-granite/granite-4.0-3b-vision
- Granite 4.0 Speech: https://huggingface.co/ibm-granite/granite-4.0-1b-speech
- Saeid Homayoun Hugging Face profile: https://huggingface.co/SADHON

## IBM source

- IBM Granite GitHub: https://github.com/ibm-granite
- Granite 4.0 language models: https://github.com/ibm-granite/granite-4.0-language-models

## Quick start

```bash
pip install -r requirements.txt
python examples/accounting_assistant.py
```

The example loads the model directly from IBM's Hugging Face repository. No model weights are committed to this GitHub repository.

## Governance

This integration is for research and education. Model outputs must be treated as machine-generated analysis, not audit evidence, accounting advice, or final professional judgement. Preserve source provenance and human approval for consequential uses.
