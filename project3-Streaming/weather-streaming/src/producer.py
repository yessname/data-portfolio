import json
import time
from datetime import datetime, timezone

import requests
from confluent_kafka import Producer

BOOTSTRAP_SERVERS = "localhost:29092"
TOPIC = "weather"

producer = Producer({"bootstrap.servers": BOOTSTRAP_SERVERS})

def now_utc():
    return datetime.now(timezone.utc).isoformat()

while True:
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=52.2297&longitude=21.0122&current_weather=true"
    )
    data = requests.get(url, timeout=10).json()
    current = data["current_weather"]

    event = {
        "ts_utc": now_utc(),
        "city": "Warsaw",
        "temperature_c": current["temperature"],
        "wind_kph": current["windspeed"],
        "source": "open-meteo"
    }

    producer.produce(
        TOPIC,
        value=json.dumps(event).encode("utf-8")
    )
    producer.flush()

    print("sent:", event)
    time.sleep(60)
