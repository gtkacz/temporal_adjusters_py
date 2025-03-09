import unittest
from datetime import date, datetime

from temporal_adjuster.temporal_adjuster import TemporalAdjuster


class TestAbsoluteDateOperations(unittest.TestCase):
	def test_int_to_day_of_year_single(self):
		"""Test int_to_day_of_year with a single date."""
		result = TemporalAdjuster.int_to_day_of_year(date(2021, 1, 1), 1)
		self.assertEqual(result, date(2021, 1, 1))

		result = TemporalAdjuster.int_to_day_of_year(date(2021, 6, 15), 180)
		self.assertEqual(result, date(2021, 6, 29))

		result = TemporalAdjuster.int_to_day_of_year(date(2021, 12, 31), 365)
		self.assertEqual(result, date(2021, 12, 31))

		dt = datetime(2021, 5, 10, 12, 30, 45)
		result = TemporalAdjuster.int_to_day_of_year(dt, 150)
		expected = datetime(2021, 5, 30, 12, 30, 45)
		self.assertEqual(result, expected)

	def test_int_to_day_of_year_sequence(self):
		"""Test int_to_day_of_year with a sequence of dates."""
		dates = [date(2021, 1, 1), date(2021, 6, 15), date(2021, 12, 31)]
		result = TemporalAdjuster.int_to_day_of_year(dates, 10)
		expected = [date(2021, 1, 10), date(2021, 1, 10), date(2021, 1, 10)]
		self.assertEqual(result, expected)

		result = TemporalAdjuster.int_to_day_of_year(date(2021, 5, 1), 1)
		expected = date(2021, 1, 1)
		self.assertEqual(result, expected)

		result = TemporalAdjuster.int_to_day_of_year(date(2021, 5, 1), 32)
		expected = date(2021, 2, 1)
		self.assertEqual(result, expected)

		result = TemporalAdjuster.int_to_day_of_year(date(2021, 5, 1), 60)
		expected = date(2021, 3, 1)
		self.assertEqual(result, expected)

		result = TemporalAdjuster.int_to_day_of_year(date(2021, 5, 1), 91)
		expected = date(2021, 4, 1)
		self.assertEqual(result, expected)

	def test_int_to_day_of_month_single(self):
		"""Test int_to_day_of_month with a single date."""
		result = TemporalAdjuster.int_to_day_of_month(date(2021, 1, 1), 1)
		self.assertEqual(result, date(2021, 1, 1))

		result = TemporalAdjuster.int_to_day_of_month(date(2021, 6, 15), 15)
		self.assertEqual(result, date(2021, 6, 15))

		result = TemporalAdjuster.int_to_day_of_month(date(2021, 12, 31), 31)
		self.assertEqual(result, date(2021, 12, 31))

		dt = datetime(2021, 5, 10, 12, 30, 45)
		result = TemporalAdjuster.int_to_day_of_month(dt, 20)
		expected = datetime(2021, 5, 20, 12, 30, 45)
		self.assertEqual(result, expected)

	def test_int_to_day_of_month_sequence(self):
		"""Test int_to_day_of_month with a sequence of dates."""
		dates = [date(2021, 1, 1), date(2021, 6, 15), date(2021, 12, 31)]
		result = TemporalAdjuster.int_to_day_of_month(dates, 10)
		expected = [date(2021, 1, 10), date(2021, 6, 10), date(2021, 12, 10)]
		self.assertEqual(result, expected)

		result = TemporalAdjuster.int_to_day_of_month(date(2021, 5, 1), 1)
		expected = date(2021, 5, 1)
		self.assertEqual(result, expected)

		result = TemporalAdjuster.int_to_day_of_month(date(2021, 5, 1), 15)
		expected = date(2021, 5, 15)
		self.assertEqual(result, expected)

		result = TemporalAdjuster.int_to_day_of_month(date(2021, 5, 1), 30)
		expected = date(2021, 5, 30)
		self.assertEqual(result, expected)

	def test_date_to_int_of_year_single(self):
		"""Test date_to_int_of_year with a single date."""
		result = TemporalAdjuster.date_to_int_of_year(date(2021, 1, 1))
		self.assertEqual(result, 1)

		result = TemporalAdjuster.date_to_int_of_year(date(2021, 7, 1))
		self.assertEqual(result, 182)

		result = TemporalAdjuster.date_to_int_of_year(date(2021, 12, 31))
		self.assertEqual(result, 365)

		result = TemporalAdjuster.date_to_int_of_year(date(2020, 12, 31))
		self.assertEqual(result, 366)

		dt = datetime(2021, 5, 10, 12, 30, 45)
		result = TemporalAdjuster.date_to_int_of_year(dt)
		self.assertEqual(result, 130)

	def test_date_to_int_of_year_sequence(self):
		"""Test date_to_int_of_year with a sequence of dates."""
		dates = [date(2021, 1, 1), date(2021, 2, 1), date(2021, 3, 1)]
		result = TemporalAdjuster.date_to_int_of_year(dates)
		expected = [1, 32, 60]
		self.assertEqual(result, expected)

		dates = [date(2021, 1, 1), datetime(2021, 2, 1, 12, 0, 0), date(2021, 3, 1)]
		result = TemporalAdjuster.date_to_int_of_year(dates)
		expected = [1, 32, 60]
		self.assertEqual(result, expected)

		dates = [date(2020, 3, 1), date(2021, 3, 1)]
		result = TemporalAdjuster.date_to_int_of_year(dates)
		self.assertEqual(result, expected)

	def test_date_to_int_of_month_single(self):
		"""Test date_to_int_of_month with a single date."""
		result = TemporalAdjuster.date_to_int_of_month(date(2021, 1, 1))
		self.assertEqual(result, 1)

		result = TemporalAdjuster.date_to_int_of_month(date(2021, 6, 15))
		self.assertEqual(result, 15)

		result = TemporalAdjuster.date_to_int_of_month(date(2021, 12, 31))
		self.assertEqual(result, 31)

		dt = datetime(2021, 5, 10, 12, 30, 45)
		result = TemporalAdjuster.date_to_int_of_month(dt)
		self.assertEqual(result, 10)

	def test_date_to_int_of_month_sequence(self):
		"""Test date_to_int_of_month with a sequence of dates."""
		dates = [date(2021, 1, 1), date(2021, 6, 15), date(2021, 12, 31)]
		result = TemporalAdjuster.date_to_int_of_month(dates)
		expected = [1, 15, 31]
		self.assertEqual(result, expected)

		dates = [date(2021, 1, 5), datetime(2021, 2, 10, 12, 0, 0), date(2021, 3, 15)]
		result = TemporalAdjuster.date_to_int_of_month(dates)
		expected = [5, 10, 15]
		self.assertEqual(result, expected)

	def test_edge_cases(self):
		"""Test edge cases and potential error conditions."""
		result = TemporalAdjuster.int_to_day_of_year(date(2020, 1, 1), 60)
		self.assertEqual(result, date(2020, 2, 29))

		result = TemporalAdjuster.date_to_int_of_year([])
		self.assertEqual(result, [])

		result = TemporalAdjuster.date_to_int_of_month([date(2021, 5, 20)])
		self.assertEqual(result, [20])
