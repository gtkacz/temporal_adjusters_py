from datetime import date, datetime
from unittest import TestCase

from temporal_adjuster.temporal_adjuster import TemporalAdjuster


class TestTemporalAdjusterForFirstAndLastDays(TestCase):
    def test_first_day_of_week_success(self):
        tests = [
            (date(2024, 6, 13), date(2024, 6, 10)),
            (date(2024, 6, 10), date(2024, 6, 10)),
            (date(2025, 1, 1), date(2024, 12, 30)),
            (datetime(2024, 6, 13), datetime(2024, 6, 10)),
            (datetime(2024, 6, 10), datetime(2024, 6, 10)),
            (datetime(2025, 1, 1), datetime(2024, 12, 30)),
        ]

        for index, test in enumerate(tests):
            with self.subTest(
                f"Testing method first_day_of_week (subtest {index}) with inputs: {test}"
            ):
                test_input, test_expected_output = test

                self.assertEqual(
                    TemporalAdjuster.first_day_of_week(test_input), test_expected_output
                )

    def test_first_day_of_next_week_success(self):
        tests = [
            (date(2024, 6, 13), date(2024, 6, 17)),
            (date(2024, 12, 31), date(2025, 1, 6)),
            (datetime(2024, 6, 13), datetime(2024, 6, 17)),
            (datetime(2024, 12, 31), datetime(2025, 1, 6)),
        ]

        for index, test in enumerate(tests):
            with self.subTest(
                f"Testing method first_day_of_next_week (subtest {index}) with inputs: {test}"
            ):
                test_input, test_expected_output = test

                self.assertEqual(
                    TemporalAdjuster.first_day_of_next_week(test_input),
                    test_expected_output,
                )

    def test_first_day_of_last_week_success(self):
        tests = [
            (date(2024, 6, 13), date(2024, 6, 3)),
            (date(2025, 1, 1), date(2024, 12, 23)),
            (datetime(2024, 6, 13), datetime(2024, 6, 3)),
            (datetime(2025, 1, 1), datetime(2024, 12, 23)),
        ]

        for index, test in enumerate(tests):
            with self.subTest(
                f"Testing method first_day_of_last_week (subtest {index}) with inputs: {test}"
            ):
                test_input, test_expected_output = test

                self.assertEqual(
                    TemporalAdjuster.first_day_of_last_week(test_input),
                    test_expected_output,
                )

    def test_first_day_of_month_success(self):
        tests = [
            (date(2024, 6, 13), date(2024, 6, 1)),
            (date(2025, 1, 1), date(2025, 1, 1)),
            (datetime(2024, 6, 13), datetime(2024, 6, 1)),
            (datetime(2025, 1, 1), datetime(2025, 1, 1)),
        ]

        for index, test in enumerate(tests):
            with self.subTest(
                f"Testing method first_day_of_month (subtest {index}) with inputs: {test}"
            ):
                test_input, test_expected_output = test

                self.assertEqual(
                    TemporalAdjuster.first_day_of_month(test_input),
                    test_expected_output,
                )

    def test_first_day_of_next_month_success(self):
        tests = [
            (date(2024, 6, 13), date(2024, 7, 1)),
            (date(2024, 12, 28), date(2025, 1, 1)),
            (datetime(2024, 6, 13), datetime(2024, 7, 1)),
            (datetime(2024, 12, 28), datetime(2025, 1, 1)),
        ]

        for index, test in enumerate(tests):
            with self.subTest(
                f"Testing method first_day_of_next_month (subtest {index}) with inputs: {test}"
            ):
                test_input, test_expected_output = test

                self.assertEqual(
                    TemporalAdjuster.first_day_of_next_month(test_input),
                    test_expected_output,
                )

    def test_first_day_of_last_month_success(self):
        tests = [
            (date(2024, 6, 13), date(2024, 5, 1)),
            (date(2025, 1, 1), date(2024, 12, 1)),
            (datetime(2024, 6, 13), datetime(2024, 5, 1)),
            (datetime(2025, 1, 1), datetime(2024, 12, 1)),
        ]

        for index, test in enumerate(tests):
            with self.subTest(
                f"Testing method first_day_of_last_month (subtest {index}) with inputs: {test}"
            ):
                test_input, test_expected_output = test

                self.assertEqual(
                    TemporalAdjuster.first_day_of_last_month(test_input),
                    test_expected_output,
                )

    def test_first_day_of_year_success(self):
        tests = [
            (date(2024, 6, 13), date(2024, 1, 1)),
            (date(2025, 1, 1), date(2025, 1, 1)),
            (datetime(2024, 6, 13), datetime(2024, 1, 1)),
            (datetime(2025, 1, 1), datetime(2025, 1, 1)),
        ]

        for index, test in enumerate(tests):
            with self.subTest(
                f"Testing method first_day_of_year (subtest {index}) with inputs: {test}"
            ):
                test_input, test_expected_output = test

                self.assertEqual(
                    TemporalAdjuster.first_day_of_year(test_input), test_expected_output
                )

    def test_first_day_of_next_year_success(self):
        tests = [
            (date(2024, 6, 13), date(2025, 1, 1)),
            (date(2025, 1, 1), date(2026, 1, 1)),
            (datetime(2024, 6, 13), datetime(2025, 1, 1)),
            (datetime(2025, 1, 1), datetime(2026, 1, 1)),
        ]

        for index, test in enumerate(tests):
            with self.subTest(
                f"Testing method first_day_of_next_year (subtest {index}) with inputs: {test}"
            ):
                test_input, test_expected_output = test

                self.assertEqual(
                    TemporalAdjuster.first_day_of_next_year(test_input),
                    test_expected_output,
                )

    def test_first_day_of_last_year_success(self):
        tests = [
            (date(2024, 6, 13), date(2023, 1, 1)),
            (date(2025, 1, 1), date(2024, 1, 1)),
            (datetime(2024, 6, 13), datetime(2023, 1, 1)),
            (datetime(2025, 1, 1), datetime(2024, 1, 1)),
        ]

        for index, test in enumerate(tests):
            with self.subTest(
                f"Testing method first_day_of_last_year (subtest {index}) with inputs: {test}"
            ):
                test_input, test_expected_output = test

                self.assertEqual(
                    TemporalAdjuster.first_day_of_last_year(test_input),
                    test_expected_output,
                )

    def test_last_day_of_week_success(self):
        tests = [
            (date(2024, 6, 13), date(2024, 6, 16)),
            (date(2024, 6, 16), date(2024, 6, 16)),
            (date(2024, 12, 31), date(2025, 1, 5)),
            (datetime(2024, 6, 13), datetime(2024, 6, 16)),
            (datetime(2024, 6, 16), datetime(2024, 6, 16)),
            (datetime(2024, 12, 31), datetime(2025, 1, 5)),
        ]

        for index, test in enumerate(tests):
            with self.subTest(
                f"Testing method last_day_of_week (subtest {index}) with inputs: {test}"
            ):
                test_input, test_expected_output = test

                self.assertEqual(
                    TemporalAdjuster.last_day_of_week(test_input), test_expected_output
                )

    def test_last_day_of_next_week_success(self):
        tests = [
            (date(2024, 6, 13), date(2024, 6, 23)),
            (date(2024, 12, 31), date(2025, 1, 12)),
            (datetime(2024, 6, 13), datetime(2024, 6, 23)),
            (datetime(2024, 12, 31), datetime(2025, 1, 12)),
        ]

        for index, test in enumerate(tests):
            with self.subTest(
                f"Testing method last_day_of_next_week (subtest {index}) with inputs: {test}"
            ):
                test_input, test_expected_output = test

                self.assertEqual(
                    TemporalAdjuster.last_day_of_next_week(test_input),
                    test_expected_output,
                )

    def test_last_day_of_last_week_success(self):
        tests = [
            (date(2024, 6, 13), date(2024, 6, 9)),
            (date(2025, 1, 1), date(2024, 12, 29)),
            (datetime(2024, 6, 13), datetime(2024, 6, 9)),
            (datetime(2025, 1, 1), datetime(2024, 12, 29)),
        ]

        for index, test in enumerate(tests):
            with self.subTest(
                f"Testing method last_day_of_last_week (subtest {index}) with inputs: {test}"
            ):
                test_input, test_expected_output = test

                self.assertEqual(
                    TemporalAdjuster.last_day_of_last_week(test_input),
                    test_expected_output,
                )

    def test_last_day_of_month_success(self):
        tests = [
            (date(2024, 6, 13), date(2024, 6, 30)),
            (date(2024, 6, 30), date(2024, 6, 30)),
            (datetime(2024, 6, 13), datetime(2024, 6, 30)),
            (datetime(2024, 6, 30), datetime(2024, 6, 30)),
        ]

        for index, test in enumerate(tests):
            with self.subTest(
                f"Testing method last_day_of_month (subtest {index}) with inputs: {test}"
            ):
                test_input, test_expected_output = test

                self.assertEqual(
                    TemporalAdjuster.last_day_of_month(test_input), test_expected_output
                )

    def test_last_day_of_next_month_success(self):
        tests = [
            (date(2024, 6, 13), date(2024, 7, 31)),
            (date(2024, 12, 28), date(2025, 1, 31)),
            (datetime(2024, 6, 13), datetime(2024, 7, 31)),
            (datetime(2024, 12, 28), datetime(2025, 1, 31)),
        ]

        for index, test in enumerate(tests):
            with self.subTest(
                f"Testing method last_day_of_next_month (subtest {index}) with inputs: {test}"
            ):
                test_input, test_expected_output = test

                self.assertEqual(
                    TemporalAdjuster.last_day_of_next_month(test_input),
                    test_expected_output,
                )

    def test_last_day_of_last_month_success(self):
        tests = [
            (date(2024, 6, 13), date(2024, 5, 31)),
            (date(2025, 1, 1), date(2024, 12, 31)),
            (datetime(2024, 6, 13), datetime(2024, 5, 31)),
            (datetime(2025, 1, 1), datetime(2024, 12, 31)),
        ]

        for index, test in enumerate(tests):
            with self.subTest(
                f"Testing method last_day_of_last_month (subtest {index}) with inputs: {test}"
            ):
                test_input, test_expected_output = test

                self.assertEqual(
                    TemporalAdjuster.last_day_of_last_month(test_input),
                    test_expected_output,
                )

    def test_last_day_of_year_success(self):
        tests = [
            (date(2024, 6, 13), date(2024, 12, 31)),
            (date(2025, 1, 1), date(2025, 12, 31)),
            (datetime(2024, 6, 13), datetime(2024, 12, 31)),
            (datetime(2025, 1, 1), datetime(2025, 12, 31)),
        ]

        for index, test in enumerate(tests):
            with self.subTest(
                f"Testing method last_day_of_year (subtest {index}) with inputs: {test}"
            ):
                test_input, test_expected_output = test

                self.assertEqual(
                    TemporalAdjuster.last_day_of_year(test_input), test_expected_output
                )

    def test_last_day_of_next_year_success(self):
        tests = [
            (date(2024, 6, 13), date(2025, 12, 31)),
            (date(2025, 1, 1), date(2026, 12, 31)),
            (datetime(2024, 6, 13), datetime(2025, 12, 31)),
            (datetime(2025, 1, 1), datetime(2026, 12, 31)),
        ]

        for index, test in enumerate(tests):
            with self.subTest(
                f"Testing method last_day_of_next_year (subtest {index}) with inputs: {test}"
            ):
                test_input, test_expected_output = test

                self.assertEqual(
                    TemporalAdjuster.last_day_of_next_year(test_input),
                    test_expected_output,
                )

    def test_last_day_of_last_year_success(self):
        tests = [
            (date(2024, 6, 13), date(2023, 12, 31)),
            (date(2025, 1, 1), date(2024, 12, 31)),
            (datetime(2024, 6, 13), datetime(2023, 12, 31)),
            (datetime(2025, 1, 1), datetime(2024, 12, 31)),
        ]

        for index, test in enumerate(tests):
            with self.subTest(
                f"Testing method last_day_of_last_year (subtest {index}) with inputs: {test}"
            ):
                test_input, test_expected_output = test

                self.assertEqual(
                    TemporalAdjuster.last_day_of_last_year(test_input),
                    test_expected_output,
                )
