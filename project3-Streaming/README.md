Weather Streaming Pipeline (Kafka)

This project is a simple real-time data streaming pipeline built with Python and Apache Kafka. It demonstrates how weather data can be ingested from an external API, published as events to a Kafka topic, and consumed in real time for further processing.

---

Project Goals

- Ingest real-time weather data from a public API
- Publish weather events to Apache Kafka
- Consume streaming data in real time
- Persist raw events in an append-only format

---

Data Source

The project uses the Open-Meteo API (free public weather API).

API documentation:
https://open-meteo.com/

---

Tech Stack

- Python
- Apache Kafka
- Docker
- Open-Meteo API

---

Streaming Architecture

The pipeline consists of two main components:

1. Producer

- Periodically requests current weather data from the API
- Converts API responses into structured JSON events
- Publishes events to a Kafka topic

2. Consumer

- Subscribes to the Kafka topic
- Reads events in real time
- Writes raw events to a local file in JSON Lines format

---

Event Format

Each Kafka message represents a single weather observation, 
Example:

{
  "ts_utc": "2026-01-08T20:15:00Z",
  "city": "Warsaw",
  "temperature_c": -5.8,
  "wind_kph": 13.3,
  "source": "open-meteo"
}

Consumed events are stored in JSON Lines (.jsonl) format:

---

Project Structure

project/
├─ weather-streaming/
│ └─ src/
│ │ └─ data
│ │ │ └─ raw_events.jsonl
│ │ ├─ consumer.py
│ │ └─ producer.py
│ └─ docker-compose.yaml
└─ README.md

---

How to Run
1. Start Kafka using Docker:
docker compose up -d

2. Create Kafka Topic:
docker exec -it kafka bash -lc "/opt/kafka/bin/kafka-topics.sh --bootstrap-server kafka:9092 --create --topic weather --partitions 1 --replication-factor 1"

3. Run Consumer

In one terminal:
python src/consumer.py

4. Run Producer

In another terminal:
python src/producer.py

