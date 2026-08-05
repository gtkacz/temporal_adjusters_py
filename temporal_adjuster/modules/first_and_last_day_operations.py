# Copyright (c) 2024 Gabriel Mitelman Tkacz
"""Operations for finding the first and last days of calendar periods."""

from calendar import monthrange
from datetime import timedelta

from temporal_adjuster.common.types.dates import DateT

_ONE_DAY = timedelta(days=1)
_ONE_WEEK = timedelta(weeks=1)


class _TemporalAdjusterForFirstAndLastDays:
    @staticmethod
    def first_day_of_week(date: DateT) -> DateT:
        """Returns the first day of the week of the given date. The week starts on Monday.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The first day of the week of the given date.

        """
        return date - timedelta(days=date.weekday())

    @staticmethod
    def first_day_of_next_week(date: DateT) -> DateT:
        """Returns the first day of the next week of the given date. The week starts on Monday.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The first day of the next week of the given date.

        """
        return _TemporalAdjusterForFirstAndLastDays.first_day_of_week(date) + _ONE_WEEK

    @staticmethod
    def first_day_of_last_week(date: DateT) -> DateT:
        """Returns the first day of the last week of the given date. The week starts on Monday.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The first day of the last week of the given date.

        """
        return _TemporalAdjusterForFirstAndLastDays.first_day_of_week(date) - _ONE_WEEK

    @staticmethod
    def first_day_of_month(date: DateT) -> DateT:
        """Returns the first day of the month of the given date.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The first day of the month of the given date.

        """
        return date.replace(day=1)

    @staticmethod
    def first_day_of_next_month(date: DateT) -> DateT:
        """Returns the first day of the next month of the given date.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The first day of the next month of the given date.

        """
        return _TemporalAdjusterForFirstAndLastDays.last_day_of_month(date) + _ONE_DAY

    @staticmethod
    def first_day_of_last_month(date: DateT) -> DateT:
        """Returns the first day of the last month of the given date.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The first day of the last month of the given date.

        """
        return (date.replace(day=1) - _ONE_DAY).replace(day=1)

    @staticmethod
    def first_day_of_year(date: DateT) -> DateT:
        """Returns the first day of the year of the given date.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The first day of the year of the given date.

        """
        return date.replace(month=1, day=1)

    @staticmethod
    def first_day_of_next_year(date: DateT) -> DateT:
        """Returns the first day of the next year of the given date.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The first day of the next year of the given date.

        """
        return date.replace(year=date.year + 1, month=1, day=1)

    @staticmethod
    def first_day_of_last_year(date: DateT) -> DateT:
        """Returns the first day of the last year of the given date.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The first day of the last year of the given date.

        """
        return date.replace(year=date.year - 1, month=1, day=1)

    @staticmethod
    def last_day_of_week(date: DateT) -> DateT:
        """Returns the last day of the week of the given date. The week ends on Sunday.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The last day of the week of the given date.

        """
        return date + timedelta(days=6 - date.weekday())

    @staticmethod
    def last_day_of_next_week(date: DateT) -> DateT:
        """Returns the last day of the next week of the given date. The week ends on Sunday.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The last day of the next week of the given date.

        """
        return _TemporalAdjusterForFirstAndLastDays.last_day_of_week(date) + _ONE_WEEK

    @staticmethod
    def last_day_of_last_week(date: DateT) -> DateT:
        """Returns the last day of the last week of the given date. The week ends on Sunday.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The last day of the last week of the given date.

        """
        return _TemporalAdjusterForFirstAndLastDays.last_day_of_week(date) - _ONE_WEEK

    @staticmethod
    def last_day_of_month(date: DateT) -> DateT:
        """Returns the last day of the month of the given date.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The last day of the month of the given date.

        """
        return date.replace(day=monthrange(date.year, date.month)[1])

    @staticmethod
    def last_day_of_next_month(date: DateT) -> DateT:
        """Returns the last day of the next month of the given date.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The last day of the next month of the given date.

        """
        return _TemporalAdjusterForFirstAndLastDays.last_day_of_month(
            _TemporalAdjusterForFirstAndLastDays.first_day_of_next_month(date),
        )

    @staticmethod
    def last_day_of_last_month(date: DateT) -> DateT:
        """Returns the last day of the last month of the given date.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The last day of the last month of the given date.

        """
        return date.replace(day=1) - _ONE_DAY

    @staticmethod
    def last_day_of_year(date: DateT) -> DateT:
        """Returns the last day of the year of the given date.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The last day of the year of the given date.

        """
        return date.replace(month=12, day=31)

    @staticmethod
    def last_day_of_next_year(date: DateT) -> DateT:
        """Returns the last day of the next year of the given date.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The last day of the next year of the given date.

        """
        return date.replace(year=date.year + 1, month=12, day=31)

    @staticmethod
    def last_day_of_last_year(date: DateT) -> DateT:
        """Returns the last day of the last year of the given date.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The last day of the last year of the given date.

        """
        return date.replace(year=date.year - 1, month=12, day=31)
