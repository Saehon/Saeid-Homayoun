import json, pathlib
P=pathlib.Path(__file__).parents[1]
x=json.loads((P/"fixtures/microsoft-fy2025-track-b.json").read_text())
N=["AggLoss","Restate","Seg","Age","BankInd","Size","Cash","InstOwn","Prior404302"]
def test_identity(): assert x["issuer"]["cik"]=="0000789019" and x["issuer"]["accession"]=="0000950170-25-100235"
def test_nine_unique(): assert [i["name"] for i in x["candidate_inputs"]]==N and len(set(N))==9
def test_fail_closed(): assert all(i["status"]=="UNAVAILABLE" and i["value"] is None for i in x["candidate_inputs"])
def test_no_proxy_scoring(): assert x["scientific_firewall"]["proxy_may_be_scored_as_exact"] is False
def test_outcome_separation(): assert x["observed_outcome"]["may_enter_predictors"] is False and x["scientific_firewall"]["outcome_may_enter_predictors"] is False
def test_no_pseudo_gkm(): assert x["scientific_firewall"]["apply_gkm_coefficients"] is False and x["scientific_firewall"]["generate_gkm_probability"] is False
def test_temporal_identity(): assert x["issuer"]["fiscal_year_end"]=="2025-06-30" and x["issuer"]["filed"]=="2025-07-30"
def test_deterministic_serialization(): assert json.dumps(x,sort_keys=True,separators=(",",":"))==json.dumps(json.loads(json.dumps(x)),sort_keys=True,separators=(",",":"))
