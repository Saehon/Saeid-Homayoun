# ANFISpy integration

This folder adds a reproducible entry point for using **ANFISpy** in the Saeid-Homayoun research repository.

## What it provides

ANFISpy is a PyTorch implementation of adaptive neuro-fuzzy inference systems. Its upstream project documents support for regression, classification, recurrent neuro-fuzzy models (RANFIS, GRU-ANFIS, LSTM-ANFIS), CANFIS, fuzzy membership functions, rule inspection, and GPU-enabled PyTorch workflows.

Upstream repository: https://github.com/mZaiam/ANFISpy

## Install locally

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r tools/anfispy/requirements.txt
python tools/anfispy/verify_anfispy.py
```

The upstream package also documents direct installation with:

```bash
pip install anfispy
```

## Intended research uses

- Neuro-fuzzy regression and classification
- ICFR weakness prediction
- Audit-risk classification
- Fraud/anomaly modelling
- CAM/KAM risk modelling
- Time-series experiments with RANFIS / GRU-ANFIS / LSTM-ANFIS
- Interpretable fuzzy-rule analysis

## Licensing and attribution

ANFISpy is an external dependency. Its upstream repository is licensed under **GNU GPL-3.0**. This integration does not copy ANFISpy source code into this repository; it installs the package from its published distribution. Review the upstream license before redistribution or embedding in another deliverable.

For academic use, cite the ANFISpy paper indicated by the upstream authors:

Monteiro, M. Z., & Wasques, V. F. (2026). *ANFISpy: a python package for neuro-fuzzy models*. Neural Computing and Applications.
