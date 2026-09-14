# ECONOVA-S™ GPT-5.6 Sol Product Prototype v0.1

**Status:** runnable research-design prototype  
**Backend:** OpenAI GPT-5.6 Sol (`gpt-5.6-sol`) via the Responses API  
**Architecture:** exactly two permanent cores + supporting AI-to-AI Scientific Intelligence Fabric™

## Run the prototype

Source: [`prototype/`](./prototype/)

```bash
cd prototype
python -m venv .venv
# activate the virtual environment
pip install -r requirements.txt
# copy .env.example to .env and add OPENAI_API_KEY
streamlit run app.py
```

## Product workflow

`Research Question → Systems Map / Causal DAG → Hypothesis Tournament → ERA Empirical Design → Independent Scientific Red Team → Evidence Passport™ → Human Gate`

The first three stages use GPT-5.6 Sol. Evidence Passport generation and the Human Gate are deterministic application logic, preventing the model from approving itself.

## Scientific boundary

This prototype creates governed research designs. It does not itself establish an empirical or causal result. `discovery_claim_allowed` remains `false` until real-data provenance, construct validation, identification, replication/OOS, economic significance, welfare validation, and final human scientific approval are completed.

## IP

The repository's ECONOVA-S™ Research and Non-Commercial License applies. Commercial use requires prior written permission.

Copyright © 2026 Saeid Homayoun. ORCID: 0000-0002-2536-0446.
