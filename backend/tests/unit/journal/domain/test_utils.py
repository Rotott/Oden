from datetime import UTC, datetime

from src.journal.domain.utils import utc_now


# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Return type
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


def test_utc_now_returns_datetime():
    result = utc_now()

    assert isinstance(result, datetime)


# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Timezone
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


def test_utc_now_returns_utc_timezone():
    result = utc_now()

    assert result.tzinfo is UTC


def test_utc_now_returns_timezone_aware_datetime():
    result = utc_now()

    assert result.tzinfo is not None
    assert result.utcoffset() is not None


def test_utc_now_has_zero_utc_offset():
    result = utc_now()

    assert result.utcoffset().total_seconds() == 0


# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Current timestamp
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


def test_utc_now_returns_current_time(utc_reference_time):
    result = utc_now()
    time_after_call = datetime.now(UTC)

    assert utc_reference_time <= result <= time_after_call
