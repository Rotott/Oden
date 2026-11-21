from datetime import UTC, datetime

import pytest


@pytest.fixture
def utc_reference_time() -> datetime:
    """Capture the current UTC time before the test runs."""
    return datetime.now(UTC)
