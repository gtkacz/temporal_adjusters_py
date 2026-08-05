# Copyright (c) 2024 Gabriel Mitelman Tkacz

import math
from collections.abc import Iterator
from datetime import timedelta
from types import NotImplementedType
from typing import ClassVar, Self


def _reconstruct_extended_timedelta(
    values: tuple[float, float, float, float, float, float, float],
) -> "ExtendedTimeDelta":
    (
        microseconds,
        seconds,
        days,
        months,
        years,
        days_in_month,
        days_in_year,
    ) = values
    return ExtendedTimeDelta(
        microseconds=microseconds,
        seconds=seconds,
        days=days,
        months=months,
        years=years,
        days_in_month=days_in_month,
        days_in_year=days_in_year,
    )


class ExtendedTimeDelta(timedelta):
    """An extended version of Python's timedelta that supports months and years.

    This class extends the standard timedelta by adding support for months and years.
    Since timedelta does not natively support months and years, the conversion assumes
    fixed lengths: 30.436875 days per month and 365.25 days per year by default.
    Note that these conversions are approximations and may not be suitable for all
    use cases.

    ``ExtendedTimeDelta`` is a ``timedelta`` subclass for compatibility, but the
    extra month and year components are not part of ``timedelta``'s C-level state.
    Convert it with :meth:`to_timedelta` before using it as the right-hand operand
    of date or datetime arithmetic so those components are included.
    """

    DAYS_IN_MONTH: ClassVar[float] = 30.436875
    DAYS_IN_YEAR: ClassVar[float] = 365.25

    _days_in_month: float
    _days_in_year: float
    _months: int | float
    _years: int

    __slots__ = (
        "_days_in_month",
        "_days_in_year",
        "_months",
        "_years",
    )

    def __new__(  # ruff: ignore[too-many-arguments, too-many-locals, too-many-positional-arguments]
        cls,
        microseconds: float = 0,
        milliseconds: float = 0,
        seconds: float = 0,
        minutes: float = 0,
        hours: float = 0,
        days: float = 0,
        weeks: float = 0,
        months: float = 0,
        years: float = 0,
        *,
        days_in_month: float = DAYS_IN_MONTH,
        days_in_year: float = DAYS_IN_YEAR,
    ) -> Self:
        """Create a new ExtendedTimeDelta instance.

        This method processes additional keyword arguments `months` and `years`
        and converts them into days using the approximations (defaults to 30 days per month,
        12 months per year).

        Args:
                days (int or float, optional): Number of days.
                microseconds (int, optional): Number of microseconds.
                milliseconds (int, optional): Number of milliseconds.
                seconds (int or float, optional): Number of seconds.
                minutes (int, optional): Number of minutes.
                hours (int, optional): Number of hours.
                weeks (int or float, optional): Number of weeks.
                months (int or float, optional): Number of months (assumes 30 days per month).
                years (int or float, optional): Number of years (assumes 12 months per year).
                days_in_month (float, optional): Average number of days in a month.
                days_in_year (float, optional): Average number of days in a year.

        Returns:
                ExtendedTimeDelta: A new instance of ExtendedTimeDelta.

        Raises:
                TypeError: If a conversion setting is not numeric.
                ValueError: If a conversion setting is not positive and finite.

        Example:
                >>> et = ExtendedTimeDelta(days=45, months=1)
                >>> print(et)
                1 month, 15 days, 0:00:00

        """
        for name, value in (
            ("days_in_month", days_in_month),
            ("days_in_year", days_in_year),
        ):
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise TypeError(f"{name} must be a real number")
            if not math.isfinite(value) or value <= 0:
                raise ValueError(f"{name} must be a positive finite number")

        days_in_month = float(days_in_month)
        days_in_year = float(days_in_year)

        # Process microseconds
        microseconds = int(microseconds)
        extra_microseconds = microseconds % 1e6
        seconds += microseconds // 1e6
        microseconds = extra_microseconds

        # Process seconds
        if isinstance(seconds, float):
            s_frac, s_whole = math.modf(seconds)
            seconds = int(s_whole)
            microseconds += s_frac * 1e6
        else:
            seconds = int(seconds)

        extra_seconds = seconds % 60
        minutes += seconds // 60
        seconds = extra_seconds

        # Process days
        if isinstance(days, float):
            d_frac, d_whole = math.modf(days)
            days = int(d_whole)
            seconds += d_frac * 86400
        else:
            days = int(days)

        extra_days = days % days_in_month
        months += days // days_in_month
        days = extra_days

        # Process months
        if isinstance(months, float):
            m_frac, m_whole = math.modf(months)
            months = int(m_whole)
            days += m_frac * days_in_month
        else:
            months = int(months)

        extra_months = months % 12
        years += months // 12
        months = extra_months

        # Process years
        if isinstance(years, float):
            y_frac, y_whole = math.modf(years)
            years = int(y_whole)
            months += y_frac * 12
        else:
            years = int(years)

        self = super().__new__(
            cls,
            days=days,
            seconds=seconds,
            microseconds=microseconds,
            milliseconds=milliseconds,
            weeks=weeks,
            minutes=minutes,
            hours=hours,
        )

        self._months = months
        self._years = years
        self._days_in_month = days_in_month
        self._days_in_year = days_in_year

        return self

    @property
    def months(self) -> int | float:
        """int: The months component of the ExtendedTimeDelta.

        Returns:
                int: The number of months.

        Example:
                >>> et = ExtendedTimeDelta(months=5)
                >>> et.months
                5

        """
        return self._months

    @property
    def years(self) -> int:
        """int: The years component of the ExtendedTimeDelta.

        Returns:
                int: The number of years.

        Example:
                >>> et = ExtendedTimeDelta(years=2)
                >>> et.years
                2

        """
        return self._years

    @property
    def days_in_month(self) -> float:
        """The month length used when converting this instance."""
        return self._days_in_month

    @property
    def days_in_year(self) -> float:
        """The year length used when converting this instance."""
        return self._days_in_year

    def __add__(self, other: object) -> Self | NotImplementedType:
        """Add two ExtendedTimeDelta or timedelta objects.

        Args:
                other (ExtendedTimeDelta or timedelta): The time delta to add.

        Returns:
                ExtendedTimeDelta: A new ExtendedTimeDelta representing the sum.

        Example:
                >>> et1 = ExtendedTimeDelta(years=1, days=10)
                >>> et2 = ExtendedTimeDelta(months=6, days=5)
                >>> result = et1 + et2
                >>> result
                ExtendedTimeDelta(years=1, months=6, days=15, seconds=0, microseconds=0)

        """
        if isinstance(other, ExtendedTimeDelta):
            return type(self)(
                days=self.days + other.days,
                seconds=self.seconds + other.seconds,
                microseconds=self.microseconds + other.microseconds,
                months=self.months + other.months,
                years=self.years + other.years,
                days_in_month=self.days_in_month,
                days_in_year=self.days_in_year,
            )
        if isinstance(other, timedelta):
            parent_self = self.to_timedelta()
            parent_result = parent_self + other
            return type(self).from_timedelta(
                parent_result,
                days_in_month=self.days_in_month,
                days_in_year=self.days_in_year,
            )
        return NotImplemented

    __radd__ = __add__

    def __sub__(self, other: object) -> Self | NotImplementedType:
        """Subtract an ExtendedTimeDelta or timedelta from this ExtendedTimeDelta.

        Args:
                other (ExtendedTimeDelta or timedelta): The time delta to subtract.

        Returns:
                ExtendedTimeDelta: A new ExtendedTimeDelta representing the difference.

        Example:
                >>> et1 = ExtendedTimeDelta(years=2, months=3, days=10)
                >>> et2 = ExtendedTimeDelta(years=1, months=1, days=5)
                >>> result = et1 - et2
                >>> result
                ExtendedTimeDelta(years=1, months=2, days=5, seconds=0, microseconds=0)

        """
        if isinstance(other, ExtendedTimeDelta):
            return type(self)(
                days=self.days - other.days,
                seconds=self.seconds - other.seconds,
                microseconds=self.microseconds - other.microseconds,
                months=self.months - other.months,
                years=self.years - other.years,
                days_in_month=self.days_in_month,
                days_in_year=self.days_in_year,
            )
        if isinstance(other, timedelta):
            parent_self = self.to_timedelta()
            parent_result = parent_self - other
            return type(self).from_timedelta(
                parent_result,
                days_in_month=self.days_in_month,
                days_in_year=self.days_in_year,
            )
        return NotImplemented

    def __mul__(self, other: object) -> Self | NotImplementedType:
        """Multiply this ExtendedTimeDelta by an integer.

        Args:
                other (int): The multiplier.

        Returns:
                ExtendedTimeDelta: A new ExtendedTimeDelta representing the product.

        Example:
                >>> et = ExtendedTimeDelta(years=1, days=15)
                >>> result = et * 2
                >>> result.years, result.days
                (2, 30)

        """
        if isinstance(other, (int, float)):
            return type(self)(
                days=self.days * other,
                seconds=self.seconds * other,
                microseconds=self.microseconds * other,
                months=self.months * other,
                years=self.years * other,
                days_in_month=self.days_in_month,
                days_in_year=self.days_in_year,
            )
        return NotImplemented

    __rmul__ = __mul__

    def __eq__(self, other: object) -> bool | NotImplementedType:
        """Check equality between this ExtendedTimeDelta and another.

        Args:
                other (ExtendedTimeDelta or timedelta): The time delta to compare.

        Returns:
                bool: True if both time deltas are equal, False otherwise.

        Example:
                >>> et1 = ExtendedTimeDelta(years=1, days=30)
                >>> et2 = ExtendedTimeDelta(months=14)
                >>> et1 == et2
                True

        """
        if isinstance(other, (ExtendedTimeDelta, timedelta)):
            return self._cmp(other) == 0
        return NotImplemented

    def __ne__(self, other: object) -> bool | NotImplementedType:
        """Check inequality between this ExtendedTimeDelta and another.

        Returns:
                bool: True if the durations differ, otherwise False.
        """
        result = self.__eq__(other)
        if result is NotImplemented:
            return NotImplemented
        return not result

    def __lt__(self, other: object) -> bool | NotImplementedType:
        """Check if this ExtendedTimeDelta is less than another time delta.

        Args:
                other (ExtendedTimeDelta or timedelta): The time delta to compare.

        Returns:
                bool: True if this instance is less than `other`, False otherwise.

        Example:
                >>> et1 = ExtendedTimeDelta(years=1)
                >>> et2 = ExtendedTimeDelta(years=2)
                >>> et1 < et2
                True

        """
        if isinstance(other, (ExtendedTimeDelta, timedelta)):
            return self._cmp(other) < 0
        return NotImplemented

    def __le__(self, other: object) -> bool | NotImplementedType:
        """Check if this ExtendedTimeDelta is less than or equal to another time delta.

        Args:
                other (ExtendedTimeDelta or timedelta): The time delta to compare.

        Returns:
                bool: True if this instance is less than or equal to `other`, False otherwise.

        Example:
                >>> et1 = ExtendedTimeDelta(months=3)
                >>> et2 = ExtendedTimeDelta(months=3, days=1)
                >>> et1 <= et2
                True

        """
        if isinstance(other, (ExtendedTimeDelta, timedelta)):
            return self._cmp(other) <= 0
        return NotImplemented

    def __gt__(self, other: object) -> bool | NotImplementedType:
        """Check if this ExtendedTimeDelta is greater than another time delta.

        Args:
                other (ExtendedTimeDelta or timedelta): The time delta to compare.

        Returns:
                bool: True if this instance is greater than `other`, False otherwise.

        Example:
                >>> et1 = ExtendedTimeDelta(days=10)
                >>> et2 = ExtendedTimeDelta(days=5)
                >>> et1 > et2
                True

        """
        if isinstance(other, (ExtendedTimeDelta, timedelta)):
            return self._cmp(other) > 0
        return NotImplemented

    def __ge__(self, other: object) -> bool | NotImplementedType:
        """Check if this ExtendedTimeDelta is greater than or equal to another time delta.

        Args:
                other (ExtendedTimeDelta or timedelta): The time delta to compare.

        Returns:
                bool: True if this instance is greater than or equal to `other`, False otherwise.

        Example:
                >>> et1 = ExtendedTimeDelta(days=5)
                >>> et2 = ExtendedTimeDelta(days=5)
                >>> et1 >= et2
                True

        """
        if isinstance(other, (ExtendedTimeDelta, timedelta)):
            return self._cmp(other) >= 0
        return NotImplemented

    def _cmp(self, other: timedelta) -> int:
        """Compare this ExtendedTimeDelta with another time delta.

        For ExtendedTimeDelta, the comparison first considers the years, then months,
        and finally defers to the parent timedelta's comparison for remaining components.

        Args:
                other (ExtendedTimeDelta or timedelta): The time delta to compare.

        Returns:
                int: Negative if self < other, zero if self == other, positive if self > other.

        Raises:
                TypeError: If `other` is not an ExtendedTimeDelta or timedelta.

        """
        self_timedelta = self.to_timedelta()
        if isinstance(other, ExtendedTimeDelta):
            other_timedelta = other.to_timedelta()
        elif isinstance(other, timedelta):
            other_timedelta = other
        else:
            error_message = "other must be an ExtendedTimeDelta or timedelta"
            raise TypeError(error_message)

        return (self_timedelta > other_timedelta) - (self_timedelta < other_timedelta)

    def __hash__(self) -> int:
        """Return the hash of the ExtendedTimeDelta.

        The hash is computed based on the years, months, days, seconds, and microseconds.

        Returns:
                int: The hash value.

        Example:
                >>> et = ExtendedTimeDelta(years=1, months=2)
                >>> isinstance(hash(et), int)
                True

        """
        return hash(self.to_timedelta())

    def __repr__(self) -> str:
        """Return the official string representation of the ExtendedTimeDelta.

        This representation is intended to be unambiguous and, if possible, match the
        source code necessary to recreate the object.

        Returns:
                str: The string representation.

        Example:
                >>> et = ExtendedTimeDelta(years=1, months=2, days=3)
                >>> repr(et)
                'ExtendedTimeDelta(years=1, months=2, days=3)'

        """
        args = []
        if self.years != 0:
            args.append(f"years={self.years}")
        if self.months != 0:
            args.append(f"months={self.months}")
        if self.days != 0:
            args.append(f"days={self.days}")
        if self.seconds != 0:
            args.append(f"seconds={self.seconds}")
        if self.microseconds != 0:
            args.append(f"microseconds={self.microseconds}")
        if not args:
            args.append("0")
        return f"ExtendedTimeDelta({', '.join(args)})"

    def __str__(self) -> str:
        """Return a human-readable string representation of the ExtendedTimeDelta.

        This method returns a string that includes the years, months, and the standard
        timedelta representation for days, seconds, and microseconds.

        Returns:
                str: The human-readable string.

        Example:
                >>> et = ExtendedTimeDelta(years=1, months=2)
                >>> str(et)
                '1 year, 2 months, 0:00:00'

        """
        parts = []
        if self.years != 0:
            plural = "s" if abs(self.years) != 1 else ""
            parts.append(f"{self.years} year{plural}")
        if self.months != 0:
            plural = "s" if abs(self.months) != 1 else ""
            parts.append(f"{self.months} month{plural}")
        parent_str = super().__str__()
        if parent_str:
            parts.append(parent_str)
        return ", ".join(parts)

    def __reduce__(self) -> tuple:
        """Return the information necessary to pickle the ExtendedTimeDelta.

        This method is used by the pickle module to serialize and deserialize the
        ExtendedTimeDelta instance.

        Returns:
                tuple: A tuple containing the class reference and the initialization arguments.

        """
        return (
            _reconstruct_extended_timedelta,
            (
                (
                    self.microseconds,
                    self.seconds,
                    self.days,
                    self.months,
                    self.years,
                    self.days_in_month,
                    self.days_in_year,
                ),
            ),
        )

    def to_dict(self) -> dict[str, int | float]:
        """Return a dictionary representation of the ExtendedTimeDelta.

        Returns:
                dict: A dictionary representation of the ExtendedTimeDelta.

        """
        return {
            "microseconds": self.microseconds,
            "seconds": self.seconds,
            "days": self.days,
            "months": self.months,
            "years": self.years,
        }

    def __iter__(self) -> Iterator[tuple[str, int | float]]:
        return iter(self.to_dict().items())

    @classmethod
    def from_timedelta(
        cls,
        td: timedelta,
        *,
        days_in_month: float = DAYS_IN_MONTH,
        days_in_year: float = DAYS_IN_YEAR,
    ) -> Self:
        """Create an ExtendedTimeDelta instance from a standard timedelta.

        Args:
                td (timedelta): A standard timedelta object.
                days_in_month (float, optional): Month length for the new instance.
                days_in_year (float, optional): Year length for the new instance.

        Returns:
                ExtendedTimeDelta: An instance equivalent to the provided timedelta.

        Example:
                >>> td = timedelta(days=10, seconds=3600)
                >>> et = ExtendedTimeDelta.from_timedelta(td)
                >>> et
                ExtendedTimeDelta(years=0, months=0, days=10, seconds=3600, microseconds=0)

        """
        return cls(
            days=td.days,
            seconds=td.seconds,
            microseconds=td.microseconds,
            days_in_month=days_in_month,
            days_in_year=days_in_year,
        )

    def to_timedelta(self) -> timedelta:
        """Convert the ExtendedTimeDelta instance to a standard timedelta.

        This method converts the ExtendedTimeDelta instance to a standard timedelta by
        aggregating the years, months, and days into a total number of days. The conversion
        uses the default approximations of 365 days per year and 30 days per month.

        Returns:
                timedelta: A standard timedelta object representing the equivalent duration.

        Example:
                >>> etd = ExtendedTimeDelta(years=1, months=2, days=15, seconds=30)
                >>> td = etd.to_timedelta()
                >>> td
                timedelta(days=412, seconds=30)

        """
        total_days = self.years * self.days_in_year + self.months * self.days_in_month + self.days
        return timedelta(
            days=total_days,
            seconds=self.seconds,
            microseconds=self.microseconds,
        )

    def to_microseconds(self) -> float:
        """Return the total number of microseconds contained in the ExtendedTimeDelta.

        The calculation includes years and months by converting them into days using
        the approximations (defaults to 365 days per year and 30 days per month).

        Returns:
                float: The total microseconds represented by the ExtendedTimeDelta.

        Example:
                >>> et = ExtendedTimeDelta(years=1, months=1, days=1)
                >>> et.to_microseconds()
                34214400000000.0

        """
        seconds_per_day = 24 * 60 * 60

        total_seconds = self.seconds + self.days * seconds_per_day + self.months * self.days_in_month * seconds_per_day + self.years * self.days_in_year * seconds_per_day

        return (total_seconds * 1e6) + self.microseconds

    def to_seconds(self) -> float:
        """Return the total number of seconds contained in the ExtendedTimeDelta.

        The calculation includes years and months by converting them into days using
        the approximations (defaults to 365 days per year and 30 days per month).

        Returns:
                float: The total seconds represented by the ExtendedTimeDelta.

        Example:
                >>> et = ExtendedTimeDelta(years=1, months=1, days=1)
                >>> et.to_seconds()
                        34273746.0

        """
        return self.to_microseconds() / 1e6

    def to_minutes(self) -> float:
        """Return the total number of minutes contained in the ExtendedTimeDelta.

        The calculation includes years and months by converting them into days using
        the approximations (defaults to 365 days per year and 30 days per month).

        Returns:
                float: The total minutes represented by the ExtendedTimeDelta.

        Example:
                >>> et = ExtendedTimeDelta(years=1, months=1, days=1)
                >>> et.to_minutes()
                571229.1

        """
        return self.to_seconds() / 60

    def to_hours(self) -> float:
        """Return the total number of hours contained in the ExtendedTimeDelta.

        The calculation includes years and months by converting them into days using
        the approximations (defaults to 365 days per year and 30 days per month).

        Returns:
                float: The total hours represented by the ExtendedTimeDelta.

        Example:
                >>> et = ExtendedTimeDelta(years=1, months=1, days=1)
                >>> et.to_hours()
                9520.484999999999

        """
        return self.to_minutes() / 60

    def to_days(self) -> float:
        """Return the total number of days contained in the ExtendedTimeDelta.

        The calculation includes years and months by converting them into days using
        the approximations (defaults 365 days per year and 30 days per month).

        Returns:
                float: The total days represented by the ExtendedTimeDelta.

        Example:
                >>> et = ExtendedTimeDelta(years=1, months=1, days=1)
                >>> et.to_days()
                396.68687499999993

        """
        return self.to_hours() / 24

    def to_weeks(self) -> float:
        """Return the total number of weeks contained in the ExtendedTimeDelta.

        The calculation includes years and months by converting them into days using
        the approximations (defaults 365 days per year and 30 days per month).

        Returns:
                float: The total weeks represented by the ExtendedTimeDelta.

        Example:
                >>> et = ExtendedTimeDelta(years=1, months=1, days=1)
                >>> et.to_weeks()
                56.66955357142856

        """
        return self.to_days() / 7

    def to_months(self) -> float:
        """Return the total number of months contained in the ExtendedTimeDelta.

        The calculation includes years and months by converting them into days using
        the approximations (defaults to 365 days per year and 30 days per month).

        Returns:
                float: The total months represented by the ExtendedTimeDelta.

        Example:
                >>> et = ExtendedTimeDelta(years=1, months=1, days=1)
                >>> et.to_months()
                13.0

        """
        return (self.years * 12) + self.months

    def to_years(self) -> float:
        """Return the total number of years contained in the ExtendedTimeDelta.

        The calculation includes years and months by converting them into days using
        the approximations (defaults to 365 days per year and 30 days per month).

        Returns:
                float: The total years represented by the ExtendedTimeDelta.

        Example:
                >>> et = ExtendedTimeDelta(years=1, months=1, days=1)
                >>> et.to_years()
                1.0833333333333333

        """
        return self.to_months() / 12
