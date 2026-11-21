from datetime import UTC, datetime


def utc_now() -> datetime:
    # Return the current time as a UTC timestamp.
    return datetime.now(UTC)
