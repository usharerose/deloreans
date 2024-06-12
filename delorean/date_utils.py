"""
delorean.date_utils

This module provides components on date-related parameters management
"""
import datetime
from enum import Enum


class DateGranularity(Enum):
    """
    supported date granularity
    """
    DAILY = 'daily'

    def validate_date_completion(
        self,
        start_date: datetime.date,
        end_date: datetime.date,
    ) -> None:
        """
        validate date range completion according to the granularity

        Args:
            start_date (datetime.date): start of date range
            end_date (datetime.date): end of date range
        """
        try:
            validate_func = getattr(self, f'_validate_{self.value}')
        except AttributeError:
            raise NotImplementedError(
                f'Completion validation on {self.name} has not been implemented'
            )
        is_completion = validate_func(start_date, end_date)
        if not is_completion:
            raise

    @staticmethod
    def _validate_daily(
        start_date: datetime.date,  # NOQA
        end_date: datetime.date,  # NOQA
    ) -> bool:
        return True


class DateRange:

    def __init__(
        self,
        start_date: datetime.date,
        end_date: datetime.date,
        date_granularity: DateGranularity,
    ):
        self._start_date = start_date
        self._end_date = end_date
        self._date_granularity = date_granularity
        self._validate_date_type()
        self._validate_date_relativity()
        self._validate_date_granularity_type()
        self._date_granularity.validate_date_completion(
            self._start_date,
            self._end_date,
        )

    @property
    def start_date(self) -> datetime.date:
        return self._start_date

    @property
    def end_date(self) -> datetime.date:
        return self._end_date

    @property
    def date_granularity(self) -> DateGranularity:
        return self._date_granularity

    def _validate_date_type(self) -> None:
        """
        date parameters should be datetime.date
        """
        for a_date in (self._start_date, self._end_date):
            if not isinstance(a_date, datetime.date):
                raise ValueError(
                    f'Invalid date {a_date!r}, should be datetime.date'
                )

    def _validate_date_relativity(self) -> None:
        """
        end date should be equal or greater than start date
        """
        if self._end_date < self._start_date:
            raise ValueError(
                f'Invalid date range, '
                f'the end one {self._end_date} should be equal or greater than the start one {self._start_date}'
            )

    def _validate_date_granularity_type(self) -> None:
        """
        date granularity should be defined enum
        """
        if not isinstance(self._date_granularity, DateGranularity):
            raise ValueError(
                f'Invalid date granularity {self._date_granularity!r}, should be DateGranularity'
            )


class SpanGranularity(Enum):
    """
    supported date span granularity
    """
    DAILY = 'daily'


class DateSpan:

    def __init__(
        self,
        span_count: int,
        span_granularity: SpanGranularity,
    ) -> None:
        self._span_count = span_count
        self._span_granularity = span_granularity
        self._validate_span_count()
        self._validate_span_granularity_type()

    @property
    def span_count(self) -> int:
        return self._span_count

    @property
    def span_granularity(self) -> SpanGranularity:
        return self._span_granularity

    def _validate_span_count(self) -> None:
        """
        validate input span count on
        1. data type which should be integer
        2. value which should be positive
        """
        if not isinstance(self._span_count, int):
            raise TypeError(
                f'Invalid span count {self._span_count!r}, should be int'
            )
        if self._span_count < 0:
            raise ValueError(
                f'Invalid span count {self._span_count!r}, should be positive'
            )

    def _validate_span_granularity_type(self) -> None:
        """
        span granularity should be defined enum
        """
        if not isinstance(self._span_granularity, SpanGranularity):
            raise TypeError(
                f'Invalid span granularity {self._span_granularity!r}, should be SpanGranularity'
            )
