from ..common.decorators import sequenceable
from ..common.types import AnyDate


class _MiscellaneousAdjuster:
	@staticmethod
	@sequenceable(target='date')
	def day_of_year(dt: AnyDate) -> int:
		"""
		Returns the day of the year of the given date.

		Args:
		    dt (DateT): The date to adjust.

		Returns:
		    int: The day of the year of the given date.
		"""
		return dt.timetuple().tm_yday
