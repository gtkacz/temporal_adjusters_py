from datetime import date, datetime, time
from typing import TypeVar, Union

AnyDate = Union[datetime, date]
DateT = TypeVar('DateT', bound=AnyDate)

AnyTime = Union[datetime, time]
TimeT = TypeVar('TimeT', bound=AnyTime)
