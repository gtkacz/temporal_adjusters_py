from datetime import date, datetime
from typing import TypeVar, Union

AnyDate = Union[datetime, date]
DateT = TypeVar('DateT', bound=AnyDate)
