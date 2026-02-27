import pandas as pd

def load_to_parquet(df: pd.DataFrame, output_path: str):
    """Load step: write DataFrame to Parquet format."""
    df.to_parquet(output_path, index=False)
