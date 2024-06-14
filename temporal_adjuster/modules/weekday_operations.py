from dateutil.relativedelta import relativedelta

from common.enums import ISOWeekday, Weekday
from common.exceptions import DateError
from common.types import DateT
from .first_and_last_day_operations import _TemporalAdjusterForFirstAndLastDays


class _TemporalAdjusterForWeekday:
    @staticmethod
    def next(weekday: Weekday, date: DateT) -> DateT:
        """
        Returns the next date of the given day of the week.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The next date of the given day of the week.
        """
        return (
            date + relativedelta(weekday=weekday.value)
            if date.weekday() != weekday.value
            else date + relativedelta(weekday=weekday.value) + relativedelta(weeks=1)
        )

    @staticmethod
    def next_or_same(weekday: Weekday, date: DateT) -> DateT:
        """
        Returns the next date of the given day of the week. If the given date is the same day of the week, the given date is returned.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The next date of the given day of the week.
        """
        return (
            date
            if date.weekday() == weekday.value
            else _TemporalAdjusterForWeekday.next(weekday, date)
        )

    @staticmethod
    def last(weekday: Weekday, date: DateT) -> DateT:
        """
        Returns the last date of the given day of the week.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The last date of the given day of the week.
        """
        return (
            _TemporalAdjusterForWeekday.next(weekday, date) - relativedelta(weeks=1)
            if date.weekday() != weekday.value
            else _TemporalAdjusterForWeekday.next(weekday, date)
            - relativedelta(weeks=2)
        )

    @staticmethod
    def last_or_same(weekday: Weekday, date: DateT) -> DateT:
        """
        Returns the last date of the given day of the week. If the given date is the same day of the week, the given date is returned.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The last date of the given day of the week.
        """
        return (
            date
            if date.weekday() == weekday.value
            else _TemporalAdjusterForWeekday.last(weekday, date)
        )

    @staticmethod
    def first_of_month(weekday: Weekday, date: DateT) -> DateT:
        """
        Returns the first date of the given day of the week in the month of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The first date of the given day of the week in the month of the given date.
        """
        return date.replace(day=1) + relativedelta(weekday=weekday.value)

    @staticmethod
    def first_of_next_month(weekday: Weekday, date: DateT) -> DateT:
        """
        Returns the first date of the given day of the week in the month after the month of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The first date of the given day of the week in the month after the month of the given date.
        """
        return _TemporalAdjusterForWeekday.first_of_month(
            weekday, _TemporalAdjusterForFirstAndLastDays.first_day_of_next_month(date)
        )

    @staticmethod
    def first_of_last_month(weekday: Weekday, date: DateT) -> DateT:
        """
        Returns the first date of the given day of the week in the month before the month of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The first date of the given day of the week in the month before the month of the given date.
        """
        return _TemporalAdjusterForWeekday.first_of_month(
            weekday, _TemporalAdjusterForFirstAndLastDays.first_day_of_last_month(date)
        )

    @staticmethod
    def last_of_month(weekday: Weekday, date: DateT) -> DateT:
        """
        Returns the last date of the given day of the week in the month of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The last date of the given day of the week in the month of the given date.
        """
        return _TemporalAdjusterForWeekday.last(
            weekday, date.replace(day=1) + relativedelta(months=1)
        )

    @staticmethod
    def last_of_next_month(weekday: Weekday, date: DateT) -> DateT:
        """
        Returns the last date of the given day of the week in the month after the month of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The last date of the given day of the week in the month after the month of the given date.
        """
        return _TemporalAdjusterForWeekday.last_of_month(
            weekday, _TemporalAdjusterForFirstAndLastDays.first_day_of_next_month(date)
        )

    @staticmethod
    def last_of_last_month(weekday: Weekday, date: DateT) -> DateT:
        """
        Returns the last date of the given day of the week in the month before the month of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The last date of the given day of the week in the month before the month of the given date.
        """
        return _TemporalAdjusterForWeekday.last_of_month(
            weekday, _TemporalAdjusterForFirstAndLastDays.first_day_of_last_month(date)
        )

    @staticmethod
    def first_of_year(weekday: Weekday, date: DateT) -> DateT:
        """
        Returns the first date of the given day of the week in the year of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The first date of the given day of the week in the year of the given date.
        """
        return date.replace(month=1, day=1) + relativedelta(weekday=weekday.value)

    @staticmethod
    def first_of_next_year(weekday: Weekday, date: DateT) -> DateT:
        """
        Returns the first date of the given day of the week in the year after the year of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The first date of the given day of the week in the year after the year of the given date.
        """
        return _TemporalAdjusterForWeekday.first_of_year(
            weekday, _TemporalAdjusterForFirstAndLastDays.first_day_of_next_year(date)
        )

    @staticmethod
    def first_of_last_year(weekday: Weekday, date: DateT) -> DateT:
        """
        Returns the first date of the given day of the week in the year before the year of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The first date of the given day of the week in the year before the year of the given date.
        """
        return _TemporalAdjusterForWeekday.first_of_year(
            weekday, _TemporalAdjusterForFirstAndLastDays.first_day_of_last_year(date)
        )

    @staticmethod
    def last_of_year(weekday: Weekday, date: DateT) -> DateT:
        """
        Returns the last date of the given day of the week in the year of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The last date of the given day of the week in the year of the given date.
        """
        return _TemporalAdjusterForWeekday.last(weekday, date.replace(month=12, day=31))

    @staticmethod
    def last_of_next_year(weekday: Weekday, date: DateT) -> DateT:
        """
        Returns the last date of the given day of the week in the year after the year of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The last date of the given day of the week in the year after the year of the given date.
        """
        return _TemporalAdjusterForWeekday.last_of_year(
            weekday, _TemporalAdjusterForFirstAndLastDays.first_day_of_next_year(date)
        )

    @staticmethod
    def last_of_last_year(weekday: Weekday, date: DateT) -> DateT:
        """
        Returns the last date of the given day of the week in the year before the year of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The last date of the given day of the week in the year before the year of the given date.
        """
        return _TemporalAdjusterForWeekday.last_of_year(
            weekday, _TemporalAdjusterForFirstAndLastDays.first_day_of_last_year(date)
        )

    @staticmethod
    def nth_from_date(weekday: Weekday, date: DateT, n: int) -> DateT:
        """
        Returns the nth date of the given day of the week from the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.
            n (int): The nth occurrence of the given day of the week.

        Raises:
            ValueError: If n is less than 1 or greater than 5.
            DateError: If the nth occurrence of the given day of the week does not exist from the given date.

        Returns:
            DateT: The nth date of the given day of the week from the given date.
        """
        return date + relativedelta(weekday=weekday.value, weeks=n - 1)

    @staticmethod
    def nth_of_month(weekday: Weekday, date: DateT, n: int) -> DateT:
        """
        Returns the nth date of the given day of the week in the month of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.
            n (int): The nth occurrence of the given day of the week.

        Raises:
            ValueError: If n is less than 1 or greater than 5.
            DateError: If the month does not have a nth occurrence of the given day of the week.

        Returns:
            DateT: The nth date of the given day of the week in the month of the given date.
        """
        if n < 1 or n > 5:
            raise ValueError(f"The value of n must be between 1 and 5, but is {n}.")

        output_date = date.replace(day=1) + relativedelta(
            weekday=weekday.value, weeks=n - 1
        )

        if output_date.month != date.month:
            raise DateError(
                f"The month does not have a {n}th occurrence of {weekday.name.lower()}."
            )

        return output_date

    @staticmethod
    def nth_of_year(weekday: Weekday, date: DateT, n: int) -> DateT:
        """
        Returns the nth date of the given day of the week in the year of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.
            n (int): The nth occurrence of the given day of the week.

        Raises:
            ValueError: If n is less than 1 or greater than 5.
            DateError: If the year does not have a nth occurrence of the given day of the week.

        Returns:
            DateT: The nth date of the given day of the week in the year of the given date.
        """
        if n < 1 or n > 54:
            raise ValueError(f"The value of n must be between 1 and 54, but is {n}.")

        output_date = date.replace(month=1, day=1) + relativedelta(
            weekday=weekday.value, weeks=n - 1
        )

        if output_date.year != date.year:
            raise DateError(
                f"The year does not have a {n}th occurrence of {weekday.name.lower()}."
            )

        return output_date