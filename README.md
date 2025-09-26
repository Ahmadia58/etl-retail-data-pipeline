# etl-retail-data-pipeline
Data engineering project
## Sales Orders ETL Pipeline

This project builds a mini ETL pipeline to extract orders data, clean it, and load into a PostgreSQL database.

### Tech Stack
- Python
include the follwing libreries
- Logging (log and monitor)
- Os 
- Alchamy 
- Pytest
- Flask
-faker
- Pandas
and 
- PostgreSQL
- Task Scheduler (for scheduling)
### Structure
- extract/ : raw data extraction
We generate order data with API called extract_api.py.
In this project we create a dataset by Faker library called extract_orders.csv 
if there are any deficiencies, 
we improve them during the Transform stage.

- transform/ : cleaning and normalization
In this phase, we read the "orders_2025_06_06.csv" file of data_source folder and then 
check for things like having 
-an empty value, 
-duplicate values, and 
-the data type of the order_date column.
 If there is a discrepancy, we transform them.

- load/ : data insertion
I use postgreSQL for database. 
Also, I use SQL shell to create database and its table as orders.
The Alchamy Python library was used to load data from the source to the database.
You can use the Alchamy, text Python library to incrementally load data into the database.
## 🛠️Monitoring & Logging

To monitor ETL execution:
- `logging` module is used at each step
- All logs are saved in `etl_log.txt`
- Possible errors, data quality warnings and success messages are logged
- Suitable for checking the status of cron job execution and analyzing possible problems
### Run
```bash
python run_pipeline.py

or schedule with:
Task scaedualer 

## ✨ Features

- Automated ETL testing
- Scheduled execution with Task scheduler.
- Full documentation

🛠️ Requirements
we use requirements.txt to install all necessary packages.

✨ Future Developments
-Connect to API instead of CSV file
-Use Apache Airflow






