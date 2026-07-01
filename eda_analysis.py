"""
eda_analysis.py
----------------
Exploratory data analysis + statistical summary generation for the
cleaned Telco churn dataset. Produces a JSON + Markdown summary of key
findings, consumed by the reporting script.

Usage:
    python analysis/eda_analysis.py
"""

import os
import json
import pandas as pd

CLEAN_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "processed", "telco_churn_clean.csv")
OUT_JSON = os.path.join(os.path.dirname(__file__), "..", "reports", "summary_stats.json")


def load_data() -> pd.DataFrame:
    return pd.read_csv(CLEAN_FILE)


def analyze(df: pd.DataFrame) -> dict:
    total = len(df)
    churned = df["is_churned"].sum()
    churn_rate = round(100 * churned / total, 2)

    by_contract = (
        df.groupby("contract")["is_churned"].mean().mul(100).round(2).to_dict()
    )
    by_internet = (
        df.groupby("internet_service")["is_churned"].mean().mul(100).round(2).to_dict()
    )
    by_payment = (
        df.groupby("payment_method")["is_churned"].mean().mul(100).round(2).to_dict()
    )
    by_tenure_group = (
        df.groupby("tenure_group")["is_churned"].mean().mul(100).round(2).to_dict()
    )

    revenue_at_risk = round(df.loc[df.is_churned == 1, "monthly_charges"].sum(), 2)
    clv_lost = round(df.loc[df.is_churned == 1, "clv_estimate"].sum(), 2)
    avg_tenure_churned = round(df.loc[df.is_churned == 1, "tenure"].mean(), 1)
    avg_tenure_retained = round(df.loc[df.is_churned == 0, "tenure"].mean(), 1)

    services_vs_churn = (
        df.groupby("num_services")["is_churned"].mean().mul(100).round(2).to_dict()
    )

    summary = {
        "total_customers": int(total),
        "churned_customers": int(churned),
        "overall_churn_rate_pct": churn_rate,
        "churn_rate_by_contract": by_contract,
        "churn_rate_by_internet_service": by_internet,
        "churn_rate_by_payment_method": by_payment,
        "churn_rate_by_tenure_group": by_tenure_group,
        "churn_rate_by_num_services": services_vs_churn,
        "monthly_revenue_at_risk": revenue_at_risk,
        "estimated_clv_lost": clv_lost,
        "avg_tenure_churned_months": avg_tenure_churned,
        "avg_tenure_retained_months": avg_tenure_retained,
    }
    return summary


def run():
    df = load_data()
    summary = analyze(df)
    os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
    with open(OUT_JSON, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"Saved summary statistics -> {OUT_JSON}")
    print(json.dumps(summary, indent=2))
    return summary


if __name__ == "__main__":
    run()
