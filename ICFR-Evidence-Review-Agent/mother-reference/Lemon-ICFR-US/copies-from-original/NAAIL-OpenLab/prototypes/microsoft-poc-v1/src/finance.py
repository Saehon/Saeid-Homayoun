"""Finance utilities for the Microsoft POC."""
def margins(revenue, operating_income, net_income):
    return {"operating_margin": operating_income/revenue, "net_margin": net_income/revenue}

def free_cash_flow(operating_cash_flow, capex):
    return operating_cash_flow-capex

def simple_leverage(total_liabilities, total_assets):
    return total_liabilities/total_assets
