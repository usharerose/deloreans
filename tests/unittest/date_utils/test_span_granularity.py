import datetime
from unittest import TestCase

from delorean.date_utils.date_range import DateRange
from delorean.date_utils.date_granularity import DateGranularity
from delorean.date_utils.span_granularity import (
    Daily,
    Weekly,
    Monthly,
    Yearly,
    Periodic,
)


class SpanGranularityDailyTestCase(TestCase):

    def setUp(self):
        self.granularity = Daily()

    def test_name(self):
        self.assertEqual(self.granularity.name, 'daily')

    def test_daily_first_period_index(self):
        start_date = datetime.date(2024, 6, 18)
        end_date = datetime.date(2024, 6, 21)
        date_range = DateRange(
            start_date,
            end_date,
            DateGranularity.DAILY,
        )
        self.assertEqual(
            self.granularity.get_first_period_index(date_range),
            0,
        )

    def test_daily_first_period_located_start_date(self):
        start_date = datetime.date(2024, 6, 18)
        end_date = datetime.date(2024, 6, 21)
        date_range = DateRange(
            start_date,
            end_date,
            DateGranularity.DAILY,
        )
        self.assertEqual(
            self.granularity.get_first_period_located_start_date(date_range),
            datetime.date(2024, 6, 18),
        )

    def test_unsupported_weekly_date_granularity(self):
        start_date = datetime.date(2024, 6, 17)
        end_date = datetime.date(2024, 6, 23)
        date_range = DateRange(
            start_date,
            end_date,
            DateGranularity.WEEKLY,
        )
        with self.assertRaises(NotImplementedError):
            self.granularity.get_first_period_index(date_range)
        with self.assertRaises(NotImplementedError):
            self.granularity.get_first_period_located_start_date(date_range)

    def test_unsupported_monthly_date_granularity(self):
        start_date = datetime.date(2024, 1, 1)
        end_date = datetime.date(2024, 1, 31)
        date_range = DateRange(
            start_date,
            end_date,
            DateGranularity.MONTHLY,
        )
        with self.assertRaises(NotImplementedError):
            self.granularity.get_first_period_index(date_range)
        with self.assertRaises(NotImplementedError):
            self.granularity.get_first_period_located_start_date(date_range)

    def test_unsupported_yearly_date_granularity(self):
        start_date = datetime.date(2024, 1, 1)
        end_date = datetime.date(2024, 12, 31)
        date_range = DateRange(
            start_date,
            end_date,
            DateGranularity.YEARLY,
        )
        with self.assertRaises(NotImplementedError):
            self.granularity.get_first_period_index(date_range)
        with self.assertRaises(NotImplementedError):
            self.granularity.get_first_period_located_start_date(date_range)


class SpanGranularityWeeklyTestCase(TestCase):

    def setUp(self):
        self.granularity = Weekly()

    def test_name(self):
        self.assertEqual(self.granularity.name, 'weekly')

    def test_daily_first_period_index(self):
        start_date = datetime.date(2024, 6, 18)
        end_date = datetime.date(2024, 6, 21)
        date_range = DateRange(
            start_date,
            end_date,
            DateGranularity.DAILY,
        )
        self.assertEqual(
            self.granularity.get_first_period_index(date_range),
            1,
        )

    def test_daily_first_period_located_start_date(self):
        start_date = datetime.date(2024, 6, 18)
        end_date = datetime.date(2024, 6, 21)
        date_range = DateRange(
            start_date,
            end_date,
            DateGranularity.DAILY,
        )
        self.assertEqual(
            self.granularity.get_first_period_located_start_date(date_range),
            datetime.date(2024, 6, 17),
        )

    def test_weekly_first_period_index(self):
        start_date = datetime.date(2024, 6, 3)
        end_date = datetime.date(2024, 6, 23)
        date_range = DateRange(
            start_date,
            end_date,
            DateGranularity.WEEKLY,
        )
        self.assertEqual(
            self.granularity.get_first_period_index(date_range),
            0,
        )

    def test_weekly_first_period_located_start_date(self):
        start_date = datetime.date(2024, 6, 3)
        end_date = datetime.date(2024, 6, 23)
        date_range = DateRange(
            start_date,
            end_date,
            DateGranularity.WEEKLY,
        )
        self.assertEqual(
            self.granularity.get_first_period_located_start_date(date_range),
            datetime.date(2024, 6, 3),
        )

    def test_unsupported_monthly_date_granularity(self):
        start_date = datetime.date(2024, 1, 1)
        end_date = datetime.date(2024, 1, 31)
        date_range = DateRange(
            start_date,
            end_date,
            DateGranularity.MONTHLY,
        )
        with self.assertRaises(NotImplementedError):
            self.granularity.get_first_period_index(date_range)
        with self.assertRaises(NotImplementedError):
            self.granularity.get_first_period_located_start_date(date_range)

    def test_unsupported_yearly_date_granularity(self):
        start_date = datetime.date(2024, 1, 1)
        end_date = datetime.date(2024, 12, 31)
        date_range = DateRange(
            start_date,
            end_date,
            DateGranularity.YEARLY,
        )
        with self.assertRaises(NotImplementedError):
            self.granularity.get_first_period_index(date_range)
        with self.assertRaises(NotImplementedError):
            self.granularity.get_first_period_located_start_date(date_range)


class SpanGranularityMonthlyTestCase(TestCase):

    def setUp(self):
        self.granularity = Monthly()

    def test_name(self):
        self.assertEqual(self.granularity.name, 'monthly')

    def test_daily_first_period_index(self):
        start_date = datetime.date(2024, 6, 18)
        end_date = datetime.date(2024, 6, 21)
        date_range = DateRange(
            start_date,
            end_date,
            DateGranularity.DAILY,
        )
        self.assertEqual(
            self.granularity.get_first_period_index(date_range),
            17,
        )

    def test_daily_first_period_located_start_date(self):
        start_date = datetime.date(2024, 6, 18)
        end_date = datetime.date(2024, 6, 21)
        date_range = DateRange(
            start_date,
            end_date,
            DateGranularity.DAILY,
        )
        self.assertEqual(
            self.granularity.get_first_period_located_start_date(date_range),
            datetime.date(2024, 6, 1),
        )

    def test_daily_first_period_index_in_leap_year_feb(self):
        start_date = datetime.date(2016, 2, 29)
        end_date = datetime.date(2016, 3, 14)
        date_range = DateRange(
            start_date,
            end_date,
            DateGranularity.DAILY,
        )
        self.assertEqual(
            self.granularity.get_first_period_index(date_range),
            28,
        )

    def test_weekly_first_period_index(self):
        start_date = datetime.date(2024, 2, 26)
        end_date = datetime.date(2024, 3, 10)
        date_range = DateRange(
            start_date,
            end_date,
            DateGranularity.WEEKLY,
        )
        self.assertEqual(
            self.granularity.get_first_period_index(date_range),
            4,
        )

    def test_weekly_first_period_located_start_date(self):
        start_date = datetime.date(2024, 2, 26)
        end_date = datetime.date(2024, 3, 10)
        date_range = DateRange(
            start_date,
            end_date,
            DateGranularity.WEEKLY,
        )
        self.assertEqual(
            self.granularity.get_first_period_located_start_date(date_range),
            datetime.date(2024, 1, 29),
        )

    def test_weekly_first_period_index_at_another_month(self):
        start_date = datetime.date(2024, 4, 29)
        end_date = datetime.date(2024, 5, 12)
        date_range = DateRange(
            start_date,
            end_date,
            DateGranularity.WEEKLY,
        )
        self.assertEqual(
            self.granularity.get_first_period_index(date_range),
            0,
        )

    def test_weekly_first_period_located_start_date_at_another_month(self):
        start_date = datetime.date(2024, 4, 29)
        end_date = datetime.date(2024, 5, 12)
        date_range = DateRange(
            start_date,
            end_date,
            DateGranularity.WEEKLY,
        )
        self.assertEqual(
            self.granularity.get_first_period_located_start_date(date_range),
            datetime.date(2024, 4, 29),
        )

    def test_monthly_first_period_index(self):
        start_date = datetime.date(2024, 1, 1)
        end_date = datetime.date(2024, 1, 31)
        date_range = DateRange(
            start_date,
            end_date,
            DateGranularity.MONTHLY,
        )
        self.assertEqual(
            self.granularity.get_first_period_index(date_range),
            0,
        )

    def test_monthly_first_period_located_start_date(self):
        start_date = datetime.date(2024, 1, 1)
        end_date = datetime.date(2024, 1, 31)
        date_range = DateRange(
            start_date,
            end_date,
            DateGranularity.MONTHLY,
        )
        self.assertEqual(
            self.granularity.get_first_period_located_start_date(date_range),
            datetime.date(2024, 1, 1),
        )

    def test_unsupported_yearly_date_granularity(self):
        start_date = datetime.date(2024, 1, 1)
        end_date = datetime.date(2024, 12, 31)
        date_range = DateRange(
            start_date,
            end_date,
            DateGranularity.YEARLY,
        )
        with self.assertRaises(NotImplementedError):
            self.granularity.get_first_period_index(date_range)
        with self.assertRaises(NotImplementedError):
            self.granularity.get_first_period_located_start_date(date_range)


class SpanGranularityYearlyTestCase(TestCase):

    def setUp(self):
        self.granularity = Yearly()

    def test_name(self):
        self.assertEqual(self.granularity.name, 'yearly')

    def test_daily_first_period_index(self):
        start_date = datetime.date(2024, 6, 18)
        end_date = datetime.date(2024, 6, 21)
        date_range = DateRange(
            start_date,
            end_date,
            DateGranularity.DAILY,
        )
        self.assertEqual(
            self.granularity.get_first_period_index(date_range),
            169,
        )

    def test_daily_first_period_located_start_date(self):
        start_date = datetime.date(2024, 6, 18)
        end_date = datetime.date(2024, 6, 21)
        date_range = DateRange(
            start_date,
            end_date,
            DateGranularity.DAILY,
        )
        self.assertEqual(
            self.granularity.get_first_period_located_start_date(date_range),
            datetime.date(2024, 1, 1),
        )

    def test_daily_first_period_index_in_leap_year(self):
        start_date = datetime.date(2024, 12, 31)
        end_date = datetime.date(2024, 12, 31)
        date_range = DateRange(
            start_date,
            end_date,
            DateGranularity.DAILY,
        )
        self.assertEqual(
            self.granularity.get_first_period_index(date_range),
            365,
        )

    def test_daily_first_period_located_start_date_in_leap_year(self):
        start_date = datetime.date(2024, 12, 31)
        end_date = datetime.date(2024, 12, 31)
        date_range = DateRange(
            start_date,
            end_date,
            DateGranularity.DAILY,
        )
        self.assertEqual(
            self.granularity.get_first_period_located_start_date(date_range),
            datetime.date(2024, 1, 1),
        )

    def test_weekly_first_period_index(self):
        start_date = datetime.date(2024, 6, 10)
        end_date = datetime.date(2024, 6, 23)
        date_range = DateRange(
            start_date,
            end_date,
            DateGranularity.WEEKLY,
        )
        self.assertEqual(
            self.granularity.get_first_period_index(date_range),
            23,
        )

    def test_weekly_first_period_located_start_date(self):
        start_date = datetime.date(2024, 6, 10)
        end_date = datetime.date(2024, 6, 23)
        date_range = DateRange(
            start_date,
            end_date,
            DateGranularity.WEEKLY,
        )
        self.assertEqual(
            self.granularity.get_first_period_located_start_date(date_range),
            datetime.date(2024, 1, 1),
        )

    def test_weekly_first_period_index_at_another_year(self):
        start_date = datetime.date(2018, 12, 31)
        end_date = datetime.date(2019, 1, 6)
        date_range = DateRange(
            start_date,
            end_date,
            DateGranularity.WEEKLY,
        )
        self.assertEqual(
            self.granularity.get_first_period_index(date_range),
            0,
        )

    def test_weekly_first_period_located_start_date_at_another_year(self):
        start_date = datetime.date(2018, 12, 31)
        end_date = datetime.date(2019, 1, 6)
        date_range = DateRange(
            start_date,
            end_date,
            DateGranularity.WEEKLY,
        )
        self.assertEqual(
            self.granularity.get_first_period_located_start_date(date_range),
            datetime.date(2018, 12, 31),
        )

    def test_weekly_first_period_index_at_fifty_week_year(self):
        start_date = datetime.date(2015, 12, 28)
        end_date = datetime.date(2016, 1, 3)
        date_range = DateRange(
            start_date,
            end_date,
            DateGranularity.WEEKLY,
        )
        self.assertEqual(
            self.granularity.get_first_period_index(date_range),
            52,
        )

    def test_weekly_first_period_located_start_date_at_fifty_week_year(self):
        start_date = datetime.date(2015, 12, 28)
        end_date = datetime.date(2016, 1, 3)
        date_range = DateRange(
            start_date,
            end_date,
            DateGranularity.WEEKLY,
        )
        self.assertEqual(
            self.granularity.get_first_period_located_start_date(date_range),
            datetime.date(2014, 12, 29),
        )

    def test_monthly_first_period_index(self):
        start_date = datetime.date(2023, 12, 1)
        end_date = datetime.date(2024, 6, 30)
        date_range = DateRange(
            start_date,
            end_date,
            DateGranularity.MONTHLY,
        )
        self.assertEqual(
            self.granularity.get_first_period_index(date_range),
            11,
        )

    def test_monthly_first_period_located_start_date(self):
        start_date = datetime.date(2023, 12, 1)
        end_date = datetime.date(2024, 6, 30)
        date_range = DateRange(
            start_date,
            end_date,
            DateGranularity.MONTHLY,
        )
        self.assertEqual(
            self.granularity.get_first_period_located_start_date(date_range),
            datetime.date(2023, 1, 1),
        )

    def test_yearly_first_period_index(self):
        start_date = datetime.date(2023, 1, 1)
        end_date = datetime.date(2024, 12, 31)
        date_range = DateRange(
            start_date,
            end_date,
            DateGranularity.YEARLY,
        )
        self.assertEqual(
            self.granularity.get_first_period_index(date_range),
            0,
        )

    def test_yearly_first_period_located_start_date(self):
        start_date = datetime.date(2023, 1, 1)
        end_date = datetime.date(2024, 12, 31)
        date_range = DateRange(
            start_date,
            end_date,
            DateGranularity.YEARLY,
        )
        self.assertEqual(
            self.granularity.get_first_period_located_start_date(date_range),
            datetime.date(2023, 1, 1),
        )


class SpanGranularityPeriodicTestCase(TestCase):

    def setUp(self):
        self.granularity = Periodic()

    def test_name(self):
        self.assertEqual(self.granularity.name, 'periodic')

    def test_daily_first_period_index(self):
        start_date = datetime.date(2024, 6, 18)
        end_date = datetime.date(2024, 6, 21)
        date_range = DateRange(
            start_date,
            end_date,
            DateGranularity.DAILY,
        )
        self.assertEqual(
            self.granularity.get_first_period_index(date_range),
            0,
        )

    def test_daily_first_period_located_start_date(self):
        start_date = datetime.date(2024, 6, 18)
        end_date = datetime.date(2024, 6, 21)
        date_range = DateRange(
            start_date,
            end_date,
            DateGranularity.DAILY,
        )
        self.assertEqual(
            self.granularity.get_first_period_located_start_date(date_range),
            datetime.date(2024, 6, 18),
        )

    def test_weekly_first_period_index(self):
        start_date = datetime.date(2024, 6, 10)
        end_date = datetime.date(2024, 6, 23)
        date_range = DateRange(
            start_date,
            end_date,
            DateGranularity.WEEKLY,
        )
        self.assertEqual(
            self.granularity.get_first_period_index(date_range),
            0,
        )

    def test_weekly_first_period_located_start_date(self):
        start_date = datetime.date(2024, 6, 10)
        end_date = datetime.date(2024, 6, 23)
        date_range = DateRange(
            start_date,
            end_date,
            DateGranularity.WEEKLY,
        )
        self.assertEqual(
            self.granularity.get_first_period_located_start_date(date_range),
            datetime.date(2024, 6, 10),
        )

    def test_monthly_first_period_index(self):
        start_date = datetime.date(2023, 12, 1)
        end_date = datetime.date(2024, 6, 30)
        date_range = DateRange(
            start_date,
            end_date,
            DateGranularity.MONTHLY,
        )
        self.assertEqual(
            self.granularity.get_first_period_index(date_range),
            0,
        )

    def test_monthly_first_period_located_start_date(self):
        start_date = datetime.date(2023, 12, 1)
        end_date = datetime.date(2024, 6, 30)
        date_range = DateRange(
            start_date,
            end_date,
            DateGranularity.MONTHLY,
        )
        self.assertEqual(
            self.granularity.get_first_period_located_start_date(date_range),
            datetime.date(2023, 12, 1),
        )

    def test_yearly_first_period_index(self):
        start_date = datetime.date(2023, 1, 1)
        end_date = datetime.date(2024, 12, 31)
        date_range = DateRange(
            start_date,
            end_date,
            DateGranularity.YEARLY,
        )
        self.assertEqual(
            self.granularity.get_first_period_index(date_range),
            0,
        )

    def test_yearly_first_period_located_start_date(self):
        start_date = datetime.date(2023, 1, 1)
        end_date = datetime.date(2024, 12, 31)
        date_range = DateRange(
            start_date,
            end_date,
            DateGranularity.YEARLY,
        )
        self.assertEqual(
            self.granularity.get_first_period_located_start_date(date_range),
            datetime.date(2023, 1, 1),
        )
