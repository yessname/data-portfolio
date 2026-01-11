import json
import os
from confluent_kafka import Consumer

BOOTSTRAP_SERVERS = "localhost:29092"
TOPIC = "weather"

os.makedirs("data", exist_ok=True)

consumer = Consumer({
    "bootstrap.servers": BOOTSTRAP_SERVERS,
    "group.id": "weather-simple",
    "auto.offset.reset": "earliest"
})

consumer.subscribe([TOPIC])

print("listening...")

with open("data/raw_events.jsonl", "a", encoding="utf-8") as f:
    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            print("error:", msg.error())
            continue

        event = json.loads(msg.value().decode("utf-8"))
        print("got:", event)

        f.write(json.dumps(event) + "\n")
        f.flush()