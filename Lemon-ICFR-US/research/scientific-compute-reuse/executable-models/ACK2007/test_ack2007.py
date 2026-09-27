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
