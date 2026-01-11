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

1. Start the Docker services:

docker compose up -d

2. Open Airflow UI

Open Airflow in your browser:
http://localhost:8080 (username: airflow, password: airflow)

3. Run the pipeline (Airflow DAG)

In the Airflow UI:

- Find the DAG named airbnb_etl
- Enable it using the toggle on the left
- Trigger it manually ("Trigger DAG")

Airflow will execute the full ETL flow: extract → transform → load.
When all tasks turn green, the pipeline finished successfully and the data has been loaded.

4. Database access notes

Inside Docker, Airflow connects to PostgreSQL using the internal hostname (postgres)
