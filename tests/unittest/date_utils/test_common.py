import datetime
from unittest import TestCase

from delorean.date_utils.common import (
    get_start_date_of_monthly_start_week,
    get_week_anchor_date,
    get_weeks_offset_between_dates,
)


class GetWeekAnchorDateTestCase(TestCase):

    def test_with_date_before_thursday(self):
        sample_date = datetime.date(2024, 6, 10)
        self.assertEqual(
            get_week_anchor_date(sample_date),
            datetime.date(2024, 6, 13),
        )

    def test_with_thursday(self):
        sample_date = datetime.date(2023, 3, 2)
        self.assertEqual(
            get_week_anchor_date(sample_date),
            datetime.date(2023, 3, 2),
        )

    def test_with_date_after_thursday(self):
        sample_date = datetime.date(2020, 2, 29)
        self.assertEqual(
            get_week_anchor_date(sample_date),
            datetime.date(2020, 2, 27),
        )


class GetWeeksOffsetBetweenDatesTestCase(TestCase):

    def test_get_weeks_offset_between_dates(self):
        prev_date = datetime.date(2024, 6, 10)
        cur_date = datetime.date(2024, 6, 21)
        self.assertEqual(
            get_weeks_offset_between_dates(prev_date, cur_date),
            25 - 24,
        )

    def test_offset_cross_months(self):
        prev_date = datetime.date(2024, 2, 29)
        cur_date = datetime.date(2024, 6, 21)
        self.assertEqual(
            get_weeks_offset_between_dates(prev_date, cur_date),
            25 - 9,
        )

    def test_offset_cross_years(self):
        prev_date = datetime.date(2019, 12, 3)
        cur_date = datetime.date(2021, 3, 21)
        self.assertEqual(
            get_weeks_offset_between_dates(prev_date, cur_date),
            11 + 53 + (52 - 49),
        )


class GetStartDateOfMonthlyStartWeekTestCase(TestCase):

    def test_get_start_date_of_monthly_start_week(self):
        self.assertEqual(
            get_start_date_of_monthly_start_week(2024, 6),
            datetime.date(2024, 6, 3),
        )

    def test_start_date_at_another_month(self):
        self.assertEqual(
            get_start_date_of_monthly_start_week(2024, 5),
            datetime.date(2024, 4, 29),
        )
