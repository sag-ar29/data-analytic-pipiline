from sqlalchemy import create_engine
import pandas as pd

def load_to_database(df: pd.DataFrame, table_name: str, db_url: str = "sqlite:///./analytics.db") -> int:
    """
    Persists processed DataFrames into relational storage.
    """
    engine = create_engine(db_url)
    df.to_sql(table_name, con=engine, if_exists="replace", index=False)
    return len(df)

