import json

from fastavro import parse_schema, validate
from fastavro._validate_common import ValidationError


def load_schema(schema_path: str):
    with open(schema_path, "r", encoding="utf-8") as f:
        schema = json.load(f)

    return parse_schema(schema)


def validate_event(event: dict, schema) -> bool:
    try:
        return validate(event, schema)
    except ValidationError:
        return False