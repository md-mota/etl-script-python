# CSV to Parquet ETL Pipeline

A simple ETL pipeline built in Python that:
- Extracts data from a CSV file
- Transforms and cleans the data
- Loads the result into a Parquet file

## Project Structure
'''
csv-to-parquet-etl/
│
├── data/
│   ├── input.csv
│   └── output.parquet
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── main.py
│
├── requirements.txt
└── README.md
'''

## How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Place your CSV file at:
   data/input.csv

3. Run the ETL pipeline:
   python src/main.py

4. The Parquet file will be generated at:
   data/output.parquet

## Technologies Used
- Python
- Pandas
- PyArrow (for Parquet)
