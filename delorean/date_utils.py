"""
delorean.date_utils

This module provides components on date-related parameters management
"""
import datetime
from enum import Enum
from typing import Iterable


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


def _strict_zip(*iterables: Iterable) -> Iterable:
    """
    refer to: https://peps.python.org/pep-0618/#reference-implementation
    can call zip() with keyword arguments 'strict' instead in python 3.10 or later

    which validates iterables lengths' consistency
    In this scenario, it is for making sure that
    each date granularity has registered their valid span granularity
    """
    if not iterables:
        yield
    iterators = tuple(iter(iterable) for iterable in iterables)
    items = []
    try:
        while True:
            items = []
            for iterator in iterators:
                items.append(next(iterator))
            yield tuple(items)
    except StopIteration:
        pass

    if items:
        processed_iters = len(items)
        plural = " " if processed_iters == 1 else "s 1-"
        msg = f"_strict_zip() argument {processed_iters + 1} is shorter than argument{plural}{processed_iters}"
        raise ValueError(msg)

    sentinel = object()
    for i, iterator in enumerate(iterators[1:], 1):
        if next(iterator, sentinel) is not sentinel:
            plural = " " if i == 1 else "s 1-"
            msg = f"_strict_zip() argument {i+1} is longer than argument{plural}{i}"
            raise ValueError(msg)


# Commonly, finer date range can offset with rougher span granularity
# Here is the collection of valid combinations
# Please register the valid span granularity when support new date granularity
VALID_GRAINS_COMB = dict(_strict_zip(
    [item for name, item in DateGranularity.__members__.items()],
    [
        {SpanGranularity.DAILY},
    ],
))
