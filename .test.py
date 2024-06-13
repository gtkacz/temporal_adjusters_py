from temporal_adjusters.src.main import TemporalAdjuster
from datetime import datetime, date
from temporal_adjusters.src.util.enums import DayOfWeek

dt = date.today()

# print(TemporalAdjuster.first_day_of_month(dt))
print(TemporalAdjuster.first_in_next_month(DayOfWeek.FRIDAY, dt))