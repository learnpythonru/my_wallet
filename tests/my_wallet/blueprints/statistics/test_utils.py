import datetime

import pytest


@pytest.fixture
def date_from():
    return datetime.datetime(2023, 2, 12, 23, 00)


@pytest.fixture
def date_to():
    return datetime.datetime(2023, 2, 12, 20, 00)


def test_is_report_range_valid(date_from: datetime.date, date_to: datetime.date) -> None:
    assert (date_to <= date_from) \
           == (datetime.datetime(2023, 2, 12, 20, 00) <= datetime.datetime(2023, 2, 12, 23, 00))
