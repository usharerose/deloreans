import datetime
from unittest import TestCase

from delorean.date_utils import (
    DateGranularity,
    DateRange,
    DateSpan,
    SpanGranularity,
)


class DateGranularityTestCase(TestCase):

    def test_enum_items(self):
        self.assertEqual(DateGranularity.DAILY.value, 'daily')

    def test_validate_daily_completion(self):
        start_date = datetime.date(2024, 6, 10)
        end_date = datetime.date(2024, 6, 16)
        self.assertIsNone(
            DateGranularity.DAILY.validate_date_completion(start_date, end_date)
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


class DateSpanTestCase(TestCase):

    def test_span_count(self):
        span_count = 1
        span_granularity = SpanGranularity.DAILY
        date_span = DateSpan(span_count, span_granularity)

        self.assertEqual(date_span.span_count, 1)

    def test_span_granularity(self):
        span_count = 1
        span_granularity = SpanGranularity.DAILY
        date_span = DateSpan(span_count, span_granularity)

        self.assertEqual(date_span.span_granularity, SpanGranularity.DAILY)

    def test_invalid_span_count_type(self):
        span_count = '1'
        span_granularity = SpanGranularity.DAILY

        with self.assertRaises(TypeError):
            DateSpan(span_count, span_granularity)  # NOQA

    def test_invalid_span_count_value(self):
        span_count = -1
        span_granularity = SpanGranularity.DAILY

        with self.assertRaises(ValueError):
            DateSpan(span_count, span_granularity)  # NOQA

    def test_invalid_span_granularity(self):
        span_count = 1
        span_granularity = 'daily'

        with self.assertRaises(TypeError):
            DateSpan(span_count, span_granularity)  # NOQA
