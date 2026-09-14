import pandas as pd

from econova.data_sources import companyfacts_to_long, latest_filed_fact, attach_latest_ff_factors


def sample_companyfacts():
    return {
        "cik": 1,
        "entityName": "Example Corp",
        "facts": {
            "us-gaap": {
                "Revenues": {
                    "label": "Revenues",
                    "description": "Revenue",
                    "units": {
                        "USD": [
                            {"val": 100, "start": "2024-01-01", "end": "2024-12-31", "filed": "2025-02-15", "fy": 2024, "fp": "FY", "form": "10-K", "accn": "0001", "frame": "CY2024"},
                            {"val": 120, "start": "2025-01-01", "end": "2025-12-31", "filed": "2026-02-15", "fy": 2025, "fp": "FY", "form": "10-K", "accn": "0002", "frame": "CY2025"},
                        ]
                    },
                }
            }
        },
    }


def test_companyfacts_flatten_and_chronology():
    df = companyfacts_to_long(sample_companyfacts())
    assert len(df) == 2
    assert df["filed"].dtype.kind == "M"
    known = latest_filed_fact(df, tag="Revenues", as_of="2025-12-31", unit="USD")
    assert known is not None
    assert known["value"] == 100


def test_future_filing_is_blocked():
    df = companyfacts_to_long(sample_companyfacts())
    known = latest_filed_fact(df, tag="Revenues", as_of="2025-01-31", unit="USD")
    assert known is None


def test_backward_factor_attachment():
    research = pd.DataFrame({"information_date": pd.to_datetime(["2025-02-20", "2025-03-20"])})
    ff = pd.DataFrame({
        "date": pd.to_datetime(["2025-01-01", "2025-02-01", "2025-03-01"]),
        "Mkt-RF": [0.01, 0.02, 0.03],
        "SMB": [0, 0, 0],
        "HML": [0, 0, 0],
        "RMW": [0, 0, 0],
        "CMA": [0, 0, 0],
        "RF": [0.001, 0.001, 0.001],
        "source": ["FF"] * 3,
    })
    out = attach_latest_ff_factors(research, ff)
    assert out.loc[0, "Mkt-RF"] == 0.02
    assert out.loc[1, "Mkt-RF"] == 0.03
