from dateutil.relativedelta import relativedelta

from ..common.decorators import sequenceable
from ..common.types.dates import DateT


class _TemporalAdjusterForFirstAndLastDays:
    @staticmethod
    @sequenceable(target="date")
    def first_day_of_week(date: DateT) -> DateT:
        """
        Returns the first day of the week of the given date. The week starts on Monday.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The first day of the week of the given date.
        """
        return date - relativedelta(days=date.weekday())

    @staticmethod
    @sequenceable(target="date")
    def first_day_of_next_week(date: DateT) -> DateT:
        """
        Returns the first day of the next week of the given date. The week starts on Monday.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The first day of the next week of the given date.
        """
        return _TemporalAdjusterForFirstAndLastDays.first_day_of_week(
            date
        ) + relativedelta(weeks=1)

    @staticmethod
    @sequenceable(target="date")
    def first_day_of_last_week(date: DateT) -> DateT:
        """
        Returns the first day of the last week of the given date. The week starts on Monday.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The first day of the next week of the given date.
        """
        return _TemporalAdjusterForFirstAndLastDays.first_day_of_week(
            date
        ) + relativedelta(weeks=-1)

    @staticmethod
    @sequenceable(target="date")
    def first_day_of_month(date: DateT) -> DateT:
        """
        Returns the first day of the month of the given date.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The first day of the month of the given date.
        """
        return date.replace(day=1)

    @staticmethod
    @sequenceable(target="date")
    def first_day_of_next_month(date: DateT) -> DateT:
        """
        Returns the first day of the next month of the given date.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The first day of the next month of the given date.
        """
        return _TemporalAdjusterForFirstAndLastDays.first_day_of_month(
            date
        ) + relativedelta(months=1)

    @staticmethod
    @sequenceable(target="date")
    def first_day_of_last_month(date: DateT) -> DateT:
        """
        Returns the first day of the last month of the given date.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The first day of the next month of the given date.
        """
        return _TemporalAdjusterForFirstAndLastDays.first_day_of_month(
            date
        ) + relativedelta(months=-1)

    @staticmethod
    @sequenceable(target="date")
    def first_day_of_year(date: DateT) -> DateT:
        """
        Returns the first day of the year of the given date.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The first day of the year of the given date.
        """
        return date.replace(month=1, day=1)

    @staticmethod
    @sequenceable(target="date")
    def first_day_of_next_year(date: DateT) -> DateT:
        """
        Returns the first day of the next year of the given date.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The first day of the next year of the given date.
        """
        return _TemporalAdjusterForFirstAndLastDays.first_day_of_year(
            date
        ) + relativedelta(years=1)

    @staticmethod
    @sequenceable(target="date")
    def first_day_of_last_year(date: DateT) -> DateT:
        """
        Returns the first day of the last year of the given date.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The first day of the next year of the given date.
        """
        return _TemporalAdjusterForFirstAndLastDays.first_day_of_year(
            date
        ) + relativedelta(years=-1)

    @staticmethod
    @sequenceable(target="date")
    def last_day_of_week(date: DateT) -> DateT:
        """
        Returns the last day of the week of the given date. The week ends on Sunday.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The last day of the week of the given date.
        """
        return date + relativedelta(days=6 - date.weekday())

    @staticmethod
    @sequenceable(target="date")
    def last_day_of_next_week(date: DateT) -> DateT:
        """
        Returns the last day of the next week of the given date. The week ends on Sunday.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The last day of the next week of the given date.
        """
        return _TemporalAdjusterForFirstAndLastDays.last_day_of_week(
            date
        ) + relativedelta(weeks=1)

    @staticmethod
    @sequenceable(target="date")
    def last_day_of_last_week(date: DateT) -> DateT:
        """
        Returns the last day of the last week of the given date. The week ends on Sunday.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The last day of the last week of the given date.
        """
        return _TemporalAdjusterForFirstAndLastDays.last_day_of_week(
            date
        ) + relativedelta(weeks=-1)

    @staticmethod
    @sequenceable(target="date")
    def last_day_of_month(date: DateT) -> DateT:
        """
        Returns the last day of the month of the given date.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The last day of the month of the given date.
        """
        return date.replace(day=1) + relativedelta(months=1, days=-1)

    @staticmethod
    @sequenceable(target="date")
    def last_day_of_next_month(date: DateT) -> DateT:
        """
        Returns the last day of the next month of the given date.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The last day of the next month of the given date.
        """
        return _TemporalAdjusterForFirstAndLastDays.last_day_of_month(
            date + relativedelta(months=1)
        )

    @staticmethod
    @sequenceable(target="date")
    def last_day_of_last_month(date: DateT) -> DateT:
        """
        Returns the last day of the last month of the given date.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The last day of the last month of the given date.
        """
        return _TemporalAdjusterForFirstAndLastDays.first_day_of_month(
            date
        ) + relativedelta(days=-1)

    @staticmethod
    @sequenceable(target="date")
    def last_day_of_year(date: DateT) -> DateT:
        """
        Returns the last day of the year of the given date.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The last day of the year of the given date.
        """
        return date.replace(month=12, day=31)

    @staticmethod
    @sequenceable(target="date")
    def last_day_of_next_year(date: DateT) -> DateT:
        """
        Returns the last day of the next year of the given date.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The last day of the next year of the given date.
        """
        return _TemporalAdjusterForFirstAndLastDays.last_day_of_year(
            date
        ) + relativedelta(years=1)

    @staticmethod
    @sequenceable(target="date")
    def last_day_of_last_year(date: DateT) -> DateT:
        """
        Returns the last day of the last year of the given date.

        Args:
            date (DateT): The date to adjust.

        Returns:
            DateT: The last day of the last year of the given date.
        """
        return _TemporalAdjusterForFirstAndLastDays.last_day_of_year(
            date
        ) + relativedelta(years=-1)
