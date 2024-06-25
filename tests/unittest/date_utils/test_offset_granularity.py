from unittest import TestCase

from deloreans.date_utils.offset_granularity import DatePeriodOffset, OffsetGranularity


class DatePeriodOffsetTestCase(TestCase):

    def test_offset(self):
        sample_offset = 1
        sample_offset_granularity = OffsetGranularity.DAILY
        date_period_offset = DatePeriodOffset(sample_offset, sample_offset_granularity)

        self.assertEqual(date_period_offset.offset, 1)

    def test_offset_granularity(self):
        sample_offset = 1
        sample_offset_granularity = OffsetGranularity.DAILY
        date_period_offset = DatePeriodOffset(sample_offset, sample_offset_granularity)

        self.assertEqual(date_period_offset.offset_granularity, OffsetGranularity.DAILY)

    def test_invalid_offset_type(self):
        sample_offset = '1'
        offset_granularity = OffsetGranularity.DAILY

        with self.assertRaises(TypeError):
            DatePeriodOffset(sample_offset, offset_granularity)  # NOQA

    def test_invalid_offset_granularity(self):
        sample_offset = 1
        sample_offset_granularity = 'daily'

        with self.assertRaises(TypeError):
            DatePeriodOffset(sample_offset, sample_offset_granularity)  # NOQA
