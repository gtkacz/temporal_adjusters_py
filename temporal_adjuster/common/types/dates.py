from datetime import date, datetime, time
from typing import TypeVar, Union

from temporal_adjuster.common.types.__extended_timedelta import ExtendedTimeDelta

AnyDate = Union[datetime, date]
DateT = TypeVar('DateT', bound=AnyDate)

AnyTime = Union[datetime, time]
TimeT = TypeVar('TimeT', bound=AnyTime)
