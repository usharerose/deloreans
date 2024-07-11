from enum import Enum

from ..exceptions import INVALID_DATA_TYPE_TEMPLATE


class OffsetGranularity(Enum):
    """
    supported date offset granularity
    """
    DAILY = 'daily'
    WEEKLY = 'weekly'
    MONTHLY = 'monthly'
    YEARLY = 'yearly'
    PERIODIC = 'periodic'


class DatePeriodOffset:

    def __init__(
        self,
        offset: int,
        offset_granularity: OffsetGranularity,
    ) -> None:
        self._offset = offset
        self._offset_granularity = offset_granularity
        self._validate_offset()
        self._validate_offset_granularity_type()

    @property
    def offset(self) -> int:
        return self._offset

    @property
    def offset_granularity(self) -> OffsetGranularity:
        return self._offset_granularity

    def _validate_offset(self) -> None:
        if not isinstance(self._offset, int):
            raise TypeError(
                INVALID_DATA_TYPE_TEMPLATE.format(
                    input_args=self._offset,
                    input_dtype=type(self._offset),
                    dtype=int,

                )
            )

    def _validate_offset_granularity_type(self) -> None:
        """
        offset granularity should be defined enum
        """
        if not isinstance(self._offset_granularity, OffsetGranularity):
            raise TypeError(
                INVALID_DATA_TYPE_TEMPLATE.format(
                    input_args=self._offset_granularity,
                    input_dtype=type(self._offset_granularity),
                    dtype=OffsetGranularity,
                )
            )
