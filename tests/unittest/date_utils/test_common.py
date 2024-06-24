import datetime
from unittest import TestCase

from delorean.date_utils.common import (
    get_weekly_start_date,
    get_start_date_of_monthly_start_week,
    get_week_anchor_date,
    get_weeks_offset,
    get_daily_start_date_of_located_daily,
    get_daily_period_idx_of_located_daily,
    get_prev_daily_start_date_from_daily_located,
    get_daily_period_in_daily_by_index,
    get_daily_start_date_of_located_weekly,
    get_daily_period_idx_of_located_weekly,
    get_prev_weekly_start_date_from_daily_located,
    get_daily_period_in_weekly_by_index,
    get_daily_start_date_of_located_monthly,
    get_daily_period_idx_of_located_monthly,
    get_prev_monthly_start_date_from_daily_located,
    get_daily_period_in_monthly_by_index,
    get_daily_start_date_of_located_yearly,
    get_daily_period_idx_of_located_yearly,
    get_prev_yearly_start_date_from_daily_located,
    get_daily_period_in_yearly_by_index,
    get_weekly_start_date_of_located_weekly,
    get_weekly_period_idx_of_located_weekly,
    get_prev_weekly_start_date_from_weekly_located,
    get_weekly_period_in_weekly_by_index,
    get_weekly_start_date_of_located_monthly,
    get_weekly_period_idx_of_located_monthly,
    get_prev_monthly_start_date_from_weekly_located,
    get_weekly_period_in_monthly_by_index,
    get_weekly_start_date_of_located_yearly,
    get_weekly_period_idx_of_located_yearly,
    get_prev_yearly_start_date_from_weekly_located,
    get_weekly_period_in_yearly_by_index,
    get_monthly_start_date_of_located_monthly,
    get_monthly_period_idx_of_located_monthly,
    get_prev_monthly_start_date_from_monthly_located,
    get_monthly_period_in_monthly_by_index,
    get_monthly_start_date_of_located_yearly,
    get_monthly_period_idx_of_located_yearly,
    get_prev_yearly_start_date_from_monthly_located,
    get_monthly_period_in_yearly_by_index,
    get_yearly_start_date_of_located_yearly,
    get_yearly_period_idx_of_located_yearly,
    get_prev_yearly_start_date_from_yearly_located,
    get_yearly_period_in_yearly_by_index,
)


class GetWeeklyStartDateTestCase(TestCase):

    def test_get_weekly_start_date(self):
        sample_date = datetime.date(2024, 6, 10)
        self.assertEqual(
            get_weekly_start_date(sample_date),
            datetime.date(2024, 6, 10),
        )

    def test_get_located_at_another_month(self):
        sample_date = datetime.date(2024, 6, 2)
        self.assertEqual(
            get_weekly_start_date(sample_date),
            datetime.date(2024, 5, 27),
        )

    def test_get_located_at_another_year(self):
        sample_date = datetime.date(2025, 1, 1)
        self.assertEqual(
            get_weekly_start_date(sample_date),
            datetime.date(2024, 12, 30),
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


class GetWeeksOffsetTestCase(TestCase):

    def test_get_weeks_offset(self):
        prev_date = datetime.date(2024, 6, 10)
        cur_date = datetime.date(2024, 6, 21)
        self.assertEqual(
            get_weeks_offset(prev_date, cur_date),
            25 - 24,
        )

    def test_offset_cross_months(self):
        prev_date = datetime.date(2024, 2, 29)
        cur_date = datetime.date(2024, 6, 21)
        self.assertEqual(
            get_weeks_offset(prev_date, cur_date),
            25 - 9,
        )

    def test_offset_cross_years(self):
        prev_date = datetime.date(2019, 12, 3)
        cur_date = datetime.date(2021, 3, 21)
        self.assertEqual(
            get_weeks_offset(prev_date, cur_date),
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


class GetLocatedPeriodStartDateTestCase(TestCase):

    def test_get_daily_start_date_of_located_daily(self):
        start_date = datetime.date(2024, 6, 18)
        self.assertEqual(
            get_daily_start_date_of_located_daily(start_date),
            datetime.date(2024, 6, 18),
        )

    def test_get_daily_start_date_of_located_weekly(self):
        start_date = datetime.date(2024, 6, 18)
        self.assertEqual(
            get_daily_start_date_of_located_weekly(start_date),
            datetime.date(2024, 6, 17),
        )

    def test_get_daily_start_date_of_located_monthly(self):
        start_date = datetime.date(2024, 6, 18)
        self.assertEqual(
            get_daily_start_date_of_located_monthly(start_date),
            datetime.date(2024, 6, 1),
        )

    def test_get_daily_start_date_of_located_leap_year_feb(self):
        start_date = datetime.date(2016, 2, 29)
        self.assertEqual(
            get_daily_start_date_of_located_monthly(start_date),
            datetime.date(2016, 2, 1),
        )

    def test_get_daily_start_date_of_located_yearly(self):
        start_date = datetime.date(2024, 6, 18)
        self.assertEqual(
            get_daily_start_date_of_located_yearly(start_date),
            datetime.date(2024, 1, 1),
        )

    def test_get_daily_start_date_of_located_leap_year(self):
        start_date = datetime.date(2024, 2, 29)
        self.assertEqual(
            get_daily_start_date_of_located_yearly(start_date),
            datetime.date(2024, 1, 1),
        )

    def test_get_weekly_start_date_of_located_weekly(self):
        start_date = datetime.date(2024, 6, 3)
        self.assertEqual(
            get_weekly_start_date_of_located_weekly(start_date),
            datetime.date(2024, 6, 3),
        )

    def test_get_weekly_start_date_of_located_monthly(self):
        start_date = datetime.date(2024, 2, 26)
        self.assertEqual(
            get_weekly_start_date_of_located_monthly(start_date),
            datetime.date(2024, 1, 29),
        )

    def test_get_weekly_start_date_of_located_monthly_which_has_another_month_num(self):
        start_date = datetime.date(2024, 4, 29)
        self.assertEqual(
            get_weekly_start_date_of_located_monthly(start_date),
            datetime.date(2024, 4, 29),
        )

    def test_get_weekly_start_date_of_located_yearly(self):
        start_date = datetime.date(2024, 6, 10)
        self.assertEqual(
            get_weekly_start_date_of_located_yearly(start_date),
            datetime.date(2024, 1, 1),
        )

    def test_get_weekly_start_date_of_located_yearly_which_has_another_year_num(self):
        start_date = datetime.date(2018, 12, 31)
        self.assertEqual(
            get_weekly_start_date_of_located_yearly(start_date),
            datetime.date(2018, 12, 31),
        )

    def test_get_weekly_start_date_of_located_yearly_which_has_fifty_three_weeks(self):
        start_date = datetime.date(2015, 12, 28)
        self.assertEqual(
            get_weekly_start_date_of_located_yearly(start_date),
            datetime.date(2014, 12, 29),
        )

    def test_get_monthly_start_date_of_located_monthly(self):
        start_date = datetime.date(2024, 1, 1)
        self.assertEqual(
            get_monthly_start_date_of_located_monthly(start_date),
            datetime.date(2024, 1, 1),
        )

    def test_get_monthly_start_date_of_located_yearly(self):
        start_date = datetime.date(2023, 12, 1)
        self.assertEqual(
            get_monthly_start_date_of_located_yearly(start_date),
            datetime.date(2023, 1, 1),
        )

    def test_get_yearly_start_date_of_located_yearly(self):
        start_date = datetime.date(2023, 1, 1)
        self.assertEqual(
            get_yearly_start_date_of_located_yearly(start_date),
            datetime.date(2023, 1, 1),
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


class GetPrevLocatedPeriodStartDateTestCase(TestCase):

    def test_get_prev_daily_start_date_from_daily_located(self):
        sample_date = datetime.date(2024, 6, 18)
        self.assertEqual(
            get_prev_daily_start_date_from_daily_located(sample_date, 13),
            datetime.date(2024, 6, 5),
        )

    def test_get_prev_weekly_start_date_from_daily_located(self):
        sample_date = datetime.date(2024, 6, 18)
        self.assertEqual(
            get_prev_weekly_start_date_from_daily_located(sample_date, 7),
            datetime.date(2024, 4, 29),
        )

    def test_get_prev_monthly_start_date_from_daily_located(self):
        sample_date = datetime.date(2024, 6, 18)
        self.assertEqual(
            get_prev_monthly_start_date_from_daily_located(sample_date, 6),
            datetime.date(2023, 12, 1),
        )

    def test_get_prev_monthly_start_date_from_daily_located_at_leap_year_feb(self):
        sample_date = datetime.date(2016, 2, 29)
        self.assertEqual(
            get_prev_monthly_start_date_from_daily_located(sample_date, 1),
            datetime.date(2016, 1, 1),
        )

    def test_get_prev_yearly_start_date_from_daily_located(self):
        sample_date = datetime.date(2024, 6, 18)
        self.assertEqual(
            get_prev_yearly_start_date_from_daily_located(sample_date, 3),
            datetime.date(2021, 1, 1),
        )

    def test_get_prev_weekly_start_date_from_weekly_located(self):
        sample_date = datetime.date(2024, 6, 3)
        self.assertEqual(
            get_prev_weekly_start_date_from_weekly_located(sample_date, 24),
            datetime.date(2023, 12, 18),
        )

    def test_get_prev_monthly_start_date_from_weekly_located(self):
        sample_date = datetime.date(2024, 2, 26)
        self.assertEqual(
            get_prev_monthly_start_date_from_weekly_located(sample_date, 4),
            datetime.date(2023, 10, 2),
        )

    def test_get_prev_monthly_start_date_from_weekly_located_which_has_another_month_num(self):
        sample_date = datetime.date(2024, 4, 29)
        self.assertEqual(
            get_prev_monthly_start_date_from_weekly_located(sample_date, 2),
            datetime.date(2024, 3, 4),
        )

    def test_get_prev_yearly_start_date_from_weekly_located(self):
        sample_date = datetime.date(2024, 6, 10)
        self.assertEqual(
            get_prev_yearly_start_date_from_weekly_located(sample_date, 3),
            datetime.date(2021, 1, 4),
        )

    def test_get_prev_yearly_start_date_from_weekly_located_which_has_another_year_num(self):
        sample_date = datetime.date(2018, 12, 31)
        self.assertEqual(
            get_prev_yearly_start_date_from_weekly_located(sample_date, 3),
            datetime.date(2016, 1, 4),
        )

    def test_get_prev_monthly_start_date_from_monthly_located(self):
        sample_date = datetime.date(2024, 1, 1)
        self.assertEqual(
            get_prev_monthly_start_date_from_monthly_located(sample_date, 15),
            datetime.date(2022, 10, 1),
        )

    def test_get_prev_yearly_start_date_from_monthly_located(self):
        sample_date = datetime.date(2023, 12, 1)
        self.assertEqual(
            get_prev_yearly_start_date_from_monthly_located(sample_date, 5),
            datetime.date(2018, 1, 1),
        )

    def test_get_prev_yearly_start_date_from_yearly_located(self):
        sample_date = datetime.date(2023, 1, 1)
        self.assertEqual(
            get_prev_yearly_start_date_from_yearly_located(sample_date, 10),
            datetime.date(2013, 1, 1),
        )


class GetPeriodInUnitPeriodByIndexTestCase(TestCase):

    def test_get_daily_period_in_daily_by_index(self):
        sample_date = datetime.date(2024, 6, 18)
        sample_index = 0
        self.assertEqual(
            get_daily_period_in_daily_by_index(sample_date, sample_index),
            datetime.date(2024, 6, 18),
        )

    def test_get_daily_period_in_weekly_by_index(self):
        sample_date = datetime.date(2024, 6, 17)
        sample_index = 5
        self.assertEqual(
            get_daily_period_in_weekly_by_index(sample_date, sample_index),
            datetime.date(2024, 6, 22),
        )

    def test_get_daily_period_in_monthly_by_index(self):
        sample_date = datetime.date(2024, 6, 1)
        sample_index = 13
        self.assertEqual(
            get_daily_period_in_monthly_by_index(sample_date, sample_index),
            datetime.date(2024, 6, 14),
        )

    def test_get_daily_period_in_yearly_by_index(self):
        sample_date = datetime.date(2024, 1, 1)
        sample_index = 59
        self.assertEqual(
            get_daily_period_in_yearly_by_index(sample_date, sample_index),
            datetime.date(2024, 2, 29),
        )

    def test_get_weekly_period_in_weekly_by_index(self):
        sample_date = datetime.date(2024, 6, 3)
        sample_index = 0
        self.assertEqual(
            get_weekly_period_in_weekly_by_index(sample_date, sample_index),
            datetime.date(2024, 6, 3),
        )

    def test_get_weekly_period_in_monthly_by_index(self):
        sample_date = datetime.date(2024, 1, 29)
        sample_index = 3
        self.assertEqual(
            get_weekly_period_in_monthly_by_index(sample_date, sample_index),
            datetime.date(2024, 2, 19),
        )

    def test_get_weekly_period_in_yearly_by_index(self):
        sample_date = datetime.date(2024, 1, 1)
        sample_index = 49
        self.assertEqual(
            get_weekly_period_in_yearly_by_index(sample_date, sample_index),
            datetime.date(2024, 12, 9),
        )

    def test_get_monthly_period_in_monthly_by_index(self):
        sample_date = datetime.date(2024, 6, 1)
        sample_index = 0
        self.assertEqual(
            get_monthly_period_in_monthly_by_index(sample_date, sample_index),
            datetime.date(2024, 6, 1),
        )

    def test_get_monthly_period_in_yearly_by_index(self):
        sample_date = datetime.date(2023, 1, 1)
        sample_index = 9
        self.assertEqual(
            get_monthly_period_in_yearly_by_index(sample_date, sample_index),
            datetime.date(2023, 10, 1),
        )

    def test_get_yearly_period_in_yearly_by_index(self):
        sample_date = datetime.date(2023, 1, 1)
        sample_index = 0
        self.assertEqual(
            get_yearly_period_in_yearly_by_index(sample_date, sample_index),
            datetime.date(2023, 1, 1),
        )
