"""Date type definitions for the temporal adjuster package."""

from datetime import date, datetime, time
from typing import TypeVar, Union

#: Type alias for any date-like object (datetime or date)
AnyDate = Union[datetime, date]

#: TypeVar bound to date-like objects
DateT = TypeVar('DateT', bound=AnyDate)

#: Type alias for any time-like object (datetime or time)
AnyTime = Union[datetime, time]

#: TypeVar bound to time-like objects
TimeT = TypeVar('TimeT', bound=AnyTime)
