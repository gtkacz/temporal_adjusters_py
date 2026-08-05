# Copyright (c) 2024 Gabriel Mitelman Tkacz
"""Operations for adjusting times and datetimes."""

from datetime import datetime, time, timedelta
from typing import cast

from temporal_adjuster.common.types import AnyTime, TimeT


class _TimeAdjuster:
    @staticmethod
    def time_difference(time_obj_1: AnyTime, time_obj_2: AnyTime) -> timedelta:
        """Calculate the positive difference between two time objects.

        accounting for wrapping around midnight.

        Args:
            time_obj_1 (AnyTime): The first time object.
            time_obj_2 (AnyTime): The second time object.

        Returns:
            timedelta: The positive difference between the two time objects.

        Example:
            >>> from datetime import time
            >>> time_difference(time(23, 0), time(1, 0))
            datetime.timedelta(seconds=7200)

        """
        total_seconds1 = _TimeAdjuster.time_to_seconds(time_obj_1)
        total_seconds2 = _TimeAdjuster.time_to_seconds(time_obj_2)
        delta_seconds = (total_seconds2 - total_seconds1) % (24 * 3600)

        return timedelta(seconds=delta_seconds)

    @staticmethod
    def is_time_in_range(time_obj: AnyTime, start: AnyTime, end: AnyTime) -> bool:
        """Check whether ``time_obj`` is within the range [start, end].

        Handles ranges that cross midnight. If ``start`` and ``end`` are equal,
        the range contains only that single time.

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

        return start <= time_obj <= end if start <= end else time_obj >= start or time_obj <= end

    @staticmethod
    def round_time(time_obj: TimeT, round_to: int = 60) -> TimeT:
        """Round a time object to the nearest multiple of round_to seconds.

        Rounding is applied to the wall-clock reading; any ``tzinfo`` on the
        input is carried over unchanged.

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
        if isinstance(time_obj, time):
            rounded_time = _TimeAdjuster.seconds_to_time(rounded_seconds)
            return cast("TimeT", rounded_time.replace(tzinfo=time_obj.tzinfo))
        datetime_obj = cast("datetime", time_obj)
        midnight = datetime.combine(
            datetime_obj.date(),
            time.min,
            tzinfo=datetime_obj.tzinfo,
        )
        return cast("TimeT", midnight + timedelta(seconds=rounded_seconds))

    @staticmethod
    def time_to_seconds(time_obj: AnyTime) -> float:
        """Convert a time object to the total number of seconds since midnight.

        Args:
            time_obj (AnyTime): The time object to convert.

        Returns:
            float: The total number of seconds since midnight.

        Raises:
            TypeError: If time_obj is not a time or datetime instance.

        """
        if not isinstance(time_obj, (time, datetime)):
            error_message = "time_obj must be a time or datetime instance"
            raise TypeError(error_message)

        return time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second + time_obj.microsecond / 1e6

    @staticmethod
    def seconds_to_time(seconds: float) -> time:
        """Convert the total number of seconds since midnight to a time object.

        Args:
            seconds (float): The total number of seconds since midnight.

        Returns:
            time: The time object.

        """
        microseconds_per_second = 1_000_000
        microseconds_per_day = 24 * 3600 * microseconds_per_second
        total_microseconds = round((seconds % (24 * 3600)) * microseconds_per_second)
        total_microseconds %= microseconds_per_day

        hour, remainder = divmod(total_microseconds, 3600 * microseconds_per_second)
        minute, remainder = divmod(remainder, 60 * microseconds_per_second)
        second, microsecond = divmod(remainder, microseconds_per_second)

        return time(hour, minute, second, microsecond)
