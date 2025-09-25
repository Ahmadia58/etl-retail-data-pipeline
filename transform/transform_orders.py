import pandas as pd
import logging
logging.basicConfig(
    filename='etl_log.txt',
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

logging.info(f"Start of Transformation ")
extracted=pd.read_csv('/Users/Ahmad/etl_project/extract/extracted_orders2.csv')
extracted=extracted.dropna()
extracted=extracted.drop_duplicates()
extracted['order_date']=pd.to_datetime(extracted['order_date'])
extracted=extracted[extracted['amount']>0]
Q90=extracted['amount'].quantile(0.9)
outlaier=extracted[extracted['amount']>Q90]
logging.info(f"outlaier of extracted: {outlaier.value_counts().sum()} ")
extracted=extracted[extracted['amount']<=Q90]
def categorize_amount(amount):
    if amount < 100:
        return "Low"
    elif amount > 500: 
        return "High"
    else:  
        return "Medium"

extracted['amount_category'] = extracted['amount'].apply(categorize_amount)
extracted['tax']=extracted['amount']*.09
extracted.to_csv("/Users/Ahmad/etl_project/transform/transformed_orders1.csv")
extracted = extracted[extracted['amount'] > 0]
logging.info(f"After removing negative values: {len(extracted)}")
if len(extracted[extracted['amount_category']=="High"])>150:
    logging.warning(f"Low number of valid orders: {len(extracted[extracted['amount_category']=="High"])}")








