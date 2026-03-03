# 🛒 Superstore ETL Pipeline (Star Schema)

ETL pipeline built with **Python** and **PostgreSQL**, focused on preparing raw transactional data for analytical use by modeling it into a **star schema**.

The pipeline processes the publicly available Superstore dataset and demonstrates how raw data can be cleaned, normalized, and loaded into a staging layer as a foundation for building fact and dimension tables.

---

## 📌 Project Overview

This project demonstrates:

- Extraction of raw transactional data from CSV
- Data cleaning and standardization using pandas
- Loading cleaned data into a PostgreSQL staging schema
- Preparation for dimensional modeling (star schema)
- Core data engineering concepts: ETL, staging, dimensional modeling

---

## 🎯 Project Goals

- Extract raw Superstore data from CSV  
- Clean and standardize data using Python (pandas)  
- Load cleaned data into a staging schema in PostgreSQL  
- Prepare data for analytical modeling using a star schema  
- Demonstrate ETL and data warehouse fundamentals  

---

## 📊 Dataset

The project uses the **Superstore dataset**, which contains retail order data such as:

- Customers  
- Products  
- Shipping details  
- Sales  
- Profit  

The dataset represents a typical transactional source system suitable for analytical transformation.

Source:  
https://www.kaggle.com/datasets/vivek468/superstore-dataset-final

---

## 🛠 Tech Stack

- Python  
- pandas  
- SQLAlchemy  
- PostgreSQL  
- Power BI  

---

## 🏗 Data Modeling Approach

The ETL pipeline loads cleaned data into a staging table:


staging.raw_orders


From this staging layer, the data can be transformed into a **star schema**.

---

### 📦 Fact Table

fact_sales

row_id (PK)
order_id (degenerate dimension)
customer_sk (FK → dim_customer)
product_sk (FK → dim_product)
location_sk (FK → dim_location)
order_date_id (FK → dim_date)
ship_date_id (FK → dim_date)
ship_mode_sk (FK → dim_ship_mode)
sales
quantity
discount
profit


---

### 📚 Dimension Tables

dim_customer

customer_id (PK)
customer_name
segment

dim_product

product_id (PK)
product_name
category
sub_category

dim_location

location_id (PK)
country
region
state
city
postal_code

dim_date

date_sk (PK)
date
year
month
day
day_of_week
day_of_week_name
week
quarter

dim_ship_mode

ship_mode_id (PK)
ship_mode_name


---

This approach separates raw data ingestion from analytical modeling and follows common data warehouse practices.


---

## 📈 Analytics & Visualization

An analytical dashboard was created in **Power BI** based on the data modeled using a star schema.

The dashboard provides insights into:

- Total sales and profit over time  
- Sales performance by product category and sub-category  
- Regional sales analysis  
- Additional business metrics  

Power BI imports data directly from PostgreSQL and uses the fact and dimension tables as the data source.

---

## 🚀 How to Run

### 1. Ensure PostgreSQL is running

Create a database named:


superstore


---

### 2. Run the ETL pipeline


python superstore_etl.py


---

### 3. Verify data

After successful execution, the cleaned data will be available in PostgreSQL under:


staging.raw_orders
