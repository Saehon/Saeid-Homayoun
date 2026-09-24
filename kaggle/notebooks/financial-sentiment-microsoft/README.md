# Finance sentiment model with a Microsoft accounting example

This private Kaggle script trains a CPU-only TF-IDF + logistic regression
classifier for **negative / neutral / positive** financial text. It uses the
train, validation and test CSVs from the GitHub reference repository at a pinned
commit. The source files are fetched during the Kaggle run; they are not copied
into this repository or republished as a Kaggle dataset. The reference study
and dataset were created by the authors credited in that repository, not by
this notebook's author:

https://github.com/Saehon/Financial-Sentiment-Analysis-and-Classification-Deep-Learning-Models

The script verifies SHA-256 checksums, excludes exact duplicate and
contradictory text labels from training, and excludes text overlap across
train, validation and test. It compares the classifier with a majority-class
baseline, saves held-out test metrics and a confusion matrix, and writes the
trained model to `/kaggle/working/financial_sentiment_model.joblib`.

It then attaches the existing private Kaggle dataset
`sadhon/microsoft-accounting-demo-sec-10k`, checks its CSV against the
canonical GitHub checksum, and constructs **two illustrative sentences** about
Microsoft's year-over-year revenue changes. These sentences are generated
from GAAP numbers, not quoted from the 10-K, and are not test observations.
Predicted sentiment is a text-classification demonstration, not an audit
conclusion or a statement about financial performance.

**Limit:** The reference CSVs lack reliable filing dates and company identifiers
for a chronological or company-held-out assessment. Test metrics therefore do
not establish performance on new companies, SEC filings, CAMs, KAMs, or later
reporting periods. Some source sentences carry contradictory labels; their
exclusion and the resulting sample counts are recorded in `model_metrics.json`.

## Reproduce locally

From a workspace with both repositories checked out:

```bash
FINANCE_DATA_DIR=/path/to/Financial-Sentiment-Analysis-and-Classification-Deep-Learning-Models/Datasets \
MICROSOFT_CSV=/path/to/Saeid-Homayoun/open-data/microsoft-demo-001/microsoft_financials.csv \
MODEL_OUTPUT_DIR=/tmp/finance-sentiment-output \
python kaggle/notebooks/financial-sentiment-microsoft/financial_sentiment_microsoft.py
```

`pandas`, `scikit-learn` and `joblib` are required. The notebook stays private
while its Kaggle execution and source permissions are reviewed.
