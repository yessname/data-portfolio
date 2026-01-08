Airbnb NYC ETL Pipeline

This project is a ETL pipeline built with Apache Airflow, PostgreSQL and Docker.  
It demonstrates how to orchestrate data extraction, transformation, loading and how to perform data analysis on the processed dataset.

The pipeline works with the publicly available Airbnb NYC dataset.
https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data

---

Project Goals

- Automate data ingestion using Airflow
- Clean and transform raw Airbnb data using Python
- Load processed data into PostgreSQL
- Perform basic analysis and visualization in a Jupyter Notebook
- Build analytical reports and dashboards using Power BI

---

Tech Stack

- Python, pandas, SQLAlchemy, matplotlib
- Apache Airflow
- PostgreSQL
- Docker
- Jupyter Notebook
- Power BI

---

Project Structure

project/
├─ dags/
│ └─ etl_dag.py
├─ data/
│ ├─ raw/
│ └─ clean/
├─ notebooks/
│ └─ airbnb_analysis.ipynb
├─ sql/
│ └─ create_table.sql
├─ src/
│ └─ etl.py
├─ docker-compose.yaml
└─ README.md

---

How to run

To run the pipeline, first start the Docker containers by running “docker compose up” in the project root. This launches PostgreSQL, the Airflow webserver, and the Airflow scheduler. Once the services are running, open Airflow in your browser at http://localhost:8080 (username “airflow” and password “airflow”).

In the Airflow UI, find the DAG named “airbnb_etl”. Enable it using the toggle on the left, then trigger it manually. The pipeline will execute the full ETL flow: extract, transform and load. After all tasks turn green, the data has been successfully processed.

Airflow connects to the database using the internal Docker hostname “postgres”. If you want to access the database from your local machine, connect through localhost on the port exposed in docker-compose.