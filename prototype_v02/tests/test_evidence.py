from econova.evidence import load_registry, retrieve_evidence

def test_registry_and_retrieval():
    r = load_registry()
    assert len(r) >= 5
    x = retrieve_evidence("green innovation ESG patents", r, 3)
    assert any("green" in " ".join(c["domains"]).lower() for c in x)
