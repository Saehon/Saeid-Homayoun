# GKM2017 Public Reconstruction Contract

## Scientific identity
Ge, Weili; Koester, Allison; McVay, Sarah (2017), "Benefits and costs of Sarbanes-Oxley Section 404(b) exemption: Evidence from small firms’ internal control disclosures", Journal of Accounting and Economics 63(2–3), 358–384. DOI: 10.1016/j.jacceco.2017.01.001.

## Role
Track A exact-literature executable-score candidate. Track B SEC-native reconstruction remains a separate gate. Never label a proxy implementation as exact replication.

## Published Equation [2] contract
Raw = 0.301*AggLoss + 0.940*Restate + 0.072*Seg - 0.344*Age - 0.714*BankInd - 0.361*Size - 1.088*Cash - 1.285*InstOwn + 3.161*Prior404302

Predicted_Ineffective = exp(Raw)/(1+exp(Raw))

No intercept is added because Equation [2] as published contains no intercept term. Reported suspected-misreporter cutoff: 0.217.

## Variable reconstruction gate

| Variable | Literature definition dependency | Public reconstruction class | Exact-equivalence gate |
|---|---|---|---|
| AggLoss | historical aggregate loss construction | SEC/XBRL candidate | HOLD until exact lookback, numerator/denominator and winsorization definition are reproduced |
| Restate | historical restatement indicator | SEC filing/restatement evidence candidate | HOLD until paper event definition and period alignment are reproduced |
| Seg | segment count | SEC segment disclosures candidate | HOLD until count rule matches paper/Compustat segment construction |
| Age | log years listed in Compustat | public listing-history proxy possible | FAIL_EXACT_PUBLIC until Compustat-start definition can be definition-equivalently reconstructed |
| BankInd | banking-industry indicator | SIC/industry mapping candidate | PASS_CANDIDATE subject to exact industry-code rule |
| Size | paper-specific firm-size construction | SEC/XBRL/market data candidate | HOLD until exact measure/date is locked |
| Cash | cash scaled per paper definition | SEC/XBRL candidate | PASS_CANDIDATE subject to exact denominator and winsorization |
| InstOwn | institutional ownership | public 13F reconstruction possible | HOLD: aggregation, manager universe, report date and denominator must match |
| Prior404302 | prior ineffective-control disclosure history | SEC 10-K/302/404 evidence candidate | PASS_CANDIDATE subject to exact lookback and coding rule |

## Population preprocessing
The paper winsorizes continuous variables at fiscal-year 1st/99th percentiles. Therefore an exact score for a single firm-year is not definition-complete without the applicable fiscal-year reference population and exact sample filters. A single-company SEC POC may execute only if it either (a) reconstructs the required reference distribution or (b) is explicitly labeled SEC-native/proxy and not exact replication.

## Gate decision
TRACK_A_EXACT_LITERATURE: PASS_CANDIDATE
TRACK_B_SEC_NATIVE: HOLD
M1_FREEZE: NO

## Required next evidence
1. Lock exact Table 3 Panel C definitions for AggLoss, Seg, Size, Cash, InstOwn and Prior404302 from the primary PDF.
2. Specify fiscal-year winsorization population and sample filters.
3. Test SEC/public definition-equivalence for each variable.
4. If any indispensable variable remains non-equivalent, freeze GKM2017 only as Track A and build Track B as a separately labeled public-data model.
