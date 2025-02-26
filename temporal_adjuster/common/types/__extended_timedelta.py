import math
from datetime import timedelta
from typing import Union


class ExtendedTimeDelta(timedelta):
	"""An extended version of Python's timedelta that supports months and years.

	This class extends the standard timedelta by adding support for months and years.
	Since timedelta does not natively support months and years, the conversion assumes
	fixed lengths: 30 days per month and 365 days per year. Note that these conversions
	are approximations and may not be suitable for all use cases.
	"""

	__slots__ = (
		'_months',
		'_years',
		'_days',
		'_seconds',
		'_microseconds',
		'_hashcode',
	)

	def __new__(
		cls,
		microseconds: Union[int, float] = 0,
		milliseconds: Union[int, float] = 0,
		seconds: Union[int, float] = 0,
		minutes: Union[int, float] = 0,
		hours: Union[int, float] = 0,
		days: Union[int, float] = 0,
		weeks: Union[int, float] = 0,
		months: Union[int, float] = 0,
		years: Union[int, float] = 0,
		*,
		days_in_month: Union[int, float] = 30.436875,
		days_in_year: Union[int, float] = 365.25,
	) -> 'ExtendedTimeDelta':
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

		Returns:
			ExtendedTimeDelta: A new instance of ExtendedTimeDelta.

		Example:
			>>> et = ExtendedTimeDelta(days=45, months=1)
			>>> print(et)
			1 month, 15 days, 0:00:00
		"""
		cls.DAYS_IN_MONTH = days_in_month
		cls.DAYS_IN_YEAR = days_in_year

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

		extra_days = days % cls.DAYS_IN_MONTH
		months += days // cls.DAYS_IN_MONTH
		days = extra_days

		# Process months
		if isinstance(months, float):
			m_frac, m_whole = math.modf(months)
			months = int(m_whole)
			days += m_frac * cls.DAYS_IN_MONTH
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

		return self

	@property
	def months(self) -> int:
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

	def __add__(self, other) -> 'ExtendedTimeDelta':
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
			return ExtendedTimeDelta(
				days=self.days + other.days,
				seconds=self.seconds + other.seconds,
				microseconds=self.microseconds + other.microseconds,
				months=self.months + other.months,
				years=self.years + other.years,
			)
		elif isinstance(other, timedelta):
			parent_self = self.to_timedelta()
			parent_result = parent_self + other
			return ExtendedTimeDelta.from_timedelta(parent_result)

	__radd__ = __add__

	def __sub__(self, other) -> 'ExtendedTimeDelta':
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
			return ExtendedTimeDelta(
				days=self.days - other.days,
				seconds=self.seconds - other.seconds,
				microseconds=self.microseconds - other.microseconds,
				months=self.months - other.months,
				years=self.years - other.years,
			)
		elif isinstance(other, timedelta):
			parent_self = self.to_timedelta()
			parent_result = parent_self - other
			return ExtendedTimeDelta.from_timedelta(parent_result)

	def __mul__(self, other) -> 'ExtendedTimeDelta':
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
		if isinstance(other, int) or isinstance(other, float):
			return ExtendedTimeDelta(
				days=self.days * other,
				seconds=self.seconds * other,
				microseconds=self.microseconds * other,
				months=self.months * other,
				years=self.years * other,
			)

	def __eq__(self, other) -> bool:
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
		if isinstance(other, ExtendedTimeDelta):
			return (
				self.years == other.years
				and self.months == other.months
				and self.days == other.days
				and self.seconds == other.seconds
				and self.microseconds == other.microseconds
			)
		elif isinstance(other, timedelta):
			parent_self = self.to_timedelta()
			return parent_self == other

	def __lt__(self, other) -> bool:
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

	def __le__(self, other) -> bool:
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

	def __gt__(self, other) -> bool:
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

	def __ge__(self, other) -> bool:
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

	def _cmp(self, other) -> int:
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
		if isinstance(other, ExtendedTimeDelta):
			return self.to_microseconds() - other.to_microseconds()
		elif isinstance(other, timedelta):
			return self.to_timedelta() - other

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
		return hash(
			(self.years, self.months, self.days, self.seconds, self.microseconds)
		)

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
			args.append(f'years={self.years}')
		if self.months != 0:
			args.append(f'months={self.months}')
		if self.days != 0:
			args.append(f'days={self.days}')
		if self.seconds != 0:
			args.append(f'seconds={self.seconds}')
		if self.microseconds != 0:
			args.append(f'microseconds={self.microseconds}')
		if not args:
			args.append('0')
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
			plural = 's' if abs(self.years) != 1 else ''
			parts.append(f'{self.years} year{plural}')
		if self.months != 0:
			plural = 's' if abs(self.months) != 1 else ''
			parts.append(f'{self.months} month{plural}')
		parent_str = super().__str__()
		if parent_str:
			parts.append(parent_str)
		return ', '.join(parts)

	def __reduce__(self) -> tuple:
		"""Return the information necessary to pickle the ExtendedTimeDelta.

		This method is used by the pickle module to serialize and deserialize the
		ExtendedTimeDelta instance.

		Returns:
			tuple: A tuple containing the class reference and the initialization arguments.
		"""
		return (
			self.__class__,
			(
				self.microseconds,
				0,  # milliseconds not stored separately
				self.seconds,
				0,  # minutes not stored separately
				0,  # hours not stored separately
				self.days,
				0,  # weeks not stored separately
				self.months,
				self.years,
			),
		)

	def __dict__(self) -> dict:
		"""Return a dictionary representation of the ExtendedTimeDelta.

		Returns:
			dict: A dictionary representation of the ExtendedTimeDelta.
		"""
		return {
			'microseconds': self.microseconds,
			'seconds': self.seconds,
			'days': self.days,
			'months': self.months,
			'years': self.years,
		}

	def __iter__(self) -> iter:
		return iter(self.__dict__().items())

	@classmethod
	def from_timedelta(cls, td) -> 'ExtendedTimeDelta':
		"""Create an ExtendedTimeDelta instance from a standard timedelta.

		Args:
			td (timedelta): A standard timedelta object.

		Returns:
			ExtendedTimeDelta: An instance equivalent to the provided timedelta.

		Example:
			>>> td = timedelta(days=10, seconds=3600)
			>>> et = ExtendedTimeDelta.from_timedelta(td)
			>>> et
			ExtendedTimeDelta(years=0, months=0, days=10, seconds=3600, microseconds=0)
		"""
		return cls(days=td.days, seconds=td.seconds, microseconds=td.microseconds)

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
		total_days = (
			self.years * self.DAYS_IN_YEAR
			+ self.months * self.DAYS_IN_MONTH
			+ self.days
		)
		return timedelta(
			days=total_days, seconds=self.seconds, microseconds=self.microseconds
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
		SECONDS_PER_DAY = 24 * 60 * 60

		total_seconds = (
			self.seconds
			+ self.days * SECONDS_PER_DAY
			+ self.months * self.DAYS_IN_MONTH * SECONDS_PER_DAY
			+ self.years * self.DAYS_IN_YEAR * SECONDS_PER_DAY
		)

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
