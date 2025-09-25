import pandas as pd
import logging
import os

logging.basicConfig(filename='etl_log.txt',
				   level=logging.INFO,
                   format='%(asctime)s:%(levelname)s:%(message)s'
)
logging.info(f"Start of Extraction")

try:
    df = pd.read_csv("/Users/Ahmad/etl_project/data_sources/orders_2025_06_06.csv")
    df.to_csv("/Users/Ahmad/etl_project/extract/extracted_orders.csv", index=False)
    df.to_parquet("/Users/Ahmad/etl_project/extract/extracted_orders.parquet", index=False)
    logging.info("Data extracted successfully.")
except Exception as e:
    logging.error(f"Error in the extraction phase: {e}")
