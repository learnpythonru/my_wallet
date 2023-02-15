from datetime import datetime


def is_report_range_valid(date_from: datetime.date, date_to: datetime.date) -> bool:
    return date_to <= date_from


if __name__ == '__main__':
    date_to = '2001-02-15 11:47:37.088072'
    date_from = '2023-03-18 20:15:35.088006'
    assert is_report_range_valid(date_from, date_to) == (date_to <= date_from)

    date_to = '2023-03-18 20:15:35.088006'
    date_from = '2023-03-18 20:15:35.088006'
    assert is_report_range_valid(date_from, date_to) == (date_to <= date_from)

    date_to = '2051-02-15 11:47:37.088072'
    date_from = '2023-03-18 20:15:35.088006'
    assert is_report_range_valid(date_from, date_to) == (date_to <= date_from)
    