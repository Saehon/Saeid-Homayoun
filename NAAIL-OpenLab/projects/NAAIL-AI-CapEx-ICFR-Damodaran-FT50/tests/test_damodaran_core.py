"""Synthetic values only: arithmetic unit tests, NOT empirical findings."""
import pytest

from src.damodaran_core import economic_profit, fcff, return_on_invested_capital


def test_fcff_synthetic_example():
    assert fcff(100.0, 0.25, 20.0, 40.0, 10.0) == pytest.approx(45.0)


def test_roic_synthetic_example():
    assert return_on_invested_capital(25.0, 200.0) == pytest.approx(0.125)


def test_economic_profit_synthetic_example():
    assert economic_profit(0.125, 0.08, 200.0) == pytest.approx(9.0)


def test_rejects_invalid_tax_rate():
    with pytest.raises(ValueError, match="tax"):
        fcff(100, 1.25, 10, 25, 0)


def test_rejects_invalid_capital():
    with pytest.raises(ValueError, match="positive"):
        return_on_invested_capital(10, 0)
