import pandas as pd

def extract_csv(path: str) -> pd.DataFrame:
    """Extract step: read CSV into a DataFrame."""
    return pd.read_csv(path)
