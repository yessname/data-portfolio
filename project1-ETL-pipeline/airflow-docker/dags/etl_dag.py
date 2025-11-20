from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

from src.etl import extract, transform, load


default_args = {
    "owner": "art",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
}


with DAG(
    dag_id="airbnb_etl",
    description="Airbnb ETL",
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    max_active_runs=1
) as dag:

    dag.doc_md = ""

    extract_task = PythonOperator(
        task_id="extract_listings",
        python_callable=extract,
        doc_md="",
    )

    transform_task = PythonOperator(
        task_id="transform_listings",
        python_callable=transform,
        doc_md="",
    )

    load_task = PythonOperator(
        task_id="load_listings",
        python_callable=load,
        doc_md="",
    )

    extract_task >> transform_task >> load_task