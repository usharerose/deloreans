"""
delorean.app

This module provides a component 'DeLorean' on core logic
"""
import datetime
from typing import Tuple

from delorean.date_utils import (
    DateGranularity,
    DateRange,
    DatePeriodOffset,
    OffsetGranularity,
    VALID_GRAINS_COMB,
)
import delorean.date_utils.common as common_date_utils


class DeLorean:

    def __init__(
        self,
        start_date: datetime.date,
        end_date: datetime.date,
        date_granularity: DateGranularity,
        offset: int,
        offset_granularity: OffsetGranularity,
    ) -> None:
        self._date_range = DateRange(start_date, end_date, date_granularity)
        self._date_period_offset = DatePeriodOffset(offset, offset_granularity)
        self._validate_grain_comb()
        self._date_grain_name = date_granularity.name.lower()
        self._offset_grain_name = offset_granularity.name.lower()

    def _validate_grain_comb(self) -> None:
        date_granularity = self._date_range.date_granularity
        offset_granularity = self._date_period_offset.offset_granularity

        if date_granularity not in VALID_GRAINS_COMB:
            raise ValueError(
                f"Date granularity {date_granularity!r} is not registered "
                f"in granularity combinations."
            )
        valid_offset_granularity = VALID_GRAINS_COMB[date_granularity]
        if offset_granularity not in valid_offset_granularity:
            raise ValueError(
                f"Invalid offset granularity {offset_granularity!r} "
                f"when date granularity is {date_granularity!r}"
            )

    def _get_start_period_index(self) -> int:
        try:
            func = getattr(
                common_date_utils,
                f'get_{self._date_grain_name}_index_of_{self._offset_grain_name}',
            )
        except AttributeError:
            raise NotImplementedError(
                f'{self._date_grain_name} period\'s index in {self._offset_grain_name} period '
                f'has not been implemented'
            )
        return func(self._date_range.start_date)

    def _get_compared_located_period_start_date(self) -> datetime.date:
        try:
            func = getattr(
                common_date_utils,
                f'get_compared_start_{self._date_grain_name}_located_{self._offset_grain_name}',
            )
        except AttributeError:
            raise NotImplementedError(
                f'start {self._date_grain_name} period in {self._offset_grain_name} period '
                f'has not been implemented'
            )
        return func(self._date_range.start_date, self._date_period_offset.offset)

    def _get_compared_start_date(
        self,
        located_period_start_date: datetime.date,
        period_index: int,
    ) -> datetime.date:
        try:
            func = getattr(
                common_date_utils,
                f'get_{self._date_grain_name}_with_index_in_{self._offset_grain_name}',
            )
        except AttributeError:
            raise NotImplementedError(
                f'{self._date_grain_name} period with index in {self._offset_grain_name} period '
                f'has not been implemented'
            )
        return func(located_period_start_date, period_index)

    def get(self) -> Tuple[datetime.date, datetime.date]:
        start_period_index = self._get_start_period_index()
        base_start_date = self._get_compared_located_period_start_date()
        compared_start_date = self._get_compared_start_date(
            base_start_date,
            start_period_index,
        )

        date_granularity = self._date_range.date_granularity
        given_date_range_length = date_granularity.get_date_range_length(
            self._date_range.start_date,
            self._date_range.end_date,
        )
        compared_end_date = date_granularity.get_end_date(
            compared_start_date,
            given_date_range_length,
        )

        return compared_start_date, compared_end_date
