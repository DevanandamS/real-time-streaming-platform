def is_valid_purchase(event: dict) -> bool:
    return event["amount"] > 0