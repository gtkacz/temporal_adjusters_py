# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [2.0.0] - 2026-08-05

### Removed

- **Breaking:** Sequence inputs are no longer supported. The `sequenceable` decorator ran `inspect.signature` on every call (19x slower than a list comprehension), silently replaced pandas `Series` indexes with a `RangeIndex`, and failed on `dict` inputs. Apply adjusters to collections explicitly instead: `[TemporalAdjuster.next(Weekday.MONDAY, d) for d in dates]`.
- **Breaking:** Dropped the `numpy` and `python-dateutil` runtime dependencies. The package now has zero runtime dependencies.

### Changed

- **Breaking:** `time_difference` returns a plain `datetime.timedelta` instead of `ExtendedTimeDelta`.
- **Breaking:** `nth_from_date` raises `ValueError` for `n < 1` instead of silently returning past dates.
- **Breaking:** `nth_of_year` rejects `n = 54`; the valid range is 1-53, the maximum number of weekday occurrences in a year.
- All date arithmetic now uses the standard library (`timedelta`, `date.replace`, `calendar.monthrange`); scalar adjusters run 17-36x faster.

### Deprecated

- `ExtendedTimeDelta` now emits a `DeprecationWarning`: date arithmetic silently ignores its month and year components because they are not part of `timedelta`'s C-level state. Use `datetime.timedelta` for exact durations or `dateutil.relativedelta` for calendar-aware arithmetic.

### Added

- `previous` and `previous_or_same` aliases for `last` and `last_or_same`, matching Java's `TemporalAdjusters.previous`/`previousOrSame` naming.
- `nth_of_month` accepts negative `n`, counting backward from the end of the month (`-1` is the last occurrence), matching Java's `TemporalAdjusters.dayOfWeekInMonth`.
- Working-day adjusters with a configurable weekend: `next_working_day`, `next_working_day_or_same`, `previous_working_day`, and `previous_working_day_or_same`.
- Quarter operations: `first_day_of_quarter` and `last_day_of_quarter` with `next`/`last` variants, plus `first_of_quarter` and `last_of_quarter` weekday adjusters.

### Fixed

- `round_time` preserves `tzinfo` on timezone-aware inputs instead of returning naive objects.
- The README quick-start example called `next` with an argument it does not accept; docstring examples across the facade and `ExtendedTimeDelta` now show the values the code actually produces.

## [1.3.0] - 2024-XX-XX

### Added

- New `day_of_year` method, that returns an integer ranging from 1-365 (or 366 for leap years) corresponding to the day of the year.
- New `which_of_month` and `which_of_year` weekday methods, that return an integer representing which occurrence of a weekday in a month or year a given date falls on. For example, `which_of_month` will return 1 for the first Monday of the month, 2 for the second Monday, and so on. Similarly, `which_of_year` will return 1 for the first Monday of the year, 2 for the second Monday, and so on.
- Altered sequence processing to make use of numpy vectorization.

## [1.2.0] - 2024-06-20

### Added

- Altered sequence processing to make use of numpy vectorization.

## [1.1.1] - 2024-06-17

### Fixed

- Added support for older Python versions that were failing because of Ubuntu version on CI runner.

## [1.1.0] - 2024-06-17

### Added

- Added support for `ISOWeekday`, meaning the int value of the weekdays follow the ISO-8601 standard: from 1 (Monday) to 7 (Sunday), to all weekday-based operations. You can also pass `int` or `str` objects corresponding to Pythonic weekdays.
- Added support for calling any method on sequences. Instead of passing a single temporal-like, you can pass any sequence of temporal-likes (for instance `list`, `np.ndarray`, `pd.Series`, etc.) and get back the same sequence with all temporal objects adjusted.
