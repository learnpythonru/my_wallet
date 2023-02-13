import datetime


def is_report_range_valid(date_from: datetime.date, date_to: datetime.date) -> bool:
    return date_to <= date_from


if __name__ == '__main__':

    test_date_from = datetime.datetime.strptime('13/02/23 13:55:26', '%d/%m/%y %H:%M:%S')
    test_date_to = datetime.datetime.strptime('13/01/23 13:55:26', '%d/%m/%y %H:%M:%S')
    assert is_report_range_valid(date_from = test_date_from, date_to = test_date_to) == True

