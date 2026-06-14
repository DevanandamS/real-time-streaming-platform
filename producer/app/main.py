import json

from app.config import RAW_TOPIC
from app.logger import get_logger
from app.producer import create_producer

logger = get_logger(__name__)


def delivery_report(err, msg):
    if err:
        logger.error(
            "message_delivery_failed",
            extra={"error": str(err)}
        )
    else:
        logger.info(
            "message_delivered",
            extra={
                "topic": msg.topic(),
                "partition": msg.partition(),
                "offset": msg.offset(),
            },
        )


def main():
    producer = create_producer()

    event = {
        "event_id": "evt_001",
        "user_id": "usr_001",
        "product_id": "prd_001",
        "amount": 99.99,
        "event_time": "2026-06-14T14:00:00Z",
    }

    producer.produce(
        topic=RAW_TOPIC,
        value=json.dumps(event),
        callback=delivery_report,
    )

    producer.flush()


if __name__ == "__main__":
    main()