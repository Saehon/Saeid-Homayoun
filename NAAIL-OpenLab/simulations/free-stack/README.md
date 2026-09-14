# NAAIL OpenLab™ — Free Simulation Stack

**Parent architecture:** NAAIL OpenLab™ — V2026.3 Multi-Agent Digital Twin  
**Applies to:** IFRS Intelligence Agent™, PCAOB Intelligence Agent™, education, reproducibility, and research-safe Digital Twin exercises.

## Goal

Provide a **zero-paid-API core simulation path** that can run with Python, synthetic cases, and public evidence. External models and datasets are optional adapters and never become authoritative evidence merely because they are convenient or free.

## Free core

```text
Synthetic / public evidence
        ↓
Source + license gate
        ↓
Evidence Passport
        ↓
Deterministic Digital Twin simulation
        ↓
Issue classifier + evidence mapper
        ↓
Critic / alternative explanation checks
        ↓
Decision DAG
        ↓
Human Gate
```

The deterministic core uses only the Python standard library. It therefore runs locally or in GitHub Actions without a paid model API.

## Optional free/open adapters

### GitHub
Use GitHub for versioned code, public replication packages, SEC/EDGAR utilities, test fixtures, CI, and exact commit pinning. External repositories remain third-party assets and must pass license/provenance review before code or data are redistributed.

### Hugging Face
Optional local models may enrich retrieval, similarity, classification, or text analytics. The default approved embedding example in the registry is `sentence-transformers/all-MiniLM-L6-v2` (Apache-2.0). Other models require model-card/license review before institutional or redistributed use.

Model output is **analysis**, not IFRS/PCAOB authority.

### Kaggle
Kaggle can be used as an optional source of public datasets or notebooks through `kagglehub` / Kaggle CLI. Every dataset must be registered by handle and pass a dataset-specific license, provenance, and leakage review. Kaggle data must not silently replace the authoritative source when SEC, PCAOB, or another primary source is available.

### Other free sources
- PCAOB public inspection-report datasets and public reports;
- SEC EDGAR/XBRL/CompanyFacts;
- public audit reports and issuer filings;
- public enforcement releases;
- synthetic Client XYZ / Reporting Entity XYZ cases;
- open-source Python/R packages with compatible licenses.

## IFRS simulation rule

The repository does **not** bundle copyrighted IFRS Standards text. IFRS simulations use synthetic facts and user-authorized/publicly redistributable evidence. A human reviewer must link conclusions back to lawfully accessed authoritative IFRS material before professional reliance.

## PCAOB simulation rule

The PCAOB simulation may use public PCAOB inspection datasets, public reports, SEC/public filings, licensed research data, and synthetic cases. It must never imply access to non-public inspection files or confidential firm/client information.

## Run the free core

```bash
python NAAIL-OpenLab/simulations/free-stack/run_simulation.py --agent ifrs --input NAAIL-OpenLab/simulations/free-stack/examples/ifrs_synthetic_case.json
python NAAIL-OpenLab/simulations/free-stack/run_simulation.py --agent pcaob --input NAAIL-OpenLab/simulations/free-stack/examples/pcaob_synthetic_case.json
```

Outputs remain `PENDING_HUMAN_APPROVAL` by design.

## Optional adapters

`optional_adapters.py` provides guarded entry points for Hugging Face embeddings and Kaggle datasets. These imports are optional and are not used by the deterministic CI path.

## Governance

Every simulation inherits:

`provenance → rights/license gate → evidence class → deterministic/model analysis → adversarial check → reproducibility → limitations → Human Gate`

No free source, model, notebook, or repository bypasses the NAAIL Scientific Discovery Contract.