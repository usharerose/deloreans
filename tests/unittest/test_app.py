
import datetime
from unittest import TestCase

from deloreans.app import DeLoreans
from deloreans.date_utils import (
    DateGranularity,
    OffsetGranularity,
)


class DeLoreansTestCase(TestCase):

    def test_initialization(self) -> None:
        start_date = datetime.date(2024, 6, 10)
        end_date = datetime.date(2024, 6, 16)
        date_granularity = DateGranularity.DAILY
        offset = 3
        offset_granularity = OffsetGranularity.DAILY
        self.assertIsNotNone(DeLoreans(
            start_date,
            end_date,
            date_granularity,
            offset,
            offset_granularity,
        ))

    def test_get_compared_date_range(self):
        start_date = datetime.date(2024, 6, 10)
        end_date = datetime.date(2024, 6, 16)
        date_granularity = DateGranularity.DAILY
        offset = 3
        offset_granularity = OffsetGranularity.DAILY
        executor = DeLoreans(
            start_date,
            end_date,
            date_granularity,
            offset,
            offset_granularity,
        )
        self.assertEqual(
            executor.get(),
            (datetime.date(2024, 6, 13), datetime.date(2024, 6, 19))
        )
