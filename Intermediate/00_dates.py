# Dates

from datetime import datetime

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.weekday())
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

now = datetime.now()

print_date(now)

# Formatting Date Output

year_2026 = datetime(2026, 1, 1)

print_date(year_2026)

# Time Objects to Represent Time
# time() is an empty object by default

from datetime import time

current_time = time()

print(current_time.hour) # 0
print(current_time.minute) # 0
print(current_time.second) # 0
print(current_time) # 00:00:00

current_time = time(21, 6, 50)

print(current_time.hour) # 21
print(current_time.minute) # 6
print(current_time.second) # 50
print(current_time) # 21:06:50

# Using date from datetime
# date() needs at least three arguments (year, month, day) or use a method

from datetime import date

current_date = date(2024, 4, 20)

print(current_date.year) # 2024
print(current_date.month) # 4
print(current_date.day) # 20
print(current_date) # 2024-04-20

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)
print(current_date) # 2025-01-14

# Operations with dates (modify dates)

current_date = date(current_date.year, current_date.month + 1, current_date.day)
print(current_date) # 2025-02-14

# Difference of two dates
# they have to be the same type of date (datetime, date, time, etc)

today = date.today()
new_year = date(year=2026, month=1, day=1)
difference = new_year - today
print(difference) # 352 days, 0:00:00
difference = year_2026 - now
print(difference) # 351 days, 10:18:28.463146

# Use of timedelta()

from datetime import timedelta

start_time = timedelta(200, 100, 100, weeks=10)
end_time = timedelta(300, 100, 100, weeks=13)
print(end_time - start_time) # 121 days, 0:00:00
print(end_time + start_time) # 661 days, 0:03:20.000200
print(end_time / start_time) # 1.4481462270804388