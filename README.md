<center>

# Temporal Adjuster

<p align="center">

Adjusters are a key tool for modifying temporal objects. They exist to externalize the process of adjustment, permitting different approaches, as per the strategy design pattern. Temporal Adjuster provides tools that help pinpoint very specific moments in time, without having to manually count days, weeks, or months. In essence, a Temporal Adjuster is a function that encapsulates a specific date/time manipulation rule. It operates on a temporal object (representing a date, time, or datetime) to produce a new temporal object adjusted according to the rule. Examples might be an adjuster that sets the date avoiding weekends, or one that sets the date to the last day of the month.

</p>

[![PyPI status](https://img.shields.io/pypi/status/temporal-adjuster.svg)](https://pypi.python.org/pypi/temporal-adjuster/)
[![Package Version](https://shields.io/pypi/v/temporal_adjuster)](https://pypi.org/project/temporal_adjuster/)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/temporal-adjuster)](https://pypi.org/project/temporal-adjuster/)
[![Downloads Per Month](https://shields.io/pypi/dm/temporal_adjuster)](https://pypistats.org/packages/temporal_adjuster)
![Libraries.io dependency status for Github repo](https://img.shields.io/librariesio/github/gtkacz/temporal_adjusters_py)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

[![CI](https://github.com/gtkacz/temporal_adjusters_py/actions/workflows/CI.yml/badge.svg?branch=main)](https://github.com/gtkacz/temporal_adjusters_py/actions/workflows/CI.yml)
[![codecov](https://codecov.io/gh/gtkacz/temporal_adjuster_py-python/branch/main/graph/badge.svg?token=5KNECS8JYF)](https://codecov.io/gh/gtkacz/temporal_adjuster_py-python)
[![Documentation Status](https://readthedocs.org/projects/temporal-adjuster/badge/?version=latest)](http://temporal-adjuster.readthedocs.io/?badge=latest)
[![Github commits](https://badgen.net/github/commits/gtkacz/temporal_adjusters_py)](https://Github.com/gtkacz/temporal_adjusters_py/commit/)
[![Github latest commit](https://badgen.net/github/last-commit/gtkacz/temporal_adjusters_py)](https://Github.com/gtkacz/temporal_adjusters_py/commit/)
![Github code size in bytes](https://img.shields.io/github/languages/code-size/gtkacz/temporal_adjusters_py)
![Github repo file or directory count](https://img.shields.io/github/directory-file-count/gtkacz/temporal_adjusters_py)

[![Github stars](https://badgen.net/github/stars/gtkacz/temporal_adjusters_py)](https://Github.com/gtkacz/temporal_adjusters_py/stargazers/)
[![Github watchers](https://badgen.net/github/watchers/gtkacz/temporal_adjusters_py/)](https://Github.com/gtkacz/temporal_adjusters_py/watchers/)
[![Github issues](https://img.shields.io/github/issues/gtkacz/temporal_adjusters_py.svg)](https://Github.com/gtkacz/temporal_adjusters_py/issues/)
[![Github issues-closed](https://img.shields.io/github/issues-closed/gtkacz/temporal_adjusters_py.svg)](https://Github.com/gtkacz/temporal_adjusters_py/issues?q=is%3Aissue+is%3Aclosed)
[![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/gtkacz/temporal_adjusters_py.svg)](http://isitmaintained.com/project/gtkacz/temporal_adjusters_py "Average time to resolve an issue")
[![Percentage of issues still open](http://isitmaintained.com/badge/open/gtkacz/temporal_adjusters_py.svg)](http://isitmaintained.com/project/gtkacz/temporal_adjusters_py "Percentage of issues still open")
[![Github pull-requests](https://img.shields.io/github/issues-pr/gtkacz/temporal_adjusters_py.svg)](https://Github.com/gtkacz/temporal_adjusters_py/pull/)
<!-- [![Github contributors](https://img.shields.io/github/contributors/gtkacz/temporal_adjusters_py/badges.svg)](https://Github.com/gtkacz/temporal_adjusters_py/badges/graphs/contributors/) -->

</center>

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

If you have any suggestions or improvements for this package, feel free to submit a pull request or open an issue on the [GitHub repository](https://github.com/gtkacz/temporal_adjusters_py) as per the CONTRIBUTING document. We appreciate any feedback or contributions!


<!-- [![Stargazers over time](https://starchart.cc/gtkacz/temporal_adjusters_py.svg)](https://starchart.cc/gtkacz/temporal_adjusters_py)
[![Contributors over time](https://contributor-graph-api.apiseven.com/contributors-svg?chart=contributorOverTime&repo=gtkacz/temporal_adjusters_py)](https://www.apiseven.com/en/contributor-graph?chart=contributorOverTime&repo=gtkacz/temporal_adjusters_py) -->
