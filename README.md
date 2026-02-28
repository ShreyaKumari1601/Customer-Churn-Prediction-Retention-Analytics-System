# Customer Churn Prediction & Retention Analytics System

## Overview
This project predicts customer churn using behavioral and demographic data.
It includes data preprocessing, feature engineering, model training, evaluation,
and retention insights generation.

## Tech Stack
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn

## Project Structure
```
Customer_Churn_Prediction_System/
│
├── data/
│   └── sample_churn_data.csv
├── notebooks/
│   └── churn_analysis.ipynb
├── src/
│   ├── data_preprocessing.py
│   ├── model_training.py
│   ├── evaluation.py
│   └── retention_insights.py
├── models/
│   └── churn_model.pkl
├── requirements.txt
└── README.md
```

## How to Run

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Train model:
   ```
   python src/model_training.py
   ```

3. Evaluate model:
   ```
   python src/evaluation.py
   ```

## Business Impact
Helps SaaS companies identify high-risk customers and implement proactive
retention strategies.
