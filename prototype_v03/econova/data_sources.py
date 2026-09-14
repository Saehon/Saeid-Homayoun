from __future__ import annotations

from dataclasses import dataclass
from io import BytesIO, StringIO
import time
import zipfile
from typing import Iterable

import pandas as pd
import requests


FF5_URL = "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_5_Factors_2x3_CSV.zip"
FF_LIBRARY = "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html"

DAMODARAN_DATASETS = {
    "wacc": "https://pages.stern.nyu.edu/~adamodar/pc/datasets/wacc.xls",
    "fundgr": "https://pages.stern.nyu.edu/~adamodar/pc/datasets/fundgr.xls",
    "pedata": "https://pages.stern.nyu.edu/~adamodar/pc/datasets/pedata.xls",
    "eva": "https://pages.stern.nyu.edu/~adamodar/pc/datasets/EVA.xls",
}
DAMODARAN_CURRENT = "https://pages.stern.nyu.edu/adamodar/New_Home_Page/datacurrent.html"

SEC_TICKERS = "https://www.sec.gov/files/company_tickers.json"
SEC_COMPANYFACTS = "https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"


def _http_get(url: str, *, user_agent: str, timeout: int = 60) -> requests.Response:
    r = requests.get(
        url,
        headers={
            "User-Agent": user_agent,
            "Accept-Encoding": "gzip, deflate",
            "Host": requests.utils.urlparse(url).netloc,
        },
        timeout=timeout,
    )
    r.raise_for_status()
    return r


def fetch_fama_french_5factor(
    user_agent: str = "ECONOVA-S academic research prototype/0.3"
) -> pd.DataFrame:
    """Fetch official monthly Fama/French 5-factor data and return decimal returns."""
    r = _http_get(FF5_URL, user_agent=user_agent)
    with zipfile.ZipFile(BytesIO(r.content)) as z:
        raw = z.read(z.namelist()[0]).decode("utf-8", errors="replace")

    lines = raw.splitlines()
    header_idx = next(i for i, line in enumerate(lines) if "Mkt-RF" in line and "SMB" in line)
    body: list[str] = []
    for line in lines[header_idx + 1 :]:
        first = line.split(",")[0].strip()
        if not first.isdigit() or len(first) != 6:
            break
        body.append(line)

    csv_text = lines[header_idx] + "\n" + "\n".join(body)
    df = pd.read_csv(StringIO(csv_text))
    df.columns = [c.strip() for c in df.columns]
    df = df.rename(columns={df.columns[0]: "yyyymm"})
    df["date"] = pd.to_datetime(df["yyyymm"].astype(str), format="%Y%m")
    factors = ["Mkt-RF", "SMB", "HML", "RMW", "CMA", "RF"]
    for col in factors:
        df[col] = pd.to_numeric(df[col], errors="coerce") / 100.0
    df["source"] = "Kenneth French Data Library"
    return df[["date"] + factors + ["source"]].dropna().reset_index(drop=True)


def fetch_damodaran(
    dataset: str,
    *,
    user_agent: str = "ECONOVA-S academic research prototype/0.3",
    sheet_name=0,
) -> pd.DataFrame:
    """Fetch one official Damodaran industry spreadsheet.

    The legacy .xls format requires xlrd. The function intentionally returns the source
    table without silently mapping SEC SIC codes to Damodaran industries.
    """
    key = dataset.lower()
    if key not in DAMODARAN_DATASETS:
        raise ValueError(f"Unknown Damodaran dataset: {dataset}. Choose {sorted(DAMODARAN_DATASETS)}")
    url = DAMODARAN_DATASETS[key]
    r = _http_get(url, user_agent=user_agent)
    df = pd.read_excel(BytesIO(r.content), sheet_name=sheet_name)
    df.attrs["source"] = "Aswath Damodaran / NYU Stern"
    df.attrs["source_url"] = url
    df.attrs["dataset_key"] = key
    return df


@dataclass
class SECClient:
    """Small SEC XBRL client with explicit identity and conservative pacing."""

    user_agent: str
    min_interval_seconds: float = 0.12

    def __post_init__(self):
        if not self.user_agent or "@" not in self.user_agent:
            raise ValueError(
                "SECClient requires an identifying User-Agent including a contact email, "
                "for example 'ECONOVA-S research yourname@example.com'."
            )
        self._last_request = 0.0
        self._session = requests.Session()
        self._session.headers.update(
            {
                "User-Agent": self.user_agent,
                "Accept-Encoding": "gzip, deflate",
            }
        )

    def _get_json(self, url: str) -> dict:
        elapsed = time.monotonic() - self._last_request
        if elapsed < self.min_interval_seconds:
            time.sleep(self.min_interval_seconds - elapsed)
        r = self._session.get(url, timeout=60)
        self._last_request = time.monotonic()
        r.raise_for_status()
        return r.json()

    def ticker_map(self) -> pd.DataFrame:
        payload = self._get_json(SEC_TICKERS)
        rows = list(payload.values())
        df = pd.DataFrame(rows)
        df["cik_str"] = pd.to_numeric(df["cik_str"], errors="raise").astype(int)
        df["cik10"] = df["cik_str"].map(lambda x: f"{x:010d}")
        return df.rename(columns={"ticker": "symbol"})

    def companyfacts(self, cik: int | str) -> dict:
        cik10 = f"{int(cik):010d}"
        return self._get_json(SEC_COMPANYFACTS.format(cik=cik10))


def companyfacts_to_long(
    payload: dict,
    *,
    taxonomies: Iterable[str] = ("us-gaap", "dei", "ifrs-full"),
    forms: Iterable[str] = ("10-K", "10-Q", "20-F", "40-F", "6-K"),
) -> pd.DataFrame:
    """Flatten SEC CompanyFacts into a chronology-aware long panel."""
    accepted_taxonomies = set(taxonomies)
    accepted_forms = set(forms)
    facts = payload.get("facts", {})
    rows: list[dict] = []

    for taxonomy, concepts in facts.items():
        if taxonomy not in accepted_taxonomies:
            continue
        for tag, meta in concepts.items():
            label = meta.get("label")
            description = meta.get("description")
            for unit, observations in meta.get("units", {}).items():
                for obs in observations:
                    if obs.get("form") not in accepted_forms:
                        continue
                    rows.append(
                        {
                            "cik": payload.get("cik"),
                            "entity_name": payload.get("entityName"),
                            "taxonomy": taxonomy,
                            "tag": tag,
                            "label": label,
                            "description": description,
                            "unit": unit,
                            "value": obs.get("val"),
                            "start": obs.get("start"),
                            "end": obs.get("end"),
                            "filed": obs.get("filed"),
                            "fy": obs.get("fy"),
                            "fp": obs.get("fp"),
                            "form": obs.get("form"),
                            "accession": obs.get("accn"),
                            "frame": obs.get("frame"),
                        }
                    )

    df = pd.DataFrame(rows)
    if df.empty:
        return df
    for col in ["start", "end", "filed"]:
        df[col] = pd.to_datetime(df[col], errors="coerce")
    return df.sort_values(["filed", "taxonomy", "tag", "end"], kind="stable").reset_index(drop=True)


def latest_filed_fact(
    facts_long: pd.DataFrame,
    *,
    tag: str,
    as_of: str | pd.Timestamp,
    unit: str | None = None,
) -> pd.Series | None:
    """Return the latest filing-known observation as of a specified date.

    This prevents using facts that were filed after the empirical information date.
    """
    if facts_long.empty:
        return None
    t = pd.Timestamp(as_of)
    x = facts_long[(facts_long["tag"] == tag) & (facts_long["filed"] <= t)].copy()
    if unit is not None:
        x = x[x["unit"] == unit]
    if x.empty:
        return None
    x = x.sort_values(["filed", "end"], kind="stable")
    return x.iloc[-1]


def attach_latest_ff_factors(
    research_dates: pd.DataFrame,
    ff: pd.DataFrame,
    *,
    date_col: str = "information_date",
) -> pd.DataFrame:
    """Attach the most recent observable Fama–French month to each information date."""
    left = research_dates.copy()
    left[date_col] = pd.to_datetime(left[date_col])
    right = ff.copy()
    right["date"] = pd.to_datetime(right["date"])
    return pd.merge_asof(
        left.sort_values(date_col),
        right.sort_values("date"),
        left_on=date_col,
        right_on="date",
        direction="backward",
    )
