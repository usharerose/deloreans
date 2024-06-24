import datetime
from unittest import TestCase

from delorean.date_utils import (
    DateGranularity,
    DateRange,
    DatePeriodOffset,
    OffsetGranularity,
)


class DateRangeTestCase(TestCase):

    def test_date_range(self):
        start_date = datetime.date(2024, 6, 10)
        end_date = datetime.date(2024, 6, 10)
        date_granularity = DateGranularity.DAILY
        date_range = DateRange(start_date, end_date, date_granularity)

        self.assertEqual(start_date, date_range.start_date)
        self.assertEqual(end_date, date_range.end_date)

    def test_invalid_date_type(self):
        start_date = '2024-06-10'
        end_date = '2024-06-10'
        date_granularity = DateGranularity.DAILY
        with self.assertRaises(ValueError):
            DateRange(start_date, end_date, date_granularity)  # NOQA

    def test_invalid_date_values(self):
        start_date = datetime.date(2024, 6, 11)
        end_date = datetime.date(2024, 6, 10)
        date_granularity = DateGranularity.DAILY
        with self.assertRaises(ValueError):
            DateRange(start_date, end_date, date_granularity)

    def test_invalid_date_granularity(self):
        start_date = datetime.date(2024, 6, 11)
        end_date = datetime.date(2024, 6, 15)
        date_granularity = 'daily'
        with self.assertRaises(ValueError):
            DateRange(start_date, end_date, date_granularity)  # NOQA


class DatePeriodOffsetTestCase(TestCase):

    def test_offset(self):
        sample_offset = 1
        sample_offset_granularity = OffsetGranularity.DAILY
        date_period_offset = DatePeriodOffset(sample_offset, sample_offset_granularity)

        self.assertEqual(date_period_offset.offset, 1)

    def test_offset_granularity(self):
        sample_offset = 1
        sample_offset_granularity = OffsetGranularity.DAILY
        date_period_offset = DatePeriodOffset(sample_offset, sample_offset_granularity)

        self.assertEqual(date_period_offset.offset_granularity, OffsetGranularity.DAILY)

    def test_invalid_offset_type(self):
        sample_offset = '1'
        offset_granularity = OffsetGranularity.DAILY

        with self.assertRaises(TypeError):
            DatePeriodOffset(sample_offset, offset_granularity)  # NOQA

    def test_invalid_offset_granularity(self):
        sample_offset = 1
        sample_offset_granularity = 'daily'

        with self.assertRaises(TypeError):
            DatePeriodOffset(sample_offset, sample_offset_granularity)  # NOQA
