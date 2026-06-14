from confluent_kafka import Consumer

from app.config import KAFKA_BOOTSTRAP_SERVERS


def create_consumer(group_id: str, topic: str) -> Consumer:
    config = {
        "bootstrap.servers": KAFKA_BOOTSTRAP_SERVERS,
        "group.id": group_id,
        "auto.offset.reset": "earliest",
    }

    consumer = Consumer(config)

    consumer.subscribe([topic])

    return consumer