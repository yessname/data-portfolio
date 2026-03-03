# 🏠 Airbnb NYC ETL Pipeline

ETL pipeline built with **Apache Airflow**, **PostgreSQL**, and **Docker**.  
The project demonstrates orchestration of data extraction, transformation, and loading (ETL) using a publicly available dataset.

Dataset used: NYC Airbnb Open Data (Kaggle)

---

## 📌 Project Overview

This project automates the full ETL workflow:

- Extract raw Airbnb data  
- Transform and clean the dataset using Python  
- Load processed data into PostgreSQL  
- Perform data analysis in Jupyter Notebook  

---

## 🎯 Project Goals

- Automate data ingestion using Apache Airflow  
- Clean and transform raw Airbnb data using Python  
- Load processed data into PostgreSQL  
- Perform exploratory data analysis  

---

## 🛠 Tech Stack

- Python  
- pandas  
- SQLAlchemy  
- matplotlib  
- Apache Airflow  
- PostgreSQL  
- Docker  
- Jupyter Notebook  

---

## 🚀 How to Run

### 1. Start Docker services


docker compose up -d


### 2. Open Airflow UI

Open in your browser:


http://localhost:8080


Credentials:  
- Username: airflow  
- Password: airflow  

### 3. Run the ETL Pipeline

In the Airflow UI:

1. Find the DAG named `airbnb_etl`
2. Enable it using the toggle
3. Click **Trigger DAG**

Airflow will execute the full ETL flow:


extract → transform → load


When all tasks turn green, the pipeline finished successfully and the data has been loaded into PostgreSQL.

---

## 🗄 Database Notes

Inside Docker, Airflow connects to PostgreSQL using the internal hostname:


postgres


---

## 📊 Analysis

Data analysis and visualizations are available in:


notebooks/airbnb_analysis.ipynb


---

## 📎 Dataset

NYC Airbnb Open Data:  
https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data
