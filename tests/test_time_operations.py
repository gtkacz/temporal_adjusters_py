import unittest
from datetime import datetime, time, timedelta

from temporal_adjuster.temporal_adjuster import TemporalAdjuster


class TestTimeAdjuster(unittest.TestCase):
	def test_time_difference_single(self):
		"""Test time_difference with single time objects."""
		# Test normal case (second time is later)
		result = TemporalAdjuster.time_difference(time(10, 0), time(11, 0))
		self.assertEqual(result, timedelta(hours=1))

		# Test case crossing midnight
		result = TemporalAdjuster.time_difference(time(23, 0), time(1, 0))
		self.assertEqual(result, timedelta(hours=2))

		# Test with datetime objects
		dt1 = datetime(2021, 1, 1, 10, 0)
		dt2 = datetime(2021, 1, 1, 11, 30)
		result = TemporalAdjuster.time_difference(dt1, dt2)
		self.assertEqual(result, timedelta(hours=1, minutes=30))

		# Test with different dates (should ignore dates)
		dt1 = datetime(2021, 1, 1, 22, 0)
		dt2 = datetime(2021, 1, 2, 1, 0)
		result = TemporalAdjuster.time_difference(dt1, dt2)
		self.assertEqual(result, timedelta(hours=3))

		# Test with exact same time
		result = TemporalAdjuster.time_difference(time(12, 30), time(12, 30))
		self.assertEqual(result, timedelta(0))

		# Test with microseconds
		t1 = time(12, 30, 45, 500000)
		t2 = time(12, 30, 46, 250000)
		result = TemporalAdjuster.time_difference(t1, t2)
		self.assertEqual(result, timedelta(seconds=0.75))

	def test_time_difference_sequence(self):
		"""Test time_difference with sequences of time objects."""
		# Test with sequence of first time objects
		times1 = [time(9, 0), time(10, 0), time(23, 0)]
		time2 = time(12, 0)
		result = TemporalAdjuster.time_difference(times1, time2)
		expected = [timedelta(hours=3), timedelta(hours=2), timedelta(hours=13)]
		self.assertEqual(result, expected)

		# Test with sequences for both time objects
		times1 = [time(9, 0), time(10, 0), time(23, 0)]
		time2 = time(10, 0)
		result = TemporalAdjuster.time_difference(times1, time2)
		expected = [timedelta(hours=1), timedelta(hours=0), timedelta(hours=-13)]
		self.assertEqual(result, expected)

	def test_is_time_in_range_single(self):
		"""Test is_time_in_range with single time objects."""
		# Test normal range (no midnight crossing)
		self.assertTrue(
			TemporalAdjuster.is_time_in_range(time(12, 0), time(9, 0), time(17, 0))
		)
		self.assertTrue(
			TemporalAdjuster.is_time_in_range(time(9, 0), time(9, 0), time(17, 0))
		)
		self.assertTrue(
			TemporalAdjuster.is_time_in_range(time(17, 0), time(9, 0), time(17, 0))
		)
		self.assertFalse(
			TemporalAdjuster.is_time_in_range(time(8, 0), time(9, 0), time(17, 0))
		)
		self.assertFalse(
			TemporalAdjuster.is_time_in_range(time(18, 0), time(9, 0), time(17, 0))
		)

		# Test range crossing midnight
		self.assertTrue(
			TemporalAdjuster.is_time_in_range(time(23, 0), time(22, 0), time(6, 0))
		)
		self.assertTrue(
			TemporalAdjuster.is_time_in_range(time(0, 0), time(22, 0), time(6, 0))
		)
		self.assertTrue(
			TemporalAdjuster.is_time_in_range(time(6, 0), time(22, 0), time(6, 0))
		)
		self.assertFalse(
			TemporalAdjuster.is_time_in_range(time(7, 0), time(22, 0), time(6, 0))
		)
		self.assertFalse(
			TemporalAdjuster.is_time_in_range(time(21, 0), time(22, 0), time(6, 0))
		)

		# Test with datetime objects
		dt = datetime(2021, 1, 1, 12, 0)
		dt_start = datetime(2021, 1, 1, 9, 0)
		dt_end = datetime(2021, 1, 1, 17, 0)
		self.assertTrue(TemporalAdjuster.is_time_in_range(dt, dt_start, dt_end))

		# Test with mixed time and datetime objects
		self.assertTrue(
			TemporalAdjuster.is_time_in_range(time(12, 0), dt_start, dt_end)
		)
		self.assertTrue(TemporalAdjuster.is_time_in_range(dt, time(9, 0), time(17, 0)))

	def test_is_time_in_range_sequence(self):
		"""Test is_time_in_range with sequences of time objects."""
		# Test with sequence of time objects to check
		times = [time(8, 0), time(12, 0), time(18, 0)]
		start = time(9, 0)
		end = time(17, 0)
		result = TemporalAdjuster.is_time_in_range(times, start, end)
		expected = [False, True, False]
		self.assertEqual(result, expected)

		# Test with sequence crossing midnight
		times = [time(23, 0), time(3, 0), time(7, 0)]
		start = time(22, 0)
		end = time(6, 0)
		result = TemporalAdjuster.is_time_in_range(times, start, end)
		expected = [True, True, False]
		self.assertEqual(result, expected)

		# Test with mixed time and datetime objects
		times = [time(8, 0), datetime(2021, 1, 1, 12, 0), time(18, 0)]
		start = datetime(2021, 1, 1, 9, 0)
		end = time(17, 0)
		result = TemporalAdjuster.is_time_in_range(times, start, end)
		expected = [False, True, False]
		self.assertEqual(result, expected)

	def test_round_time_single(self):
		"""Test round_time with single time objects."""
		# Test rounding time objects
		self.assertEqual(TemporalAdjuster.round_time(time(10, 29), 60), time(10, 29))
		self.assertEqual(
			TemporalAdjuster.round_time(time(10, 29, 35), 60), time(10, 30)
		)
		self.assertEqual(
			TemporalAdjuster.round_time(time(10, 29, 25), 60), time(10, 29)
		)

		# Test rounding with different intervals
		self.assertEqual(
			TemporalAdjuster.round_time(time(10, 17), 15 * 60), time(10, 15)
		)
		self.assertEqual(
			TemporalAdjuster.round_time(time(10, 22), 15 * 60), time(10, 30)
		)
		self.assertEqual(TemporalAdjuster.round_time(time(10, 7), 15 * 60), time(10, 0))

		# Test rounding to hour
		self.assertEqual(TemporalAdjuster.round_time(time(10, 29), 3600), time(10, 0))
		self.assertEqual(TemporalAdjuster.round_time(time(10, 31), 3600), time(11, 0))

		# Test rounding datetime objects
		dt = datetime(2021, 1, 1, 10, 29, 35)
		expected = datetime(2021, 1, 1, 10, 30)
		self.assertEqual(TemporalAdjuster.round_time(dt, 60), expected)

		# Test rounding at midnight boundary
		self.assertEqual(TemporalAdjuster.round_time(time(23, 59, 30), 60), time(0, 0))
		dt = datetime(2021, 1, 1, 23, 59, 30)
		expected = datetime(2021, 1, 2, 0, 0)  # Should maintain date
		self.assertEqual(TemporalAdjuster.round_time(dt, 60), expected)

	def test_round_time_sequence(self):
		"""Test round_time with sequences of time objects."""
		# Test with sequence of time objects
		times = [time(10, 14), time(10, 29, 35), time(10, 45)]
		result = TemporalAdjuster.round_time(times, 15 * 60)
		expected = [time(10, 15), time(10, 30), time(10, 45)]
		self.assertEqual(result, expected)

		# Test with sequence of datetime objects
		dts = [
			datetime(2021, 1, 1, 10, 14),
			datetime(2021, 1, 1, 10, 29, 35),
			datetime(2021, 1, 1, 10, 45),
		]
		result = TemporalAdjuster.round_time(dts, 15 * 60)
		expected = [
			datetime(2021, 1, 1, 10, 15),
			datetime(2021, 1, 1, 10, 30),
			datetime(2021, 1, 1, 10, 45),
		]
		self.assertEqual(result, expected)

		# Test with different rounding intervals
		times = [time(10, 29, 35)]
		intervals = [60, 15 * 60, 30 * 60]
		results = [
			TemporalAdjuster.round_time(times[0], interval) for interval in intervals
		]
		expected = [time(10, 30), time(10, 30), time(10, 30)]
		self.assertEqual(results, expected)

	def test_time_to_seconds_single(self):
		"""Test time_to_seconds with single time objects."""
		# Test with time objects
		self.assertEqual(TemporalAdjuster.time_to_seconds(time(0, 0)), 0)
		self.assertEqual(TemporalAdjuster.time_to_seconds(time(1, 0)), 3600)
		self.assertEqual(TemporalAdjuster.time_to_seconds(time(0, 1)), 60)
		self.assertEqual(TemporalAdjuster.time_to_seconds(time(0, 0, 1)), 1)
		self.assertEqual(TemporalAdjuster.time_to_seconds(time(1, 30, 45)), 5445)

		# Test with microseconds
		self.assertEqual(
			TemporalAdjuster.time_to_seconds(time(1, 30, 45, 500000)), 5445.5
		)

		# Test with datetime objects
		dt = datetime(2021, 1, 1, 1, 30, 45, 500000)
		self.assertEqual(TemporalAdjuster.time_to_seconds(dt), 5445.5)

	def test_time_to_seconds_sequence(self):
		"""Test time_to_seconds with sequences of time objects."""
		# Test with sequence of time objects
		times = [time(0, 0), time(1, 30), time(12, 0), time(23, 59, 59)]
		result = TemporalAdjuster.time_to_seconds(times)
		expected = [0, 5400, 43200, 86399]
		self.assertEqual(result, expected)

		# Test with sequence of datetime objects
		dts = [
			datetime(2021, 1, 1, 0, 0),
			datetime(2021, 1, 1, 1, 30),
			datetime(2021, 1, 1, 12, 0),
			datetime(2021, 1, 1, 23, 59, 59),
		]
		result = TemporalAdjuster.time_to_seconds(dts)
		expected = [0, 5400, 43200, 86399]
		self.assertEqual(result, expected)

		# Test with mixed time and datetime objects
		mixed = [time(0, 0), datetime(2021, 1, 1, 1, 30), time(12, 0)]
		result = TemporalAdjuster.time_to_seconds(mixed)
		expected = [0, 5400, 43200]
		self.assertEqual(result, expected)

	def test_seconds_to_time_single(self):
		"""Test seconds_to_time with single values."""
		# Test basic conversions
		self.assertEqual(TemporalAdjuster.seconds_to_time(0), time(0, 0))
		self.assertEqual(TemporalAdjuster.seconds_to_time(3600), time(1, 0))
		self.assertEqual(TemporalAdjuster.seconds_to_time(5445), time(1, 30, 45))

		# Test with fractional seconds
		self.assertEqual(
			TemporalAdjuster.seconds_to_time(5445.5), time(1, 30, 45, 500000)
		)

		# Test wrapping around midnight
		self.assertEqual(TemporalAdjuster.seconds_to_time(86400), time(0, 0))
		self.assertEqual(TemporalAdjuster.seconds_to_time(90000), time(1, 0))

		# Test with negative values (should wrap around)
		self.assertEqual(TemporalAdjuster.seconds_to_time(-3600), time(23, 0))

	# def test_seconds_to_time_sequence(self):
	# 	"""Test seconds_to_time with sequences of values."""
	# 	# Test with sequence of seconds
	# 	seconds = [0, 3600, 5445, 86399]
	# 	result = TemporalAdjuster.seconds_to_time(seconds)
	# 	expected = [time(0, 0), time(1, 0), time(1, 30, 45), time(23, 59, 59)]
	# 	self.assertEqual(result, expected)

	# 	# Test with fractional seconds
	# 	seconds = [5445.5, 5445.75]
	# 	result = TemporalAdjuster.seconds_to_time(seconds)
	# 	expected = [time(1, 30, 45, 500000), time(1, 30, 45, 750000)]
	# 	self.assertEqual(result, expected)

	# 	# Test wrapping around midnight
	# 	seconds = [86400, 90000, 172800]
	# 	result = TemporalAdjuster.seconds_to_time(seconds)
	# 	expected = [time(0, 0), time(1, 0), time(0, 0)]
	# 	self.assertEqual(result, expected)

	def test_edge_cases(self):
		"""Test edge cases and potential error conditions."""
		# Test exact midnight
		self.assertEqual(TemporalAdjuster.time_to_seconds(time(0, 0)), 0)
		self.assertEqual(TemporalAdjuster.seconds_to_time(0), time(0, 0))
		self.assertEqual(TemporalAdjuster.seconds_to_time(86400), time(0, 0))

		# Test time range with start and end being the same
		self.assertTrue(
			TemporalAdjuster.is_time_in_range(time(12, 0), time(12, 0), time(12, 0))
		)

		# Test rounding with very small intervals
		self.assertEqual(
			TemporalAdjuster.round_time(time(10, 30, 45), 1), time(10, 30, 45)
		)

		# Test rounding with very large intervals
		day_seconds = 24 * 60 * 60
		self.assertEqual(
			TemporalAdjuster.round_time(time(10, 30), day_seconds), time(0, 0)
		)
		self.assertEqual(
			TemporalAdjuster.round_time(time(13, 0), day_seconds), time(0, 0)
		)

		# Test empty sequence
		self.assertEqual(TemporalAdjuster.time_to_seconds([]), [])
		self.assertEqual(TemporalAdjuster.seconds_to_time([]), [])


if __name__ == '__main__':
	unittest.main()
