import pandas as pd
from sqlalchemy import create_engine
import logging
logging.basicConfig(filename='etl_log.txt',
				   level=logging.INFO,
                   format='%(asctime)s:%(levelname)s:%(message)s'
)
logging.info(f"Start of Loading")

# ساخت اتصال
engine = create_engine("postgresql://postgres:1013@localhost:5432/data_engineer_project")
logging.info(f"Engine created")
# خواندن فایل CSV
df = pd.read_csv("C:/Users/Ahmad/etl_project/etl-retail-data-pipeline/transform/transformed_orders1.csv")

# ذخیره در دیتابیس
df.to_sql("orders1", engine, schema="public", index=False, if_exists="replace")
logging.info(f"Data loaded in database")



