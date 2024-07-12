"""
deloreans.app

This module provides a component 'DeLoreans' on core logic
"""
import datetime
from typing import Tuple

from .date_utils import (
    common as common_date_utils,
    DateGranularity,
    DateRange,
    DatePeriodOffset,
    OffsetGranularity,
    VALID_GRAINS_COMB,
)
from .date_utils.common import (
    GET_BASE_INDEX_FUNC_TEMPLATE,
    GET_COMPARED_LOCATED_PERIOD_FUNC_TEMPLATE,
    GET_DATE_WITH_INDEX_FUNC_TEMPLATE,
)
from .exceptions import (
    IndexOverflowError,
    START_DATE_OVERFLOW_ERROR_MSG,
    UNREGISTERED_DATE_GRANULARITY_TEMPLATE,
    UNREGISTERED_GRANULARITY_COMBO_TEMPLATE,
)


class DeLoreans:

    def __init__(
        self,
        start_date: datetime.date,
        end_date: datetime.date,
        date_granularity: DateGranularity,
        offset: int,
        offset_granularity: OffsetGranularity,
        firstweekday: int = 0,
    ) -> None:
        self._date_range = DateRange(
            start_date,
            end_date,
            date_granularity,
            firstweekday,
        )
        self._date_period_offset = DatePeriodOffset(offset, offset_granularity)
        self._validate_grain_comb()
        self._date_grain_name = date_granularity.name.lower()
        self._offset_grain_name = offset_granularity.name.lower()

    def _validate_grain_comb(self) -> None:
        date_granularity = self._date_range.date_granularity
        offset_granularity = self._date_period_offset.offset_granularity
        if date_granularity not in VALID_GRAINS_COMB:
            raise ValueError(
                UNREGISTERED_DATE_GRANULARITY_TEMPLATE.format(
                    date_granularity=date_granularity,
                )
            )
        valid_offset_granularity = VALID_GRAINS_COMB[date_granularity]
        if offset_granularity not in valid_offset_granularity:
            raise ValueError(
                UNREGISTERED_GRANULARITY_COMBO_TEMPLATE.format(
                    offset_granularity=offset_granularity,
                    date_granularity=date_granularity,
                )
            )

    def _get_start_period_index(self) -> int:
        if self._date_period_offset.offset_granularity == OffsetGranularity.PERIODIC:
            offset_grain_name = self._date_grain_name
        else:
            offset_grain_name = self._offset_grain_name

        try:
            func = getattr(
                common_date_utils,
                GET_BASE_INDEX_FUNC_TEMPLATE.format(
                    date_granularity_name=self._date_grain_name,
                    offset_granularity_name=offset_grain_name,
                )
            )
        except AttributeError:
            raise NotImplementedError
        return func(
            self._date_range.start_date,
            firstweekday=self._date_range.firstweekday,
        )

    def _get_compared_located_period_start_date(self) -> datetime.date:
        if self._date_period_offset.offset_granularity == OffsetGranularity.PERIODIC:
            offset_grain_name = self._date_grain_name
            given_date_range_length = self._date_range.date_granularity.get_date_range_length(
                self._date_range.start_date,
                self._date_range.end_date,
            )
            offset = int(self._date_period_offset.offset * given_date_range_length)
        else:
            offset_grain_name = self._offset_grain_name
            offset = self._date_period_offset.offset

        try:
            func = getattr(
                common_date_utils,
                GET_COMPARED_LOCATED_PERIOD_FUNC_TEMPLATE.format(
                    date_granularity_name=self._date_grain_name,
                    offset_granularity_name=offset_grain_name,
                )
            )
        except AttributeError:
            raise NotImplementedError
        return func(
            self._date_range.start_date,
            offset,
            firstweekday=self._date_range.firstweekday,
        )

    def _get_compared_start_date(
        self,
        located_period_start_date: datetime.date,
        period_index: int,
    ) -> datetime.date:
        if self._date_period_offset.offset_granularity == OffsetGranularity.PERIODIC:
            offset_grain_name = self._date_grain_name
        else:
            offset_grain_name = self._offset_grain_name

        try:
            func = getattr(
                common_date_utils,
                GET_DATE_WITH_INDEX_FUNC_TEMPLATE.format(
                    date_granularity_name=self._date_grain_name,
                    offset_granularity_name=offset_grain_name,
                )
            )
        except AttributeError:
            raise NotImplementedError
        return func(
            located_period_start_date,
            period_index,
            firstweekday=self._date_range.firstweekday,
        )

    def get(self) -> Tuple[datetime.date, datetime.date]:
        """
        1. get the start date of compared date range
           1.1 get the index of given date range's start period in offset-granularity-unit date period
           1.2 get the start date-granularity period in away offset-granularity-unit date period
           1.3 get the date period which is away from the above period as compared date range's start date

        2. get the end date of compared date range
           2.1 get the length of given date range
           2.2 get the end date away from compared date range's start date with above length
               as compared date range's end date
        """
        start_period_index = self._get_start_period_index()
        base_start_date = self._get_compared_located_period_start_date()
        try:
            compared_start_date = self._get_compared_start_date(
                base_start_date,
                start_period_index,
            )
        except IndexOverflowError:
            raise ValueError(START_DATE_OVERFLOW_ERROR_MSG)

        date_granularity = self._date_range.date_granularity
        given_date_range_length = date_granularity.get_date_range_length(
            self._date_range.start_date,
            self._date_range.end_date,
            self._date_range.firstweekday,
        )
        compared_end_date = date_granularity.get_end_date(
            compared_start_date,
            given_date_range_length,
            self._date_range.firstweekday
        )

        return compared_start_date, compared_end_date
