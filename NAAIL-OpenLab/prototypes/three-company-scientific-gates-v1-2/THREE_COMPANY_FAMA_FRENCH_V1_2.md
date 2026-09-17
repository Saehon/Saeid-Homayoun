# NAAIL Prototype V1.2 — Three-Company Fama–French Scientific Gate

**Run date:** 2026-09-17  
**Status:** `EXECUTED`  
**Companies:** Microsoft (`MSFT`), Walmart (`WMT`), JPMorgan Chase (`JPM`)  
**Primary window:** 2024-01 through 2026-07 (31 monthly observations per company)  
**Models:** CAPM, Fama–French 3-factor, Fama–French 5-factor  
**Inference:** OLS coefficients with HC3 heteroskedasticity-robust standard errors

## Data and provenance

Company prices are month-end IEX close observations retrieved through the connected Alpaca market-data interface. Walmart's 3-for-1 forward split with ex-date 2024-02-26 is explicitly adjusted before return construction. Cash-dividend announcements are retained for a dividend-inclusive monthly holding-return approximation used as a sensitivity test.

Factor values are from the Kenneth R. French U.S. Fama/French 5 Factors (2x3) monthly series. The official Data Library reports monthly coverage through July 2026. The frozen values used here were cross-checked against a July-2026 (`202607`) CRSP-snapshot mirror carrying the source-file hash metadata.

## Main price-return results

| Ticker | Model | N | Monthly alpha | HC3 p(alpha) | Mkt beta | HC3 p(Mkt) | R² | Adj. R² |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| MSFT | CAPM | 31 | -0.0089 | 0.5462 | 1.2425 | 0.0000 | 0.2786 | 0.2538 |
| MSFT | FF3 | 31 | -0.0075 | 0.5761 | 1.1237 | 0.0000 | 0.4596 | 0.3995 |
| MSFT | FF5 | 31 | -0.0040 | 0.7955 | 1.3488 | 0.0001 | 0.6736 | 0.6083 |
| WMT | CAPM | 31 | 0.0147 | 0.1654 | 0.6306 | 0.0535 | 0.1424 | 0.1128 |
| WMT | FF3 | 31 | 0.0145 | 0.2522 | 0.6433 | 0.0958 | 0.1447 | 0.0497 |
| WMT | FF5 | 31 | 0.0150 | 0.3112 | 0.7171 | 0.0817 | 0.2275 | 0.0730 |
| JPM | CAPM | 31 | 0.0108 | 0.1912 | 0.8582 | 0.0001 | 0.3176 | 0.2941 |
| JPM | FF3 | 31 | 0.0068 | 0.4457 | 1.0227 | 0.0001 | 0.4036 | 0.3373 |
| JPM | FF5 | 31 | 0.0075 | 0.5074 | 1.0583 | 0.0001 | 0.4141 | 0.2970 |

### FF5 factor coefficients, 31-month primary window

| Ticker | Alpha | p(alpha) | Mkt-RF | p(Mkt) | SMB | HML | RMW | CMA | R² |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| MSFT | -0.0040 | 0.7955 | 1.3488 | 0.0001 | -0.4821 | -0.9863 | 1.2904 | -0.1738 | 0.6736 |
| WMT | 0.0150 | 0.3112 | 0.7171 | 0.0817 | 0.1331 | 0.0764 | 0.5664 | -0.4266 | 0.2275 |
| JPM | 0.0075 | 0.5074 | 1.0583 | 0.0001 | 0.1004 | 0.4652 | 0.1712 | 0.0572 | 0.4141 |

## Robustness and falsification checks

1. **Walmart stock split correction.** Using raw, unadjusted closes would imply a February 2024 return of about **-64.53%**. Applying the verified 3-for-1 split yields about **+6.41%**. The unadjusted specification is rejected as mechanically invalid.
2. **Dividend-inclusive sensitivity.** Adding declared cash dividends to monthly holding returns produces only small changes in the 31-month FF5 estimates: the qualitative market-beta pattern and model fit are stable.
3. **Window sensitivity.** A shorter 2025-01 through 2026-07 window (19 observations) is also estimated. Because this leaves few residual degrees of freedom for FF5, it is treated as a sensitivity check, not a preferred specification.
4. **Small-sample warning.** Thirty-one observations remain limited for a five-factor model. Coefficients should not be interpreted as long-run structural exposures.
5. **IEX coverage boundary.** The market-price input is an IEX feed, not consolidated SIP/CRSP security-return data.
6. **Dividend approximation boundary.** The dividend-inclusive monthly series adds cash dividends in the ex-date month and is not a fully reinvested daily total-return index.

## Interpretation boundary

The factor regressions are now genuinely executed, but this is not a causal test and not investment advice. A factor loading is an exposure estimate over the stated sample, not proof of a business mechanism. Statistical significance is not treated as scientific discovery.

## Promotion decision

Step 7 (`Fama–French`) can move from `REGISTERED_NOT_EXECUTED` to **`EXECUTED`** for all three companies within this bounded 31-month research-prototype scope.

Longer-history consolidated-price and exact reinvested-total-return replication remain desirable before any stronger scientific claim.
