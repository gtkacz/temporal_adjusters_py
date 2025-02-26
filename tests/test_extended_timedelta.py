import pickle
import unittest
from datetime import timedelta

from temporal_adjuster.common.types.dates import ExtendedTimeDelta


class TestExtendedTimeDelta(unittest.TestCase):
	def setUp(self):
		# Save original class attributes to restore after each test
		self.original_days_in_month = 30
		self.original_days_in_year = 365

	def tearDown(self):
		# Restore class attributes to their original state
		if self.original_days_in_month is not None:
			ExtendedTimeDelta.DAYS_IN_MONTH = self.original_days_in_month
		else:
			if hasattr(ExtendedTimeDelta, 'DAYS_IN_MONTH'):
				del ExtendedTimeDelta.DAYS_IN_MONTH
		if self.original_days_in_year is not None:
			ExtendedTimeDelta.DAYS_IN_YEAR = self.original_days_in_year
		else:
			if hasattr(ExtendedTimeDelta, 'DAYS_IN_YEAR'):
				del ExtendedTimeDelta.DAYS_IN_YEAR

	def test_initialization_default(self):
		et = ExtendedTimeDelta()
		self.assertEqual(et.years, 0)
		self.assertEqual(et.months, 0)
		self.assertEqual(et.days, 0)
		self.assertEqual(et.seconds, 0)
		self.assertEqual(et.microseconds, 0)

	def test_initialization_years_months(self):
		et = ExtendedTimeDelta(years=2, months=6)
		self.assertEqual(et.years, 2)
		self.assertEqual(et.months, 6)
		self.assertEqual(et.days, 0)

	def test_initialization_days_conversion(self):
		et = ExtendedTimeDelta(days=30, days_in_month=30)
		self.assertEqual(et.months, 1)
		self.assertEqual(et.days, 0)

	def test_initialization_fractional_years(self):
		et = ExtendedTimeDelta(years=1.5)
		self.assertEqual(et.years, 1)
		self.assertEqual(et.months, 6)

	def test_initialization_fractional_months(self):
		et = ExtendedTimeDelta(months=1.5)
		self.assertEqual(et.months, 1)
		self.assertEqual(et.days, 15)
		self.assertEqual(et.seconds, 18873)
		self.assertEqual(et.microseconds, 0)

	def test_initialization_fractional_days(self):
		et = ExtendedTimeDelta(days=1.5)
		self.assertEqual(et.days, 1)
		self.assertEqual(et.seconds, 43200)

	def test_initialization_negative_days(self):
		et = ExtendedTimeDelta(days=-5, days_in_month=30)
		self.assertEqual(et.years, -1)
		self.assertEqual(et.months, 11)
		self.assertEqual(et.days, 25)

	def test_properties(self):
		et = ExtendedTimeDelta(years=3, months=4, days=5, seconds=6, microseconds=7)
		self.assertEqual(et.years, 3)
		self.assertEqual(et.months, 4)
		self.assertEqual(et.days, 5)
		self.assertEqual(et.seconds, 6)
		self.assertEqual(et.microseconds, 7)

	def test_add_extended_timedelta(self):
		et1 = ExtendedTimeDelta(years=1, months=2)
		et2 = ExtendedTimeDelta(months=3, days=4)
		result = et1 + et2
		self.assertEqual(result.years, 1)
		self.assertEqual(result.months, 5)
		self.assertEqual(result.days, 4)

	def test_add_timedelta(self):
		et = ExtendedTimeDelta(days=5)
		td = timedelta(days=3)
		result = et + td
		self.assertEqual(result.days, 8)

	def test_sub_extended_timedelta(self):
		et1 = ExtendedTimeDelta(years=2, months=5)
		et2 = ExtendedTimeDelta(years=1, months=3)
		result = et1 - et2
		self.assertEqual(result.years, 1)
		self.assertEqual(result.months, 2)

	def test_sub_timedelta(self):
		et = ExtendedTimeDelta(days=10)
		td = timedelta(days=3)
		result = et - td
		self.assertEqual(result.days, 7)

	def test_multiply_by_int(self):
		et = ExtendedTimeDelta(years=1, months=2)
		result = et * 2
		self.assertEqual(result.years, 2)
		self.assertEqual(result.months, 4)

	def test_equality(self):
		et1 = ExtendedTimeDelta(years=1, months=2)
		et2 = ExtendedTimeDelta(years=1, months=2)
		self.assertEqual(et1, et2)

	def test_equality_with_timedelta(self):
		et = ExtendedTimeDelta(days=5)
		td = timedelta(days=5)
		self.assertEqual(et, td)

	def test_comparison(self):
		et1 = ExtendedTimeDelta(years=2)
		et2 = ExtendedTimeDelta(years=1)
		self.assertGreater(et1, et2)
		self.assertLess(et2, et1)
		self.assertGreaterEqual(et1, et2)
		self.assertLessEqual(et2, et1)

	def test_repr(self):
		et = ExtendedTimeDelta(years=1, months=2, days=3, seconds=4, microseconds=5)
		expected = (
			'ExtendedTimeDelta(years=1, months=2, days=3, seconds=4, microseconds=5)'
		)
		self.assertEqual(repr(et), expected)

	def test_str_singular_plural(self):
		et = ExtendedTimeDelta(years=1, months=2, days=3, seconds=7200)
		self.assertEqual(str(et), '1 year, 2 months, 3 days, 2:00:00')

	def test_hash(self):
		et1 = ExtendedTimeDelta(years=1, months=2)
		et2 = ExtendedTimeDelta(years=1, months=2)
		self.assertEqual(hash(et1), hash(et2))

	def test_pickle(self):
		et = ExtendedTimeDelta(years=1, months=2, days=3)
		pickled = pickle.dumps(et)
		unpickled = pickle.loads(pickled)
		self.assertEqual(et, unpickled)

	def test_from_timedelta(self):
		td = timedelta(days=30)
		et = ExtendedTimeDelta.from_timedelta(td)
		self.assertEqual(et.days, 30)

	def test_to_timedelta(self):
		et = ExtendedTimeDelta(days=5)
		td = et.to_timedelta()
		self.assertEqual(td, timedelta(days=5))

	def test_to_seconds(self):
		et = ExtendedTimeDelta(days=1)
		self.assertEqual(et.to_seconds(), 86400.0)

	def test_to_days(self):
		et = ExtendedTimeDelta(months=1, days_in_month=30)
		self.assertAlmostEqual(et.to_days(), 30.0)

	def test_custom_days_in_month(self):
		et = ExtendedTimeDelta(months=1, days_in_month=30)
		self.assertEqual(et.to_timedelta().days, 30)
