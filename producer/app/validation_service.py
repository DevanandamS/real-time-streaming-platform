import json

from app.consumer import create_consumer
from app.logger import get_logger
from app.event_router import send_to_topic
from app.config import VALIDATED_TOPIC


logger = get_logger(__name__)


def main():
    consumer = create_consumer(
        group_id="validation-service",
        topic="raw_events",
    )

    logger.info("validation_service_started")

    try:
        while True:
            msg = consumer.poll(1.0)

            if msg is None:
                continue

            if msg.error():
                logger.error(
                    "consumer_error",
                    extra={"error": str(msg.error())},
                )
                continue

            event = json.loads(
                msg.value().decode("utf-8")
            )

            logger.info(
                "event_validated",
                extra={"event": event},
            )

            send_to_topic(
                VALIDATED_TOPIC,
                event,
            )

    finally:
        consumer.close()


if __name__ == "__main__":
    main()