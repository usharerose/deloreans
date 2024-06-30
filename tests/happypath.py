import datetime
from unittest import TestCase

import deloreans
from deloreans import DateGranularity, OffsetGranularity


class HappyPathTestCase(TestCase):

    def test_daily_period_year_over_year_comparison(self):
        """
        Compare daily date period (2024-03-01 ~ 2024-03-31)
        with another one which is at previous year

        2024 is a leap year which has 31 (Jan) + 29 (Feb) = 60 days before Mar 1st

        With consistent beginning position,
        the compared daily period would also start from the 61st day of the year
        so that the start date of compared date period within non-leap year
        would be Mar 2nd which also has 31 (Jan) + 28 (Feb) + 1 (Mar 1st) = 60 days before it

        With consistency of date period size,
        the compared daily period would also have same amount of days (31 days)
        which are 30 (Mar 2nd to Mar 31st) + 1 (Apr 1st)

        ##############################################################################################
                                                     2024
                  January                          February                          March
        Mon Tue Wed Thu Fri Sat Sun      Mon Tue Wed Thu Fri Sat Sun      Mon Tue Wed Thu Fri Sat Sun
          1   2   3   4   5   6   7                    1   2   3   4                       [1   2   3
          8   9  10  11  12  13  14        5   6   7   8   9  10  11        4   5   6   7   8   9  10
         15  16  17  18  19  20  21       12  13  14  15  16  17  18       11  12  13  14  15  16  17
         22  23  24  25  26  27  28       19  20  21  22  23  24  25       18  19  20  21  22  23  24
         29  30  31                       26  27  28 *29                   25  26  27  28  29  30  31]
        ##############################################################################################
                                                     2023
                  January                          February                          March
        Mon Tue Wed Thu Fri Sat Sun      Mon Tue Wed Thu Fri Sat Sun      Mon Tue Wed Thu Fri Sat Sun
                                  1                1   2   3   4   5                1  [2   3   4   5
          2   3   4   5   6   7   8        6   7   8   9  10  11  12        6   7   8   9  10  11  12
          9  10  11  12  13  14  15       13  14  15  16  17  18  19       13  14  15  16  17  18  19
         16  17  18  19  20  21  22       20  21  22  23  24  25  26       20  21  22  23  24  25  26
         23  24  25  26  27  28  29       27  28                           27  28  29  30  31
         30  31
                   April
        Mon Tue Wed Thu Fri Sat Sun
                             1]   2
          3   4   5   6   7  8    9
         10  11  12  13  14 15   16
         17  18  19  20  21 22   23
         24  25  26  27  28 29   30
        ##############################################################################################
        """
        sample_kwargs = {
            'start_date': datetime.date(2024, 3, 1),
            'end_date': datetime.date(2024, 3, 31),
            'date_granularity': DateGranularity.DAILY,
            'offset': -1,
            'offset_granularity': OffsetGranularity.YEARLY,
        }
        actual_start_date, actual_end_date = deloreans.get(**sample_kwargs)

        expected_start_date = datetime.date(2023, 3, 2)
        expected_end_date = datetime.date(2023, 4, 1)

        self.assertEqual(actual_start_date, expected_start_date)
        self.assertEqual(actual_end_date, expected_end_date)

    def test_monthly_period_year_over_year_comparison(self):
        """
        If assumed the date period 2024-03-01 ~ 2024-03-31
        should be compared with any year's 03-01 ~ 03-31,

        the granularity of date period has changed from daily to monthly,
        which means compare Mar 2024 with any year's March.

        e.g. Mar 2019 v.s. Mar 2024,
        March is always the third month of a year,
        and the start date and end date of a month is consistent in both leap and non-leap year
        #################################
             2023                2023
        Jan Feb [Mar]       Jan Feb [Mar]
        Apr May   Jun       Apr May   Jun
        Jul Aug   Sep       Jul Aug   Sep
        Oct Nov   Dec       Oct Nov   Dec
        #################################
        """
        sample_kwargs = {
            'start_date': datetime.date(2024, 3, 1),
            'end_date': datetime.date(2024, 3, 31),
            'date_granularity': DateGranularity.MONTHLY,
            'offset': -5,
            'offset_granularity': OffsetGranularity.YEARLY,
        }
        actual_start_date, actual_end_date = deloreans.get(**sample_kwargs)

        expected_start_date = datetime.date(2019, 3, 1)
        expected_end_date = datetime.date(2019, 3, 31)

        self.assertEqual(actual_start_date, expected_start_date)
        self.assertEqual(actual_end_date, expected_end_date)

    def test_weekly_period_year_over_year_comparison(self):
        """
        DeLoreans refers to ISO 8601's core definition to determine that
        which month / year that a week located:

        The month / year that the majority (4 or more days) of a week locate at.

        In this case's scenario, the given weeks would be year-on-year compared with
        the same weeks in another year:

        e.g. W01 ~ W13 2024 v.s. W01 ~ W13 2015

        ##########################################################################################################
                                                             2024
                      January                              February                              March
            Mon Tue Wed Thu Fri Sat Sun          Mon Tue Wed Thu Fri Sat Sun          Mon Tue Wed Thu Fri Sat Sun
        W01   1   2   3   4   5   6   7      W05               1   2   3   4      W09                   1   2   3
        W02   8   9  10  11  12  13  14      W06   5   6   7   8   9  10  11      W10   4   5   6   7   8   9  10
        W03  15  16  17  18  19  20  21      W07  12  13  14  15  16  17  18      W11  11  12  13  14  15  16  17
        W04  22  23  24  25  26  27  28      W08  19  20  21  22  23  24  25      W12  18  19  20  21  22  23  24
        W05  29  30  31                      W09  26  27  28  29                  W13  25  26  27  28  29  30  31
        ##########################################################################################################
                                                             2015
                      January                              February                              March
            Mon Tue Wed Thu Fri Sat Sun          Mon Tue Wed Thu Fri Sat Sun          Mon Tue Wed Thu Fri Sat Sun
        W01               1   2   3   4      W05                           1      W09                           1
        W02   5   6   7   8   9  10  11      W06   2   3   4   5   6   7   8      W10   2   3   4   5   6   7   8
        W03  12  13  14  15  16  17  18      W07   9  10  11  12  13  14  15      W11   9  10  11  12  13  14  15
        W04  19  20  21  22  23  24  25      W08  16  17  18  19  20  21  22      W12  16  17  18  19  20  21  22
        W05  26  27  28  29  30  31          W09  23  24  25  26  27  28          W13  23  24  25  26  27  28  29
                                                                                  W14  30  31
        ##########################################################################################################
        """
        sample_kwargs = {
            'start_date': datetime.date(2024, 1, 1),
            'end_date': datetime.date(2024, 3, 31),
            'date_granularity': DateGranularity.WEEKLY,
            'offset': -9,
            'offset_granularity': OffsetGranularity.YEARLY,
        }
        actual_start_date, actual_end_date = deloreans.get(**sample_kwargs)
        expected_start_date = datetime.date(2014, 12, 29)
        expected_end_date = datetime.date(2015, 3, 29)
        self.assertEqual(actual_start_date, expected_start_date)
        self.assertEqual(actual_end_date, expected_end_date)

    def test_weekly_period_with_sunday_first_year_over_year_comparison(self):
        """
        DeLoreans allow user to to customize the start weekday of week:
          * ISO:                   Monday to Sunday
          * US system:             Sunday to Saturday
          * Some Muslim countries: Saturday to Friday

        However, week ownership still follow the 'majority' rule,
        which make no partial weeks, and week can be allocated to a single month / year.

        In this case's scenario, the two sides of the comparison are the same as last case that:
          * W01 ~ W13 2024 v.s. W01 ~ W13 2015, but week starts from Sunday instead

        ##########################################################################################################
                                                             2024
                      January                              February                              March
            Sun Mon Tue Wed Thu Fri Sat          Sun Mon Tue Wed Thu Fri Sat          Sun Mon Tue Wed Thu Fri Sat
        W01       1   2   3   4   5   6      W05                   1   2   3      W09                       1   2
        W02   7   8   9  10  11  12  13      W06  4   5   6   7   8   9  10       W10   3   4   5   6   7   8   9
        W03  14  15  16  17  18  19  20      W07 11  12  13  14  15  16  17       W11  10  11  12  13  14  15  16
        W04  21  22  23  24  25  26  27      W08 18  19  20  21  22  23  24       W12  17  18  19  20  21  22  23
        W05  28  29  30  31                  W09 25  26  27  28  29               W13  24  25  26  27  28  29  30
                                                                                  W14  31
        ##########################################################################################################
                                                             2015
                      January                             February                               March
            Sun Mon Tue Wed Thu Fri Sat          Sun Mon Tue Wed Thu Fri Sat          Sun Mon Tue Wed Thu Fri Sat
        W52                   1   2   3      W05   1   2   3   4   5   6   7      W09   1   2   3   4   5   6   7
        W01   4   5   6   7   8   9  10      W06   8   9  10  11  12  13  14      W10   8   9  10  11  12  13  14
        W02  11  12  13  14  15  16  17      W07  15  16  17  18  19  20  21      W11  15  16  17  18  19  20  21
        W03  18  19  20  21  22  23  24      W08  22  23  24  25  26  27  28      W12  22  23  24  25  26  27  28
        W04  25  26  27  28  29  30  31                                           W13  29  30  31
        * In this scenario, Jan 1st, 2015 would allocate to W52 2014 instead of W01 2015
        ##########################################################################################################
        """
        sample_kwargs = {
            'start_date': datetime.date(2023, 12, 31),
            'end_date': datetime.date(2024, 3, 30),
            'date_granularity': DateGranularity.WEEKLY,
            'offset': -9,
            'offset_granularity': OffsetGranularity.YEARLY,
            'firstweekday': 6,
        }
        actual_start_date, actual_end_date = deloreans.get(**sample_kwargs)
        expected_start_date = datetime.date(2015, 1, 4)
        expected_end_date = datetime.date(2015, 4, 4)
        self.assertEqual(actual_start_date, expected_start_date)
        self.assertEqual(actual_end_date, expected_end_date)

    def test_monthly_period_standing_for_first_half_in_year_year_over_year_comparison(self):
        """
        Comparing 1st half year performance with various years is a common scenario.

        You can declare monthly date range with multiple periods which can represent half year,
        since,
          * 1st half year is always January to June
          * 2nd half year is always July to December
        """
        sample_kwargs = {
            'start_date': datetime.date(2024, 1, 1),
            'end_date': datetime.date(2024, 6, 30),
            'date_granularity': DateGranularity.MONTHLY,
            'offset': -1,
            'offset_granularity': OffsetGranularity.YEARLY,
        }
        actual_start_date, actual_end_date = deloreans.get(**sample_kwargs)
        expected_start_date = datetime.date(2023, 1, 1)
        expected_end_date = datetime.date(2023, 6, 30)
        self.assertEqual(actual_start_date, expected_start_date)
        self.assertEqual(actual_end_date, expected_end_date)

    def test_monthly_period_standing_for_quarter_in_year_year_over_year_comparison(self):
        """
        Also, quarterly comparison is a common scenario
        which also can be represented by multiple monthly periods

        e.g. 2024 Q2 v.s. 2023 Q2, which Q2 is always: April, May and June
        """
        sample_kwargs = {
            'start_date': datetime.date(2024, 4, 1),
            'end_date': datetime.date(2024, 6, 30),
            'date_granularity': DateGranularity.MONTHLY,
            'offset': -1,
            'offset_granularity': OffsetGranularity.YEARLY,
        }
        actual_start_date, actual_end_date = deloreans.get(**sample_kwargs)
        expected_start_date = datetime.date(2023, 4, 1)
        expected_end_date = datetime.date(2023, 6, 30)
        self.assertEqual(actual_start_date, expected_start_date)
        self.assertEqual(actual_end_date, expected_end_date)

    def test_monthly_period_month_over_month(self):
        """
        It allows user to get the previous date range next to the given one,
        with same granularity and amount of unit date periods

        e.g. 2024 May ~ June, compared with the previous one,
             which is March ~ April that two months
        """
        sample_kwargs = {
            'start_date': datetime.date(2024, 5, 1),
            'end_date': datetime.date(2024, 6, 30),
            'date_granularity': DateGranularity.MONTHLY,
            'offset': -1,
            'offset_granularity': OffsetGranularity.PERIODIC,
        }
        actual_start_date, actual_end_date = deloreans.get(**sample_kwargs)
        expected_start_date = datetime.date(2024, 3, 1)
        expected_end_date = datetime.date(2024, 4, 30)
        self.assertEqual(actual_start_date, expected_start_date)
        self.assertEqual(actual_end_date, expected_end_date)

    def test_weekly_period_week_over_week(self):
        """
        Not only monthly period, but also any granularity (e.g. weekly),
        can do it

        e.g. 2024 W01 ~ W04, compared with the previous weeks,
             which is 2023 W49 ~ W52

             ...
             | 2023 W45 ~ W48 |
             | 2023 W49 ~ W52 |  * expected
             | 2024 W01 ~ W04 |  given
             | 2024 W05 ~ W08 |
             | 2024 W09 ~ W12 |
             ...
        """
        sample_kwargs = {
            'start_date': datetime.date(2024, 1, 1),
            'end_date': datetime.date(2024, 1, 28),
            'date_granularity': DateGranularity.WEEKLY,
            'offset': -1,
            'offset_granularity': OffsetGranularity.PERIODIC,
        }
        actual_start_date, actual_end_date = deloreans.get(**sample_kwargs)
        expected_start_date = datetime.date(2023, 12, 4)
        expected_end_date = datetime.date(2023, 12, 31)
        self.assertEqual(actual_start_date, expected_start_date)
        self.assertEqual(actual_end_date, expected_end_date)

    def test_weekly_period_week_over_week_with_gap(self):
        """
        You can change the value offset, making two date ranges have gaps

        e.g. 2024 W01 ~ W04, compared with the last one before that,
             which is 2023 W45 ~ W48
             contains one date range with same length between them


             ...
             | 2023 W45 ~ W48 |  * expected
             | 2023 W49 ~ W52 |
             | 2024 W01 ~ W04 |  given
             | 2024 W05 ~ W08 |
             | 2024 W09 ~ W12 |
             ...
        """
        sample_kwargs = {
            'start_date': datetime.date(2024, 1, 1),
            'end_date': datetime.date(2024, 1, 28),
            'date_granularity': DateGranularity.WEEKLY,
            'offset': -2,
            'offset_granularity': OffsetGranularity.PERIODIC,
        }
        actual_start_date, actual_end_date = deloreans.get(**sample_kwargs)
        expected_start_date = datetime.date(2023, 11, 6)
        expected_end_date = datetime.date(2023, 12, 3)
        self.assertEqual(actual_start_date, expected_start_date)
        self.assertEqual(actual_end_date, expected_end_date)
