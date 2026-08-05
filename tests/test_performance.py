from datetime import date, timedelta
from timeit import timeit
from unittest import TestCase

from temporal_adjuster.common.enums import Weekday
from temporal_adjuster.temporal_adjuster import TemporalAdjuster


class TestPerformance(TestCase):
    # ~27 years of deterministic dates; the stride keeps weekdays and months varied.
    test_input, test_n = (
        [date(1990, 1, 1) + timedelta(days=(i * 37) % 10_000) for i in range(10_000)],
        10,
    )

    # 100k scalar calls take well under a second; the bound only guards against
    # gross regressions such as reintroducing per-call signature inspection.
    max_execution_time = 5

    def test_next_success(self):
        execution_time = timeit(
            lambda: [TemporalAdjuster.next(Weekday.MONDAY, item) for item in self.test_input],
            number=self.test_n,
        )

        self.assertLess(execution_time, self.max_execution_time)

    def test_first_day_of_next_week_success(self):
        execution_time = timeit(
            lambda: [TemporalAdjuster.first_day_of_next_week(item) for item in self.test_input],
            number=self.test_n,
        )

        self.assertLess(execution_time, self.max_execution_time)
