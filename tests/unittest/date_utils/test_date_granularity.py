import datetime
from unittest import TestCase

from deloreans.date_utils.date_granularity import DateGranularity


class DateGranularityDailyTestCase(TestCase):

    def setUp(self):
        self.granularity = DateGranularity.DAILY

    def test_validate_date_completion(self):
        start_date = datetime.date(2024, 6, 15)
        end_date = datetime.date(2024, 6, 17)
        self.assertIsNone(self.granularity.validate_date_completion(start_date, end_date))

    def test_get_date_range_length(self):
        start_date = datetime.date(2024, 6, 15)
        end_date = datetime.date(2024, 6, 17)
        self.assertEqual(
            self.granularity.get_date_range_length(start_date, end_date),
            3,
        )

    def test_get_date_range_length_cross_year(self):
        start_date = datetime.date(2022, 12, 23)
        end_date = datetime.date(2023, 3, 12)
        self.assertEqual(
            self.granularity.get_date_range_length(start_date, end_date),
            9 + 31 + 28 + 12,
        )

    def test_get_date_range_length_with_leap_year(self):
        start_date = datetime.date(2023, 12, 23)
        end_date = datetime.date(2025, 1, 12)
        self.assertEqual(
            self.granularity.get_date_range_length(start_date, end_date),
            9 + 366 + 12,
        )

    def test_get_end_date(self):
        start_date = datetime.date(2024, 6, 24)
        date_range_length = 13
        self.assertEqual(
            self.granularity.get_end_date(start_date, date_range_length),
            datetime.date(2024, 7, 6),
        )


class DateGranularityWeeklyTestCase(TestCase):

    def setUp(self):
        self.granularity = DateGranularity.WEEKLY

    def test_validate_full_weeks(self):
        start_date = datetime.date(2024, 5, 27)
        end_date = datetime.date(2024, 6, 23)
        self.assertIsNone(self.granularity.validate_date_completion(start_date, end_date))

    def test_validate_partial_weeks(self):
        start_date = datetime.date(2024, 5, 30)
        end_date = datetime.date(2024, 6, 23)
        with self.assertRaises(ValueError):
            self.granularity.validate_date_completion(start_date, end_date)

    def test_validate_partial_but_seven_times_day_weeks(self):
        sample_start_date = datetime.date(2024, 6, 2)
        sample_end_date = datetime.date(2024, 6, 29)

        self.assertEqual(((sample_end_date - sample_start_date).days + 1) % 7, 0)
        with self.assertRaises(ValueError):
            self.granularity.validate_date_completion(sample_start_date, sample_end_date)

    def test_validate_full_weeks_start_from_sunday(self):
        sample_start_date = datetime.date(2024, 6, 2)
        sample_end_date = datetime.date(2024, 6, 29)
        sample_firstweekday = 6
        self.assertIsNone(
            self.granularity.validate_date_completion(
                sample_start_date,
                sample_end_date,
                sample_firstweekday,
            ),
        )

    def test_get_date_range_length(self):
        start_date = datetime.date(2024, 5, 27)
        end_date = datetime.date(2024, 6, 23)
        self.assertEqual(
            self.granularity.get_date_range_length(start_date, end_date),
            4,
        )

    def test_get_date_range_size_cross_year(self):
        start_date = datetime.date(2023, 12, 25)
        end_date = datetime.date(2024, 3, 31)
        self.assertEqual(
            self.granularity.get_date_range_length(start_date, end_date),
            14,
        )

    def test_get_end_date(self):
        start_date = datetime.date(2024, 6, 24)
        date_range_length = 6
        self.assertEqual(
            self.granularity.get_end_date(start_date, date_range_length),
            datetime.date(2024, 8, 4),
        )


class DateGranularityMonthlyTestCase(TestCase):

    def setUp(self):
        self.granularity = DateGranularity.MONTHLY

    def test_validate_full_months(self):
        start_date = datetime.date(2024, 1, 1)
        end_date = datetime.date(2024, 6, 30)
        self.assertIsNone(self.granularity.validate_date_completion(start_date, end_date))

    def test_validate_full_months_cross_year(self):
        start_date = datetime.date(2023, 2, 1)
        end_date = datetime.date(2024, 2, 29)
        self.assertIsNone(self.granularity.validate_date_completion(start_date, end_date))

    def test_validate_partial_months_in_leap_year(self):
        start_date = datetime.date(2023, 12, 1)
        end_date = datetime.date(2024, 2, 28)
        with self.assertRaises(ValueError):
            self.granularity.validate_date_completion(start_date, end_date)

    def test_get_date_range_length(self):
        start_date = datetime.date(2024, 3, 1)
        end_date = datetime.date(2024, 6, 30)
        self.assertEqual(
            self.granularity.get_date_range_length(start_date, end_date),
            4,
        )

    def test_get_date_range_length_cross_year(self):
        start_date = datetime.date(2022, 11, 1)
        end_date = datetime.date(2023, 3, 31)
        self.assertEqual(
            self.granularity.get_date_range_length(start_date, end_date),
            2 + 3,
        )

    def test_get_date_range_length_cross_multiple_years(self):
        start_date = datetime.date(2022, 11, 1)
        end_date = datetime.date(2024, 5, 31)
        self.assertEqual(
            self.granularity.get_date_range_length(start_date, end_date),
            2 + 12 + 5,
        )

    def test_get_end_date(self):
        start_date = datetime.date(2024, 6, 1)
        date_range_length = 2
        self.assertEqual(
            self.granularity.get_end_date(start_date, date_range_length),
            datetime.date(2024, 7, 31),
        )

    def test_get_end_date_in_leap_year_feb(self):
        start_date = datetime.date(2023, 11, 1)
        date_range_length = 4
        self.assertEqual(
            self.granularity.get_end_date(start_date, date_range_length),
            datetime.date(2024, 2, 29),
        )


class DateGranularityYearlyTestCase(TestCase):

    def setUp(self):
        self.granularity = DateGranularity.YEARLY

    def test_validate_date_completion(self):
        start_date = datetime.date(2023, 1, 1)
        end_date = datetime.date(2024, 12, 31)
        self.assertIsNone(self.granularity.validate_date_completion(start_date, end_date))

    def test_validate_partial_years(self):
        start_date = datetime.date(2023, 2, 1)
        end_date = datetime.date(2024, 2, 29)
        with self.assertRaises(ValueError):
            self.granularity.validate_date_completion(start_date, end_date)

    def test_get_date_range_length(self):
        start_date = datetime.date(2022, 1, 1)
        end_date = datetime.date(2024, 12, 31)
        self.assertEqual(
            self.granularity.get_date_range_length(start_date, end_date),
            3,
        )

    def test_get_end_date(self):
        start_date = datetime.date(2022, 1, 1)
        date_range_length = 3
        self.assertEqual(
            self.granularity.get_end_date(start_date, date_range_length),
            datetime.date(2024, 12, 31),
        )
