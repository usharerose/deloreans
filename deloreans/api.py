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
) -> Tuple[datetime.date, datetime.date]:
    component = DeLoreans(
        start_date,
        end_date,
        date_granularity,
        offset,
        offset_granularity,
    )
    return component.get()
