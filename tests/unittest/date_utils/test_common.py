import datetime
from unittest import TestCase

from deloreans.date_utils.common import (
    get_weekly_start_date,
    get_start_weekly_of_month,
    get_week_anchor_date,
    get_weeks_offset,
    get_start_daily_of_daily,
    get_daily_index_of_daily,
    get_compared_start_daily_located_daily,
    get_daily_with_index_in_daily,
    get_start_daily_of_weekly,
    get_daily_index_of_weekly,
    get_compared_start_daily_located_weekly,
    get_daily_with_index_in_weekly,
    get_start_daily_of_monthly,
    get_daily_index_of_monthly,
    get_compared_start_daily_located_monthly,
    get_daily_with_index_in_monthly,
    get_start_daily_of_yearly,
    get_daily_index_of_yearly,
    get_compared_start_daily_located_yearly,
    get_daily_with_index_in_yearly,
    get_start_weekly_of_weekly,
    get_weekly_index_of_weekly,
    get_compared_start_weekly_located_weekly,
    get_weekly_with_index_in_weekly,
    get_start_weekly_of_monthly,
    get_weekly_index_of_monthly,
    get_compared_start_weekly_located_monthly,
    get_weekly_with_index_in_monthly,
    get_start_weekly_of_yearly,
    get_weekly_index_of_yearly,
    get_compared_start_weekly_located_yearly,
    get_weekly_with_index_in_yearly,
    get_start_monthly_of_monthly,
    get_monthly_index_of_monthly,
    get_compared_start_monthly_located_monthly,
    get_monthly_with_index_in_monthly,
    get_start_monthly_of_yearly,
    get_monthly_index_of_yearly,
    get_compared_start_monthly_located_yearly,
    get_monthly_with_index_in_yearly,
    get_start_yearly_of_yearly,
    get_yearly_index_of_yearly,
    get_compared_start_yearly_located_yearly,
    get_yearly_with_index_in_yearly,
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

    def test_start_from_sunday(self):
        sample_date = datetime.date(2024, 6, 28)
        sample_firstweekday = 6
        self.assertEqual(
            get_weekly_start_date(sample_date, sample_firstweekday),
            datetime.date(2024, 6, 23),
        )

    def test_start_from_saturday(self):
        sample_date = datetime.date(2024, 1, 3)
        sample_firstweekday = 5
        self.assertEqual(
            get_weekly_start_date(sample_date, sample_firstweekday),
            datetime.date(2023, 12, 30),
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

    def test_anchor_date_when_start_saturday(self):
        sample_date = datetime.date(2024, 6, 10)
        sample_firstweekday = 5
        self.assertEqual(
            get_week_anchor_date(sample_date, sample_firstweekday),
            datetime.date(2024, 6, 11),
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

    def test_offset_cross_years_with_sunday_start(self):
        sample_base_date = datetime.date(2019, 12, 3)
        sample_compared_date = datetime.date(2021, 3, 21)
        sample_firstweekday = 6
        self.assertEqual(
            get_weeks_offset(
                sample_base_date,
                sample_compared_date,
                sample_firstweekday,
            ),
            12 + 53 + (52 - 49),  # 2021-03-21 would locate at Week 12, 2021 when week starts with Sunday
        )


class GetStartWeeklyOfMonthTestCase(TestCase):

    def test_get_start_weekly_of_month(self):
        self.assertEqual(
            get_start_weekly_of_month(2024, 6),
            datetime.date(2024, 6, 3),
        )

    def test_get_start_weekly_of_month_with_sunday_start(self):
        sample_firstweekday = 6
        self.assertEqual(
            get_start_weekly_of_month(
                2024,
                6,
                sample_firstweekday,
            ),
            datetime.date(2024, 6, 2),
        )

    def test_start_date_at_another_month(self):
        self.assertEqual(
            get_start_weekly_of_month(2024, 5),
            datetime.date(2024, 4, 29),
        )


class GetLocatedPeriodStartDateTestCase(TestCase):

    def test_get_start_daily_of_daily(self):
        start_date = datetime.date(2024, 6, 18)
        self.assertEqual(
            get_start_daily_of_daily(start_date),
            datetime.date(2024, 6, 18),
        )

    def test_get_start_daily_of_weekly(self):
        start_date = datetime.date(2024, 6, 18)
        self.assertEqual(
            get_start_daily_of_weekly(start_date),
            datetime.date(2024, 6, 17),
        )

    def test_get_start_daily_of_monthly(self):
        start_date = datetime.date(2024, 6, 18)
        self.assertEqual(
            get_start_daily_of_monthly(start_date),
            datetime.date(2024, 6, 1),
        )

    def test_get_start_daily_of_leap_year_feb(self):
        start_date = datetime.date(2016, 2, 29)
        self.assertEqual(
            get_start_daily_of_monthly(start_date),
            datetime.date(2016, 2, 1),
        )

    def test_get_start_daily_of_yearly(self):
        start_date = datetime.date(2024, 6, 18)
        self.assertEqual(
            get_start_daily_of_yearly(start_date),
            datetime.date(2024, 1, 1),
        )

    def test_get_start_daily_of_leap_year(self):
        start_date = datetime.date(2024, 2, 29)
        self.assertEqual(
            get_start_daily_of_yearly(start_date),
            datetime.date(2024, 1, 1),
        )

    def test_get_start_weekly_of_weekly(self):
        start_date = datetime.date(2024, 6, 3)
        self.assertEqual(
            get_start_weekly_of_weekly(start_date),
            datetime.date(2024, 6, 3),
        )

    def test_get_start_weekly_of_monthly(self):
        start_date = datetime.date(2024, 2, 26)
        self.assertEqual(
            get_start_weekly_of_monthly(start_date),
            datetime.date(2024, 1, 29),
        )

    def test_get_start_weekly_of_monthly_which_has_another_month_num(self):
        start_date = datetime.date(2024, 4, 29)
        self.assertEqual(
            get_start_weekly_of_monthly(start_date),
            datetime.date(2024, 4, 29),
        )

    def test_get_start_weekly_of_yearly(self):
        start_date = datetime.date(2024, 6, 10)
        self.assertEqual(
            get_start_weekly_of_yearly(start_date),
            datetime.date(2024, 1, 1),
        )

    def test_get_start_weekly_of_yearly_which_has_another_year_num(self):
        start_date = datetime.date(2018, 12, 31)
        self.assertEqual(
            get_start_weekly_of_yearly(start_date),
            datetime.date(2018, 12, 31),
        )

    def test_get_start_weekly_of_yearly_which_has_fifty_three_weeks(self):
        start_date = datetime.date(2015, 12, 28)
        self.assertEqual(
            get_start_weekly_of_yearly(start_date),
            datetime.date(2014, 12, 29),
        )

    def test_get_start_monthly_of_monthly(self):
        start_date = datetime.date(2024, 1, 1)
        self.assertEqual(
            get_start_monthly_of_monthly(start_date),
            datetime.date(2024, 1, 1),
        )

    def test_get_start_monthly_of_yearly(self):
        start_date = datetime.date(2023, 12, 1)
        self.assertEqual(
            get_start_monthly_of_yearly(start_date),
            datetime.date(2023, 1, 1),
        )

    def test_get_start_yearly_of_yearly(self):
        start_date = datetime.date(2023, 1, 1)
        self.assertEqual(
            get_start_yearly_of_yearly(start_date),
            datetime.date(2023, 1, 1),
        )


class GetPeriodIdxTestCase(TestCase):

    def test_get_daily_index_of_daily(self):
        start_date = datetime.date(2024, 6, 18)
        self.assertEqual(
            get_daily_index_of_daily(start_date),
            0,
        )

    def test_get_daily_index_of_weekly(self):
        start_date = datetime.date(2024, 6, 18)
        self.assertEqual(
            get_daily_index_of_weekly(start_date),
            1,
        )

    def test_get_daily_index_of_monthly(self):
        start_date = datetime.date(2024, 6, 18)
        self.assertEqual(
            get_daily_index_of_monthly(start_date),
            17,
        )

    def test_get_daily_index_of_leap_year_feb(self):
        start_date = datetime.date(2016, 2, 29)
        self.assertEqual(
            get_daily_index_of_monthly(start_date),
            28,
        )

    def test_get_daily_index_of_yearly(self):
        start_date = datetime.date(2024, 6, 18)
        self.assertEqual(
            get_daily_index_of_yearly(start_date),
            169,
        )

    def test_get_daily_index_of_leap_year(self):
        start_date = datetime.date(2024, 12, 31)
        self.assertEqual(
            get_daily_index_of_yearly(start_date),
            365,
        )

    def test_get_weekly_index_of_weekly(self):
        start_date = datetime.date(2024, 6, 3)
        self.assertEqual(
            get_weekly_index_of_weekly(start_date),
            0,
        )

    def test_get_weekly_index_of_monthly(self):
        start_date = datetime.date(2024, 2, 26)
        self.assertEqual(
            get_weekly_index_of_monthly(start_date),
            4,
        )

    def test_get_weekly_index_of_monthly_which_has_another_month_num(self):
        start_date = datetime.date(2024, 4, 29)
        self.assertEqual(
            get_weekly_index_of_monthly(start_date),
            0,
        )

    def test_get_weekly_index_of_yearly(self):
        start_date = datetime.date(2024, 6, 10)
        self.assertEqual(
            get_weekly_index_of_yearly(start_date),
            23,
        )

    def test_get_weekly_index_of_yearly_which_has_another_year_num(self):
        start_date = datetime.date(2018, 12, 31)
        self.assertEqual(
            get_weekly_index_of_yearly(start_date),
            0,
        )

    def test_get_weekly_index_of_yearly_which_has_fifty_three_weeks(self):
        start_date = datetime.date(2015, 12, 28)
        self.assertEqual(
            get_weekly_index_of_yearly(start_date),
            52,
        )

    def test_get_monthly_index_of_monthly(self):
        start_date = datetime.date(2024, 1, 1)
        self.assertEqual(
            get_monthly_index_of_monthly(start_date),
            0,
        )

    def test_get_monthly_index_of_yearly(self):
        start_date = datetime.date(2023, 12, 1)
        self.assertEqual(
            get_monthly_index_of_yearly(start_date),
            11,
        )

    def test_get_yearly_index_of_yearly(self):
        start_date = datetime.date(2023, 1, 1)
        self.assertEqual(
            get_yearly_index_of_yearly(start_date),
            0,
        )


class GetComparedStartPeriodLocatedPeriodTestCase(TestCase):

    def test_get_compared_start_daily_located_daily(self):
        sample_date = datetime.date(2024, 6, 18)
        sample_offset = -13
        self.assertEqual(
            get_compared_start_daily_located_daily(sample_date, sample_offset),
            datetime.date(2024, 6, 5),
        )

    def test_get_compared_start_daily_located_weekly(self):
        sample_date = datetime.date(2024, 6, 18)
        sample_offset = -7
        self.assertEqual(
            get_compared_start_daily_located_weekly(sample_date, sample_offset),
            datetime.date(2024, 4, 29),
        )

    def test_get_compared_start_daily_located_monthly(self):
        sample_date = datetime.date(2024, 6, 18)
        sample_offset = -6
        self.assertEqual(
            get_compared_start_daily_located_monthly(sample_date, sample_offset),
            datetime.date(2023, 12, 1),
        )

    def test_get_compared_start_daily_located_leap_year_feb(self):
        sample_date = datetime.date(2016, 2, 29)
        sample_offset = -1
        self.assertEqual(
            get_compared_start_daily_located_monthly(sample_date, sample_offset),
            datetime.date(2016, 1, 1),
        )

    def test_get_compared_start_daily_located_yearly(self):
        sample_date = datetime.date(2024, 6, 18)
        sample_offset = -3
        self.assertEqual(
            get_compared_start_daily_located_yearly(sample_date, sample_offset),
            datetime.date(2021, 1, 1),
        )

    def test_get_compared_start_weekly_located_weekly(self):
        sample_date = datetime.date(2024, 6, 3)
        sample_offset = -24
        self.assertEqual(
            get_compared_start_weekly_located_weekly(sample_date, sample_offset),
            datetime.date(2023, 12, 18),
        )

    def test_get_compared_start_weekly_located_monthly(self):
        sample_date = datetime.date(2024, 2, 26)
        sample_offset = -4
        self.assertEqual(
            get_compared_start_weekly_located_monthly(sample_date, sample_offset),
            datetime.date(2023, 10, 2),
        )

    def test_get_compared_start_weekly_located_monthly_which_has_another_month_num(self):
        sample_date = datetime.date(2024, 4, 29)
        sample_offset = -2
        self.assertEqual(
            get_compared_start_weekly_located_monthly(sample_date, sample_offset),
            datetime.date(2024, 3, 4),
        )

    def test_get_compared_start_weekly_located_yearly(self):
        sample_date = datetime.date(2024, 6, 10)
        sample_offset = -3
        self.assertEqual(
            get_compared_start_weekly_located_yearly(sample_date, sample_offset),
            datetime.date(2021, 1, 4),
        )

    def test_get_compared_start_weekly_located_yearly_which_has_another_year_num(self):
        sample_date = datetime.date(2018, 12, 31)
        sample_offset = -3
        self.assertEqual(
            get_compared_start_weekly_located_yearly(sample_date, sample_offset),
            datetime.date(2016, 1, 4),
        )

    def test_get_compared_start_monthly_located_monthly(self):
        sample_date = datetime.date(2024, 1, 1)
        sample_offset = -15
        self.assertEqual(
            get_compared_start_monthly_located_monthly(sample_date, sample_offset),
            datetime.date(2022, 10, 1),
        )

    def test_get_compared_start_monthly_located_yearly(self):
        sample_date = datetime.date(2023, 12, 1)
        sample_offset = -5
        self.assertEqual(
            get_compared_start_monthly_located_yearly(sample_date, sample_offset),
            datetime.date(2018, 1, 1),
        )

    def test_get_compared_start_yearly_located_yearly(self):
        sample_date = datetime.date(2023, 1, 1)
        sample_offset = -10
        self.assertEqual(
            get_compared_start_yearly_located_yearly(sample_date, sample_offset),
            datetime.date(2013, 1, 1),
        )


class GetPeriodWithIndexInUnitPeriodTestCase(TestCase):

    def test_get_daily_with_index_in_daily(self):
        sample_date = datetime.date(2024, 6, 18)
        sample_index = 0
        self.assertEqual(
            get_daily_with_index_in_daily(sample_date, sample_index),
            datetime.date(2024, 6, 18),
        )

    def test_get_daily_with_index_in_weekly(self):
        sample_date = datetime.date(2024, 6, 17)
        sample_index = 5
        self.assertEqual(
            get_daily_with_index_in_weekly(sample_date, sample_index),
            datetime.date(2024, 6, 22),
        )

    def test_get_daily_with_index_in_monthly(self):
        sample_date = datetime.date(2024, 6, 1)
        sample_index = 13
        self.assertEqual(
            get_daily_with_index_in_monthly(sample_date, sample_index),
            datetime.date(2024, 6, 14),
        )

    def test_get_daily_with_exceeded_index_in_monthly(self):
        sample_date = datetime.date(2024, 11, 1)
        sample_index = 33
        with self.assertRaises(ValueError):
            get_daily_with_index_in_monthly(sample_date, sample_index)

    def test_get_daily_with_index_in_yearly(self):
        sample_date = datetime.date(2024, 1, 1)
        sample_index = 59
        self.assertEqual(
            get_daily_with_index_in_yearly(sample_date, sample_index),
            datetime.date(2024, 2, 29),
        )

    def test_get_weekly_with_index_in_weekly(self):
        sample_date = datetime.date(2024, 6, 3)
        sample_index = 0
        self.assertEqual(
            get_weekly_with_index_in_weekly(sample_date, sample_index),
            datetime.date(2024, 6, 3),
        )

    def test_get_weekly_with_index_in_monthly(self):
        sample_date = datetime.date(2024, 1, 29)
        sample_index = 3
        self.assertEqual(
            get_weekly_with_index_in_monthly(sample_date, sample_index),
            datetime.date(2024, 2, 19),
        )

    def test_get_weekly_with_index_in_yearly(self):
        sample_date = datetime.date(2024, 1, 1)
        sample_index = 49
        self.assertEqual(
            get_weekly_with_index_in_yearly(sample_date, sample_index),
            datetime.date(2024, 12, 9),
        )

    def test_get_monthly_with_index_in_monthly(self):
        sample_date = datetime.date(2024, 6, 1)
        sample_index = 0
        self.assertEqual(
            get_monthly_with_index_in_monthly(sample_date, sample_index),
            datetime.date(2024, 6, 1),
        )

    def test_get_monthly_with_index_in_yearly(self):
        sample_date = datetime.date(2023, 1, 1)
        sample_index = 9
        self.assertEqual(
            get_monthly_with_index_in_yearly(sample_date, sample_index),
            datetime.date(2023, 10, 1),
        )

    def test_get_yearly_with_index_in_yearly(self):
        sample_date = datetime.date(2023, 1, 1)
        sample_index = 0
        self.assertEqual(
            get_yearly_with_index_in_yearly(sample_date, sample_index),
            datetime.date(2023, 1, 1),
        )
