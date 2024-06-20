# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

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
