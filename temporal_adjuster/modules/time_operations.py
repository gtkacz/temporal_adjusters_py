from datetime import datetime, time, timedelta

from ..common.types import AnyTime, TimeT


class _TimeAdjuster:
	@staticmethod
	def time_difference(t1: AnyTime, t2: AnyTime) -> timedelta:
		"""
		Calculate the positive difference between two time objects,
		accounting for wrapping around midnight.
		"""
		total_seconds1 = _TimeAdjuster.time_to_seconds(t1)
		total_seconds2 = _TimeAdjuster.time_to_seconds(t2)
		delta_seconds = (total_seconds2 - total_seconds1) % (24 * 3600)

		return timedelta(seconds=delta_seconds)

	@staticmethod
	def is_time_in_range(start: AnyTime, end: AnyTime, t: AnyTime) -> bool:
		"""
		Check if a time object t is within the range [start, end].
		Handles ranges that cross midnight.
		"""
		if isinstance(start, datetime):
			start = start.time()

		if isinstance(end, datetime):
			end = end.time()

		if isinstance(t, datetime):
			t = t.time()

		return start <= t <= end if start <= end else t >= start or t <= end

	@staticmethod
	def round_time(t: TimeT, round_to: int = 60) -> TimeT:
		"""
		Round a time object to the nearest 'round_to' seconds.
		For example, round_to=60 rounds to the nearest minute.
		"""
		total_seconds = _TimeAdjuster.time_to_seconds(t)
		rounded_seconds = int((total_seconds + round_to / 2) // round_to * round_to)
		rounded_seconds %= 24 * 3600  # Ensure it wraps around midnight
		return (
			_TimeAdjuster.seconds_to_time(rounded_seconds)
			if isinstance(t, time)
			else datetime.combine(
				t.date(), _TimeAdjuster.seconds_to_time(rounded_seconds)
			)
		)

	@staticmethod
	def time_to_seconds(t: AnyTime) -> float:
		"""
		Convert a time object to the total number of seconds since midnight.
		"""
		return t.hour * 3600 + t.minute * 60 + t.second + t.microsecond / 1e6

	@staticmethod
	def seconds_to_time(seconds: float) -> time:
		"""
		Convert total seconds since midnight to a time object,
		handling wrap-around at 24 hours.
		"""
		seconds %= 24 * 3600  # Wrap around 24 hours
		hour = int(seconds // 3600)
		seconds %= 3600
		minute = int(seconds // 60)
		seconds %= 60

		return time(hour, minute, int(seconds), (seconds - int(seconds)) * 1e6)
