
import datetime
from unittest import TestCase

from delorean.app import DeLorean
from delorean.date_utils import (
    DateGranularity,
    SpanGranularity,
)


class DeLoreanTestCase(TestCase):

    def test_initialization(self) -> None:
        start_date = datetime.date(2024, 6, 10)
        end_date = datetime.date(2024, 6, 16)
        date_granularity = DateGranularity.DAILY
        span_count = 3
        span_granularity = SpanGranularity.DAILY
        self.assertIsNotNone(DeLorean(
            start_date,
            end_date,
            date_granularity,
            span_count,
            span_granularity,
        ))

    def test_get_compared_date_range(self):
        start_date = datetime.date(2024, 6, 10)
        end_date = datetime.date(2024, 6, 16)
        date_granularity = DateGranularity.DAILY
        span_count = 3
        span_granularity = SpanGranularity.DAILY
        executor = DeLorean(
            start_date,
            end_date,
            date_granularity,
            span_count,
            span_granularity,
        )
        self.assertEqual(
            executor.get(),
            (datetime.date(2024, 6, 13), datetime.date(2024, 6, 19))
        )
