# 🌦 Weather Streaming Pipeline (Kafka)

A simple real-time data streaming pipeline built with **Python** and **Apache Kafka**.

The project demonstrates how weather data can be ingested from an external API, published as events to a Kafka topic, and consumed in real time for further processing.

---

## 📌 Project Overview

This project demonstrates:

- Real-time ingestion of weather data from a public API  
- Publishing events to Apache Kafka  
- Consuming streaming data in real time  
- Persisting raw events in append-only format  

---

## 🎯 Project Goals

- Ingest real-time weather data from a public API  
- Publish weather events to Apache Kafka  
- Consume streaming data in real time  
- Persist raw events in JSON Lines format  

---

## 🌍 Data Source

The project uses the **Open-Meteo API** (free public weather API).

API documentation:  
https://open-meteo.com/

---

## 🛠 Tech Stack

- Python  
- Apache Kafka  
- Docker  
- Open-Meteo API  

---

## 🏗 Streaming Architecture

The pipeline consists of two main components:

### Producer

- Periodically requests current weather data from the API  
- Converts API responses into structured JSON events  
- Publishes events to a Kafka topic  

### Consumer

- Subscribes to the Kafka topic  
- Reads events in real time  
- Writes raw events to a local file in JSON Lines (`.jsonl`) format  

---

## 📦 Event Format

Each Kafka message represents a single weather observation.

Example:

```json
{
  "ts_utc": "2026-01-08T20:15:00Z",
  "city": "Warsaw",
  "temperature_c": -5.8,
  "wind_kph": 13.3,
  "source": "open-meteo"
}
```

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
