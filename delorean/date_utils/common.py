import datetime
from datetime import timedelta


def get_located_week_start_date(a_date: datetime.date) -> datetime.date:
    """
    get the start date of week which input date located
    """
    date_index = a_date.weekday()
    return a_date - timedelta(days=date_index)


def get_week_anchor_date(a_date: datetime.date) -> datetime.date:
    """
    The fourth day of week determine the year and month that week located
    """
    assert isinstance(a_date, datetime.date)
    start_date = get_located_week_start_date(a_date)
    return start_date + timedelta(days=3)


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
    month_first_date = datetime.date(year, month, 1)
    week_anchor_date = get_week_anchor_date(month_first_date)

    if month_first_date <= week_anchor_date:
        return get_located_week_start_date(month_first_date)
    return get_located_week_start_date(month_first_date + timedelta(days=7))


# ===============================================================================================
#
#   series functions around date range's first period
#
#   1. get_%(date_range_granularity)s_start_date_of_located_%(offset_granularity)s
#      first period (which granularity is named as date_range_granularity)
#      is at a rougher date period (which granularity is named as offset_granularity)
#
#      the function would return the first date of that located date period,
#      the first date depends on date range's granularity
#      e.g. when offset_granularity is 'monthly' and
#           * date range is daily, then first date would be the 1st of month
#           * date range is weekly, then first date would be
#             the 1st of month's 1st week (probably not 1st of month)
#      Args:
#          a_date: datetime.date
#          the date at above first period (probably not the beginning)
#      Return:
#          start_date: datetime.date
#
#   2. get_%(date_range_granularity)s_period_idx_of_located_%(offset_granularity)s
#      the function would return the index of date range's first period at the located period
#      e.g. when offset_granularity is 'monthly' and
#           * date range is daily, then the result would be the date index in located month
#           * date range is weekly, then the result would be the week index in located month
#      Args:
#          a_date: datetime.date
#          the date at above first period (probably not the beginning)
#      Return:
#          index: int
#
#   3. get_prev_%(offset_granularity)s_start_date_from_%(date_range_granularity)s_located
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

def get_daily_start_date_of_located_daily(a_date: datetime.date) -> datetime.date:
    return a_date


def get_daily_period_idx_of_located_daily(a_date: datetime.date) -> int:
    located_start_date = get_daily_start_date_of_located_daily(a_date)
    return (a_date - located_start_date).days


def get_prev_daily_start_date_from_daily_located(a_date: datetime.date, span_count: int) -> datetime.date:
    cur_start_date = a_date
    return cur_start_date - timedelta(days=span_count)


def get_daily_start_date_of_located_weekly(a_date: datetime.date) -> datetime.date:
    return get_located_week_start_date(a_date)


def get_daily_period_idx_of_located_weekly(a_date: datetime.date) -> int:
    located_start_date = get_daily_start_date_of_located_weekly(a_date)
    return (a_date - located_start_date).days


def get_prev_weekly_start_date_from_daily_located(a_date: datetime.date, span_count: int) -> datetime.date:
    cur_start_date = get_daily_start_date_of_located_weekly(a_date)
    return cur_start_date - timedelta(weeks=span_count)


def get_daily_start_date_of_located_monthly(a_date: datetime.date) -> datetime.date:
    return datetime.date(a_date.year, a_date.month, 1)


def get_daily_period_idx_of_located_monthly(a_date: datetime.date) -> int:
    located_start_date = get_daily_start_date_of_located_monthly(a_date)
    return (a_date - located_start_date).days


def get_prev_monthly_start_date_from_daily_located(a_date: datetime.date, span_count: int) -> datetime.date:
    located_start_date = get_daily_start_date_of_located_monthly(a_date)
    located_year, located_month = located_start_date.year, located_start_date.month

    total_months = (located_year * 12 + located_month) - span_count
    another_year = total_months // 12
    another_month = total_months % 12
    if another_month == 0:
        another_year -= 1
        another_month = 12
    return datetime.date(another_year, another_month, 1)


def get_daily_start_date_of_located_yearly(a_date: datetime.date) -> datetime.date:
    return datetime.date(a_date.year, 1, 1)


def get_daily_period_idx_of_located_yearly(a_date: datetime.date) -> int:
    located_start_date = get_daily_start_date_of_located_yearly(a_date)
    return (a_date - located_start_date).days


def get_prev_yearly_start_date_from_daily_located(a_date: datetime.date, span_count: int) -> datetime.date:
    located_start_date = get_daily_start_date_of_located_yearly(a_date)
    return datetime.date(located_start_date.year - span_count, 1, 1)


def get_weekly_start_date_of_located_weekly(a_date: datetime.date) -> datetime.date:
    return get_located_week_start_date(a_date)


def get_weekly_period_idx_of_located_weekly(a_date: datetime.date) -> int:  # NOQA
    return 0


def get_prev_weekly_start_date_from_weekly_located(a_date: datetime.date, span_count: int) -> datetime.date:
    located_start_date = get_weekly_start_date_of_located_weekly(a_date)
    return located_start_date - timedelta(weeks=span_count)


def get_weekly_start_date_of_located_monthly(a_date: datetime.date) -> datetime.date:
    week_anchor_date = get_week_anchor_date(a_date)
    return get_start_date_of_monthly_start_week(week_anchor_date.year, week_anchor_date.month)


def get_weekly_period_idx_of_located_monthly(a_date: datetime.date) -> int:
    located_start_date = get_weekly_start_date_of_located_monthly(a_date)
    week_start_date = get_located_week_start_date(a_date)
    return (week_start_date - located_start_date).days // 7


def get_prev_monthly_start_date_from_weekly_located(a_date: datetime.date, span_count: int) -> datetime.date:
    week_anchor_date = get_week_anchor_date(a_date)
    prev_month_start_date = get_prev_monthly_start_date_from_daily_located(week_anchor_date, span_count)
    return get_start_date_of_monthly_start_week(prev_month_start_date.year, prev_month_start_date.month)


def get_weekly_start_date_of_located_yearly(a_date: datetime.date) -> datetime.date:
    week_anchor_date = get_week_anchor_date(a_date)
    return get_start_date_of_monthly_start_week(week_anchor_date.year, 1)


def get_weekly_period_idx_of_located_yearly(a_date: datetime.date) -> int:
    located_start_date = get_weekly_start_date_of_located_yearly(a_date)
    week_start_date = get_located_week_start_date(a_date)
    return (week_start_date - located_start_date).days // 7


def get_prev_yearly_start_date_from_weekly_located(a_date: datetime.date, span_count: int) -> datetime.date:
    week_anchor_date = get_week_anchor_date(a_date)
    prev_year_start_date = get_prev_yearly_start_date_from_daily_located(week_anchor_date, span_count)
    return get_start_date_of_monthly_start_week(prev_year_start_date.year, 1)


def get_monthly_start_date_of_located_monthly(a_date: datetime.date) -> datetime.date:
    return datetime.date(a_date.year, a_date.month, 1)


def get_monthly_period_idx_of_located_monthly(a_date: datetime.date) -> int:  # NOQA
    return 0


def get_prev_monthly_start_date_from_monthly_located(a_date: datetime.date, span_count: int) -> datetime.date:
    located_start_date = get_monthly_start_date_of_located_monthly(a_date)
    return get_prev_monthly_start_date_from_daily_located(located_start_date, span_count)


def get_monthly_start_date_of_located_yearly(a_date: datetime.date) -> datetime.date:
    return datetime.date(a_date.year, 1, 1)


def get_monthly_period_idx_of_located_yearly(a_date: datetime.date) -> int:
    located_start_date = get_monthly_start_date_of_located_yearly(a_date)
    return a_date.month - located_start_date.month


def get_prev_yearly_start_date_from_monthly_located(a_date: datetime.date, span_count: int) -> datetime.date:
    located_start_date = get_monthly_start_date_of_located_yearly(a_date)
    return datetime.date(located_start_date.year - span_count, 1, 1)


def get_yearly_start_date_of_located_yearly(a_date: datetime.date) -> datetime.date:
    return datetime.date(a_date.year, 1, 1)


def get_yearly_period_idx_of_located_yearly(a_date: datetime.date) -> int:  # NOQA
    return 0


def get_prev_yearly_start_date_from_yearly_located(a_date: datetime.date, span_count: int) -> datetime.date:
    located_start_date = get_yearly_start_date_of_located_yearly(a_date)
    return datetime.date(located_start_date.year - span_count, 1, 1)
