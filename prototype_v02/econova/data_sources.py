from __future__ import annotations
from io import BytesIO, StringIO
import zipfile
import requests
import pandas as pd

FF5_URL = "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_5_Factors_2x3_CSV.zip"
FF_LIBRARY = "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html"
CLIMATE_TRACE_DATA = "https://climatetrace.org/data"

def fetch_fama_french_5factor(timeout: int = 30) -> pd.DataFrame:
    headers = {"User-Agent": "ECONOVA-S research prototype/0.2"}
    r = requests.get(FF5_URL, timeout=timeout, headers=headers)
    r.raise_for_status()
    with zipfile.ZipFile(BytesIO(r.content)) as z:
        raw = z.read(z.namelist()[0]).decode("utf-8", errors="replace")
    lines = raw.splitlines()
    header_idx = next(i for i,l in enumerate(lines) if "Mkt-RF" in l and "SMB" in l)
    body = []
    for line in lines[header_idx+1:]:
        first = line.split(",")[0].strip()
        if not first.isdigit() or len(first) != 6:
            break
        body.append(line)
    csv = lines[header_idx] + "\n" + "\n".join(body)
    df = pd.read_csv(StringIO(csv))
    df.columns = [c.strip() for c in df.columns]
    df = df.rename(columns={df.columns[0]:"yyyymm"})
    df["date"] = pd.to_datetime(df["yyyymm"].astype(str), format="%Y%m")
    factors = ["Mkt-RF","SMB","HML","RMW","CMA","RF"]
    for c in factors:
        df[c] = pd.to_numeric(df[c], errors="coerce") / 100.0
    return df[["date"] + factors].dropna().reset_index(drop=True)

def climate_trace_instructions() -> dict:
    return {
        "official_data_page": CLIMATE_TRACE_DATA,
        "mode": "upload verified CSV/export",
        "reason": "Schema varies across download packages; explicit mapping is safer than silent guessing.",
        "recommended_fields": ["asset/source identifier","year/date","CO2e emissions","sector","owner/company","country"]
    }
