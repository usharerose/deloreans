"""
delorean.app

This module provides a component 'DeLorean' on core logic
"""
import datetime
from typing import Tuple


class DeLorean:

    def __init__(
        self,
        start_date: datetime.date,
        end_date: datetime.date,
        date_granularity: str,
        span_count: int,
        span_granularity: str,
    ):
        pass

    def get(self) -> Tuple[datetime.date, datetime.date]:
        pass
