from classifier import classify_noncompliance

assert classify_noncompliance("Internal Control—Integrated Framework (1992)") == 1
assert classify_noncompliance("Internal Control—Integrated Framework (2013)") == 0
assert classify_noncompliance("Internal Control—Integrated Framework") is None
assert classify_noncompliance("Integrated Framework (1992) and Integrated Framework (2013)") is None
assert classify_noncompliance("") is None
