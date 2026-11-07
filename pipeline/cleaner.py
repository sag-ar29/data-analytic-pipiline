import pandas as pd
import numpy as np

def clean_transaction_data(filepath: str) -> pd.DataFrame:
    """
    Ingests and sanitizes raw transaction datasets:
    - Imputes / drops invalid records
    - Standardizes date formats
    - Categorizes spend bands
    """
    df = pd.read_csv(filepath)
    
    # 1. Drop records missing mandatory identifiers
    df = df.dropna(subset=['transaction_id', 'user_id'])
    
    # 2. Parse timestamps
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    # 3. Clean numeric fields
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce').fillna(0.0)
    
    # 4. Standardize text categories
    df['category'] = df['category'].str.strip().str.capitalize()
    df['status'] = df['status'].str.strip().str.lower()
    
    # 5. Enrich dataset: Add spend segment
    df['spend_segment'] = np.where(
        df['amount'] >= 500, 'High',
        np.where(df['amount'] >= 100, 'Medium', 'Low')
    )
    
    return df

def generate_user_analytics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generates aggregated analytics per user.
    """
    completed_tx = df[df['status'] == 'completed']
    
    analytics = completed_tx.groupby('user_id').agg(
        total_spent=('amount', 'sum'),
        total_transactions=('transaction_id', 'count'),
        avg_transaction_value=('amount', 'mean'),
        primary_category=('category', lambda x: x.mode()[0] if not x.empty else 'N/A')
    ).reset_index()
    
    analytics['avg_transaction_value'] = analytics['avg_transaction_value'].round(2)
    return analytics

