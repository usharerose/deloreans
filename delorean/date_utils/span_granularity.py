import datetime
from datetime import timedelta
from enum import Enum

from delorean.date_utils.common import (
    get_start_weekly_of_month,
    get_week_anchor_date,
    get_weeks_offset,
)
from delorean.date_utils.date_range import DateRange


class BaseGranularity:

    name: str

    def get_first_period_index(
        self,
        date_range: DateRange,
    ) -> int:
        """
        get the index of date range's first period inner the span-granularity date period
        can only support finer DateGranularity than SpanGranularity

        private methods should be named as '_get_%(date_granularity_name)s_period_index'
        """
        granularity_name = date_range.date_granularity.name.lower()
        try:
            func = getattr(self, f'_get_{granularity_name}_period_index')
        except AttributeError:
            raise NotImplementedError(
                f'get_index on {granularity_name} has not been implemented'
            )
        return func(date_range.start_date)

    def get_first_period_located_start_date(
        self,
        date_range: DateRange
    ) -> datetime.date:
        """
        get the start date of date period that date range's first period located
        can only support finer DateGranularity than SpanGranularity

        private methods should be named as '_get_%(date_granularity_name)s_located_start_date'
        """
        granularity_name = date_range.date_granularity.name.lower()
        try:
            func = getattr(self, f'_get_{granularity_name}_located_start_date')
        except AttributeError:
            raise NotImplementedError(
                f'get_location on {granularity_name} has not been implemented'
            )
        return func(date_range.start_date)


class Daily(BaseGranularity):

    name = 'daily'

    def _get_daily_period_index(  # NOQA
        self,
        a_date: datetime.date,  # NOQA
    ) -> int:
        return 0

    def _get_daily_located_start_date(  # NOQA
        self,
        a_date: datetime.date,
    ) -> datetime.date:
        return a_date


class Weekly(BaseGranularity):

    name = 'weekly'

    def _get_daily_period_index(  # NOQA
        self,
        a_date: datetime.date,  # NOQA
    ) -> int:
        return a_date.weekday()

    def _get_weekly_period_index(  # NOQA
        self,
        a_date: datetime.date,  # NOQA
    ) -> int:
        return 0

    def _get_daily_located_start_date(  # NOQA
        self,
        a_date: datetime.date,
    ) -> datetime.date:
        weekday = a_date.weekday()
        return a_date - timedelta(days=weekday)

    def _get_weekly_located_start_date(  # NOQA
        self,
        a_date: datetime.date,
    ) -> datetime.date:
        return a_date


class Monthly(BaseGranularity):

    name = 'monthly'

    def _get_daily_period_index(  # NOQA
        self,
        a_date: datetime.date,  # NOQA
    ) -> int:
        return a_date.day - 1

    def _get_weekly_period_index(  # NOQA
        self,
        a_date: datetime.date,  # NOQA
    ) -> int:
        key_date = get_week_anchor_date(a_date)
        first_week_start_date = get_start_weekly_of_month(key_date.year, key_date.month)
        return get_weeks_offset(first_week_start_date, a_date)

    def _get_monthly_period_index(  # NOQA
        self,
        a_date: datetime.date,  # NOQA
    ) -> int:
        return 0

    def _get_daily_located_start_date(  # NOQA
        self,
        a_date: datetime.date,
    ) -> datetime.date:
        return datetime.date(a_date.year, a_date.month, 1)

    def _get_weekly_located_start_date(  # NOQA
        self,
        a_date: datetime.date,
    ) -> datetime.date:
        key_date = get_week_anchor_date(a_date)
        first_week_start_date = get_start_weekly_of_month(key_date.year, key_date.month)
        return first_week_start_date

    def _get_monthly_located_start_date(  # NOQA
        self,
        a_date: datetime.date,
    ) -> datetime.date:
        return a_date


class Yearly(BaseGranularity):

    name = 'yearly'

    def _get_daily_period_index(  # NOQA
        self,
        a_date: datetime.date,  # NOQA
    ) -> int:
        return (a_date - datetime.date(a_date.year, 1, 1)).days

    def _get_weekly_period_index(  # NOQA
        self,
        a_date: datetime.date,  # NOQA
    ) -> int:
        key_date = get_week_anchor_date(a_date)
        first_week_start_date = get_start_weekly_of_month(key_date.year, 1)
        return get_weeks_offset(first_week_start_date, a_date)

    def _get_monthly_period_index(  # NOQA
        self,
        a_date: datetime.date,  # NOQA
    ) -> int:
        return a_date.month - 1

    def _get_yearly_period_index(  # NOQA
        self,
        a_date: datetime.date,  # NOQA
    ) -> int:
        return 0

    def _get_daily_located_start_date(  # NOQA
        self,
        a_date: datetime.date,
    ) -> datetime.date:
        return datetime.date(a_date.year, 1, 1)

    def _get_weekly_located_start_date(  # NOQA
        self,
        a_date: datetime.date,
    ) -> datetime.date:
        key_date = get_week_anchor_date(a_date)
        first_week_start_date = get_start_weekly_of_month(key_date.year, 1)
        return first_week_start_date

    def _get_monthly_located_start_date(  # NOQA
        self,
        a_date: datetime.date,
    ) -> datetime.date:
        return datetime.date(a_date.year, 1, 1)

    def _get_yearly_located_start_date(  # NOQA
        self,
        a_date: datetime.date,
    ) -> datetime.date:
        return a_date


class Periodic(BaseGranularity):

    name = 'periodic'

    def _get_daily_period_index(  # NOQA
        self,
        a_date: datetime.date,  # NOQA
    ) -> int:
        return 0

    def _get_weekly_period_index(  # NOQA
        self,
        a_date: datetime.date,  # NOQA
    ) -> int:
        return 0

    def _get_monthly_period_index(  # NOQA
        self,
        a_date: datetime.date,  # NOQA
    ) -> int:
        return 0

    def _get_yearly_period_index(  # NOQA
        self,
        a_date: datetime.date,  # NOQA
    ) -> int:
        return 0

    def _get_daily_located_start_date(  # NOQA
        self,
        a_date: datetime.date,
    ) -> datetime.date:
        return a_date

    def _get_weekly_located_start_date(  # NOQA
        self,
        a_date: datetime.date,
    ) -> datetime.date:
        key_date = get_week_anchor_date(a_date)
        first_week_start_date = get_start_weekly_of_month(key_date.year, 1)
        return a_date

    def _get_monthly_located_start_date(  # NOQA
        self,
        a_date: datetime.date,
    ) -> datetime.date:
        return a_date

    def _get_yearly_located_start_date(  # NOQA
        self,
        a_date: datetime.date,
    ) -> datetime.date:
        return a_date


class SpanGranularity(Enum):
    """
    supported date span granularity
    """
    DAILY = Daily()
    WEEKLY = Weekly()
    MONTHLY = Monthly()
    YEARLY = Yearly()
    PERIODIC = Periodic()


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
