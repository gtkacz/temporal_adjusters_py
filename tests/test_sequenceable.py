from datetime import date
from unittest import TestCase

from pandas import Series
from pandas.testing import assert_series_equal

from temporal_adjuster.common.enums import Weekday
from temporal_adjuster.temporal_adjuster import TemporalAdjuster


class TestSequenceable(TestCase):
	# Weekday operations module
	def test_next_success(self):
		tests = [
			(
				Weekday.SATURDAY,
				[date(2024, 6, 13), date(2024, 6, 15)],
				[date(2024, 6, 15), date(2024, 6, 22)],
				self.assertListEqual,
			),
			(
				Weekday.SATURDAY,
				set([date(2024, 6, 13), date(2024, 6, 15)]),
				set([date(2024, 6, 15), date(2024, 6, 22)]),
				self.assertSetEqual,
			),
			(
				Weekday.SATURDAY,
				tuple([date(2024, 6, 13), date(2024, 6, 15)]),
				tuple([date(2024, 6, 15), date(2024, 6, 22)]),
				self.assertTupleEqual,
			),
			(
				Weekday.SATURDAY,
				Series([date(2024, 6, 13), date(2024, 6, 15)]),
				Series([date(2024, 6, 15), date(2024, 6, 22)]),
				assert_series_equal,
			),
		]

		for index, test in enumerate(tests):
			with self.subTest(
				f'Testing method next (subtest {index}) with inputs: {test}'
			):
				(
					test_input_weekday,
					test_input_date,
					test_expected_output,
					assertion_method,
				) = test

				assertion_method(
					TemporalAdjuster.next(test_input_weekday, test_input_date),
					test_expected_output,
				)

	# First and last day operations module
	def test_first_day_of_next_week_success(self):
		tests = [
			(
				[date(2024, 6, 13), date(2024, 12, 31)],
				[date(2024, 6, 17), date(2025, 1, 6)],
				self.assertListEqual,
			),
			(
				set([date(2024, 6, 13), date(2024, 12, 31)]),
				set([date(2024, 6, 17), date(2025, 1, 6)]),
				self.assertSetEqual,
			),
			(
				tuple([date(2024, 6, 13), date(2024, 12, 31)]),
				tuple([date(2024, 6, 17), date(2025, 1, 6)]),
				self.assertTupleEqual,
			),
			(
				Series([date(2024, 6, 13), date(2024, 12, 31)]),
				Series([date(2024, 6, 17), date(2025, 1, 6)]),
				assert_series_equal,
			),
		]

		for index, test in enumerate(tests):
			with self.subTest(
				f'Testing method next (subtest {index}) with inputs: {test}'
			):
				test_input_date, test_expected_output, assertion_method = test

				assertion_method(
					TemporalAdjuster.first_day_of_next_week(test_input_date),
					test_expected_output,
				)
