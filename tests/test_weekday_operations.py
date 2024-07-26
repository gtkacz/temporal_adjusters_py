from datetime import date, datetime
from unittest import TestCase

from temporal_adjuster.common.enums import ISOWeekday, Weekday
from temporal_adjuster.common.exceptions import DateError
from temporal_adjuster.temporal_adjuster import TemporalAdjuster


class TestTemporalAdjusterForWeekdays(TestCase):
	def test_next_success(self):
		tests = [
			(Weekday.SATURDAY, date(2024, 6, 13), date(2024, 6, 15)),
			(Weekday.SATURDAY, date(2024, 6, 15), date(2024, 6, 22)),
			(Weekday.SATURDAY, date(2024, 12, 31), date(2025, 1, 4)),
			(ISOWeekday.SATURDAY, datetime(2024, 6, 13), datetime(2024, 6, 15)),
			(ISOWeekday.SATURDAY, datetime(2024, 6, 15), datetime(2024, 6, 22)),
			(ISOWeekday.SATURDAY, datetime(2024, 12, 31), datetime(2025, 1, 4)),
			('SATURDAY', datetime(2024, 6, 13), datetime(2024, 6, 15)),
			('SATURDAY', datetime(2024, 6, 15), datetime(2024, 6, 22)),
			('SATURDAY', datetime(2024, 12, 31), datetime(2025, 1, 4)),
			(5, datetime(2024, 6, 13), datetime(2024, 6, 15)),
			(5, datetime(2024, 6, 15), datetime(2024, 6, 22)),
			(5, datetime(2024, 12, 31), datetime(2025, 1, 4)),
		]

		for index, test in enumerate(tests):
			with self.subTest(
				f'Testing method next (subtest {index}) with inputs: {test}'
			):
				test_input_weekday, test_input_date, test_expected_output = test

				output = TemporalAdjuster.next(test_input_weekday, test_input_date)

				self.assertEqual(
					output,
					test_expected_output,
				)

				self.assertEqual(output.weekday(), test_expected_output.weekday())

	def test_next_or_same_success(self):
		tests = [
			(Weekday.SATURDAY, date(2024, 6, 13), date(2024, 6, 15)),
			(Weekday.SATURDAY, date(2024, 6, 15), date(2024, 6, 15)),
			(Weekday.SATURDAY, date(2024, 12, 31), date(2025, 1, 4)),
			(ISOWeekday.SATURDAY, datetime(2024, 6, 13), datetime(2024, 6, 15)),
			(ISOWeekday.SATURDAY, datetime(2024, 6, 15), datetime(2024, 6, 15)),
			(ISOWeekday.SATURDAY, datetime(2024, 12, 31), datetime(2025, 1, 4)),
		]

		for index, test in enumerate(tests):
			with self.subTest(
				f'Testing method next_or_same (subtest {index}) with inputs: {test}'
			):
				test_input_weekday, test_input_date, test_expected_output = test

				output = TemporalAdjuster.next_or_same(
					test_input_weekday, test_input_date
				)

				self.assertEqual(
					output,
					test_expected_output,
				)

				self.assertEqual(output.weekday(), test_expected_output.weekday())

	def test_last_success(self):
		tests = [
			(Weekday.SATURDAY, date(2024, 6, 13), date(2024, 6, 8)),
			(Weekday.SATURDAY, date(2024, 6, 15), date(2024, 6, 8)),
			(Weekday.SATURDAY, date(2025, 1, 1), date(2024, 12, 28)),
			(ISOWeekday.SATURDAY, datetime(2024, 6, 13), datetime(2024, 6, 8)),
			(ISOWeekday.SATURDAY, datetime(2024, 6, 15), datetime(2024, 6, 8)),
			(ISOWeekday.SATURDAY, datetime(2025, 1, 1), datetime(2024, 12, 28)),
		]

		for index, test in enumerate(tests):
			with self.subTest(
				f'Testing method last (subtest {index}) with inputs: {test}'
			):
				test_input_weekday, test_input_date, test_expected_output = test

				output = TemporalAdjuster.last(test_input_weekday, test_input_date)

				self.assertEqual(
					output,
					test_expected_output,
				)

				self.assertEqual(output.weekday(), test_expected_output.weekday())

	def test_last_or_same_success(self):
		tests = [
			(Weekday.SATURDAY, date(2024, 6, 13), date(2024, 6, 8)),
			(Weekday.SATURDAY, date(2024, 6, 15), date(2024, 6, 15)),
			(Weekday.SATURDAY, date(2025, 1, 1), date(2024, 12, 28)),
			(ISOWeekday.SATURDAY, datetime(2024, 6, 13), datetime(2024, 6, 8)),
			(ISOWeekday.SATURDAY, datetime(2024, 6, 15), datetime(2024, 6, 15)),
			(ISOWeekday.SATURDAY, datetime(2025, 1, 1), datetime(2024, 12, 28)),
		]

		for index, test in enumerate(tests):
			with self.subTest(
				f'Testing method last_or_same (subtest {index}) with inputs: {test}'
			):
				test_input_weekday, test_input_date, test_expected_output = test

				output = TemporalAdjuster.last_or_same(
					test_input_weekday, test_input_date
				)

				self.assertEqual(
					output,
					test_expected_output,
				)

				self.assertEqual(output.weekday(), test_expected_output.weekday())

	def test_first_of_month_success(self):
		tests = [
			(Weekday.SATURDAY, date(2024, 6, 13), date(2024, 6, 1)),
			(Weekday.SATURDAY, date(2024, 6, 15), date(2024, 6, 1)),
			(Weekday.SATURDAY, date(2025, 1, 1), date(2025, 1, 4)),
			(ISOWeekday.SATURDAY, datetime(2024, 6, 13), datetime(2024, 6, 1)),
			(ISOWeekday.SATURDAY, datetime(2024, 6, 15), datetime(2024, 6, 1)),
			(ISOWeekday.SATURDAY, datetime(2025, 1, 1), datetime(2025, 1, 4)),
		]

		for index, test in enumerate(tests):
			with self.subTest(
				f'Testing method first_of_month (subtest {index}) with inputs: {test}'
			):
				test_input_weekday, test_input_date, test_expected_output = test

				output = TemporalAdjuster.first_of_month(
					test_input_weekday, test_input_date
				)

				self.assertEqual(
					output,
					test_expected_output,
				)

				self.assertEqual(output.weekday(), test_expected_output.weekday())

	def test_first_of_next_month_success(self):
		tests = [
			(Weekday.SATURDAY, date(2024, 6, 13), date(2024, 7, 6)),
			(Weekday.SATURDAY, date(2024, 6, 15), date(2024, 7, 6)),
			(Weekday.SATURDAY, date(2025, 1, 1), date(2025, 2, 1)),
			(ISOWeekday.SATURDAY, datetime(2024, 6, 13), datetime(2024, 7, 6)),
			(ISOWeekday.SATURDAY, datetime(2024, 6, 15), datetime(2024, 7, 6)),
			(ISOWeekday.SATURDAY, datetime(2025, 1, 1), datetime(2025, 2, 1)),
		]

		for index, test in enumerate(tests):
			with self.subTest(
				f'Testing method first_of_next_month (subtest {index}) with inputs: {test}'
			):
				test_input_weekday, test_input_date, test_expected_output = test

				output = TemporalAdjuster.first_of_next_month(
					test_input_weekday, test_input_date
				)

				self.assertEqual(
					output,
					test_expected_output,
				)

				self.assertEqual(output.weekday(), test_expected_output.weekday())

	def test_first_of_last_month_success(self):
		tests = [
			(Weekday.SATURDAY, date(2024, 6, 13), date(2024, 5, 4)),
			(Weekday.SATURDAY, date(2025, 1, 1), date(2024, 12, 7)),
			(ISOWeekday.SATURDAY, datetime(2024, 6, 13), datetime(2024, 5, 4)),
			(ISOWeekday.SATURDAY, datetime(2025, 1, 1), datetime(2024, 12, 7)),
		]

		for index, test in enumerate(tests):
			with self.subTest(
				f'Testing method first_of_last_month (subtest {index}) with inputs: {test}'
			):
				test_input_weekday, test_input_date, test_expected_output = test

				output = TemporalAdjuster.first_of_last_month(
					test_input_weekday, test_input_date
				)

				self.assertEqual(
					output,
					test_expected_output,
				)

				self.assertEqual(output.weekday(), test_expected_output.weekday())

	def test_last_of_month_success(self):
		tests = [
			(Weekday.SATURDAY, date(2024, 6, 13), date(2024, 6, 29)),
			(Weekday.SATURDAY, date(2024, 6, 15), date(2024, 6, 29)),
			(Weekday.SATURDAY, date(2025, 1, 1), date(2025, 1, 25)),
			(ISOWeekday.SATURDAY, datetime(2024, 6, 13), datetime(2024, 6, 29)),
			(ISOWeekday.SATURDAY, datetime(2024, 6, 15), datetime(2024, 6, 29)),
			(ISOWeekday.SATURDAY, datetime(2025, 1, 1), datetime(2025, 1, 25)),
		]

		for index, test in enumerate(tests):
			with self.subTest(
				f'Testing method last_of_month (subtest {index}) with inputs: {test}'
			):
				test_input_weekday, test_input_date, test_expected_output = test

				output = TemporalAdjuster.last_of_month(
					test_input_weekday, test_input_date
				)

				self.assertEqual(
					output,
					test_expected_output,
				)

				self.assertEqual(output.weekday(), test_expected_output.weekday())

	def test_last_of_next_month_success(self):
		tests = [
			(Weekday.SATURDAY, date(2024, 6, 13), date(2024, 7, 27)),
			(Weekday.SATURDAY, date(2024, 6, 15), date(2024, 7, 27)),
			(Weekday.SATURDAY, date(2025, 1, 1), date(2025, 2, 22)),
			(ISOWeekday.SATURDAY, datetime(2024, 6, 13), datetime(2024, 7, 27)),
			(ISOWeekday.SATURDAY, datetime(2024, 6, 15), datetime(2024, 7, 27)),
			(ISOWeekday.SATURDAY, datetime(2025, 1, 1), datetime(2025, 2, 22)),
		]

		for index, test in enumerate(tests):
			with self.subTest(
				f'Testing method last_of_next_month (subtest {index}) with inputs: {test}'
			):
				test_input_weekday, test_input_date, test_expected_output = test

				output = TemporalAdjuster.last_of_next_month(
					test_input_weekday, test_input_date
				)

				self.assertEqual(
					output,
					test_expected_output,
				)

				self.assertEqual(output.weekday(), test_expected_output.weekday())

	def test_last_of_last_month_success(self):
		tests = [
			(Weekday.SATURDAY, date(2024, 6, 13), date(2024, 5, 25)),
			(Weekday.SATURDAY, date(2024, 6, 15), date(2024, 5, 25)),
			(Weekday.SATURDAY, date(2025, 1, 1), date(2024, 12, 28)),
			(ISOWeekday.SATURDAY, datetime(2024, 6, 13), datetime(2024, 5, 25)),
			(ISOWeekday.SATURDAY, datetime(2024, 6, 15), datetime(2024, 5, 25)),
			(ISOWeekday.SATURDAY, datetime(2025, 1, 1), datetime(2024, 12, 28)),
		]

		for index, test in enumerate(tests):
			with self.subTest(
				f'Testing method last_of_last_month (subtest {index}) with inputs: {test}'
			):
				test_input_weekday, test_input_date, test_expected_output = test

				output = TemporalAdjuster.last_of_last_month(
					test_input_weekday, test_input_date
				)

				self.assertEqual(
					output,
					test_expected_output,
				)

				self.assertEqual(output.weekday(), test_expected_output.weekday())

	def test_first_of_year_success(self):
		tests = [
			(Weekday.SATURDAY, date(2024, 6, 13), date(2024, 1, 6)),
			(Weekday.SATURDAY, date(2024, 6, 15), date(2024, 1, 6)),
			(Weekday.SATURDAY, date(2025, 1, 1), date(2025, 1, 4)),
			(ISOWeekday.SATURDAY, datetime(2024, 6, 13), datetime(2024, 1, 6)),
			(ISOWeekday.SATURDAY, datetime(2024, 6, 15), datetime(2024, 1, 6)),
			(ISOWeekday.SATURDAY, datetime(2025, 1, 1), datetime(2025, 1, 4)),
		]

		for index, test in enumerate(tests):
			with self.subTest(
				f'Testing method first_of_year (subtest {index}) with inputs: {test}'
			):
				test_input_weekday, test_input_date, test_expected_output = test

				output = TemporalAdjuster.first_of_year(
					test_input_weekday, test_input_date
				)

				self.assertEqual(
					output,
					test_expected_output,
				)

				self.assertEqual(output.weekday(), test_expected_output.weekday())

	def test_first_of_last_year_success(self):
		tests = [
			(Weekday.SATURDAY, date(2024, 6, 13), date(2023, 1, 7)),
			(Weekday.SATURDAY, date(2025, 1, 1), date(2024, 1, 6)),
			(ISOWeekday.SATURDAY, datetime(2024, 6, 13), datetime(2023, 1, 7)),
			(ISOWeekday.SATURDAY, datetime(2025, 1, 1), datetime(2024, 1, 6)),
		]

		for index, test in enumerate(tests):
			with self.subTest(
				f'Testing method first_of_last_year (subtest {index}) with inputs: {test}'
			):
				test_input_weekday, test_input_date, test_expected_output = test

				output = TemporalAdjuster.first_of_last_year(
					test_input_weekday, test_input_date
				)

				self.assertEqual(
					output,
					test_expected_output,
				)

				self.assertEqual(output.weekday(), test_expected_output.weekday())

	def test_last_of_year_success(self):
		tests = [
			(Weekday.SATURDAY, date(2024, 6, 13), date(2024, 12, 28)),
			(ISOWeekday.SATURDAY, datetime(2024, 6, 13), datetime(2024, 12, 28)),
		]

		for index, test in enumerate(tests):
			with self.subTest(
				f'Testing method last_of_year (subtest {index}) with inputs: {test}'
			):
				test_input_weekday, test_input_date, test_expected_output = test

				output = TemporalAdjuster.last_of_year(
					test_input_weekday, test_input_date
				)

				self.assertEqual(
					output,
					test_expected_output,
				)

				self.assertEqual(output.weekday(), test_expected_output.weekday())

	def test_first_of_next_year_success(self):
		tests = [
			(Weekday.SATURDAY, date(2024, 6, 13), date(2025, 1, 4)),
			(Weekday.SATURDAY, date(2025, 1, 1), date(2026, 1, 3)),
			(ISOWeekday.SATURDAY, datetime(2024, 6, 13), datetime(2025, 1, 4)),
			(ISOWeekday.SATURDAY, datetime(2025, 1, 1), datetime(2026, 1, 3)),
		]

		for index, test in enumerate(tests):
			with self.subTest(
				f'Testing method first_of_next_year (subtest {index}) with inputs: {test}'
			):
				test_input_weekday, test_input_date, test_expected_output = test

				output = TemporalAdjuster.first_of_next_year(
					test_input_weekday, test_input_date
				)

				self.assertEqual(
					output,
					test_expected_output,
				)

				self.assertEqual(output.weekday(), test_expected_output.weekday())

	def test_last_of_next_year_success(self):
		tests = [
			(Weekday.SATURDAY, date(2024, 6, 13), date(2025, 12, 27)),
			(Weekday.SATURDAY, date(2025, 1, 1), date(2026, 12, 26)),
			(ISOWeekday.SATURDAY, datetime(2024, 6, 13), datetime(2025, 12, 27)),
			(ISOWeekday.SATURDAY, datetime(2025, 1, 1), datetime(2026, 12, 26)),
		]

		for index, test in enumerate(tests):
			with self.subTest(
				f'Testing method last_of_next_year (subtest {index}) with inputs: {test}'
			):
				test_input_weekday, test_input_date, test_expected_output = test

				output = TemporalAdjuster.last_of_next_year(
					test_input_weekday, test_input_date
				)

				self.assertEqual(
					output,
					test_expected_output,
				)

				self.assertEqual(output.weekday(), test_expected_output.weekday())

	def test_last_of_last_year_success(self):
		tests = [
			(Weekday.SATURDAY, date(2024, 6, 13), date(2023, 12, 30)),
			(Weekday.SATURDAY, date(2025, 1, 1), date(2024, 12, 28)),
			(ISOWeekday.SATURDAY, datetime(2024, 6, 13), datetime(2023, 12, 30)),
			(ISOWeekday.SATURDAY, datetime(2025, 1, 1), datetime(2024, 12, 28)),
		]

		for index, test in enumerate(tests):
			with self.subTest(
				f'Testing method last_of_last_year (subtest {index}) with inputs: {test}'
			):
				test_input_weekday, test_input_date, test_expected_output = test

				output = TemporalAdjuster.last_of_last_year(
					test_input_weekday, test_input_date
				)

				self.assertEqual(
					output,
					test_expected_output,
				)

				self.assertEqual(output.weekday(), test_expected_output.weekday())

	def test_nth_from_date_success(self):
		tests = [
			(Weekday.SATURDAY, date(2024, 6, 13), 1, date(2024, 6, 15)),
			(Weekday.SATURDAY, date(2024, 6, 13), 2, date(2024, 6, 22)),
			(Weekday.SATURDAY, date(2024, 6, 13), 3, date(2024, 6, 29)),
			(ISOWeekday.SATURDAY, datetime(2024, 6, 13), 1, datetime(2024, 6, 15)),
			(ISOWeekday.SATURDAY, datetime(2024, 6, 13), 2, datetime(2024, 6, 22)),
			(ISOWeekday.SATURDAY, datetime(2024, 6, 13), 3, datetime(2024, 6, 29)),
		]

		for index, test in enumerate(tests):
			with self.subTest(
				f'Testing method nth_from_date (subtest {index}) with inputs: {test}'
			):
				(
					test_input_weekday,
					test_input_date,
					test_input_n,
					test_expected_output,
				) = test

				output = TemporalAdjuster.nth_from_date(
					test_input_weekday, test_input_date, test_input_n
				)

				self.assertEqual(
					output,
					test_expected_output,
				)

				self.assertEqual(output.weekday(), test_expected_output.weekday())

	def test_nth_of_month_success(self):
		tests = [
			(Weekday.SATURDAY, date(2024, 6, 13), 1, date(2024, 6, 1)),
			(Weekday.SATURDAY, date(2024, 6, 13), 2, date(2024, 6, 8)),
			(Weekday.SATURDAY, date(2024, 6, 13), 3, date(2024, 6, 15)),
			(Weekday.SATURDAY, date(2024, 6, 13), 4, date(2024, 6, 22)),
			(Weekday.SATURDAY, date(2024, 6, 13), 5, date(2024, 6, 29)),
			(ISOWeekday.SATURDAY, datetime(2024, 6, 13), 1, datetime(2024, 6, 1)),
			(ISOWeekday.SATURDAY, datetime(2024, 6, 13), 2, datetime(2024, 6, 8)),
			(ISOWeekday.SATURDAY, datetime(2024, 6, 13), 3, datetime(2024, 6, 15)),
			(ISOWeekday.SATURDAY, datetime(2024, 6, 13), 4, datetime(2024, 6, 22)),
			(ISOWeekday.SATURDAY, datetime(2024, 6, 13), 5, datetime(2024, 6, 29)),
		]

		for index, test in enumerate(tests):
			with self.subTest(
				f'Testing method nth_of_month (subtest {index}) with inputs: {test}'
			):
				(
					test_input_weekday,
					test_input_date,
					test_input_n,
					test_expected_output,
				) = test

				output = TemporalAdjuster.nth_of_month(
					test_input_weekday, test_input_date, test_input_n
				)

				self.assertEqual(
					output,
					test_expected_output,
				)

				self.assertEqual(output.weekday(), test_expected_output.weekday())

	def test_nth_of_month_exception_invalid_n(self):
		tests = [
			(Weekday.SATURDAY, date(2024, 6, 13), -1),
			(Weekday.SATURDAY, date(2024, 6, 13), 0),
			(Weekday.SATURDAY, date(2024, 6, 13), 6),
			(Weekday.SATURDAY, date(2024, 6, 13), 7),
			(ISOWeekday.SATURDAY, datetime(2024, 6, 13), -1),
			(ISOWeekday.SATURDAY, datetime(2024, 6, 13), 0),
			(ISOWeekday.SATURDAY, datetime(2024, 6, 13), 6),
			(ISOWeekday.SATURDAY, datetime(2024, 6, 13), 7),
		]

		for index, test in enumerate(tests):
			with self.subTest(
				f'Testing method nth_of_month (subtest {index}) with inputs: {test}'
			):
				test_input_weekday, test_input_date, test_input_n = test

				with self.assertRaises(ValueError) as context:
					TemporalAdjuster.nth_of_month(
						test_input_weekday, test_input_date, test_input_n
					)

				self.assertEqual(
					f'The value of n must be between 1 and 5, but is {test_input_n}.',
					str(context.exception),
				)

	def test_nth_of_month_exception_no_nth_weekday(self):
		tests = [
			(Weekday.SATURDAY, date(2024, 7, 1), 5),
			(Weekday.SATURDAY, date(1992, 6, 13), 5),
			(ISOWeekday.SATURDAY, datetime(2024, 7, 1), 5),
			(ISOWeekday.SATURDAY, datetime(1992, 6, 13), 5),
		]

		for index, test in enumerate(tests):
			with self.subTest(
				f'Testing method nth_of_month (subtest {index}) with inputs: {test}'
			):
				test_input_weekday, test_input_date, test_input_n = test

				with self.assertRaises(Exception) as context:
					TemporalAdjuster.nth_of_month(
						test_input_weekday, test_input_date, test_input_n
					)

				self.assertEqual(
					f'The month does not have a {test_input_n}th occurrence of {test_input_weekday.name.lower()}.',
					str(context.exception),
				)

				self.assertEqual(context.exception.__class__, DateError)

	def test_nth_of_year_success(self):
		tests = [
			(Weekday.SATURDAY, date(2024, 6, 13), 1, date(2024, 1, 6)),
			(Weekday.SATURDAY, date(2024, 6, 13), 10, date(2024, 3, 9)),
			(ISOWeekday.SATURDAY, datetime(2024, 6, 13), 1, datetime(2024, 1, 6)),
			(ISOWeekday.SATURDAY, datetime(2024, 6, 13), 10, datetime(2024, 3, 9)),
		]

		for index, test in enumerate(tests):
			with self.subTest(
				f'Testing method nth_of_year (subtest {index}) with inputs: {test}'
			):
				(
					test_input_weekday,
					test_input_date,
					test_input_n,
					test_expected_output,
				) = test

				output = TemporalAdjuster.nth_of_year(
					test_input_weekday, test_input_date, test_input_n
				)

				self.assertEqual(
					output,
					test_expected_output,
				)

				self.assertEqual(output.weekday(), test_expected_output.weekday())

	def test_nth_of_year_exception_invalid_n(self):
		tests = [
			(Weekday.SATURDAY, date(2024, 6, 13), -1),
			(Weekday.SATURDAY, date(2024, 6, 13), 0),
			(Weekday.SATURDAY, date(2024, 6, 13), 55),
			(ISOWeekday.SATURDAY, datetime(2024, 6, 13), -1),
			(ISOWeekday.SATURDAY, datetime(2024, 6, 13), 0),
			(ISOWeekday.SATURDAY, datetime(2024, 6, 13), 55),
		]

		for index, test in enumerate(tests):
			with self.subTest(
				f'Testing method nth_of_year (subtest {index}) with inputs: {test}'
			):
				test_input_weekday, test_input_date, test_input_n = test

				with self.assertRaises(ValueError) as context:
					TemporalAdjuster.nth_of_year(
						test_input_weekday, test_input_date, test_input_n
					)

				self.assertEqual(
					f'The value of n must be between 1 and 54, but is {test_input_n}.',
					str(context.exception),
				)

	def test_nth_of_year_exception_no_nth_weekday(self):
		tests = [
			(Weekday.SATURDAY, date(2024, 7, 1), 53),
			(Weekday.SATURDAY, date(1992, 6, 13), 53),
			(ISOWeekday.SATURDAY, datetime(2024, 7, 1), 53),
			(ISOWeekday.SATURDAY, datetime(1992, 6, 13), 53),
		]

		for index, test in enumerate(tests):
			with self.subTest(
				f'Testing method nth_of_year (subtest {index}) with inputs: {test}'
			):
				test_input_weekday, test_input_date, test_input_n = test

				with self.assertRaises(Exception) as context:
					TemporalAdjuster.nth_of_year(
						test_input_weekday, test_input_date, test_input_n
					)

				self.assertEqual(
					f'The year does not have a {test_input_n}th occurrence of {test_input_weekday.name.lower()}.',
					str(context.exception),
				)

				self.assertEqual(context.exception.__class__, DateError)
