"""DARWIN V2.1 scaffold. Does not simulate data or produce empirical results."""
import csv
from pathlib import Path

SAMPLE_FIELDS = ['company_name','cik10','fiscal_year','filing_date','sample_inclusion','source_url','license_status','data_status']
RESULT_FIELDS = ['run_id','analysis_type','model_id','outcome','term','estimate','standard_error','p_value','n_obs','sample_hash','code_commit','verification_status']

def validate_headers(path, required):
    with Path(path).open(newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        missing = set(required) - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f'Missing columns: {sorted(missing)}')
        return sum(1 for _ in reader)

if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('--sample', required=True)
    p.add_argument('--results', required=True)
    a = p.parse_args()
    n = validate_headers(a.sample, SAMPLE_FIELDS)
    m = validate_headers(a.results, RESULT_FIELDS)
    print({'sample_rows':n,'result_rows':m,'status':'SCHEMA_ONLY_NO_EMPIRICAL_RUN'})
