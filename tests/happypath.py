import datetime
from unittest import TestCase

import deloreans
from deloreans import DateGranularity, OffsetGranularity


class HappyPathTestCase(TestCase):

    def test_daily_period_month_over_month(self):
        """
        compared daily date range which is at previous month
        """
        sample_kwargs = {
            'start_date': datetime.date(2024, 6, 1),
            'end_date': datetime.date(2024, 6, 15),
            'date_granularity': DateGranularity.DAILY,
            'offset': -1,
            'offset_granularity': OffsetGranularity.MONTHLY,
        }
        actual_start_date, actual_end_date = deloreans.get(**sample_kwargs)
        expected_start_date = datetime.date(2024, 5, 1)
        expected_end_date = datetime.date(2024, 5, 15)
        self.assertEqual(actual_start_date, expected_start_date)
        self.assertEqual(actual_end_date, expected_end_date)

    def test_week_date_month_over_month(self):
        """
        compared week date period which is at previous month

        e.g. first 8 weeks at 2024 Q2 (April to June) compared with previous quarter
        """
        sample_kwargs = {
            'start_date': datetime.date(2024, 4, 1),
            'end_date': datetime.date(2024, 5, 26),
            'date_granularity': DateGranularity.WEEKLY,
            'offset': -3,
            'offset_granularity': OffsetGranularity.MONTHLY,
        }
        actual_start_date, actual_end_date = deloreans.get(**sample_kwargs)
        expected_start_date = datetime.date(2024, 1, 1)
        expected_end_date = datetime.date(2024, 2, 25)
        self.assertEqual(actual_start_date, expected_start_date)
        self.assertEqual(actual_end_date, expected_end_date)

    def test_half_year_vs_half_year(self):
        """
        2nd half year vs 1st half year
        """
        sample_kwargs = {
            'start_date': datetime.date(2024, 7, 1),
            'end_date': datetime.date(2024, 12, 31),
            'date_granularity': DateGranularity.MONTHLY,
            'offset': -6,
            'offset_granularity': OffsetGranularity.MONTHLY,
        }
        actual_start_date, actual_end_date = deloreans.get(**sample_kwargs)
        expected_start_date = datetime.date(2024, 1, 1)
        expected_end_date = datetime.date(2024, 6, 30)
        self.assertEqual(actual_start_date, expected_start_date)
        self.assertEqual(actual_end_date, expected_end_date)

    def test_quarter_vs_quarter(self):
        """
        Q3 vs Q1 in the same year
        """
        sample_kwargs = {
            'start_date': datetime.date(2024, 7, 1),
            'end_date': datetime.date(2024, 9, 30),
            'date_granularity': DateGranularity.MONTHLY,
            'offset': -6,
            'offset_granularity': OffsetGranularity.MONTHLY,
        }
        actual_start_date, actual_end_date = deloreans.get(**sample_kwargs)
        expected_start_date = datetime.date(2024, 1, 1)
        expected_end_date = datetime.date(2024, 3, 31)
        self.assertEqual(actual_start_date, expected_start_date)
        self.assertEqual(actual_end_date, expected_end_date)

    def test_month_year_over_year(self):
        """
        February 2024 vs February 2023
        """
        sample_kwargs = {
            'start_date': datetime.date(2024, 2, 1),
            'end_date': datetime.date(2024, 2, 29),
            'date_granularity': DateGranularity.MONTHLY,
            'offset': -1,
            'offset_granularity': OffsetGranularity.YEARLY,
        }
        actual_start_date, actual_end_date = deloreans.get(**sample_kwargs)
        expected_start_date = datetime.date(2023, 2, 1)
        expected_end_date = datetime.date(2023, 2, 28)
        self.assertEqual(actual_start_date, expected_start_date)
        self.assertEqual(actual_end_date, expected_end_date)

    def test_monthly_link_relative_comparison(self):
        """
        February 2024 vs January 2024
        """
        sample_kwargs = {
            'start_date': datetime.date(2024, 2, 1),
            'end_date': datetime.date(2024, 2, 29),
            'date_granularity': DateGranularity.MONTHLY,
            'offset': -1,
            'offset_granularity': OffsetGranularity.PERIODIC,
        }
        actual_start_date, actual_end_date = deloreans.get(**sample_kwargs)
        expected_start_date = datetime.date(2024, 1, 1)
        expected_end_date = datetime.date(2024, 1, 31)
        self.assertEqual(actual_start_date, expected_start_date)
        self.assertEqual(actual_end_date, expected_end_date)

    def test_quarterly_link_relative_comparison(self):
        """
        Q2 2024 vs Q1 2024
        """
        sample_kwargs = {
            'start_date': datetime.date(2024, 4, 1),
            'end_date': datetime.date(2024, 6, 30),
            'date_granularity': DateGranularity.MONTHLY,
            'offset': -1,
            'offset_granularity': OffsetGranularity.PERIODIC,
        }
        actual_start_date, actual_end_date = deloreans.get(**sample_kwargs)
        expected_start_date = datetime.date(2024, 1, 1)
        expected_end_date = datetime.date(2024, 3, 31)
        self.assertEqual(actual_start_date, expected_start_date)
        self.assertEqual(actual_end_date, expected_end_date)
