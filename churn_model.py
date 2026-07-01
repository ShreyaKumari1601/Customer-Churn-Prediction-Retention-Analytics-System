"""
churn_model.py
--------------
A simple, interpretable churn prediction model (Logistic Regression)
trained on the cleaned dataset. This is intentionally kept lightweight
since the project's focus is data analytics/BI, not ML production —
but it adds a predictive angle: which customers are most likely to
churn next, and which features drive that risk.

Outputs:
    reports/model_metrics.json      - accuracy, precision, recall, AUC
    reports/feature_importance.png  - top churn drivers (coefficients)

Usage:
    python analysis/churn_model.py
"""

import os
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_auc_score

CLEAN_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "processed", "telco_churn_clean.csv")
REPORTS_DIR = os.path.join(os.path.dirname(__file__), "..", "reports")
CHART_DIR = os.path.join(os.path.dirname(__file__), "..", "visuals", "output")


def prepare_features(df: pd.DataFrame):
    features = [
        "tenure", "monthly_charges", "total_charges", "num_services",
        "senior_citizen", "partner", "dependents", "paperless_billing",
        "contract", "internet_service", "payment_method",
    ]
    X = df[features].copy()
    y = df["is_churned"]

    # Encode categoricals
    X = pd.get_dummies(X, drop_first=True)
    return X, y


def run():
    df = pd.read_csv(CLEAN_FILE)
    X, y = prepare_features(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_test_s = scaler.transform(X_test)

    model = LogisticRegression(max_iter=1000, class_weight="balanced")
    model.fit(X_train_s, y_train)

    y_pred = model.predict(X_test_s)
    y_prob = model.predict_proba(X_test_s)[:, 1]

    metrics = {
        "accuracy": round(accuracy_score(y_test, y_pred), 3),
        "precision": round(precision_score(y_test, y_pred), 3),
        "recall": round(recall_score(y_test, y_pred), 3),
        "roc_auc": round(roc_auc_score(y_test, y_prob), 3),
        "model": "LogisticRegression(class_weight='balanced')",
        "n_train": len(X_train),
        "n_test": len(X_test),
    }

    os.makedirs(REPORTS_DIR, exist_ok=True)
    with open(os.path.join(REPORTS_DIR, "model_metrics.json"), "w") as f:
        json.dump(metrics, f, indent=2)
    print("Model metrics:", json.dumps(metrics, indent=2))

    # Feature importance (top +/- coefficients)
    coefs = pd.Series(model.coef_[0], index=X.columns).sort_values()
    top = pd.concat([coefs.head(8), coefs.tail(8)])

    plt.figure(figsize=(7, 6))
    colors = ["#E9724C" if v > 0 else "#4C9F70" for v in top.values]
    plt.barh(top.index, top.values, color=colors)
    plt.axvline(0, color="black", linewidth=0.8)
    plt.title("Top Churn Drivers (Logistic Regression Coefficients)")
    plt.xlabel("Coefficient (positive = increases churn risk)")
    plt.tight_layout()
    os.makedirs(CHART_DIR, exist_ok=True)
    plt.savefig(os.path.join(CHART_DIR, "10_feature_importance.png"), dpi=150)
    plt.close()
    print(f"Saved chart -> {os.path.join(CHART_DIR, '10_feature_importance.png')}")

    return metrics


if __name__ == "__main__":
    run()
