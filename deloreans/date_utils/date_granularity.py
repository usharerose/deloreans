import datetime
from datetime import timedelta
from enum import Enum

from deloreans.date_utils.common import (
    get_weekly_start_date,
    get_weeks_offset,
    get_start_monthly_of_monthly,
    get_compared_start_monthly_located_monthly,
    get_start_yearly_of_yearly,
    get_compared_start_yearly_located_yearly,
)
from ..exceptions import PARTIAL_DATE_RANGE_TEMPLATE


class BaseGranularity:

    @classmethod
    def validate_date_completion(
        cls,
        start_date: datetime.date,
        end_date: datetime.date,
        firstweekday: int = 0,
    ) -> bool:
        if start_date > end_date:
            raise ValueError

        is_start_date = cls._is_start_date(start_date, firstweekday)
        is_end_date = cls._is_end_date(end_date, firstweekday)
        if all([is_start_date, is_end_date]):
            return True
        return False

    @staticmethod
    def _is_start_date(
        a_date: datetime.date,
        firstweekday: int = 0,
    ) -> bool:
        """
        Whether the given date is the start date of granularity-unit date period or not
        """
        raise NotImplementedError

    @staticmethod
    def _is_end_date(
        a_date: datetime.date,
        firstweekday: int = 0,
    ) -> bool:
        """
        Whether the given date is the end date of granularity-unit date period or not
        """
        raise NotImplementedError

    @classmethod
    def get_date_range_length(
        cls,
        start_date: datetime.date,
        end_date: datetime.date,
        firstweekday: int = 0,
    ) -> int:
        """
        Provide the count of date periods with given granularity
        e.g. 1 day, 2 weeks, 3 months, 4 years
        """
        if start_date > end_date:
            raise ValueError
        return cls._get_date_range_length(start_date, end_date, firstweekday)

    @staticmethod
    def _get_date_range_length(
        start_date: datetime.date,
        end_date: datetime.date,
        firstweekday: int = 0,
    ) -> int:
        raise NotImplementedError

    @classmethod
    def get_end_date(
        cls,
        start_date: datetime.date,
        date_range_length: int,
        firstweekday: int = 0,
    ) -> datetime.date:
        if not cls._is_start_date(
            start_date,
            firstweekday,
        ):
            raise ValueError
        if date_range_length < 1:
            raise ValueError

        return cls._get_end_date(start_date, date_range_length)

    @staticmethod
    def _get_end_date(
        start_date: datetime.date,
        date_range_length: int,
    ) -> datetime.date:
        raise NotImplementedError


class Daily(BaseGranularity):

    @staticmethod
    def _is_start_date(
        a_date: datetime.date,
        firstweekday: int = 0,
    ) -> bool:
        return True

    @staticmethod
    def _is_end_date(
        a_date: datetime.date,
        firstweekday: int = 0,
    ) -> bool:
        return True

    @staticmethod
    def _get_date_range_length(
        start_date: datetime.date,
        end_date: datetime.date,
        firstweekday: int = 0,
    ) -> int:
        return (end_date - start_date).days + 1

    @staticmethod
    def _get_end_date(
        start_date: datetime.date,
        date_range_length: int,
    ) -> datetime.date:
        return start_date + timedelta(days=date_range_length - 1)


class Weekly(BaseGranularity):

    @staticmethod
    def _is_start_date(
        a_date: datetime.date,
        firstweekday: int = 0,
    ) -> bool:
        week_start_date = get_weekly_start_date(a_date, firstweekday)
        return a_date == week_start_date

    @staticmethod
    def _is_end_date(
        a_date: datetime.date,
        firstweekday: int = 0,
    ) -> bool:
        next_week_start_date = get_weekly_start_date(
            a_date + timedelta(days=7),
            firstweekday,
        )
        week_end_date = next_week_start_date + timedelta(days=-1)
        return a_date == week_end_date

    @staticmethod
    def _get_date_range_length(
        start_date: datetime.date,
        end_date: datetime.date,
        firstweekday: int = 0,
    ) -> int:
        return get_weeks_offset(start_date, end_date, firstweekday) + 1

    @staticmethod
    def _get_end_date(
        start_date: datetime.date,
        date_range_length: int,
    ) -> datetime.date:
        exceeded_week_start_date = start_date + timedelta(weeks=date_range_length)
        return exceeded_week_start_date + timedelta(days=-1)


class Monthly(BaseGranularity):

    @staticmethod
    def _is_start_date(
        a_date: datetime.date,
        firstweekday: int = 0,
    ) -> bool:
        month_start_date = get_start_monthly_of_monthly(a_date)
        return a_date == month_start_date

    @staticmethod
    def _is_end_date(
        a_date: datetime.date,
        firstweekday: int = 0,
    ) -> bool:
        exceeded_month_start_date = get_compared_start_monthly_located_monthly(a_date, 1)
        month_end_date = exceeded_month_start_date + timedelta(days=-1)
        return a_date == month_end_date

    @staticmethod
    def _get_date_range_length(
        start_date: datetime.date,
        end_date: datetime.date,
        firstweekday: int = 0,
    ) -> int:
        start_total_months = 12 * start_date.year + start_date.month
        end_total_months = 12 * end_date.year + end_date.month
        return end_total_months - start_total_months + 1

    @staticmethod
    def _get_end_date(
        start_date: datetime.date,
        date_range_length: int,
    ) -> datetime.date:
        exceeded_month_start_date = get_compared_start_monthly_located_monthly(
            start_date,
            date_range_length,
        )
        month_end_date = exceeded_month_start_date + timedelta(days=-1)
        return month_end_date


class Yearly(BaseGranularity):

    @staticmethod
    def _is_start_date(
        a_date: datetime.date,
        firstweekday: int = 0,
    ) -> bool:
        year_start_date = get_start_yearly_of_yearly(a_date)
        return a_date == year_start_date

    @staticmethod
    def _is_end_date(
        a_date: datetime.date,
        firstweekday: int = 0,
    ) -> bool:
        exceeded_start_date = get_compared_start_yearly_located_yearly(a_date, 1)
        year_end_date = exceeded_start_date + timedelta(days=-1)
        return a_date == year_end_date

    @staticmethod
    def _get_date_range_length(
        start_date: datetime.date,
        end_date: datetime.date,
        firstweekday: int = 0,
    ) -> int:
        return end_date.year - start_date.year + 1

    @staticmethod
    def _get_end_date(
        start_date: datetime.date,
        date_range_length: int,
    ) -> datetime.date:
        exceeded_start_date = get_compared_start_yearly_located_yearly(
            start_date,
            date_range_length,
        )
        return exceeded_start_date + timedelta(days=-1)


class DateGranularity(Enum):
    """
    supported date granularity
    """
    DAILY = Daily
    WEEKLY = Weekly
    MONTHLY = Monthly
    YEARLY = Yearly

    def validate_date_completion(
        self,
        start_date: datetime.date,
        end_date: datetime.date,
        firstweekday: int = 0,
    ) -> None:
        is_completion = self.value.validate_date_completion(
            start_date,
            end_date,
            firstweekday,
        )
        if not is_completion:
            raise ValueError(
                PARTIAL_DATE_RANGE_TEMPLATE.format(
                    start_date=start_date,
                    end_date=end_date,
                    date_granularity_name=self.name.lower(),
                )
            )

    def get_date_range_length(
        self,
        start_date: datetime.date,
        end_date: datetime.date,
        firstweekday: int = 0,
    ) -> int:
        return self.value.get_date_range_length(
            start_date,
            end_date,
            firstweekday,
        )

    def get_end_date(
        self,
        start_date: datetime.date,
        date_range_length: int,
        firstweekday: int = 0,
    ) -> datetime.date:
        return self.value.get_end_date(
            start_date,
            date_range_length,
            firstweekday,
        )
