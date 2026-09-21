from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PortfolioComponent:
    component: str
    repository: str
    role: str
    status: str


COMPONENTS: tuple[PortfolioComponent, ...] = (
    PortfolioComponent("AAA Finance & Operations Audit", "Saehon/AAA", "Deterministic controls, forensic analytics and audit evidence foundation.", "reference-and-port"),
    PortfolioComponent("IFRS-AI Inspector", "Saehon/IFRS-AI-Inspector", "Standards-aware reporting, evidence provenance and deterministic verification.", "adapter-boundary"),
    PortfolioComponent("AuditData API", "Saehon/AuditData-API", "Audit-data ingestion and normalized evidence access.", "adapter-boundary"),
    PortfolioComponent("Multi-Agent BERT", "Saehon/Google-Antigravity-using-a-multi-agent-BERT-architecture", "Financial-text classification and NLP risk signals.", "adapter-boundary"),
    PortfolioComponent("Financial Sentiment Models", "Saehon/Financial-Sentiment-Analysis-and-Classification-Deep-Learning-Models", "Narrative and disclosure-risk signals.", "adapter-boundary"),
    PortfolioComponent("TimesFM", "Saehon/timesfm", "Forecasting and temporal anomaly baselines.", "adapter-boundary"),
    PortfolioComponent("GAN Lab", "Saehon/ganlab", "Adversarial and synthetic scenario generation.", "adapter-boundary"),
    PortfolioComponent("Synthetic Data", "Saehon/fg-data-synthetic", "Synthetic control and audit populations.", "adapter-boundary"),
    PortfolioComponent("NAAIL OpenLab", "Saehon/Saeid-Homayoun", "Stable Knowledge Core, replaceable Technology Core, evidence governance and Human Gate.", "governance-home"),
)
