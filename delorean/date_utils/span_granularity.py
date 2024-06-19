from enum import Enum


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
