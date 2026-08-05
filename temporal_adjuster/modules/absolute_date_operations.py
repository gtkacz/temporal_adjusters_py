# Copyright (c) 2024 Gabriel Mitelman Tkacz
"""Operations for adjusting absolute dates."""

from calendar import isleap, monthrange
from operator import index

from dateutil.relativedelta import relativedelta

from temporal_adjuster.common.types.dates import DateT


class _AbsoluteDateOperations:
    @staticmethod
    def _validate_day_index(int_value: int, maximum: int, period: str) -> int:
        type_error_message = "int_value must be an integer"
        if isinstance(int_value, bool):
            raise TypeError(type_error_message)

        try:
            int_value = index(int_value)
        except TypeError as error:
            raise TypeError(type_error_message) from error

        if not 1 <= int_value <= maximum:
            raise ValueError(
                f"int_value must be between 1 and {maximum} for the given {period}",
            )
        return int_value

    @staticmethod
    def int_to_day_of_year(date: DateT, int_value: int) -> DateT:
        """Returns the date of the given day of the year.

        Args:
            date (DateT): The date to adjust.
            int_value (int): The day of the year.

        Returns:
            DateT: The date of the given day of the year.

        Example:
            >>> from datetime import date
            >>> int_to_day_of_year(date(2021, 10, 10), 1)
            datetime.date(2021, 1, 1)

        """
        maximum = 366 if isleap(date.year) else 365
        int_value = _AbsoluteDateOperations._validate_day_index(
            int_value,
            maximum,
            "year",
        )
        return date.replace(month=1, day=1) + relativedelta(days=int_value - 1)

    @staticmethod
    def int_to_day_of_month(date: DateT, int_value: int) -> DateT:
        """Returns the date of the given day of the month.

        Args:
            date (DateT): The date to adjust.
            int_value (int): The day of the month.

        Returns:
            DateT: The date of the given day of the month.

        Example:
            >>> from datetime import date
            >>> int_to_day_of_month(date(2021, 1, 1), 1)
            datetime.date(2021, 1, 1)

        """
        maximum = monthrange(date.year, date.month)[1]
        int_value = _AbsoluteDateOperations._validate_day_index(
            int_value,
            maximum,
            "month",
        )
        return date.replace(day=int_value)

    @staticmethod
    def date_to_int_of_year(date: DateT) -> int:
        """Returns the integer value for the given day of the year of the given date.

        Args:
            date (DateT): The date to adjust.

        Returns:
            int: The day of the year of the given date.

        Example:
            >>> from datetime import date
            >>> date_to_int_of_year(date(2021, 1, 1))
            1

        """
        return date.timetuple().tm_yday

    @staticmethod
    def date_to_int_of_month(date: DateT) -> int:
        """Returns the integer value for the given day of the month of the given date.

        Args:
            date (DateT): The date to adjust.

        Returns:
            int: The day of the month of the given date.

        Example:
            >>> from datetime import date
            >>> date_to_int_of_month(date(2021, 1, 1))
            1

        """
        return date.day
