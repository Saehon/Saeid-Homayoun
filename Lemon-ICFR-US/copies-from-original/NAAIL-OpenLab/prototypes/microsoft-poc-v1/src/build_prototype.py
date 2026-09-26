"""NAAIL Microsoft POC V1: reproducible calculations from public seed facts.
This public script intentionally implements only non-sensitive prototype arithmetic.
"""
from __future__ import annotations
import json

FY2026 = {
    "revenue": 331_839.0,
    "operating_income": 155_237.0,
    "net_income": 133_749.0,
    "total_assets": 758_376.0,
    "total_liabilities": 315_989.0,
    "equity": 442_387.0,
    "current_assets": 207_710.0,
    "current_liabilities": 168_825.0,
    "operating_cash_flow": 182_935.0,
    "capex": 115_948.0,
    "rd": 35_562.0,
}

def financial_features(x=FY2026):
    fcf = x["operating_cash_flow"] - x["capex"]
    return {
        "operating_margin": x["operating_income"]/x["revenue"],
        "net_margin": x["net_income"]/x["revenue"],
        "current_ratio": x["current_assets"]/x["current_liabilities"],
        "liabilities_to_assets": x["total_liabilities"]/x["total_assets"],
        "rd_intensity": x["rd"]/x["revenue"],
        "free_cash_flow": fcf,
        "fcf_margin": fcf/x["revenue"],
    }

def tdabc_example(hourly_human_cost=85.0, practical_minutes_per_hour=48.0, required_minutes=27.0):
    capacity_cost_rate = hourly_human_cost/practical_minutes_per_hour
    return {
        "capacity_cost_rate_per_minute": capacity_cost_rate,
        "required_minutes": required_minutes,
        "human_activity_cost": capacity_cost_rate*required_minutes,
    }

def ai_task_cost(input_tokens, output_tokens, input_per_m, output_per_m):
    return input_tokens/1_000_000*input_per_m + output_tokens/1_000_000*output_per_m

if __name__ == "__main__":
    print(json.dumps({"financial_features": financial_features(), "tdabc": tdabc_example()}, indent=2))
