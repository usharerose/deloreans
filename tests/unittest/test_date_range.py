import datetime
from unittest import TestCase

from delorean.date_range import DateRange


class DateRangeTestCase(TestCase):

    def test_date_range(self):
        start_date = datetime.date(2024, 6, 10)
        end_date = datetime.date(2024, 6, 10)
        date_range = DateRange(start_date, end_date)

        self.assertEqual(start_date, date_range.start_date)
        self.assertEqual(end_date, date_range.end_date)

    def test_invalid_date_type(self):
        start_date = '2024-06-10'
        end_date = '2024-06-10'
        with self.assertRaises(ValueError):
            DateRange(start_date, end_date)  # NOQA

    def test_invalid_date_values(self):
        start_date = datetime.date(2024, 6, 11)
        end_date = datetime.date(2024, 6, 10)
        with self.assertRaises(ValueError):
            DateRange(start_date, end_date)
