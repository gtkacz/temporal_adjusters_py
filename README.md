# Temporal Adjuster

Adjusters are a key tool for modifying temporal objects. They exist to externalize the process of adjustment, permitting different approaches, as per the strategy design pattern. Temporal Adjuster provides tools that help pinpoint very specific moments in time, without having to manually count days, weeks, or months. In essence, a Temporal Adjuster is a function that encapsulates a specific date/time manipulation rule. It operates on a temporal object (representing a date, time, or datetime) to produce a new temporal object adjusted according to the rule. Examples might be an adjuster that sets the date avoiding weekends, or one that sets the date to the last day of the month.

[![codecov](https://codecov.io/gh/gtkacz/temporal_adjuster_py-python/branch/main/graph/badge.svg?token=5KNECS8JYF)](https://codecov.io/gh/gtkacz/temporal_adjuster_py-python)
[![Downloads per Month](https://shields.io/pypi/dm/temporal_adjuster)](https://pypistats.org/packages/temporal_adjuster)
[![Package version](https://shields.io/pypi/v/temporal_adjuster)](https://pypi.org/project/temporal_adjuster/)

## Installation

You can install Temporal Adjuster using pip:

```sh
pip install temporal-adjuster
```

## Usage

This package provides a set of predefined temporal adjusters that can be used to adjust a temporal object in various ways. For example:

```py
>>> from datetime import date, datetime

>>> from temporal_adjuster import TemporalAdjuster
>>> from temporal_adjuster.common.enums import Weekday

>>> TemporalAdjuster.first_day_of_next_week(date(2021, 1, 1))
datetime.date(2021, 1, 4)

>>> TemporalAdjuster.last_day_of_last_month(datetime(2021, 1, 1))
datetime.datetime(2020, 12, 31)

>>> TemporalAdjuster.first_of_year(Weekday.SATURDAY, date(2021, 1, 1))
datetime.date(2021, 1, 2)

>>> TemporalAdjuster.nth_of_month(Weekday.SUNDAY, datetime(2021, 5, 1), 2)
datetime.datetime(2021, 5, 9)

>>> TemporalAdjuster.next(Weekday.MONDAY, datetime(2021, 2, 11), 2)
datetime.datetime(2021, 2, 15)
```

## Contributing

If you have any suggestions or improvements for pynimbar, feel free to submit a pull request or open an issue on the [GitHub repository](https://github.com/gtkacz/temporal_adjusters_py) as per the CONTRIBUTING document. We appreciate any feedback or contributions!
