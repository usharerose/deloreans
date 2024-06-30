"""
deloreans.api

This module implements the DeLoreans API
"""
import datetime
from typing import Tuple

from deloreans.app import DeLoreans
from deloreans.date_utils import DateGranularity, OffsetGranularity


def get(
    start_date: datetime.date,
    end_date: datetime.date,
    date_granularity: DateGranularity,
    offset: int,
    offset_granularity: OffsetGranularity,
    firstweekday: int = 0,
) -> Tuple[datetime.date, datetime.date]:
    """
    provide compared date range according to given parameters

    Args:
        start_date (datetime.date): start date of date range
        end_date (datetime.date): end date of date range
        date_granularity (DateGranularity): granularity of date range, e.g. daily, weekly
        offset (int): away from given date range, to the future when positive
        offset_granularity (OffsetGranularity): granularity of offset period, e.g. year-over-year
        firstweekday (int): define the start date's weekday of week, 0 is Monday, 6 is Sunday

    Returns:
        compared_start_date (datetime.date): start date of compared date range
        compared_end_date (datetime.date): end date of compared date range
    """
    component = DeLoreans(
        start_date,
        end_date,
        date_granularity,
        offset,
        offset_granularity,
        firstweekday,
    )
    return component.get()
