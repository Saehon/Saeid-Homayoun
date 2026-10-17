"""Point-in-time PCAOB inspection selector. Facts: official PCAOB public releases."""
import csv
from datetime import date

def select(path, asof):
    with open(path, newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
    eligible = [r for r in rows if date.fromisoformat(r['public_release_date']) <= date.fromisoformat(asof)]
    if not eligible:
        return None
    row = max(eligible, key=lambda r: (int(r['inspection_year']), r['public_release_date']))
    n, d = row['part_ia_audits'], row['audits_reviewed']
    return {'inspection_year': int(row['inspection_year']),
            'release': row['release_number'],
            'public_release_date': row['public_release_date'],
            'selected_sample_part_ia_rate': int(n)/int(d) if n and d else None}

if __name__ == '__main__':
    print(select('inspection_vintage_events.csv', '2024-12-06'))
