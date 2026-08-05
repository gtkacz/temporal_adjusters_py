# Copyright (c) 2024 Gabriel Mitelman Tkacz
"""Date type definitions for the temporal adjuster package."""

from datetime import date, datetime, time
from typing import TypeVar

#: Type alias for any date-like object (datetime or date)
AnyDate = datetime | date

#: TypeVar constrained to date-like types. Constrained rather than bound so
#: type checkers resolve arithmetic and replace() per concrete type instead of
#: collapsing the result to the date base class.
DateT = TypeVar("DateT", date, datetime)

#: Type alias for any time-like object (datetime or time)
AnyTime = datetime | time

#: TypeVar bound to time-like objects
TimeT = TypeVar("TimeT", bound=AnyTime)
