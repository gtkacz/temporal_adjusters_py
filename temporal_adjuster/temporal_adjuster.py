from .modules import _TemporalAdjusterForFirstAndLastDays, _TemporalAdjusterForWeekday


class TemporalAdjuster(
    _TemporalAdjusterForFirstAndLastDays, _TemporalAdjusterForWeekday
):
    """
    This class provides tools that help pinpoint very specific moments in time, without having to manually count days, weeks, or months. In essence, a Temporal Adjuster is a function that encapsulates a specific date/time manipulation rule. It operates on a temporal object (representing a date, time, or datetime) to produce a new temporal object adjusted according to the rule. This class provides a set of predefined temporal adjusters that can be used to adjust a temporal object in various ways.

    Examples:

    ```
    >>> from datetime import date, datetime

    >>> from temporal_adjuster import TemporalAdjuster
    >>> from temporal_adjuster.common.enums import Weekday

    >>> TemporalAdjuster.first_day_of_next_week(date(2021, 1, 1))
    datetime.date(2021, 1, 4)

    >>> TemporalAdjuster.last_day_of_last_week(date(2021, 1, 1))
    datetime.date(2020, 12, 27)

    >>> TemporalAdjuster.first_of_month(Weekday.SATURDAY, date(2021, 1, 1))
    datetime.date(2021, 2, 6)

    >>> TemporalAdjuster.nth_of_month(Weekday.SUNDAY, date(2021, 5, 1), 2)
    datetime.date(2021, 5, 9)

    ```
    """

    pass
