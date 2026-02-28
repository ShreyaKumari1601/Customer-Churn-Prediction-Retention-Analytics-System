import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_and_preprocess(filepath):
    df = pd.read_csv(filepath)
    
    categorical_cols = ["contract_type", "payment_method"]
    le = LabelEncoder()
    
    for col in categorical_cols:
        df[col] = le.fit_transform(df[col])
    
    X = df.drop("churn", axis=1)
    y = df["churn"]
    
    return X, y
