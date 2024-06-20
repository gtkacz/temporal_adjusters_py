from .common.enums import ISOWeekday as ISOWeekday, Weekday as Weekday
from .common.types import DateT as DateT
from typing import Sequence

class TemporalAdjuster:
    """
    This class provides tools that help pinpoint very specific moments in time, without having to manually count days, weeks, or months. In essence, a Temporal Adjuster is a function that encapsulates a specific date/time manipulation rule. It operates on a temporal object (representing a date, time, or datetime) to produce a new temporal object adjusted according to the rule. This class provides a set of predefined temporal adjusters that can be used to adjust a temporal object in various ways.

    Examples:

    ```
    >>> from datetime import date, datetime

    >>> from temporal_adjuster import TemporalAdjuster
    >>> from temporal_adjuster.common.enums import Weekday

    >>> TemporalAdjuster.first_day_of_next_week(date(2021, 1, 1))
    datetime.date(2021, 1, 4)

    >>> TemporalAdjuster.last_day_of_last_week(date(2021, 1, 1))
    datetime.date(2020, 12, 27)

    >>> TemporalAdjuster.first_of_month(Weekday.SATURDAY, date(2021, 1, 1))
    datetime.date(2021, 2, 6)

    >>> TemporalAdjuster.nth_of_month(Weekday.SUNDAY, date(2021, 5, 1), 2)
    datetime.date(2021, 5, 9)

    ```
    """

    @staticmethod
    def first_day_of_week(date: DateT | Sequence[DateT]) -> DateT | Sequence[DateT]:
        """
        Returns the first day of the week of the given date. The week starts on Monday.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The first day of the week of the given date.
        """

    @staticmethod
    def first_day_of_next_week(
        date: DateT | Sequence[DateT],
    ) -> DateT | Sequence[DateT]:
        """
        Returns the first day of the next week of the given date. The week starts on Monday.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The first day of the next week of the given date.
        """

    @staticmethod
    def first_day_of_last_week(
        date: DateT | Sequence[DateT],
    ) -> DateT | Sequence[DateT]:
        """
        Returns the first day of the last week of the given date. The week starts on Monday.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The first day of the next week of the given date.
        """

    @staticmethod
    def first_day_of_month(date: DateT | Sequence[DateT]) -> DateT | Sequence[DateT]:
        """
        Returns the first day of the month of the given date.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The first day of the month of the given date.
        """

    @staticmethod
    def first_day_of_next_month(
        date: DateT | Sequence[DateT],
    ) -> DateT | Sequence[DateT]:
        """
        Returns the first day of the next month of the given date.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The first day of the next month of the given date.
        """

    @staticmethod
    def first_day_of_last_month(
        date: DateT | Sequence[DateT],
    ) -> DateT | Sequence[DateT]:
        """
        Returns the first day of the last month of the given date.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The first day of the next month of the given date.
        """

    @staticmethod
    def first_day_of_year(date: DateT | Sequence[DateT]) -> DateT | Sequence[DateT]:
        """
        Returns the first day of the year of the given date.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The first day of the year of the given date.
        """

    @staticmethod
    def first_day_of_next_year(
        date: DateT | Sequence[DateT],
    ) -> DateT | Sequence[DateT]:
        """
        Returns the first day of the next year of the given date.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The first day of the next year of the given date.
        """

    @staticmethod
    def first_day_of_last_year(
        date: DateT | Sequence[DateT],
    ) -> DateT | Sequence[DateT]:
        """
        Returns the first day of the last year of the given date.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The first day of the next year of the given date.
        """

    @staticmethod
    def last_day_of_week(date: DateT | Sequence[DateT]) -> DateT | Sequence[DateT]:
        """
        Returns the last day of the week of the given date. The week ends on Sunday.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The last day of the week of the given date.
        """

    @staticmethod
    def last_day_of_next_week(date: DateT | Sequence[DateT]) -> DateT | Sequence[DateT]:
        """
        Returns the last day of the next week of the given date. The week ends on Sunday.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The last day of the next week of the given date.
        """

    @staticmethod
    def last_day_of_last_week(date: DateT | Sequence[DateT]) -> DateT | Sequence[DateT]:
        """
        Returns the last day of the last week of the given date. The week ends on Sunday.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The last day of the last week of the given date.
        """

    @staticmethod
    def last_day_of_month(date: DateT | Sequence[DateT]) -> DateT | Sequence[DateT]:
        """
        Returns the last day of the month of the given date.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The last day of the month of the given date.
        """

    @staticmethod
    def last_day_of_next_month(
        date: DateT | Sequence[DateT],
    ) -> DateT | Sequence[DateT]:
        """
        Returns the last day of the next month of the given date.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The last day of the next month of the given date.
        """

    @staticmethod
    def last_day_of_last_month(
        date: DateT | Sequence[DateT],
    ) -> DateT | Sequence[DateT]:
        """
        Returns the last day of the last month of the given date.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The last day of the last month of the given date.
        """

    @staticmethod
    def last_day_of_year(date: DateT | Sequence[DateT]) -> DateT | Sequence[DateT]:
        """
        Returns the last day of the year of the given date.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The last day of the year of the given date.
        """

    @staticmethod
    def last_day_of_next_year(date: DateT | Sequence[DateT]) -> DateT | Sequence[DateT]:
        """
        Returns the last day of the next year of the given date.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The last day of the next year of the given date.
        """

    @staticmethod
    def last_day_of_last_year(date: DateT | Sequence[DateT]) -> DateT | Sequence[DateT]:
        """
        Returns the last day of the last year of the given date.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The last day of the last year of the given date.
        """

    @staticmethod
    def next(
        weekday: Weekday | ISOWeekday, date: DateT | Sequence[DateT]
    ) -> DateT | Sequence[DateT]:
        """
        Returns the next date of the given day of the week.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The next date of the given day of the week.
        """

    @staticmethod
    def next_or_same(
        weekday: Weekday | ISOWeekday, date: DateT | Sequence[DateT]
    ) -> DateT | Sequence[DateT]:
        """
        Returns the next date of the given day of the week. If the given date is the same day of the week, the given date is returned.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The next date of the given day of the week.
        """

    @staticmethod
    def last(
        weekday: Weekday | ISOWeekday, date: DateT | Sequence[DateT]
    ) -> DateT | Sequence[DateT]:
        """
        Returns the last date of the given day of the week.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The last date of the given day of the week.
        """

    @staticmethod
    def last_or_same(
        weekday: Weekday | ISOWeekday, date: DateT | Sequence[DateT]
    ) -> DateT | Sequence[DateT]:
        """
        Returns the last date of the given day of the week. If the given date is the same day of the week, the given date is returned.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The last date of the given day of the week.
        """

    @staticmethod
    def first_of_month(
        weekday: Weekday | ISOWeekday, date: DateT | Sequence[DateT]
    ) -> DateT | Sequence[DateT]:
        """
        Returns the first date of the given day of the week in the month of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The first date of the given day of the week in the month of the given date.
        """

    @staticmethod
    def first_of_next_month(
        weekday: Weekday | ISOWeekday, date: DateT | Sequence[DateT]
    ) -> DateT | Sequence[DateT]:
        """
        Returns the first date of the given day of the week in the month after the month of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The first date of the given day of the week in the month after the month of the given date.
        """

    @staticmethod
    def first_of_last_month(
        weekday: Weekday | ISOWeekday, date: DateT | Sequence[DateT]
    ) -> DateT | Sequence[DateT]:
        """
        Returns the first date of the given day of the week in the month before the month of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The first date of the given day of the week in the month before the month of the given date.
        """

    @staticmethod
    def last_of_month(
        weekday: Weekday | ISOWeekday, date: DateT | Sequence[DateT]
    ) -> DateT | Sequence[DateT]:
        """
        Returns the last date of the given day of the week in the month of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The last date of the given day of the week in the month of the given date.
        """

    @staticmethod
    def last_of_next_month(
        weekday: Weekday | ISOWeekday, date: DateT | Sequence[DateT]
    ) -> DateT | Sequence[DateT]:
        """
        Returns the last date of the given day of the week in the month after the month of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The last date of the given day of the week in the month after the month of the given date.
        """

    @staticmethod
    def last_of_last_month(
        weekday: Weekday | ISOWeekday, date: DateT | Sequence[DateT]
    ) -> DateT | Sequence[DateT]:
        """
        Returns the last date of the given day of the week in the month before the month of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The last date of the given day of the week in the month before the month of the given date.
        """

    @staticmethod
    def first_of_year(
        weekday: Weekday | ISOWeekday, date: DateT | Sequence[DateT]
    ) -> DateT | Sequence[DateT]:
        """
        Returns the first date of the given day of the week in the year of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The first date of the given day of the week in the year of the given date.
        """

    @staticmethod
    def first_of_next_year(
        weekday: Weekday | ISOWeekday, date: DateT | Sequence[DateT]
    ) -> DateT | Sequence[DateT]:
        """
        Returns the first date of the given day of the week in the year after the year of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The first date of the given day of the week in the year after the year of the given date.
        """

    @staticmethod
    def first_of_last_year(
        weekday: Weekday | ISOWeekday, date: DateT | Sequence[DateT]
    ) -> DateT | Sequence[DateT]:
        """
        Returns the first date of the given day of the week in the year before the year of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The first date of the given day of the week in the year before the year of the given date.
        """

    @staticmethod
    def last_of_year(
        weekday: Weekday | ISOWeekday, date: DateT | Sequence[DateT]
    ) -> DateT | Sequence[DateT]:
        """
        Returns the last date of the given day of the week in the year of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The last date of the given day of the week in the year of the given date.
        """

    @staticmethod
    def last_of_next_year(
        weekday: Weekday | ISOWeekday, date: DateT | Sequence[DateT]
    ) -> DateT | Sequence[DateT]:
        """
        Returns the last date of the given day of the week in the year after the year of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The last date of the given day of the week in the year after the year of the given date.
        """

    @staticmethod
    def last_of_last_year(
        weekday: Weekday | ISOWeekday, date: DateT | Sequence[DateT]
    ) -> DateT | Sequence[DateT]:
        """
        Returns the last date of the given day of the week in the year before the year of the given date.

        Args:
            weekday (Weekday): The day of the week.
            date (DateT): The reference date.

        Returns:
            DateT: The last date of the given day of the week in the year before the year of the given date.
        """

    @staticmethod
    def nth_from_date(
        weekday: Weekday | ISOWeekday, date: DateT | Sequence[DateT], n: int
    ) -> DateT | Sequence[DateT]:
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

    @staticmethod
    def nth_of_month(
        weekday: Weekday | ISOWeekday, date: DateT | Sequence[DateT], n: int
    ) -> DateT | Sequence[DateT]:
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

    @staticmethod
    def nth_of_year(
        weekday: Weekday | ISOWeekday, date: DateT | Sequence[DateT], n: int
    ) -> DateT | Sequence[DateT]:
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
