import datetime
from unittest import TestCase

from delorean.date_utils.common import (
    get_start_date_of_monthly_start_week,
    get_week_anchor_date,
    get_weeks_offset_between_dates,
    get_daily_period_idx_of_located_daily,
    get_daily_period_idx_of_located_weekly,
    get_daily_period_idx_of_located_monthly,
    get_daily_period_idx_of_located_yearly,
    get_weekly_period_idx_of_located_weekly,
    get_weekly_period_idx_of_located_monthly,
    get_weekly_period_idx_of_located_yearly,
    get_monthly_period_idx_of_located_monthly,
    get_monthly_period_idx_of_located_yearly,
    get_yearly_period_idx_of_located_yearly,
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


class GetPeriodIdxTestCase(TestCase):

    def test_get_daily_period_idx_of_located_daily(self):
        start_date = datetime.date(2024, 6, 18)
        self.assertEqual(
            get_daily_period_idx_of_located_daily(start_date),
            0,
        )

    def test_get_daily_period_idx_of_located_weekly(self):
        start_date = datetime.date(2024, 6, 18)
        self.assertEqual(
            get_daily_period_idx_of_located_weekly(start_date),
            1,
        )

    def test_get_daily_period_idx_of_located_monthly(self):
        start_date = datetime.date(2024, 6, 18)
        self.assertEqual(
            get_daily_period_idx_of_located_monthly(start_date),
            17,
        )

    def test_get_daily_period_idx_of_leap_year_feb(self):
        start_date = datetime.date(2016, 2, 29)
        self.assertEqual(
            get_daily_period_idx_of_located_monthly(start_date),
            28,
        )

    def test_get_daily_period_idx_of_located_yearly(self):
        start_date = datetime.date(2024, 6, 18)
        self.assertEqual(
            get_daily_period_idx_of_located_yearly(start_date),
            169,
        )

    def test_get_daily_period_idx_of_leap_year(self):
        start_date = datetime.date(2024, 12, 31)
        self.assertEqual(
            get_daily_period_idx_of_located_yearly(start_date),
            365,
        )

    def test_get_weekly_period_idx_of_located_weekly(self):
        start_date = datetime.date(2024, 6, 3)
        self.assertEqual(
            get_weekly_period_idx_of_located_weekly(start_date),
            0,
        )

    def test_get_weekly_period_idx_of_located_monthly(self):
        start_date = datetime.date(2024, 2, 26)
        self.assertEqual(
            get_weekly_period_idx_of_located_monthly(start_date),
            4,
        )

    def test_get_weekly_period_idx_which_has_another_month_num(self):
        start_date = datetime.date(2024, 4, 29)
        self.assertEqual(
            get_weekly_period_idx_of_located_monthly(start_date),
            0,
        )

    def test_get_weekly_period_idx_of_located_yearly(self):
        start_date = datetime.date(2024, 6, 10)
        self.assertEqual(
            get_weekly_period_idx_of_located_yearly(start_date),
            23,
        )

    def test_get_weekly_period_idx_which_has_another_year_num(self):
        start_date = datetime.date(2018, 12, 31)
        self.assertEqual(
            get_weekly_period_idx_of_located_yearly(start_date),
            0,
        )

    def test_get_weekly_period_idx_which_has_fifty_three_weeks(self):
        start_date = datetime.date(2015, 12, 28)
        self.assertEqual(
            get_weekly_period_idx_of_located_yearly(start_date),
            52,
        )

    def test_get_monthly_period_idx_of_located_monthly(self):
        start_date = datetime.date(2024, 1, 1)
        self.assertEqual(
            get_monthly_period_idx_of_located_monthly(start_date),
            0,
        )

    def test_get_monthly_period_idx_of_located_yearly(self):
        start_date = datetime.date(2023, 12, 1)
        self.assertEqual(
            get_monthly_period_idx_of_located_yearly(start_date),
            11,
        )

    def test_get_yearly_period_idx_of_located_yearly(self):
        start_date = datetime.date(2023, 1, 1)
        self.assertEqual(
            get_yearly_period_idx_of_located_yearly(start_date),
            0,
        )
