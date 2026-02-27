import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """Transform step: clean and normalize the data."""
    df = df.dropna()
    df.columns = [col.lower().strip() for col in df.columns]
    return df
