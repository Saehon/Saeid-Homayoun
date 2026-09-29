"""LEMON-SCI Executable Scientific Model #1: ACK2007.

Pre-results engineering compiler object. The current coefficient vector is retained
unchanged as a regression pin pending direct verification against the published
JAE 2007 primary results table. This module does not claim scientific coefficient
verification or out-of-sample validity.
"""
from dataclasses import dataclass
from math import exp, isfinite
from typing import Mapping

COEFFICIENTS = {
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
INTERCEPT = -3.752
REQUIRED = tuple(COEFFICIENTS)

@dataclass(frozen=True)
class ACK2007Prediction:
    linear_predictor: float
    probability: float

def _validate(x: Mapping[str, float]) -> None:
    missing = [k for k in REQUIRED if k not in x]
    extra = [k for k in x if k not in COEFFICIENTS]
    if missing:
        raise ValueError(f"Missing ACK2007 variables: {missing}")
    if extra:
        raise ValueError(f"Unknown ACK2007 variables: {extra}")
    for k in REQUIRED:
        v = x[k]
        if not isinstance(v, (int, float)) or not isfinite(float(v)):
            raise ValueError(f"{k} must be a finite numeric value")

def linear_predictor(x: Mapping[str, float]) -> float:
    _validate(x)
    return INTERCEPT + sum(COEFFICIENTS[k] * float(x[k]) for k in REQUIRED)

def logistic(z: float) -> float:
    # Numerically stable sigmoid.
    if z >= 0:
        return 1.0 / (1.0 + exp(-z))
    ez = exp(z)
    return ez / (1.0 + ez)

def predict(x: Mapping[str, float]) -> ACK2007Prediction:
    z = linear_predictor(x)
    return ACK2007Prediction(z, logistic(z))
