# Copyright (c) 2024 Gabriel Mitelman Tkacz
"""Operations for adjusting dates to particular weekdays."""

from dateutil.relativedelta import relativedelta

from temporal_adjuster.common.decorators import sequenceable
from temporal_adjuster.common.enums import ISOWeekday, Weekday
from temporal_adjuster.common.exceptions import DateError
from temporal_adjuster.common.types import AnyDate, DateT

from .absolute_date_operations import _AbsoluteDateOperations
from .first_and_last_day_operations import _TemporalAdjusterForFirstAndLastDays

WeekdayLike = Weekday | ISOWeekday | str | int


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
    @sequenceable(target="date")
    def next(weekday: WeekdayLike, date: DateT) -> DateT:
        """Returns the next date of the given day of the week.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The next date of the given day of the week.

        """
        weekday = _TemporalAdjusterForWeekday.__normalize_weekday(weekday)

        return date + relativedelta(weekday=weekday.value) if date.weekday() != weekday.value else date + relativedelta(weekday=weekday.value) + relativedelta(weeks=1)

    @staticmethod
    @sequenceable(target="date")
    def next_or_same(weekday: WeekdayLike, date: DateT) -> DateT:
        """Returns the next date of the given day of the week. If the given date is the same day of the week, the given date is returned.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The next date of the given day of the week.

        """
        weekday = _TemporalAdjusterForWeekday.__normalize_weekday(weekday)

        return date if date.weekday() == weekday.value else _TemporalAdjusterForWeekday.next(weekday, date)

    @staticmethod
    @sequenceable(target="date")
    def last(weekday: WeekdayLike, date: DateT) -> DateT:
        """Returns the last date of the given day of the week.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The last date of the given day of the week.

        """
        weekday = _TemporalAdjusterForWeekday.__normalize_weekday(weekday)

        return _TemporalAdjusterForWeekday.next(weekday, date) - relativedelta(weeks=1) if date.weekday() != weekday.value else _TemporalAdjusterForWeekday.next(weekday, date) - relativedelta(weeks=2)

    @staticmethod
    @sequenceable(target="date")
    def last_or_same(weekday: WeekdayLike, date: DateT) -> DateT:
        """Returns the last date of the given day of the week. If the given date is the same day of the week, the given date is returned.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The last date of the given day of the week.

        """
        weekday = _TemporalAdjusterForWeekday.__normalize_weekday(weekday)

        return date if date.weekday() == weekday.value else _TemporalAdjusterForWeekday.last(weekday, date)

    @staticmethod
    @sequenceable(target="date")
    def first_of_month(weekday: WeekdayLike, date: DateT) -> DateT:
        """Returns the first date of the given day of the week in the month of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The first date of the given day of the week in the month of the given date.

        """
        weekday = _TemporalAdjusterForWeekday.__normalize_weekday(weekday)

        return date.replace(day=1) + relativedelta(weekday=weekday.value)

    @staticmethod
    @sequenceable(target="date")
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
    @sequenceable(target="date")
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
    @sequenceable(target="date")
    def last_of_month(weekday: WeekdayLike, date: DateT) -> DateT:
        """Returns the last date of the given day of the week in the month of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The last date of the given day of the week in the month of the given date.

        """
        weekday = _TemporalAdjusterForWeekday.__normalize_weekday(weekday)

        return _TemporalAdjusterForWeekday.last(
            weekday,
            date.replace(day=1) + relativedelta(months=1),
        )

    @staticmethod
    @sequenceable(target="date")
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
    @sequenceable(target="date")
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
    @sequenceable(target="date")
    def first_of_year(weekday: WeekdayLike, date: DateT) -> DateT:
        """Returns the first date of the given day of the week in the year of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The first date of the given day of the week in the year of the given date.

        """
        weekday = _TemporalAdjusterForWeekday.__normalize_weekday(weekday)

        return date.replace(month=1, day=1) + relativedelta(weekday=weekday.value)

    @staticmethod
    @sequenceable(target="date")
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
    @sequenceable(target="date")
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
    @sequenceable(target="date")
    def last_of_year(weekday: WeekdayLike, date: DateT) -> DateT:
        """Returns the last date of the given day of the week in the year of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The last date of the given day of the week in the year of the given date.

        """
        weekday = _TemporalAdjusterForWeekday.__normalize_weekday(weekday)

        return _TemporalAdjusterForWeekday.last(weekday, date.replace(month=12, day=31))

    @staticmethod
    @sequenceable(target="date")
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
    @sequenceable(target="date")
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
    @sequenceable(target="date")
    def nth_from_date(
        weekday: WeekdayLike,
        date: DateT,
        n: int,
    ) -> DateT:
        """Returns the nth date of the given day of the week from the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.
            n (int): The nth occurrence of the given day of the week.

        Returns:
            DateT: The nth date of the given day of the week from the given date.

        """
        weekday = _TemporalAdjusterForWeekday.__normalize_weekday(weekday)

        return date + relativedelta(weekday=weekday.value, weeks=n - 1)

    @staticmethod
    @sequenceable(target="date")
    def nth_of_month(weekday: WeekdayLike, date: DateT, n: int) -> DateT:
        """Returns the nth date of the given day of the week in the month of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.
            n (int): The nth occurrence of the given day of the week.

        Returns:
            DateT: The nth date of the given day of the week in the month of the given date.

        Raises:
            ValueError: If n is less than 1 or greater than 5.
            DateError: If the month does not have a nth occurrence of the given day of the week.

        """
        weekday = _TemporalAdjusterForWeekday.__normalize_weekday(weekday)

        if n < 1 or n > 5:
            raise ValueError(f"The value of n must be between 1 and 5, but is {n}.")

        output_date = date.replace(day=1) + relativedelta(
            weekday=weekday.value,
            weeks=n - 1,
        )

        if output_date.month != date.month:
            raise DateError(
            f"The month does not have a {n}th occurrence of {weekday.name.lower()}.",
            )

        return output_date

    @staticmethod
    @sequenceable(target="date")
    def nth_of_year(weekday: WeekdayLike, date: DateT, n: int) -> DateT:
        """Returns the nth date of the given day of the week in the year of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.
            n (int): The nth occurrence of the given day of the week.

        Returns:
            DateT: The nth date of the given day of the week in the year of the given date.

        Raises:
            ValueError: If n is less than 1 or greater than 54.
            DateError: If the year does not have a nth occurrence of the given day of the week.

        """
        weekday = _TemporalAdjusterForWeekday.__normalize_weekday(weekday)

        if n < 1 or n > 54:
            raise ValueError(f"The value of n must be between 1 and 54, but is {n}.")

        output_date = date.replace(month=1, day=1) + relativedelta(
            weekday=weekday.value,
            weeks=n - 1,
        )

        if output_date.year != date.year:
            raise DateError(
            f"The year does not have a {n}th occurrence of {weekday.name.lower()}.",
            )

        return output_date

    @staticmethod
    @sequenceable(target="date")
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
    @sequenceable(target="date")
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
