from dateutil.relativedelta import relativedelta

from ..common.decorators import sequenceable
from ..common.types.dates import DateT


class _AbsoluteDateOperations:
	@staticmethod
	@sequenceable(target='date')
	def int_to_day_of_year(date: DateT, int_value: int) -> DateT:
		"""
		Returns the date of the given day of the year.

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
		return date.replace(month=1, day=1) + relativedelta(days=int_value - 1)

	@staticmethod
	@sequenceable(target='date')
	def int_to_day_of_month(date: DateT, int_value: int) -> DateT:
		"""
		Returns the date of the given day of the month.

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
		return date.replace(day=1) + relativedelta(days=int_value - 1)

	@staticmethod
	@sequenceable(target='date')
	def date_to_int_of_year(date: DateT) -> int:
		"""
		Returns the integer value for the given day of the year of the given date.

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
	@sequenceable(target='date')
	def date_to_int_of_month(date: DateT) -> int:
		"""
		Returns the integer value for the given day of the month of the given date.

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
