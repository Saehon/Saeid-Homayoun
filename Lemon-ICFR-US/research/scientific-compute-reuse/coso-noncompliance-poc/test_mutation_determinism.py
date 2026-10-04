from classifier import classify_noncompliance

cases = [
    ("Internal Control - Integrated Framework (1992)", 1),
    ("Internal Control - Integrated Framework (2013)", 0),
    ("Internal Control—Integrated Framework", None),
    ("Integrated Framework (1992) and Integrated Framework (2013)", None),
    ("COSO framework", None),
    ("", None),
]
for text, expected in cases:
    a = classify_noncompliance(text)
    b = classify_noncompliance(text)
    assert a == expected
    assert b == expected
    assert a == b
