from enum import Enum


class DayOfWeek(Enum):
    """
    A day-of-week, such as 'Tuesday'.
    DayOfWeek is an enum representing the 7 days of the week - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday and Sunday.

    In addition to the textual enum name, each day-of-week has an int value. The int value follows the Python datetime standard, from 0 (Monday) to 6 (Sunday).
    """
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6
