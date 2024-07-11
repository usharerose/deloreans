import datetime

from deloreans.date_utils.date_granularity import DateGranularity
from ..exceptions import (
    INVALID_DATA_TYPE_TEMPLATE,
    INVALID_DATE_RANGE_TEMPLATE,
    INVALID_WEEKDAY_ERROR_MSG,
)


class DateRange:

    def __init__(
        self,
        start_date: datetime.date,
        end_date: datetime.date,
        date_granularity: DateGranularity,
        firstweekday: int = 0,
    ):
        self._start_date = start_date
        self._end_date = end_date
        self._date_granularity = date_granularity
        self._firstweekday = firstweekday
        self._validate_firstweekday()
        self._validate_date_type()
        self._validate_date_relativity()
        self._validate_date_granularity_type()
        self._date_granularity.validate_date_completion(
            self._start_date,
            self._end_date,
            self._firstweekday,
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

    @property
    def firstweekday(self) -> int:
        return self._firstweekday

    def _validate_date_type(self) -> None:
        """
        date parameters should be datetime.date
        """
        for a_date in (self._start_date, self._end_date):
            if not isinstance(a_date, datetime.date):
                raise ValueError(
                    INVALID_DATA_TYPE_TEMPLATE.format(
                        input_args=a_date,
                        input_dtype=type(a_date),
                        dtype=datetime.date,
                    )
                )

    def _validate_date_relativity(self) -> None:
        """
        end date should be equal or greater than start date
        """
        if self._end_date < self._start_date:
            raise ValueError(
                INVALID_DATE_RANGE_TEMPLATE.format(
                    end_date=self._end_date,
                    start_date=self._start_date,
                )
            )

    def _validate_date_granularity_type(self) -> None:
        """
        date granularity should be defined enum
        """
        if not isinstance(self._date_granularity, DateGranularity):
            raise ValueError(
                INVALID_DATA_TYPE_TEMPLATE.format(
                    input_args=self._date_granularity,
                    input_dtype=type(self._date_granularity),
                    dtype=DateGranularity,
                )
            )

    def _validate_firstweekday(self):
        if not isinstance(self._firstweekday, int):
            raise TypeError(
                INVALID_DATA_TYPE_TEMPLATE.format(
                    input_args=self._firstweekday,
                    input_dtype=type(self._firstweekday),
                    dtype=int,
                )
            )
        if not 0 <= self._firstweekday < 7:
            raise ValueError(INVALID_WEEKDAY_ERROR_MSG)
