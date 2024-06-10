"""
delorean.api

This module implements the DeLorean API
"""
import datetime
from typing import Tuple

from delorean.app import DeLorean


def get(
    start_date: datetime.date,
    end_date: datetime.date,
    date_granularity: str,
    span_count: int,
    span_granularity: str,
) -> Tuple[datetime.date, datetime.date]:
    component = DeLorean(
        start_date,
        end_date,
        date_granularity,
        span_count,
        span_granularity,
    )
    return component.get()
