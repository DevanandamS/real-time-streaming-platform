import json

from app.producer import create_producer


producer = create_producer()


def send_to_topic(topic: str, event: dict):
    producer.produce(
        topic=topic,
        value=json.dumps(event),
    )

    producer.flush()