from unittest import TestCase
from datetime import date, timedelta

from nba_data.data.date_range import DateRange


class TestDateRange(TestCase):
    start = date(year=2015, month=1, day=1)
    end = date(year=2015, month=1, day=2)

    def test_instantiation(self):
        self.assertIsNotNone(DateRange(start=TestDateRange.start, end=TestDateRange.end))
        self.assertRaises(AssertionError, DateRange, 1, TestDateRange.end)
        self.assertRaises(AssertionError, DateRange, TestDateRange.start, 1)
        self.assertRaises(AssertionError, DateRange, TestDateRange.start, TestDateRange.start - timedelta(days=1))

    def test_is_date_in_range(self):
        date_range = DateRange(TestDateRange.start, TestDateRange.end)
        self.assertFalse(date_range.is_date_in_range(value=TestDateRange.start - timedelta(days=1)))
        self.assertFalse(date_range.is_date_in_range(value=TestDateRange.end + timedelta(days=1)))
        self.assertTrue(date_range.is_date_in_range(value=TestDateRange.start))

