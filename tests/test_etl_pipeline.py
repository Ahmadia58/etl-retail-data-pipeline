
import pandas as pd
import os

def test_extracted_file_exists():
    assert os.path.exists("/Users/Ahmad/etl_project/extract/extracted_orders1.csv")

def test_transformed_file_columns():
    df = pd.read_csv("/Users/Ahmad/etl_project/transform/transformed_orders1.csv")
    expected_cols = ["order_id", "customer_name", "product", "amount", "tax", "amount_category", "order_date"]
    missing_cols = [col for col in expected_cols if col not in df.columns]
    assert not missing_cols, f"Missing columns: {missing_cols}"



def test_no_negative_amounts():
    df = pd.read_csv("/Users/Ahmad/etl_project/transform/transformed_orders1.csv")
    assert (df["amount"] >= 0).all()
