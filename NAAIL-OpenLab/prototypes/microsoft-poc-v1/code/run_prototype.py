from sec_xbrl_ingest import validate_frozen_facts
from financial_features import ratio, free_cash_flow_proxy, simple_price_return
from management_accounting import capacity_cost_rate, tdabc_cost

def main():
    validate_frozen_facts()
    op_margin = ratio(155237,331839)
    fcf = free_cash_flow_proxy(182935,115948)
    ret = simple_price_return(492.10,372.92)
    ccr = capacity_cost_rate(85,48)
    print("XBRL frozen validation: PASS")
    print("Operating margin:", round(op_margin,6))
    print("FCF proxy USDm:", fcf)
    print("FY2026 MSFT simple price return:", round(ret,6))
    print("TDABC 12-minute human review:", round(tdabc_cost(ccr,12),4))

if __name__ == "__main__":
    main()
