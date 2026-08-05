# Copyright (c) 2024 Gabriel Mitelman Tkacz
"""Operations for adjusting dates to particular weekdays."""

from datetime import timedelta

from temporal_adjuster.common.enums import ISOWeekday, Weekday
from temporal_adjuster.common.exceptions import DateError
from temporal_adjuster.common.types import AnyDate, DateT

from .absolute_date_operations import _AbsoluteDateOperations
from .first_and_last_day_operations import _TemporalAdjusterForFirstAndLastDays

WeekdayLike = Weekday | ISOWeekday | str | int

_DAYS_IN_WEEK = 7


class _TemporalAdjusterForWeekday:
    @staticmethod
    def __normalize_weekday(weekday: WeekdayLike) -> Weekday:
        """Parses the given weekday to the Pythonic format.

        Args:
            weekday (Union[Weekday, ISOWeekday, str, int]): The weekday to parse.

        Returns:
            Weekday: The parsed weekday.

        """
        if isinstance(weekday, Weekday):
            return weekday

        if isinstance(weekday, ISOWeekday):
            return Weekday[weekday.name]

        if isinstance(weekday, str):
            return Weekday[weekday.upper()]

        return Weekday(weekday)

    @staticmethod
    def next(weekday: WeekdayLike, date: DateT) -> DateT:
        """Returns the next date of the given day of the week.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The next date of the given day of the week.

        """
        weekday = _TemporalAdjusterForWeekday.__normalize_weekday(weekday)

        return date + timedelta(days=(weekday.value - date.weekday()) % _DAYS_IN_WEEK or _DAYS_IN_WEEK)

    @staticmethod
    def next_or_same(weekday: WeekdayLike, date: DateT) -> DateT:
        """Returns the next date of the given day of the week. If the given date is the same day of the week, the given date is returned.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The next date of the given day of the week.

        """
        weekday = _TemporalAdjusterForWeekday.__normalize_weekday(weekday)

        return date + timedelta(days=(weekday.value - date.weekday()) % _DAYS_IN_WEEK)

    @staticmethod
    def last(weekday: WeekdayLike, date: DateT) -> DateT:
        """Returns the last date of the given day of the week.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The last date of the given day of the week.

        """
        weekday = _TemporalAdjusterForWeekday.__normalize_weekday(weekday)

        return date - timedelta(days=(date.weekday() - weekday.value) % _DAYS_IN_WEEK or _DAYS_IN_WEEK)

    @staticmethod
    def last_or_same(weekday: WeekdayLike, date: DateT) -> DateT:
        """Returns the last date of the given day of the week. If the given date is the same day of the week, the given date is returned.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The last date of the given day of the week.

        """
        weekday = _TemporalAdjusterForWeekday.__normalize_weekday(weekday)

        return date - timedelta(days=(date.weekday() - weekday.value) % _DAYS_IN_WEEK)

    @staticmethod
    def previous(weekday: WeekdayLike, date: DateT) -> DateT:
        """Returns the previous date of the given day of the week.

        Alias of :meth:`last` matching the naming of Java's ``TemporalAdjusters.previous``.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The previous date of the given day of the week.

        """
        return _TemporalAdjusterForWeekday.last(weekday, date)

    @staticmethod
    def previous_or_same(weekday: WeekdayLike, date: DateT) -> DateT:
        """Returns the previous date of the given day of the week. If the given date is the same day of the week, the given date is returned.

        Alias of :meth:`last_or_same` matching the naming of Java's ``TemporalAdjusters.previousOrSame``.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The previous date of the given day of the week.

        """
        return _TemporalAdjusterForWeekday.last_or_same(weekday, date)

    @staticmethod
    def first_of_month(weekday: WeekdayLike, date: DateT) -> DateT:
        """Returns the first date of the given day of the week in the month of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The first date of the given day of the week in the month of the given date.

        """
        weekday = _TemporalAdjusterForWeekday.__normalize_weekday(weekday)

        return _TemporalAdjusterForWeekday.next_or_same(weekday, date.replace(day=1))

    @staticmethod
    def first_of_next_month(weekday: WeekdayLike, date: DateT) -> DateT:
        """Returns the first date of the given day of the week in the month after the month of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The first date of the given day of the week in the month after the month of the given date.

        """
        weekday = _TemporalAdjusterForWeekday.__normalize_weekday(weekday)

        return _TemporalAdjusterForWeekday.first_of_month(
            weekday,
            _TemporalAdjusterForFirstAndLastDays.first_day_of_next_month(date),
        )

    @staticmethod
    def first_of_last_month(weekday: WeekdayLike, date: DateT) -> DateT:
        """Returns the first date of the given day of the week in the month before the month of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The first date of the given day of the week in the month before the month of the given date.

        """
        weekday = _TemporalAdjusterForWeekday.__normalize_weekday(weekday)

        return _TemporalAdjusterForWeekday.first_of_month(
            weekday,
            _TemporalAdjusterForFirstAndLastDays.first_day_of_last_month(date),
        )

    @staticmethod
    def last_of_month(weekday: WeekdayLike, date: DateT) -> DateT:
        """Returns the last date of the given day of the week in the month of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The last date of the given day of the week in the month of the given date.

        """
        weekday = _TemporalAdjusterForWeekday.__normalize_weekday(weekday)

        return _TemporalAdjusterForWeekday.last_or_same(
            weekday,
            _TemporalAdjusterForFirstAndLastDays.last_day_of_month(date),
        )

    @staticmethod
    def last_of_next_month(weekday: WeekdayLike, date: DateT) -> DateT:
        """Returns the last date of the given day of the week in the month after the month of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The last date of the given day of the week in the month after the month of the given date.

        """
        weekday = _TemporalAdjusterForWeekday.__normalize_weekday(weekday)

        return _TemporalAdjusterForWeekday.last_of_month(
            weekday,
            _TemporalAdjusterForFirstAndLastDays.first_day_of_next_month(date),
        )

    @staticmethod
    def last_of_last_month(weekday: WeekdayLike, date: DateT) -> DateT:
        """Returns the last date of the given day of the week in the month before the month of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The last date of the given day of the week in the month before the month of the given date.

        """
        weekday = _TemporalAdjusterForWeekday.__normalize_weekday(weekday)

        return _TemporalAdjusterForWeekday.last_of_month(
            weekday,
            _TemporalAdjusterForFirstAndLastDays.first_day_of_last_month(date),
        )

    @staticmethod
    def first_of_year(weekday: WeekdayLike, date: DateT) -> DateT:
        """Returns the first date of the given day of the week in the year of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The first date of the given day of the week in the year of the given date.

        """
        weekday = _TemporalAdjusterForWeekday.__normalize_weekday(weekday)

        return _TemporalAdjusterForWeekday.next_or_same(
            weekday,
            date.replace(month=1, day=1),
        )

    @staticmethod
    def first_of_next_year(weekday: WeekdayLike, date: DateT) -> DateT:
        """Returns the first date of the given day of the week in the year after the year of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The first date of the given day of the week in the year after the year of the given date.

        """
        weekday = _TemporalAdjusterForWeekday.__normalize_weekday(weekday)

        return _TemporalAdjusterForWeekday.first_of_year(
            weekday,
            _TemporalAdjusterForFirstAndLastDays.first_day_of_next_year(date),
        )

    @staticmethod
    def first_of_last_year(weekday: WeekdayLike, date: DateT) -> DateT:
        """Returns the first date of the given day of the week in the year before the year of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The first date of the given day of the week in the year before the year of the given date.

        """
        weekday = _TemporalAdjusterForWeekday.__normalize_weekday(weekday)

        return _TemporalAdjusterForWeekday.first_of_year(
            weekday,
            _TemporalAdjusterForFirstAndLastDays.first_day_of_last_year(date),
        )

    @staticmethod
    def last_of_year(weekday: WeekdayLike, date: DateT) -> DateT:
        """Returns the last date of the given day of the week in the year of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The last date of the given day of the week in the year of the given date.

        """
        weekday = _TemporalAdjusterForWeekday.__normalize_weekday(weekday)

        return _TemporalAdjusterForWeekday.last_or_same(
            weekday,
            date.replace(month=12, day=31),
        )

    @staticmethod
    def last_of_next_year(weekday: WeekdayLike, date: DateT) -> DateT:
        """Returns the last date of the given day of the week in the year after the year of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The last date of the given day of the week in the year after the year of the given date.

        """
        weekday = _TemporalAdjusterForWeekday.__normalize_weekday(weekday)

        return _TemporalAdjusterForWeekday.last_of_year(
            weekday,
            _TemporalAdjusterForFirstAndLastDays.first_day_of_next_year(date),
        )

    @staticmethod
    def last_of_last_year(weekday: WeekdayLike, date: DateT) -> DateT:
        """Returns the last date of the given day of the week in the year before the year of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The last date of the given day of the week in the year before the year of the given date.

        """
        weekday = _TemporalAdjusterForWeekday.__normalize_weekday(weekday)

        return _TemporalAdjusterForWeekday.last_of_year(
            weekday,
            _TemporalAdjusterForFirstAndLastDays.first_day_of_last_year(date),
        )

    @staticmethod
    def nth_from_date(
        weekday: WeekdayLike,
        date: DateT,
        n: int,
    ) -> DateT:
        """Returns the nth date of the given day of the week from the given date.

        Counting starts at the given date: if the date already falls on the
        requested weekday, it is the first occurrence.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.
            n (int): The nth occurrence of the given day of the week.

        Returns:
            DateT: The nth date of the given day of the week from the given date.

        Raises:
            ValueError: If n is less than 1.

        """
        weekday = _TemporalAdjusterForWeekday.__normalize_weekday(weekday)

        if n < 1:
            raise ValueError(f"The value of n must be at least 1, but is {n}.")

        return _TemporalAdjusterForWeekday.next_or_same(weekday, date) + timedelta(
            weeks=n - 1,
        )

    @staticmethod
    def nth_of_month(weekday: WeekdayLike, date: DateT, n: int) -> DateT:
        """Returns the nth date of the given day of the week in the month of the given date.

        Negative values of n count backward from the end of the month: -1 is
        the last occurrence, -2 the second-to-last, and so on, matching Java's
        ``TemporalAdjusters.dayOfWeekInMonth``.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.
            n (int): The nth occurrence of the given day of the week.

        Returns:
            DateT: The nth date of the given day of the week in the month of the given date.

        Raises:
            ValueError: If n is 0 or outside the range -5 to 5.
            DateError: If the month does not have a nth occurrence of the given day of the week.

        """
        weekday = _TemporalAdjusterForWeekday.__normalize_weekday(weekday)

        if n == 0 or abs(n) > 5:
            raise ValueError(f"The value of n must be between -5 and 5, excluding 0, but is {n}.")

        output_date = (
            _TemporalAdjusterForWeekday.first_of_month(weekday, date) + timedelta(weeks=n - 1)
            if n > 0
            else _TemporalAdjusterForWeekday.last_of_month(weekday, date) + timedelta(weeks=n + 1)
        )

        if output_date.month != date.month:
            ordinal = f"{n}th" if n > 0 else f"{-n}th-to-last"
            raise DateError(
            f"The month does not have a {ordinal} occurrence of {weekday.name.lower()}.",
            )

        return output_date

    @staticmethod
    def nth_of_year(weekday: WeekdayLike, date: DateT, n: int) -> DateT:
        """Returns the nth date of the given day of the week in the year of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.
            n (int): The nth occurrence of the given day of the week.

        Returns:
            DateT: The nth date of the given day of the week in the year of the given date.

        Raises:
            ValueError: If n is less than 1 or greater than 53.
            DateError: If the year does not have a nth occurrence of the given day of the week.

        """
        weekday = _TemporalAdjusterForWeekday.__normalize_weekday(weekday)

        if n < 1 or n > 53:
            raise ValueError(f"The value of n must be between 1 and 53, but is {n}.")

        output_date = _TemporalAdjusterForWeekday.first_of_year(
            weekday,
            date,
        ) + timedelta(weeks=n - 1)

        if output_date.year != date.year:
            raise DateError(
            f"The year does not have a {n}th occurrence of {weekday.name.lower()}.",
            )

        return output_date

    @staticmethod
    def which_of_month(weekday: WeekdayLike, date: AnyDate) -> int:
        """Returns the occurrence of the given day of the week in the month of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            int: The occurrence of the given day of the week in the month of the given date.

        Raises:
            ValueError: If the date does not fall on the requested weekday.

        """
        weekday = _TemporalAdjusterForWeekday.__normalize_weekday(weekday)

        if date.weekday() != weekday.value:
            raise ValueError(
            f"The date {date} does not fall on {weekday.name.lower()}.",
            )

        return (date.day - 1) // 7 + 1

    @staticmethod
    def which_of_year(weekday: WeekdayLike, date: AnyDate) -> int:
        """Returns the occurrence of the given day of the week in the year of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            int: The occurrence of the given day of the week in the year of the given date.

        Raises:
            ValueError: If the date does not fall on the requested weekday.

        """
        weekday = _TemporalAdjusterForWeekday.__normalize_weekday(weekday)

        if date.weekday() != weekday.value:
            raise ValueError(
            f"The date {date} does not fall on {weekday.name.lower()}.",
            )

        return (_AbsoluteDateOperations.date_to_int_of_year(date) - 1) // 7 + 1
