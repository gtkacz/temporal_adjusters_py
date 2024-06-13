# Temporal Adjusters

Common and useful Temporal Adjusters.
Adjusters are a key tool for modifying temporal objects. They exist to externalize the process of adjustment, permitting different approaches, as per the strategy design pattern. Examples might be an adjuster that sets the date avoiding weekends, or one that sets the date to the last day of the month.

[![codecov](https://codecov.io/gh/gtkacz/temporal_adjusters_py-python/branch/main/graph/badge.svg?token=5KNECS8JYF)](https://codecov.io/gh/gtkacz/temporal_adjusters_py-python)
[![Downloads per Month](https://shields.io/pypi/dm/temporal_adjusters_py)](https://pypistats.org/packages/temporal_adjusters_py)
[![Package version](https://shields.io/pypi/v/temporal_adjusters_py)](https://pypi.org/project/temporal_adjusters_py/)

## Installation

You can install Temporal Adjusters using pip:

```sh
pip install temporal_adjusters
```

## Usage

Temporal Adjusters provides a context manager that allows you to use the loading animation as a context manager. This can be useful if you want to ensure that the loading animation is automatically stopped when an error occurs or when your code finishes executing. For example:

```py
>>> from datetime import date

>>> from temporal_adjusters import TemporalAdjuster
>>> from temporal_adjusters.common.enums import Weekday

>>> test_date = date(2024, 5, 1)

>>> TemporalAdjuster.next(Weekday.MONDAY, test_date)
datetime.date(2024, 5, 6)

>>> TemporalAdjuster.last_day_of_next_month(test_date)
datetime.date(2024, 6, 30)

```

## Contributing

If you have any suggestions or improvements for pynimbar, feel free to submit a pull request or open an issue on the [GitHub repository](https://github.com/gtkacz/pynimbar). We appreciate any feedback or contributions!
