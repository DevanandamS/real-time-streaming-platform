from confluent_kafka import Producer

from app.config import KAFKA_BOOTSTRAP_SERVERS


def create_producer() -> Producer:
    config = {
        "bootstrap.servers": KAFKA_BOOTSTRAP_SERVERS,
        "acks": "all",
        "retries": 5,
        "enable.idempotence": True,
    }

    return Producer(config)