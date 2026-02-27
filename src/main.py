from extract import extract_csv
from transform import transform_data
from load import load_to_parquet

def run_etl():
    input_path = "data/input.csv"
    output_path = "data/output.parquet"

    df = extract_csv(input_path)
    df = transform_data(df)
    load_to_parquet(df, output_path)

    print(f"ETL complete. Parquet file saved to {output_path}")

if __name__ == "__main__":
    run_etl()
