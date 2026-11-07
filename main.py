import os
from pipeline.cleaner import clean_transaction_data, generate_user_analytics
from pipeline.db_loader import load_to_database

def run_pipeline():
    raw_data_path = os.path.join(os.path.dirname(__file__), "sample_data.csv")
    print(f"[1/3] Ingesting raw data from {raw_data_path}...")
    
    cleaned_df = clean_transaction_data(raw_data_path)
    print(f"      Successfully sanitized {len(cleaned_df)} valid transactions.")
    
    print("[2/3] Computing aggregation metrics...")
    analytics_df = generate_user_analytics(cleaned_df)
    print(f"      Calculated metrics for {len(analytics_df)} distinct users.")
    
    print("[3/3] Loading aggregated insights into relational database...")
    count = load_to_database(analytics_df, "user_spend_analytics")
    print(f"      Successfully persisted {count} records into 'user_spend_analytics' table.")
    print("\n--- Pipeline Summary ---")
    print(analytics_df.to_string(index=False))

if __name__ == "__main__":
    run_pipeline()

