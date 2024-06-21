import datetime
from datetime import timedelta
from enum import Enum


class BaseGranularity:

    name: str

    def validate_date_completion(
        self,
        start_date: datetime.date,
        end_date: datetime.date,
    ) -> bool:
        is_partial_start = self._is_partial_start(start_date)
        is_partial_end = self._is_partial_end(end_date)
        if any([is_partial_start, is_partial_end]):
            return False
        return True

    def _is_partial_start(self, start_date: datetime.date) -> bool:
        raise NotImplementedError

    def _is_partial_end(self, end_date: datetime.date) -> bool:
        raise NotImplementedError

    def get_date_range_size(
        self,
        start_date: datetime.date,
        end_date: datetime.date,
    ) -> int:
        raise NotImplementedError


class Daily(BaseGranularity):

    name = 'daily'

    def _is_partial_start(self, start_date: datetime.date) -> bool:
        return False

    def _is_partial_end(self, end_date: datetime.date) -> bool:
        return False

    def get_date_range_size(
        self,
        start_date: datetime.date,
        end_date: datetime.date,
    ) -> int:
        return (end_date - start_date).days + 1


class Weekly(BaseGranularity):

    name = 'weekly'

    def _is_partial_start(self, start_date: datetime.date) -> bool:
        return not start_date.weekday() == 0

    def _is_partial_end(self, end_date: datetime.date) -> bool:
        return not end_date.weekday() == 6

    def get_date_range_size(
        self,
        start_date: datetime.date,
        end_date: datetime.date,
    ) -> int:
        return int(((end_date - start_date).days + 1) / 7)


class Monthly(BaseGranularity):

    name = 'monthly'

    def _is_partial_start(self, start_date: datetime.date) -> bool:
        return not start_date.day == 1

    def _is_partial_end(self, end_date: datetime.date) -> bool:
        year = end_date.year + (end_date.month + 1) // 12
        month = (end_date.month + 1) % 12
        next_month_first_day = datetime.date(year, month, 1)
        last_day = (next_month_first_day + timedelta(days=-1)).day
        return not end_date.day == last_day

    def get_date_range_size(
        self,
        start_date: datetime.date,
        end_date: datetime.date,
    ) -> int:
        start_year = start_date.year
        end_year = end_date.year
        if start_year == end_year:
            return end_date.month - start_date.month + 1

        year_diff = end_year - start_year - 1
        result = (12 - start_date.month + 1) + year_diff * 12 + end_date.month
        return result


class Yearly(BaseGranularity):

    name = 'yearly'

    def _is_partial_start(self, start_date: datetime.date) -> bool:
        return not (start_date.day == 1 and start_date.month == 1)

    def _is_partial_end(self, end_date: datetime.date) -> bool:
        return not (end_date.day == 31 and end_date.month == 12)

    def get_date_range_size(
        self,
        start_date: datetime.date,
        end_date: datetime.date,
    ) -> int:
        return end_date.year - start_date.year + 1


class DateGranularity(Enum):
    """
    supported date granularity
    """
    DAILY = Daily()
    WEEKLY = Weekly()
    MONTHLY = Monthly()
    YEARLY = Yearly()

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
        is_completion = self.value.validate_date_completion(start_date, end_date)
        if not is_completion:
            raise
