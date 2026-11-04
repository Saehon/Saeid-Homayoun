"""Minimal import smoke test for the ANFISpy integration."""

from ANFISpy import ANFIS, RANFIS

if __name__ == "__main__":
    print("ANFISpy import OK")
    print("Available core classes:", ANFIS.__name__, RANFIS.__name__)
