# NAAIL OpenLab — Scientific Core Benchmarks

Canonical hierarchy:

```
NAAIL OpenLab
└── Scientific Core
    └── Benchmarks
        └── Customer-Zero
            └── Microsoft FY2026
```

## Microsoft FY2026 Customer-Zero

The executable benchmark currently remains at:
`benchmarks/customer-zero-msft-2026/`

This index is the canonical architectural mapping. Existing files are intentionally not moved or deleted, preserving history and links.

### Scientific role
- reproducible SEC/XBRL evidence benchmark;
- multi-engine extraction comparison;
- Evidence Passport;
- falsification/reviewer gate;
- human approval;
- reusable evaluation infrastructure for downstream NAAIL projects.

### Separation rule
Customer-Zero is infrastructure under NAAIL Scientific Core. It is not merged into LEMON/ICFR, CAM/KAM, IFRS Value Intelligence, or PCAOB Embedded Inspection. Those projects may consume validated benchmark components independently.

### Promotion gate
Only reproducible PASS artifacts with compatible licensing may be promoted/cross-synced to Hugging Face or Kaggle.
