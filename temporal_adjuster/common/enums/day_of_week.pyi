from enum import IntEnum

class Weekday(IntEnum):
	"""
	A day-of-week, such as 'Tuesday'.
	Weekday is an enum representing the 7 days of the week - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday and Sunday.

	In addition to the textual enum name, each day-of-week has an int value. The int value follows the Python datetime standard, from 0 (Monday) to 6 (Sunday).
	"""

	MONDAY: int
	TUESDAY: int
	WEDNESDAY: int
	THURSDAY: int
	FRIDAY: int
	SATURDAY: int
	SUNDAY: int

class ISOWeekday(IntEnum):
	"""
	A day-of-week, such as 'Tuesday'.
	Weekday is an enum representing the 7 days of the week - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday and Sunday.

	In addition to the textual enum name, each day-of-week has an int value. The int value follows the ISO-8601 standard, from 1 (Monday) to 7 (Sunday).
	"""

	MONDAY: int
	TUESDAY: int
	WEDNESDAY: int
	THURSDAY: int
	FRIDAY: int
	SATURDAY: int
	SUNDAY: int
