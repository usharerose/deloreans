import datetime
from datetime import timedelta


def get_week_anchor_date(a_date: datetime.date) -> datetime.date:
    """
    Thursday of week determine the year and month that week belongs to
    """
    assert isinstance(a_date, datetime.date)
    weekday = a_date.weekday()
    date_delta = 3 - weekday
    key_date = a_date + timedelta(days=date_delta)
    return key_date


def get_weeks_offset_between_dates(
    prev_date: datetime.date,
    cur_date: datetime.date,
) -> int:
    """
    Count of week offset from
    the week that prev_date belonging
    to the week that cur_date belonging to
    """
    assert isinstance(prev_date, datetime.date)
    assert isinstance(cur_date, datetime.date)
    assert cur_date >= prev_date
    cur_week_key_date = get_week_anchor_date(cur_date)
    prev_week_key_date = get_week_anchor_date(prev_date)
    return ((cur_week_key_date - prev_week_key_date).days + 1) // 7


def get_start_date_of_monthly_start_week(year: int, month: int) -> datetime.date:
    """
    get the start date of week
    which is the first week of given month
    """
    assert isinstance(year, int)
    assert isinstance(month, int)
    assert year > 0
    assert 1 <= month <= 12
    belonging_month_first_date = datetime.date(year, month, 1)
    first_date_weekday = belonging_month_first_date.weekday()
    if first_date_weekday <= 3:
        date_delta = 3 - first_date_weekday
    else:
        date_delta = 10 - first_date_weekday
    first_week_start_date = belonging_month_first_date + timedelta(days=date_delta) - timedelta(days=3)
    return first_week_start_date
