import datetime
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


class DateGranularity(Enum):
    """
    supported date granularity
    """
    DAILY = Daily()

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
