from datetime import datetime, time

from ..common.decorators import sequenceable
from ..common.types import AnyTime, ExtendedTimeDelta, TimeT


class _TimeAdjuster:
	@staticmethod
	@sequenceable(target='time_obj_1')
	def time_difference(time_obj_1: AnyTime, time_obj_2: AnyTime) -> ExtendedTimeDelta:
		"""
		Calculate the positive difference between two time objects,
		accounting for wrapping around midnight.

		Args:
			time_obj_1 (AnyTime): The first time object.
			time_obj_2 (AnyTime): The second time object.

		Returns:
			ExtendedTimeDelta: The positive difference between the two time objects.

		Example:
			>>> from datetime import time
			>>> time_difference(time(23, 0), time(1, 0))
			ExtendedTimeDelta(seconds=7200)
		"""
		total_seconds1 = _TimeAdjuster.time_to_seconds(time_obj_1)
		total_seconds2 = _TimeAdjuster.time_to_seconds(time_obj_2)
		delta_seconds = (total_seconds2 - total_seconds1) % (24 * 3600)

		return ExtendedTimeDelta(seconds=delta_seconds)

	@staticmethod
	@sequenceable(target='time_obj')
	def is_time_in_range(time_obj: AnyTime, start: AnyTime, end: AnyTime) -> bool:
		"""
		Check if a time object time_obj is within the range [start, end].
		Handles ranges that cross midnight.

		Args:
			time_obj (AnyTime): The time to check.
			start (AnyTime): The start of the range.
			end (AnyTime): The end of the range.

		Returns:
			bool: True if time_obj is within the range [start, end].

		Example:
			>>> from datetime import time
			>>> is_time_in_range(time(23, 0), time(1, 0), time(0, 0))
			True
		"""
		if isinstance(start, datetime):
			start = start.time()

		if isinstance(end, datetime):
			end = end.time()

		if isinstance(time_obj, datetime):
			time_obj = time_obj.time()

		return (
			start <= time_obj <= end
			if start <= end
			else time_obj >= start or time_obj <= end
		)

	@staticmethod
	@sequenceable(target='time_obj')
	def round_time(time_obj: TimeT, round_to: int = 60) -> TimeT:
		"""
		Round a time object to the nearest multiple of round_to seconds.

		Args:
			time_obj (TimeT): The time object to round.
			round_to (int, optional): The number of seconds to round to. Defaults to 60.

		Returns:
			TimeT: The rounded time object.

		Example:
			>>> from datetime import time
			>>> round_time(time(23, 59, 30), 60)
			datetime.time(0, 0)
		"""
		total_seconds = _TimeAdjuster.time_to_seconds(time_obj)
		rounded_seconds = int((total_seconds + round_to / 2) // round_to * round_to)
		rounded_seconds %= 24 * 3600  # Ensure it wraps around midnight
		return (
			_TimeAdjuster.seconds_to_time(rounded_seconds)
			if isinstance(time_obj, time)
			else datetime.combine(
				time_obj.date(), _TimeAdjuster.seconds_to_time(rounded_seconds)
			)
		)

	@staticmethod
	@sequenceable(target='time_obj')
	def time_to_seconds(time_obj: AnyTime) -> float:
		"""
		Convert a time object to the total number of seconds since midnight.

		Args:
			time_obj (AnyTime): The time object to convert.

		Returns:
			float: The total number of seconds since midnight.
		"""
		return (
			time_obj.hour * 3600
			+ time_obj.minute * 60
			+ time_obj.second
			+ time_obj.microsecond / 1e6
		)

	@staticmethod
	@sequenceable(target='seconds')
	def seconds_to_time(seconds: float) -> time:
		"""
		Convert the total number of seconds since midnight to a time object.

		Args:
			seconds (float): The total number of seconds since midnight.

		Returns:
			time: The time object.
		"""
		seconds %= 24 * 3600  # Wrap around 24 hours
		hour = int(seconds // 3600)
		seconds %= 3600
		minute = int(seconds // 60)
		seconds %= 60

		return time(hour, minute, int(seconds), int((seconds - int(seconds)) * 1e6))
