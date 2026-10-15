# Simple CAM Pilot — Hugging Face + Google Drive + GitHub

This is a **synthetic smoke test**, not an execution of Jev, OpenJev, or a Hugging Face model. The probability values in `example_cam_predictions.csv` are invented solely to demonstrate the file format. Do not cite its metrics as research results.

## Verified connected resources (2026-10-15)
- Hugging Face account: https://huggingface.co/SADHON (authenticated; no model deployment asserted).
- Google Drive CAM validation sheet: https://docs.google.com/spreadsheets/d/1EBHt3Un6mL3_8GPP4C9w-KqNjdaGXs-EwMHATDVi2gY/edit
- Google Drive Risk–CAM results sheet: https://docs.google.com/spreadsheets/d/1q7IFjPfUT5Wx1tDU3pz_VYHpa941yqCrKiDD3xlrB-Y/edit
- Third-party candidates: https://github.com/ZimmyGao/openjev-rlcd ; https://github.com/Heman10x-NGU/openJev-verdict-2.0 ; https://github.com/muthuishere/openjevx

## Run immediately, without installation
From the repository root:

```bash
python research/jev-ai-audit/benchmark.py --variants
python research/jev-ai-audit/benchmark.py --input research/jev-ai-audit/example_cam_predictions.csv
```

Output is descriptive grouped Brier, precision and recall. The two rows per variant are too few for inference.

## Optional Google Colab + Drive workflow
In an authenticated Colab notebook (not GitHub Actions):

```python
from google.colab import drive
drive.mount('/content/drive')
# Choose an authorized local export from your canonical Drive workbook.
# Never write raw research datasets, tokens, or client information into public GitHub.
# Export only the approved columns to a private CSV for local model scoring.
```

For a *real* run, first inspect the source sheet schema and document a mapping from actual observed outcome and risk-domain labels. A CAM disclosure is NOT itself evidence of effectiveness; absence of ICFR material weakness disclosure is NOT proof of effectiveness. Keep effective/ineffective/unknown and industry/domain taxonomy intact. Use ASC 606 for US revenue.

Next obtain authorized model predictions from the chosen Hugging Face or OpenJev implementation; map to `variant,industry,domain,icfr_status,label,p_event` and run the same benchmark script. Do not label a model as executed merely because its name appears in the CSV. Keep the full firm/year/split/provenance ledger in the private canonical Drive project.

## Controls
- No API keys in GitHub.
- No copies of actual Google Drive data in this public repository.
- No model installed, inference performed, or real CAM data scored in this example.
- For publication: chronological held-out split, calibration, PR-AUC, bootstrap intervals, pre-registered hypothesis, cost and leakage checks.
