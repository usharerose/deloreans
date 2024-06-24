import datetime
from datetime import timedelta


def get_weekly_start_date(a_date: datetime.date) -> datetime.date:
    """
    get the start date of week which given date located
    """
    date_index = a_date.weekday()
    return a_date - timedelta(days=date_index)


def get_week_anchor_date(a_date: datetime.date) -> datetime.date:
    """
    The fourth day of week determine the year and month that week located
    """
    assert isinstance(a_date, datetime.date)
    start_date = get_weekly_start_date(a_date)
    return start_date + timedelta(days=3)


def get_weeks_offset(
    base_date: datetime.date,
    compared_date: datetime.date,
) -> int:
    """
    Weeks offset between the weeks which given dates located

    e.g. according to ISO week data:
         base_date is 2024-04-30, which is at 2024 no.18 week
         compared_date is 2024-06-01, which is at 2024 no.22 week

         then the offset of week is 22 - 18 = 4
    """
    base_week_anchor_date = get_week_anchor_date(base_date)
    compared_week_anchor_date = get_week_anchor_date(compared_date)
    return ((compared_week_anchor_date - base_week_anchor_date).days + 1) // 7


def get_start_weekly_of_month(year: int, month: int) -> datetime.date:
    """
    get the start week of a month,
    which is represented by week's start date
    """
    assert isinstance(year, int)
    assert isinstance(month, int)
    assert year > 0
    assert 1 <= month <= 12
    daily_start_date = datetime.date(year, month, 1)
    week_anchor_date = get_week_anchor_date(daily_start_date)

    # the week represented by anchor date is in previous month
    # so that the first week should be the next one
    if daily_start_date > week_anchor_date:
        return get_weekly_start_date(daily_start_date + timedelta(days=7))

    return get_weekly_start_date(daily_start_date)


# ===============================================================================================
#
#   series functions around date range's first period
#
#   1. get_prev_%(offset_granularity)s_start_date_from_%(date_range_granularity)s_located
#      the function would return the first date of unit date period,
#      which is away from the unit date period that date range's first period located
#      Args:
#          a_date: datetime.date
#          the date at above first period (probably not the beginning)
#
#          span_count: int
#          offset from located date period to compared located date period
#      Return:
#          start_date: datetime.date
#
# ===============================================================================================


# ==========================================================================================================
#
#   Series of functions which provide start period of a unit date period
#
#   The pattern of function name is like:
#   get_start_%(date_period_granularity)s_of_%(located_unit_period_granularity)s
#
#   Args:
#       a_date (datetime.date): the date located in a single date period,
#                               representing this period
#                               e.g. if a_date was '2024-06-20'
#                                    when granularity is 'daily': represent '2024-06-20'
#                                    when 'weekly': No.25 week of 2024according to ISO week date
#                                    when 'monthly': June 2024
#                                    when 'yearly': 2024
#
#   Return:
#       start_date (datetime.date): the start date which representing its start period of location
#                                   e.g. if the located unit period is June 2024
#                                        * date granularity is 'daily':
#                                          return '2024-06-01' which is the first day
#                                        * date granularity is 'weekly':
#                                          start week is No.23 week of 2024, its start day is '2024-06-03'
#                                          then return '2024-06-03'
#
# ==========================================================================================================


def get_start_daily_of_daily(a_date: datetime.date) -> datetime.date:
    return a_date


def get_start_daily_of_weekly(a_date: datetime.date) -> datetime.date:
    return get_weekly_start_date(a_date)


def get_start_daily_of_monthly(a_date: datetime.date) -> datetime.date:
    return datetime.date(a_date.year, a_date.month, 1)


def get_start_daily_of_yearly(a_date: datetime.date) -> datetime.date:
    return datetime.date(a_date.year, 1, 1)


def get_start_weekly_of_weekly(a_date: datetime.date) -> datetime.date:
    return get_weekly_start_date(a_date)


def get_start_weekly_of_monthly(a_date: datetime.date) -> datetime.date:
    week_anchor_date = get_week_anchor_date(a_date)
    return get_start_weekly_of_month(week_anchor_date.year, week_anchor_date.month)


def get_start_weekly_of_yearly(a_date: datetime.date) -> datetime.date:
    """
    special case that the month is January
    """
    week_anchor_date = get_week_anchor_date(a_date)
    return get_start_weekly_of_month(week_anchor_date.year, 1)


def get_start_monthly_of_monthly(a_date: datetime.date) -> datetime.date:
    return datetime.date(a_date.year, a_date.month, 1)


def get_start_monthly_of_yearly(a_date: datetime.date) -> datetime.date:
    return datetime.date(a_date.year, 1, 1)


# =================================================================================================
#
#   Series of functions which provide period's index of a unit date period
#
#   The pattern of function name is like:
#   get_%(date_period_granularity)s_index_of_%(located_unit_period_granularity)s
#
#   Args:
#       a_date (datetime.date): the date located in a single date period,
#                               representing this period
#                               e.g. if a_date was '2024-06-20'
#                                    when granularity is 'daily': represent '2024-06-20'
#                                    when 'weekly': No.25 week of 2024 according to ISO week date
#                                    when 'monthly': June 2024
#                                    when 'yearly': 2024
#
#   Return:
#       index (int): the index of the single date period in located unit date period
#                    e.g. if the located unit period is June 2024
#                         * date granularity is 'daily':
#                           return the index of given date from June 1st, 2024
#                         * date granularity is 'weekly':
#                           return the index of week (given date located) from No.25 week of 2024
#                           which is the start week of June 2024 according to ISO week date
#
# =================================================================================================


def get_daily_index_of_daily(a_date: datetime.date) -> int:  # NOQA
    return 0


def get_daily_index_of_weekly(a_date: datetime.date) -> int:
    start_date = get_start_daily_of_weekly(a_date)
    return (a_date - start_date).days


def get_daily_index_of_monthly(a_date: datetime.date) -> int:
    start_date = get_start_daily_of_monthly(a_date)
    return (a_date - start_date).days


def get_daily_index_of_yearly(a_date: datetime.date) -> int:
    start_date = get_start_daily_of_yearly(a_date)
    return (a_date - start_date).days


def get_weekly_index_of_weekly(a_date: datetime.date) -> int:  # NOQA
    return 0


def get_weekly_index_of_monthly(a_date: datetime.date) -> int:
    located_start_date = get_start_weekly_of_monthly(a_date)
    week_start_date = get_weekly_start_date(a_date)
    return (week_start_date - located_start_date).days // 7


def get_weekly_index_of_yearly(a_date: datetime.date) -> int:
    located_start_date = get_start_weekly_of_yearly(a_date)
    week_start_date = get_weekly_start_date(a_date)
    return (week_start_date - located_start_date).days // 7


def get_monthly_index_of_monthly(a_date: datetime.date) -> int:  # NOQA
    return 0


def get_monthly_index_of_yearly(a_date: datetime.date) -> int:
    located_start_date = get_start_monthly_of_yearly(a_date)
    return a_date.month - located_start_date.month


def get_yearly_index_of_yearly(a_date: datetime.date) -> int:  # NOQA
    return 0


def get_compared_start_daily_located_daily(a_date: datetime.date, offset: int) -> datetime.date:
    return a_date + timedelta(days=offset)


def get_compared_start_daily_located_weekly(a_date: datetime.date, offset: int) -> datetime.date:
    return get_start_daily_of_weekly(a_date) + timedelta(weeks=offset)


def get_compared_start_daily_located_monthly(a_date: datetime.date, offset: int) -> datetime.date:
    located_start_date = get_start_daily_of_monthly(a_date)
    located_year, located_month = located_start_date.year, located_start_date.month

    total_months = (located_year * 12 + located_month) + offset
    compared_year = total_months // 12
    compared_month = total_months % 12
    if compared_month == 0:
        compared_year -= 1
        compared_month = 12
    return datetime.date(compared_year, compared_month, 1)


def get_compared_start_daily_located_yearly(a_date: datetime.date, offset: int) -> datetime.date:
    located_start_date = get_start_daily_of_yearly(a_date)
    return datetime.date(located_start_date.year + offset, 1, 1)


def get_compared_start_weekly_located_weekly(a_date: datetime.date, offset: int) -> datetime.date:
    located_start_date = get_start_weekly_of_weekly(a_date)
    return located_start_date + timedelta(weeks=offset)


def get_daily_period_in_daily_by_index(a_date: datetime.date, index: int) -> datetime.date:  # NOQA
    if index != 0:
        raise ValueError
    return a_date


def get_daily_period_in_weekly_by_index(a_date: datetime.date, index: int) -> datetime.date:
    if not 0 <= index < 7:
        raise ValueError
    week_start_date = get_weekly_start_date(a_date)
    return week_start_date + timedelta(days=index)


def get_daily_period_in_monthly_by_index(a_date: datetime.date, index: int) -> datetime.date:
    total_months = (a_date.year * 12 + a_date.month) + 1
    next_month_start_date = datetime.date(total_months // 12, total_months % 12, 1)
    capacity = (next_month_start_date - timedelta(days=1)).day
    if not 0 <= index < capacity:
        raise ValueError

    month_start_date = datetime.date(a_date.year, a_date.month, 1)
    return month_start_date + timedelta(days=index)


def get_daily_period_in_yearly_by_index(a_date: datetime.date, index: int) -> datetime.date:
    year_start_date = datetime.date(a_date.year, 1, 1)
    year_end_date = datetime.date(a_date.year, 12, 31)
    capacity = (year_end_date - year_start_date).days + 1
    if not 0 <= index < capacity:
        raise ValueError

    year_start_date = datetime.date(a_date.year, 1, 1)
    return year_start_date + timedelta(days=index)


def get_weekly_period_in_weekly_by_index(a_date: datetime.date, index: int) -> datetime.date:  # NOQA
    if index != 0:
        raise ValueError
    return get_weekly_start_date(a_date)


def get_prev_monthly_start_date_from_weekly_located(a_date: datetime.date, span_count: int) -> datetime.date:
    week_anchor_date = get_week_anchor_date(a_date)
    prev_month_start_date = get_compared_start_daily_located_monthly(week_anchor_date, span_count)
    return get_start_weekly_of_month(prev_month_start_date.year, prev_month_start_date.month)


def get_weekly_period_in_monthly_by_index(a_date: datetime.date, index: int) -> datetime.date:
    anchor_date = get_week_anchor_date(a_date)
    week_start_date = get_start_weekly_of_month(anchor_date.year, anchor_date.month)
    start_date = week_start_date + timedelta(weeks=index)

    # each month has different amount of weeks
    # if index is out of month's capacity, raise exception
    week_anchor_date = get_week_anchor_date(start_date)
    if any([week_anchor_date.year != anchor_date.year, week_anchor_date.month != anchor_date.month]):
        raise ValueError
    return start_date


def get_prev_yearly_start_date_from_weekly_located(a_date: datetime.date, span_count: int) -> datetime.date:
    week_anchor_date = get_week_anchor_date(a_date)
    prev_year_start_date = get_compared_start_daily_located_yearly(week_anchor_date, span_count)
    return get_start_weekly_of_month(prev_year_start_date.year, 1)


def get_weekly_period_in_yearly_by_index(a_date: datetime.date, index: int) -> datetime.date:
    anchor_date = get_week_anchor_date(a_date)
    week_start_date = get_start_weekly_of_month(anchor_date.year, 1)
    start_date = week_start_date + timedelta(weeks=index)

    # each month has different amount of weeks
    # if index is out of month's capacity, raise exception
    week_anchor_date = get_week_anchor_date(start_date)
    if week_anchor_date.year != anchor_date.year:
        raise ValueError
    return start_date


def get_prev_monthly_start_date_from_monthly_located(a_date: datetime.date, span_count: int) -> datetime.date:
    located_start_date = get_start_monthly_of_monthly(a_date)
    return get_compared_start_daily_located_monthly(located_start_date, span_count)


def get_monthly_period_in_monthly_by_index(a_date: datetime.date, index: int) -> datetime.date:  # NOQA
    if index != 0:
        raise ValueError
    return datetime.date(a_date.year, a_date.month, 1)


def get_prev_yearly_start_date_from_monthly_located(a_date: datetime.date, span_count: int) -> datetime.date:
    located_start_date = get_start_monthly_of_yearly(a_date)
    return datetime.date(located_start_date.year - span_count, 1, 1)


def get_monthly_period_in_yearly_by_index(a_date: datetime.date, index: int) -> datetime.date:
    year_start_date = datetime.date(a_date.year, 1, 1)
    if not 0 <= index < 12:
        raise ValueError
    return datetime.date(year_start_date.year, year_start_date.month + index, 1)


def get_yearly_start_date_of_located_yearly(a_date: datetime.date) -> datetime.date:
    return datetime.date(a_date.year, 1, 1)


def get_prev_yearly_start_date_from_yearly_located(a_date: datetime.date, span_count: int) -> datetime.date:
    located_start_date = get_yearly_start_date_of_located_yearly(a_date)
    return datetime.date(located_start_date.year - span_count, 1, 1)


def get_yearly_period_in_yearly_by_index(a_date: datetime.date, index: int) -> datetime.date:
    if index != 0:
        raise ValueError
    return datetime.date(a_date.year, 1, 1)
