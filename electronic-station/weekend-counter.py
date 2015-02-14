import datetime as dt
from datetime import date

def checkio(day_start, day_end):
  counter = 1 if day_start.weekday() in (5,6) else 0
  
  while day_start < day_end:
    
    day_start = day_start + dt.timedelta(1)
    
    if day_start.weekday() in (5,6):
      counter += 1
  
  return counter

print checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2
print checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8
print checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2
