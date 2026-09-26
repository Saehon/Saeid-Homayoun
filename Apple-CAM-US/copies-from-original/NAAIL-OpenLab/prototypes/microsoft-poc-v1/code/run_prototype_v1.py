from financial_features_v1 import ratio, free_cash_flow_proxy, simple_price_return
from management_accounting_v1 import capacity_cost_rate, tdabc_cost


def main():
    op_margin = ratio(155237,331839)
    fcf = free_cash_flow_proxy(182935,115948)
    ret = simple_price_return(492.10,372.92)
    ccr = capacity_cost_rate(85,48)
    print('Operating margin:', round(op_margin,6))
    print('FCF proxy USDm:', fcf)
    print('FY2026 MSFT simple price return:', round(ret,6))
    print('TDABC 12-minute human review:', round(tdabc_cost(ccr,12),4))

if __name__ == '__main__':
    main()
