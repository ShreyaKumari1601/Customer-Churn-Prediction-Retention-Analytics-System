"""
run_pipeline.py
----------------
Runs the entire Customer Churn Analytics pipeline end-to-end:
Extract -> Clean -> Load -> EDA -> Model -> Visualizations.

Usage:
    python run_pipeline.py
"""

import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, "etl"))
sys.path.insert(0, os.path.join(ROOT, "analysis"))
sys.path.insert(0, os.path.join(ROOT, "visuals"))


def main():
    print("=" * 70)
    print("STEP 1/4: ETL (Extract -> Clean -> Load)")
    print("=" * 70)
    import load as etl_load
    df = etl_load.clean_and_get_df()
    etl_load.load(df)

    print("\n" + "=" * 70)
    print("STEP 2/4: Exploratory Data Analysis")
    print("=" * 70)
    import eda_analysis
    eda_analysis.run()

    print("\n" + "=" * 70)
    print("STEP 3/4: Churn Prediction Model")
    print("=" * 70)
    import churn_model
    churn_model.run()

    print("\n" + "=" * 70)
    print("STEP 4/4: Generating Visualizations")
    print("=" * 70)
    import generate_charts
    generate_charts.main()

    print("\nPipeline complete. See /reports and /visuals/output for results.")


if __name__ == "__main__":
    main()
