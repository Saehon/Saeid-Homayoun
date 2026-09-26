def ratio(n, d):
    if d == 0:
        raise ZeroDivisionError('denominator is zero')
    return n / d

def free_cash_flow_proxy(operating_cash_flow, additions_to_ppe):
    return operating_cash_flow - additions_to_ppe

def simple_price_return(first_close, last_close):
    return last_close / first_close - 1
