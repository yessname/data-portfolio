import pandas as pd
import os
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine

DATA_DIR = "data"
RAW_FILE_PATH = os.path.join(DATA_DIR, "raw", "Superstore.csv")

STAGING_SCHEMA = "staging"
STAGING_TABLE = "raw_orders"

DB_USER = "postgres"
DB_PASSWORD = "Artsem"
DB_PORT = "5432"
DB_NAME = "superstore"
DB_HOST = "localhost"

DB_CONN_STR = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

def get_engine(conn_str: str = DB_CONN_STR) -> Engine:
    return create_engine(conn_str)

#Extract
def extract_superstore(path: str = RAW_FILE_PATH) -> pd.DataFrame:
    print( os.getcwd())
    df = pd.read_csv(path, encoding="latin1")
    return df

#Transform
def transform_superstore(df: pd.DataFrame) -> pd.DataFrame:
    columns = [
        "Row ID",
        "Order ID",
        "Order Date",
        "Ship Date",
        "Ship Mode",
        "Customer ID",
        "Customer Name",
        "Segment",
        "Country",
        "City",
        "State",
        "Postal Code",
        "Region",
        "Category",
        "Sub-Category",
        "Product ID",
        "Product Name",
        "Sales",
        "Quantity",
        "Discount",
        "Profit",
    ]
    df = df[columns]

    df = df.rename(
        columns={
            "Row ID": "row_id",
            "Order ID": "order_id",
            "Order Date": "order_date",
            "Ship Date": "ship_date",
            "Ship Mode": "ship_mode",
            "Customer ID": "customer_id",
            "Customer Name": "customer_name",
            "Segment": "segment",
            "Country": "country",
            "City": "city",
            "State": "state",
            "Postal Code": "postal_code",
            "Region": "region",
            "Category": "category",
            "Sub-Category": "sub_category",
            "Product ID": "product_id",
            "Product Name": "product_name",
            "Sales": "sales",
            "Quantity": "quantity",
            "Discount": "discount",
            "Profit": "profit",
        }
    )

    date_cols = ["order_date", "ship_date"]
    for col in date_cols:
        df[col] = pd.to_datetime(df[col], errors="coerce")

    numeric_cols = ["sales", "quantity", "discount", "profit"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna(
        subset=[
            "order_id",
            "order_date",
            "customer_id",
            "product_id",
            "sales",
        ]
    )

    return df

#Load
def load_to_staging(
    df: pd.DataFrame,
    engine: Engine,
    schema: str = STAGING_SCHEMA,
    table: str = STAGING_TABLE,
) -> None:
    df.to_sql(
        name=table,
        con=engine,
        schema=schema,
        if_exists="replace",
        index=False,
    )


def run_superstore_etl() -> None:
    engine = get_engine()

    with engine.begin() as conn:
        conn.execute(text(f'CREATE SCHEMA IF NOT EXISTS "{STAGING_SCHEMA}";'))

    df_raw = extract_superstore()
    df_clean = transform_superstore(df_raw)
    load_to_staging(df_clean, engine)


if __name__ == "__main__":
    run_superstore_etl()
