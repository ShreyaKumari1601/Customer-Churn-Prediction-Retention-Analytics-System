import pandas as pd

def generate_retention_insights(filepath):
    df = pd.read_csv(filepath)
    churn_rate = df['churn'].mean()
    
    high_risk_segment = df[df['tenure'] < 12]
    high_risk_rate = high_risk_segment['churn'].mean()
    
    print(f"Overall Churn Rate: {churn_rate:.2f}")
    print(f"Churn Rate for Customers with <12 months tenure: {high_risk_rate:.2f}")
    
    if high_risk_rate > churn_rate:
        print("Recommendation: Focus retention campaigns on new customers.")
    else:
        print("Recommendation: Evaluate other behavioral features.")
        
if __name__ == "__main__":
    generate_retention_insights("data/sample_churn_data.csv")
