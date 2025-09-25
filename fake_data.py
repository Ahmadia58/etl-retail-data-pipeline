
from faker import Faker
import pandas as pd
import random

fake = Faker()
data = []
for _ in range(1000):
    data.append({
        "order_id": fake.uuid4(),
        "customer_name": fake.name(),
        "product": fake.word(),
        "amount": round(random.uniform(-10, 900), 2),
        "order_date": fake.date_this_year()
    })

df = pd.DataFrame(data)
df.to_csv("/Users/Ahmad/etl_project/data_sources/orders_2025_06_06.csv", index=False)
