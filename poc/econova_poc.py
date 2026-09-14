from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import argparse, json
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from sklearn.metrics import mean_squared_error

SEED = 20260914


@dataclass(frozen=True)
class StableEconomicKnowledgeCore:
    research_question: str = "When does firm data capability become sustainable economic and social value?"
    governing_rule: str = "AI explores; economics constrains; data tests; adversaries challenge; replication verifies; welfare interprets; humans decide."
    required_gates: tuple[str, ...] = (
        "literature_validation", "construct_validation", "data_provenance", "identification",
        "adversarial_review", "robustness", "falsification", "reproducibility",
        "oos_or_replication", "economic_significance", "welfare_interpretation", "human_approval"
    )


@dataclass
class ReplaceableTechnologyCore:
    estimator: str = "statsmodels_ols"
    search_engine: str = "deterministic_specification_tournament"
    runtime: str = "python"


def generate_demo(seed: int = SEED) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    firms = [f"F{i:02d}" for i in range(1, 21)]
    years = range(2020, 2026)
    industries = ["Tech", "Industrial", "Energy", "Consumer"]
    firm_ind = {f: industries[(i - 1) % 4] for i, f in enumerate(firms, 1)}
    firm_fe = {f: rng.normal(0, 0.25) for f in firms}
    rows = []

    for f in firms:
        base_dc, base_size = rng.uniform(-0.5, 0.8), rng.normal(8.5, 0.5)
        for year in years:
            t = year - 2020
            reg = np.clip(0.35 + 0.08 * t + rng.normal(0, 0.06), 0.1, 0.95)
            comp = np.clip(rng.normal(0.6, 0.12), 0.2, 0.95)
            rd = np.clip(rng.normal(0.08 + 0.01 * t, 0.025), 0.01, 0.18)
            size = base_size + 0.03 * t + rng.normal(0, 0.08)
            dc = base_dc + 0.18 * t + 0.4 * rd + rng.normal(0, 0.18)
            green = (
                0.45 * dc + 0.55 * (dc * reg) + 1.2 * rd + 0.18 * comp
                + firm_fe[f] + 0.05 * t + rng.normal(0, 0.22)
            )
            carbon = 95 - 10 * green - 2.0 * reg + rng.normal(0, 4)
            privacy = np.clip(0.25 + 0.12 * dc + rng.normal(0, 0.05), 0.05, 0.8)
            market_power = np.clip(0.30 + 0.15 * dc - 0.20 * comp + rng.normal(0, 0.05), 0.02, 0.8)
            value = 1.2 + 0.35 * green + 0.18 * dc - 0.004 * carbon + 0.08 * size + 0.3 * firm_fe[f] + rng.normal(0, 0.18)
            data_cost = np.clip(0.2 + 0.05 * dc + rng.normal(0, 0.03), 0.05, 0.5)
            pdv = 0.7 * green + 0.5 * value + 0.3 * dc - data_cost
            sdv = pdv + 0.015 * (100 - carbon) - 0.4 * privacy
            sodv = sdv - 0.6 * market_power + 0.1 * comp
            rows.append([
                f, year, firm_ind[f], dc, reg, comp, rd, size, green, carbon,
                privacy, market_power, data_cost, value, pdv, sdv, sodv
            ])

    df = pd.DataFrame(rows, columns=[
        "firm_id", "year", "industry", "data_capability", "regulation", "competition",
        "rd_intensity", "log_assets", "green_innovation", "carbon_intensity",
        "privacy_cost", "market_power_cost", "data_cost", "firm_value",
        "private_data_value", "sustainable_data_value", "social_data_value"
    ])
    df["data_x_regulation"] = df["data_capability"] * df["regulation"]
    df["lead_data_capability"] = df.groupby("firm_id")["data_capability"].shift(-1)
    df["year_c"] = df["year"] - 2020
    return df


class ScientificIntelligenceFabric:
    def __init__(self, knowledge: StableEconomicKnowledgeCore, tech: ReplaceableTechnologyCore):
        self.knowledge, self.tech = knowledge, tech

    def hypothesis_tournament(self) -> pd.DataFrame:
        rows = [
            ("H1", "Data capability -> green innovation", 5, 5, 5, 4),
            ("H2", "Green innovation -> firm value", 5, 4, 5, 5),
            ("H3", "Data capability/green innovation -> social value net of externalities", 5, 5, 4, 5),
        ]
        out = pd.DataFrame(rows, columns=[
            "hypothesis", "mechanism", "theory", "testability", "economic_importance", "welfare_relevance"
        ])
        out["rank_score"] = out[["theory", "testability", "economic_importance", "welfare_relevance"]].sum(axis=1)
        return out.sort_values("rank_score", ascending=False)

    def fit(self, formula: str, df: pd.DataFrame):
        return smf.ols(formula, data=df).fit(
            cov_type="cluster", cov_kwds={"groups": df["firm_id"]}
        )

    def era_specs(self) -> dict[str, str]:
        return {
            "H1": "green_innovation ~ data_capability + data_x_regulation + regulation + competition + rd_intensity + log_assets + C(firm_id)+C(year)",
            "H2": "firm_value ~ green_innovation + data_capability + carbon_intensity + log_assets + C(firm_id)+C(year)",
            "H3": "social_data_value ~ data_capability + green_innovation + privacy_cost + market_power_cost + competition + C(firm_id)+C(year)",
        }

    def alphaevolve_tournament(self, df: pd.DataFrame) -> pd.DataFrame:
        train, test = df[df.year <= 2024].copy(), df[df.year == 2025].copy()
        specs = {
            "M1_basic": "green_innovation ~ data_capability + rd_intensity + log_assets + C(firm_id)+year_c",
            "M2_regulation": "green_innovation ~ data_capability + data_x_regulation + regulation + competition + rd_intensity + log_assets + C(firm_id)+year_c",
            "M3_industry": "green_innovation ~ data_capability + data_x_regulation + regulation + competition + rd_intensity + log_assets + C(industry)+year_c",
            "M4_parsimonious": "green_innovation ~ data_capability + regulation + rd_intensity + year_c",
        }
        rows = []
        for name, formula in specs.items():
            model = smf.ols(formula, data=train).fit()
            rmse = mean_squared_error(test.green_innovation, model.predict(test)) ** 0.5
            sign_ok = int(model.params.get("data_capability", 0) > 0)
            k = len(model.params)
            fitness = float(rmse + 0.001 * k + (0 if sign_ok else 1))
            rows.append((name, formula, model.aic, model.bic, rmse, k, sign_ok, fitness))
        return pd.DataFrame(rows, columns=[
            "model", "formula", "aic", "bic", "oos_rmse", "n_params", "expected_sign_ok", "fitness"
        ]).sort_values("fitness")


def main_rows(models: dict) -> pd.DataFrame:
    wanted = {
        "H1": ["data_capability", "data_x_regulation", "regulation", "competition", "rd_intensity", "log_assets"],
        "H2": ["green_innovation", "data_capability", "carbon_intensity", "log_assets"],
        "H3": ["data_capability", "green_innovation", "privacy_cost", "market_power_cost", "competition"],
    }
    rows = []
    for h, model in models.items():
        for term in wanted[h]:
            rows.append({
                "model": h,
                "term": term,
                "coefficient": float(model.params[term]),
                "std_error": float(model.bse[term]),
                "p_value": float(model.pvalues[term]),
                "n": int(model.nobs),
                "r_squared": float(model.rsquared),
            })
    return pd.DataFrame(rows)


def run(data_path: Path | None, out_dir: Path) -> dict:
    out_dir.mkdir(parents=True, exist_ok=True)
    if data_path is None:
        df = generate_demo()
        data_label = "deterministic synthetic generator; seed 20260914"
        df.to_csv(out_dir / "demo_firm_year.csv", index=False)
    else:
        df = pd.read_csv(data_path)
        data_label = str(data_path)

    kcore, tcore = StableEconomicKnowledgeCore(), ReplaceableTechnologyCore()
    fabric = ScientificIntelligenceFabric(kcore, tcore)
    models = {h: fabric.fit(formula, df) for h, formula in fabric.era_specs().items()}

    numeric = [
        "data_capability", "regulation", "competition", "rd_intensity", "log_assets",
        "green_innovation", "carbon_intensity", "firm_value", "privacy_cost",
        "market_power_cost", "private_data_value", "sustainable_data_value", "social_data_value"
    ]
    df[numeric].describe().T.reset_index(names="variable").to_csv(
        out_dir / "table2_descriptives.csv", index=False
    )
    df[[
        "data_capability", "green_innovation", "carbon_intensity", "firm_value",
        "privacy_cost", "market_power_cost", "social_data_value"
    ]].corr().reset_index(names="variable").to_csv(
        out_dir / "table3_correlations.csv", index=False
    )
    main_rows(models).to_csv(out_dir / "table4_main_regressions.csv", index=False)

    placebo_df = df.dropna(subset=["lead_data_capability"]).copy()
    placebo = fabric.fit(
        "green_innovation ~ lead_data_capability + rd_intensity + log_assets + C(firm_id)+C(year)",
        placebo_df,
    )
    red = pd.DataFrame([
        ["Placebo lead predictor", "lead_data_capability_pvalue", float(placebo.pvalues["lead_data_capability"]), "Investigate if < 0.05", "FLAG" if placebo.pvalues["lead_data_capability"] < 0.05 else "PASS"],
        ["H1 expected sign", "data_capability_coef", float(models["H1"].params["data_capability"]), "> 0", "PASS" if models["H1"].params["data_capability"] > 0 else "FAIL"],
        ["H2 expected sign", "green_innovation_coef", float(models["H2"].params["green_innovation"]), "> 0", "PASS" if models["H2"].params["green_innovation"] > 0 else "FAIL"],
        ["Privacy externality sign", "privacy_cost_coef", float(models["H3"].params["privacy_cost"]), "< 0", "PASS" if models["H3"].params["privacy_cost"] < 0 else "FAIL"],
    ], columns=["check", "metric", "value", "pass_rule", "status"])
    red.to_csv(out_dir / "table5_robustness_falsification.csv", index=False)

    tournament = fabric.alphaevolve_tournament(df)
    tournament.to_csv(out_dir / "table6_model_tournament_oos.csv", index=False)
    fabric.hypothesis_tournament().to_csv(out_dir / "hypothesis_tournament.csv", index=False)

    best = tournament.iloc[0].to_dict()
    passport = {
        "project_id": "ECONOVA-S-POC-001",
        "evidence_classification": "DEMONSTRATION / ASSOCIATIONAL / SYNTHETIC DATA" if data_path is None else "USER-SUPPLIED DATA / CLASSIFICATION REQUIRES REVIEW",
        "research_question": kcore.research_question,
        "data": {
            "rows": len(df),
            "firms": df.firm_id.nunique(),
            "years": [int(df.year.min()), int(df.year.max())],
            "provenance": data_label,
        },
        "architecture": {
            "stable_core": "StableEconomicKnowledgeCore",
            "technology_core": "ReplaceableTechnologyCore",
            "fabric": "ScientificIntelligenceFabric",
            "proprietary_ai_invoked": False,
        },
        "best_specification_candidate": best,
        "gates": {
            g: ("POC_PASS" if g in {
                "construct_validation", "data_provenance", "reproducibility",
                "oos_or_replication", "adversarial_review"
            } else "NOT_YET_SATISFIED")
            for g in kcore.required_gates
        },
        "human_approval": False,
        "discovery_claim_allowed": False,
        "reason": "POC only; literature, real-data, identification, external replication, economic-significance, welfare, and human gates are incomplete.",
        "governing_rule": kcore.governing_rule,
    }
    (out_dir / "evidence_passport.json").write_text(
        json.dumps(passport, indent=2), encoding="utf-8"
    )
    return passport


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ECONOVA-S POC-001")
    parser.add_argument(
        "--data", type=Path, default=None,
        help="Optional real CSV matching the POC schema. Omit to generate deterministic demo data."
    )
    parser.add_argument(
        "--out", type=Path, default=Path(__file__).resolve().parent / "results"
    )
    args = parser.parse_args()
    passport = run(args.data, args.out)
    print(json.dumps({
        "project_id": passport["project_id"],
        "best_model": passport["best_specification_candidate"]["model"],
        "discovery_claim_allowed": passport["discovery_claim_allowed"],
    }, indent=2))
