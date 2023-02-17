import datetime


def is_report_range_valid(date_from: datetime.date, date_to: datetime.date) -> bool:
    return date_to <= date_from

if __name__ == '__main__':
    date_to_test = datetime.date(2023, 2, 15)
    date_from_test = datetime.date(2023, 2, 16)
    assert not is_report_range_valid(date_to_test, date_from_test)
    assert is_report_range_valid(date_from_test, date_to_test)
    assert is_report_range_valid(datetime.date(2023, 2, 16), datetime.date(2023, 2, 16))

