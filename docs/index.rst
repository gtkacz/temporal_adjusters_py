.. Temporal Adjuster documentation master file, created by
   sphinx-quickstart on Mon Jun 17 20:44:21 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Temporal Adjuster's documentation!
=============================================

Temporal Adjuster provides tools that help pinpoint very specific moments in time, without having to manually count days, weeks, or months.
In essence, a Temporal Adjuster is a function that encapsulates a specific date/time manipulation rule. It operates on a temporal
object (representing a date, time, or datetime) to produce a new temporal object adjusted according to the rule.

.. toctree::
   :maxdepth: 3
   :caption: Contents:

   ta


Quick Examples
--------------

.. code-block:: python

   from datetime import date, datetime

   from temporal_adjuster import TemporalAdjuster
   from temporal_adjuster.common.enums import Weekday

   # Get the first day of next week
   TemporalAdjuster.first_day_of_next_week(date(2021, 1, 1))
   # datetime.date(2021, 1, 4)

   # Get the last day of the previous month
   TemporalAdjuster.last_day_of_last_month(datetime(2021, 1, 1))
   # datetime.datetime(2020, 12, 31)

   # Get the first Saturday of the year
   TemporalAdjuster.first_of_year(Weekday.SATURDAY, date(2021, 1, 1))
   # datetime.date(2021, 1, 2)

   # Get the second Sunday of the month
   TemporalAdjuster.nth_of_month(Weekday.SUNDAY, datetime(2021, 5, 1), 2)
   # datetime.datetime(2021, 5, 9)


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
