"""Small, auditable free-cash-flow and economic-profit helpers.

Research utility, not valuation or investment advice. Units must be consistent.
"""
from __future__ import annotations

from math import isfinite


def _real(name: str, value: float) -> float:
    number = float(value)
    if not isfinite(number):
        raise ValueError(f"{name} must be finite")
    return number


def fcff(
    ebit: float,
    effective_tax_rate: float,
    depreciation_amortization: float,
    capital_expenditure: float,
    change_in_non_cash_nwc: float,
) -> float:
    """FCFF = EBIT * (1 - tax) + D&A - total capex - change in noncash NWC.

    The capex parameter is TOTAL company capex, *not* AI-specific capex.
    """
    e = _real("ebit", ebit)
    tax = _real("effective_tax_rate", effective_tax_rate)
    if not 0 <= tax <= 1:
        raise ValueError("effective_tax_rate must be in [0, 1]")
    return (
        e * (1 - tax)
        + _real("depreciation_amortization", depreciation_amortization)
        - _real("capital_expenditure", capital_expenditure)
        - _real("change_in_non_cash_nwc", change_in_non_cash_nwc)
    )


def return_on_invested_capital(nopat: float, beginning_invested_capital: float) -> float:
    """ROIC = after-tax operating income / beginning invested capital."""
    capital = _real("beginning_invested_capital", beginning_invested_capital)
    if capital <= 0:
        raise ValueError("beginning_invested_capital must be positive")
    return _real("nopat", nopat) / capital


def economic_profit(
    roic: float, wacc: float, beginning_invested_capital: float
) -> float:
    """Residual/economic profit: (ROIC - WACC) * beginning invested capital."""
    capital = _real("beginning_invested_capital", beginning_invested_capital)
    if capital <= 0:
        raise ValueError("beginning_invested_capital must be positive")
    return (_real("roic", roic) - _real("wacc", wacc)) * capital
