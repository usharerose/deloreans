import datetime

from deloreans.date_utils.date_granularity import DateGranularity


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
