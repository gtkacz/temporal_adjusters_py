from datetime import date, datetime
from typing import TypeVar

AnyDate = datetime | date
DateT = TypeVar('DateT', bound=AnyDate)
