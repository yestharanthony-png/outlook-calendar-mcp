from datetime import datetime


def parse_datetime(dt: str) -> datetime:
    """
    Convert Graph datetime string into datetime object.
    """

    return datetime.fromisoformat(
        dt.split(".")[0]
    )


def format_datetime(dt: datetime) -> str:
    """
    Convert datetime object into Graph datetime string.
    """

    return dt.strftime("%Y-%m-%dT%H:%M:%S")