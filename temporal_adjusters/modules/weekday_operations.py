import stat
from dateutil.relativedelta import relativedelta

from ..util.enums import DayOfWeek
from ..util.types import DateT

from .first_and_last_days import _TemporalAdjusterForFirstAndLastDays


class _TemporalAdjusterForWeekday:
    @staticmethod
    def next(day_of_week: DayOfWeek, date: DateT) -> DateT:
        """
        Returns the next date of the given day of the week.

        Args:
            day_of_week (DayOfWeek): The day of the week.
            date (DateT): The date.

        Returns:
            DateT: The next date of the given day of the week.
        """
        return date + relativedelta(weekday=day_of_week.value)

    @staticmethod
    def next_or_same(day_of_week: DayOfWeek, date: DateT) -> DateT:
        """
        Returns the next date of the given day of the week. If the given date is the same day of the week, the given date is returned.

        Args:
            day_of_week (DayOfWeek): The day of the week.
            date (DateT): The date.

        Returns:
            DateT: The next date of the given day of the week.
        """
        return date if date.weekday() == day_of_week.value else _TemporalAdjusterForWeekday.next(day_of_week, date)

    @staticmethod
    def previous(day_of_week: DayOfWeek, date: DateT) -> DateT:
        """
        Returns the previous date of the given day of the week.

        Args:
            day_of_week (DayOfWeek): The day of the week.
            date (DateT): The date.

        Returns:
            DateT: The previous date of the given day of the week.
        """
        return _TemporalAdjusterForWeekday.next(day_of_week, date) - relativedelta(weeks=1)

    @staticmethod
    def previous_or_same(day_of_week: DayOfWeek, date: DateT) -> DateT:
        """
        Returns the previous date of the given day of the week. If the given date is the same day of the week, the given date is returned.

        Args:
            day_of_week (DayOfWeek): The day of the week.
            date (DateT): The date.

        Returns:
            DateT: The previous date of the given day of the week.
        """
        return date if date.weekday() == day_of_week.value else _TemporalAdjusterForWeekday.previous(day_of_week, date)

    @staticmethod
    def first_in_month(day_of_week: DayOfWeek, date: DateT) -> DateT:
        """
        Returns the first date of the given day of the week in the month of the given date.

        Args:
            day_of_week (DayOfWeek): The day of the week.
            date (DateT): The date.

        Returns:
            DateT: The first date of the given day of the week in the month of the given date.
        """
        return date.replace(day=1) + relativedelta(weekday=day_of_week.value)

    @staticmethod
    def first_in_next_month(day_of_week: DayOfWeek, date: DateT) -> DateT:
        """
        Returns the first date of the given day of the week in the month after the month of the given date.

        Args:
            day_of_week (DayOfWeek): The day of the week.
            date (DateT): The date.

        Returns:
            DateT: The first date of the given day of the week in the month after the month of the given date.
        """
        return _TemporalAdjusterForWeekday.first_in_month(day_of_week, _TemporalAdjusterForFirstAndLastDays.first_day_of_next_month(date))

    @staticmethod
    def first_in_last_month(day_of_week: DayOfWeek, date: DateT) -> DateT:
        """
        Returns the first date of the given day of the week in the month before the month of the given date.

        Args:
            day_of_week (DayOfWeek): The day of the week.
            date (DateT): The date.

        Returns:
            DateT: The first date of the given day of the week in the month before the month of the given date.
        """
        return _TemporalAdjusterForWeekday.first_in_month(day_of_week, _TemporalAdjusterForFirstAndLastDays.first_day_of_previous_month(date))

    @staticmethod
    def last_in_month(day_of_week: DayOfWeek, date: DateT) -> DateT:
        """
        Returns the last date of the given day of the week in the month of the given date.

        Args:
            day_of_week (DayOfWeek): The day of the week.
            date (DateT): The date.

        Returns:
            DateT: The last date of the given day of the week in the month of the given date.
        """
        return _TemporalAdjusterForWeekday.previous(day_of_week, date.replace(day=1) + relativedelta(months=1))

    @staticmethod
    def last_in_next_month(day_of_week: DayOfWeek, date: DateT) -> DateT:
        """
        Returns the last date of the given day of the week in the month after the month of the given date.

        Args:
            day_of_week (DayOfWeek): The day of the week.
            date (DateT): The date.

        Returns:
            DateT: The last date of the given day of the week in the month after the month of the given date.
        """
        return _TemporalAdjusterForWeekday.last_in_month(day_of_week, _TemporalAdjusterForFirstAndLastDays.first_day_of_next_month(date))

    @staticmethod
    def last_in_last_month(day_of_week: DayOfWeek, date: DateT) -> DateT:
        """
        Returns the last date of the given day of the week in the month before the month of the given date.

        Args:
            day_of_week (DayOfWeek): The day of the week.
            date (DateT): The date.

        Returns:
            DateT: The last date of the given day of the week in the month before the month of the given date.
        """
        return _TemporalAdjusterForWeekday.last_in_month(day_of_week, _TemporalAdjusterForFirstAndLastDays.first_day_of_last_month(date))

    @staticmethod
    def first_in_year(day_of_week: DayOfWeek, date: DateT) -> DateT:
        """
        Returns the first date of the given day of the week in the year of the given date.

        Args:
            day_of_week (DayOfWeek): The day of the week.
            date (DateT): The date.

        Returns:
            DateT: The first date of the given day of the week in the year of the given date.
        """
        return date.replace(month=1, day=1) + relativedelta(weekday=day_of_week.value)

    @staticmethod
    def first_in_next_year(day_of_week: DayOfWeek, date: DateT) -> DateT:
        """
        Returns the first date of the given day of the week in the year after the year of the given date.

        Args:
            day_of_week (DayOfWeek): The day of the week.
            date (DateT): The date.

        Returns:
            DateT: The first date of the given day of the week in the year after the year of the given date.
        """
        return _TemporalAdjusterForWeekday.first_in_year(day_of_week, _TemporalAdjusterForFirstAndLastDays.first_day_of_next_year(date))

    @staticmethod
    def first_in_last_year(day_of_week: DayOfWeek, date: DateT) -> DateT:
        """
        Returns the first date of the given day of the week in the year before the year of the given date.

        Args:
            day_of_week (DayOfWeek): The day of the week.
            date (DateT): The date.

        Returns:
            DateT: The first date of the given day of the week in the year before the year of the given date.
        """
        return _TemporalAdjusterForWeekday.first_in_year(day_of_week, _TemporalAdjusterForFirstAndLastDays.first_day_of_last_year(date))
