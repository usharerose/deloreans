"""
delorean.api

This module implements the DeLorean API
"""
import datetime
from typing import Tuple

from delorean.app import DeLorean
from delorean.date_utils import DateGranularity, SpanGranularity


def get(
    start_date: datetime.date,
    end_date: datetime.date,
    date_granularity: DateGranularity,
    span_count: int,
    span_granularity: SpanGranularity,
) -> Tuple[datetime.date, datetime.date]:
    component = DeLorean(
        start_date,
        end_date,
        date_granularity,
        span_count,
        span_granularity,
    )
    return component.get()
