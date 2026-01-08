import pandas as pd
import os
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

DATA_DIR = "data"
RAW_FILE_PATH = os.path.join(DATA_DIR, "raw", "AB_NYC_2019.csv")
STAGING_DIR = os.path.join(DATA_DIR, "staging")
STAGING_FILE_PATH = os.path.join(STAGING_DIR, "AB_NYC_2019_extracted.csv")
CLEAN_DIR = os.path.join(DATA_DIR, "clean")
CLEAN_FILE_PATH = os.path.join(CLEAN_DIR, "AB_NYC_2019.parquet")

DB_USER = "airflow"
DB_PASSWORD = "airflow"
DB_PORT = "5432"
DB_NAME = "airflow"
DB_HOST = "postgres"

DB_CONN_STR = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


def get_engine(conn_str: str = DB_CONN_STR) -> Engine:
    return create_engine(conn_str)

#Extract
def extract():
    df = pd.read_csv('data/raw/AB_NYC_2019.csv')

    os.makedirs("data/staging", exist_ok=True)
    df.to_csv("data/staging/AB_NYC_2019_extracted.csv", index=False)

    print("Extraction completed")

    return df

#Transform
def transform():
    df = pd.read_csv('data/staging/AB_NYC_2019_extracted.csv')
    cols = [
        "id",
        "host_id",
        "neighbourhood_group",
        "neighbourhood",
        "latitude",
        "longitude",
        "room_type",
        "price",
        "minimum_nights",
        "number_of_reviews",
        "last_review",
        "reviews_per_month",
        "calculated_host_listings_count",
        "availability_365"
    ]
    df = df[cols]

    df = df.rename(columns={
        "id": "listing_id",
        "calculated_host_listings_count": "host_listings_count"
    })

    df["listing_id"] = pd.to_numeric(df["listing_id"], errors="coerce").astype("Int64")
    df["host_id"] = pd.to_numeric(df["host_id"], errors="coerce").astype("Int64")
    df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")
    df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce")
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["minimum_nights"] = pd.to_numeric(df["minimum_nights"], errors="coerce").astype("Int64")
    df["number_of_reviews"] = pd.to_numeric(df["number_of_reviews"], errors="coerce").astype("Int64")
    df["last_review"] = pd.to_datetime(df["last_review"], errors="coerce")
    df["reviews_per_month"] = pd.to_numeric(df["reviews_per_month"], errors="coerce")
    df["host_listings_count"] = pd.to_numeric(df["host_listings_count"], errors="coerce").astype("Int64")
    df["availability_365"] = pd.to_numeric(df["availability_365"], errors="coerce").astype("Int64")

    df = df.dropna(subset=["listing_id", "host_id", "neighbourhood", "longitude", "latitude", "room_type", "price"])

    df = df[df["price"] > 0]

    os.makedirs("data/staging", exist_ok=True)
    df.to_parquet("data/staging/AB_NYC_2019_transformed.parquet")

    print("Transformation completed")

    return df

#Loading
def load():
    df = pd.read_parquet("data/staging/AB_NYC_2019_transformed.parquet")

    engine = get_engine()
    
    df.to_sql(
        name="listings",
        #schema="airbnb",
        con=engine,
        if_exists="replace",
        index=False
    )

    print("Loading completed")
