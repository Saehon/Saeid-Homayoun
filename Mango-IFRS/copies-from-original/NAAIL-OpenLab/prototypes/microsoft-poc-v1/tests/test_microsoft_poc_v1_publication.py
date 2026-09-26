import csv, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def test_two_core_constitution():
    twin=json.loads((ROOT/'microsoft_digital_twin.json').read_text(encoding='utf-8'))
    assert twin['architecture']['permanent_cores']==['Stable Knowledge Core™','Replaceable Technology Core™']
    assert twin['architecture']['third_core'] is False

def test_human_gate_boundaries():
    twin=json.loads((ROOT/'microsoft_digital_twin.json').read_text(encoding='utf-8'))
    assert twin['human_gate']['production_approval']=='NO'
    assert twin['human_gate']['scientific_validation']=='PENDING_INDEPENDENT_REPLICATION'

def test_external_benchmark_is_not_professional_validation():
    rows=list(csv.DictReader(open(ROOT/'ai_cost_benchmark.csv',encoding='utf-8')))
    assert rows
    assert all(r['cost_metric_status']=='EXTERNAL_COST_PER_SUCCESSFUL_TASK' for r in rows)
