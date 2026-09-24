# SEC EDGAR Microsoft 10-K — Simple Kaggle Test

This is the first end-to-end test of:

**ChatGPT → GitHub → GitHub Actions → Kaggle**

It is based on the Microsoft example already present in the user's `Saehon/sec-edgar-downloader` repository:

```python
dl.get("10-K", "MSFT", limit=1)
```

For this first integration test, the Kaggle script uses a verified SEC EDGAR metadata snapshot for Microsoft's Form 10-K for the fiscal year ended June 30, 2026. It runs offline and writes:

`/kaggle/working/microsoft_sec_edgar_10k_summary.csv`

The notebook is private by default while the pipeline is being validated.
