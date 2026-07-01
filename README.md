# 📊 Customer Churn Prediction & Retention Analytics System

An end-to-end **data analytics project** covering the full lifecycle of a real business analytics workflow: data sourcing, ETL, cleaning, exploratory analysis, SQL querying, a lightweight predictive model, and executive reporting with visualizations.

**Dataset:** [Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) (7,043 customers, 21 attributes) — sourced from Kaggle / IBM's public sample data.

---

## 🎯 Project Goals

- Identify **why** customers churn and **who** is most likely to churn next.
- Quantify **revenue at risk** from churn.
- Deliver actionable retention recommendations backed by data.
- Demonstrate a realistic, reproducible data analyst workflow: **Extract → Transform → Load → Analyze → Visualize → Report**.

---

## 🗂️ Repository Structure

```
churn-project/
├── data/
│   ├── raw/                     # Original, unmodified source data
│   │   └── telco_churn.csv
│   └── processed/                # Cleaned data + SQLite warehouse
│       ├── telco_churn_clean.csv
│       └── churn_warehouse.db
├── etl/
│   ├── extract.py                # EXTRACT: pull raw data
│   ├── transform_clean.py        # TRANSFORM: clean + feature engineer
│   └── load.py                   # LOAD: load into SQLite warehouse
├── sql/
│   └── queries.sql               # Analytical SQL queries (8 business questions)
├── analysis/
│   ├── eda_analysis.py           # Exploratory data analysis + summary stats
│   └── churn_model.py            # Logistic regression churn prediction model
├── visuals/
│   ├── generate_charts.py        # Generates all charts
│   └── output/                   # 10 generated PNG charts
├── reports/
│   ├── Churn_Analysis_Report.md  # Full written analytics report
│   ├── summary_stats.json        # Machine-readable EDA summary
│   └── model_metrics.json        # Model performance metrics
├── requirements.txt
├── run_pipeline.py                # Runs the entire pipeline end-to-end
├── LICENSE
└── README.md
```

---

## 🔄 Pipeline Overview

| Stage | Script | Description |
|---|---|---|
| **Extract** | `etl/extract.py` | Downloads the raw Telco churn CSV |
| **Transform / Clean** | `etl/transform_clean.py` | Fixes data types, imputes missing values, deduplicates, engineers features (`tenure_group`, `num_services`, `clv_estimate`, etc.) |
| **Load** | `etl/load.py` | Loads cleaned data into a local SQLite warehouse (`churn_warehouse.db`) |
| **Analyze** | `analysis/eda_analysis.py` | Computes churn rate breakdowns by contract, tenure, payment method, services, etc. |
| **Model** | `analysis/churn_model.py` | Trains a Logistic Regression churn classifier (ROC-AUC 0.836) |
| **Visualize** | `visuals/generate_charts.py` | Generates 10 charts (pie, bar, KDE, heatmap) |
| **Report** | `reports/Churn_Analysis_Report.md` | Executive summary + recommendations |

---

## 🚀 Quickstart

```bash
# 1. Clone the repo
git clone https://github.com/<your-username>/customer-churn-retention-analytics.git
cd customer-churn-retention-analytics

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the full pipeline (ETL -> analysis -> model -> charts)
python run_pipeline.py
```

Or run each stage individually:

```bash
python etl/extract.py
python etl/transform_clean.py
python etl/load.py
python analysis/eda_analysis.py
python analysis/churn_model.py
python visuals/generate_charts.py
```

Query the warehouse directly with SQL:
```bash
sqlite3 data/processed/churn_warehouse.db < sql/queries.sql
```

---

## 📈 Key Insights

- **Overall churn rate: 26.5%** — 1,869 of 7,043 customers churned.
- **Month-to-month contracts churn at 42.7%** vs **2.8%** for two-year contracts.
- **Electronic check payers churn at 45.3%**, nearly 3x the rate of autopay customers.
- **~47% of customers churn within their first 12 months** — the highest-risk window.
- **$139K/month in revenue is currently at risk** from churned customers; **~$2.86M in estimated lifetime value already lost**.
- A simple logistic regression model achieves **0.836 ROC-AUC** in predicting churn.

📄 Full write-up: [`reports/Churn_Analysis_Report.md`](reports/Churn_Analysis_Report.md)

---

## 📊 Sample Visualizations

| Churn by Contract Type | Churn by Tenure Group |
|---|---|
| ![contract](visuals/output/02_churn_by_contract.png) | ![tenure](visuals/output/03_churn_by_tenure_group.png) |

| Revenue at Risk | Feature Importance |
|---|---|
| ![revenue](visuals/output/09_revenue_at_risk_by_contract.png) | ![features](visuals/output/10_feature_importance.png) |

*(See `visuals/output/` for all 10 charts.)*

---

## 🛠️ Tech Stack

- **Python**: pandas, numpy — ETL & data wrangling
- **SQLite**: lightweight analytical data warehouse
- **matplotlib / seaborn**: data visualization
- **scikit-learn**: churn prediction model
- **Markdown / JSON**: reporting outputs

---

## 📌 Business Recommendations

1. Incentivize migration from month-to-month to annual contracts.
2. Drive autopay adoption to reduce payment-related churn.
3. Strengthen onboarding and engagement in the first 12 months.
4. Investigate fiber-optic service experience and pricing.
5. Deploy the churn model monthly to proactively flag high-risk, high-value customers.

---

## 📄 License

This project is licensed under the MIT License — see [LICENSE](LICENSE).

## 🙌 Data Source Attribution

Dataset originally published on [Kaggle: Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) by BlastChar, based on IBM sample data.
