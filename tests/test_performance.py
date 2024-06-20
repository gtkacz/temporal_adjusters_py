from datetime import date
from random import randint
from timeit import timeit
from unittest import TestCase

from psutil import cpu_count, cpu_freq

from temporal_adjuster.common.enums import Weekday
from temporal_adjuster.temporal_adjuster import TemporalAdjuster


class TestPerformance(TestCase):
    test_input, test_n = (
        [
            date(randint(1900, 2024), randint(1, 12), randint(1, 28))
            for _ in range(10_000)
        ],
        10,
    )

    try:
        max_execution_time = 2.25 ** round(
            100_000 / (cpu_count(logical=True) * cpu_freq().max or 25_000)
        )
    except Exception:
        max_execution_time = 25

    # Weekday operations module
    def test_next_success(self):
        execution_time = timeit(
            lambda: TemporalAdjuster.next(Weekday.MONDAY, self.test_input),
            number=self.test_n,
        )

        self.assertLess(execution_time, self.max_execution_time)

    # First and last day operations module
    def test_first_day_of_next_week_success(self):
        execution_time = timeit(
            lambda: TemporalAdjuster.first_day_of_next_week(self.test_input),
            number=self.test_n,
        )

        self.assertLess(execution_time, self.max_execution_time)
