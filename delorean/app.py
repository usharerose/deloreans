"""
delorean.app

This module provides a component 'DeLorean' on core logic
"""
import datetime
from typing import Tuple

from delorean.date_utils import (
    DateGranularity,
    DateRange,
    DateSpan,
    SpanGranularity,
    VALID_GRAINS_COMB,
)


class DeLorean:

    def __init__(
        self,
        start_date: datetime.date,
        end_date: datetime.date,
        date_granularity: DateGranularity,
        span_count: int,
        span_granularity: SpanGranularity,
    ) -> None:
        self._date_range = DateRange(start_date, end_date, date_granularity)
        self._date_span = DateSpan(span_count, span_granularity)
        self._validate_grain_comb()

    def _validate_grain_comb(self) -> None:
        date_granularity = self._date_range.date_granularity
        span_granularity = self._date_span.span_granularity

        if date_granularity not in VALID_GRAINS_COMB:
            raise ValueError(
                f"Date granularity {date_granularity!r} is not registered "
                f"in granularity combinations."
            )
        valid_span_granularity = VALID_GRAINS_COMB[date_granularity]
        if span_granularity not in valid_span_granularity:
            raise ValueError(
                f"Invalid span granularity {span_granularity!r} "
                f"when date granularity is {date_granularity!r}"
            )

    def get(self) -> Tuple[datetime.date, datetime.date]:
        pass
