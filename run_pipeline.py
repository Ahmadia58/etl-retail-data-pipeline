import os
import pandas as pd
import datetime
from PIL import Image
import logging

logging.basicConfig(
    filename='etl_log.txt',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)
logging.info(f"[{datetime.datetime.now()}] etl_project is started\n")
os.system('python extract/extract_orders.py')
os.system('python transform/transform_orders.py')
os.system('python load/load_to_postgres.py')
os.startfile('etl_log.txt')


# نمایش تصویر

#img = Image.open("/Users/Ahmad/etl_project/image.jpg")
#img.show()

