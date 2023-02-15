import datetime


def is_report_range_valid(date_from: datetime.date, date_to: datetime.date) -> bool:
    return date_to <= date_from


if __name__ == '__main__':
    date_to = '2001-02-15 12:24:18.917611'
    date_from = '2023-02-15 12:24:18.917611'
    assert is_report_range_valid(date_from, date_to) == True
    date_to = '2051-02-15 12:24:18.917611'
    date_from = '2023-02-15 12:24:18.917611'
    assert is_report_range_valid(date_from, date_to) == False