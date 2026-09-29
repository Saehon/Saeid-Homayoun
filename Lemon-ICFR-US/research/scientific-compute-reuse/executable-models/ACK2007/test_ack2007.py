import math
import pytest
from ack2007 import COEFFICIENTS, INTERCEPT, REQUIRED, linear_predictor, logistic, predict

ZERO = {k: 0.0 for k in REQUIRED}

def test_coefficient_count_and_intercept():
    assert len(COEFFICIENTS) == 14
    assert INTERCEPT == -3.752

def test_zero_vector_equals_intercept():
    assert linear_predictor(ZERO) == pytest.approx(INTERCEPT)

def test_zero_vector_probability_is_mathematical_execution_only():
    p = predict(ZERO).probability
    assert p == pytest.approx(1 / (1 + math.exp(3.752)))
    assert 0 < p < 1

def test_single_predictor_contribution():
    x = dict(ZERO); x["AUDITOR_RESIGN"] = 1
    assert linear_predictor(x) == pytest.approx(INTERCEPT + 1.506)

def test_missing_variable_rejected():
    x = dict(ZERO); x.pop("RZSCORE")
    with pytest.raises(ValueError): predict(x)

def test_unknown_variable_rejected():
    x = dict(ZERO); x["LEAKAGE"] = 1
    with pytest.raises(ValueError): predict(x)

def test_nonfinite_rejected():
    x = dict(ZERO); x["SIZE"] = float("nan")
    with pytest.raises(ValueError): predict(x)

@pytest.mark.parametrize("z", [-1000,-10,0,10,1000])
def test_logistic_stable_and_bounded(z):
    p = logistic(z)
    assert 0 <= p <= 1


EXPECTED_COEFFICIENT_PIN = {
    "SEGMENTS": 0.078,
    "FOREIGN_SALES": 0.466,
    "M&A": 0.177,
    "RESTRUCTURE": 0.296,
    "RGROWTH": 0.064,
    "INVENTORY": 0.785,
    "SIZE": -0.048,
    "%LOSS": 0.192,
    "RZSCORE": -0.016,
    "AUDITOR_RESIGN": 1.506,
    "AUDITOR": 0.965,
    "RESTATEMENT": 0.470,
    "INST_CON": 0.085,
    "LITIGATION": 0.263,
}

def test_complete_coefficient_vector_is_regression_pinned_without_fixture_mutation():
    assert COEFFICIENTS == EXPECTED_COEFFICIENT_PIN
    assert tuple(COEFFICIENTS) == tuple(EXPECTED_COEFFICIENT_PIN)

@pytest.mark.parametrize("name,beta", EXPECTED_COEFFICIENT_PIN.items())
def test_each_coefficient_contributes_exactly_once(name, beta):
    x = dict(ZERO)
    x[name] = 1.0
    assert linear_predictor(x) == pytest.approx(INTERCEPT + beta)
