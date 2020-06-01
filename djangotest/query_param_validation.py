import datetime
from rest_framework.validators import ValidationError


def parse_birthday_filter(date_str: str):
    birthday_filter_format = '%d%m'
    try:
        return datetime.datetime.strptime(date_str, birthday_filter_format)
    except ValueError:
        raise ValidationError(detail=f"Incorrect data format for birthday filters: should be {birthday_filter_format}")
