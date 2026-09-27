from ack2007 import predict, REQUIRED

FIXTURES = {
"ZERO": {k:0.0 for k in REQUIRED},
"AUDITOR_RESIGN_ONLY": {**{k:0.0 for k in REQUIRED}, "AUDITOR_RESIGN":1.0},
"SCHEMA_VALID": {
"SEGMENTS":2,"FOREIGN_SALES":1,"M&A":0,"RESTRUCTURE":0,"RGROWTH":5,
"INVENTORY":0.10,"SIZE":8,"%LOSS":0.33,"RZSCORE":4,"AUDITOR_RESIGN":0,
"AUDITOR":1,"RESTATEMENT":0,"INST_CON":0.20,"LITIGATION":0}
}
for name,x in FIXTURES.items():
    y=predict(x)
    print(name, f"z={y.linear_predictor:.12f}", f"p={y.probability:.12f}")
