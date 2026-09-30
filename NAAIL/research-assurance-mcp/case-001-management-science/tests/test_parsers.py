from src.stata_parser import parse_reghdfe_command, parse_n
from src.sas_parser import parse as parse_sas

def test_stata_spec():
    s=parse_reghdfe_command("reghdfe EADelay Post, a(gvkey sec_filing_limit) cluster(rdq)")
    assert s.dependent_variable=="EADelay"
    assert s.absorb==["gvkey","sec_filing_limit"]
    assert s.cluster=="rdq"

def test_stata_n():
    assert parse_n("Number of obs = 4,821")==4821

def test_sas_warning():
    x=parse_sas("proc means data=work.a;\nWARNING: test warning")
    assert "MEANS" in x["procedures"]
    assert len(x["warnings"])==1
