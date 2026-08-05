import unittest
from datetime import UTC, datetime, time, timedelta

from temporal_adjuster.temporal_adjuster import TemporalAdjuster


class TestTimeAdjuster(unittest.TestCase):
    def test_time_difference_single(self):
        result = TemporalAdjuster.time_difference(time(10, 0), time(11, 0))
        self.assertEqual(result, timedelta(hours=1))

        result = TemporalAdjuster.time_difference(time(23, 0), time(1, 0))
        self.assertEqual(result, timedelta(hours=2))

        dt1 = datetime(2021, 1, 1, 10, 0)
        dt2 = datetime(2021, 1, 1, 11, 30)
        result = TemporalAdjuster.time_difference(dt1, dt2)
        self.assertEqual(result, timedelta(hours=1, minutes=30))

        dt1 = datetime(2021, 1, 1, 22, 0)
        dt2 = datetime(2021, 1, 2, 1, 0)
        result = TemporalAdjuster.time_difference(dt1, dt2)
        self.assertEqual(result, timedelta(hours=3))

        result = TemporalAdjuster.time_difference(time(12, 30), time(12, 30))
        self.assertEqual(result, timedelta(0))

        t1 = time(12, 30, 45, 500000)
        t2 = time(12, 30, 46, 250000)
        result = TemporalAdjuster.time_difference(t1, t2)
        self.assertEqual(result, timedelta(seconds=0.75))

    def test_is_time_in_range_single(self):
        self.assertTrue(
            TemporalAdjuster.is_time_in_range(time(12, 0), time(9, 0), time(17, 0)),
        )
        self.assertTrue(
            TemporalAdjuster.is_time_in_range(time(9, 0), time(9, 0), time(17, 0)),
        )
        self.assertTrue(
            TemporalAdjuster.is_time_in_range(time(17, 0), time(9, 0), time(17, 0)),
        )
        self.assertFalse(
            TemporalAdjuster.is_time_in_range(time(8, 0), time(9, 0), time(17, 0)),
        )
        self.assertFalse(
            TemporalAdjuster.is_time_in_range(time(18, 0), time(9, 0), time(17, 0)),
        )

        self.assertTrue(
            TemporalAdjuster.is_time_in_range(time(23, 0), time(22, 0), time(6, 0)),
        )
        self.assertTrue(
            TemporalAdjuster.is_time_in_range(time(0, 0), time(22, 0), time(6, 0)),
        )
        self.assertTrue(
            TemporalAdjuster.is_time_in_range(time(6, 0), time(22, 0), time(6, 0)),
        )
        self.assertFalse(
            TemporalAdjuster.is_time_in_range(time(7, 0), time(22, 0), time(6, 0)),
        )
        self.assertFalse(
            TemporalAdjuster.is_time_in_range(time(21, 0), time(22, 0), time(6, 0)),
        )

        dt = datetime(2021, 1, 1, 12, 0)
        dt_start = datetime(2021, 1, 1, 9, 0)
        dt_end = datetime(2021, 1, 1, 17, 0)
        self.assertTrue(TemporalAdjuster.is_time_in_range(dt, dt_start, dt_end))

        self.assertTrue(
            TemporalAdjuster.is_time_in_range(time(12, 0), dt_start, dt_end),
        )
        self.assertTrue(TemporalAdjuster.is_time_in_range(dt, time(9, 0), time(17, 0)))

    def test_round_time_single(self):
        self.assertEqual(TemporalAdjuster.round_time(time(10, 29), 60), time(10, 29))
        self.assertEqual(
            TemporalAdjuster.round_time(time(10, 29, 35), 60),
            time(10, 30),
        )
        self.assertEqual(
            TemporalAdjuster.round_time(time(10, 29, 25), 60),
            time(10, 29),
        )

        self.assertEqual(
            TemporalAdjuster.round_time(time(10, 17), 15 * 60),
            time(10, 15),
        )
        self.assertEqual(
            TemporalAdjuster.round_time(time(10, 22), 15 * 60),
            time(10, 15),
        )
        self.assertEqual(TemporalAdjuster.round_time(time(10, 7), 15 * 60), time(10, 0))

        self.assertEqual(TemporalAdjuster.round_time(time(10, 29), 3600), time(10, 0))
        self.assertEqual(TemporalAdjuster.round_time(time(10, 31), 3600), time(11, 0))

        dt = datetime(2021, 1, 1, 10, 29, 35)
        expected = datetime(2021, 1, 1, 10, 30)
        self.assertEqual(TemporalAdjuster.round_time(dt, 60), expected)

        self.assertEqual(TemporalAdjuster.round_time(time(23, 59, 30), 60), time(0, 0))
        dt = datetime(2021, 1, 1, 23, 59, 30)
        expected = datetime(2021, 1, 2, 0, 0)
        self.assertEqual(TemporalAdjuster.round_time(dt, 60), expected)

    def test_round_time_preserves_tzinfo(self):
        aware_dt = datetime(2021, 1, 1, 10, 29, 35, tzinfo=UTC)
        result = TemporalAdjuster.round_time(aware_dt, 60)
        self.assertEqual(result, datetime(2021, 1, 1, 10, 30, tzinfo=UTC))
        self.assertEqual(result.tzinfo, UTC)

        aware_time = time(10, 29, 35, tzinfo=UTC)
        result = TemporalAdjuster.round_time(aware_time, 60)
        self.assertEqual(result, time(10, 30, tzinfo=UTC))
        self.assertEqual(result.tzinfo, UTC)

        naive_result = TemporalAdjuster.round_time(time(10, 29, 35), 60)
        self.assertIsNone(naive_result.tzinfo)

    def test_round_time_multiple_intervals(self):
        intervals = [60, 15 * 60, 30 * 60]
        results = [TemporalAdjuster.round_time(time(10, 29, 35), interval) for interval in intervals]
        expected = [time(10, 30), time(10, 30), time(10, 30)]
        self.assertEqual(results, expected)

    def test_time_to_seconds_single(self):
        self.assertEqual(TemporalAdjuster.time_to_seconds(time(0, 0)), 0)
        self.assertEqual(TemporalAdjuster.time_to_seconds(time(1, 0)), 3600)
        self.assertEqual(TemporalAdjuster.time_to_seconds(time(0, 1)), 60)
        self.assertEqual(TemporalAdjuster.time_to_seconds(time(0, 0, 1)), 1)
        self.assertEqual(TemporalAdjuster.time_to_seconds(time(1, 30, 45)), 5445)

        self.assertEqual(
            TemporalAdjuster.time_to_seconds(time(1, 30, 45, 500000)),
            5445.5,
        )

        dt = datetime(2021, 1, 1, 1, 30, 45, 500000)
        self.assertEqual(TemporalAdjuster.time_to_seconds(dt), 5445.5)

    def test_seconds_to_time_single(self):
        self.assertEqual(TemporalAdjuster.seconds_to_time(0), time(0, 0))
        self.assertEqual(TemporalAdjuster.seconds_to_time(3600), time(1, 0))
        self.assertEqual(TemporalAdjuster.seconds_to_time(5445), time(1, 30, 45))

        self.assertEqual(
            TemporalAdjuster.seconds_to_time(5445.5),
            time(1, 30, 45, 500000),
        )

        self.assertEqual(TemporalAdjuster.seconds_to_time(86400), time(0, 0))
        self.assertEqual(TemporalAdjuster.seconds_to_time(90000), time(1, 0))

        self.assertEqual(TemporalAdjuster.seconds_to_time(-3600), time(23, 0))

    def test_edge_cases(self):
        self.assertEqual(TemporalAdjuster.time_to_seconds(time(0, 0)), 0)
        self.assertEqual(TemporalAdjuster.seconds_to_time(0), time(0, 0))
        self.assertEqual(TemporalAdjuster.seconds_to_time(86400), time(0, 0))

        self.assertTrue(
            TemporalAdjuster.is_time_in_range(time(12, 0), time(12, 0), time(12, 0)),
        )
        self.assertFalse(
            TemporalAdjuster.is_time_in_range(time(13, 0), time(12, 0), time(12, 0)),
        )

        self.assertEqual(
            TemporalAdjuster.round_time(time(10, 30, 45), 1),
            time(10, 30, 45),
        )

        day_seconds = 24 * 60 * 60
        self.assertEqual(
            TemporalAdjuster.round_time(time(10, 30), day_seconds),
            time(0, 0),
        )
        self.assertEqual(
            TemporalAdjuster.round_time(time(13, 0), day_seconds),
            time(0, 0),
        )

    def test_time_to_seconds_rejects_invalid_type(self):
        with self.assertRaisesRegex(TypeError, r"time_obj must be a time or datetime"):
            TemporalAdjuster.time_to_seconds(123)

    def test_seconds_to_time_rounds_microseconds(self):
        self.assertEqual(
            TemporalAdjuster.seconds_to_time(59.9999996),
            time(0, 1),
        )
        self.assertEqual(
            TemporalAdjuster.seconds_to_time(86399.9999996),
            time(0, 0),
        )
