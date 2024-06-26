import datetime
from unittest import TestCase

from deloreans.date_utils import (
    DateGranularity,
    DateRange,
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

    def test_firstweekday(self):
        start_date = datetime.date(2024, 6, 10)
        end_date = datetime.date(2024, 6, 10)
        date_granularity = DateGranularity.DAILY
        firstweekday = 6
        date_range = DateRange(
            start_date,
            end_date,
            date_granularity,
            firstweekday,
        )

        self.assertEqual(start_date, date_range.start_date)
        self.assertEqual(end_date, date_range.end_date)
        self.assertEqual(firstweekday, date_range.firstweekday)

    def test_weekly_completion(self):
        start_date = datetime.date(2024, 2, 11)
        end_date = datetime.date(2024, 2, 24)
        date_granularity = DateGranularity.WEEKLY
        with self.assertRaises(ValueError):
            DateRange(
                start_date,
                end_date,
                date_granularity,
            )

    def test_weekly_completion_with_sunday_start(self):
        start_date = datetime.date(2024, 2, 11)
        end_date = datetime.date(2024, 2, 24)
        date_granularity = DateGranularity.WEEKLY
        firstweekday = 6
        date_range = DateRange(
            start_date,
            end_date,
            date_granularity,
            firstweekday,
        )

        self.assertEqual(start_date, date_range.start_date)
        self.assertEqual(end_date, date_range.end_date)
        self.assertEqual(firstweekday, date_range.firstweekday)

    def test_invalid_firstweekday_type(self):
        start_date = datetime.date(2024, 6, 10)
        end_date = datetime.date(2024, 6, 10)
        date_granularity = DateGranularity.DAILY
        firstweekday = '6'

        with self.assertRaises(TypeError):
            DateRange(
                start_date,
                end_date,
                date_granularity,
                firstweekday,  # NOQA
            )

    def test_invalid_firstweekday_value(self):
        start_date = datetime.date(2024, 6, 10)
        end_date = datetime.date(2024, 6, 10)
        date_granularity = DateGranularity.DAILY
        firstweekday = 9

        with self.assertRaises(ValueError):
            DateRange(
                start_date,
                end_date,
                date_granularity,
                firstweekday,
            )
